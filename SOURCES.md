# 素材来源与融入计划

> 本书的可审计性从素材开始。本文件列出全部素材来源、用途、核查状态。
> 规则：**没有来源的数字不进正文**；核不实的标"待核实"并开 Issue。

## 采集状态总览（2026-11-12）

**已完成 P0.5 证据层**：58 张卡（`claim-0001`–`claim-0061`，0032–0034 未使用）。其中 0061 为 P1 复核轮新建的 A 级专卡。
**唯一裁决文件**：[evidence/claims/INDEX.md](evidence/claims/INDEX.md)——口径冲突、独立性警告、原文异常、黑名单来源全部在那里，动笔前必读。

| 类别 | 状态 |
|---|---|
| 行业数据（C 级） | ✅ MVP 所需已采集（0001–0009） |
| 政策与监管（C 级） | ✅ 指南 / 肥胖率 / GLP-1 获批与价格 / AI 监管 / PIPL 已取得（0039/0040/0042/0048/0049/0053/0054） |
| 学术文献（A/B 级） | ✅ MVP 所需已采集（0010–0038、0041、0043–0047、0050–0052、0055–0060） |
| 认证与教育（C/D 级） | ⏳ 未启动（P2） |
| 社区田野（D 级） | ⏳ 未启动；**但链路腐烂实测已完成，见下** |
| 访谈（D 级） | ❌ **0 条**。MVP 九章的开篇人物目前全部无素材支撑 |
| 作者经历（E 级） | ❌ **0 条**。待作者决定是否公开 |

**核查状态提醒**：58 张卡中 **46 张仍标「待核实」**——AI 检索的内容未经人工签字，**这不是瑕疵，这是本书论点的落实**（EDITORIAL 第七节）。

### 链路腐烂实测（本轮意外收获，本身即证据）

采集过程中实测到的中文链路状态，供第 18 章（翻译的失真）、26 章（平台迁移）、30 章（算法末法）使用：

| 目标 | 实测结果 |
|---|---|
| gov.cn 肥胖率发布页 | **404** |
| nhc.gov.cn | **412** |
| 搜狐视频（科普原始出处） | **软 404**（返回 200 但内容不存在） |
| 知乎 | **403** |
| 今日头条 | 200 但**仅 JS 壳**，无正文 |
| 百度知道 | 含 `ai_detect` 元数据，**疑批量生产** |
| archive.org | **不可达**（curl 000）→ 全部存档快照「待建」 |
| NMPA 官网获批查询 | **412** → 三个流传日期皆为公告日，批准日待查 |

→ **当原始出处打不开、而 AI 生成的内容填满搜索结果，「末法」就不只是隐喻。**

## 零、隐私边界（最高优先级）

作者本地工作区（`claw/`）中的私人语料——包括千问对话记录、健康与医疗问答、个人日志——**仅作本地私有参考，不进入本公开仓库**。

- ✅ 允许：从中提炼写作线索、问题清单、脱敏后的观点，作为构思起点
- ❌ 禁止：原文摘录、可识别信息、聊天截图、个人健康数据、原始文件复制
- 本仓库 `.gitignore` 已排除 `_private/`、`素材-本地/`、`*.local.md`、`*.private.md`、`evidence/interviews/raw/`
- 所有进入正文的个人经验，必须是作者主动选择公开的内容，并在 [CONFLICTS.md](CONFLICTS.md) 中说明

## 一、本地私有参考（不入库）

| 素材 | 用途 | 处理方式 |
|---|---|---|
| 健康-医疗-养生 对话语料 | 第 20–25 章的问题意识与常见误区清单 | 只提炼问题，不引原文 |
| 行业-趋势-分析 对话语料 | 第 01、30、34、35 章的分析角度 | 只提炼角度，结论重新用公开证据支撑 |
| 运动与健身 对话语料 | 第 19、24 章的自学路径与自我实验 | 同上 |
| 科学科普 对话语料 | 第 18、29 章的传播失真案例线索 | 同上 |
| 《判断之书》（作者已出版开源书） | 第 24、28、31 章的框架互文 | 可公开引用，注明书名与章节 |

## 二、行业数据（C 级）

| 来源 | 用于 | 核查状态 |
|---|---|---|
| 三体云动《中国健身行业数据报告》（历年） | 01 市场规模、02 单店模型、03 教练处境 | ✅ 已采集 → [0003](evidence/claims/claim-0003-china-gym-member-attendance.md)（2.63 / 7.56 次）、[0004](evidence/claims/claim-0004-china-fitness-market-structure.md)（场馆减 2.3 万家 vs 消费称增 34.2%）⚠️「活跃会员」定义仍缺 |
| Keep 港股财报与招股书 | 01 市场结构、11 知识付费、30 平台 | ✅ 已采集 → [0007](evidence/claims/claim-0007-keep-revenue-structure.md)（收入大头已是卖货） |
| 乐刻 / 超级猩猩公开资料 | 02 月付制对照 | ✅ 已采集 → [0006](evidence/claims/claim-0006-monthly-pay-inverted-incentive.md) ⚠️ 月付制连锁合计占全国场馆不到 1/20，是细分市场不是解药 |
| 艾瑞 / 易观 / 德勤 健身与体重管理报告 | 01 市场规模交叉验证 | ⏳ 待采集（注意发布方利益相关） |
| 健身房预付卡纠纷裁判文书 | 02 预售跑路、06 监管 | ✅ 部分 → [0005](evidence/claims/claim-0005-prepaid-gym-closure-refund.md)（闭店时无担保债权）⚠️ 法释〔2025〕4 号建议另建卡 |
| 健身机构暴雷媒体报道 | 02 现金流结构 | ✅ 部分（并入 0004/0005）⚠️ 需交叉验证 |
| 私教薪酬结构公开资料 | 03 劳动处境、35 AI 对照 | ✅ 已采集 → [0008](evidence/claims/claim-0008-pt-pay-sales-kpi.md)（底薪 1500 + 课时费 60–150 + 提成 6%–8%） |

## 三、政策与监管（C 级）

| 来源 | 用于 | 核查状态 |
|---|---|---|
| 国家卫健委《肥胖症诊疗指南（2024 年版）》 | 14 疾病承认史、20 秤、22 反弹、34 针剂、36 落点、37 最小实践 | ✅ **PDF 已入库可复核**：[`evidence/data/obesity-guideline-2024.pdf`](evidence/data/obesity-guideline-2024.pdf)（79 页，MD5 `b004c90bbdb849731c6c7362971ed07e`）。**两卡分工**：[0042](evidence/claims/claim-0042-china-obesity-guideline-2024.md)（A，治疗定位/诊断切点/行政发布程序，成文 2024-10-12、政策库发布 10-20）＋ **[0061](evidence/claims/claim-0061-obesity-guideline-fulltext-search.md)（A，全文检索事实与测量层级，2026-11-12 新建）**。⚠️「健身」0 次、「慢性复发性疾病」0 次**已从 C 级卡 0009 升格至 0061**，计数须做**三法**（朴素/去空白/允许页码插入）。⚠️ 0061 另收紧：「复发」4 次、CBT 设「维持和预防复发」模块 → **不得写「指南回避复发性」**；词频**不得推论「官方忽视运动」** |
| 《中国居民营养与慢性病状况报告》 | 01 肥胖率、21 饮食环境 | ⚠️ **二手取得** → [0053](evidence/claims/claim-0053-china-adult-overweight-obesity-prevalence.md)（34.3% / 16.4%，2015—2019 监测）；gov.cn 404、nhc.gov.cn 412，需回溯《营养学报》2020;42(6):521 |
| 国家职业资格目录（历版） | 07 国职变迁、15 营养师身份 | ⏳ 待采集（P2） |
| 注册营养师管理办法 / 中国营养学会文件 | 15 身份战争 | ⏳ 待采集（P2） |
| 市场监管总局处罚公告 | 04 产品史、05 营销、06 监管 | ⏳ 待检索 |
| 广告法相关条款与判例 | 05 话术、06 监管 | ⏳ 待检索 |
| 药监局 GLP-1 类药物获批时间线与适应症 | 34 针剂 | ✅ 已采集 → [0039](evidence/claims/claim-0039-china-approval-timeline.md) ⚠️ **NMPA 批准日待查**（官网 412，三个流传日期皆为公告日） |
| 医保目录与价格公开信息 | 34 可及性 | ✅ 已采集 → [0040](evidence/claims/claim-0040-china-price-access-2026.md)（2463→1284.36 元；**减重适应症全自费**）⚠️ 324.12 元规格两源冲突 |
| AI 医疗器械与互联网诊疗监管文件 | 35 责任归属 | ✅ **原文已取得** → [0048](evidence/claims/claim-0048-china-ai-medical-regulation-liability.md)（CAC 令 15 号、NMPA 2021 年 47 号、国卫办医发〔2022〕2 号第 13/21/24/34 条）**已核实** |
| 个人信息保护法（PIPL） | 35 数据隐私 | ✅ **原文已取得** → [0049](evidence/claims/claim-0049-health-data-sensitive-pipl.md)（第 28/29/55/69/73 条，过错推定）**已核实** |

## 四、学术文献（A/B 级）

| 主题 | 用于 | 核查状态 |
|---|---|---|
| 代谢适应 / adaptive thermogenesis 经典研究 | 22 平台期 | ✅ → [0010](evidence/claims/claim-0010-adaptive-thermogenesis-magnitude-dispute.md) **有争议**（30–100 vs −500 kcal/d，反方须同等篇幅） |
| Biggest Loser 参赛者长期随访 | 22 反弹 | ✅ → [0011](evidence/claims/claim-0011-biggest-loser-six-year-rmr.md) ⚠️ **789/−504 已作废**，2016 更正为 664/−370；n=14 不可外推 |
| 瘦素、ghrelin 与减重后食欲调节 | 22 激素反扑 | ✅ → [0013](evidence/claims/claim-0013-hormonal-adaptation-persistence.md)（Sumithran NEJM 2011，DOI 已核实） |
| set point vs settling point 争论综述 | 22 设定值 | ✅ → [0014](evidence/claims/claim-0014-setpoint-vs-settlingpoint.md) **有争议，本书不选边** |
| NEAT / NREE 在能量限制下的变化 | 22 你确实不动了 | ✅ → [0012](evidence/claims/claim-0012-neat-decline-under-restriction.md) ⚠️ **Levine 1999 不可引**（过量进食研究） |
| 依从性衰减与摄入自报失真 | 22 最强竞争解释、05 平台期话术 | ✅ → [0017](evidence/claims/claim-0017-plateau-adherence-underreporting.md)（低报 47±16%）、[0018](evidence/claims/claim-0018-energy-balance-dynamics-plateau.md)（3500 kcal 规则错误） |
| 长期维持成功率与干预 RCT | 22 维持、35 AI 反方、36 落点 | ✅ → [0015](evidence/claims/claim-0015-nwcr-successful-maintainers.md)（⚠️ 幸存者偏差）、[0016](evidence/claims/claim-0016-weight-regain-timecourse.md)、[0019](evidence/claims/claim-0019-maintenance-intervention-rct.md)（**全书承重墙**） |
| BIA 体脂测量效度研究 | 20 秤的暴政 | ✅ → [0020](evidence/claims/claim-0020-bia-scale-validity.md)（个体层面不可互换，误差可达十余百分点） |
| DEXA 精度与局限 | 20 测量幻觉 | ✅ → [0021](evidence/claims/claim-0021-dexa-precision-limits.md)（设备间系统差异，生物学变异 > 技术误差） |
| 短期体重变化成分与日波动 | 20 日波动、05 七天瘦十斤 | ✅ → [0022](evidence/claims/claim-0022-daily-weight-fluctuation.md) 🚫 **「1–2 kg」原始出处未找到**；「钠锁水」被原始研究反驳 |
| 自我称重的益处与风险 | 20 数据焦虑 | ✅ → [0023](evidence/claims/claim-0023-self-weighing-maintenance.md)（成人 modest 益处；青少年与部分年轻女性可能有害） |
| 睡眠限制对食欲激素与胰岛素敏感性的 RCT | 23 睡眠 | ⏳ 待检索（P2） |
| 局部减脂 / 空腹有氧 / 碳水时序的对照研究 | 附录 B 真伪对照、05 话术解剖台 | ✅ → [0024](evidence/claims/claim-0024-spot-reduction.md) **有争议**、[0025](evidence/claims/claim-0025-fasted-cardio.md)（急性≠长期）、[0026](evidence/claims/claim-0026-nutrient-timing.md) **有争议** |
| 易胖体质 / 代谢受损 / 排毒 / 三分练七分吃 | 05 话术解剖台 | ✅ → [0027](evidence/claims/claim-0027-easy-gain-constitution.md)、[0028](evidence/claims/claim-0028-metabolic-damage.md)、[0029](evidence/claims/claim-0029-detox-toxins.md)（含严重不良事件与未申报药物）、[0030](evidence/claims/claim-0030-diet-exercise-ratio.md)（方向真、比例编） |
| 身材焦虑的性别结构与跨文化证据 | 05 性别小节 | ✅ → [0031](evidence/claims/claim-0031-gendered-body-marketing.md) ⚠️ **Karazsia 2017 下降；中国方向相反**；Grabe 2008 符号未明不得引 |
| STEP 系列（semaglutide）/ SURMOUNT 系列（tirzepatide） | 34 针剂效应量与局限 | ✅ → [0035](evidence/claims/claim-0035-step1-semaglutide-effect-size.md)、[0036](evidence/claims/claim-0036-surmount1-tirzepatide-dose-response.md) ⚠️ **非头对头，禁止比较优劣** |
| GLP-1 停药后体重回升研究 | 34 停药之后 | ✅ → [0037](evidence/claims/claim-0037-weight-regain-after-discontinuation.md) ⚠️ 引文纠正为 **Wilding DOM 2022 + Rubino JAMA 2021** |
| GLP-1 与去脂体重 / 肌肉流失 | 34 力量训练必要性、36 生理支柱 | ✅ → [0038](evidence/claims/claim-0038-lean-mass-loss-resistance-training.md)、[0060](evidence/claims/claim-0060-glp1-exercise-muscle-bone-fitness.md) ⚠️ **Look 更正已关闭（仅 Figure 4 图轴单位）；Batsis 勘误正文仍未取得**（PMID 42258831，Cloudflare 403 → **28.3% 非终局**）；**构成基本相同：药组 74/26 vs 安慰剂组 75/25**；**客观功能终点全缺，但 SF-36v2 自评功能药组改善** |
| GLP-1 不良反应与长期安全性 | 34 反方 | ✅ → [0041](evidence/claims/claim-0041-adverse-effects-longterm-gap.md) ⚠️「超过 5 年缺口」已撤回 → **约 3.3 年** |
| 食欲的生理机制（摄入 / RMR / 中介） | 34 机制 | ✅ → [0043](evidence/claims/claim-0043-appetite-physiology-not-morality.md)（−35% 摄入、RMR 不变、<1 pp 由胃肠不适中介） |
| 心血管硬终点与腰围中介 | 34 瘦≠健康 | ✅ → [0044](evidence/claims/claim-0044-select-cardiovascular-hard-endpoint.md)（HR 0.80，**仅约 33% 由腰围缩小中介**） |
| 肥胖污名与健康后果研究 | 33 道德叙事、36 身体意象 | ✅ → [0055](evidence/claims/claim-0055-weight-stigma-health-harms.md)、[0056](evidence/claims/claim-0056-obesity-heritability-not-destiny.md)、[0057](evidence/claims/claim-0057-fat-equals-lazy-attribution-stigma.md) ⚠️ 三张卡是三个论断，**不得计为一个论断的三个来源** |
| 进食障碍筛查工具（SCOFF 等）与诊疗指南 | 25 强迫边界 | ⏳ 待检索（P2） |
| 自我决定理论（Deci & Ryan）与身份认同 | 36 为什么还要练 | ✅ → [0058](evidence/claims/claim-0058-autonomous-motivation-identity-maintenance.md) ⚠️ 效应 small-to-medium、**创始人自评**；身份 r=.44 **无干预 RCT**；含阶级与意义叙事的强反证 |
| 运动对抑郁焦虑的效应与偏倚 | 36 心理支柱 | ✅ → [0059](evidence/claims/claim-0059-exercise-depression-effect-size-bias.md) ⚠️ **四个数必须并陈**；偏倚方向文献分裂；全部试验 performance bias 高风险 |
| 动机性推理 / 身份保护认知 | 29 撕逼解剖学 | ⏳ 待检索（P2） |
| LLM 健康建议质量与幻觉评测 | 35 AI 教练 | ✅ → [0045](evidence/claims/claim-0045-llm-health-advice-quality.md)、[0046](evidence/claims/claim-0046-hallucination-confidence-calibration.md)、[0051](evidence/claims/claim-0051-wearable-llm-health-agents-2026.md) ⚠️ **综述证据库止于 2025-02**；PH-LLM/PHIA **全 Alphabet 作者** |
| 视觉动作识别与运动纠错 | 35 能力边界 | ✅ → [0047](evidence/claims/claim-0047-visual-pose-form-correction.md) ⚠️「演示阶段」已作废（16 周单臂验证）；角度误差分米级 |
| AI 健康伪科普供给 | 35 末法加剧、30 算法 | ✅ → [0050](evidence/claims/claim-0050-ai-health-misinformation-supply.md) **已核实**；[0052](evidence/claims/claim-0052-ai-no-conflict-platform-has.md) ⚠️ 后半句为 **E 级推断** |
| 单病例实验设计方法学 | 24 n=1 | ⏳ 待检索（P2） |
| 行为改变技术（BCT）分类与效果 | 37 最小实践 | ⏳ 待检索（P2） |

## 五、需补：认证与教育（C/D 级）

| 来源 | 用于 | 核查状态 |
|---|---|---|
| NSCA / ACE / ACSM / NASM 官方认证要求与继续教育规则 | 07 证书通胀、17 继续教育 | 待抓取（注明日期并存档） |
| 国内"包过"培训机构公开招生文案 | 07 产业链 | 待采样（公开可见，脱敏） |
| 体育院校运动人体科学培养方案与就业质量报告 | 13 科班去向 | 待采集 |
| 医学院校课程方案（营养与运动占比） | 14 医学院不教肥胖 | 待采集 |
| Exercise is Medicine 官方资料与国内试点报道 | 16 运动处方 | 待采集 |

## 六、需补：社区田野（D 级）

| 来源 | 用于 | 核查状态 |
|---|---|---|
| 贴吧 / 豆瓣 / Keep 社区历史帖（公开） | 26 平台迁移、27 黑话 | 待采样（注明日期，脱敏） |
| 小红书 / B站 / 抖音 内容形态采样 | 26 载体约束、30 算法 | 待采样 |
| KOL 公开商业合作披露与翻车报道 | 28 信任经济学 | 待采集 |
| 生酮 vs 低脂等争论的公开帖 | 29 撕逼解剖学 | 待采样 |
| 营销素材采样（前后对比图、话术） | 05 焦虑定价学 | 待采样（只采公开可见，不存他人身体照片） |

**田野合规**：遵守平台条款；只采公开可见内容；不存可识别个人信息；不存他人身体照片；采样注明日期与平台。

## 七、访谈计划（D 级）

| 对象 | 人数 | 用于 | 状态 |
|---|---|---|---|
| 在职私教 | 5–6 | 03 劳动处境、07 认证、10 线上 | 待约 |
| 前教练 / 转行者 | 3–4 | 03 青春饭、07 证书通胀 | 待约 |
| 工作室主理人 | 2–3 | 08 业态、38 商业模式 | 待约 |
| 训练营营员（含青少年营，严格脱敏） | 2–3 | 09 封闭营 | 待约（伦理审查优先） |
| 注册营养师 / 临床营养科 | 2–3 | 15 身份、21 厨房 | 待约 |
| 内分泌 / 减重门诊医生 | 2 | 14 医学院、34 针剂 | 待约 |
| 体育院校毕业生 | 2–3 | 13 科班去向 | 待约 |
| 资深爱好者 / 社区维护者 | 3–4 | 19 自学、26–31 社区 | 待约 |
| 反复反弹者 | 4–5 | 00 序章、22 反弹、39 终章 | 待约 |
| GLP-1 使用者（含停药者） | 3–4 | 34 针剂 | 待约 |

提纲与知情同意模板见 [evidence/interviews/](evidence/interviews/)。原始录音与未脱敏转录不入仓库。

## 八、融入计划

| 阶段 | 主要素材动作 |
|---|---|
| **P0.5** | ✅ **已完成**：MVP 九章所需 A/B/C 级来源采集与建卡（57 张；P1 复核轮 +1 → **58**）+ INDEX 口径裁决 |
| P1 MVP | **人工复核签字 46 张「待核实」卡**；取 Batsis 勘误正文（Look 更正已关闭，仅图轴单位）；补 D/E 级人物素材；访谈暂缓 |
| P2 | 完成访谈计划；补齐行业数据与认证资料；补中国人群证据 |
| P3 | 社区田野采样；附录 B 真伪对照表逐条建卡 |
| P4 | 读者投稿融入；社区共建 claims |

## 九、来源冲突处理

- 中文报道与原始研究冲突 → 以原始研究为准，记录冲突
- 行业报告之间冲突 → 并列呈现，注明发布方立场，不强行取平均
- 作者经验与文献冲突 → 保留两者，标注 E 级与 A/B 级的差异，这本身是第 24 章的素材
- **同一数字在不同卡里口径不同 → 以 [INDEX §2 口径裁决表](evidence/claims/INDEX.md) 为准，不在正文里自行取平均或选边**
- **原文本身异常（CI 跨零写成显著、单位错、符号不明）→ 登记在 INDEX §5.2，不得直接引用**
- **来源已被列入黑名单（编造数字）→ INDEX §5.3，永久不得引用**