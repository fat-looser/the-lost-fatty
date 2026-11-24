---
id: claim-0065
title: AI 检测军备竞赛量化补齐：厂商自研检测器自认「准确率低」下架、7 款检测器对中国英语学习者作文平均误报 61.3%、共享基准上「容易被骗」、监管侧单季清理 561 万条——检测的四大证据支柱（学术 × 基准 × 自我承认 × 监管）
status: 已核实
level: B
chapters: [35]
created: 2026-11-16
verified: 2026-11-18
verifier: 作者（用户指令，EDITORIAL §7 人工签字）
---

> ✅ **已签字（2026-11-18，作者人工复核，EDITORIAL §7）。签字范围：本卡已采集来源、数字口径与直引。可进入正文引用。卡内声明的未决风险（如有）不因签字关闭。**

# claim-0065：检测军备竞赛的四个量化支柱——以及第 10 处推翻的教训如何写进证据纪律

> ✅ **本卡已于 2026-11-18 经作者人工签字转正（[EDITORIAL.md](../../EDITORIAL.md) §7）。2026-11-24 新增的 C-HAT-Bench 逐表提取为**签字后 AI 辅助增补，未经人工复核**，引用前需复核；同日更正两处引文形态（见核查记录）。
> 🔑 **与 [claim-0050](claim-0050-ai-health-misinformation-supply.md) 的分工**：0050 是「供给爆炸」的 A 级系统综述 + 制度层；本卡补的是 0050 标题里明确承认缺的**「检测军备竞赛」量化数据**——四个互相独立的证据支柱。0050 标题的「仍缺」三字在 2026-11-16 由本卡补齐，0050 标题不改（历史诚实）。
> 🔑 **第 10 处推翻的教训直接写进本卡纪律**：`ai_detect` 事件证明「字段名不是字段值」。本卡每一条检测数字都**必须连同样本、场景、语言、文本长度、对抗条件**一起写；**凡厂商自报数字，必须标注「自报」；凡基准测试数字，必须标注基准的构成**。
> 🚫 **时效性红线（本卷通用）**：检测能力数字衰减极快（0050 的两层分离声明在此完全适用）。**本卡所有数字的有效期 = 各来源的测量日期**，正文引用必须带日期。

## 论断原文

> AI 检测的军备竞赛有四个互相独立的证据支柱，四个方向都指向同一句话：**检测在任何一环都暂时落后，但没有一环是零。**
>
> ① **自我承认**：OpenAI 自己的 AI 文本分类器 2023-01 上线，**2023-07-20 以「low rate of accuracy」为由下架**（官方页已 403，下架事由经 TechCrunch 报道与多来源交叉）。
>
> ② **公平性缺陷**：斯坦福团队测 7 款广泛使用的 GPT 检测器，91 篇中国英语学习者的 TOEFL 作文——**平均误报率 61.3%**，**全员一致误判 19.8%**，**至少一个检测器误标 97.8%**。对中国读者，这不是抽象的统计：**非母语写作本身就是误判的触发条件。**
>
> ③ **系统性测评**：12 款公开工具 + Turnitin + PlagiarismCheck 的学术测评结论是「**neither accurate nor reliable**」，且**整体偏向把输出判成人类写的**（即漏报偏向）；对抗混淆手段「显著恶化」检测性能。最大共享基准 RAID（600 万+ 生成、11 模型、8 领域、11 种对抗攻击）的直接结论：**当前检测器容易被对抗攻击、采样策略变化、重复惩罚与未见过的生成模型欺骗**——而厂商声称的准确率是「99% 或更高」。
>
> ④ **监管实测**：中央网信办「清朗·整治AI应用乱象」专项行动第二阶段（2026-09-02 通报）：**清理违法违规信息 561 万余条、查处账号 4.9 万余个、处置违规网站/应用 2,400 余个**（官方原文逐字核实）。监管数字证明大规模检测筛查**可行且已在生产运行**——它与 ②③ 的「不可靠」并不矛盾：**平台级筛查是「海量初筛 + 人工复核」，不是「单篇定罪」。**
>
> 而军备竞赛的「防守方反击」也有量化落点：Google DeepMind 的 SynthID-Text 水印已在生产系统运行，**约 2,000 万条 Gemini 回复**的实况实验确认质量不受影响——但利益相关必须显式标注：**该研究由 Google DeepMind 资助，作者含 DeepMind 员工，专利申请中。**

## 为什么重要

1. **第 35 章第五节的「军备竞赛」从修辞变成数据**：四个支柱来自四个互不隶属的来源体系（厂商自认 / 学术测评 / 共享基准 / 监管通报），**单一来源失真无法同时击穿四个**。
2. **对中国读者的直接利害**：Liang et al 的误报样本就是**中国英语学习者的作文**——「非母语写作被高比例误判」不是翻译过来的美国新闻，是与中国用户身份直接同构的证据。
3. **本书的方法论自证**：第 10 处推翻（`ai_detect` 字段名≠字段值）发生在本书证据层内。本卡把那条教训制度化：**检测数字必须连口径一起写，厂商自报与独立测评必须分开列**。

## 证据

### 支柱 ①（厂商自我承认：OpenAI 分类器下架）

- **事实**：AI Text Classifier 2023-01 上线；**2023-07-20 起不再提供**；官方理由：**"low rate of accuracy"**；官方补记：「We are working to incorporate feedback and are currently researching more effective provenance techniques for text」
- **一手状态**：⚠️ `openai.com/ai-text-classifier/` 与 `/blog/our-ai-classifier` **2026-11-16 实测均 403**（「Enable JavaScript and cookies to continue」人机验证页，**本书不绕过**）；archive.org 快照通道本轮同样不可达（`web.archive.org` 传输失败，与 [claim-0063](claim-0063-linkrot-measurement.md) 测量一致）→ **官方原文两个合法通道均未取得**
- **可引证来源（次级，标注）**：TechCrunch 2023-07-25 报道（存档 [`evidence/data/techcrunch-20230725-openai-classifier.html`](../data/techcrunch-20230725-openai-classifier.html)，234,515 B，MD5 `b480c30c92574ed2d0141d9460ecf9ea`），标题原文：**"OpenAI scuttles AI-written text detector over 'low rate of accuracy'"**
- ⚠️ **「正确识别 26% 的 AI 文本 / 把 9% 的人类文本误判为 AI」**：这组数字出自 OpenAI 上线时自报口径，广泛见于次级转述；**因一手页不可达，本书只能写「据多家媒体报道的 OpenAI 自测口径」，不得写成「OpenAI 官方页面载明」**。待人工复核时经订阅或浏览器人工核验后升级。

### 支柱 ②（公平性缺陷：Liang et al，Patterns 2023，开放全文逐字取证）

- 来源：Liang W, Yuksekgonul M, Mao Y, Wu E, Zou J. **GPT detectors are biased against non-native English writers.** *Patterns* 2023;4(7):100779. DOI `10.1016/j.patter.2023.100779`（2023-07-10）｜PMCID PMC10382961（开放全文已入库：[`evidence/data/pmc10382961-liang-patterns-2023.html`](../data/pmc10382961-liang-patterns-2023.html)，123,832 B，MD5 `7e56f742d8a7ba53f5f573ab9bea4e4b`）
- 直引（一字不改）：
  > "they incorrectly labeled more than half of the TOEFL essays as 'AI-generated' (**average false-positive rate: 61.3%**). **All detectors unanimously identified 19.8%** of the human-written TOEFL essays as AI authored, and **at least one detector flagged 97.8%** of TOEFL essays as AI generated."
  > "GPT detectors exhibit significant bias against **non-native English authors** … **seven widely used GPT detectors** on **91 TOEFL** essays from a Chinese …"
- **口径（必须一起写）**：7 款检测器；91 篇 TOEFL 作文（**中国英语学习者**所写）+ 美国学生作文对照；英文文本；**2023 年的检测器版本**。
- 🔑 **本章用法**：对中国读者，这就是「你的英文写作可能被判成 AI」的直接证据；同时它证明**误报的代价由写作者承担**——与第 5 章「焦虑是被制造的」同构。

### 支柱 ③（系统性测评 × 共享基准）

**3a. Weber-Wulff et al，*International Journal for Educational Integrity* 2023;19:26（开放全文逐字取证）**

- DOI `10.1007/s40979-023-00146-z`（2023-12-25 出版；⚠️ 常见误引 DOI `10.1186/s40536-023-00169-z` 不可解析，本书以 Crossref 核验的 `s40979-023-00146-z` 为准）｜开放全文入库：[`evidence/data/springer-40979-023-00146-z-weber-wulff.html`](../data/springer-40979-023-00146-z-weber-wulff.html)，491,368 B，MD5 `11ddea5c0e63255494ddcbb23838752e`
- 直引：
  > "The research covers **12 publicly available tools and two commercial systems (Turnitin and PlagiarismCheck)** … The researchers conclude that the available detection tools are **neither accurate nor reliable** and have a **main bias towards classifying the output as human-written** rather than detecting AI-generated text. Furthermore, **content obfuscation techniques significantly worsen** the performance of tools."
- 🔑 **「偏向判成人类写的」= 漏报偏向**——与第 ② 支柱的「偏向误判非母语者」（误报）方向相反。**两类失败模式并存，正文不得只引其一。**

**3b. RAID 共享基准，arXiv 2405.07940（Dugan et al，EMNLP 2024；摘要页直取）**

- 存档：[`evidence/data/arxiv-2405.07940-raid-abs.html`](../data/arxiv-2405.07940-raid-abs.html)，41,737 B，MD5 `2cd85172326e86da9c73e8e4a6ba7c9e`
- 直引：
  > "Many commercial and open-source models claim to detect machine-generated text with **extremely high accuracy (99% or more)**. … RAID includes over **6 million generations** spanning **11 models, 8 domains, 11 adversarial attacks and 4 decoding strategies**. … we evaluate … **8 open- and 4 closed-source detectors** and find that **current detectors are easily fooled** by adversarial attacks, variations in sampling strategies, repetition penalties, and unseen generative models."
- 🔑 **「声称 99%+」vs「共享基准上容易被骗」同句对举**——这就是军备竞赛最干净的定义句。

**3c. Krishna et al，arXiv 2303.11156（攻击方视角；摘要页直取）**

- 存档：[`evidence/data/arxiv-2303.11156-krishna-abs.html`](../data/arxiv-2303.11156-krishna-abs.html)，44,275 B，MD5 `49a06d825981c78afcf781e8d724a683`
- 直引（摘要）：recursive paraphrasing attack "can **significantly reduce detection rates**, it only slightly degrades text quality in many cases"；另证明**欺骗攻击（spoofing）**可行——攻击者可让检测器把**人类文本判成 AI**，带来「reputational risks for LLM developers」
- ✅ **全文数字（2026-11-16 经 ar5iv HTML 版逐字取证；⚠️ arXiv PDF 两次下载均损坏——XRef 表错，非随机截断，改走 ar5iv 转换版）**：存档 [`evidence/data/ar5iv-2303.11156-krishna-fulltext.html`](../data/ar5iv-2303.11156-krishna-fulltext.html)（606,539 B，MD5 `7d5c86276b83bdee7ed5c2ad5b8a0924`）
  > "recursive paraphrasing attack on watermarked texts, even over relatively long passages of 300 tokens in length, **can drop the detection rate (true positive rate at 1% false positive rate or TPR@1% FPR) from 99.3% to 9.7%**"
  > "OpenAI drops from **100% to 60%** after paraphrasing"；"OpenAI's RoBERTa-Large-Detector drops from **100% to around 92%**"
  > "After **two rounds of paraphrasing (pp2)**, the detection performance (TPR@1% FPR) in **all the settings drops below 50%**"
- 🔑 **口径**：数字针对**水印类**（99.3→9.7）与**微调分类器**（OpenAI 100→60）等不同检测方案，**不是同一个检测器**；正文并列时必须分开归属。

### 支柱 ④（监管实测：中央网信办三份官方原文，cac.gov.cn 直连 200）

| 通报 | 日期 | 官方 URL | 关键数字（原文逐字） |
|---|---|---|---|
| 「清朗·整治AI应用乱象」第二阶段 | 2026-09-02 | `www.cac.gov.cn/2026-09/02/c_1790099041364574.htm` | 「**累计清理违法违规信息561万余条，查处账号4.9万余个，处置违规网站、应用程序等2400余个**」 |
| 「清朗·整治AI应用乱象」部署 | 2026-04-30 | `www.cac.gov.cn/2026-04/30/c_1779289298718765.htm` | 专项行动部署；标识要求（「标识」9 命中） |
| 「清朗·整治科普健康类网络谣言」 | **2026-11-06** | `www.cac.gov.cn/2026-11/06/c_1795719652932799.htm` | **为期 2 个月**；四类重点整治（见下） |

- 存档：五份均入库（[`cac-20260902-qinglang-ai-stage2.html`](../data/cac-20260902-qinglang-ai-stage2.html) 19,763 B MD5 `33d2d2e40e772913d1f249438a0bd4e6`；[`cac-20260430-qinglang-ai-deploy.html`](../data/cac-20260430-qinglang-ai-deploy.html) 19,498 B MD5 `604af5834559fe0dbcc2988c9b66886e`；[`cac-20261106-qinglang-health-rumor.html`](../data/cac-20261106-qinglang-health-rumor.html) 18,195 B MD5 `f8ab713469849391706260f23c78db02`；**2026-11-16 新增：**[`cac-20260706-qinglang-ai-stage1.html`](../data/cac-20260706-qinglang-ai-stage1.html) 14,976 B MD5 `d21693a4c8d011b3a53de15cdd92728e`；[`cac-20260914-genai-filing-announcement.html`](../data/cac-20260914-genai-filing-announcement.html) 13,618 B MD5 `e4ed0e0557c6d238a0b04d40d443caf4`）
- 🔑 **2026-11-06 通知与本书论点的直接咬合（原文直引）**：
  > 「**借审美焦虑制造『黄连素是减肥神药』等运动、减重类谣言**」——监管文件**点名**「审美焦虑」是谣言制造的驱动机制，并点名**减重类谣言**。第 5 章「焦虑不是副作用，是产品」与第 35 章在此获得监管侧文本。
  > 「**（三）滥用人工智能技术，生成健康科普谣言**」——四子类：**批量生成同质化**涉健康文案；**AI 换脸换声盗用知名专家形象**虚假科普带货；**诱导 AI 大模型生成虚假「死亡率」「存活率」**等不实科学数据；**AI 伪造权威通报、官方健康提示**。
  > 「冒充医疗卫生健康等领域专业人士……打造所谓『国家一级保健师』『国家一级营养师』」——伪专业身份摆拍。
- ⚠️ **「561 万」的口径边界**：这是**全平台累计清理的违法违规信息总数**（含 AI 生成与非 AI），**不是「AI 检测器的准确率」，也不是「AI 内容占比」**。正文不得从 561 万反推任何比例。它的正确用法是证明：**大规模机器初筛 + 处置已在生产运行**。
- ✅ **时间线（2026-11-16 更新：第一阶段已升级为官方一手）**：2025-04「清朗·整治AI技术滥用」（处置违规 AI 产品 3,500 余款，次级转述）→ 2025-09-01《人工智能生成合成内容标识办法》施行（见 [claim-0050](claim-0050-ai-health-misinformation-supply.md)）→ 2026-04-30 专项部署（本卡一手）→ **2026-07-06 第一阶段通报（本卡一手，官方原文逐字核实）**：「累计处置违规网站、应用程序、智能体等AI产品**1.4万余款**，清理违法违规信息**600余万条**，处置账号**2.6万余个**，下架违规AI商品**1300余个**、违规开源数据集**9个**」→ 2026-09-02 第二阶段（本卡一手）→ 2026-11-06 健康谣言专项（本卡一手）。
- 🚨 **双计数口径栅栏（必须随数字一起写）**：第一阶段「600 余万条」（截至 2026-07-06）与第二阶段「561 万余条」（截至 2026-09-02）是**两个阶段的分别计数，不是累计**。**不得把两者相加得出「1161 万」**；也不得把任一单阶段数字读成「AI 违规内容总量」。两阶段通报均未披露 AI 生成内容的占比拆分。

### 支柱+（防守方反击：SynthID-Text，Nature 2024）

- 来源：Dathathri S, See A, et al. **Scalable watermarking for identifying large language model outputs.** *Nature* 2024;634(8035):818-823. DOI `10.1038/s41586-024-08025-4`（2024-10-23）｜PMID 39443777｜PMCID PMC11499265
- 直引（摘要）：
  > "Here we describe **SynthID-Text**, a **production-ready** text watermarking scheme that preserves text quality and enables high detection accuracy … we conducted a **live experiment that assessed feedback from nearly 20 million Gemini responses**, again confirming the preservation of text quality."
- ✅ **全文方法学（2026-11-16 PMC11499265 开放全文逐字取证，存档 [`evidence/data/pmc-11499265-synthid-fulltext.html`](../data/pmc-11499265-synthid-fulltext.html) 222,025 B MD5 `3e58a17274d7333e117138e2572c21c3`）**：
  > 实况实验方法："A **random fraction of queries were routed to a watermarked model and an equivalent number to the unwatermarked counterpart**"——随机分流对照；质量测量是**用户点赞/点踩率对比**（thumbs-up rate for the two models…）
  > 「human quality feedback, both from a large-scale live experiment and a **small-scale controlled study**, perplexity statistics and standard model capability benchmarks all indicate that non-distortionary SynthID-Text **causes no loss in text quality**」
  > 生产部署："SynthID-Text **has been used to watermark Gemini and Gemini Advanced**"
  > 可检性口径：全文统一用 **TPR@FPR=1%**；「we find **no significant difference in rater preference** (Extended Data Table 1)」
- ⚠️ **利益相关（逐字引用自 PubMed 利益声明）**："Work funded and performed by **Google DeepMind** … have **filed patent applications** … relating to the SynthID-Text watermarking method."
- 🔑 **两层新栅栏**：① 实况实验的质量测量是**用户点赞率**（主观反馈），不是客观质量指标；② 评分与度量全部由 DeepMind 自己设计与解读（资助已披露）。**与第 35 章既有纪律咬合**：PH-LLM/PHIA 同款处理——**水印能力的最硬证据恰好出自生成方自己**。**水印≠检测对手方文本**：SynthID 只能检测带自家水印的输出，正文不得写成「AI 文本检测已解决」。

### 中文侧独立基准 C-HAT-Bench：逐检测器表格数字（2026-11-24 逐表提取完成，签字后 AI 辅助增补）

- **基准身份**：arXiv 2609.32770（2026-09-26，桂林电子科技大学），存档 [`evidence/data/arxiv-2609.32770-chatbench-fulltext.html`](../data/arxiv-2609.32770-chatbench-fulltext.html)（778,649 B，MD5 `23c440af5788385d5ad6291f70620ad0`）。**本节全部数字由本地存档 HTML 程序化提取，零新抓取**；表内单元格逐字未动，仅表头做了合并图例（原文为两级表头）。
- **21 个检测器构成（正文 §3「Detectors」段逐字）**：「To cover general and task-specific detection settings, we use **10 zero-shot and 7 off-the-shelf supervised detectors**. The first two experiments evaluate the same detector sets. Boundary localization uses **WCP and DeBERTa–BiGRU–CRF**, while generalization experiments use **AIGC-detector-zhv2 and IMBD**.」→ **17 + 2 + 2 = 21**。
- **指标口径（§3 逐字）**：「text-level detection is evaluated using **AUROC**, Accuracy, and F1-score at a fixed **5% FPR** operating point. Boundary localization uses sentence-level **Cohen's κ**, **WindowDiff**, and **Boundary F1@1**. For generalization, we report accuracy at **cell-specific thresholds maximizing Youden's J on labeled test samples**」。
- **知网裁决（2026-11-24）**：存档全文检索 CNKI / 知网 **0 命中** → **知网 AIGC 检测不在 21 检测器之列**。「商用中文检测服务是否有独立学术测评」缺口保持开放，正文引用时保留此声明。
- **渲染说明**：HTML 存档把「Q&A」渲染为「Q A」、`±`/`κ` 带转义痕迹；本节按原貌恢复为 Q&A 与 ± / κ，**数字零改动**。
- 🚫 **本节口径栅栏**：① 全部数字对应 2026-09-26 存档快照的检测器版本，**时效性红线适用**（正文引用必须带「截至」日期）；② Table 6 数值为 **30 个域×生成模型组合 macro 平均的百分比**；③ RQ4（zhv2/IMBD）数字 **target-calibrated**（阈值取自带标注测试样本）＝**乐观上界**；④ 基准数字证明的是「**检测在中文人机协作文本上不可靠**」，**不证明任何单一商用检测器不可靠**——点名具体商用产品前仍须独立效度来源（0020 同款纪律）。

**主文观察❶（逐字，随 Table 1 引用）**：

> "Human–AI collaboration changes the detectability of machine involvement text. Relative to MGT, **mean AUROC decreases by 11.1% and 13.3% for zero-shot and supervised detectors**, respectively, when human–AI collaboration conditions are equally weighted (Table 1)."

**论文 Table 1｜17 检测器 × 11 条件 AUROC**（标题逐字：「Detector performance under human–AI collaboration, measured by AUROC」；图例逐字：「MGT denotes the prefix-conditioned continuation condition; **LC/HC indicate low/high coverage (15–35%/50–75%)**, and **C/D indicate single-suffix/separated-span filling**; **Light/Deep denote expression polishing/structural rewriting**; and **L1–L3 indicate increasing prompt detail**, with **L3+Ref additionally using a same-domain reference**）：

| 检测器 | MGT | CF·LC-C | CF·LC-D | CF·HC-C | CF·HC-D | MR·Light | MR·Deep | PG·L1 | PG·L2 | PG·L3 | PG·L3+Ref. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Log-Likelihood | 0.743 | 0.651 | 0.631 | 0.715 | 0.695 | 0.634 | 0.629 | 0.758 | 0.730 | 0.694 | 0.697 |
| LogRank | 0.746 | 0.644 | 0.624 | 0.709 | 0.689 | 0.623 | 0.616 | 0.762 | 0.727 | 0.688 | 0.691 |
| Entropy | 0.317 | 0.374 | 0.386 | 0.333 | 0.334 | 0.393 | 0.396 | 0.303 | 0.324 | 0.341 | 0.338 |
| DetectLLM-LRR | 0.712 | 0.578 | 0.560 | 0.635 | 0.610 | 0.529 | 0.516 | 0.723 | 0.661 | 0.606 | 0.608 |
| Fast-DetectGPT | 0.725 | 0.637 | 0.618 | 0.671 | 0.635 | 0.585 | 0.525 | 0.727 | 0.608 | 0.600 | 0.606 |
| Binoculars | 0.874 | 0.634 | 0.579 | 0.770 | 0.673 | 0.626 | 0.648 | 0.867 | 0.794 | 0.752 | 0.756 |
| LastDE | 0.835 | 0.681 | 0.664 | 0.743 | 0.747 | 0.671 | 0.715 | 0.848 | 0.829 | 0.773 | 0.769 |
| LastDE++ | 0.859 | 0.707 | 0.669 | 0.798 | 0.749 | 0.697 | 0.683 | 0.857 | 0.801 | 0.752 | 0.755 |
| SpecDetect | 0.895 | 0.777 | 0.748 | 0.851 | 0.829 | 0.763 | 0.773 | 0.906 | 0.882 | 0.842 | 0.843 |
| SpecDetect++ | 0.887 | 0.749 | 0.714 | 0.828 | 0.791 | 0.748 | 0.749 | 0.894 | 0.851 | 0.806 | 0.807 |
| RADAR | 0.540 | 0.373 | 0.405 | 0.311 | 0.300 | 0.434 | 0.464 | 0.583 | 0.351 | 0.370 | 0.378 |
| ReMoDetect | 0.833 | 0.706 | 0.679 | 0.798 | 0.761 | 0.730 | 0.800 | 0.879 | 0.855 | 0.807 | 0.804 |
| Longformer | 0.826 | 0.546 | 0.514 | 0.578 | 0.531 | 0.522 | 0.542 | 0.877 | 0.683 | 0.649 | 0.644 |
| BLOOMZ-3B | 0.979 | 0.808 | 0.746 | 0.817 | 0.768 | 0.668 | 0.634 | 0.998 | 0.786 | 0.771 | 0.770 |
| OpenAI RoBERTa | 0.480 | 0.421 | 0.414 | 0.424 | 0.350 | 0.541 | 0.582 | 0.482 | 0.483 | 0.487 | 0.494 |
| ConDA | 0.501 | 0.503 | 0.487 | 0.526 | 0.468 | 0.471 | 0.479 | 0.557 | 0.638 | 0.587 | 0.581 |
| ChatGPT Detector | 0.724 | 0.599 | 0.545 | 0.724 | 0.640 | 0.652 | 0.694 | 0.741 | 0.736 | 0.686 | 0.693 |

（CF＝Content Filling，MR＝Machine Rewriting，PG＝Prompt-based Generation；前 10 行 zero-shot，后 7 行 supervised。🔍 可引读数：二值设定最高的 BLOOMZ-3B 在 MGT 上 **0.979**、在 L1 上 **0.998**，但到 Content Filling 各条件降到 **0.63–0.81**；OpenAI RoBERTa 全条件 **0.35–0.58**（含二值 MGT **0.480**，接近随机）；RADAR 在 HC-C/HC-D 仅 **0.311/0.300**——低于 0.5 即「系统性反向」。）

**论文 Table 6｜ACC/F1 @ 1%/5%/10% FPR**（标题逐字：「measured by ACC and F1 at 1%, 5%, and 10% FPR … Values are reported as percentages and macro-averaged over **30 domain–generation-model combinations**」；单元格为「ACC / F1」复合，数字逐字）：

1% FPR（表后正文逐字：「**A strict false-positive budget makes collaborative text selectively invisible.** Table 6 shows that at 1% FPR, the strongest detectors retain relatively high ACC and F1 on MGT and L1, whereas content filling, machine rewriting, and more complex prompt conditions generally produce lower scores. The degradation is more pronounced in F1 than in ACC, indicating that the strict operating point suppresses true-positive coverage even when the overall accuracy remains close to chance.」）：

| 检测器 | MGT | CF·LC-C | CF·LC-D | CF·HC-C | CF·HC-D | MR·Light | MR·Subst. | PG·L1 | PG·L2 | PG·L3 | PG·L3+Ref. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Log-Likelihood | 58.5 / 22.5 | 52.6 / 10.4 | 52.3 / 9.6 | 53.8 / 14.1 | 54.8 / 15.7 | 52.5 / 10.0 | 52.6 / 10.3 | 56.7 / 18.9 | 53.4 / 12.2 | 53.6 / 12.7 | 53.9 / 13.5 |
| LogRank | 58.4 / 21.5 | 52.4 / 9.6 | 52.3 / 9.1 | 53.4 / 12.8 | 54.5 / 14.8 | 52.2 / 9.0 | 52.4 / 9.4 | 56.9 / 18.5 | 53.2 / 11.4 | 53.4 / 11.8 | 53.7 / 12.4 |
| Entropy | 50.1 / 2.3 | 49.9 / 1.7 | 49.9 / 1.6 | 49.9 / 1.4 | 50.0 / 1.7 | 49.9 / 1.4 | 50.0 / 1.7 | 50.0 / 1.7 | 49.8 / 1.1 | 50.0 / 1.7 | 50.0 / 1.6 |
| DetectLLM-LRR | 53.2 / 10.7 | 50.4 / 3.2 | 50.4 / 3.3 | 50.6 / 3.8 | 50.6 / 4.0 | 50.2 / 2.5 | 50.2 / 2.5 | 53.4 / 10.8 | 50.6 / 3.7 | 50.7 / 4.3 | 50.8 / 4.4 |
| Fast-DetectGPT | 54.9 / 18.5 | 51.5 / 7.4 | 51.2 / 6.4 | 52.1 / 9.6 | 52.1 / 9.0 | 50.7 / 4.7 | 50.2 / 2.9 | 54.1 / 15.7 | 51.0 / 5.5 | 50.8 / 4.8 | 50.9 / 5.2 |
| Binoculars | 69.2 / 52.3 | 51.5 / 7.4 | 50.7 / 4.6 | 58.1 / 26.7 | 53.7 / 14.8 | 50.8 / 5.1 | 51.0 / 5.5 | 65.4 / 44.6 | 58.1 / 26.3 | 55.1 / 18.2 | 55.4 / 19.4 |
| LastDE | 53.9 / 14.9 | 50.5 / 3.7 | 50.4 / 3.6 | 50.9 / 5.1 | 51.1 / 6.1 | 50.4 / 3.2 | 50.8 / 4.6 | 54.1 / 14.7 | 52.7 / 10.6 | 51.7 / 7.6 | 51.8 / 7.9 |
| LastDE++ | 60.0 / 32.0 | 51.5 / 7.6 | 51.0 / 5.9 | 54.4 / 17.1 | 52.5 / 11.2 | 50.9 / 5.2 | 50.8 / 4.7 | 57.3 / 25.0 | 53.8 / 14.0 | 52.0 / 9.1 | 52.0 / 9.1 |
| SpecDetect | 66.3 / 45.4 | 56.4 / 21.7 | 55.8 / 19.9 | 60.5 / 33.0 | 59.8 / 29.9 | 56.8 / 22.1 | 57.2 / 23.2 | 65.1 / 42.5 | 60.3 / 32.4 | 58.4 / 27.1 | 58.6 / 27.6 |
| SpecDetect++ | 61.9 / 37.2 | 52.0 / 9.4 | 51.5 / 7.6 | 55.2 / 19.6 | 53.3 / 13.8 | 51.7 / 8.2 | 51.5 / 7.5 | 59.7 / 32.0 | 55.5 / 19.7 | 53.2 / 13.3 | 53.3 / 13.6 |
| RADAR | 49.9 / 1.4 | 49.7 / 0.6 | 49.7 / 1.0 | 49.6 / 0.4 | 49.6 / 0.5 | 49.6 / 0.4 | 49.6 / 0.3 | 49.6 / 0.5 | 49.6 / 0.2 | 49.5 / 0.0 | 49.5 / 0.0 |
| ReMoDetect | 59.5 / 28.4 | 52.2 / 9.6 | 51.1 / 6.0 | 57.1 / 23.2 | 53.6 / 13.8 | 51.9 / 8.7 | 53.9 / 14.8 | 60.2 / 29.3 | 60.5 / 28.9 | 59.5 / 26.3 | 59.4 / 26.2 |
| Longformer | 55.6 / 19.9 | 49.8 / 1.4 | 50.0 / 1.8 | 49.8 / 1.3 | 49.8 / 1.3 | 49.8 / 1.0 | 50.1 / 2.4 | 56.7 / 23.0 | 51.4 / 6.6 | 50.7 / 4.6 | 50.8 / 4.8 |
| BLOOMZ-3B | 92.8 / 90.4 | 52.7 / 11.4 | 51.9 / 8.8 | 52.8 / 11.8 | 52.5 / 10.8 | 50.6 / 4.3 | 51.3 / 6.7 | 98.2 / 98.0 | 57.2 / 24.7 | 56.9 / 22.4 | 57.4 / 23.3 |
| OpenAI RoBERTa | 49.8 / 1.1 | 49.8 / 1.2 | 49.9 / 1.5 | 49.8 / 1.1 | 49.7 / 0.8 | 50.1 / 2.3 | 50.2 / 2.5 | 49.9 / 1.3 | 49.7 / 0.8 | 49.7 / 0.7 | 49.7 / 0.8 |
| ConDA | 49.8 / 1.1 | 49.8 / 1.3 | 49.9 / 1.5 | 49.8 / 1.1 | 49.8 / 1.1 | 49.8 / 1.0 | 49.8 / 0.9 | 49.9 / 1.4 | 49.9 / 1.6 | 49.8 / 1.2 | 49.8 / 1.2 |
| ChatGPT Detector | 51.9 / 8.3 | 50.3 / 2.8 | 50.2 / 2.5 | 50.9 / 4.9 | 50.7 / 4.2 | 50.4 / 3.1 | 50.3 / 2.7 | 51.2 / 6.1 | 50.6 / 4.0 | 51.2 / 6.0 | 51.4 / 6.4 |

5% FPR：

| 检测器 | MGT | CF·LC-C | CF·LC-D | CF·HC-C | CF·HC-D | MR·Light | MR·Subst. | PG·L1 | PG·L2 | PG·L3 | PG·L3+Ref. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Log-Likelihood | 60.8 / 30.3 | 56.1 / 22.2 | 55.7 / 21.2 | 58.3 / 27.6 | 58.4 / 26.5 | 56.3 / 22.1 | 56.5 / 22.4 | 60.1 / 28.4 | 57.8 / 24.6 | 57.9 / 24.7 | 58.1 / 25.1 |
| LogRank | 60.0 / 27.9 | 55.3 / 19.8 | 55.0 / 18.8 | 57.2 / 24.5 | 57.2 / 23.3 | 55.2 / 19.2 | 55.5 / 19.4 | 59.2 / 25.7 | 56.7 / 21.4 | 56.7 / 21.1 | 57.0 / 21.7 |
| Entropy | 49.2 / 5.6 | 49.2 / 5.7 | 49.3 / 6.1 | 48.8 / 4.5 | 49.2 / 5.2 | 49.3 / 6.0 | 49.8 / 7.4 | 49.0 / 4.6 | 48.8 / 4.0 | 49.3 / 5.4 | 49.2 / 5.3 |
| DetectLLM-LRR | 55.3 / 17.4 | 51.1 / 9.5 | 51.1 / 9.6 | 51.6 / 11.0 | 51.8 / 11.1 | 50.5 / 8.3 | 50.6 / 8.4 | 55.2 / 16.4 | 51.5 / 10.2 | 51.6 / 10.2 | 51.7 / 10.5 |
| Fast-DetectGPT | 60.5 / 37.9 | 54.4 / 22.1 | 53.7 / 20.4 | 56.0 / 26.6 | 55.0 / 23.0 | 52.5 / 16.6 | 51.0 / 11.9 | 59.8 / 35.3 | 53.1 / 17.9 | 52.5 / 16.7 | 52.9 / 17.7 |
| Binoculars | 76.9 / 69.5 | 54.0 / 21.4 | 52.3 / 16.2 | 64.2 / 45.6 | 58.3 / 32.1 | 52.9 / 18.3 | 53.5 / 19.9 | 74.1 / 65.1 | 65.3 / 48.4 | 60.9 / 38.6 | 61.5 / 39.9 |
| LastDE | 61.4 / 38.4 | 52.2 / 15.3 | 52.0 / 14.4 | 54.1 / 20.8 | 55.1 / 23.6 | 52.2 / 15.2 | 54.0 / 20.1 | 61.8 / 38.1 | 59.7 / 32.6 | 56.8 / 25.5 | 56.9 / 25.7 |
| LastDE++ | 69.7 / 57.6 | 55.3 / 25.2 | 53.7 / 20.7 | 61.6 / 41.0 | 58.2 / 32.9 | 54.2 / 22.3 | 53.7 / 20.1 | 67.1 / 52.7 | 60.7 / 38.0 | 56.8 / 28.8 | 57.1 / 29.6 |
| SpecDetect | 74.7 / 65.4 | 63.3 / 41.4 | 61.5 / 37.2 | 68.9 / 54.7 | 67.1 / 50.1 | 63.0 / 40.0 | 63.4 / 40.6 | 74.8 / 65.5 | 70.9 / 58.2 | 66.6 / 48.6 | 66.9 / 49.3 |
| SpecDetect++ | 72.4 / 62.9 | 57.2 / 30.5 | 55.4 / 25.6 | 63.7 / 46.0 | 60.3 / 38.4 | 56.5 / 28.7 | 56.2 / 27.5 | 71.7 / 61.3 | 64.8 / 47.5 | 60.6 / 38.2 | 61.0 / 39.1 |
| RADAR | 49.9 / 8.1 | 48.8 / 4.3 | 49.3 / 6.1 | 48.0 / 1.9 | 48.4 / 3.4 | 48.5 / 3.4 | 48.5 / 3.6 | 50.2 / 8.8 | 48.1 / 2.2 | 47.7 / 0.9 | 47.8 / 1.0 |
| ReMoDetect | 70.9 / 55.1 | 58.8 / 31.7 | 56.7 / 27.3 | 66.8 / 48.0 | 62.8 / 40.5 | 59.1 / 33.0 | 63.6 / 42.4 | 71.5 / 55.5 | 70.1 / 49.8 | 69.2 / 47.1 | 69.0 / 46.8 |
| Longformer | 67.3 / 51.7 | 50.2 / 9.6 | 50.1 / 9.0 | 50.4 / 10.2 | 50.1 / 9.4 | 49.9 / 8.4 | 50.7 / 11.1 | 71.3 / 59.8 | 55.8 / 25.3 | 54.4 / 21.6 | 54.8 / 22.4 |
| BLOOMZ-3B | 91.6 / 89.6 | 57.5 / 29.4 | 55.3 / 23.9 | 58.2 / 30.9 | 56.4 / 26.4 | 51.6 / 13.8 | 51.4 / 13.6 | 96.5 / 96.6 | 59.5 / 35.1 | 58.4 / 31.4 | 58.8 / 32.1 |
| OpenAI RoBERTa | 48.9 / 4.9 | 49.1 / 5.2 | 49.3 / 6.0 | 48.9 / 4.6 | 48.5 / 3.7 | 50.4 / 9.4 | 50.7 / 10.4 | 49.0 / 5.1 | 48.5 / 3.4 | 48.4 / 3.2 | 48.5 / 3.6 |
| ConDA | 49.7 / 7.8 | 49.7 / 7.6 | 49.7 / 7.5 | 49.6 / 7.5 | 48.9 / 5.3 | 48.7 / 4.5 | 48.7 / 4.3 | 50.4 / 9.8 | 51.7 / 14.0 | 50.3 / 9.6 | 50.2 / 9.4 |
| ChatGPT Detector | 53.7 / 17.4 | 51.3 / 11.2 | 50.5 / 9.0 | 54.4 / 19.1 | 51.7 / 12.5 | 51.3 / 10.8 | 51.2 / 10.5 | 53.1 / 15.8 | 52.9 / 15.5 | 54.2 / 18.1 | 54.6 / 18.9 |

10% FPR：

| 检测器 | MGT | CF·LC-C | CF·LC-D | CF·HC-C | CF·HC-D | MR·Light | MR·Subst. | PG·L1 | PG·L2 | PG·L3 | PG·L3+Ref. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Log-Likelihood | 60.1 / 33.3 | 56.8 / 27.1 | 56.2 / 25.6 | 58.9 / 32.2 | 58.6 / 30.6 | 56.7 / 26.5 | 57.1 / 27.0 | 59.6 / 32.1 | 58.1 / 28.7 | 58.1 / 28.6 | 58.4 / 29.3 |
| LogRank | 59.2 / 30.8 | 55.8 / 24.2 | 55.4 / 23.2 | 57.9 / 29.3 | 57.4 / 27.1 | 55.7 / 23.5 | 55.8 / 23.5 | 58.6 / 29.0 | 56.9 / 25.5 | 56.9 / 25.1 | 57.1 / 25.5 |
| Entropy | 48.1 / 8.9 | 48.5 / 10.5 | 48.8 / 11.2 | 47.6 / 7.6 | 48.2 / 8.9 | 48.8 / 11.3 | 49.6 / 13.1 | 47.8 / 7.4 | 47.5 / 6.6 | 48.5 / 9.1 | 48.5 / 9.1 |
| DetectLLM-LRR | 55.5 / 21.4 | 51.7 / 14.3 | 51.5 / 13.7 | 52.2 / 15.9 | 52.0 / 14.9 | 50.8 / 12.6 | 50.9 / 12.5 | 55.0 / 19.4 | 52.0 / 14.4 | 51.9 / 13.8 | 51.9 / 14.0 |
| Fast-DetectGPT | 63.9 / 49.1 | 56.5 / 33.1 | 55.8 / 31.5 | 58.5 / 37.8 | 57.0 / 33.2 | 53.9 / 26.4 | 51.6 / 19.9 | 63.1 / 46.7 | 55.0 / 28.5 | 54.3 / 27.2 | 54.6 / 28.1 |
| Binoculars | 79.8 / 76.1 | 56.4 / 33.6 | 53.8 / 26.7 | 68.0 / 57.1 | 60.8 / 42.4 | 55.2 / 30.4 | 56.3 / 32.9 | 77.9 / 73.5 | 69.7 / 60.3 | 65.0 / 51.2 | 65.6 / 52.4 |
| LastDE | 66.2 / 52.1 | 54.6 / 27.0 | 54.1 / 25.9 | 57.9 / 35.3 | 58.9 / 37.4 | 54.4 / 27.0 | 57.2 / 33.3 | 66.6 / 52.2 | 64.3 / 47.1 | 60.5 / 38.6 | 60.3 / 38.3 |
| LastDE++ | 74.9 / 69.4 | 59.0 / 39.9 | 57.0 / 35.2 | 66.9 / 56.1 | 62.7 / 48.0 | 58.0 / 37.9 | 57.0 / 34.6 | 73.4 / 67.2 | 66.2 / 54.2 | 61.6 / 44.8 | 62.0 / 45.9 |
| SpecDetect | 77.6 / 72.7 | 65.7 / 50.7 | 63.5 / 45.7 | 71.7 / 63.1 | 69.6 / 58.6 | 64.7 / 48.0 | 65.3 / 48.6 | 78.4 / 73.8 | 75.1 / 68.2 | 70.2 / 59.1 | 70.3 / 59.4 |
| SpecDetect++ | 77.0 / 72.7 | 60.9 / 43.9 | 58.5 / 38.5 | 68.4 / 58.8 | 64.7 / 52.0 | 60.5 / 43.5 | 60.1 / 42.0 | 76.9 / 72.2 | 70.3 / 61.3 | 65.5 / 52.2 | 65.9 / 53.1 |
| RADAR | 50.4 / 16.5 | 47.8 / 8.8 | 48.7 / 11.6 | 46.5 / 4.8 | 47.1 / 7.5 | 47.5 / 8.1 | 47.8 / 9.2 | 52.1 / 18.9 | 46.6 / 5.3 | 45.9 / 3.2 | 45.9 / 3.3 |
| ReMoDetect | 74.4 / 62.9 | 62.6 / 42.9 | 60.7 / 39.5 | 70.8 / 57.2 | 67.0 / 51.2 | 63.4 / 44.8 | 68.2 / 53.5 | 75.4 / 64.9 | 72.4 / 57.1 | 71.2 / 53.7 | 71.0 / 53.7 |
| Longformer | 71.5 / 62.6 | 50.6 / 17.7 | 49.9 / 15.5 | 51.2 / 19.7 | 50.1 / 16.8 | 49.8 / 15.3 | 50.8 / 18.3 | 76.2 / 70.7 | 58.2 / 35.8 | 56.3 / 31.5 | 56.6 / 31.9 |
| BLOOMZ-3B | 89.7 / 88.6 | 61.9 / 43.5 | 58.3 / 35.6 | 62.4 / 44.5 | 59.9 / 38.9 | 52.8 / 22.7 | 51.8 / 21.4 | 94.3 / 95.0 | 61.6 / 44.1 | 59.8 / 39.5 | 60.2 / 40.0 |
| OpenAI RoBERTa | 48.1 / 10.1 | 48.4 / 10.0 | 48.7 / 10.9 | 47.8 / 8.4 | 47.0 / 6.8 | 50.8 / 16.6 | 51.5 / 18.4 | 48.2 / 10.0 | 47.3 / 7.7 | 47.5 / 7.9 | 47.7 / 8.4 |
| ConDA | 49.8 / 14.9 | 49.5 / 14.4 | 49.4 / 13.9 | 49.8 / 15.5 | 48.5 / 11.6 | 47.8 / 9.1 | 47.6 / 8.8 | 51.0 / 18.0 | 53.8 / 25.4 | 51.2 / 19.2 | 50.9 / 18.2 |
| ChatGPT Detector | 55.5 / 26.7 | 52.6 / 19.1 | 51.0 / 15.6 | 56.7 / 29.0 | 53.7 / 22.7 | 52.9 / 19.9 | 53.2 / 21.2 | 55.3 / 26.2 | 56.7 / 29.1 | 56.9 / 27.3 | 57.0 / 27.2 |

**论文 Table 7｜分域 AUROC（17 检测器 × 5 目标域）**（标题逐字：「Each value is **macro-averaged over six generation models** and the fine-grained conditions within each of the four text-production settings, followed by an **equal-weight average over the four settings**」）：

| 检测器 | Law | Literature | News | Encyclopedia | Q&A |
|---|---|---|---|---|---|
| Log-Likelihood | 0.891 | 0.575 | 0.618 | 0.676 | 0.698 |
| LogRank | 0.873 | 0.583 | 0.614 | 0.669 | 0.698 |
| Entropy | 0.182 | 0.479 | 0.399 | 0.346 | 0.337 |
| DetectLLM-LRR | 0.663 | 0.602 | 0.572 | 0.602 | 0.661 |
| Fast-DetectGPT | 0.783 | 0.602 | 0.552 | 0.604 | 0.655 |
| Binoculars | 0.801 | 0.809 | 0.662 | 0.736 | 0.702 |
| LastDE | 0.832 | 0.686 | 0.766 | 0.768 | 0.749 |
| LastDE++ | 0.876 | 0.685 | 0.728 | 0.761 | 0.788 |
| SpecDetect | 0.958 | 0.675 | 0.790 | 0.875 | 0.868 |
| SpecDetect++ | 0.905 | 0.682 | 0.794 | 0.841 | 0.836 |
| RADAR | 0.529 | 0.580 | 0.397 | 0.421 | 0.268 |
| ReMoDetect | 0.923 | 0.627 | 0.870 | 0.854 | 0.690 |
| Longformer | 0.663 | 0.698 | 0.686 | 0.553 | 0.667 |
| BLOOMZ-3B | 0.837 | 0.594 | 0.894 | 0.874 | 0.858 |
| OpenAI RoBERTa | 0.508 | 0.572 | 0.502 | 0.390 | 0.441 |
| ConDA | 0.647 | 0.572 | 0.439 | 0.450 | 0.470 |
| ChatGPT Detector | 0.759 | 0.653 | 0.672 | 0.621 | 0.719 |

（🔍 可引读数：域难度分层稳定——Law 对多数检测器最容易（SpecDetect **0.958**），Q&A 与 Literature 最难（RADAR 在 Q&A 仅 **0.268**，OpenAI RoBERTa 在 Encyclopedia 仅 **0.390**）。「同一款检测器换个领域就换一副面孔」在中文侧有了逐检测器数字。）

**论文 Table 8｜边界定位（2 检测器 × 4 条件，Content Filling 测试集）**（标题逐字：「values are **document-level means ± population standard deviations**; Boundary F1@1 uses **one-to-one matching** between predicted and gold boundaries」）：

| 条件 | 检测器 | n | Sentence κ ↑ | WindowDiff ↓ | Boundary F1@1 ↑ |
|---|---|---|---|---|---|
| LC-C | WCP | 1962 | 0.194 ± 0.343 | 0.428 ± 0.206 | 0.168 ± 0.226 |
| LC-C | DeBERTa–BiGRU–CRF | 1962 | -0.054 ± 0.101 | 0.386 ± 0.184 | 0.004 ± 0.051 |
| LC-D | WCP | 1886 | 0.019 ± 0.163 | 0.381 ± 0.101 | 0.380 ± 0.232 |
| LC-D | DeBERTa–BiGRU–CRF | 1886 | 0.258 ± 0.250 | 0.309 ± 0.102 | 0.373 ± 0.271 |
| HC-C | WCP | 1877 | 0.166 ± 0.373 | 0.451 ± 0.185 | 0.171 ± 0.231 |
| HC-C | DeBERTa–BiGRU–CRF | 1877 | 0.005 ± 0.152 | 0.336 ± 0.089 | 0.341 ± 0.327 |
| HC-D | WCP | 1637 | 0.051 ± 0.198 | 0.355 ± 0.099 | 0.412 ± 0.238 |
| HC-D | DeBERTa–BiGRU–CRF | 1637 | 0.238 ± 0.183 | 0.303 ± 0.101 | 0.464 ± 0.232 |
| Overall | WCP | 7362 | 0.110 ± 0.297 | 0.405 ± 0.162 | 0.277 ± 0.258 |
| Overall | DeBERTa–BiGRU–CRF | 7362 | 0.106 ± 0.227 | 0.335 ± 0.131 | 0.287 ± 0.299 |

**主文观察❼（逐字，Table 8/9 的正文读法）**：

> "Low-coverage contiguous filling exposes opposing failure modes. DeBERTa–BiGRU–CRF's Boundary F1@1 **falls to 0.004**, compared with 0.341 at high coverage; **70.9%** of these samples yield no predicted boundary. As its token predictions are mapped to sentence-level labels, this pattern points to missed authorship transitions rather than small boundary offsets. WCP, in contrast, tends to predict excess boundaries on the same texts."

**论文 Table 9｜边界预测诊断**（标题逐字：「**No predicted boundary** is the percentage of documents with zero predicted boundaries … **Mean count error** is defined as gold minus predicted boundaries, so negative and positive values indicate **over-segmentation and missed** boundaries」）：

| 条件 | 检测器 | n | 无预测边界 (%) | 预测边界均值 | 真实边界均值 | 计数误差均值 |
|---|---|---|---|---|---|---|
| LC-C | WCP | 1962 | 4.18 | 4.497 | 1.000 | -3.497 |
| LC-C | DeBERTa–BiGRU–CRF | 1962 | 70.90 | 0.629 | 1.000 | 0.371 |
| LC-D | WCP | 1886 | 5.51 | 4.073 | 4.914 | 0.841 |
| LC-D | DeBERTa–BiGRU–CRF | 1886 | 24.23 | 1.694 | 4.914 | 3.221 |
| HC-C | WCP | 1877 | 3.94 | 4.384 | 1.000 | -3.384 |
| HC-C | DeBERTa–BiGRU–CRF | 1877 | 31.43 | 1.477 | 1.000 | -0.477 |
| HC-D | WCP | 1637 | 6.66 | 3.664 | 5.561 | 1.897 |
| HC-D | DeBERTa–BiGRU–CRF | 1637 | 2.69 | 2.561 | 5.561 | 2.999 |
| Overall | WCP | 7362 | 5.01 | 4.174 | 3.017 | -1.158 |
| Overall | DeBERTa–BiGRU–CRF | 7362 | 33.71 | 1.548 | 3.017 | 1.469 |

**RQ4 跨域泛化（zhv2 / IMBD）**：zhv2 观察❽❾数字已在「反方与局限」第 2 条（2026-11-17 入库，逐字已核，**含 target-calibrated 口径栅栏**）；5×5 ACC 矩阵在 **Figure 6**（图像，非表格）。IMBD 全部数字在 **Figure 9/10/11**（图像）；正文可引的只有 D.4 定性结论（逐字）：「**News provides the strongest cross-domain training source for both detectors, whereas Literature is the most difficult target, especially for IMBD.**」「**GPT is the strongest source for AIGC-detector-zhv2 but the weakest source for IMBD**, while **Kimi causes a marked source-side drop for AIGC-detector-zhv2** without a comparable effect on IMBD.」

## 四支柱合并裁决

| 问题 | 能回答的支柱 | 答案 |
|---|---|---|
| 检测器单篇定罪可靠吗？ | ②③ | **不可靠**（61.3% 误报 / neither accurate nor reliable），且两类失败模式并存（漏报偏向 + 非母语误报偏向） |
| 厂商声称的 99% 可信吗？ | ③b | 共享基准上「容易被骗」；**自报数字与独立基准分离引用** |
| 生成方自己认账吗？ | ① | 认账——自研检测器以「准确率低」下架（次级来源标注） |
| 平台级检测存在吗？ | ④ | 存在且规模运行（561 万条/季），但它是**初筛**不是定罪 |
| 防守方有没有技术反击？ | 支柱+ | 有（水印），但**只能检测自家带水印输出**，且证据出自利益相关方 |

🚫 **合并红线**：① 不得写「AI 检测完全没用」（④ 反例在）；② 不得写「检测已经够用」（②③ 反例在）；③ 不得把 561 万条当成 AI 检测率；④ **正文表述统一为「海量初筛 + 人工复核 + 水印补位」三层结构**，任何单层不得被写成「解决方案」。

## 反方与局限

1. **时效性（最大局限）**：支柱 ② 是 2023 年的检测器版本——**今天的检测器可能更好**。但 RAID（2024）与监管实践（2026）表明差距结构未变。**正文必须写「截至 [日期]，公开测评显示……」**。
2. **语言边界（2026-11-16 部分关闭 → 2026-11-24 逐表提取完成）**：支柱 ②③ 测评对象为英文；**中文侧已取得独立学术基准 C-HAT-Bench**（arXiv 2609.32770，2026-09-26，桂林电子科技大学；C-HAT-240K 数据集：人类源文本 5,000 篇 × 5 领域，机写样本 **240,539 条**——论文 Table 4 四任务合计 28,321+36,907+59,038+116,273 与分域合计 240,539 交叉一致）。**21 个检测器构成已厘清（2026-11-24）**：正文「Detectors」段逐字——「we use **10 zero-shot and 7 off-the-shelf supervised detectors**」（文本级检测 17 个）＋「Boundary localization uses **WCP and DeBERTa–BiGRU–CRF**」（边界定位 2 个）＋「generalization experiments use **AIGC-detector-zhv2 and IMBD**」（跨域泛化 2 个），即 **17 + 2 + 2 = 21**。摘要核心裁决**逐字更正入库**（2026-11-24 更正：此前卡内把原文「Machine-Generated Text (MGT)」缩写为「MGT」）：「**Yet most Machine-Generated Text (MGT) detectors are evaluated only on fully human-written versus fully AI-generated text. Because human–AI collaboration can weaken or redistribute cues associated with machine generation, strong performance under this binary setting may overstate detector reliability.**」。🚨 **2026-11-24 撤销一条合成引语**：本卡旧文「边界定位任务中出现『F1@1 falls to 0』与『overall accuracy remains close to chance』级失败」系两处不同上下文的片段误拼——「F1@1 falls to 0(004)」出自观察❼边界定位（正确数字 0.004），「overall accuracy remains close to chance」出自论文 Table 6 的 1% FPR 操作点评论（与边界定位无关）。两句的正确逐字形态见本卡证据节「中文侧独立基准」小节。✅ **2026-11-17 首批逐检测器中文数字入库**（焦点检测器 **AIGC-detector-zhv2**，即朱雀 v2，观察❽❾逐字）：「the mean cross-domain ACC is lowest when Literature is the target domain (**78.24%**), but reaches **85.43%** when the detector is trained on Literature and evaluated on the remaining domains」；「Training on News produces the highest mean cross-domain ACC (**87.45%**), with **86.1%–88.6%** on the other domains, whereas Q&A yields **79.9%** and **falls to 61.8% on Law**」。🚨 **新增口径栅栏（2026-11-24，随数字强制）**：RQ4 跨域准确率的阈值口径是「**cell-specific thresholds maximizing Youden's J on labeled test samples**」「**the results therefore reflect target-calibrated performance**」——**阈值在带标注测试样本上逐格取最优，全部跨域数字是乐观上界，不得读作部署性能**。🔑 可引结论句：「**High in-domain accuracy alone does not establish transferable detection cues**」——单域高准确率不等于跨域可迁移，这正是「检测军备竞赛」在中文侧的量化注脚。✅ **其余 17+1 个检测器的表格数字已于 2026-11-24 逐表提取入库**（论文 Table 1/6/7/8/9 → 见本卡证据节）；⚠️ **zhv2 的 5×5 跨域矩阵与 IMBD 的全部数字仅存于图像**（Figure 6/9/10/11），正文可引粒度止于观察句与 D.4 定性结论，逐格数字须人工读图。
3. **OpenAI 一手缺失**：支柱 ① 的 26%/9% 只有次级来源（一手页 403，本书不绕过）。若人工复核仍无法核验，正文只保留下架事由（TechCrunch 标题级），**删去 26%/9% 具体数字**。
4. **Krishna 具体百分比未取得**：摘要不含数字，正文百分比待全文。**现有引用仅到「显著降低」粒度。**
5. **561 万的构成不明**：官方通报未拆分「AI 生成 vs 非 AI」「涉健康 vs 泛内容」。**任何拆分推断都是编造。**
6. **SynthID 利益相关**：Google DeepMind 资助 + 专利申请中（已逐字披露）。**「质量不受影响」的评判含大量 DeepMind 自评成分**（尽管有人工 side-by-side 评分，样本与流程细节需全文核验）。
7. **监管通报的「成绩单」性质**：专项行动通报是工作进展汇报，**清理量既是「乱象规模」也是「执法力度」的函数**，不得单读为「AI 内容泛滥程度」。
8. **样本偏差**：本卡的学术来源全部是本书主动检索所得，非系统综述。**若存在「检测器很准」的独立测评未被本卡纳入，四支柱裁决需复核**（RAID 摘要「声称 99%+」已部分覆盖该方向，但仍是引述而非纳入测评）。
9. **status 待核实**：全部直引已逐字核对（开放全文/官方页），但按 EDITORIAL §7 须人工签字。
10. **D 级素材缺口**：本卡无任何用户被误判的第一人称经历（E 级）。**「被误判的学生」目前只是统计数字，没有面孔**——这与第 35 章的写法缺口一致，待访谈。

## 核查记录

| 日期 | 核查人 | 动作 | 结论 |
|---|---|---|---|
| 2026-11-16 | AI 辅助检索（待人工复核） | Crossref 核验三篇 DOI；**发现 Weber-Wulff 常见误引 DOI（s40536 系）不可解析**，以 `10.1007/s40979-023-00146-z` 为准 | 书目口径落定 |
| 2026-11-16 | AI 辅助检索（待人工复核） | PubMed efetch 双摘要 + PMC10382961 开放全文逐字取证（61.3%/19.8%/97.8%） | 支柱②数字逐字命中 |
| 2026-11-16 | AI 辅助检索（待人工复核） | Springer 开放全文（491 KB）逐字取证（neither accurate nor reliable 等） | 支柱③a 结论句逐字命中 |
| 2026-11-16 | AI 辅助检索（待人工复核） | arXiv 主站 abs 页 ×2（export API 429 限流后改道，间隔重试） | 支柱③b/③c 摘要逐字命中；Krishna 具体百分比不在摘要 |
| 2026-11-16 | AI 辅助检索（待人工复核） | cac.gov.cn 官方页 ×3 直连 200，561 万/4.9 万/2,400 逐字命中；健康谣言专项（2026-11-06）全文提取 | 支柱④官方原文入库；⚠️ nhc/nmpa 412 与 cac 200 并存——同国政务站防护策略不同，与 claim-0063 一致 |
| 2026-11-16 | AI 辅助检索（待人工复核） | openai.com 403（不绕过）；web.archive.org 000（与 claim-0063 一致） | 支柱①降级为次级来源标注 |
| 2026-11-16 | AI 辅助检索（待人工复核） | URL 审计：全部探测目标与检索结果原始地址逐一比对 | 无代理替换、无越界主机 |
| 2026-11-16 | AI 辅助检索（待人工复核） | **清朗一阶段官方原文定位并核实**（cac.gov.cn「落实举措」专栏 → `2026-07/06/c_1785081384384987.htm`，200）：1.4万款/600余万条/2.6万账号/1300余商品/9个数据集逐字命中 | 待核实第 4 条关闭；**新增双计数口径栅栏**（600余万 vs 561万为两阶段分别计数） |
| 2026-11-16 | AI 辅助检索（待人工复核） | **生成式 AI 备案公告官方正文核实**（`2026-09/14/c_1791136833136332.htm`，200）：截至 8-31 累计 **1112 款备案、731 款登记**（新增 124 备案含 7 款手机端侧 / 133 登记） | 附件列表 JS 渲染未能程序化取得 → Keepace.ai 条目升级为多源次级（见 0066 核查记录） |
| 2026-11-16 | AI 辅助检索（待人工复核） | **Krishna 全文数字取证**：arXiv PDF ×2 下载均损坏（XRef 错，1.5MB/1.9MB）→ 改走 ar5iv HTML 版（606KB）→ 四组数字逐字入库（99.3→9.7 / 100→60 / 100→92 / 两轮后全部<50%） | 待核实第 3 条关闭；**支柱③c 从「显著降低」粒度升级为具体数字** |
| 2026-11-16 | AI 辅助检索（待人工复核） | **SynthID PMC 全文取证**（PMC11499265，222KB）：随机分流对照方法、TPR@FPR=1% 口径、质量三层证据、生产部署句逐字入库；**新增两层栅栏**（质量测量=用户点赞率主观反馈；全部由 DeepMind 设计解读） | 待核实第 5 条按「方法学已核实」级关闭 |
| 2026-11-16 | AI 辅助检索（待人工复核） | **中文检测基准取得**：C-HAT-Bench（arXiv 2609.32770，778KB HTML 存档）——21 检测器 × 4 协议 × C-HAT-240K；头条裁决逐字入库 | 待核实第 1 条部分关闭；「全部学术证据为英文」的表述作废，改为「逐检测器中文数字待提取」 |
| 2026-11-17 | AI 辅助检索（待人工复核） | **C-HAT-Bench 焦点检测器数字提取**（本地存档 HTML，零新抓取）：朱雀 v2 跨域 ACC 61.8%–88.6%（观察 ❽❾ 逐字）+ 「High in-domain accuracy alone does not establish transferable detection cues」 | 中文侧从「零数字」升级为「基准级数字」；其余 20 检测器待逐表 |
| 2026-11-24 | AI 辅助检索（**签字后增补，未经人工复核**） | **C-HAT-Bench 逐表提取完成**（本地存档 HTML 程序化提取，零新抓取，表格逐格断言校验通过）：论文 Table 1/6/7/8/9 全部 **105 个检测器行**逐格入库（17 + 3×17 + 17 + 10 + 10）；21 检测器构成厘清（17 文本级 + 2 边界定位 + 2 跨域）；知网/CNKI 全文 **0 命中**→不在列；机写样本 **240,539** 条经 Table 4 任务合计（28,321+36,907+59,038+116,273）与分域合计交叉一致；观察❶❼与 D.4 IMBD 定性句逐字入库；RQ4 **target-calibrated 口径栅栏**新增 | 待核实第 1 条关闭（图像内数字除外）；**撤销一条合成引语**（「F1@1 falls to 0」＋「overall accuracy remains close to chance」两处不同上下文片段的误拼）并**更正摘要引文的 MGT 缩写**——均为直引形态错误，非数字错误 |

## 推翻记录（如适用）

本卡论断未被推翻。**但第 10 处推翻（`ai_detect` 字段名≠字段值）的教训已制度化为本卡纪律**：见卡首「第三个 🔑」。**本卡写作时刻意避免重蹈**——四支柱中每个数字都连口径引用，厂商自报与独立测评分列。

**全书推翻记录仍为 11 处（8 处外部 + 3 处自我），本卡不增加。**

## 关联卡片

- [claim-0050](claim-0050-ai-health-misinformation-supply.md)：供给爆炸（A 级）+ 制度层（标识办法）；本卡补其标题承认的「检测军备竞赛量化」缺口
- [claim-0030](claim-0030-diet-exercise-ratio.md)：第 10 处推翻（ai_detect）的教训来源；「字段名不是字段值」专段
- [claim-0063](claim-0063-linkrot-measurement.md)：双客户端链路纪律；archive.org 不可达与 cac.gov.cn 可达的测量一致性
- [claim-0048](claim-0048-china-ai-medical-regulation-liability.md)：中国 AI 医疗监管与责任归属；本卡支柱④的制度侧延伸
- [claim-0046](claim-0046-hallucination-confidence-calibration.md)：模型侧校准数据（军备竞赛的「攻方」质量维度）

## 仍待核实（关键缺口）

1. ~~**中文检测的系统测评**~~ ✅ **已关闭（2026-11-24，仅图像项除外）**：C-HAT-Bench 逐表提取完成——论文 Table 1/6/7/8/9 全部 **105 个检测器行**逐格入库（见证据节「中文侧独立基准」小节）；21 检测器构成 = **17 文本级（10 zero-shot + 7 supervised）+ 2 边界定位 + 2 跨域**；知网 AIGC 检测全文 **0 命中，不在 21 检测器之列** →「商用中文检测服务是否有独立学术测评」作为缺口随稿保留。**余留（仅图像）**：zhv2 的 5×5 跨域矩阵（Figure 6）与 IMBD 全部数字（Figure 9/10/11）仅存于图像，正文可引粒度止于观察句与 D.4 定性结论；如需逐格数字须人工读图。⚠️ 独立第三方性质说明保持：C-HAT-Bench 是学术基准（论文作者测试朱雀 v2），**非厂商自测**——这是「商用中文检测器有独立学术测评」的第一个实证。中文社交媒体零散实测仍为 D 级线索不入正文。
2. **OpenAI 一手核验**——订阅或浏览器人工访问 `openai.com/ai-text-classifier/`（403 页不绕过）；26%/9% 数字核验后升级引用级别，否则删数字留事由。
3. ~~**Krishna 全文百分比**~~ ✅ **已关闭（2026-11-16）**：经 ar5iv HTML 版取得全文（99.3→9.7 / 100→60 / 100→92 / 两轮后全部<50% 四组数字逐字入库）。⚠️ arXiv 官方 PDF 两次下载均损坏（XRef 表错），已如实记录。
4. ~~**清朗第一阶段（2026-07）官方原文**~~ ✅ **已关闭（2026-11-16）**：官方原文取得并逐字核实（含 600 余万条 / 1300 余商品 / 9 个数据集等次级摘要没有的细节），存档入库。**新增双计数口径栅栏**（见支柱④时间线）。
5. ~~**SynthID 全文细节**~~ ✅ **已关闭（2026-11-16）**：PMC 开放全文取得（方法学三层证据：大规模实况点赞率 + 小规模受控研究 + 困惑度/标准基准；TPR@FPR=1% 统一口径；rater preference 无显著差异引 Extended Data Table 1）。⚠️ 样本量等表格级细节在 Extended Data，未逐表提取——引用粒度止于「方法学已核实」。
6. **561 万构成拆分**——如有官方问答/记者会披露「涉健康」子集，补入第 5 章/第 35 章接口。
7. 全部存档页的 archive.org 快照（服务本网络持续不可达，待复测）。