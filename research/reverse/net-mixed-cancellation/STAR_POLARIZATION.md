# 两边星形活跃图：总混合首项为零迫使线性极化

2026-09-08，PRIVATE_CORE。状态：独立有界推导，待根全文核验。未读本项正在写作的 `INDEPENDENT.md`，未使用其口头结论。

**结论：在本轮给定的全非正交、长度两两不同、三频线性独立及非零种子条件下，如果双向活跃图恰为两边星形，而且所有接收的总混合首项 \(M_0\) 为零，则每个种子都必为一个非零复标量乘一个非零实横向向量。没有需要增加的额外假设。**

证明只使用两条叶节点接收行；中心行的相消条件没有用于该必要性结论。本文不证明这些假设组有解，也不求解中心行，不给充分性或候选接纳。全部手工符号，无科学程序、数组、数值求值、扫描、Git、额度重置或外发，没有选择实际频率、初值或时间。本轮只写入本文件。

## 1. 对象、定义和实际来源

固定同一组三个线性独立整数频率，重新标为中心 \(p_0\) 与叶节点 \(p_1,p_2\)。所有成对点积均非零，三个平方长度两两不同。保持同一份非零复横向种子 \(U_i\perp p_i\)，负模为共轭。

边 \(\{i,j\}\) 双向活跃的准确条件是
\[
(U_i\cdot p_j)(U_j\cdot p_i)\ne0.
\tag{SP.1}
\]
假设活跃边恰为 \(\{0,1\}\)、\(\{0,2\}\)。记完整混合根空间和为
\[
H_{i\leftarrow j}=D_{ij,+}+D_{ij,-},
\qquad (M_0)_{2p_i}=\frac16\sum_{j\ne i}H_{i\leftarrow j}.
\tag{SP.2}
\]
这里 \(D_{ij,\sigma}\) 是已接受 MIXED_ROOT 独立稿 MI.16–20 的完整三层有序 Fourier–Leray 映射，对应本合同的 \(G_{ij,\sigma}\)。SP.2 是三次时间首项，未把不同正时间热核假定为相同。

称 \(U_i\) 为线性极化，是指存在 \(\alpha_i\in\mathbb C\setminus\{0\}\) 和 \(R_i\in\mathbb R^3\setminus\{0\}\)，使 \(U_i=\alpha_iR_i\)、\(R_i\perp p_i\)。这不要求 \(U_i\) 本身为实向量，也不固定各种子的整体复相位。

实际数学来源如下，路径相对于 `research/reverse/`。

| 来源与实读范围 | SHA-256 |
|---|---|
| net-mixed-cancellation/CONTRACT.md，本连续审查已全文读取，本轮字节未变 | 8ec55579d3288a15e47f2b1af17a2d981ac174fb649dc496fb6d5ac0d9b2e7e8 |
| mixed-polarization/MIXED_ROOT_INDEPENDENT.md，本连续审查已全文读取并完成非作者核验，本轮直接从 MI.19–20 推导以下系数，字节未变 | cad93f863ad371723d4510f20588a0f7abcee3e4f8e2984010f88ebcb2fc2dbf |

本稿没有把源文件内部列出的其他文件冒记为实读，也没有借用尚未审查的新稿结论。

## 2. 活跃边上的完整平面与法向和

先考虑一条有向接收边 \(p\leftarrow q\)，记
\[
P=|p|^2,\quad Q=|q|^2,\quad c=p\cdot q\ne0,
\quad\Delta=PQ-c^2>0,\quad d=P-Q\ne0,
\]
\[
S=P+Q,\quad\lambda_\sigma=S+2\sigma c,
\quad E_\sigma=4P+Q+4\sigma c,
\]
\[
\Lambda=\lambda_+\lambda_->0,
\qquad\Omega=E_+E_->0.
\tag{SP.3}
\]
沿用固定实基
\[
e=q-\frac cPp,\quad f=p-\frac cQq,\quad n=p\times q,
\qquad U=u e+v n,\quad V=x f+y n.
\tag{SP.4}
\]
活跃条件等价于 \(ux\ne0\)。令
\[
w=\frac vu,\qquad z=\frac yx,
\quad a_\sigma=\frac{d(Q+2\sigma c)}{\lambda_\sigma E_\sigma},
\quad\beta=\frac{4cPd}{Q\Lambda}\ne0.
\tag{SP.5}
\]
\(a_\sigma,\beta\) 只是当前固定几何的实系数，不是新极化自由度。

MI.19 的两项完整相加给
\[
\boxed{
H_e=\frac{8ic\Delta^3d(2P+Q)\chi}
{P^2Q^2\Lambda\Omega}u^2|x|^2,
\qquad\chi=4P^2-PQ+Q^2-4c^2.}
\tag{SP.6}
\]
为核对通分，置 \(T=(P+Q)(4P+Q)\)、\(b_0=2P+Q\)，则
\(\lambda_\sigma E_\sigma=T+8c^2+6\sigma b_0c\)。
\((P+c)(Q+2c)\lambda_-E_--(P-c)(Q-2c)\lambda_+E_+\)
的奇次项相减后恰为 \(2c(2P+Q)\chi\)，产生 SP.6。

MI.20 的法向项则给
\[
\boxed{
H_n=\frac{2i\Delta^3}{P^2Q}u^2|x|^2
\left[(2-a_+-a_-)\Re z
+i(a_+-a_-)\Im z+\beta w\right].}
\tag{SP.7}
\]
这里先保留 \(\overline x y=|x|^2z\)、\(x\overline y=|x|^2\overline z\)，然后再取实、虚部。法向的 \(uv\) 项使用恒等式
\[
\frac{Q+c}{\lambda_+}-\frac{Q-c}{\lambda_-}
=\frac{2cd}{\Lambda}.
\]
因此 SP.7 的 \(\beta\) 与两个相干项的符号均来自完整有序系数，没有相位平均或删去反序作用。

## 3. 活跃且 \(H=0\) 的必要几何与极化关系

\(e,n\) 是复化横向平面中的两个独立实方向。在活跃边上，SP.6 除 \(\chi\) 外的全部因子非零，所以
\[
H=0\quad\Longrightarrow\quad\chi=0.
\tag{SP.8}
\]
由此
\[
4c^2=4P^2-PQ+Q^2,
\qquad4\Delta=(Q-P)(4P-Q)>0.
\]
因为 \(P,Q>0\)，必有
\[
\boxed{P<Q<4P.}
\tag{SP.9}
\]
因此零混合输出的活跃接收端必须比发送端短。若某个固定几何不满足该必要条件，则它已经不能满足本稿的叶行零假设；本文不据此搜索或选择新几何。

在 \(\chi=0\) 上，直接化简得到
\[
\Lambda=3P(Q-P),\qquad
\Omega=3Q(4P-Q),
\]
\[
a_++a_-=\frac{4P}{3Q},\qquad
a_+-a_-=-\frac{4c}{3Q},\qquad
\beta=-\frac{4c}{3Q}.
\tag{SP.10}
\]
例如完整通分给
\[
a_++a_-=
\frac{2d[Q(P+Q)(4P+Q)-4(6P+Q)c^2]}{\Lambda\Omega},
\]
\[
a_+-a_-=
\frac{4cd[4P^2-PQ-2Q^2+8c^2]}{\Lambda\Omega}.
\]
代入 SP.8，即分别给 SP.10；没有对符号值求数值近似。

把 SP.10 代入法向零式 SP.7，精确得到
\[
\boxed{
\frac vu=\frac{3Q-2P}{2c}\Re\!\left(\frac yx\right)
-i\Im\!\left(\frac yx\right).}
\tag{SP.11}
\]
特别地，
\[
\boxed{\Im(v/u)=-\Im(y/x).}
\tag{SP.12}
\]

在当前活跃条件下，\(u,x\ne0\)。由于 \(e,n\) 和 \(f,n\) 均为独立实基，
\[
U\text{ 线性极化}\iff v/u\in\mathbb R,
\qquad
V\text{ 线性极化}\iff y/x\in\mathbb R.
\tag{SP.13}
\]
例如若 \(v/u\) 实，则 \(U=u[e+(v/u)n]\)，方括号是非零实横向向量；反向由实基中的坐标比得到。故 SP.12 证明：
\[
\boxed{
\text{活跃边上 }H_{p\leftarrow q}=0
\quad\Longrightarrow\quad
U\text{ 线性极化当且仅当 }V\text{ 线性极化}.}
\tag{SP.14}
\]
该结论没有说任意活跃零边的两个种子已经线性极化；非零虚部互为相反数仍可能满足单边必要式。星形的非活跃叶边将在下一节提供线性极化的起点。

## 4. 星形的非活跃边提供一个线性叶种子

先不除以任何坐标。由完整 MI.19–20，若 \(u=0\) 或 \(x=0\)，则每个 \(D_\sigma\) 的平面与法向单项均为零。因此
\[
(U_i\cdot p_j)(U_j\cdot p_i)=0
\quad\Longrightarrow\quad
H_{i\leftarrow j}=H_{j\leftarrow i}=0.
\tag{SP.15}
\]
这包括某个点积为零但种子本身非零的分支；没有把双向活跃定义误换成两个点积都为零。

叶边 \(\{1,2\}\) 非活跃，故
\[
U_1\cdot p_2=0\quad\text{或}\quad U_2\cdot p_1=0.
\tag{SP.16}
\]
若第一项为零，结合 \(U_1\cdot p_1=0\) 及 \(p_1,p_2\) 非平行，得到
\[
U_1\in\operatorname{span}_{\mathbb C}(p_1\times p_2)
\setminus\{0\}.
\]
所以 \(U_1\) 线性极化。若第二项为零，同理 \(U_2\) 线性极化；若两项都为零，两者都线性极化。因此至少有一个线性叶种子。

由 SP.15，两个叶节点的接收行没有彼此贡献。总 \(M_0=0\) 因而给
\[
H_{1\leftarrow0}=0,
\qquad H_{2\leftarrow0}=0.
\tag{SP.17}
\]
这两条边按假设均活跃，所以都可以使用 SP.14。从已经线性极化的那个叶种子出发，第一条相应的零边迫使中心 \(U_0\) 线性极化；另一条叶行零边又迫使另一叶种子线性极化。

线性极化是向量本身的性质，独立于各边所用实横向基。因此这里没有把中心在两种边基下的相干坐标当成同一自由变量，也没有逐边重选中心种子。

综上，存在非零复数 \(\alpha_0,\alpha_1,\alpha_2\) 和非零实横向向量 \(R_0,R_1,R_2\)，使
\[
\boxed{U_i=\alpha_iR_i,\quad R_i\perp p_i,
\qquad i=0,1,2.}
\tag{SP.18}
\]

## 5. 本检验完成与未付范围

本轮实际完成的是 SP.18 的必要性证明，没有反例。附带得到两条叶边各自必须满足 SP.8–9，所以星形中心必须比两个叶频率都长，且中心平方长度小于每个叶平方长度的四倍。这些是从原假设推出的必要条件，不是新加的假设。

中心行
\(H_{0\leftarrow1}+H_{0\leftarrow2}=0\)
没有用于线性极化推论，也没有在此求解。不能由三个种子均线性极化反向推出任何叶行或中心行相消，更不能据此说存在满足全部假设的数据。若固定几何不满足上述必要几何式，本项只记录假设不相容，不继续选几何或扫描。

全非正交、长度不同和双向活跃使 SP.5–12 中的除法合法；本稿不把该关系推广到正交、等长或不活跃边。非活跃边另由无除法的 SP.15–16 处理。

\(M_0=0\) 是完整四叶响应在全部接收模上的三次首项条件。它不表示不同正时间热核下的混合根恒为零，不支付 \(W_0\ne0\)、中心行相消、实际来源占优、模板返回、可迭代机制、跨代统一误差、同一固定初值无限尺度或有限总时间。没有实际候选或奇性结论。NECESSARY POLARIZATION CONDITION ONLY；NO-CANDIDATE ACCEPTED；NOT CLAY。
