# 固定节点残差下界的最终独立审查

2026-09-08。PRIVATE_CORE。有限范围 PASS：同一固定 Q52/C¹ Hermite 参照在 t*=5/8 违反旧 r₂≤10^-7 e^-2t 包络；本次 24 模下界不决定 ε=2·10^-7。未发现阻断 NODAL_RESIDUAL_OUTCOME.md 这一限定结论的问题。

本轮实际全文读取最终下界合同、独立 Fraction 合同、比较实现、独立实现源码、结论稿和更新后的根复核文本；解析两份已完成运行的全部 24 模精确结果及其日志。NODE_TRIAL_OUTCOME.md 已全文读，但本次签核只覆盖新增残差段与共同科学边界，不重复认证其中全部旧生产、导数门和终点档案。

本审查者没有编写或运行这两个残差卷积实现。本轮另写并实际执行 check_nodal_final_records.py，只使用已有 F/R 分子分母作有限代数核对、解析资源记录及重算文件 SHA。没有解码节点、重跑 p+q 卷积、FFT、积分、模式选择或负对照。该区别也直接写入终审 JSON。

## 1. 固定模式、完整输入对和数学对象

实际 selection、主结果与独立结果的 24 个模式按同一顺序一致。它们恰为绝对坐标 (9,4,4) 的三个位置及全部符号，均有 |k|²=113 且在输入 G 外。此处线性项 d_k+|k|²c_k 精确为零，是有限参照支撑的结果，不能推广到输入 G 内或真实 NS 解。

每个输出的输入盒交集计数可直接解析得到

(17−9)(17−4)(17−4)=8·13·13=1352。

k 含一个奇数坐标 9，所以没有 p=q=k/2 的整数对；两两分组应有 676 个不同无序对。实际每模记录恰为 1352 有序对、676 双项和 0 对角项，总计 32448 对。这个计数核对不需要再次做卷积。

主实现逐字典序 p 保留每个合格有序对。独立源码逐系数 Fraction 共轭平均后作 P，再按 p<q 加入两个不同通道，p=q 单独一次；它没有把反序项粗暴乘 2。记录的有序对覆盖串 SHA 完全相等。独立程序只读取主运行字节作绑定，并从 selection 提取固定 K，没有读取主 exact-result.json 或导入主卷积函数来计算。

实际 K 共轭闭合，但原下界不依赖这一巧合，也未额外乘 2。独立源码最后对可配对输出另查残差共轭；这不是以对称性替代所选模式的实际卷积。

## 2. 比较实现与本轮额外记录代数核对

check_nodal_residual_agreement.py 先验证两份执行完成状态和固定节点；要求输出各有 24 项、模式顺序相同且主模式互不重复。逐模式核对 |k|²、配对计数和覆盖串 SHA，再比较

F_primary/D² = F_independent，

T_primary/(D²|k|²) = R_independent。

三个复分量的比较完整，分别是 72 个复 F 分量和 72 个复 R 分量。比较器还核对独立保存的线性项和投影项装配符号、每模 |k|⁴|R_k|²、总 Λ、P₃₂、必要 ε² 下界，以及两套不同约分方式的整数交叉乘积与差。P₃₂ 在脚本中从 5/(2j) 的有理递推重新得到，参数没有误用 2t*。

这个比较器面向当前严格正证据，明确要求 ΛP₃₂>10^-14；它不是对任意未触发记录都返回一致性的通用比较器。其行为与本次用途一致。

本轮新增的记录解析进一步从每模已经保存的 F 自行形成

P_kF=F−k(k·F)/|k|²，

核对保存的 projected_F；再由全体 k∉G 验证保存线性项为零，核对 R=iP_kF 的实虚符号、主 T 分母和两个结果的权重总和。该检查没有再次计算 F 的输入卷积，是对已有精确记录的后处理代数验证。

主记录的 D=2^53L、D⁴ 和 P₃₂(5/2) 也实际核对。全部结果一致。本轮记录状态为 PASS_EXISTING_RECORD_ARITHMETIC_AND_HASH_AUDIT，不能称为第三次独立卷积。

## 3. 严格否定旧门的可读证据

两种独立算术表示给出同一个精确 Λ。主结果保存 N/D⁴，独立结果保存约分 Fraction。完整分子分母保留原文件，不用小数替代。

本轮从实际结果独立解析并严格核对

Λ>83/10¹⁷，

P₈(5/2)=3588667/294912>121/10。

因为 exp(5/2)≥P₈(5/2)，有

||D²R(t*)||₂² exp(4t*)≥Λexp(5/2)

> (83/10¹⁷)(121/10)=10043/10¹⁸>10^-14。

所以旧 ε=10^-7 的节点不等式严格失败。主实际判据使用更强的 P₃₂，两个整数边与正差也被记录解析逐项核对。结论稿把近似小数仅用于阅读，证明依赖完整整数和以上有理比较，范围正确。

这是一处节点对全窗充分条件的反例。它不需要也没有得到完整残差上界；丢弃其它输出的非负 Parseval 项只会使下界更弱。所选输出内部的全部相消已经在精确 F 中处理。

## 4. 对 ε=2·10^-7 的结论仍未定

本轮实际有理解析得到

10^-14<ΛP₃₂(5/2)<4·10^-14。

因此已保存的必要 ε² 下界没有否定 (2·10^-7)²。还可以从同一结果直接核对更强的限制

13Λ<4·10^-14。

已有纯解析指数界 exp(5/2)<13 可由 e<11/4<25/9 得到：

exp(5/2)<(11/4)²·5/3=605/48<13。

所以即使用此 24 模的精确 Λexp(5/2)，也仍达不到新门的平方阈值。这排除了把 P₃₂ 截断的微小保守性误当成这里尚未作出新判定的主要理由。

上述事实仍不证明 ε=2·10^-7 可行。完整残差可能由其余输出或其它时刻违反新门；本轮没有计算这些新证据。不能用已有浮点总残差补充为严格下界，也不能事后扩大 K 来替换本次固定检验。结论稿对此已有明确限制。

## 5. 实际独立运行与负对照的证据范围

原两个卷积运行有各自源码、输入认证、环境和最终资源记录，且时间顺序为固定选择后执行独立核。主运行的落盘后 stdout 观测为 0.2912580829579383 秒、RSS 91602944 字节、目录 2752701 字节；独立运行的最终 stdout 观测为 0.701790250139311 秒、RSS 67174400 字节、目录 78516 字节。它们分别适用 60 秒和 120 秒的锁定计算预算，均低于各自上限。

本轮只重算了当前文件大小，分别仍为 2752701 和 78516 字节；没有重新测量原运行的时间或 RSS。独立外部 stdout/stderr 合计 3161 字节，与结论稿的含日志 81677 字节相符。主目录大小明确不含外部 tee 日志。未发现把数组访问次数当作实际耗时的问题。

比较记录保存了 F、R、weight、coverage、N、P32 六个内存变异的拒绝原因。源码的六次修改分别触发与标签对应的比较失败路径，原文件不被变异。本轮读取并核对这六条记录，没有重新执行它们。它们证明指定损坏被检测到，不是对全部潜在实现错误的穷尽保证。

原 exact-result.json 仍保留执行当时的 PROVISIONAL_UNTIL_RUN_LOG_COMPLETE_AND_INDEPENDENT_REVIEW，符合不可覆盖原始证据的做法。其后实际完成的 run、独立核、比较与本终审共同提供最终接受范围，无需回写原始记录。

## 6. 结论稿、恢复与不扩大范围

NODAL_RESIDUAL_OUTCOME.md 的主结论、模式/配对数、输入对象、两次运行、整数见证及新预算未定均与所读记录一致。NODAL_RESIDUAL_ROOT_REVIEW.md 已将执行前文字标为历史记录并追加执行后事实；NODE_TRIAL_OUTCOME.md 新增残差段没有把本次结果提升为原解结论。

本次确立的是固定参照与旧充分条件的不相容。它不是 ||u−v|| 的下界、真实 NS 的奇性机制或任意后验方法失败，也不否定原固定初值的全球性。新的 μ_j 全空间/全时间上界、完整连续残差上界及正控制比较仍须支付，原初值状态仍是 NO-CERTIFICATE-YET-FOR-FIXED-a。

我没有运行 git、修改原始证据、追加新模式、改动参数或触发其它研究/发布操作。后续只应使用保存的结果恢复，不自动重跑已成功的核。

## 7. 实际文件绑定和阅读深度

本轮实际重新核对比较记录的 18 条已有输入绑定。新增终审记录汇集 29 个实际字节绑定；下面再绑定该记录及其 stdout，共 31 项。

对 JSON 结果、运行/选择记录、日志、比较实现及独立源码作了实际阅读和相应解析。四份选择 NPY、原始节点块及模式表只重新读取字节计算 SHA，本轮没有重解码它们。主卷积源码以已核绑定关联根代理的全文源码审查，本轮没有再全文审查该主实现；不能由此声称所有文件都被同等深度重新证明。

实际运行的 check_nodal_final_records.py 及其结果、stdout 完整保留。它的检查限于本文件所述记录代数和哈希，不导入原核、不选择模式、不求和原始 p+q 作用。所有原始科学结果保持不变。

| 实际证据路径 | SHA-256 |
| --- | --- |
| `research/reverse/fixed-seed-global-screen/C1_RESIDUAL_CONTRACT.md` | `a001077c4e1828827a3e7738e154bdd1b02541ff44d63032a475e2f0b5017251` |
| `research/reverse/fixed-seed-global-screen/INDEPENDENT_NODAL_RESIDUAL_CONTRACT.md` | `ee8b7fb5ac4b3adaf8d131c8e7625a2687d694322bab9d9da0997654ca405c57` |
| `research/reverse/fixed-seed-global-screen/NODAL_RESIDUAL_CONTRACT_REVIEW.md` | `71738e047e2514c857fac571c665430af8c6f50e9526a0a86942cee1ac47dc12` |
| `research/reverse/fixed-seed-global-screen/NODAL_RESIDUAL_LOWER_CONTRACT.md` | `6d8dbc0bdc4f04416e84f4b9db6cdf4336dd066e7496b974f9429a88c35d9026` |
| `research/reverse/fixed-seed-global-screen/NODAL_RESIDUAL_OUTCOME.md` | `1ccfa93c7d69857251ff05a77ecc5bff24a5af2b0cb850a79e057ce9bc04931a` |
| `research/reverse/fixed-seed-global-screen/NODAL_RESIDUAL_ROOT_REVIEW.md` | `268f916366962cd210bebefdb59c11580b0f88beafdfd9a2d273d6c77e365a7a` |
| `research/reverse/fixed-seed-global-screen/NODE_TRIAL_OUTCOME.md` | `5a95b85195250051cacfcbdbdee95609785cad0a1d5dc5be31045b08bba062dc` |
| `research/reverse/fixed-seed-global-screen/RESIDUAL_COST_PREFLIGHT.md` | `dfc54d9be18ca0d47a5c4ea13433523327ff9f0f85691d512bdbcfeed646be4e` |
| `research/reverse/fixed-seed-global-screen/audit_nodal_residual_lower.py` | `855581a1ef55dc6bfe54b1823b01aec13dfb4fb724329ded6551ba6b919d6fdd` |
| `research/reverse/fixed-seed-global-screen/check_nodal_final_records.py` | `afee0f3a3b992256388b13bcbf9d827ea8f6a36a525130934acf32b140970ea9` |
| `research/reverse/fixed-seed-global-screen/check_nodal_residual_agreement.py` | `b39843e365dfb443b2d36449942a724a543713c9378069bb4a68ac024e69e5f3` |
| `research/reverse/fixed-seed-global-screen/independent-nodal-residual.stderr.log` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `research/reverse/fixed-seed-global-screen/independent-nodal-residual.stdout.log` | `e87c46f604244744e82418f3625dd0316eedf3892055596bd2c80f9d2e9dcccc` |
| `research/reverse/fixed-seed-global-screen/independent_nodal_residual_lower.py` | `42330a0e6eb67fb5dbde3022d81b7ed8b7c134eb8e3894bcf9627075e202b9ac` |
| `research/reverse/fixed-seed-global-screen/nodal-residual-independent-agreement.json` | `65a438c54c06207dc809908f81f7c1e265e4bba01765c3875c311b49e7cb6fea` |
| `research/reverse/fixed-seed-global-screen/nodal-residual-independent-trial-01/RUN_CLAIM.json` | `e7b8fef5e8eb09ce0fe27c3674f3812ce4122ec86671b08dcaa50a523f5e41bd` |
| `research/reverse/fixed-seed-global-screen/nodal-residual-independent-trial-01/run.json` | `afa6ff96f1f3654883c535902a4a2aa5c71e39ba858f7e9ca0ca913e34162609` |
| `research/reverse/fixed-seed-global-screen/nodal-residual-root-run.log` | `b2b0aeabe1196f3498d237072dce132fc4aad6fef440ac17627eada0e054298a` |
| `research/reverse/fixed-seed-global-screen/nodal-residual-root-witness.json` | `c8e3a6e77cffc661d91e831ceb7ec18146f38602a283c21c4673de2b8f3c330d` |
| `research/reverse/fixed-seed-global-screen/nodal-residual-trial-01/exact-result.json` | `ff1e7e8a1e7ed34d80bfb2d7c363ffd932d2437f0f7b1f6dcd3e07e5fa6de3d6` |
| `research/reverse/fixed-seed-global-screen/nodal-residual-trial-01/run.json` | `1c86e99028c1d279c2beddd7f932462112814720ebc71ffb5f737256079411be` |
| `research/reverse/fixed-seed-global-screen/nodal-residual-trial-01/selection-candidates.npy` | `40f08e4175f072bd64bade32bae893c38e5dd53104b509f13af83542e53294b9` |
| `research/reverse/fixed-seed-global-screen/nodal-residual-trial-01/selection-full-R35.npy` | `4a110149934828be3d3f461fec9ac10070ec5233073c0d4a9b12015e58f40933` |
| `research/reverse/fixed-seed-global-screen/nodal-residual-trial-01/selection-ranking.npy` | `b45dbc923c99309e54116c74f729c1b97c1574003464fa647745a0d351ca379b` |
| `research/reverse/fixed-seed-global-screen/nodal-residual-trial-01/selection-scores.npy` | `dd025653872a06bf1ee6cc8b6c1b75d8bcf7566b431d5a9cdc9e75023962d719` |
| `research/reverse/fixed-seed-global-screen/nodal-residual-trial-01/selection.json` | `62c066774e2e6d6c6ab20e6d9b4f92b5599c9acda7bf64420a819997ec5f3d69` |
| `research/reverse/fixed-seed-global-screen/node-trial-01/block-01280-01343.npz` | `abf3b33282ff0b08e995c6aa1f80e7d79dbd64a55137574b77d51356b236297e` |
| `research/reverse/fixed-seed-global-screen/node-trial-01/manifest.json` | `5ac2abdfb7a14a38904f2ef1c58d81cf90bea776ce5426a56a75c6f81622c1cd` |
| `research/reverse/fixed-seed-global-screen/node-trial-01/modes.npy` | `f184c97c52e561ac53b8936ee51e68690517ad65c79e8050c93a891ac8856896` |
| `research/reverse/fixed-seed-global-screen/nodal-residual-final-record-check.json` | `24acfd7dd2d284bc6b7c1a2861f0b5a9380d63ad280fc021b3e08a2b2138c32f` |
| `research/reverse/fixed-seed-global-screen/nodal-residual-final-record-check.stdout.txt` | `f401b72e5c2276ef8b65c7a5af1d275c9530ca9eac25177a34222c311b2a5311` |
