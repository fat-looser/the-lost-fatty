---
id: claim-0021
title: DEXA 也不是绝对真值：设备间存在系统差异，水合与进食改变读数，生物学变异远大于技术误差
status: 待核实
level: B
chapters: [20]
created: 2026-11-12
verified: null
verifier: null
---

# claim-0021：DEXA 也不是绝对真值：设备间存在系统差异，水合与进食改变读数，生物学变异远大于技术误差

> ⚠️ **本卡来源已采集、DOI 已逐条核验、关键句为摘要直引，但状态保持「待核实」。**
> 按 [EDITORIAL.md](../../EDITORIAL.md) 第七节，AI 辅助检索的事实性内容须人工复核签字后方可标为「已核实」并进入正文。
> **检索结论（证据强度）：论断成立，B 级。** 未找到针对「DEXA 精度与设备间差异」的系统综述（A 级），
> 现有证据为多项 B 级横断面/重复测量研究，**因此正文断言强度须相应下调**：
> 可写「DEXA 也不是绝对真值」，不可写「DEXA 误差为 X%」这类统一数字。
> 核心量化事实：**连续两天扫描的脂肪量精度误差（1261 g）约为同日重复（660 g）的 2 倍，瘦体重（2083 g vs 617 g）超过 3 倍。**

## 论断原文

> DEXA 被健身房和体检机构叫作「金标准」。但它是带误差的估计，不是真值：换一台机器、换一个厂家，读数就变；脱水 2% 就能让瘦体重掉 1.3 公斤；同一台机器同一个人，隔一天再扫，脂肪量的波动是当天重扫的两倍。不存在一个「真实体脂率」躺在仪器里等着被读出来。

## 为什么重要

第 20 章第三节的全部。它防止本章滑向另一种误导：「家用秤不准，所以去做 DEXA 就有答案了」。**本书的论点是所有测量都是带误差的估计，而不是「换个更贵的仪器就找到真值」**。如果这条塌了，第 20 章会被读成 DEXA 广告，第四节「精确的错误」也失去落点。

它同时约束 claim-0020：把 BIA 与 DEXA 对照时，不能把 DEXA 当作无误差的参照系。

## 证据

### 来源 1（B 级，水合状态对 DEXA 的影响，主证据）

- 来源标题：Errors in dual energy x-ray absorptiometry estimation of body composition induced by hypohydration
- 发布方 / 作者：Rodríguez-Sánchez N, Galloway SD；International Journal of Sport Nutrition and Exercise Metabolism（Human Kinetics）
- 发布日期：2014-07-14（在线）；2015 年 2 月 25 卷 1 期 60–68 页
- URL / DOI：https://doi.org/10.1123/ijsnem.2014-0067 ｜ https://pubmed.ncbi.nlm.nih.gov/25029477/
- 采集日期：2026-11-12
- 存档：无 PMC 开放全文；archive.org 快照待建
- 证据级：B（受控实验性脱水方案，n=38 竞技运动员，23 男 15 女；运动热应激致体重下降 >2% 为 HYP 条件，正常水合为 EUH 条件）
- 原文关键句（直引）：
  > "A reduction in total BM (1.6 ± 0.4 kg; 2.3 ± 0.4% HYP) and total FFST (1.3 ± 0.4 kg), mainly from trunk (1.1 ± 0.5 kg), was observed using DXA when participants were HYP, reflecting the sweat loss. Estimated fat percent increased (0.3 ± 0.3%), however, total FM did not change (0.1 ± 0.2 kg)."

  > "SF and IMP declined with HYP (losses of 1.5 ± 2.9% and 1.6 ± 3% respectively) suggesting FM loss."

  > "These results highlight the need to control for hydration status when interpreting DXA body composition results and indicate that the use of DXA for FFST assessment in athletes must ensure a EUH state."
- 利益相关：斯特灵大学，无厂商雇佣声明。
- 本书用法：**这是「出汗不等于掉脂肪，但仪器会以为你掉了」的直接证据**。脱水 2.3% → DEXA 读出的去脂软组织少 1.3 kg，脂肪量几乎不变（0.1±0.2 kg），体脂率反而**升高** 0.3 个百分点。而皮褶（SF）与生物电阻抗（IMP）却读出脂肪「减少」——**三种方法在同一生理状态下给出方向相反的结论**。这一段可直接支撑第 20 章第四节。

### 来源 2（B 级，跨厂家设备间差异）

- 来源标题：Fat tissue measurements by dual-energy x-ray absorptiometry: cross-calibration of 3 different fan-beam instruments
- 发布方 / 作者：Malouf J, DiGregorio S, Del Rio L, Torres F, Marin AM, Farrerons J, Herrera S, Domingo P；Journal of Clinical Densitometry
- 发布日期：2012-06-13（在线）；2013 年 4–6 月 16 卷 2 期 212–222 页
- URL / DOI：https://doi.org/10.1016/j.jocd.2012.04.003 ｜ https://pubmed.ncbi.nlm.nih.gov/22698632/
- 采集日期：2026-11-12
- 存档：无 PMC 开放全文；archive.org 快照待建
- 证据级：B（同日跨设备交叉校准，n=91 健康成人，40 男 51 女，平均年龄 48.5±14.4 岁；设备为 Hologic Discovery、GE Lunar iDXA、GE Lunar Prodigy Advance）
- 原文关键句（直引）：
  > "Results showed a better agreement and concordance for the Lunar iDXA scanner than for any of them with the Hologic scanner. Differences were higher for any tissue or region than for the whole tissue mass. Translational equations were developed to ensure comparability of body composition measurements obtained with each of these 3 scanners."
- 利益相关：巴塞罗那 Hospital de la Santa Creu i Sant Pau，无厂商雇佣声明。**注意**：GE 与 Hologic 是竞争厂商，此类交叉校准研究的结论对双方均有商业含义，正文引用时应说明「需要换算方程才能比较」这一事实本身。
- 本书用法：**同一批人、同一天、三台机器，结果不可直接比较，必须建立换算方程。** 「换一家健身房/体检中心做 DEXA，数字变了」不是你的身体变了。摘要未给出具体 kg 差值，**正文若要点出数值必须取全文，标为待核实**。

### 来源 3（B 级，交叉验证：设备间差异随部位与体量放大）

- 来源标题：Regional body composition: cross-calibration of DXA scanners--QDR4500W and Discovery Wi
- 发布方 / 作者：Covey MK, Berry JK, Hacker ED；Obesity（Silver Spring）
- 发布日期：2009-12-03（在线）；2010 年 3 月 18 卷 3 期 632–637 页
- URL / DOI：https://doi.org/10.1038/oby.2009.420 ｜ https://pubmed.ncbi.nlm.nih.gov/19960003/
- 采集日期：2026-11-12
- 存档：无 PMC 开放全文；archive.org 快照待建
- 证据级：B（重复扫描交叉校准，n=39 女性，50.6±9.6 岁，BMI 26.8±5.5，体脂 33±7%；3 周内 4 次全身扫描）
- 原文关键句（直引）：
  > "Differences exist in body composition assessed by dual-energy X-ray absorptiometers (DXAs) between devices produced by different manufacturers and different models from the same manufacturer."

  > "The greatest interdevice difference was for truncal fat mass (0.69 +/- 0.60 kg). Differences in truncal and appendicular fat mass increased in magnitude at higher mean values."
- 利益相关：伊利诺伊大学芝加哥分校护理学院，无厂商雇佣声明。
- 本书用法：给出**具体数值**（躯干脂肪量设备间差 0.69±0.60 kg），且指出**差异随均值增大而增大（比例偏差）**。这解释了为什么体脂越高的人，换机器后数字跳得越厉害。与来源 2 结论方向一致，构成独立交叉验证（不同国家、不同设备对、不同样本）。

### 来源 4（B 级，技术误差 vs 生物学变异，本卡最关键）

- 来源标题：Same-Day Vs Consecutive-Day Precision Error of Dual-Energy X-Ray Absorptiometry for Interpreting Body Composition Change in Resistance-Trained Athletes
- 发布方 / 作者：Zemski AJ, Hind K, Keating SE, Broad EM, Marsh DJ, Slater GJ；Journal of Clinical Densitometry
- 发布日期：2018-10-29（在线）；2019 年 1–3 月 22 卷 1 期 104–114 页
- URL / DOI：https://doi.org/10.1016/j.jocd.2018.10.005 ｜ https://pubmed.ncbi.nlm.nih.gov/30454952/
- 采集日期：2026-11-12
- 存档：无 PMC 开放全文；archive.org 快照待建
- 证据级：B（重复测量精度研究，n=21 抗阻训练运动员，30.6±8.2 岁，174.2±7.2 cm，74.3±11.6 kg）
- 原文关键句（直引）：
  > "The consecutive-day precision error, in comparison to same-day precision error, was significantly different (p < 0.05), and almost twice as large for fat mass (1261 g vs 660 g), and over 3 times as large for lean mass (2083 g vs 617 g), yet still remained within the ISCD minimum acceptable limits for DXA precision error."
- 利益相关：阳光海岸大学与利兹贝克特大学，无厂商雇佣声明。
- 本书用法：**「不存在真实体脂率等着你去测出来」的最强单条证据。** 机器本身没变、人也没变，只是隔了一天，脂肪量的测量波动就从 660 g 变成 1261 g，瘦体重从 617 g 变成 2083 g。多出来的那部分不是仪器坏了，是**你身体的水、糖原、肠内容物在变**——DEXA 把它们算进了「瘦体重」。**所以 DEXA 测的也不是一个静止的真值，而是一个随生理状态漂移的量。** 建议作为第 20 章第三节的核心引证。

### 来源 5（B 级，进食影响 + 最小显著变化 LSC）

- 来源标题：Precision and Effects of a Small Meal on DXA-Derived Visceral Adipose Tissue, Appendicular Lean Mass, and Other Body Composition Estimates In Nonobese Elderly Men
- 发布方 / 作者：Thamnirat K, Taweerat P, Permpongkosol S, Kamolnate N, Kositwattanarerk A, Utamakul C, Chamroonrat W, Sritara C；Journal of Clinical Densitometry
- 发布日期：2020-05-03（在线）；2021 年 4–6 月 24 卷 2 期 308–318 页
- URL / DOI：https://doi.org/10.1016/j.jocd.2020.04.001 ｜ https://pubmed.ncbi.nlm.nih.gov/32446653/
- 采集日期：2026-11-12
- 存档：无 PMC 开放全文；archive.org 快照待建
- 证据级：B（重复扫描 + 标准化进食干预，n=36 非肥胖男性 ≥60 岁；3 次含重新摆位的扫描，最后一次在标准化餐后）
- 原文关键句（直引）：
  > "Coefficients of variation (CVs (%)) of total bone mass (Tb.BMC) and total lean mass (Tb.LM) were <1%, whereas those of total fat mass (Tb.FM) and total %fat mass (Tb.%FM) were <2%, with LSCs of 45.8 g, 706.52 g, 731.4 g, and 1.15%, respectively."

  > "After meal consumption, the mean changes in Tb.FM, Tb.BMC, and Tb.LM were -100, -8.2, and 440 g, respectively."

  > "Effects of a small meal on most parameters were trivial... suggesting that a small meal is allowable before these measurements."
- 利益相关：玛希隆大学 Ramathibodi 医院，无厂商雇佣声明。
- 本书用法：**双向使用**。（1）LSC（最小显著变化）体脂率为 **1.15 个百分点**——低于这个幅度的「体脂率变化」在统计上无法与测量噪声区分。这是第 20 章「小数点后一位的虚假精确」的量化锚点。（2）**反方**：小餐食的影响是「trivial」，作者认为测前吃一点是可以的。**本书不得把「必须严格空腹」写成硬性要求**，否则就是另一种过度外推。

## 反方与局限

- **最强反对意见一：「DEXA 仍然是现有最好的临床方法，你这是在贬低它。」** 成立，且必须写进正文。DEXA 在**同日重复精度**上表现极好（来源 5：%CV <1–2%；来源 3：两台设备 test-retest 均良好），是 ISCD 认可的临床标准，骨密度测量尤其如此。**本书的论点不是「DEXA 没用」，而是「精度高 ≠ 是真值」。** 抹掉这一点会让第 20 章变成反测量、反医学。
- **最强反对意见二：「小餐食影响可忽略，你说的进食干扰被夸大了。」** 成立（来源 5）。**须区分「小餐食」（210–250 g 食物 + 200 cc 水，影响 trivial）与「显著脱水」（>2% 体重，瘦体重少 1.3 kg，来源 1）**。二者量级完全不同。正文若写「测前别吃饭」必须限定为「避免大量进食/饮水与显著脱水」，不能一概而论。
- **最强反对意见三：「设备间差异可以用换算方程解决。」** 成立（来源 2 明确建立了 translational equations）。**但这恰恰证明原始读数不可直接比较**，且换算方程是研究者为特定三台机器拟合的，不能推广到任意两台机器。消费者换机构做 DEXA 时**没有**这个方程。
- **证据的局限**：
  - **无 A 级来源**。本次检索未找到专门针对「DEXA 体成分精度与设备间差异」的系统综述或 meta 分析；现有均为单中心 B 级研究。**按 EDITORIAL 规则，正文断言强度须下调，不得给出统一误差数字。**
  - 样本量普遍偏小（n=21 / 36 / 38 / 39 / 91），且人群高度特定：竞技运动员、抗阻训练者、≥60 岁非肥胖男性、中年女性。**外推到一般人群（尤其重度肥胖者、儿童、孕妇）无依据。**
  - 来源 1 的脱水是**运动热应激诱导的急性脱水**，与日常「早上起床有点渴」不是同一量级，不可直接套用 1.3 kg 这个数字到日常场景。
  - 来源 4 的「连续两天」差异中，**生物学变异与技术误差无法完全分离**——这正是其结论的含义，但也意味着不能把 1261 g 全部归因于「身体在变」。
  - 来源 2 摘要未给出具体 kg 差值；来源 3 的 0.69 kg 仅限躯干脂肪量，**不是全身体脂率差**。
- **什么情况下这条论断不成立**：
  - 在**同一台设备、同一操作者、严格标准化条件（晨起、空腹、排空、正常水合）**下做**长期随访**时，DEXA 的组内变化检测能力是可靠的，来源 4 也确认其精度仍在 ISCD 可接受范围内
  - 用于**骨密度**而非体成分时，DEXA 的临床地位不受本卡影响
  - 若只关心**群体均值**或**大幅变化（远超 LSC）**，设备间与日间差异的影响相对可忽略

## 核查记录

| 日期 | 核查人 | 动作 | 结论 |
|---|---|---|---|
| 2026-11-12 | AI 辅助检索（待人工复核） | 建卡；PubMed E-utilities 检索 + Crossref 逐条核验 DOI；采集 5 条 B 级来源 | 待核实（无 A 级来源，断言强度已下调；按 EDITORIAL 七待人工签字） |

**检索路径记录**：PubMed 检索词 `dual energy x-ray absorptiometry precision error body composition`、`DXA cross-calibration scanners body composition`、`hypohydration body composition measurement dual energy x-ray absorptiometry`、`DXA hydration status effect body composition measurement error`（无结果）、`dual-energy X-ray absorptiometry same-day consecutive-day precision`、`DXA least significant change body fat`、`DXA body composition systematic review precision validity`。**未找到 A 级系统综述**，已按规则降低断言强度。

**仍待核实**：
1. 来源 2 全文中的**具体设备间 kg / 百分点差值**（摘要未给）。
2. 针对一般人群（非运动员、非老年）的 DEXA 精度研究，以及是否存在 A 级系统综述。
3. 「DXA 对重度肥胖者的误差」——本次检索未覆盖，若正文涉及需补卡。
4. 全部来源的 archive.org 网页快照（本次 web.archive.org/save 超时失败）。

## 推翻记录（如适用）

暂无。