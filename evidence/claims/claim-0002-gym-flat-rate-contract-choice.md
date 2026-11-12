---
id: claim-0002
title: 健身包月合约的实际出席率远低于盈亏平衡点，消费者高估了未来的自己
status: 待核实
level: B
chapters: [2]
created: 2026-11-12
verified: null
verifier: null
---

# claim-0002：健身包月合约的实际出席率远低于盈亏平衡点，消费者高估了未来的自己

> ⚠️ **AI 辅助检索建卡（EDITORIAL §7）。** 本卡的全部数字与引文由 AI 检索并逐字比对原始 PDF 提取，
> 但**尚未通过人工核查签字**（`verifier: null`）。在人工核查通过前，第 02 章正文引用本卡须标注"待核实"。
> 引文说明：原始 PDF 为双栏排版，`pdftotext` 输出存在左右栏交错；下文引文已按语义还原为连续句子，
> 还原过程未改动任何词与数字。人工核查时请对照 PDF 原文复核。

## 论断原文

> 在美国三家健身俱乐部 7,752 名会员、长达三年的逐日刷卡记录里，选择月费超过 70 美元包月合约的人，平均每月只来 4.3 次；他们为每一次实际到店支付的价格超过 17 美元，而同一批人本可以用 10 美元一次的十次卡。整个会籍期间，他们平均放弃了约 600 美元的节省。

## 为什么重要

这是第 02 章《对赌你不来》的**学术支柱**，也是全书"激励错位"论点唯一一条来自同行评议经济学顶刊、
有逐日行为数据（而非自我报告）支撑的证据。它把"你买的不是健身，是一份'我会去'的期权"从修辞变成可测量的事实：

1. **出席率**不是问卷里的"我打算每周去三次"，是闸机记录。
2. **多付的钱**有精确金额，不是估算。
3. **高估**有直接测量（预测 9.50 次 vs 实际 4.17 次）。
4. 论文自己给出了**卖方激励**的表述——这是"结构激励"论证最干净的出处，不需要指控任何人的主观恶意。

如果这条塌了，第 02 章的"沉没成本收入"一节就只剩作者推断（E 级），全章说服力大幅下降。

## 证据

### 来源 1（主证据，已逐字核对全文 PDF）

- 来源标题：Paying Not to Go to the Gym
- 发布方 / 作者：*American Economic Review*, Vol. 96, No. 3 (June 2006), pp. 694–719；作者 Stefano DellaVigna（UC Berkeley）、Ulrike Malmendier（UC Berkeley）
- 发布日期：2006-06
- URL / DOI：
  - DOI：`10.1257/aer.96.3.694`
  - AEA 官方条目页：https://www.aeaweb.org/articles?id=10.1257/aer.96.3.694
  - **作者自存档全文 PDF（本次实际下载并提取的版本）**：https://sdellavi.com/pdf/gymempAER.pdf
  - 复制数据包（openICPSR）：https://doi.org/10.3886/E116221V1
  - 作者提供的原始数据与代码：https://sdellavi.com/datacode/gymdata.zip
- 采集日期：2026-11-12
- 存档：待建（建议对 AEA 条目页与作者 PDF 各做一份 archive.org 快照）。本次检索已在本地保存 PDF（352,278 字节，26 页）与 `pdftotext -layout` 文本（1,373 行），**未提交进仓库**。
- 证据级：**B**（观察性行为数据 + 结构模型校准；非 RCT，故不评 A）
- 原文关键句（直引，不改写）：

  **摘要（全文逐字）：**
  > "We analyze a novel dataset from three U.S. health clubs with information on both the contractual choice and the day-to-day attendance decisions of 7,752 members over three years. The observed consumer behavior is difficult to reconcile with standard preferences and beliefs. First, members who choose a contract with a flat monthly fee of over $70 attend on average 4.3 times per month. They pay a price per expected visit of more than $17, even though they could pay $10 per visit using a 10-visit pass. On average, these users forgo savings of $600 during their membership. Second, consumers who choose a monthly contract are 17 percent more likely to stay enrolled beyond one year than users committing for a year. This is surprising because monthly members pay higher fees for the option to cancel each month. We also document cancellation delays and attendance expectations, among other findings. Leading explanations for our findings are overconfidence about future self-control or about future efficiency."

  **引言（多付比例）：**
  > "First, consumers who choose a monthly membership of over $70 per month pay on average 70 percent more than they would under the pay-as-you-go contract for the same number of visits."

  **引言（受影响面）：**
  > "Eighty percent of the monthly members would have been better off had they paid per visit for the same number of visits."

  **合约菜单（Section I.C）：**
  > "We conducted a survey of the 97 health clubs in the Boston metropolitan area to document the contract design in the industry. Health clubs offer up to three options: 87 clubs offer a monthly contract and a monthly fee is automatically debited each month to a credit card or bank account until the user cancels; 90 clubs offer an annual contract."
  > "The pay-per-visit system offers two options, either to pay $12 per visit or to purchase a ten-visit pass for $100."

  **Finding 1（每次到店实际价格，Table 2）：**
  > "Users who choose an unsubsidized flat-rate contract pay a price per average attendance of over $17 in the monthly contract and over $15 in the annual contract."

  Table 2 精确值（无补贴子样本）：月付合约 Months 1–6，平均月费 **$75.26**，月均出席 **4.36** 次，每次出席价格 **$17.27**（s.e. 0.54），N = 866；年付合约 Year 1，折算月费 **$66.32**，出席 **4.36** 次，每次价格 **$15.22**（s.e. 1.25），N = 145。

  **Finding 2（出席率的稳健性）：**
  > "Across 24 (gender)\*(club)\*(age) subgroups, the average monthly attendance over the membership is lower than 4.75 visits for 23 out of 24 groups, with an overall average of 4.17 monthly visits."

  **Finding 3（高估的直接测量）：**
  > "The average forecasted number of monthly visits, 9.50 (s.e. 0.66), is more than twice as large as average attendance, 4.17."

  **Finding 4（退卡拖延）：**
  > "On average, 2.31 full months elapse between the last attendance and contract termination for monthly members, with associated membership payments of $187. This lag is at least four months for 20 percent of the users."
  > "Even though the transaction costs of cancellation are likely to be lower than $15 (time cost of sending a cancellation letter or visiting the club), users spend on average $187 in membership fees after their last attendance."

  **Finding 5（续约默认值的威力）：**
  > "Survival probability after 14 months 17 percent higher for monthly than for annual contract"（Table 1 摘要行）

  **损失金额（Section II 末，"no subsidy" 子样本、1997 年 10 月前开始的会籍段）：**
  > "The average loss per spell is $614 for agents initially enrolled in a monthly contract. This amount is 43 percent of the overall $1,423 spent on the health club membership. For agents initially enrolled in an annual contract, there is a small, insignificant gain of $1."

  **★ 卖方结构激励（Section IV，解释 9 "Persuasion"）——本卡最重要的一句：**
  > "Given that users attend on average fewer than eight times per month, flat-rate contracts are on average more profitable for the health clubs than pay-per-visit contracts. Health club employees, therefore, have incentives to persuade consumers to sign flat-rate contracts. They can do this either by not providing (sufficient) information about the pay-per-visit alternative or by urging people to take up the monthly or annual contract."

  **知情者同样多付（HMO 子样本）：**
  > "Nevertheless, the price per expected attendance over months 1 to 6 for the 1,566 HMO members enrolling with a monthly contract equals $10.31 (s.e. 0.23), significantly higher than the $6 price per visit. Thus, even informed members display the tendency to choose the more [expensive contract]."

  **政策含义（第 01 章亦引用，见 claim-0009）：**
  > "Subsidizing enrollment in health clubs is likely to have only small effects on obesity rates, given the low average attendance of members."

  **美国行业背景（Section I.A）：**
  > "As of January 2001, 16,983 clubs were operating in the United States. The industry revenues for the year 2000 totalled $11.6 billion. The memberships in the same period was 32.8 million, up from 17.4 million in 1987."

- 利益相关：**低**。作者为独立学者，发表于同行评议期刊，数据与代码公开（openICPSR + 作者站点）。
  论文结论对健身行业不利，作者无行业资助披露。这是本卡相对中国行业报告（claim-0003/0004）的核心优势。

### 来源 2（交叉验证：同一作者团队的理论 + 实证前作）

- 来源标题：Contract Design and Self-Control: Theory and Evidence
- 发布方 / 作者：*The Quarterly Journal of Economics*, Vol. 119, No. 2 (May 2004), pp. 353–402；Stefano DellaVigna、Ulrike Malmendier
- 发布日期：2004-05
- URL / DOI：作者自存档 PDF https://sdellavi.com/pdf/ContractDesignQJE04.pdf （本次检索已在作者站点确认该链接存在）
- 采集日期：2026-11-12
- 存档：待建
- 证据级：B
- 原文关键句：**待补**。本次检索仅确认了该前作的存在与链接，**未逐字提取其正文**，故不在此引用任何句子或数字。
- 利益相关：低（同上）
- 用途说明：AER 2006 正文多处引用该前作作为理论框架来源（(β,δ) 偏好、部分天真 partial naiveté、承诺装置）。
  **交叉验证的独立性有限**：同一作者团队、同一数据源，不构成"两个独立来源"。真正的独立交叉验证见来源 3。

### 来源 3（独立交叉验证：中国侧的出席率数据）

- 来源标题：《2025中国运动健身行业数据报告》（经新华社报道）
- 发布方：上海体育大学经济管理学院 + 三体云动 + IWF 国际健身展联合制作，中国健美协会指导；报道方新华社（中新网转载）
- 发布日期：报告 2026-03-13 发布；报道 2026-03-14
- URL：https://www.chinanews.com.cn/ty/2026/03-14/10586663.shtml
- 采集日期：2026-11-12
- 存档：待建
- 证据级：C
- 原文关键句（直引）：
  > "活跃会员月均到店次数增至7.56次，同比大幅增长42.1%，全部会员月均到店次数为2.63次"
- 利益相关：**高**。三体云动是健身行业 SaaS 服务商，其客户即健身房。详见 claim-0003。
- 交叉验证结论：**方向一致，量级不同**。美国无补贴包月会员月均 4.3 次；中国**全部**会员月均 2.63 次。
  两者都远低于"每周三次"的自我预期。但**口径不可直接相减**：美国样本是自选包月合约的无补贴用户，
  中国"全部会员"含大量短期卡、赠送卡、休眠卡。详见 claim-0003 的口径说明。

## 反方与局限

- **最强反对意见（必须写进正文，不能只放卡里）：**

  **1. 「600 美元损失」发生在月付自动续约合约，不是年卡。** 论文原文明确：
  月付合约每段会籍平均损失 **$614**（占总支出 $1,423 的 43%），而**年付合约用户只有 1 美元的、统计上不显著的收益**
  （"a small, insignificant gain of $1"）。
  本书第 02 章批评的是**中国的预付费年卡**。把 AER 的 $614 直接搬到中国年卡头上，是**跨合约类型的错误移植**。
  正确的用法是：AER 证明的是"**包月/包年这类 flat-rate 合约 + 低出席率 = 消费者多付**"这一机制，
  以及"**卖方在低出席率下更偏好 flat-rate 合约**"这一结构激励；
  至于中国年卡的具体损失金额，必须用中国数据（claim-0003 / claim-0005）单独论证，**不能借用 $614**。
  另需注意：美国的 monthly 是**自动扣款、需主动取消**；中国的年卡是**一次性预付、到期自动失效**。
  两者的行为学机制不同——前者利用"忘记取消"（Finding 4 的 2.31 个月拖延），后者利用"沉没成本 + 高估未来自控"。
  论文 Finding 5 恰好说明：**需要主动取消的合约，留存率反而更高**（14 个月后存续概率高 17%）。
  这对"年卡是更坏的合约"的直觉是一个真实的反证，正文必须处理。

  **2. 「预测 9.50 次」不是会员自己的预测。** Finding 3 的 9.50 来自
  > "a survey of 48 randomly chosen respondents interviewed in a mall. The mall is not near a health club, so the respondents are not selected on health club attendance."

  即**商场里随机拦访的 48 人**，不是那 7,752 名会员。论文自己警告：
  > "One should take responses to hypothetical questions with caution, however, particularly because the survey sample differs from the health club sample."

  中文媒体普遍把"会员预测自己每月去 9.5 次、实际只去 4.17 次"当成同一批人的前后对比来写——**这是错的**。
  正文若要用"高估"这个论点，必须写成"**一项 48 人商场拦访调查显示，人们预测的月均到店次数（9.50）是实际会员出席率（4.17）的两倍以上**"，
  并注明两个数字来自不同样本。48 人的样本量也极小。

  **3. 作者自己承认「销售说服」可以解释大部分发现。** 论文列出九种解释，其中第 9 种是 Persuasion：
  > "As an alternative explanation, persuasion by health club employees can explain most findings."

  作者只指出说服**无法**解释 Finding 3（高估）：
  > "Persuasion does not explain the survey evidence of overestimation of attendance (Finding 3)."

  也就是说：如果销售话术足以解释合约选择与退卡拖延，那么"消费者非理性"就不是唯一解释，
  "信息不对称 + 卖方推力"可能是主因。**这对本书其实是有利的**（指向结构而非个人愚蠢），
  但它削弱了"消费者高估自己"这一心理学论断的排他性。正文不能把两者混为一谈。

  **4. 出席记录可能漏记。** 作者用一整段辩护其数据质量（前台收卡、会员锻炼时刷卡、无排队），
  并指出这三家俱乐部因为要向补贴会员费的企业出具出席报告，"put in place one of the most advanced and reliable systems to track attendance in the industry"。
  但这仍是**三家俱乐部**的系统，不是全行业。若其他俱乐部漏记严重，行业平均出席率可能被低估。

- **证据的局限：**
  - **样本外推性**：三家新英格兰（波士顿都会区）俱乐部，1997-04 至 2000-07（club 1）/ 2001-02（clubs 2、3）入会者。
    距今 25–29 年，美国市场，**不能直接外推到 2026 年的中国**。中国的人均收入、健身房密度、私教占比、
    预付卡监管环境都不同。本卡只能作为**机制证据**，不能作为**中国量级证据**。
  - **"无补贴"子样本只占 14%**：1,070 人（月付自付 >$70/月，或年付 >$700/年即 $58/月）。
    主结论（$17.27、$614）建立在这 14% 上。其余 86% 有企业补贴，其合约选择动机不同。
    正文引用时必须说明这是**自费高价会员**的行为，不是全体会员。
  - **相关≠因果**：观察性数据。低出席率与合约选择之间的因果方向依赖结构模型假设。
  - **模型校准的敏感性**：作者报告，完全理性的时间不一致者（sophisticated）在 β=0.8 时校准出的退卡延迟仅 5 天，
    β=0.5 时也不足 15 天，而实际观察到的延迟超过 60 天；只有**部分天真**（partial naiveté，β=0.7）
    才能同时匹配 >60 天延迟与 0.2 的 >120 天延迟概率。结论对"天真程度"这一不可直接观测的参数敏感。
  - **十次卡用户不追踪出席**：论文明说 "attendance is not tracked for the pay-per-visit users"。
    因此"按次付费者出席更多"这一比较**无法从本数据直接验证**，只能由合约选择的理论推断。

- **什么情况下这条论断不成立：**
  - 若某业态的会员出席率真的达到每月 8 次以上（论文给出的 flat-rate 划算门槛），则包月合约对消费者是**理性且省钱**的选择，"对赌"框架不适用。
    注意：中国 2025 年**活跃会员**月均 7.56 次已逼近这个门槛——这正是"活跃会员"与"全部会员"必须分开讲的原因（claim-0003）。
  - 若消费者购买包月合约的动机是**承诺装置**（commitment device）而非高估出席率，且他们清楚自己会少来，
    则"多付的钱"是为自我约束付的保险费，不是被收割。论文承认这一动机存在（"in addition to the commitment device reason"）。
  - 若把"损失"定义为**相对于最优合约的货币差**，则年付用户在 AER 数据里**没有损失**。任何声称"年卡用户平均损失 600 美元"的写法都是错的。

## 核查记录

| 日期 | 核查人 | 动作 | 结论 |
|---|---|---|---|
| 2026-11-12 | AI 辅助检索（待人工签字） | 建卡。从作者站点 sdellavi.com 下载全文 PDF，`pdftotext -layout` 提取，逐字比对摘要、Finding 1–5、Table 2、Section IV 解释 9、政策含义段 | 主证据已核实到原文级；状态仍为待核实（缺人工签字） |
| 2026-11-12 | AI 辅助检索 | **排除一个重大误引风险**：NBER working paper **w10870 不是本文**。实际下载 `https://www.nber.org/system/files/working_papers/w10870/w10870.pdf` 并提取文本，确认其为 Kunreuther & Michel-Kerjan, *Policy Watch: Challenges for Terrorism Risk Insurance in the United States*, NBER WP 10870, October 2004。已删除该文件。**本书任何位置不得把 w10870 当作健身论文引用。** | 已排除 |
| 2026-11-12 | AI 辅助检索 | AEA 官方 PDF（`pubs.aeaweb.org/doi/pdfplus/10.1257/aer.96.3.694`）返回 403，付费墙；改用作者自存档版。DOI 与卷期页码经 AEA 条目页确认 | 已解决 |
| 2026-11-12 | AI 辅助检索 | 记录三项必须在正文中体现的口径纠正：①$614 属月付非年付；②9.50 来自 48 人商场拦访非会员自身；③作者承认 persuasion 可解释大部分发现 | 待人工确认正文写法 |

## 推翻记录（如适用）

暂无。

**但已预先登记一条"潜在自我推翻"**：若后续核查发现中文书稿把 $614 写成"年卡用户的损失"，
或把 9.50 写成"会员自己的预测"，则本卡的**论断原文**需要改写，并按 EDITORIAL §9 保留修订史。