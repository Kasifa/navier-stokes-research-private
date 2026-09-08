# 两条剩余虚部的独立联合消元与严格双侧界

2026-09-08，PRIVATE_CORE。状态：**得到共享虚比值之比与模平方比消去后的精确恒等式，排除中间 \(\rho_1>2\) 支，并给出更窄的纯几何双侧必要界；保留真实共享比值 T 后，对这两条虚部本身给出准确充要条件。待分开的非作者审查及根比较。**

本有界推导先按父任务消息从本代理刚全文审过的 FR.11 手工进行，并以文字回报核心恒等式和双侧界；本文件落盘前实际全文读了 `PAIRED_IMAGINARY_CONTRACT.md`。纸面合同是同一已指定任务的记录，不倒写为首次手推之前已经落盘。本稿未读对应的新根稿或其它新推导。根随后告知其先独立得到核心恒等式和 \(\rho_1<4/\mu_1\)，再读到本代理消息中的双侧界；此处如实记录形成顺序，不夸大任一稿的盲性。本代理熟悉并审过 FR 基础，本项独立性只针对对应的新联合推导。

## 1. 同一数据与直接输入

沿用本目录合同的同一组三个整数频率和种子，仅最短种子线性，最低两条 β 零；最低完整条件和两个高指定投影为零作为直接前提。本文只使用其中明确支付的实量条件：
\[
\mu_i>2,\quad M_i>X_i^2>0,\quad y_i\ne0,
\quad \rho_i\ne0,\quad\rho_2>2,
\]
\[
\chi_{10},\chi_{20},\chi_{12},\chi_{21}\ne0,
\qquad
\delta_1=\sqrt{P_1/P_2}(2-\rho_1),\quad
\delta_2=\sqrt{P_2/P_1}(2-\rho_2)<0.
\tag{PII.1}
\]
特别是中间 \(\rho_1\) 不预设正号，也不预设大于 2。所有系数比来自同一固定几何，所有 X、M、y 来自同一组三种子，不按行独立选择。

要联用的两个实残差是
\[
\mathcal I_1=
\delta_1\frac{y_2/y_1}{M_2}+\frac{\rho_1}{M_1}
-\frac{4X_1^2}{\mu_1M_1^2},
\]
\[
\mathcal I_2=
\delta_2\frac{y_1/y_2}{M_1}+\frac{\rho_2}{M_2}
-\frac{4X_2^2}{\mu_2M_2^2}.
\tag{PII.2}
\]
这些是 FR.11 的直接等式输入。本目录整包是否已完成最终接纳，不作为此处推理的前提。本文不重新证明完整 Fourier–Leray 展开，也不预先宣告两条实残差为零。

定义真实数据中间量
\[
\varepsilon_i=\frac{4X_i^2}{\mu_iM_i},\qquad
0<\varepsilon_i<\frac4{\mu_i}<2,
\tag{PII.3}
\]
\[
r=\frac{y_2}{y_1}\ne0,\qquad
T=r\frac{M_1}{M_2}\ne0.
\tag{PII.4}
\]
M、\(\mu\) 严格正，所以 PII.3 的除法合法；X 非零和 \(M_i>X_i^2\) 给两个严格端点。r 和 T 的非零性来自两个非零 y。T 不是新自由变量，而是同一数据的有符号虚比值之比 r 与正模平方比的乘积。按 FR.1 的实际 a_i，单位有向面积比为 \((|a_2|^2/|a_1|^2)r\)，仅其符号与 r 相同；下面没有将这两个比值的大小混同。

## 2. 第二虚部先固定 T 的号和值

分别把 PII.2 乘正数 M_1、M_2，得到精确等价
\[
\mathcal I_1=\mathcal I_2=0
\iff
\delta_1T=\varepsilon_1-\rho_1,\qquad
\frac{\delta_2}{T}=\varepsilon_2-\rho_2.
\tag{PII.5}
\]
这里第二个式子的 \(T^{-1}\) 正好包含 \((y_1/y_2)(M_2/M_1)\)，没有另行选择第二个共享比值。

因为 \(\rho_2>2>\varepsilon_2\)，有 \(\varepsilon_2-\rho_2<0\)，允许从第二式解出
\[
\boxed{
T=\frac{\delta_2}{\varepsilon_2-\rho_2}
=\sqrt{P_2/P_1}\,
\frac{\rho_2-2}{\rho_2-\varepsilon_2}>0.}
\tag{PII.6}
\]
这一步没有除以 \(\delta_1\) 或预设 \(\rho_1\) 的号。\(M_1/M_2>0\) 继而给 r>0，即两个 y 同号。单位有向面积 \(2|a_i|^2y_i\) 也同号；这不删除相对幅度要求，实际 r 仍必须由 PII.6 和 M_2/M_1 恢复。

## 3. 联立恒等式及 \(\rho_1>2\) 的排除

在 PII.5 中相乘，利用非零 T 消去 r 与 M_1/M_2，并用两正平方根互逆，得到
\[
\delta_1\delta_2=(2-\rho_1)(2-\rho_2)
=(\varepsilon_1-\rho_1)(\varepsilon_2-\rho_2).
\]
因此
\[
\boxed{
(\rho_1-\varepsilon_1)(\rho_2-\varepsilon_2)
=(\rho_1-2)(\rho_2-2).}
\tag{PII.7}
\]
这一步没有除任何可能为零的中间边 β 或 \(2-\rho_1\)。两个实际 \(\varepsilon_i\) 保留；它们不是可独立调节的形式端点。

展开 PII.7 并除以严格正的 \(2-\varepsilon_2\)，得两种等价写法：
\[
\boxed{
\rho_1=
\varepsilon_1-
\frac{(2-\varepsilon_1)(\rho_2-2)}{2-\varepsilon_2}
=2-(2-\varepsilon_1)
\frac{\rho_2-\varepsilon_2}{2-\varepsilon_2}.}
\tag{PII.8}
\]
第一式中被减去的分数严格正，故
\[
\boxed{\rho_1<\varepsilon_1<4/\mu_1<2.}
\tag{PII.9}
\]
因此先前单行必要门保留的 \(\rho_1>2\) 支，不能同时满足两条剩余虚部。中间 \(\delta_1>0\) 也是这一结论的后果，不是前置假设。原域 \(\rho_1\ne0\) 始终保留；本文没有以 PII.9 接纳 \(\rho_1=0\) 边界。

## 4. 保留真实 T 时，对两虚部的准确充要性

在 PII.1–4 的固定同数据域，以下两项合起来恰与 \(\mathcal I_1=\mathcal I_2=0\) 等价：
\[
\boxed{
T=\sqrt{P_2/P_1}\frac{\rho_2-2}{\rho_2-\varepsilon_2},
\qquad
(\rho_1-\varepsilon_1)(\rho_2-\varepsilon_2)
=(\rho_1-2)(\rho_2-2).}
\tag{PII.10}
\]
第二项也可等价替换成 PII.8 的精确 \(\rho_1\) 式。必要性已由上两节证明。

反向假设 PII.10，且 T 仍是 PII.4 定义的实际共享量。第一项与 \(\delta_2\) 的定义给
\(T=\delta_2/(\varepsilon_2-\rho_2)\)，所以
\(\delta_2/T=\varepsilon_2-\rho_2\)，第二虚部为零。再用第二项和 \(\delta_1\delta_2=(2-\rho_1)(2-\rho_2)\)，
\[
\delta_1T
=\frac{\delta_1\delta_2}{\varepsilon_2-\rho_2}
=\frac{(\varepsilon_1-\rho_1)(\varepsilon_2-\rho_2)}
{\varepsilon_2-\rho_2}
=\varepsilon_1-\rho_1.
\]
分母严格负而非零，第一虚部也为零。最后按 PII.5 除回正 M_i 完成等价性。反向仍未除 \(\delta_1\)。

PII.7 单独只是必要关系：相乘后并未保留真实 T 的具体值，不能由乘积关系直接反推两个式子。PII.10 补回的是实际 T 的等式，不是允许另选一个 T。即使 PII.10 成立，另两条实残差仍须独立为零，故这里的充分性只属于这两条虚部。

## 5. 严格的纯几何双侧必要界

为只保留几何系数比，记
\[
u_i=2-\varepsilon_i,\qquad
\underline u_i=2-4/\mu_i,
\qquad 0<\underline u_i<u_i<2.
\]
另设
\[
V_2=\frac{\rho_2-\varepsilon_2}{2-\varepsilon_2}
=1+\frac{\rho_2-2}{u_2}.
\tag{PII.11}
\]
因为 \(\rho_2-2>0\)，且 \(\underline u_2<u_2<2\)，有严格范围
\[
\frac{\rho_2}{2}<V_2<
1+\frac{\rho_2-2}{\underline u_2}.
\tag{PII.12}
\]
所有量均严格正。用 PII.8 的 \(\rho_1=2-u_1V_2\)，一方面
\[
\rho_1<2-\underline u_1\rho_2/2
=2-\left(1-\frac2{\mu_1}\right)\rho_2,
\]
另一方面
\[
\rho_1>
2-2\left(1+\frac{\rho_2-2}{\underline u_2}\right)
=-\frac{\rho_2-2}{1-2/\mu_2}.
\]
因此
\[
\boxed{
-\frac{\rho_2-2}{1-2/\mu_2}
<\rho_1<
2-\left(1-\frac2{\mu_1}\right)\rho_2
<\frac4{\mu_1}.}
\tag{PII.13}
\]
最后一项严格比较使用 \(\rho_2>2\)、\(1-2/\mu_1>0\)。两端分母 \(1-2/\mu_i\) 均严格正。所有端点严格性都来自原数据中的 X 非零、M 严格大于 X 平方，以及两个严格较长接收比值；没有取端点或选实际数据。

PII.13 只涉及 \(\rho_i,\mu_i\)，它们均是固定几何的系数比，因此是纯几何必要界。推导界时舍去了实际 \(\varepsilon_i\) 和 T 的具体值，故它不是 PII.10 的替代，也不是两虚部或全部原数据的充分条件。负 \(\rho_1\) 不被整体排除，仍须按此双侧界、原 \(\rho_1\ne0\) 域及实际共享数据继续检验；本文没有证明保留支存在实例。

## 6. 除法、范围与尚未解决的条件

本稿全部除法分别由以下量支付：M_i、\(\mu_i\) 严格正；两个 y 非零，使 r、T 非零；\(\rho_2-\varepsilon_2>\rho_2-2>0\)；\(2-\varepsilon_i>2-4/\mu_i>0\)；\(1-2/\mu_i>0\)。没有除 \(\delta_1\)、\(\rho_1\)、β、\(2-\rho_1\) 或未知号表达式。原有 \(\chi\ne0\)、\(\rho_1\ne0\) 不是本次消元删掉的假设。

所得结论是：两条剩余虚部共同为零必须满足 PII.6–9 和严格双侧界；其中 PII.6 与精确恒等式一起，对实际同数据的两条虚部构成充要条件。共同翻转 y1、y2 保持实际 r、T、\(\varepsilon_i\) 不变，不能用该共同符号选择来绕过这些关系。

两条实残差 \(\mathcal R_1,\mathcal R_2\) 仍未求零；固定几何和种子是否同时满足前置投影、最低完整条件及本稿两虚部，仍未证明存在或无解。其它两个 C 原方向、模板共同幅度、真实 NS 时间、无限维和跨代余项、有限两步机制、统一迭代、单初值无限尺度与有限总时间均未支付。没有实际整数几何、初值、幅度或时间选择，没有候选接纳、奇性或全局正则性结论，也没有旧失败证据修复。EXACT PAIRED IMAGINARY CONDITIONS ONLY；NO-CANDIDATE；NOT CLAY。

## 7. 实际来源与字节记录

| 来源 | 实际读取与用途 | SHA-256 |
|---|---|---|
| `full-high-row-reduction/PAIRED_IMAGINARY_CONTRACT.md` | 本文件落盘前全文实读；对应先前同一有界手推任务，明确输入和形成顺序 | `fb4550856c200bac96616202ac0e3974851c2bbe6b45e8814bb670d38b1d67ec` |
| `full-high-row-reduction/CONTRACT.md` | 本连续任务前序全文实读并审查；原同数据范围，本次实际复核字节 | `8f1dd745dc12409f3e49b7b56073b3fb38fca4a26d23774f0df4ea12292ecc6e` |
| `full-high-row-reduction/PROOF.md` | 本代理此前全文非作者核验最终修正字节；本次重读第 95–210 行，使用 FR.11、13 和明确量范围作为直接输入 | `3d02da817e164bbf8f75bdddfea74a4e0d2b14c12d890952aeeb727866cc3c6b` |

来源提及的其它文件不自动计为本次实读；本稿没有读取对应的新根联合稿。PII.3–13 为本次独立手工推导及反向自核，没有新外部定理或文献新颖性声明。工具仅用于文本和 SHA-256，无科学程序、数组、数值求值、实际选参、扫描、Git、重置或外发。本稿最终全文自读并复核源字节后停改，自身 SHA-256 另行报告。
