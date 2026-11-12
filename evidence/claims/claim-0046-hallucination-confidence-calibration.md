---
id: claim-0046
title: 「它用同样的确定性说对的和错的」——校准证据只部分支持这句话，必须改写；但高风险场景的伤害证据是硬的
status: 有争议
level: B
chapters: [35]
created: 2026-11-12
verified: null
verifier: null
---

# claim-0046：医疗幻觉与自信度校准（截至 2026-11-12）

> **两层分离声明**：
> - **能力层**（某模型的 ECE 是多少、某模型会不会编造跑步记录）——**只在 2026-11-12 之前成立**，必须带模型名与版本。这一层衰减极快，2026 年的新模型校准已明显好于 2024 年。
> - **机制层**（聚合校准指标掩盖科室差异；自报置信度 ≠ 自由文本语气；健康建议错误不可回滚；厂商把「仅供参考」当免责）——**变化慢**，是本章真正要写的东西。
>
> ⚠️ **本卡的核心结论是：大纲里那句金句需要修订。** 见下方「论断原文」与「反方与局限」。

## 论断原文

抄自 `book/vol6/ch35-ai-coach.md`（`status: outline`），逐字未改：

> - 代码错了能回滚，健康建议错了不能
> - 高风险场景：禁忌症、药物相互作用、进食障碍识别、未成年人、孕期
> - AI 的自信语气与证据强度脱钩：它用同样的确定性说对的和错的
> - **核心句**：健康建议的错误不像代码错误能回滚

金句候选（第 109–110 行）：

> - "健康建议的错误不像代码错误能回滚。"
> - "它用同样的确定性说对的和错的。"

## 为什么重要

第 35 章第二节整节压在这条上，也是「AI 既是解药也是毒药」里「毒药」那一半的机理。如果「自信语气与证据强度脱钩」被证伪，本章就只剩「AI 偶尔会错」这种谁都知道的废话，第二节塌掉，第三节的「责任归属」也失去紧迫性。

反过来，如果把它写成「AI 完全不知道自己不知道」，那是**过度概括**，会被任何读过 2026 年校准文献的读者一眼击穿，损害全书可信度。**这张卡的价值恰恰在于它逼作者把金句改准确。**

## 证据

### 来源 1（B 级：校准的直接实证，模型版本最完整）

- 来源标题：Calibration of Self-Reported Confidence and Accuracy of Large Language Models in Medical Question Answering
- 发布方 / 作者：Boie SD, Reis F, Frey N, Grünewald E, Balzer F（德国柏林 Charité 医学院）；期刊 *Journal of Medical Systems* 2026 Jun 26;50(1):103
- 发布日期：2026-06-26
- URL / DOI：doi:10.1007/s10916-026-02430-0 ；PMID 42360536 ；PMCID PMC13309378
- 采集日期：2026-11-12（NCBI eutils `efetch.fcgi?rettype=abstract&retmode=text`）
- 存档：待补
- 证据级：B（大样本模型评测，非临床研究）
- 原文关键句（直引）：
  - "Mean ECE differed by model (Claude Sonnet 4.5 best: 0.06; Gpt-4o worst: 0.127) and varied across specialties (\"Skin\" best: 0.041; \"Social & Preventive Medicine\" worst: 0.141)."
  - "Our results demonstrate that high accuracy does not guarantee reliable uncertainty estimation."
  - "pooled metrics masked a threefold ECE increase between best- and worst-performing domains"
  - "larger models exhibit improved \"self-knowledge\", but uneven overconfidence persists"
- 方法学要点：
  - **被测模型（6 个，版本明确）**：**GPT-5、GPT-5-mini、GPT-5-nano、GPT-4o、Claude Sonnet 4.5、Gemini 2.5**
  - 题库：**MedMCQA**（医学多选题）
  - 规模：**12,000 条回答**
  - 指标：**ECE（Expected Calibration Error，期望校准误差）**——模型自报置信度与实际正确率之间的偏差，越小越校准
- 利益相关：作者声明无冲突；披露仅用 GPT-5 做语言润色。

**这条证据同时支持与反驳金句，必须两面都写：**
- **支持**：ECE 在科室之间差 **三倍**（0.041 → 0.141）；「高准确率不保证可靠的不确定度估计」；「不均匀的过度自信仍然存在」。也就是说，**在预防医学/社会医学这类与减肥科普高度重叠的领域，模型最不知道自己不知道**——而减肥伪科普恰恰主要发生在这个领域。
- **反驳**：Claude Sonnet 4.5 的平均 ECE 只有 **0.06**，这是**相当好的校准**。「用同样的确定性说对的和错的」作为对 2026 年前沿模型的全称判断，**不成立**。

### 来源 2（B 级：高风险场景——进食障碍，伤害证据最硬）

- 来源标题：Generative AI for Eating Disorders: Linguistic Comparison With Online Support and Qualitative Analysis of Harms
- 发布方 / 作者：Yim SH, Yoo DW, Polymerou A, Liu Y, Saha K；期刊 *International Journal of Eating Disorders* 2026 Mar;59(3):519-533
- 发布日期：2025-11-21（Epub）；纸刊 2026 年 3 月
- URL / DOI：doi:10.1002/eat.24604 ；PMID 41272925
- 采集日期：2026-11-12（NCBI eutils 摘要全文）
- 存档：待补
- 证据级：B（语言学对照 + 临床人员质性分析）
- 原文关键句（直引）：
  - "AI responses were generally longer, more polite, yet more repetitive and less creative than human responses."
  - "Qualitative analysis revealed themes of possible reinforcement of ED behaviors, implicit biases (e.g., favoring weight loss), and an inability to acknowledge contextual nuances-such as insensitivity to emotional cues and overgeneralized health advice."
  - "All AI chatbots produced responses containing harmful content, such as promoting ED behaviors or biases, to varying degrees."
- 方法学要点：
  - 人类对照组：疫情前 Reddit 进食障碍社区 **3634 条帖子、22,359 条回复**
  - **被测模型（4 个）**：**GPT、Gemini、Llama、Mistral**。⚠️ 摘要只给模型家族名，**具体版本号待核实**（需查全文 Methods）。
  - 量化：LIWC 8 个语言维度
  - 质性：**100 条 AI 回复由临床人员逐条分析**
- 利益相关：作者声明无（Saha K 为 Georgia Tech 研究者，长期从事在线健康社区研究）。
- **为什么这条对本章特别重要**：它测的不是「答错一道题」，而是**「语气礼貌、内容更长、看起来更专业，同时在强化进食障碍行为」**——这正是「看起来不像在卖东西/不像在害人」的隐蔽伤害。而且它点出了 **implicit bias: favoring weight loss（隐性偏向减重）**：在一个全社会都赞美减重的语境里，AI 会顺着这个偏见走。这与第 33 章（污名与道德叙事）直接呼应。

### 来源 3（D 级：真实产品里的自信编造，2026 年 5 月）

- 来源标题（原文）：Google's Fitbit Air is super comfortable, but its AI coach is already hallucinating
- 发布方 / 作者：Will Sattelberg，9to5Google
- 发布日期：2026-05-14 09:30 PT
- URL / DOI：**原文单篇 URL 待核实**。已核实存在的索引页 `https://9to5google.com/guides/fitbit-air/` 返回 HTTP 200 但为 JS 壳（248,912 字节，无正文），标题与日期读自该页的搜索引擎快照（采集 2026-11-12）。已检索关键词：`9to5google Fitbit Air AI coach hallucinating Sattelberg`、`Fitbit Air health coach fabricated run`。
- **可核实的中文转载（已 curl 取到全文，HTTP 200，32,494 字节）**：
  - 标题：谷歌 Fitbit Air 手环评测：AI 健康教练出现幻觉，虚构跑步记录
  - 发布方：新浪科技 / 市场资讯，来源标注「IT之家」
  - 发布日期：2026-05-15 14:25
  - URL：`https://finance.sina.cn/stock/jdts/2026-05-15/detail-inhxyccp3439676.d.html`
  - 采集日期：2026-11-12
- 存档：`/tmp/sina.html`（临时，待转入正式存档）
- 证据级：D（记者实测 / 公开内容抽样）
- 原文关键句（直引，中文转载）：
  - "IT之家 5 月 15 日消息，科技媒体 9to5Google 昨日（5 月 14 日）发布博文，在评测 Fitbit Air 健身手环时，发现内置付费 AI 健康教练 Health Coach 存在幻觉，存在虚构跑步记录情况。"
  - "不过该媒体记者 Will Sattelberg 在评测过程中，发现 Health Coach 虚构出一段并不存在的 5.2 英里跑步记录。在交互过程中 Health Coach 承认该记录是捏造的，但随后又把责任推回用户，暗示可能是用户自己没有记录这次跑步。"
- 第二篇同作者评测（**六英里**版本，2026-05-28 08:00，标题 "Review: Fitbit Air is a near-perfect fitness tracker with an imperfect AI Health Coach"）：
  - 中文转载 `https://m.zhiding.cn/article/3188763.htm`（至顶网，2026-05-29），直引："我对谷歌这款AI驱动的健身聊天机器人的第一印象并不好，主要原因是它凭空捏造了一次六英里跑步，并以此为基础为我制定了每日建议。"
  - 直引："就算这个功能完全免费，我也不确定自己能否接受每次收到"教练"的AI回复都需要仔细核查，以确保它没有依赖错误数据。当涉及到健康和健身这样私人的事情时，让一个聊天机器人随意捏造关于你的体重、身体状况或运动水平的信息，会让人感觉很奇怪，而这些信息如果不加甄别，很可能助长一些危险的健身或饮食趋势。"
- 利益相关：9to5Google 为科技媒体，评测机通常由厂商提供；记者无卖课/卖药利益。**这是本卡里唯一一条「AI 不卖课」语境下的伤害证据**——它说明即使没有商业推销动机，幻觉本身也会造成伤害。
- ⚠️ **归属注意**：两篇均为 Will Sattelberg 所写，**不得**把「六英里」那篇归给 Android Central 或其他媒体（未经核实）。

## 反方与局限

### 最强反对意见

1. **「AI 比很多水货教练靠谱，至少它不卖课」在幻觉这一节同样成立**：水货教练也会自信地说错（「深蹲膝盖不能过脚尖」「空腹有氧才燃脂」），而且他**有动机**说错——因为说错能卖课。AI 说错时**没有推销动机**。来源 3 的 Fitbit 案例里，AI 编造跑步记录不是为了让用户买什么，纯粹是能力缺陷。**动机上的差别是真实的，不能抹掉。**
2. **校准在快速改善**：来源 1 明确写 "larger models exhibit improved 'self-knowledge'"，Claude Sonnet 4.5 的 ECE 0.06 已经相当好。**「它用同样的确定性说对的和错的」这句话，对 2024 年的模型基本成立，对 2026 年的前沿模型是过度概括。** 正文若原样保留这句金句，会被证伪。
3. **PCMag 的反面实测**（2026-09-24，`https://www.pcmag.com/picks/the-best-fitness-trackers`，直引）："In testing, I found the Health Coach extremely responsive and adaptable to changing circumstances" → 同一个产品，不同评测者结论相反。单一记者的幻觉案例**不能外推为产品的普遍失败率**。

### 证据的局限

1. **ECE 是聚合指标**：来源 1 自己就承认 "pooled metrics masked a threefold ECE increase"。**平均校准好 ≠ 逐条回答可靠**，也 ≠ 在自由对话里的语气可靠。
2. **自报置信度 ≠ 语气确定性**：来源 1 测的是模型在多选题上**被要求报出的数字置信度**；金句说的是**自由文本里的语气**。这两者不是同一个量。**目前没有已核实的研究直接测量「LLM 健康建议的语言确定性与证据等级的相关性」**。已检索关键词：`LLM health advice linguistic certainty hedging evidence strength calibration`、`large language model overconfidence free text medical advice tone`。**结论：待核实**——金句的「语气」版本缺直接证据，只能靠来源 2（更长、更礼貌、更重复）与来源 3（编造后反怪用户）做间接支撑，且必须标为间接。
3. **MedMCQA 是考试题，不是真实咨询**：有标准答案、有选项、语境干净。真实用户问的是「我膝盖响还能不能深蹲」，没有选项。
4. **来源 2 的模型版本不明**，且人类对照组是**疫情前的 Reddit 社区**——与 2026 年的 AI 不同期，属跨期比较。
5. **来源 3 是 n=1 的记者实测**，无失败率统计，无重复实验。
6. **未覆盖的高风险场景**：大纲列了「禁忌症、药物相互作用、未成年人、孕期」，本卡**只拿到了进食障碍**一项的直接证据。其余三项**待核实**。已检索关键词：`LLM drug interaction advice accuracy evaluation 2026`、`ChatGPT contraindication exercise prescription safety audit`、`LLM pediatric adolescent health advice safety evaluation`、`large language model pregnancy advice accuracy study`。已有线索（仅 esummary 核实标题，摘要未读，不得引用数字）：PMID 41710315（孕期膳食指导，DeepSeek-R1 vs ChatGPT-4.0）、PMID 41135437（CKD 饮食计划）。

### 建议的正文修订（供作者决策，本卡不代改大纲）

- 保留：**"健康建议的错误不像代码错误能回滚。"** —— 这句是**机制层**判断，不依赖任何模型能力，跨周期成立。
- 修订：**"它用同样的确定性说对的和错的。"** → 建议改为类似「**它的语气从不告诉你它有多不确定；平均看起来校准良好，但在预防医学这类领域，它的自信最不可信。**」并挂来源 1 的 ECE 0.041 vs 0.141 与「pooled metrics masked a threefold ECE increase」。
- 补一句诚实的反方：**它至少不靠说错话赚钱。**（接 claim-0052）

### 什么情况下这条论断不成立

- 若 2027 年后的模型在**自由文本健康建议**上做到「语气确定性随证据强度单调变化」，且有公开评测 → 修订后的金句也需再改。
- 若出现专门针对禁忌症/药物相互作用的评测且失败率极低 → 「高风险场景」清单需收窄。
- 若厂商把健康建议全部改为「检索 + 引用可核查来源」的架构（Google Health 已宣称「所有健康相关结论均标注来源」，见 claim-0051），幻觉率可能大幅下降 → 需重测。

## 核查记录

| 日期 | 核查人 | 动作 | 结论 |
|---|---|---|---|
| 2026-11-12 | AI 检索 + 待人工复核 | 建卡；NCBI eutils 核实来源 1、2 的完整题录与摘要直引 | 有争议 |
| 2026-11-12 | AI 检索 | curl 核实新浪/IT之家转载全文（HTTP 200, 32,494 字节），确认 5.2 英里与「反怪用户」直引 | D 级证据成立 |
| 2026-11-12 | AI 检索 | 判定金句「它用同样的确定性说对的和错的」对 2026 年前沿模型属过度概括 | 建议修订，待作者决策 |
| 2026-11-12 | AI 检索 | 标记 9to5Google 单篇 URL、来源 2 模型版本号、语气确定性研究为待核实 | 待核实 |

## 推翻记录（如适用）

- 原论断：「它用同样的确定性说对的和错的。」（大纲金句候选）
- 推翻日期：**未推翻，但已标记为「需限定」**（2026-11-12）
- 推翻理由与证据：Boie 2026（doi:10.1007/s10916-026-02430-0）显示 Claude Sonnet 4.5 平均 ECE 仅 0.06，且「larger models exhibit improved 'self-knowledge'」。全称判断不成立；但科室间三倍差异与「高准确率不保证可靠不确定度」支持**限定版**论断。
- 正文如何修订：见上方「建议的正文修订」。**最终决定权在作者，本卡不修改大纲文件。**