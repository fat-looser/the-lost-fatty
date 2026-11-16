#!/usr/bin/env python3
"""中文健康信息链路腐烂实测 — 可复现探测脚本（claim-0063）

用法：
    python3 evidence/scripts/linkrot_probe.py            # 探测并打印表格
    python3 evidence/scripts/linkrot_probe.py --json out.json

判定口径（全部显式，不靠印象）：
  - gone        : HTTP 404 / 410 —— **服务端明确说「没有这个东西」**
  - blocked     : HTTP 403 / 412 / 451 —— **服务端拒绝本客户端；不能推断内容是否存在**
  - unreachable : http=0 且**连续 3 次**传输层失败 —— **只能说本机本时段不可达**
  - soft404     : HTTP 200，但正文命中缺失标记，或最终 URL 落在 404 页
  - js_shell    : HTTP 200，HTML 很大但可提取正文极短（< 200 字）
  - ai_flagged  : HTML 含 ai_detect / "内容由AI生成" 等标记（⚠️ 只表示**字段存在**，不表示内容判定，见 claim-0030）
  - ok          : HTTP 200 且正文 >= 200 字且无上述标记

🚨 **v2 口径修正（2026-11-13）**：v1 把 404 / 403 / 412 / 传输失败**一律记为 `dead`**。
   这是本脚本自己的口径缺陷：**「内容已删除」与「本客户端被拒绝」是两件不同的事**，
   前者是关于世界的断言，后者只是关于本次测量的断言。混为一谈会制造本书正在批评的那种失真。
   v1 的原始判决保留在 JSON 的 `verdict` 字段，v2 判决另存 `verdict_v2`，**不静默改写历史测量**。

⚠️ **传输层失败必须重试，否则会把一次 SSL 抖动当成「原始出处已死」。**
   实测教训：深圳市南山区司法局转载件首轮报 `SSL: BAD_ECPOINT` 被判 dead，
   改用 curl 连探 3 次全部 HTTP 200 / 87,054 字节 —— **它活得好好的**。
   ⚠️ 关于「与存档一致」的精确说法（v2 更正，原文曾据字节数断言"一致"，属过度声称）：
     · 字节数三次测量均为 87,054 —— **相同**
     · 原始 HTML 的 MD5 三次各不相同（3849196a… / 4d6b5676… / cc365c4e…）—— **不同**
       差异仅在一段等长的会话 token 与一个时间戳（`14…8` → `22…5`）
     · **去标签后的正文 5,146 字，逐字全等** —— 这才是可声称的"一致"
   🔑 **原始 HTML 的 MD5 不是页面身份的稳定指纹；存档完整性须比对提取后的正文。**
   故 http=0 一律重试至 3 次，全败才记 unreachable，并保留每次错误类型。
   HTTP 状态码（404/403/412）是服务端明确应答，不重试。

⚠️ **urllib 在 HTTPError 分支不读响应体，故 `bytes=0` 不代表「响应为空」，只代表「未读体」。**
   实测：gov.cn 404 页 urllib 记 0 字节，curl 记 15,556 字节 / 493 字（那是 404 错误页本身）。
   凡跨客户端比较字节数，必须先确认两侧都读了体。

正文提取：去 script/style → 去标签 → HTML 实体解码 → 去全部空白。
⚠️ 本脚本只发普通 GET，不绕过任何验证码、不轮换代理、不伪造 referer 链。
   403/412 一律如实记录为「不可达」，不做重试规避。
"""
import json
import re
import html
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

# (类别, URL, 建卡时记录的状态, 来源卡)
TARGETS = [
    ("政府原始发布", "https://www.gov.cn/xinwen/2020-12/24/content_5572983.htm", "404", "0053"),
    ("政府原始发布", "https://www.nhc.gov.cn/", "412", "0039"),
    ("政府原始发布", "https://www.nmpa.gov.cn/", "412", "0039"),
    ("科普视频原始出处", "https://tv.sohu.com/v/dXMvMzM4OTE2MjEyLzY4Mjc5ODk2OS5zaHRtbA==.html?channeled=2001040002&vid=682798969", "软404", "0030"),
    ("平台404页(对照)", "https://tv.sohu.com/404/index.shtml", "—", "0030"),
    ("UGC 专栏", "https://zhuanlan.zhihu.com/p/617620296", "403", "0030"),
    ("UGC 问答", "https://zhidao.baidu.com/question/1744260259829506107.html", "ai_detect", "0030"),
    ("聚合资讯", "https://m.toutiao.com/article/7500905160182219318/", "200 但 JS 壳", "0030"),
    ("存档服务", "https://archive.org/", "curl 000 不可达", "SOURCES"),
    ("对照:开放全文", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7617101/", "—", "0053"),
    ("对照:司法原始页", "https://www.court.gov.cn/zixun/xiangqing/459321.html", "—", "0005"),
    ("对照:政府转载件", "https://www.szns.gov.cn/nsqsfj/gkmlpt/content/12/12088/post_12088095.html", "—", "0005"),
]

MISSING = ["页面不存在", "内容不存在", "你访问的页面", "您访问的页面", "已删除", "内容已删除",
           "404", "页面找不到了", "抱歉，你访问的页面", "文章不存在", "视频不存在", "已被删除"]
AI_MARK = ["ai_detect", "内容由AI生成", "内容由 AI 生成", "AI生成", "人工智能生成"]


def extract(raw: str) -> str:
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", raw, flags=re.S | re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    return re.sub(r"\s+", "", html.unescape(t))


def verdict_v2(http, marks, text_chars):
    """v2 口径：把「内容没了」「客户端被拒」「本机不可达」分开。"""
    if http == 0:
        return "unreachable"
    if http in (404, 410):
        return "gone"
    if http in (403, 412, 451):
        return "blocked"
    if http is not None and http >= 400:
        return "blocked"
    if marks and any(m.startswith(("missing:", "final_url")) for m in marks):
        return "soft404"
    if text_chars < 200:
        return "js_shell"
    if marks:
        return "ai_flagged"
    return "ok"


def probe(url: str, timeout: int = 30, attempts: int = 3):
    rec = {"url": url, "http": None, "bytes": 0, "text_chars": 0,
           "final_url": None, "verdict": None, "marks": [], "transport_errors": []}
    body = None
    for k in range(attempts):
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "zh-CN,zh;q=0.9"})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                body = r.read()
                rec["http"] = r.status
                rec["final_url"] = r.geturl()
            break
        except urllib.error.HTTPError as e:
            # 服务端明确应答，不重试。⚠️ 读体，否则 bytes=0 会被误读成「响应为空」
            rec["http"] = e.code
            try:
                body = e.read()
                rec["bytes"] = len(body)
                rec["text_chars"] = len(extract(body.decode("utf-8", "replace")))
                rec["body_md5"] = __import__("hashlib").md5(body).hexdigest()
            except Exception:
                pass
            rec["verdict"] = "dead"          # v1 历史口径，保留
            rec["verdict_v2"] = verdict_v2(e.code, [], rec["text_chars"])
            rec["attempts"] = k + 1
            return rec
        except Exception as e:
            rec["transport_errors"].append(f"{type(e).__name__}: {e}"[:140])
            if k < attempts - 1:
                time.sleep(3)
    if body is None:
        rec["http"] = 0
        rec["verdict"] = "dead"              # v1 历史口径，保留
        rec["verdict_v2"] = "unreachable"
        rec["attempts"] = attempts
        return rec
    rec["attempts"] = len(rec["transport_errors"]) + 1

    rec["bytes"] = len(body)
    raw = body.decode("utf-8", "replace")
    text = extract(raw)
    rec["text_chars"] = len(text)
    rec["body_md5"] = __import__("hashlib").md5(body).hexdigest()

    low = raw.lower()
    for m in AI_MARK:
        if m.lower() in low:
            rec["marks"].append(f"ai:{m}")
    if rec["final_url"] and "404" in rec["final_url"]:
        rec["marks"].append("final_url_has_404")
    hit = [m for m in MISSING if m in text[:4000]]
    if hit:
        rec["marks"].append("missing:" + "/".join(hit[:3]))

    if rec["http"] >= 400:
        rec["verdict"] = "dead"
    elif rec["marks"] and any(m.startswith(("missing:", "final_url")) for m in rec["marks"]):
        rec["verdict"] = "soft404"
    elif len(text) < 200:
        rec["verdict"] = "js_shell"
    elif rec["marks"]:
        rec["verdict"] = "ai_flagged"
    else:
        rec["verdict"] = "ok"
    rec["verdict_v2"] = verdict_v2(rec["http"], rec["marks"], len(text))
    return rec


def main():
    out = {"measured_at": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
           "ua": UA, "extract": "去script/style→去标签→实体解码→去空白", "results": []}
    for cat, url, prior, card in TARGETS:
        r = probe(url)
        r.update(category=cat, prior_recorded=prior, source_card=card)
        out["results"].append(r)
        print(f"{r['verdict_v2']:>11} | http={str(r['http']):>3} | {r['bytes']:>7}B | "
              f"{r['text_chars']:>6}字 | try={r.get('attempts')} | {cat} | 建卡时={prior} | {url[:56]}")
        if r["marks"]:
            print(f"{'':>10}   marks: {r['marks']}")
        if r["transport_errors"]:
            print(f"{'':>10}   transport: {r['transport_errors']}")
        time.sleep(1)
    if "--json" in sys.argv:
        p = sys.argv[sys.argv.index("--json") + 1]
        with open(p, "w", encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False, indent=2)
        print(f"\nsaved -> {p}")
    return out


if __name__ == "__main__":
    main()