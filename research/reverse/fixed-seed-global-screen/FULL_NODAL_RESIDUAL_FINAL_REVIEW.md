# 完整固定节点残差结果终审

2026-09-08。PRIVATE_CORE。**PASS：本次完整单节点结果及最终 OUTCOME 的有限范围科学审查通过。** 同一参照节点的零阶门通过，二阶指定 \(\varepsilon=2\times10^{-7}\) 包络严格被拒绝。该结论不涉及原 NS 解的正则性或奇性。

本次绑定的 FULL_NODAL_RESIDUAL_OUTCOME.md 为最终字节 223c963e10ae14c93a231901dfe1554b8c61b63324537ebc250ddb7ae15d32ee。未发现需要修改该结论稿的错误。另行研究的控制族短注不是本节点结果的依赖，本审查不覆盖它。

## 1. 作者分工和实际审查范围

主科学核及 OUTCOME 作者为 Pascal，独立 Fraction 科学核作者为 Pauli；本审查者未编写这两份科学核或 OUTCOME。已实际读取两核源码、对应执行合同及代码审批、NR 数学合同、两层数学审查和实际 run/result。此次持续工作先读完整程序，再对最终固定源码的原输入连接、直接卷积、残差与根号/结束路径补读核对；不是只看状态或作者摘要。

check_full_nodal_agreement.py 由本审查者编写。它的非作者实现审查属于根代理，实际文件为 FULL_NODAL_COMPARISON_ROOT_REVIEW.md，绑定最终比较器 a32fce39a8ed4922e6579a77dcc15673aa3cee6a2a8c7dc58577ab96b1329235。根代理在审读后执行了比较器。本轮读取该实际比较结果并核对记录连接，**不把本人自读比较器称为它的非作者审查，也不声称再次独立逐项复算全部数组。**

两条科学路径明示共享原参照节点、96位中心、旧 \(T^{12}\) 和 NR 数学定义。实现分离体现在新五张量分别用整数打包乘法和完整有序对直接循环，原值/斜率分别按共同分母及逐分量 Fraction 重建，残差分别用整数 V 和直接 Fraction 形成。独立源码的输入入口没有本轮主源码或新结果；其完成记录仍保留未读主结果的字段。这里的独立性不表示两条路径没有共同数学接口或共同旧数据。

## 2. 科学计算与数学合同的连接

两核都限定原唯一 Hermite 参照在 \(n=1280,t_*=5/8,\nu=1\)。原值和物理时间斜率从同一 Q52 档案分别共轭平均、投影；整数加减前先提升，G 保留4912个正负模式。斜率没有从中心非线性反推，原固定初值和参照未更换。

主核另外五张量共15次实大整数乘法；独立核另外五张量执行120638720个完整有序输入对。旧 \(T^{12}\) 只复用。空间索引恢复的是 H 上物理输出 \(k\)，六个张量重建时非对角项无额外倍数2。

所读两核均保持原精确线性项和完整保守 Leray 非线性。主路径
\[
L=J+sA,\quad N=sF-k(k\cdot F),\quad
V=sQP^2L+iDN,\quad \widehat R_k=V_k/(DsQP^2)
\]
与独立路径
\[
\widehat R=d+sc+iP_kF/QP^2
\]
一致：实部减去非线性投影的虚部，虚部加其真实部。中心不被假设为无散；G 外线性项零而非线性仍保留。零频率单列，不能用 \(s=0\) 除法。

两核分别保存并回读完整输出。主二阶使用全有序 \(D^2\) 的 \(s^2\) 权重抵消 Leray 分母平方，得到 \(A_2/H_0\)；零阶逐模式对 \(S/s^2\) 作商余包围。独立核从已回读的约分残差分量直接求精确两平方范数。固定128位根号根据真正有理平方等号取上端，指数使用固定32阶有限和与解析尾界。没有浮点残差或浮点指数进入严格比较。

“完整”指这份有限 Fourier 参照的完整方程残差，包括它产生的全部 H 输出、压力投影和有符号相消；不表示实际原 NS 解被证明有限谱。直接逐项比较的场是 \(\widehat R\)，原参照的
\[
R=d-\Delta c-B(c,c)
\]
通过已审 \(E_j=28^{j+1}(2M\delta+\delta^2)\) 在范数层作双边连接。不能把中心场逐项相等改说成已经逐项精确计算未舍入的原非线性。

## 3. 实际完成记录与比较证据

两条科学核记录的源提交均为 10df40f9bbebbe3086f3a7d0bc1a1d5301fb4505。主 run 为 COMPLETE，独立 run 为 COMPLETE_FULL_NODAL_INDEPENDENT；独立 result 与 run 的来源、输入、配置、checkout 和输入扰动字段相连。

实际 full-nodal-agreement.json 的 SHA 为 f2ccad0d3a963e1a0bdbf0e9695e2979271807201ef3427964b2a11052511ed8。读取的完成记录给出：

- 五个新张量359370个实虚整数标量全部相等。
- 全215622个中心残差有理分量相等，35937个 V/S 输出的平方和、共轭、无散及零频率检查通过。
- 独立二阶精确平方范数等于主 \(A_2/H_0\)，独立零阶精确平方范数位于主整数包围内。主非整除计数为8520，区间宽为 \(8520/H_0\)。
- 两核的 M、δ、E、根号区间、指数门和最终资源相连。相同区间端点不是比较器的先决条件。
- 68项来源字节绑定通过，10个小型负对照被拒绝。其中9项是已保存记录或标量的内存变异，1项是明确标记的微型合成根号边界；原文件未修改。

本轮核了该比较 JSON 与其 stdout 中的完整 comparison 对象、结果 SHA、拒绝数及状态一致，stderr 为零；没有再次执行这些逐项检查。29份小文件/记录另核实际字节，其中22份同时匹配该既有68项表中的对应绑定。未重新读取或散列原节点数组和科学二进制；完整数组证据沿用已通过审读并实际执行的比较记录。

两次实际运行的写后资源与结论稿相符：

| 运行 | 最终墙钟（秒） | 峰RSS（字节） | 最终目录（字节） | 含外部日志（字节） |
| --- | ---: | ---: | ---: | ---: |
| 主核 | 7.769261500099674 | 119848960 | 46985943 | 46987840 |
| 独立核 | 15.00825629197061 | 87588864 | 24673201 | 24746303 |

本轮仅用目录项 stat 复核字节总额，并连接末行 stdout 和 run SHA。run 中较早的46985909/24673010字节快照不被冒充写后大小。两核 stderr 均空，已观测资源低于60秒、256MiB、64MiB。该事实不预测其它节点或全时间窗的成本。

## 4. 严格显示与结果边界

本轮以标准库 Fraction 对实际存储端点作少量显示检查，没有重算根号、指数级数、投影、残差或卷积。10条显示关系分别核两核的两组区间、两个 E 上界和两核的两条门不等式；相应精确整数、分数及实际输入 SHA 保存在 full-nodal-final-review-record.json。

两份原参照残差区间均被以下精确有限小数向外包围：

\[
r_0\in[6.33755528910368,\ 6.33755528910388]\times10^{-10},
\]
\[
r_2\in[6.8193426839974872,\ 6.8193426839989922]\times10^{-8}.
\]

已实际验证这些端点就是结论稿声明的 \(10^{24}\) 精度向下/向上整数端点；\(E_0<9.59813567\times10^{-24}\)、\(E_2<7.52493836446\times10^{-21}\) 的严格显示及 \(10^{32}\) 向上取整也成立。

对记录中已保存的端点与正指数包围的乘积，另核
\[
r_0e^{5/4}<2.21202414709\times10^{-9}
<1/320000000,
\]
\[
r_2e^{5/4}>2.38018447116\times10^{-7}
>1/5000000.
\]
因此零阶节点门通过，二阶指定门被严格拒绝。下界已减去 E，所以不是仅对舍入中心的拒绝，也没有借用旧浮点诊断。若坚持这份参照的 \(r_2(t)\le\varepsilon e^{-2t}\)，仅此节点就要求 \(\varepsilon>2.38018447116\times10^{-7}\)；本项未检验更大参数是否可行。

OUTCOME 正确区分了这份统一包络被一个节点否定，与其它时间依赖包络或其它后验方法的未定状态。零阶单点通过没有认证其全窗；二阶单点拒绝没有给原 NS 误差下界，更没有证明有限时奇性或全局正则性。原固定初值的状态仍是 NO-CERTIFICATE-YET-FOR-FIXED-a。

## 5. 最终绑定

本轮没有新增可执行复算器，只保存一份紧凑的实际记录连接/显示检查 JSON。它包含29项本轮输入 SHA、10条显示检查、实际资源连接及操作排除范围。下表加上该记录共30项，路径相对反向科学树根目录。

| 实际输入 | SHA-256 |
| --- | --- |
| research/reverse/fixed-seed-global-screen/C1_RESIDUAL_CONTRACT.md | a001077c4e1828827a3e7738e154bdd1b02541ff44d63032a475e2f0b5017251 |
| research/reverse/fixed-seed-global-screen/CONTINUOUS_RESIDUAL_COST_PREFLIGHT.md | 0c7ea4b3d33d152f298058a909e446505150d1004529f1a4518c2e1fedc7f796 |
| research/reverse/fixed-seed-global-screen/CONTINUOUS_RESIDUAL_COST_ROOT_REVIEW.md | 4865cf0639e20bc6d8d6c2546e8382c08b59366814168ff2f0b309bc8ef4e5da |
| research/reverse/fixed-seed-global-screen/FULL_NODAL_COMPARISON_NOTES.md | 638dee5e4490aceeac85bf78c65fbbfc2f174685d095bf9b7ca55828666bcbb8 |
| research/reverse/fixed-seed-global-screen/FULL_NODAL_COMPARISON_ROOT_REVIEW.md | 3b6d875cab09d8c7eb81844e90b9b85d1f7b1771a89f3cb389ee10d4f1864321 |
| research/reverse/fixed-seed-global-screen/FULL_NODAL_EXECUTION_CONTRACT.md | 879deca7e881073dc3fc31506aaf681e7d243d068621092fe361fc60963ae40c |
| research/reverse/fixed-seed-global-screen/FULL_NODAL_EXECUTION_INDEPENDENT_REVIEW.md | 5f1c40039f8de23250ef103c16e2991535dadaa4824c4f05e8cc045c75b55e53 |
| research/reverse/fixed-seed-global-screen/FULL_NODAL_INDEPENDENT_CODE_REVIEW.md | f6185da959f93adcca2ad77de6f66fa52fb063d559023db9e09c10f8f43a56aa |
| research/reverse/fixed-seed-global-screen/FULL_NODAL_INDEPENDENT_EXECUTION_CONTRACT.md | 61450a286e2f300f4444a29b45fa53fe93ec1b655fab3b4f03afb4261e93307c |
| research/reverse/fixed-seed-global-screen/FULL_NODAL_PRIMARY_CODE_REVIEW.md | a28d49df6c91012f57fe2a086b2b4a4d205698187484685b755514770865e182 |
| research/reverse/fixed-seed-global-screen/FULL_NODAL_RESIDUAL_CONTRACT.md | f3c5327e59931a2e638c039078f78175f4138c53eec139cc57c1ae5fd2cb513b |
| research/reverse/fixed-seed-global-screen/FULL_NODAL_RESIDUAL_INDEPENDENT_REVIEW.md | 5a1341a58a93582b31a56a33d10a296499ed921daa2c5dac7ee9d27369c87ece |
| research/reverse/fixed-seed-global-screen/FULL_NODAL_RESIDUAL_OUTCOME.md | 223c963e10ae14c93a231901dfe1554b8c61b63324537ebc250ddb7ae15d32ee |
| research/reverse/fixed-seed-global-screen/audit_full_nodal_residual.py | 54af5a2eac8be72acacef40f1be73ba00916704d64aef539d4459375a9d18e8c |
| research/reverse/fixed-seed-global-screen/audit_full_nodal_residual_independent.py | 6b65b6f536d77c544c8803832eadcf37c72568f951a9982edf40e73dbc272fbf |
| research/reverse/fixed-seed-global-screen/check_full_nodal_agreement.py | a32fce39a8ed4922e6579a77dcc15673aa3cee6a2a8c7dc58577ab96b1329235 |
| research/reverse/fixed-seed-global-screen/full-nodal-agreement.json | f2ccad0d3a963e1a0bdbf0e9695e2979271807201ef3427964b2a11052511ed8 |
| research/reverse/fixed-seed-global-screen/full-nodal-agreement.stderr.log | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| research/reverse/fixed-seed-global-screen/full-nodal-agreement.stdout.log | 0dff347542377e124c41fd487570294b5be51aa95e01151e5954d6509c06205c |
| research/reverse/fixed-seed-global-screen/full-nodal-independent-check-only.json | 8db20c0b6b6f7d2deb01e1ecace14fef92432a914d46f0dd2b4ebd027c970695 |
| research/reverse/fixed-seed-global-screen/full-nodal-independent-trial-01/result.json | e637e7fcde5f2fa8ac7cf55d635ada579f6fae189ebf903b6a7a018c351e393b |
| research/reverse/fixed-seed-global-screen/full-nodal-independent-trial-01/run.json | b197dc3cf405e191a7f4b7ca5076e7f04b2c812c22f6610e878972ff9957039e |
| research/reverse/fixed-seed-global-screen/full-nodal-independent.stderr.log | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| research/reverse/fixed-seed-global-screen/full-nodal-independent.stdout.log | 2b7b3da465b45286e5e046f8ac13ac97c563c73af0247c21c95d403f20a1a500 |
| research/reverse/fixed-seed-global-screen/full-nodal-primary-check-only.json | d249fb91c2b5f552a699ccc85861b06b374a3e42256dfce90da056a375381fbc |
| research/reverse/fixed-seed-global-screen/full-nodal-primary.stderr.log | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| research/reverse/fixed-seed-global-screen/full-nodal-primary.stdout.log | d0188f972afcb8dde652fe50a637dae03861f0e1b15b443e85c9b32b3ceb3f9d |
| research/reverse/fixed-seed-global-screen/full-nodal-residual-trial-01/run.json | 1f2f85bc1fc2c6e48f37a525c8ce1b790b873be532176cff7f00c9a0b7bb0dd7 |
| research/reverse/fixed-seed-global-screen/kronecker-independent-agreement.json | 5510285fed346165e428bac4dfcb572548283322937a712be6465829481b5779 |
| research/reverse/fixed-seed-global-screen/full-nodal-final-review-record.json | 2c7be5ae420978d9fbddd39a503b0814558bbef971f4e9bedd9efec12704d713 |
