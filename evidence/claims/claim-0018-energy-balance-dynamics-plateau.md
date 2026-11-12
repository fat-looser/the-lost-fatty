---
id: claim-0018
title: 「3500 千卡 = 1 磅」的静态规则是错的：能量缺口随体重下降而缩小，体重按约 1 年半衰期趋向新平台；官方机构曾长期沿用该错误规则
status: 待核实
level: B
chapters: [22]
created: 2026-11-12
verified: null
verifier: null
---

# claim-0018：秤不动了，不一定是身体坏了——可能是那个缺口本来就该变小

> ⚠️ **本卡来源已采集、DOI/PMID 已逐条核验、关键句为 PMC 全文直引，但状态保持「待核实」。**
> 按 [EDITORIAL.md](../../EDITORIAL.md) 第七节，AI 辅助检索的事实性内容须人工复核签字后方可标为「已核实」并进入正文。
> 🔴 **本卡的核心来源是数学模型（B 级），不是 RCT。模型输出必须写成「模型预测」，严禁写成「研究观察到」。**
> 🚫 **伦理红线：本卡不得被写成「所以你只要算准卡路里就能瘦」的卡路里主义；也不得被写成「算卡路里完全没用」的虚无主义。本卡的论点是「静态算术错了，动态过程是真的」。**

## 论断原文

> 「少吃 3500 千卡就能瘦一磅」这句话，是错的，而且错得很系统。它假设你的消耗是个常数——但你不是常数。你轻了，维持这个更轻的身体所需的能量就少了；你动起来的成本也低了。所以**同一个饮食缺口，会随着你变瘦而自己变小**，直到它变成零，秤就不动了。**这不是故障，这是算术。** 一个经校验的动态模型给出的图景是：一个 100 公斤、久坐的男性，每天少吃约 480 千卡，体重会在大约一年里走完最大减重的一半，大约三年走完 95%，最终停在 75 公斤左右——**而那个流传甚广的静态规则会告诉你，第一年就该瘦 22 公斤，比模型预测多了整整一倍。** 更值得写的是：这个错误规则曾经被英国 NHS、美国 NIH 和美国饮食协会写进官方建议。**所以「我按计算器吃的，为什么秤不动」这个问题的答案，往往不是你的身体坏了，也不是你意志不够，而是那个计算器本身用错了公式。**

## 为什么重要

这是第 22 章第一节与第五节之间的**机制桥梁**，也是本章「去道德化」论证中**最不需要争议就能成立的一环**。

1. **它提供了一个不依赖「代谢适应」争议的平台期解释**：claim-0010 的代谢适应量级有争议、claim-0012 的 NEAT 量化证据薄弱、claim-0013 的激素因果链未闭合。**但「体重下降 → 维持所需能量下降 → 缺口缩小 → 平台」这条逻辑不需要任何有争议的生理学主张，它只需要能量守恒与体成分变化。** 这使本卡成为第 22 章**最稳固的一块砖**。
2. **它把「平台期」从道德事件还原为数学事件**：读者最常见的自我谴责是「我明明按计算器吃了，为什么不动了，一定是我哪里做错了/我意志不行」。**本卡直接指出：计算器用的公式是错的。** 这是一个**不需要指责任何人**的解释。
3. **它直接支撑本书对减重产业的批判**：如果官方机构与商业项目长期沿用静态规则，那么**它们向消费者承诺的减重速度在数学上就是不可能兑现的**。这与第 20 章（测量与承诺）、第 35 章（AI 教练的建议质量）、第 36 章（落点）直接相连。
4. **它同时是对 claim-0017 的制衡**：claim-0017 说「平台期主要是依从性衰减」，本卡说「即使依从性完美，平台也会出现，只是更晚」。**两者并列，读者才能得到完整图景。**

如果这条错了，第 22 章失去最稳固的机制解释，但其余各节仍可独立成立。

## 证据

### 来源 1（B 级：本卡唯一主来源，PMC 全文已读）

- 来源标题：Quantification of the effect of energy imbalance on bodyweight
- 发布方 / 作者：**Hall KD**, Sacks G, Chandramohan D, Chow CC, Wang YC, Gortmaker SL, Swinburn BA。*The Lancet*
- 发布日期：**2011-08-27**（378 卷 9793 期 826–837 页）
- URL / DOI：https://doi.org/10.1016/S0140-6736(11)60812-X ｜ https://pubmed.ncbi.nlm.nih.gov/21872751/
- 采集日期：**2026-11-12**
- 存档：**PMC 开放全文 PMC3880593**（NIHMS539778 作者手稿，https://pmc.ncbi.nlm.nih.gov/articles/PMC3880593/），**全文已逐段读取**；archive.org 快照待建
- 证据级：**B**（**数学模型 + 模拟**，用控食研究与流行病学数据校验；**不是 RCT，不是直接观测**）
  > ⚠️ 本卡按 B 级使用。原文发表于 *Lancet* 且为「Energy balance and obesity」系列综述之一，**权威性高，但证据类型是模型，不因期刊等级而升为 A。**

#### 1a. 静态规则的错误（直引，本卡最重要的一段）

> "**Widespread official recommendations from the National Health Service in the UK, the National Institutes of Health and the American Dietetic Association in the USA erroneously state that reduction of energy intake by about 2 MJ per day will result in slow and steady weight loss of about 0·5 kg per week.** This ubiquitous weight-loss rule (also known as the **3500 kcal per pound rule**) was derived by estimation of the energy content of weight lost but it **ignores dynamic physiological adaptations to altered body weight that lead to changes of both the resting metabolic rate as well as the energy cost of physical activity**."

- 🔴 **本卡的写作纪律**：
  - 原文点名的是 **英国 NHS、美国 NIH、美国饮食协会（American Dietetic Association）**，**用的是过去时态的 "erroneously state"**。**本卡未独立核实这三家机构在 2011 年之后是否已更正其建议。标注为待核实。**
  - **正文不得写成「这些机构现在还在这么说」。** 应写「Hall 等在 2011 年指出，这些机构的官方建议当时沿用了这一错误规则」。**若要写「至今仍在流传」，须另行核实当代来源（如商业减重 App、健身房话术），本卡未做此核实。**
  - **American Dietetic Association 已于 2012 年更名为 Academy of Nutrition and Dietetics**（**本卡未独立核实更名文件，标注为待核实的背景知识**）。正文若提及须注意名称时效。

#### 1b. 动态模型的定量预测（直引）

> "This constant diet perturbation was predicted to result in a **bodyweight plateau at about 75 kg (165 lb)** over a **10-year simulation** taking roughly **1 year to reach half of the maximum weight loss** and reaching **95% of this value after about 3 years**."

> "By contrast with our dynamic model simulations, the popular dieting rule predicts that the same 2 MJ per day reduction of energy intake will result in a **linear decrease of bodyweight over time with 22 kg lost in the first year** (not shown), which is **about 100% greater weight loss than our model prediction**."

> 摘要："the bodyweight response to a change of energy intake is slow, with **half times of about 1 year**."

- **本卡整理的模拟设定与输出（全部来自原文）**：

  | 项目 | 数值 | 备注 |
  |---|---|---|
  | 模拟对象 | **100 kg 久坐男性** | 原文设定 |
  | 摄入阶跃减少 | **2 MJ/d = 480 kcal/d** | 原文同时给出两种单位 |
  | 模型预测平台体重 | **约 75 kg（165 lb）** | 即最大减重约 25 kg |
  | 达到最大减重一半的时间 | **约 1 年** | 半衰期 |
  | 达到 95% 的时间 | **约 3 年** | — |
  | 模拟总时长 | **10 年** | — |
  | 静态规则预测第一年减重 | **22 kg** | **比模型预测多约 100%** |

  > ⚠️ **全部为模型模拟输出，不是任何受试者的实测数据。正文每次引用必须带「模型预测」四字。**
  > ⚠️ **本卡未核实原文是否给出这些预测的区间/敏感性分析。摘要与已读正文段落中未见 CI。标注为待核实。**

#### 1c. 能量当量：为什么静态规则错（直引）

> "The energy content per kg change of body fat is **39·5 MJ** and **7·6 MJ** for a kg of lean mass."

- **本卡换算（须标注为换算，1 kcal = 4.184 kJ）**：脂肪组织约 **9441 kcal/kg**，瘦体重约 **1816 kcal/kg**。
- **本卡的解读（须标注为解读）**：
  - 静态规则隐含「每减 1 磅（0.4536 kg）= 3500 kcal」，即约 **7716 kcal/kg**——**这个值介于纯脂肪（9441）与纯瘦体重（1816）之间，隐含了一个固定的脂肪/瘦体重混合比。**
  - **但实际减重的成分比是变化的**：减重早期糖原与水分流失多（瘦体重比例高，能量当量低），后期脂肪比例升高。**因此「每公斤减重对应多少千卡」不是常数。**
  - 🔴 **本卡未核实原文是否明确给出 7716 kcal/kg 这个推算值——这是本卡按 3500/0.4536 推算的，须标注为推算。**
  - **与 claim-0017 来源 4 的冲突**：Westerterp 2020 社论用 **30 MJ/kg（7 Mcal/kg ≈ 7170 kcal/kg）** 做静态推算。**两者假设不同，本卡不裁判，只登记冲突（详见 claim-0017）。**

#### 1d. 平台期与反弹的机制解释（直引，与 claim-0017 共享）

> "**A common explanation of the weight-loss plateau at 6–8 months is that a metabolic adaptation occurs such that energy expenditure decreases to match energy intake thereby halting further weight loss. Weight regain then occurs as people slowly relax their adherence to the diet that has stopped producing weight loss.**"

> "**Rather, it is more likely that adherence to the prescribed diet was not constant over this timeframe**—an interpretation supported by previous results from studies showing that **total energy expenditure is much higher than self-reported energy intake at the weight-loss plateau**."

> "The results show that the observed weight change could only have occurred if adherence to the initial reduction of energy intake by about **3·3 MJ per day (800 kcal per day)** was **rapidly and progressively relaxed, such that the patients returned to their original weight-maintenance diet within the first year**, and kept this diet for the remainder of the 3-year simulation."

> "The observed average weight regain at 3 years of **all but about 3 kg of the lost weight** contrasts with the expected weight loss of **more than 12 kg** that our model predicts would have resulted had the individuals eaten their self-reported energy intake."

- 🔴 **本卡的关键区分（强制写入正文）**：
  - **模型预测的平台在约 1 年（半衰期）到 3 年（95%）**；
  - **临床观察到的平台在 6–8 个月**（Thomas 2014 亦指出「typically stabilizes at 6 mo」，见 claim-0017）；
  - **两者不一致。** Hall 用「依从性衰减」解释这个不一致；Thomas 2014 用「间歇性不依从」解释。
  - **因此本卡的论断必须分成两句**：
    1. **即使依从性完美，平台也会出现，只是更晚（约 1–3 年而非 6 个月）。** ← 这是本卡的独立贡献，不依赖依从性争议。
    2. **实际观察到的 6 个月平台早于模型预测，其成因有争议（依从性 vs 代谢适应 vs 模型误差）。** ← 交给 claim-0017 与 claim-0010。
  - **正文严禁把「模型预测的 1–3 年平台」与「观察到的 6 个月平台」混为一谈。**

#### 1e. 能量缺口的人群尺度（直引，本卡的宏观锚点）

> 摘要："A small persistent average daily energy imbalance gap between intake and expenditure of about **30 kJ per day** underlies the observed average weight gain."

> 摘要："The average increase of energy intake needed to sustain the increased weight (the **maintenance energy gap**) has amounted to about **0·9 MJ per day**."

- **本卡换算（须标注）**：30 kJ/d ≈ **7.2 kcal/d**；0.9 MJ/d ≈ **215 kcal/d**。
- **本卡的解读（须标注为解读）**：
  - **「能量失衡缺口」（约 7 kcal/d）与「维持缺口」（约 215 kcal/d）是两个不同的量**：前者解释**为什么人群会慢慢变胖**（每天多 7 千卡，几十年累积成几公斤）；后者解释**为什么胖了之后很难瘦回去**（要维持更重的身体，每天需要多 215 千卡，所以一旦回到原来的吃法，体重就停在那里）。
  - 🔴 **这两个概念极易被混淆，通俗写作常把 215 kcal/d 说成「每天多吃一口就胖」的原因。本卡强制区分。**
  - ⚠️ **本卡未核实原文给出这两个数字的具体人群、年份与计算方法（摘要级信息）。标注为待核实，正文引用须谨慎，或先读全文相应段落。**

#### 1f. 测量精度与补偿（直引，本卡的诚实性锚点）

> "**we cannot measure the initial energy requirements of a free-living individual with a precision better than about 5%**."

> "there is evidence that **increased physical activity results in compensatory changes of energy intake** that act to attenuate the energy imbalance and that the extent of compensation has high individual variability. Conversely, **changes of energy intake might result in compensatory adaptation of non-exercise physical activity**, which also has a high degree of individual variability."

- **本卡的解读（这是本卡对「卡路里主义」的自我限制）**：
  - **5% 的精度上限意味着：对一个每日需要 2500 kcal 的人，你无法把需求测到优于 ±125 kcal。** 而一个「每天少吃 500 kcal」的处方，其实际缺口可能在 375–625 kcal 之间。
  - **加上摄入与活动的双向补偿（个体差异极大），「精确计算卡路里就能精确控制体重」在测量学上就不成立。**
  - 🔴 **因此本卡不得被写成「用动态模型就能算准」。** 动态模型纠正的是**公式的形状**（非线性、趋向平台），**不是把预测精度提高到个体可用**。**正文必须写出这一点。**

#### 1g. 与实测数据的连接（本卡的交叉验证）

- 原文 **Figure 4A 的数据点来自 Svetkey 等（原文参考文献 89）**，即 claim-0019 的 RCT（*JAMA* 2008;299:1139–1148，DOI 10.1001/jama.299.10.1139）。
- **本卡的意义**：**模型不是凭空模拟，它用了真实 RCT 的体重轨迹做校验/对照。** 这提升了模型的可信度，**但仍不改变「模型是 B 级」的判定**。
- 🔴 **本卡未逐格核实 Figure 4A 的数据点与 Svetkey 原文的对应关系。标注为待核实。**

- 利益相关：作者为 NIH/NIDDK（Hall、Chow）、Harvard（Sacks、Gortmaker、Wang）、Deakin（Swinburn）等学术机构；**本卡已读 PMC3880593 全文但未逐段核对 disclosure 段，标注为待核实**。
  > ⚠️ **须注意：Hall KD 同时也是 Fothergill 2016 与 Johannsen 2012 的作者**（见 claim-0011）。**本卡与 claim-0011 共享同一位核心作者，不是完全独立的证据线。** 这一点必须写进正文脚注。

### 来源 2（B 级：能量平衡成分的概念框架；书目已核验，全文未取得）

- 来源标题：Energy balance and its components: implications for body weight regulation
- 发布方 / 作者：**Hall KD**, Heymsfield SB, Kemnitz JW, Klein S, Schoeller DA, **Speakman JR**。*American Journal of Clinical Nutrition* 2012;95(4):989–994
- URL / DOI：https://doi.org/10.3945/ajcn.112.036350 ｜ https://pubmed.ncbi.nlm.nih.gov/22434603/
- 采集日期：**2026-11-12**
- 存档：**PMC 开放全文 PMC3302369**；Europe PMC 核心记录已核验（**该记录无摘要**）；**Europe PMC `fullTextXML` 接口返回 HTTP 500，全文未取得**
- 证据级：**B**（概念综述）
- **本卡用途**：仅作为「TEE / RMR / NREE / 食物热效应 / NEAT / AREE 等术语定义」的**候选权威来源**列出。
- 🔴 **本卡未从其取得任何内容，不得引用其任何表述。** 人工复核补齐路径：`https://pmc.ncbi.nlm.nih.gov/articles/PMC3302369/`（WebFetch 可绕过 XML 接口的 500 错误，此法在本卡其他来源上已验证有效）。
- 利益相关：学术团队；**待核实**。

### 来源 3（B 级：静态规则错误的独立佐证——社论中的能量当量冲突）

- 来源标题：Absence of evidence is no evidence for absence of the phenomenon（editorial）
- 发布方 / 作者：**Westerterp KR**。*Am J Clin Nutr* 2020;112(3):501–502
- URL / DOI：https://doi.org/10.1093/ajcn/nqaa165 ｜ https://pubmed.ncbi.nlm.nih.gov/32584964/
- 采集日期：**2026-11-12**；存档：**PMC7458766** 全文已抓取（详见 claim-0010 / claim-0017）
- 证据级：A 级期刊署名社论
- 原文关键句（直引，**本卡引用它是为了登记冲突，不是为了采用其算法**）：

  > "Cumulated over 25 wk, the energy deficit was 5.5 MJ/d (1312 kcal/d) times 175 d equals 962.5 MJ (229 Mcal) or 32 kg body weight loss, **assuming an energy equivalent of 30 MJ/kg (7 Mcal/kg) weight loss**."

- 🔴 **本卡的判定**：**Westerterp 在 2020 年仍使用静态能量当量（30 MJ/kg）做累计推算，而 Hall 2011 已论证静态规则错误。** 这构成**同一领域内两位权威的方法学冲突**。
  - **本卡不裁判谁对**：Westerterp 的推算目的是**证明摄入低报**（一个粗略的数量级论证），静态当量在该用途下可能足够；Hall 的目的是**预测体重轨迹**，必须用动态模型。**用途不同，精度要求不同。**
  - **但正文若引用任何「累计缺口 → 应减公斤数」的算术，必须写明用的是静态还是动态假设。**
- 利益相关：作者声明无利益冲突、无资助。

### 来源 4（B 级：临床平台时间与模型预测不一致的独立指出）

- 来源标题：Effect of dietary adherence on the body weight plateau: a mathematical model incorporating intermittent compliance with energy intake prescription
- 发布方 / 作者：**Thomas DM** 等，*Am J Clin Nutr* 2014;100(3):787–795；在线首发 2014-07-30
- URL / DOI：https://doi.org/10.3945/ajcn.113.079822 ｜ https://pubmed.ncbi.nlm.nih.gov/25080458/
- 采集日期：**2026-11-12**；存档：Europe PMC 核心摘要已抓取；**全文未取得**
- 证据级：**B**（数学模型）
- 原文关键句（直引）：

  > "**Clinical weight loss in individuals typically stabilizes at 6 mo. However, validated models of dynamic energy balance have consistently shown weight plateaus between 1 and 2 y. The cause for this discrepancy is unclear.**"

- **本卡的用途**：**独立佐证「模型预测平台（1–2 年）晚于临床观察平台（6 个月）」这一矛盾**，且 Thomas 明确说「the cause for this discrepancy is unclear」。**这直接支持本卡把论断拆成两句的写法（见 1d）。**
- 🔴 **注意**：Thomas 2014 说模型平台在 **1–2 年**，Hall 2011 说半衰期约 **1 年**、95% 约 **3 年**。**两者口径不同（「平台」的定义不同），本卡不宣称它们一致，只并列。**
- 利益相关：**与 Hall 2011 存在作者重叠（Heymsfield SB、Schoeller DA、Redman LM、Martin CK）**，**不是完全独立的证据线**。

## 反方与局限

### 最强反对意见（必须正面回应）

**反对意见 A：「这是数学模型，不是人体实验。你不能用模拟结果告诉读者他们的身体会怎样。」**
- **本卡完全接受，并已把「模型预测」四字设为强制口径。**
- **本卡的正面回应**：
  1. **本卡的核心论断不是「模型预测的 75 kg / 1 年 / 3 年是对的」，而是「静态规则在逻辑上必然错」。** 后者**不需要模型正确**：只要承认「维持更轻的身体需要更少能量」与「移动更轻的身体成本更低」，**缺口就必然随体重下降而缩小**。**这是能量守恒的直接推论，不是模型的假设。**
  2. **模型的作用是把这个必然趋势定量化**，而定量部分确实依赖模型假设，**因此本卡把定量数字全部标注为「模型预测」并承认其未经验证于个体**。
  3. **模型有校验**：原文用控食研究与 Svetkey RCT 的实测轨迹做对照（1g）。**这比纯理论模拟强，但仍不等于前瞻性验证。**
  4. **本卡因此把论断分成「必然成立的部分」（缺口会缩小、静态规则错）与「模型依赖的部分」（具体年数与公斤数）。** 正文可以强说前者，必须弱说后者。

**反对意见 B：「如果即使完美依从也要 1–3 年才到平台，那为什么现实中 everyone 在 6 个月就停了？你的模型根本不符合现实。」**
- **本卡接受这个矛盾，并已把它写进论断结构（1d）。**
- **本卡的正面回应**：
  1. **这个矛盾是文献公开承认的**（Thomas 2014 直引："The cause for this discrepancy is unclear"）。**本卡不假装解决了它。**
  2. **三种候选解释并列**：①依从性衰减（Hall、Thomas，见 claim-0017）；②代谢适应比模型假设的更强（见 claim-0010，但量级有争议）；③模型本身漏掉了某些生理机制。
  3. **本卡的独立贡献恰恰在于指出：即使解释①成立，也不能推出「平台期与生理无关」**——因为**缺口随体重缩小这件事本身就在起作用，只是它单独不足以造成 6 个月平台**。
  4. **正文写法**：「**模型说，就算你完全照做，秤也会在一年到三年里慢慢停住。而现实中它六个月就停了。这中间的差距，是本章最有争议的地方。**」

**反对意见 C：「你这是在替『算卡路里』辩护，而本书的立场是反对卡路里主义。」**
- **本卡的正面回应**：**恰恰相反。**
  1. **本卡证明的是「静态卡路里算术错了」**，这直接打击了减重产业最常用的营销话术（「每天少吃 500 卡，一周瘦一斤」）。
  2. **本卡同时证明「动态算术也不够」**：5% 的个体能量需求测量精度上限 + 摄入与活动的双向补偿 + 极大个体差异（1f）。**因此本卡不支持「算准就能瘦」。**
  3. **本卡的落点是**：「**你按计算器吃却没瘦，不是你的错，是计算器的公式错了；而换一个更对的公式，也仍然算不准你——因为人不是恒温箱。**」
  4. **这与本书反意志力叙事完全一致**：把失败归因于**工具与模型的缺陷**，而不是**人的品格**。

**反对意见 D：「Hall 也是 Fothergill 和 Johannsen 的作者，你的『多方证据』其实是一个人。」**
- **本卡接受，并已写在来源 1 的利益相关段与来源 4 的注记里。**
- **本卡的正面回应**：
  1. **本卡的主来源只有一篇（Hall 2011）**，其余三篇是**佐证/冲突登记**，**本卡不宣称有多方独立验证**。
  2. **但本卡的核心论断（静态规则错）不需要多方验证**——它是能量守恒的推论，**任何承认体成分变化影响消耗的人都必须接受**。
  3. **真正需要独立验证的是定量部分（1 年 / 3 年 / 75 kg）**，而**本卡明确把它标为模型依赖、未独立验证**。**因此作者重叠不构成对本卡论断的威胁，只构成对其定量精度的限制。**
  4. **人工复核建议**：寻找独立团队（非 Hall / Chow / NIDDK 体系）的动态能量平衡模型验证研究。**本卡未执行此检索，标注为待核实。** 建议关键词：`dynamic energy balance model validation independent weight loss plateau half-time`、`Thomas model vs Hall model weight loss prediction comparison`。

### 证据的局限

- 🔴 **主来源为数学模型（B 级），不是 RCT，不是前瞻观测。** 所有定量输出必须标注「模型预测」。
- 🔴 **模型输出无 CI / 无敏感性分析区间（本卡已读段落中未见）。待核实全文是否另有报告。**
- 🔴 **模拟对象为「100 kg 久坐男性」这一个案设定**，**不是人群平均，不可外推到女性、不同初始体重、不同活动水平者。**
- 🔴 **「3500 kcal/lb 规则被官方沿用」的时效未核实**：原文为 2011 年，点名 NHS / NIH / American Dietetic Association。**本卡未核实这些机构此后是否更正，也未核实当代商业话术是否仍在使用。正文不得写「至今仍在沿用」而不加核实。**
- **能量当量假设冲突**：Hall 用脂肪 39.5 MJ/kg + 瘦体重 7.6 MJ/kg 的动态混合；Westerterp 用静态 30 MJ/kg。**本卡登记冲突，不裁判。**
- **平台时间口径不一致**：Hall 半衰期约 1 年、95% 约 3 年；Thomas 说模型平台 1–2 年；临床观察 6 个月。**三个数字不可混用。**
- **测量精度上限约 5%**（原文自陈），**加上双向补偿与极大个体差异，模型不可用于个体精确预测。**
- **作者重叠**：Hall 同时是 Fothergill 2016 / Johannsen 2012 作者；Thomas 2014 与 Hall 2011 共享 Heymsfield / Schoeller / Redman / Martin。**非独立重复。**
- **宏观数字（30 kJ/d、0.9 MJ/d）的人群与方法未核实**（摘要级信息）。
- **Figure 4A 与 Svetkey 原文的逐格对应未核实。**
- **术语定义来源（Hall 2012）全文未取得**，本卡未从中引用任何内容。
- **相关 ≠ 因果**：本卡不涉及相关系数，但**模型中的因果结构是假设，不是被检验的结论**。

### 什么情况下这条论断不成立

1. 若实测证明维持更轻身体的能量需求**不随体重下降**（即消耗与体重无关）→ 本卡的核心逻辑崩塌。**但这与能量守恒及大量实测（Leibel 1995、Redman 2009）矛盾，可能性极低。**
2. 若独立团队的动态模型经前瞻性验证，给出的半衰期与平台时间与 Hall 2011 显著不同 → 本卡的定量部分须改用新数字，**但「静态规则错」的核心论断不受影响**。
3. 若核实发现 NHS / NIH / ADA 在 2011 年前就已更正建议 → 本卡关于「官方沿用错误规则」的表述须修正为历史陈述并调整措辞。
4. **本卡在任何情况下都不支持**：「算准卡路里就能精确控制体重」「平台期全是代谢适应造成的」「平台期全是没管住嘴」三种表述。

## 核查记录

| 日期 | 核查人 | 动作 | 结论 |
|---|---|---|---|
| 2026-11-12 | AI 检索助手（QoderCN） | 建卡。Europe PMC 核验 Hall 2011 / Hall 2012 / Westerterp 2020 / Thomas 2014 书目；**PMC3880593 全文逐段读取**；PMC7458766 全文已读 | 待核实 |
| 2026-11-12 | AI 检索助手 | 把论断拆为「必然成立部分」（缺口随体重缩小、静态规则错）与「模型依赖部分」（1 年 / 3 年 / 75 kg），并设强制口径 | ✅ 已写入 |
| 2026-11-12 | AI 检索助手 | **登记权威间方法学冲突**：Westerterp 2020 仍用静态 30 MJ/kg，Hall 2011 论证静态规则错误 | 🔴 已登记，不裁判 |
| 2026-11-12 | AI 检索助手 | 标注缺口：官方建议时效未核实；模型输出无 CI；宏观数字人群未核实；Hall 2012 全文 XML 接口 500 | 🔴 待核实 |
| 2026-11-12 | AI 检索助手 | 标注作者重叠（Hall ↔ Fothergill/Johannsen；Thomas ↔ Hall），**本卡不宣称多方独立验证** | 已如实记录 |
| | | 人工复核签字 | 待定 |

**本地检索缓存（临时文件，7 天后可能失效）**：
- Hall 2011 Lancet 全文：`/Users/allengaller/.qoder-cn/tmp/-Users-allengaller-Documents-GitHub-allengaller-claw/tool-outputs/session-48877376-d8c7-421d-8685-def6cc0205ef/webfetch-61cff6fc-6f79-478c-9eb9-4e6fd9155093.md`（144951 UTF-16 单位，562 行；正文 88–562 行）
- Westerterp 2020 社论：同目录 `webfetch-d648cfeb-e1c3-4958-b364-45cad76b4d85.md`

**已检索但未取得（供人工复核接续，按优先级）**：
1. 🔴 **NHS / NIH / Academy of Nutrition and Dietetics 当代官方建议是否仍用 3500 kcal 规则**：建议检索各机构官网当前体重管理页面 + Wayback 对比 2011 前后版本。**这是本卡最具传播力也最需要时效核实的一条。**
2. 🔴 **Hall 2011 全文中模型输出的敏感性分析/区间**（PMC3880593 已缓存，人工复核请查 Supplementary / Appendix 段）。
3. **Hall 2011 中 30 kJ/d 与 0.9 MJ/d 的具体人群、年份、计算方法**（同上缓存）。
4. **Hall 2012 全文**：改用 `https://pmc.ncbi.nlm.nih.gov/articles/PMC3302369/`（XML 接口 500，WebFetch 可绕过）。
5. **独立团队的动态模型验证研究**（非 Hall/Chow/NIDDK 体系）。
6. **Figure 4A 与 Svetkey 2008 原文数据的逐格对应**。
7. American Dietetic Association 更名文件（2012）。

## 推翻记录（如适用）

- 原论断：**「少吃 3500 千卡就能瘦 1 磅 / 每天少吃 500 千卡就能每周瘦 0.5 公斤，且会持续线性下降」**（静态规则；Hall 2011 指出曾被 NHS、NIH、American Dietetic Association 写入官方建议）
- 推翻日期：**2011-08-27**（Hall 等 *Lancet* 论文发表；本卡 2026-11-12 采集登记）
- 推翻理由与证据：Hall KD 等，*Lancet* 2011;378(9793):826–837，DOI **10.1016/S0140-6736(11)60812-X**，PMID **21872751**，PMC3880593。原文直引："This ubiquitous weight-loss rule (also known as the 3500 kcal per pound rule) … **ignores dynamic physiological adaptations to altered body weight** that lead to changes of both the resting metabolic rate as well as the energy cost of physical activity." 模型预测同一 2 MJ/d 缺口下第一年减重约为静态规则预测（22 kg）的一半，半衰期约 1 年，95% 约 3 年，最终平台约 75 kg（100 kg 久坐男性设定）。
- 正文如何修订：**第 22 章不得出现「每天少吃 X 千卡，一周瘦 Y 斤」式的线性承诺。** 须改为「缺口会随体重下降而缩小，体重趋向一个新平台」，并**注明具体年数与公斤数为模型预测、来自单一模拟设定、无 CI**。**同时须写出 5% 的个体测量精度上限，避免读者以为换个公式就能算准。**

> 📌 **给主控的接线提示**：本卡是第 22 章**最稳固的机制砖**（不依赖代谢适应争议），与 claim-0010（代谢适应量级）、claim-0012（活动成本随体重下降）、claim-0016（曲线形状）、claim-0017（6 个月 vs 1–3 年的矛盾）、claim-0019（Svetkey 数据被 Hall 用作校验）交叉。**本卡也是第 20 章（测量与承诺）、第 35 章（AI 教练是否会沿用静态规则）的重要前置——建议主控在这两章的卡片中反向引用本卡。**