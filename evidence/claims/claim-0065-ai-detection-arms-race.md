---
id: claim-0065
title: AI 检测军备竞赛量化补齐：厂商自研检测器自认「准确率低」下架、7 款检测器对中国英语学习者作文平均误报 61.3%、共享基准上「容易被骗」、监管侧单季清理 561 万条——检测的四大证据支柱（学术 × 基准 × 自我承认 × 监管）
status: 待核实
level: B
chapters: [35]
created: 2026-11-16
verified: null
verifier: null
---

# claim-0065：检测军备竞赛的四个量化支柱——以及第 10 处推翻的教训如何写进证据纪律

> ⚠️ **本卡为 AI 辅助检索 + 开放全文逐字取证，状态保持「待核实」。** 按 [EDITORIAL.md](../../EDITORIAL.md) 第七节，须人工复核签字后方可标为「已核实」。
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
- 直引：recursive paraphrasing attack "can **significantly reduce detection rates**, it only slightly degrades text quality in many cases"；另证明**欺骗攻击（spoofing）**可行——攻击者可让检测器把**人类文本判成 AI**，带来「reputational risks for LLM developers」
- ⚠️ **具体百分比（如「检测率降至个位数」）在正文/图表里，本次仅取得摘要 → 不得引用具体百分比，只引「显著降低」**。待全文核实后升级。

### 支柱 ④（监管实测：中央网信办三份官方原文，cac.gov.cn 直连 200）

| 通报 | 日期 | 官方 URL | 关键数字（原文逐字） |
|---|---|---|---|
| 「清朗·整治AI应用乱象」第二阶段 | 2026-09-02 | `www.cac.gov.cn/2026-09/02/c_1790099041364574.htm` | 「**累计清理违法违规信息561万余条，查处账号4.9万余个，处置违规网站、应用程序等2400余个**」 |
| 「清朗·整治AI应用乱象」部署 | 2026-04-30 | `www.cac.gov.cn/2026-04/30/c_1779289298718765.htm` | 专项行动部署；标识要求（「标识」9 命中） |
| 「清朗·整治科普健康类网络谣言」 | **2026-11-06** | `www.cac.gov.cn/2026-11/06/c_1795719652932799.htm` | **为期 2 个月**；四类重点整治（见下） |

- 存档：三份均入库（[`cac-20260902-qinglang-ai-stage2.html`](../data/cac-20260902-qinglang-ai-stage2.html) 19,763 B MD5 `33d2d2e40e772913d1f249438a0bd4e6`；[`cac-20260430-qinglang-ai-deploy.html`](../data/cac-20260430-qinglang-ai-deploy.html) 19,498 B MD5 `604af5834559fe0dbcc2988c9b66886e`；[`cac-20261106-qinglang-health-rumor.html`](../data/cac-20261106-qinglang-health-rumor.html) 18,195 B MD5 `f8ab713469849391706260f23c78db02`）
- 🔑 **2026-11-06 通知与本书论点的直接咬合（原文直引）**：
  > 「**借审美焦虑制造『黄连素是减肥神药』等运动、减重类谣言**」——监管文件**点名**「审美焦虑」是谣言制造的驱动机制，并点名**减重类谣言**。第 5 章「焦虑不是副作用，是产品」与第 35 章在此获得监管侧文本。
  > 「**（三）滥用人工智能技术，生成健康科普谣言**」——四子类：**批量生成同质化**涉健康文案；**AI 换脸换声盗用知名专家形象**虚假科普带货；**诱导 AI 大模型生成虚假「死亡率」「存活率」**等不实科学数据；**AI 伪造权威通报、官方健康提示**。
  > 「冒充医疗卫生健康等领域专业人士……打造所谓『国家一级保健师』『国家一级营养师』」——伪专业身份摆拍。
- ⚠️ **「561 万」的口径边界**：这是**全平台累计清理的违法违规信息总数**（含 AI 生成与非 AI），**不是「AI 检测器的准确率」，也不是「AI 内容占比」**。正文不得从 561 万反推任何比例。它的正确用法是证明：**大规模机器初筛 + 处置已在生产运行**。
- ⚠️ **时间线（次级来源补充，待官方逐条核验）**：2025-04「清朗·整治AI技术滥用」（处置违规 AI 产品 3,500 余款）→ 2025-09-01《人工智能生成合成内容标识办法》施行（见 [claim-0050](claim-0050-ai-health-misinformation-supply.md)）→ 2026-04 AI 应用乱象专项启动 → 2026-07 第一阶段通报（1.4 万余款 / 2.6 万余账号，次级转述）→ 2026-09-02 第二阶段（本卡一手核实）→ 2026-11-06 健康谣言专项（本卡一手核实）。

### 支柱+（防守方反击：SynthID-Text，Nature 2024）

- 来源：Dathathri S, See A, et al. **Scalable watermarking for identifying large language model outputs.** *Nature* 2024;634(8035):818-823. DOI `10.1038/s41586-024-08025-4`（2024-10-23）｜PMID 39443777｜PMCID PMC11499265
- 直引（摘要）：
  > "Here we describe **SynthID-Text**, a **production-ready** text watermarking scheme that preserves text quality and enables high detection accuracy … we conducted a **live experiment that assessed feedback from nearly 20 million Gemini responses**, again confirming the preservation of text quality."
- ⚠️ **利益相关（逐字引用自 PubMed 利益声明）**："Work funded and performed by **Google DeepMind** … have **filed patent applications** … relating to the SynthID-Text watermarking method."
- 🔑 **与第 35 章既有纪律咬合**：PH-LLM/PHIA 的 Google 资助披露已在 ch35（「批判者的证据也来自被批判的一方」）；SynthID 同样处理——**水印能力的最硬证据恰好出自生成方自己**。**水印≠检测对手方文本**：SynthID 只能检测带自家水印的输出，这一点正文必须写明，不得写成「AI 文本检测已解决」。

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
2. **语言边界**：支柱 ②③ 的测评对象全部是**英文**。**中文检测的独立系统测评本书未取得**——这对一本中文书是实质性缺口，已列入待核实第 1 条。**不得把英文测评数字直接套到中文内容上。**
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

1. **中文检测的系统测评**——本卡全部学术证据为英文场景。检索 `中文 AIGC 检测 准确率 基准`、CNKI/万方「AIGC 文本检测 评测」，优先找有公开数据集的中文学术测评。
2. **OpenAI 一手核验**——订阅或浏览器人工访问 `openai.com/ai-text-classifier/`（403 页不绕过）；26%/9% 数字核验后升级引用级别，否则删数字留事由。
3. **Krishna 全文百分比**——arXiv PDF（`arxiv.org/pdf/2303.11156`）取得后补「检测率降至 X%」级引用。
4. **清朗第一阶段（2026-07）官方原文**——「1.4 万余款 / 2.6 万余账号」目前为次级转述，官方页 URL 待定位（cac.gov.cn 列表页 2026-07 段逐条核对）。
5. **SynthID 全文细节**——人工 side-by-side 评分的样本量与流程（PMCID PMC11499265 开放）。
6. **561 万构成拆分**——如有官方问答/记者会披露「涉健康」子集，补入第 5 章/第 35 章接口。
7. 全部存档页的 archive.org 快照（服务本网络持续不可达，待复测）。