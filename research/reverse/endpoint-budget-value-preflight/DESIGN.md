# 固定十七端点的预算价值侦察设计

2026-09-09，PRIVATE_CORE，**DESIGN-ONLY / NUMERICAL_VALUE_ONLY；当前科学 worker 0、数组打开 0。** 本人是 BF/RE/FG 作者、AP 非作者审查者，也曾审读旧核与轨迹记录；本稿是具体应用设计，不称第三证明或盲审。只采用下列已停定公式为条件输入，不替尚在收口的整个成果包宣告接纳；本设计不进入该包。

固定 trajectory160_512 的原 17 份完整 U，旧整数步标 0,32,…,512 对应准确 \(t_j=jT/16\)，\(h=T/16,\ b=t_{15}\)。原 \(a_*,\nu=1,T\)、N160/K53 均不改；\(H_0=\{4\le|k|<8\},H_1=\{8\le|k|<16\},N_1=\#H_1\)。只做一个固定后处理，不积分新轨迹，不读取保存 G/W 来替连续历史。全部范数采用归一化 Haar、复分量 Hermitian 长度与全部 signed 模；旧 energy_normalized 是半个平方 L²，不能直接当 M²。

## 1. 同一个精确目标与浮点对象

记 \(C_q=\{k\in\mathbb Z^3:|k|_\infty\le q\},F=C_{53}\setminus\{0\}\)（下文简写 C53 等），按 AP.1 定义准确 \(X_j=\Pi z_j\)，其中有限 binary64 端值先视为二进有理数，\(\Pi=P_F\mathbb P(I+J)/2\)、\(Jz_k=\overline{z_{-k}}\)。准确 \(D_j=\Delta X_j+P_FB(X_j,X_j)\) 在相邻两段共用。它们定义 AP 的全窗 C¹、逐段三次 v；本轮尚未构造它。

未来浮点程序近似这些定义：完整核对频率/正负索引后作 Hermitian 平均、Leray、去均值及 F 投影；保留投影改变量、均值/共轭/散度诊断。得到的浮点 \(\widetilde X_j,\widetilde D_j\) 不自动等于准确 X/D，也不能仅凭小诊断称精确无散。原 a_* 未改；AP.2 的初始差不增只适用于准确 \(\Pi\)，不能把新增投影/FFT/舍入误差删除。

每个 j 恰做一次 N160/K53 的完整旋转核 \(P_F\mathbb P(X_j\times\operatorname{curl}X_j)\)，加 \(-|k|²X_j\) 得 D；保存全部 H₀ 端值/斜率及末端 H₁。核中双向 FFT 均 norm=forward，不取实部、不漏复相位。精确目标上旋转式等于完整有序 \(B=-\mathbb P((X\cdot\nabla)X)\)；浮点实现差不由此恒等式认证。

N160 只支付所需的保留输出：输入两次均在 C53，真二次支持在 C106，而真输出与任一保留标签的坐标差至多159<160，故无折返别名进入 C53，也覆盖 H₀。它不提供完整 C106 输出。末端另按整数标签零填充到 **N216、K=None、无 2/3 或 K71 掩码**；216>212，故整个 C106 可无别名容纳。此网格只求一次 B，不推进 NS。

固定 \(S=((F+F)\setminus F)\setminus\{0\}=C106\setminus C53\)。外立方带每个标签均可按坐标拆为两个 C53 非零输入，故该等式不依赖实际系数活跃性。一次保留整个 S 的所有正负模，节点残差目标为 \(-P_SB(X_{16},X_{16})\)，不得挑较大的模或把非零潜在支持当非零系数。

## 2. 完整 Bernstein 平方范数与 FG 上界候选

在第 j 段令 \(A_i=P_{H_0}X_i,\ Z_i=P_{H_0}D_i\)，三次 Bernstein 控制向量
\[
C_0=A_j,\quad C_1=A_j+hZ_j/3,\quad C_2=A_{j+1}-hZ_{j+1}/3,\quad C_3=A_{j+1},\qquad
P_{H_0}v(t_j+h\theta)=\sum_{i=0}^3 C_i {3\choose i}\theta^i(1-\theta)^{3-i}.
\]
内积为全 H₀ 的复 Hilbert 内积，平方取实部；产品恒等式给
\[
\|P_{H_0}v\|_2^2=\sum_{m=0}^6 q_{jm}{6\choose m}\theta^m(1-\theta)^{6-m},\qquad
q_{jm}=\sum_{i+\ell=m}\frac{{3\choose i}{3\choose\ell}}{{6\choose m}}\operatorname{Re}\langle C_i,C_\ell\rangle .
\]
完整七项为 \(q_0=\|C_0\|²,\ q_1=\operatorname{Re}\langle C_0,C_1\rangle,\ q_2=(2\operatorname{Re}\langle C_0,C_2\rangle+3\|C_1\|²)/5,\ q_3=(\operatorname{Re}\langle C_0,C_3\rangle+9\operatorname{Re}\langle C_1,C_2\rangle)/10,\ q_4=(2\operatorname{Re}\langle C_1,C_3\rangle+3\|C_2\|²)/5,\ q_5=\operatorname{Re}\langle C_2,C_3\rangle,\ q_6=\|C_3\|²\)；此行省略段标 j。

由于六次 Bernstein 基非负且和为1，准确 \(V_j=\max_{0\le m\le6}q_{jm}\ge0\) 控制该整段平方范数。混合 q 可以负，须原样保存；不能以端点最大值替 V、删交叉项或省物理 h。固定仅用这 16 个段上界，不按结果细分段。
\[
\kappa_j=\int_{t_j}^{t_{j+1}}K_1(T-r)\,dr
=\sum_{k\in H_1}\frac{e^{-|k|²(T-t_{j+1})}(1-e^{-|k|²h})}{|k|},\qquad
\bar U=H+\tfrac34\sum_{j=0}^{15}V_j\kappa_j,\quad H=\|P_{H_1}X_{16}\|_{A0}.
\]
这里 \(K_1(\tau)=\sum_{k\in H_1}|k|e^{-|k|²\tau}\)，准确对象上 \(F^v(T)\le\bar U\)，不需要求真实 \(g^v\)。浮点实现固定以 expm1 处理 \(1-e^{-|k|²h}\)，全部整数标签都入和；每个准确有理时差单独转浮点，保存该转换信息。数值 \(\bar U_{\rm num}\) 未经误差包围，**不是认证上界**。

## 3. 固定 BF/PH 比较，不填补 RE 全历史

准确 \(L=\big(\sum_{k\in S}|B(X_{16},X_{16})_k|²/|k|²\big)^{1/2}\) 是节点投影残差范数；保留全 signed 权重，不再乘2。固定只取普适 \(c_b=0\)，不求 E(b)。BF 给 \(B_{\rm BF}=\sqrt{N_1h}\,L/7\)；这是特定 RE 总预算的一项下界，不是真实误差下界。

原 \(M=\|a_*\|_2\) 从已核 INPUT_RESULT 所绑定的原 M² 有理区间读取：固定取其下端 \(m_-\) 的 \(M_-=\sqrt{\max(0,m_-)}\le M\)，保留原区间与来源，不以任何保存态能量代替。正性单调允许在 PH 的下界中使用 M_-；浮点开方/转换仍不构成认证。若原区间及准确 T 的字段/绑定无法核同，则停止，不临时构造替代值。

令 \(\rho=(r-b)/h\)，\(\Phi_6=h\rho/\sum_{n=0}^6(2n+1)P_n(2/\rho-1)^2\)，\(e_*(r)=L\sqrt{\Phi_6(r)}\)。准确公式为
\[
J_*=\int_b^T K_1(T-r)e_*(r)(2M_-+e_*(r))\,dr,\qquad
B_{\rm PH}=B_{\rm BF}+\tfrac54J_* .
\]
PH 的次数论证支付末段逐时预算下界；没有把端点 \(c\le E(T)\) 向过去传播。b 以前的完整历史仅在下界中舍去非负项，实际 RE.12 的 I、σ、ε、初始差及报告 ξ 仍全部未付。

固定 J 数值规则为 **一次64点 Gauss–Legendre**：固定64阶实对称 Jacobi 矩阵零对角、邻对角 \(n/\sqrt{4n²-1}\ (1\le n\le63)\) 的特征值 \(x_i\)，配 \(w_i=2/[(1-x_i²)P'_{64}(x_i)^2]\)。映射 \(\rho=(1+x)/2\)，积分乘 h/2；不自适应、不加第二阶数、不增加重建端点。一次 O(64³) 节点/权重生成计入同一 worker；保存64个节点/权重、顺序、正性/有限性和权重和偏差。这些浮点检查不是求积误差认证，\(J_{\rm num}\) 只为 NUMERICAL_VALUE_ONLY。

为避免 \(\rho^{-1}\) 的大幂，固定用 \(A_n=\rho^nP_n(2/\rho-1)\)：\(A_0=1,A_1=2-\rho,(n+1)A_{n+1}=(2n+1)(2-\rho)A_n-n\rho²A_{n-1}\)，再取 \(\Phi_6=h\rho^{13}/\sum_{n=0}^6(2n+1)\rho^{12-2n}A_n²\)。规定 \(\Phi_6(0)=0,\Phi_6(1)=h/49\)；64节点严格在(0,1)，异常端点/非正分母即停止。L=0 时 J 固定为0，不除 L；全部零支保留。

只报告两项 \(\bar U_{\rm num}-B_{{\rm BF},\rm num}\)、\(\bar U_{\rm num}-B_{{\rm PH},\rm num}\)，及对应 \(\bar U_{\rm num}/B_{\rm num}\)（分母0为 null，并存两原值）。阈值固定为差0/比1，不临定 ζ。非正差最多提示未来严格证书的价值，正差只说明此粗筛未显示障碍；等号/舍入不确定性不得认证任何号。即便将来严格证明 \(\bar U\le B_{\rm PH}\)，也只阻断这个 RE.12 终点严格失败认证，不判真实 NS 门。新连续 G/W、ξ、全窗与寿命仍未付。

## 4. 唯一成本方案、保留与核查

顺序流式处理17份原 U，不常驻17个大状态；每份只保留紧凑 H₀ 端值/斜率、投影诊断及原文件身份。末端额外保留紧凑 C53 的 X 和 N160 B、H₁。进入 N216 前释放160工作数组。读取原 NPZ 的 U 成员前核 header、dtype/形状、整数节点及 SHA；原/恢复件按已冻清单核同，不复制旧 G/W 科学结果。

FFT固定计数：N160 上17×(2逆+1正)三分量 batch =51 batch/153 scalar；N216 上1×(2逆+1正)=3 batch/9 scalar；总 **54 batch/162 scalar**。没有32/64网格源、四阶段、NS时间步或额外诊断 FFT。另有17次投影/斜率代数、16×7混合系数、16个κ与64个PH核的有限求和，至多96N₁次 exp/expm1 调用及一次固定64阶规则生成；这些与 I/O/哈希/序列化均计时。

显式存储单位：一个三分量 complex128 N³ 场占 \(48N³\) bytes；160为196608000B，216为483729408B，不含头、临时及 FFT 工作区。实现目标不超过六个216向量等价暂存加六个实标量216网格，逐节点分配并释放；该分配模型不是实测峰值或 NumPy 后端保证，最终源码须逐寿命核。原17检查点约3.5GB，只流式读取；开始/结束两遍整文件哈希及 U 解码 I/O 均另计，不把已完成数据审查当零成本。

旧 bench160 实测完整增广一步2.3002353329211473s、整个子生命周期2.764673625s、CHILDREN峰值2144698368B；该步含4次160及4次32/64产品，不是本次单 RHS 或216实测。仅作成本模型 \(c=2.3002353329211473/4,\ t_{\rm arith}\sim c[17+(216³\log216)/(160³\log160)]\)，另加上述 I/O、投影、求积和归档。FFT尺寸/缓存/后端会改变常数，不能把此模型当时限承诺；旧18逻辑CPU、约36GiB也不证明当前可用内存。

建议后续合同只准一次科学子进程，沿用已测 bundled Python3.12.14/NumPy2.3.5 的 complex128/CPU后端：Popen至reap墙钟上限120s、Darwin事后CHILDREN RSS≤6GiB、完整新输出≤1GiB；父SELF单列，不相加冒称同时总峰值。此为拟封顶方案而非已通过资源门；新即时内存/磁盘检查、源码静审、锁和根的外部门尚待后续合同，不借旧预算授权。超时杀同一子进程并回收，资源超限/源变动/非有限/计数不全均保留失败，不重跑或追加精度层。

派生原始输出固定保存：完整 N216 B（含 C106 外浮点尾而不悄删）、末端紧凑 X 与 N160 B、17组 H₀ 值/斜率、16×7有符号 q、V/κ/H/L²/M区间、64项求积证据、所有比较原值、阶段计数/资源/起终哈希。预计主体小于1GiB须以实际文件总字节验收；JSON预留16MiB纳入总额。采用独占目录/临时文件与无覆盖原子发布，原输入只读，失败临时证据也保留，不用删除原件换空间。

独立核查分两层：未来非作者先逐式/逐行静审；同一唯一 worker 内保存 N216 保留 C53 与末端 N160 B 的完整复向量差、全部外尾/共轭/散度诊断，并分别用有序乘积公式与七项显式式核 q，核 Hermite 端值/物理导数和 Φ 两端身份。偏差全量报告，不按结果添阈值，不称两个共享浮点 FFT 为独立证书。另一阅读者据原字节/日志/完整输出检查完成范围；另跑科学复算须另授权，不藏在本设计。

目前结论为“单一有限价值侦察方案可进入非作者设计审查”；N216实测成本、具体源码峰值、严格舍入/求积误差均未付。若执行资格或预算封顶不能落实则不启动；若侦察未显示判别价值则原样结束，不扩配置。本稿没有计算未知 L、Ū、J、M 或任何新节点数值。

## 实际阅读与字节

本轮全文读新合同、FG、PH、AP、APPLICATION_DATA_PREFLIGHT、旧 TRAJECTORY_CONTRACT 与 INPUT_RESULT；BF定向42–99行，kernel当前1–170行、driver244–309行（两源既往曾全文审）；bench result只读环境/计数/成本相关段及100–196行、receipt1–90行，不称所有字段全文审。另曾查看 trajectory160_512 result 的可见计时/计数字段与两原哈希，未据其大数组或未显示字段推论。

| 文件（相对 research/reverse/；下表为实测 SHA-256） | SHA-256 |
|---|---|
| endpoint-budget-value-preflight/CONTRACT.md | 320a7da8e24af51b106d07a54fae7383e05351f2ccbce5571da4b4d520118ae6 |
| residual-budget-floor-preflight/FIRST_GATE_TARGET_PROOF.md | e8697f04790ccaa9461263b29cd30bec5b8ac80836fa1197343dbc6ffe5a85dc |
| residual-budget-floor-preflight/PREFIX_HISTORY_PROOF.md | 755f3c3ca96d2a4197873b9b3019a34ad515165edab037d039a8de84f026cddd |
| residual-budget-floor-preflight/ROOT_APPLICATION_PREFLIGHT.md | e361e0fa8c2db879906b60ca7901f295c38fe643d5d3ffd49b37678c17a0dddb |
| residual-budget-floor-preflight/PROOF.md | 1ab573bbc9bdc16445964cc65245182357b14327dea8df0a8f070e72bbde81d1 |
| residual-budget-floor-preflight/APPLICATION_DATA_PREFLIGHT.md | 496b8e68d85706394763d699a152e50a5e7bbb42a2f8959f718c3d5f3c732d7a |
| annular-source-observation/numerical_kernel.py | 1b29e919cf5faefe1e4a5193fee0f7e0fdd11901d8aed7b3e5ade752cd23f175 |
| annular-source-observation/trajectory_driver.py | 36d143eb65b267e890f37666ac0688963c0f0ed1d706f23b7923d7d652e173e7 |
| annular-source-observation/TRAJECTORY_CONTRACT.md | 0886f1f992e7a6285e02ffd3c48650dca197d9ced3c1f8bd21a021711307447b |
| annular-source-observation/INPUT_RESULT.md | 2a8cba5e128124c24614c56a51796a53e9e3a42c9eefcc6091afcaa7c17bc781 |
| annular-source-observation/numerical-runs/bench160/result.json | 0afbed14a4e863b987c3bf723dda084a891f309a4a2924efebae6919a23fc4f1 |
| annular-source-observation/numerical-runs/bench160/execution.json | 377af0bb2d4d0657ffd47ab1370e2f099181274ad0b24921528289b521d61f6f |
| annular-source-observation/numerical-runs/trajectory160_512/result.json | f2f7cae23b0770a97ffa32706fdedb666bbead7461d956e45e3a83e652027908 |
| annular-source-observation/numerical-runs/trajectory160_512/execution.json（本轮仅hash） | 893190eacb324b0c4e2dd8c62da6da0e3c02de51084257a8e2cc8a5e53ef21f7 |

仅写本设计；科学代码写入/运行/import/compile、数组解码、实际选参、Git及外发均0。全文自读后停稿，最终SHA由任务消息给出。
