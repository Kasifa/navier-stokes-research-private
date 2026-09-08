# 策略来源、实际阅读与版本台账

2026-09-08，PRIVATE_CORE。本文只组织本次策略调整的来源与阅读元数据，不是新证明、文献全文复核、外部独立证明审查或新颖性判断。原目标仍是固定正黏性、无外力、固定三维环面、同一允许初值的同一完整 NS 解。外部方法的可借用部分与尚未支付的迁移条件，按当前 STRATEGY 和原比较报告登记，不因收录为来源而成为本地已证接口。

台账作者为 coherence_independent_resumed，是前项六载波 A/B 源码、代数记录及接收支持预筛的作者；有既往研究接触。本小节本人全文读的是当前 STRATEGY、原报告 README、原 reverse audit 和来源 manifest；对下列 PDF、论文源码及内部证据只作本次列明的 SHA-256 核验，没有新增原文段落阅读或重新执行科学计算。根与两位审者的本轮原文阅读范围来自根明确传达的阅读证言，分别署名登记，不能改写为本人实读或全课题盲审。

## 1. 外部公开稿：准确标题、URL 与当前本地字节

标题、作者与原始 URL 沿用原报告，未进行新的在线检索、下载或在线版本核验。三份现存 PDF 的 SHA 均与原 manifest 一致；这固定的是本地下载快照，不是网站以后版本。

| 原稿 | 本地快照（相对原报告目录 sources/） | 本次实际核得 SHA-256 |
|---|---|---|
| Levent Alpöge、Tristan Buckmaster，**[Blowup for the Euler Equations with Smooth Forcing](https://cims.nyu.edu/~tristanb/euler.pdf)** | euler.pdf | 97ef408bff09b4f6ed9f3867734d1eb2245f3f34e6334b28136c84c02d0ae8d8 |
| Levent Alpöge、Tristan Buckmaster，**[Blowup for the Boussinesq Equations with Smooth Forcing](https://cims.nyu.edu/~tristanb/boussinesq.pdf)** | boussinesq.pdf | 895a628d1783bcb039374686f50b895b5f450f53b8ef8aa173523487a7a4a21b |
| Levent Alpöge、Tristan Buckmaster、Matei P. Coiculescu，**[Extending the Córdoba-Martínez-Zoroa IPM Blow-Up to Uniformly Space-Time Smooth Forcing](https://cims.nyu.edu/~tristanb/ipm.pdf)** | ipm.pdf | b3ebdbb8d9a93dcca5f3b3f8796e63f7f28b48e0b0e258b909110a4b69c72a12 |

本地快照目录为 /Users/kasifa/Documents/Math/reports/2026-09-08-fluid-blowup-comparison/sources/。不将前作 arXiv 编号安到这三份新标题上，也不据原报告当时未找到编号的记录断言此后没有编号。

| 原稿 | 本轮阅读者及实际范围：以下为传达证言 | 策略用途与不适用边界 |
|---|---|---|
| Euler | 根 /root：PDF 第 2、95–112 页全文文本阅读；另视读第 104、109 页。不是全文重证。 | 报告所列模型为三维全空间有旋轴对称、零黏性、含构造的光滑外力。策略取其固定序列、因果历史、各固定导数阶可和尾、有限总物理时间及终端下界的证明组织。它没有支付当前周期正黏性无力 NS 的跨代残差。STRATEGY 特别区分页 109 的方向锥符号 ν 与 NS 黏性。 |
| Boussinesq | Hume：PDF 第 1–14、37–39 页文本阅读，视读图页 8、10、13，并手核 Lemma 3.1。根 /root：第 3、4、8、10、13、39 页定向阅读；式 (4.10) 位于第 39 页。这两份范围均不能写成全篇复核。 | 报告所列模型为二维全空间无黏、无热扩散、温度与动量双强迫系统。策略取 §1.2、Lemma 3.1 与 Theorem 3.2 中放大、转向、最新层部分幅度回零而保留梯度增益的条件组织。独立温度场、双场相位条件和第 39 页基流强迫不能删除；当前 NS 尚无相应完整状态返回机制。 |
| IPM | 本轮没有原文复读；本人仅核 PDF 字节。模型与结论继承原报告，未再读其 external-boussinesq-ipm 审查或重新审查原证明。 | 报告所列模型为二维环面 IPM，速度由 Darcy 非局部关系决定。低阶终端收敛与梯度发散并存可作量词比较；不能成为当前 NS 的迁移定理、迹反例或再生输入。本次策略不以它另开机制。 |

上述 Euler/Boussinesq 定向阅读已比仅核摘要更具体，但仍没有重证整条外部爆破构造。阅读范围和结论身份不能由页数、哈希或审者称谓扩大。

## 2. 两篇本地论文：定向适用性阅读与稿件绑定

以下题名取自原 reverse audit。没有从历史论文 URL 推断今日在线状态、arXiv 发表身份或公开许可；本台账只给实际本地稿件路径。

| 本地论文 | 本轮阅读者及范围：根传达的证言 | 策略中的有限用途 |
|---|---|---|
| **Projected-Lamb Heat Packing and Sharp Trace Obstructions for Three-Dimensional Navier–Stokes Flow** | Pasteur：main.tex 第 735–1068 行及相关定义搜索。本人本次没有读取该段原稿。 | 仅在事件与分母准确对应时，核查裸时间预算统一支付入壳/出生原子的过强估计；报告的正时间精确解事件、缩放差和条件占据表示不能改写为当前同一初值的反复事件总占据控制。未排除的临界或附加费用估计保留。 |
| **Heat-evolved Chebyshev edges and localized fluxes of sparse Fourier shears** | Pasteur：quantitative-edge.tex 第 1–160 行、parabolic.tex 第 131–183 行；frame-and-mass.tex 与 discussion.tex 全文。本人本次仅核这些文件及 main.tex 的字节。 | 仅在候选满足正标量热表示、包络/鞍点与反馈精度等前提时，借用直接控制较小相对效应的误差组织。当前有符号 Leray 向量没有自动获得这些前提。精确剪切的每个序列成员固定初值全窗结果不等于同一初值实现整个参数序列，也没有涡拉伸或再生机制。完整质量、漂移和观察系的区别不能略去。 |

这是对内部研究可用性的定向阅读登记，**不是外部独立证明审查**，也不能替代这两篇稿件各自的文献与证明审核。尤其不能把只读 parabolic.tex 第 131–183 行写成已由本次 Pasteur 阅读覆盖第 243 行后的全部通量商推导；这部分比较仍是原 reverse audit 的已读报告内容。

Projected-Lamb 根目录为 /Users/kasifa/Documents/Math/navier-stokes-arxiv-paper/papers/projected-lamb-trace-obstructions/；Heat-edge 根目录为 /Users/kasifa/Documents/Math/paper-edge-v2/papers/near-edge-extrapolation-and-parabolic-shear/arxiv/source/。

| 稿件文件 | 本次实际核得 SHA-256 |
|---|---|
| Projected-Lamb main.tex | 897049f700b8209a42185729000be195917fee2ee30844278645fad60db9ec20 |
| Heat-edge main.tex | 2851cebf1a72779f071611d0239a799cb7434788df1a9c747649e48c754659ed |
| Heat-edge sections/quantitative-edge.tex | fd091c50680d13c762da81ef4f388914293f11156c4c25f944f3b04a2b02dddb |
| Heat-edge sections/parabolic.tex | f9aa54130790581ab37e2d4060ed5ad9accb80a341275f73084db0e5e2e523b4 |
| Heat-edge sections/frame-and-mass.tex | a430ec1536cf92b9f50759bb847b005dd3c3bd569d2db50bcbf2bde07e3c35bb |
| Heat-edge sections/discussion.tex | 0a4c9619c6ea711c7267743ecbe70e8a15ed3ea887372c2f96e6bda35b7f0f51 |

两个 main.tex 的当前 SHA 与原 audit 相同。原 audit 记载 Projected-Lamb 对应提交 f799b7cd619f71a585c6d59d8c83cad1a61480b5，Heat-edge 准备稿对应 9ff88b3455894a2ac27bbcec8ecd669435a58a4f、研究冻结 ee014e3d8d332282b6e708aaa73dec23ed275b69；本台账只转录这项历史对象核对，不执行 Git，也不声称重新核对了这些提交。

## 3. 本地反向来源与比较边界

原 reverse audit 已区分固定初值的真实有限来源、固定接收图的秩障碍、新六载波现存输出与最终接纳。本文继承其有限范围，不把当前研究退写为只有形式首项，也不把这些有限结果升格为无限层。

- 第 22 包：固定数据的初始空带出生、真实两层短窗来源及局部完整 NS/无限尾；仍缺跨代统一反馈与误差。
- 第 23 包：同一旧初值、固定 16 接收及门槛下的秩一障碍和共线投影内部自作用零；不是所有图或所有实际时间的普遍排除。
- 六载波：原报告截至 22:27:22 已读 C 输出，明确不据输出自动登记新冻结。此为报告快照，不用它判断本文写作之后的汇总接纳状态。本台账只核该现存输出和主稿字节，不重审 C、不运行 A/B/C。
- ENERGY_SCREEN：按原 audit，约束指定高频包自身复制合同下的固定能量/固定模态数，不排除包外供给、模态数增长或局部浓缩。
- 新接收支持预筛：本作者已单独完成固定 D 二和的最少 F 叶数与同频零门，文件保持停定。该结构结果不能代替实际较短响应的非零证书，也没有支付下一次真实来源归因。

下列均为本次元数据核验；除刚完成的本人预筛及此前已说明的六载波主稿阅读外，本台账不新增这些科学文件的全文阅读声明。

| 文件（相对本反向树 research/reverse/） | 本次实际核得 SHA-256 |
|---|---|
| four-carrier-source-test/freeze.json | 20e78c169751fe851fa39019d6a5facd7b3dfb3fc63c9944d8c62a3f8802f679 |
| four-carrier-source-test/PROOF.md | 38668542aa347bca09537312a964125c52ec31f34ed335807c5914fae1014164 |
| four-carrier-band-extension/freeze.json | c8a99aec270304275e8e5a91ae6c6d3de31b86669ff19735f7edd45d4468a432 |
| four-carrier-band-extension/FINAL_SCOPE_REVIEW.md | 4b374637c8acd239195c06654ebe72a52650f786b18a952fd34e6ead0c5b5a36 |
| cyclic-six-carrier/PROOF.md | afd6b0009d7b357dd9ed6c9feaeb8dbb15535a5499dbd8be7911883e3c4f2725 |
| cyclic-six-carrier/verify-cyclic-output.json | 8e996350ed8702c17c6dcdd1f80f2f08b57a7a90c43b43d3e78ec348697e1268 |
| route-screen/ENERGY_SCREEN.md | 12e1ad7ec85b2e46c91bc6dc525c88d4ab688ffcd1b556ab96004125573ec6cc |
| cyclic-receiver-supply-preflight/PREFLIGHT.md | 841cc7e26a4d8b8c3e8f930e2a2da47824fdcba43cee1fd37e40864a32cf5b58 |

## 4. 本人本次全文阅读的组织来源

| 来源 | 当前读取快照 SHA-256 |
|---|---|
| [当前 STRATEGY](/Users/kasifa/Documents/Math/navier-stokes-reverse/research/reverse/strategy-20260908/STRATEGY.md) | 6bee8ae3d335d8064055f2022978958897bffd05896ab03f5096a8e87ced8a42 |
| [原报告 README](/Users/kasifa/Documents/Math/reports/2026-09-08-fluid-blowup-comparison/README.md) | 695cb01818fe9754c1cd029aab5ac059cb0b4f789b36ffcad1ed8d8891aa46e4 |
| [原 reverse audit](/Users/kasifa/Documents/Math/reports/2026-09-08-fluid-blowup-comparison/audits/reverse-papers-comparison.md) | d94bba6e0e619c0d69c774fe8777367de4e5370ff260e35142a2cff73f867a81 |
| [原来源 manifest](/Users/kasifa/Documents/Math/reports/2026-09-08-fluid-blowup-comparison/sources/manifest.json) | 7cf06e958c86ecbbda0a4233a58413952f2538a38e2aea8b4ac8c2fd8d145320 |

原报告自己的“已读附件、关键页面及外部终端收束段”的说明属于报告作者身份，不是本台账作者的新阅读。原报告包含正向及其它背景比较；本台账没有据此读写正向工作树或将其纳入新的证明输入。

本轮无 IPM 原文复读，无 Lean 源码重读、编译或内核重放；不把报告中的公开工程入口、作者自报状态或形式化元数据写成我们的独立验收。未复核全部外部引理，没有新科学程序、参数选择、扫描、Git、外发或发布。只写本文件，全文自读后另报最终 SHA 并停改。当前 NS/Clay 总目标仍为 OPEN / NOT CLAY；来源台账不增加任何已付再生机制。
