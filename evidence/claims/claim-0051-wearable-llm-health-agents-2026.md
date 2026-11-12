---
id: claim-0051
title: 可穿戴 + LLM 健康教练在 2026 年已是真实付费产品，考试分数可超过人类专家、数值题准确率 84%；但关键能力研究几乎全由 Google 资助，且尚无已完成的随机对照疗效试验
status: 有争议
level: B
chapters: [35]
created: 2026-11-12
verified: null
verifier: null
---

# claim-0051：可穿戴 + LLM agent 健康应用的现状（截至 2026-11-12）

> **两层分离声明**：
> - **能力层**（PH-LLM 考多少分、PHIA 数值题准确率多少、某产品某月上线某功能）——**只在 2026-11-12 之前成立**，必须带模型名、版本、发表年份。**这是全章衰减最快的一层。**
> - **机制层**（能力证据的生产者与被评价产品的所有者是同一家公司；考试分数 ≠ 健康结局；厂商用「不属于医疗设备」自我豁免；订阅制把「教练」变成留存工具）——**变化慢**，是本章真正要写的东西。
> - ⚠️ **本卡最重要的诚实点：支撑「AI 健康教练能力」的两篇顶刊论文，作者全部是 Alphabet 员工，研究全部由 Google LLC 资助。这不是指控造假，而是必须披露的结构性利益相关。**

## 论断原文

抄自 `book/vol6/ch35-ai-coach.md`（`status: outline`），逐字未改：

> | 可穿戴数据解读 | 部分可用 | 数据噪声 + 过度解读 |
> | 陪伴与问责 | 可模拟 | 关系真实性问题，见第10章对照 |

以及大纲第 92–93 行的最强反对意见与回应方向：

> - **最强反对意见**："AI 进步很快，你今天写的能力边界明年就过时了。"
>   - 回应方向：承认时效性，所有评估注明日期；本章重点不是能力清单，而是**责任与激励结构**——这部分变化慢

## 为什么重要

第 35 章能力清单里「可穿戴数据解读」与「陪伴与问责」两行压在这条上。它也是「AI 进步很快，你写的边界明年就过时」这一最强反对意见的**正面战场**：本卡必须证明作者知道最新进展到什么程度，然后再说明为什么责任与激励结构仍然成立。

如果这条错了（比如其实还没有真实产品、或其实已有 RCT 证明疗效），第 35 章要么显得落后，要么显得过度悲观。

## 证据

### 来源 1（B 级：PH-LLM，Nature Medicine，考试分数超过人类专家）

- 来源标题：A personal health large language model for sleep and fitness coaching
- 发布方 / 作者：Khasentino J, Belyaeva A, Liu X, 等（**Google Research**）；期刊 *Nature Medicine* 2025 Oct;31(10):3394-3403
- 发布日期：2025-08-14（Epub）；纸刊 2025 年 10 月
- URL / DOI：doi:10.1038/s41591-025-03888-0 ；PMID 40813712 ；PMCID PMC12532688
- 采集日期：2026-11-12（NCBI eutils `efetch.fcgi?rettype=abstract&retmode=text`）
- 存档：待补
- 证据级：B（模型评测 + 案例评分，非临床结局试验）
- 原文关键句（直引）：
  - "PH-LLM achieved scores that exceeded a sample of human experts on multiple-choice examinations in **sleep medicine (79% versus 76%) and fitness (88% versus 71%)**."
  - "In a comprehensive evaluation involving **857 real-world case studies**, PH-LLM performed similarly to human experts for fitness-related tasks and improved over the base Gemini model in providing personalized sleep insights."
- 方法学要点：
  - **被测模型**：**PH-LLM = 在聚合的日粒度数值传感器数据上微调的 Gemini**（⚠️ 基座 Gemini 的具体版本号待核实，摘要未给）
  - 输入：可穿戴设备的**日粒度聚合数值数据**（睡眠、健身）
  - 评测一：睡眠医学与健身的**多选题考试**，与人类专家样本对比
  - 评测二：**857 个真实案例**，健身任务与人类专家表现相当，睡眠个性化洞察优于基座 Gemini
- 利益相关（**原文直引，必须披露**）："**This study was funded by Google LLC. All authors are employees of Alphabet and may own stock as part of the standard compensation package.**"

**正确读法**：79% vs 76%、88% vs 71% 是**多选题考试分数**，不是「治好了多少人的失眠」或「让多少人减了肥」。**考试能力 ≠ 教练能力 ≠ 健康结局。** 而且 fitness 项 88% vs 71% 的差距（17 个百分点）远大于 sleep 项（3 个百分点），说明**优势高度依赖任务类型**。

### 来源 2（B 级：PHIA agent，Nature Communications，84% 数值准确率 = 16% 错误率）

- 来源标题：Transforming wearable data into personal health insights using large language model agents
- 发布方 / 作者：Merrill MA, Paruchuri A, Rezaei N, 等（**Google Research**）；期刊 *Nature Communications* 2026 Jan 12;17(1):1143
- 发布日期：2026-01-12
- URL / DOI：doi:10.1038/s41467-025-67922-y ；PMID 41526380 ；PMCID PMC12855967
- 采集日期：2026-11-12（NCBI eutils 摘要全文）
- 存档：待补
- 证据级：B
- 原文关键句（直引）：
  - "we create and share two benchmark datasets with **over 4000 health insights questions**. A **650-hour human expert evaluation** shows that PHIA significantly outperforms a strong code generation baseline, achieving **84% accuracy on objective, numerical questions** and, for open-ended ones, earning **83% favorable ratings** while being twice as likely to achieve the highest quality rating."
- 方法学要点：
  - **被测系统**：**PHIA**（Personal Health Insights Agent）= 多步推理 + 代码生成 + 信息检索
  - 基准：两个公开数据集，**超过 4000 道健康洞察问题**
  - 评测：**650 小时人类专家评估**
  - 对照：一个强代码生成基线
- 利益相关：**由 Google LLC 资助；全部作者为 Alphabet 员工**（同来源 1 的披露结构）。
- ⚠️ 基座模型版本待核实（摘要未给）。

**这条证据的双面性（本章关键）**：
- **正面**：84% 的客观数值题准确率、83% 的开放题好评率、650 小时专家评估——**这是严肃的、规模很大的评测，不是营销话术。**
- **反面**：**84% 意味着每 6 道关于你身体的数值问题里，就有 1 道答错。** 而且这是**有标准答案的客观题**，不是真实对话里的模糊问题。**「部分可用」这个判断，被这个数字精确地量化了。**

### 来源 3（B 级：唯一已注册的大规模 RCT——但截至 2026-11-12 尚无结果）

- 来源标题：Design and rationale of the my heart counts cardiovascular health study: a large-scale, fully digital biobank, and randomized trial of large language model-driven coaching of physical activity
- 发布方 / 作者：Schmiedmayer P, Johnson A, Schuetz N, 等（**Stanford**）；期刊 *American Journal of Preventive Cardiology* 2026 Mar 18;28:101565（eCollection 2026 Aug）
- 发布日期：2026-03-18
- URL / DOI：doi:10.1016/j.ajpc.2026.101565 ；PMID 42395096 ；PMCID PMC13325983
  - 预印本：medRxiv 2026-03-03，doi:10.64898/2026.03.02.26347447，PMID 41867233，PMCID PMC13001391
- 采集日期：2026-11-12（NCBI eutils 摘要全文）
- 存档：待补
- 证据级：B（**研究方案/设计论文，不是结果论文**）
- 原文关键句（直引）：
  - "**TRIAL STATUS: Recruitment commenced in March 2026 and is ongoing.**"
- 方法学要点：
  - 目标样本 **N = 15,000** 名成年人（美国 + 英国）
  - 内嵌**随机交叉设计**：基于**跨理论模型（Transtheoretical Model of Change）**定制的 LLM 提示 vs 通用提示
  - **主要终点：每日步数的变化**；统计方法：混合效应模型
- 利益相关：资助来自 ADA（美国糖尿病协会）、AHA（美国心脏协会）、Robert A Winn Excellence in Clinical Trials、Stanford Center for Digital Health、British Heart Foundation。**非厂商资助——这是本卡里唯一一条利益结构干净的能力/疗效证据来源。**
- ⚠️ **截至 2026-11-12，本试验没有公开疗效结果。** 已检索关键词：`my heart counts Stanford LLM coaching results step count 2026`、`Schmiedmayer my heart counts randomized trial results published`。**结论：待核实（结果未发表）。正文不得写「已证明 LLM 教练能增加步数」。**

**这条证据为什么重要**：它说明**学界自己知道「考试分数」不够**，正在做 15,000 人的 RCT。**在结果出来之前，任何「AI 教练有效」的断言都缺最后一环。** 这是本章「时效性」论点最有力的例证：书写在 2026 年 11 月，而关键试验正在招募中。

### 来源 4（B 级：陪伴与问责——LLM agent 能提升参与度，但只有一种人格有效）

- 来源标题：Large Language Model Agents for Improving Engagement with Behavior Change Interventions: Application to Digital Mindfulness
- 发布方 / 作者：Kumar H, Yoo S, Bernuy AZ, 等（Toronto / McMaster / Northwestern）；期刊 *Proceedings of the ACM on Human-Computer Interaction* 2025 Nov;9(7):CSCW438
- 发布日期：2025-10-16（Epub）；纸刊 2025 年 11 月
- URL / DOI：doi:10.1145/3757619 ；PMID 41768145 ；PMCID PMC12945337
- 采集日期：2026-11-12（NCBI eutils 摘要全文）
- 存档：待补
- 证据级：B（两项随机实验）
- 原文关键句（直引）：
  - "Both agents enhanced users' intentions to practice mindfulness. However, **only the information-providing LLM agent, featuring a friendly persona, significantly improved engagement with the exercises**."
- 方法学要点：两项随机实验——单次会话 **502 名众包工人**；三周纵向 **54 名参与者**。
- 利益相关：学术团队，无厂商资助披露。
- **对大纲「陪伴与问责 | 可模拟」的支撑与限定**：「可模拟」成立（意图提升），但**「模拟得像朋友」并不自动带来行为改变**——只有「提供信息 + 友好人格」的组合显著改善了实际参与。**共情本身不是有效成分，信息 + 共情才是。** 这与 claim-0045 来源 1 的「lacked cultural competence and emotional intelligence」形成有趣对照。
- ⚠️ 领域是**正念**，不是减重/运动。**外推到健身教练需谨慎。**

### 来源 5（C/D 级：真实产品与厂商自我豁免——Oura 官方页）

- 来源标题：Why Oura（中文页）
- 发布方 / 作者：**Oura Health Oy**（© 2026 Oura Health Oy）
- 发布日期：页面未标注具体日期，版权年份 2026
- URL / DOI：`https://ouraring.com/zh-CN/why-oura`
- 采集日期：2026-11-12（WebFetch 已取，所需法律脚注在返回部分内）
- 存档：待补
- 证据级：C（厂商公开法律声明）/ D（营销页）
- 原文关键句（直引）：
  - **脚注 2**："Counsel 体验适用于美国 43 个州的 Oura 会员。该服务暂不支持阿肯色州、哥伦比亚特区、堪萨斯州、密西西比州、罗德岛州、华盛顿州、西弗吉尼亚州、威斯康星州用户。Medical AI 聊天功能已包含在 Oura 会员权益内。Counsel 医师问诊与诊疗服务需额外付费。用户可以自愿选用本服务。诊疗服务由 Counsel 持证医师提供，并非由 Oura 提供。**Counsel 的 AI 提供分诊支持，不能替代临床判断。**该体验专注于日常医疗护理需求，不适用于急症救治。**Oura Ring 与 Advisor 均不属于医疗设备，不可用于诊断、治疗、治愈、监测或预防各类病症。**"
  - **脚注 1**："基于 2026 年对 **3,501 名 Oura 会员使用 Oura Ring 30 天后的调查**。"
  - 营销准确率宣称：**99% 心率精准度**（vs ECG 的 r²）、**98% HRV**、**94% 排卵检测**（vs 排卵预测试纸）、**79% 四阶段睡眠分期准确度**
  - 规模宣称："超过 500 万 全球会员"、"超过 50 位博士"、"5 代演进"、"12+ 年的经验与研究"、追踪"超过 50 项健康指标"
  - 隐私承诺："我们绝不会出售你的数据，也绝不会在未经同意的情况下分享你的数据。"
- 利益相关：**Oura 靠卖戒指与会员订阅获利。这是营销页面。**
- **两个关键机制点**：
  1. **「86% 的 Oura 会员感受到自身健康状况有所改善」的真相**：脚注 1 显示它是 **3,501 名会员戴了 30 天后的自报问卷调查**。**不是 RCT，没有对照组，没有客观终点，且由厂商自己采集。** 这是「厂商证据」与「临床证据」区别的教科书案例。
  2. **「不属于医疗设备」的自我豁免**：与 claim-0048 来源 2 的 NMPA 分类原则（非医疗器械数据 → 不作为医疗器械管理）**结构完全一致**。**中美两地的消费级 AI 健康产品，都靠「我不诊断」这句话站在器械监管之外。** 这是机制层，跨周期成立。
- ⚠️ **待核实**：Oura 女性健康专用 LLM 的发布时间存在冲突（微博转载文章日期 2026-02-25 vs 163.com 文章 2026-05-30 称「今年4月」）；官方博客 `https://ouraring.com/blog/womens-health-ai-model/` **未直接核实**。已检索关键词：`Oura womens health AI model launch date 2026 official blog`。**本卡不引用该产品发布月份。**
- ⚠️ 营销准确率宣称（99%/98%/94%/79%）的原始验证文献：页面脚注指向 `https://ouraring.com/blog/zh-CN/accuracy-of-finger-worn-wearables/`、`https://ouraring.com/blog/zh-CN/how-accurate-is-oura/`、`https://pubmed.ncbi.nlm.nih.gov/39889300/`、`https://doi.org/10.3390/s21134302`。**本卡未逐一核实这些原始文献 → 这四个百分比标注为「厂商宣称，原始文献待核实」，不得作为已核实数字进正文。**

### 来源 6（C/D 级：真实产品——Google Health Coach / Fitbit Air）

- 来源标题：（亿邦动力网报道）
- 发布方 / 作者：亿邦动力（ebrun.com）
- 发布日期：URL 日期段 20260624，正文标注 2026-06-29（⚠️ 不一致，**待核实**）
- URL / DOI：`https://www.ebrun.com/20260624/684481.shtml`
- 采集日期：2026-11-12
- 存档：待补
- 证据级：D（二手行业媒体）
- 原文关键句（直引）：
  - "该功能从2025年10月启动公开测试，近50万用户参与测试，累计收集超100万条反馈，2026年5月正式推送优化版本。"
  - "优化后的版本支持自定义界面布局、好友运动排行榜，AI回复内容精简30%，**所有健康相关结论均标注来源**，多为临床研究或权威健康机构内容。"
  - "**功能不会给出任何疾病诊断结论，所有建议最终都会提示用户咨询专业医疗人员。**"
  - "用户可自愿上传个人医疗记录用于补充分析维度，上传需要通过CLEAR完成身份核验，并定期更新授权权限。"
  - "**用户健康数据默认不会被用于谷歌AI模型训练，也不会被用于谷歌定向广告业务。**"
- 交叉印证（The Verge 评测经 CSDN 转载 `https://m.blog.csdn.net/techforward/article/details/162259044`，2026-06-24，直引）："自 2025 年 10 月以来，已有近 50 万人参与了该功能的测试，谷歌表示在去年推出改进版之前，收到了超过 100 万条反馈"；缺点："AI 健康教练需用户投入大量精力才能发挥最佳效果"。
- ⚠️ **Google 官方博客 URL 待核实**。已检索关键词：`site:blog.google Fitbit Air Google Health Coach`、`Google Health Coach general availability May 2026 official announcement`、`Fitbit app renamed Google Health official blog`。
- ⚠️ **产品时间线与价格存在冲突，全部待核实**：
  - App 更名日期：2026-05-07 vs 2026-05-19（两个二手来源不一致）
  - Google Health Premium 年费：US$99 vs US$100
  - 已核实的部分：2025-10-28 美国 Fitbit Premium 公开预览（Android 先行）；Fitbit Air 售价 US$99.99（特别版 $129.99）；2026-05-26 开售；月费 US$9.99。**这些均来自二手来源，官方原文未取到。**
- **实地幻觉证据（D 级，已核实中文转载全文）**：见 claim-0046 来源 3。9to5Google 记者 Will Sattelberg 2026-05-14 发现 Health Coach **虚构 5.2 英里跑步记录**，承认捏造后**反怪用户漏记**；2026-05-28 第二篇评测称**凭空捏造六英里跑步**并据此制定每日建议。新浪/IT之家转载 `https://finance.sina.cn/stock/jdts/2026-05-15/detail-inhxyccp3439676.d.html`（2026-05-15，已 curl 核实 HTTP 200 / 32,494 字节）。
- **反面实测（必须一并呈现）**：PCMag `https://www.pcmag.com/picks/the-best-fitness-trackers`（2026-09-24，直引）："In testing, I found the Health Coach extremely responsive and adaptable to changing circumstances"；续航 "just over eight full days"。TechRadar `https://www.techradar.com/health-fitness/fitness-trackers/google-fitbit-air-review`（2026-06-05，直引）："…but its messy AI-powered app holds it back from greatness"。
- 利益相关：Google 靠卖硬件 + 订阅获利；评测媒体通常收到厂商送测机。

### 来源 7（B 级交叉验证：16 周端侧姿态估计 + 运动处方，有身体结局）

见 **claim-0047 来源 2**（Heo S 等，*Healthcare* 2026;14(4):482，doi:10.3390/healthcare14040482，PMID 41753995）。16 周、MediaPipe、216 入组 / 146 完成、深蹲 1RM +4.39 kg（d=1.148）、体脂 −2.92%（d=−1.373）。**单臂、年轻健康男性为主、脱落 32.4%、资助声明有勘误。** 本卡不重复展开，仅作为「已有身体结局证据」的交叉引用。

## 反方与局限

### 最强反对意见

1. **「AI 比很多水货教练靠谱，至少它不卖课」在这一节最有说服力**：
   - PH-LLM 在健身多选题上 **88% vs 人类专家 71%**（来源 1）。**一个不卖课的模型，在知识考试上比人类专家组高 17 个百分点。**
   - PHIA 经过 **650 小时人类专家评估**、**4000+ 题基准**（来源 2）。水货教练的知识水平**从来没有被这样测过**。
   - Google Health Coach **近 50 万人参与公测、100 万条反馈**（来源 6）——这是真实规模的使用，不是 demo。
   - Oura 有 **500 万会员**（来源 5，厂商宣称）。
   - **对请不起私教、住在大城市以外的人，这是第一次有一个「随时在、不评判、不推销」的健康咨询入口。** 这个增益是真实的，本章必须写足。
2. **「AI 进步很快，你写的边界明年就过时」——这条反对意见是对的，本卡承认**：
   - 来源 1（2025-08）→ 来源 2（2026-01）→ 来源 3（2026-03 开始招募）→ 来源 6（2026-05 正式推送），**九个月内能力与产品形态都在变**。
   - **所以本章的重点必须放在责任与激励结构上**（claim-0048 / 0049 / 0052），能力清单只作为带日期的快照。

### 证据的局限

1. **利益结构高度集中**：来源 1、2 是**支撑「AI 健康教练能力」的两篇最权威论文**，**全部由 Google LLC 资助、全部作者为 Alphabet 员工、可能持股**。而 Google 正是 Fitbit / Google Health Coach 的所有者（来源 6）。**评价者与被评价产品的所有者是同一家公司。** 这不等于造假，但**正文必须披露**，且不能把这两篇当作独立第三方验证。
2. **考试分数 ≠ 健康结局**：来源 1 的多选题、来源 2 的有标准答案的数值题，**都不是「用了之后人变健康了吗」**。
3. **84% = 16% 错误率**（来源 2）：这是能力边界的硬数字，**且是在客观题上**。真实对话里的问题更模糊，错误率可能更高（**推断，E 级，无数据**）。
4. **唯一的非厂商 RCT 尚无结果**（来源 3）：截至 2026-11-12 仍在招募。**「AI 教练能改善健康行为」目前没有被已完成的随机对照试验证明。**
5. **厂商自报数据的性质**（来源 5）：86% 改善 = 30 天自报问卷，n=3,501，无对照，厂商自采。**99%/98%/94%/79% 的原始文献未核实。**
6. **产品事实几乎全靠二手来源**（来源 6）：Google 官方博客 URL 未取到；App 更名日期与年费存在冲突。**本卡不把这些当已核实事实。**
7. **中国本土产品完全空白**：**华为运动健康 / 小米健康 / Keep 的 AI 教练，本卡没有任何已核实证据。** 已检索关键词：`华为 运动健康 AI 教练 2026 功能`、`Keep AI 教练 上线 2026`、`小米 健康 AI 助手 大模型`、`Huawei Health AI coach 2026`、`Keep AI personal trainer launch`。**结论：待核实——这是面向中国读者时最严重的缺口，因为本书读者用的多半是这些产品，不是 Fitbit。**
8. **WHOOP 相关数据全部不可用**：本卡检索到的 WHOOP Coach / WHOOP 5.0 / Series G 估值 101 亿美元 / 250 万会员 / 2025 首次正现金流等，**全部来自头条号/投黑马等二手自媒体，未核实 → 不引用**。
9. **明确排除的伪证据来源（不得引用）**：
   - `https://healthcarediscovery.ai/whoop-5-recovery-strain-hrv-tracker/`（SEO 站，声称 WHOOP 5.0 / Oura Ring 5 / Garmin CIRQA / Fitbit Air 的「同行评议验证：均未找到」——**该站本身无资质，其「未找到」不等于「不存在」**）
   - `https://airmore.ai/best-ai-health-apps.html`（SEO 列表文）
   - 某 CSDN 博文声称「Nature 子刊 2026，深蹲追踪误差 15–30%」——**无法溯源，不采用**
   - 某腾讯云博文声称「npj Gut and Liver，48 个 LLM，300 题，Brier 0.15–0.2」——**无法溯源，不采用**
10. **来源 4 的领域外推**：正念 ≠ 健身。

### 什么情况下这条论断不成立

- 若 My Heart Counts（来源 3）发表结果且显示 LLM 教练显著增加步数 → 「尚无 RCT 证据」需更新为「已有 RCT 证据」，本卡能力层升级。
- 若出现非厂商资助的独立评测复现 PH-LLM / PHIA 的分数 → 利益结构局限减轻。
- 若 2027 年模型在数值题上准确率 > 98% → 「16% 错误率」需要重测，「部分可用」可能升级为「大部分可用」。
- 若中国厂商产品被系统评测 → 第 7 条缺口补齐，本卡需大幅扩写。

## 核查记录

| 日期 | 核查人 | 动作 | 结论 |
|---|---|---|---|
| 2026-11-12 | AI 检索 + 待人工复核 | 建卡；NCBI eutils 核实来源 1/2/3/4 的完整题录、摘要直引与资助声明 | 有争议 |
| 2026-11-12 | AI 检索 | WebFetch 取 Oura 官方中文页，核实脚注 1（3,501 人 30 天调查）与脚注 2（不属于医疗设备 / 不能替代临床判断 / 43 州） | 已核实（厂商自述） |
| 2026-11-12 | AI 检索 | curl 核实新浪/IT之家转载的 Fitbit 幻觉报道全文 | D 级证据成立 |
| 2026-11-12 | AI 检索 | 判定来源 1/2 的 Google 资助 + 全员 Alphabet 雇员为必须披露的结构性利益相关 | 已披露 |
| 2026-11-12 | AI 检索 | 标记 Google 官方 URL、产品时间线/价格冲突、Oura 准确率原始文献、Oura 女性健康 LLM 发布月份、中国本土产品为待核实 | 待核实 |
| 2026-11-12 | AI 检索 | 明确排除 4 个不可溯源的 SEO/博客来源 | 不采用 |

## 推翻记录（如适用）

- 原论断：（暂无）
- 推翻日期：（暂无）
- 推翻理由与证据：（暂无）
- 正文如何修订：（暂无）