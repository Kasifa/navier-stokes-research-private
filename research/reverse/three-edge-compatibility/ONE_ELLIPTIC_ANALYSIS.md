# 两个线性发送种子与最长非线性接收：共同非实二次根障碍

2026-09-08，PRIVATE_CORE。状态：**在 ONE_ELLIPTIC_CONTRACT 的明确几何假设下，最长行不存在极化面积非零的接收种子；已完成手工推导和自核，待非作者复核。** 本后续属于同一科学阶段，不单独正式冻结或交接。

本稿全文读取 ONE_ELLIPTIC_CONTRACT.md，直接把其中两条几何等式及开域作为假设。它们此前作为“必要门”的推导不作为本稿的已审前提。本稿没有读取本后续的新主稿或审查，也不修改此前最终文本；只从已接受 NC.7–8 的完整作用重新推导最长行。

全部为手工符号。没有选取实际频率、极化、幅度或时间；没有科学程序、数组、数值求值、扫描、Git、额度重置、外发或发布。工具仅用于文本和 SHA-256。

## OE.1 固定假设与完整最长行

保持合同的同一组三对数据，三频线性独立、成对非正交、三边全部活跃，平方长度 \(P_1<P_2<P_3\)。\(U_1,U_2\) 均为非零复标量乘非零实横向向量，\(U_3\) 的有向极化面积非零；负模严格共轭。单位黏性、无外力和三维 \(2\pi\) 环面不变。

只为最长行记
\[
p=p_3,\quad q_j=p_j,\quad P=|p|^2,\quad Q_j=|q_j|^2,\quad
c_j=p\cdot q_j,\quad d_j=P-Q_j>0,\quad
\Delta_j=PQ_j-c_j^2>0,\qquad j=1,2.
\]
合同直接假设
\[
\boxed{8c_j^2=-4Q_j^2+PQ_j+2P^2,\qquad
\frac P4<Q_j<\frac{1+\sqrt{33}}8P<P.}
\tag{OE.1}
\]
没有在本稿重新证明这些条件由其它行推出，也没有假定它们已有实际整数三频实例。

完整双有序作用仍为
\[
\mathfrak B(X,Y;r,s)
=-iP_{r+s}[(X\cdot s)Y+(Y\cdot r)X],
\qquad P_k=I-\frac{k\otimes k}{|k|^2}.
\]
对一条最长接收边，\(V_+=U_j,V_-=\overline U_j\)，保留
\[
N_\sigma=\mathfrak B(U_3,V_\sigma;p,\sigma q_j),\quad
T_\sigma=\mathfrak B(U_3,N_\sigma;p,p+\sigma q_j),
\]
\[
G_\sigma=\mathfrak B(V_{-\sigma},T_\sigma;-\sigma q_j,2p+\sigma q_j),
\qquad Z_{3j}=G_++G_-.
\tag{OE.2}
\]
所有 Leray、反序项、相干与共轭都保留。最长行要求
\[
6M_{0,3}=Z_{31}+Z_{32}=0.
\tag{OE.3}
\]
下文证明 OE.3 与当前 \(U_3\) 的非零极化面积不相容；不需要求解另外两行。

## OE.2 从完整 NC 系数到实二次映射

每条边定义最长接收的正定向单位基
\[
E_j=\frac{q_j-(c_j/P)p}{\ell_j},\quad
\ell_j=\sqrt{\Delta_j/P},\qquad
N_j=\frac p{\sqrt P}\times E_j
=\frac{p\times q_j}{\sqrt{\Delta_j}}.
\tag{OE.4}
\]
发送端也用自己的正定向单位基
\[
F_j=\frac{p-(c_j/Q_j)q_j}{\sqrt{\Delta_j/Q_j}},
\qquad \widetilde N_j=\frac{q_j}{\sqrt{Q_j}}\times F_j=-N_j.
\]
发送种子唯一写成
\[
U_j=A_j(F_j+\eta_j\widetilde N_j),\qquad
A_j\ne0,\quad \eta_j\in\mathbb R.
\tag{OE.5}
\]
发送线性极化给 \(\eta_j\) 实；全活跃性给 \(A_j\ne0\)。\(A_j\) 可以是任意非零复数，其相位会通过完整发送协方差变为 \(|A_j|^2\)，没有人为设定种子相位。

接收坐标为
\[
X_j=U_3\cdot E_j,\qquad Y_j=U_3\cdot N_j.
\]
它们是同一个 \(U_3\) 的两个不同实基坐标。暂省 \(j\) 后，沿 NC 定义
\[
\lambda_\pm=P+Q\pm2c,\quad E_\pm^{\rm freq}=4P+Q\pm4c,\quad
\Lambda=\lambda_+\lambda_-,\quad\Omega=E_+^{\rm freq}E_-^{\rm freq},
\]
\[
\alpha=2-d\left[
\frac{Q+2c}{\lambda_+E_+^{\rm freq}}+
\frac{Q-2c}{\lambda_-E_-^{\rm freq}}\right],\qquad
\kappa=\frac{4cdP}{Q\Lambda},
\]
\[
H=4P^2-PQ+Q^2-4c^2,\qquad
\chi=\frac{4cd(2P+Q)H}{Q\Lambda\Omega},\qquad
L=2(\Delta/P)^{3/2}>0.
\tag{OE.6}
\]
频率上标只是避免与单位基 \(E_j\) 混淆。

与 NC 非单位基 \(U_3=ue+vn,\ U_j=xf+yn\) 比较，
\[
u=X/\ell,\quad v=Y/\sqrt\Delta,\qquad
x=A/\sqrt{\Delta/Q},\quad y/x=-\eta/\sqrt Q.
\]
发送比值实，所以 \(I=\Im(x\bar y)=0\)，但其完整实相干量 \(R=\Re(x\bar y)\) 仍保留。把这些关系直接代入 NC.7–8，得到
\[
\boxed{
Z_{3j}=iL_j|A_j|^2
\left[\chi_jX_j^2E_j+
\left(\kappa_jX_jY_j-\sqrt{P/Q_j}\,\alpha_j\eta_jX_j^2\right)N_j\right].}
\tag{OE.7}
\]
这是 \(X_j,Y_j\) 的实系数齐次二次向量映射乘 \(i\)；它不是只检查一个分量。接收坐标仍允许复数，未把 \(X_j^2\) 改为 \(|X_j|^2\)。

## OE.3 几何使两个关键比值都严格大于二

在 OE.1 上直接化简：
\[
\Lambda=\frac32Q(P+2Q)>0,
\qquad
\Omega=3(4P^2+2PQ+3Q^2)>0,
\]
\[
H=\frac32(2P^2-PQ+2Q^2)>0.
\tag{OE.8}
\]
因此 \(\chi,\kappa\) 均非零且同为 \(c\) 的符号。定义
\[
\mu=\frac{\kappa}{\chi}
=\frac{P\Omega}{(2P+Q)H}.
\]
完整化简为
\[
\boxed{
\mu=
\frac{2P(4P^2+2PQ+3Q^2)}
{(2P+Q)(2P^2-PQ+2Q^2)}
=2+\frac{4Q(P^2-Q^2)}
{4P^3+3PQ^2+2Q^3}>2.}
\tag{OE.9}
\]
手核等式只需展开
\((2P+Q)(2P^2-PQ+2Q^2)=4P^3+3PQ^2+2Q^3\)，
再将分子减去两倍分母；差恰为 \(4Q(P^2-Q^2)>0\)。
此处仅用 \(P>Q>0\)，没有数值求值或选择。

令每条边的实常数
\[
w_j=L_j|A_j|^2\chi_j\ne0,\qquad
\tau_j=\frac{\sqrt{P/Q_j}\,\alpha_j\eta_j}{\chi_j}\in\mathbb R,
\qquad \mu_j=\frac{\kappa_j}{\chi_j}>2.
\tag{OE.10}
\]
不假定 \(w_1,w_2\) 同号，\(\tau_j\) 可以为零或任意允许实值。OE.7 恰为
\[
\boxed{
Z_{3j}=i\,w_jX_j
\left[X_jE_j+(\mu_jY_j-\tau_jX_j)N_j\right].}
\tag{OE.11}
\]

## OE.4 用两条接收投影作同一实坐标

记
\[
\mathsf C=E_1\cdot E_2,\qquad
\mathsf S=\frac p{\sqrt P}\cdot(E_1\times E_2).
\]
三频独立性给 \(\mathsf C^2+\mathsf S^2=1\)、\(\mathsf S\ne0\)，并且
\[
E_2=\mathsf CE_1+\mathsf SN_1,\qquad
N_2=-\mathsf SE_1+\mathsf CN_1.
\tag{OE.12}
\]
允许 \(\mathsf C=0\)，以下不除以它。

令
\[
a=U_3\cdot E_1,\qquad b=U_3\cdot E_2.
\]
这两个实独立线性泛函给 \(p^\perp\) 的复化一个可逆实坐标系，因此
\[
Y_1=\frac{b-\mathsf Ca}{\mathsf S},\qquad
Y_2=\frac{\mathsf Cb-a}{\mathsf S}.
\tag{OE.13}
\]
把 OE.13 代入两个 OE.11，完整最长行成为
\[
\boxed{
\frac{Z_{31}+Z_{32}}i=
\mathbf A\,a^2+\mathbf B\,ab+\mathbf D\,b^2,}
\tag{OE.14}
\]
其中三个输出向量均为实向量：
\[
\mathbf A=w_1\left[E_1-
\left(\frac{\mu_1\mathsf C}{\mathsf S}+\tau_1\right)N_1\right],
\]
\[
\mathbf B=\frac{w_1\mu_1N_1-w_2\mu_2N_2}{\mathsf S},
\]
\[
\mathbf D=w_2\left[E_2+
\left(\frac{\mu_2\mathsf C}{\mathsf S}-\tau_2\right)N_2\right].
\tag{OE.15}
\]
两个发送方向参数保留在 \(\mathbf A,\mathbf D\)，未作独立边种子的替换；\(a,b\) 来自同一个 \(U_3\)。

以下四个实点积不含 \(\tau_j\)，是整个障碍的关键：
\[
\boxed{
\mathbf A\cdot E_1=w_1,\qquad
\mathbf D\cdot E_2=w_2,\qquad
\mathbf B\cdot E_1=w_2\mu_2,\qquad
\mathbf B\cdot E_2=w_1\mu_1.}
\tag{OE.16}
\]
例如 \(N_2\cdot E_1=-\mathsf S\)、\(N_1\cdot E_2=\mathsf S\)，直接给后两个等式。特别地 \(\mathbf B\ne0\)，整个向量二次式不可能恒零；\(\mathbf A,\mathbf D\) 也非零。

## OE.5 共同非实射影根的完整边界引理

对任意实系数二维向量齐次二次式
\[
Q(a,b)=\mathbf A a^2+\mathbf B ab+\mathbf D b^2,
\]
若 \(\mathbf B\ne0\) 且它有一个非实射影零点，则
\[
\boxed{\mathbf A,\mathbf B,\mathbf D\text{ 必共线。}}
\tag{OE.17}
\]
证明与边界逐一如下。

第一，非实射影点不可能是 \([1:0]\) 或 \([0:1]\)，这两个点都是实点；零坐标对也不是射影点。因此可令 \(b\ne0\)，写 \(z=a/b\in\mathbb C\setminus\mathbb R\)。在任意实输出基中，两个分量均为次数至多二的实多项式
\[
f(z)=A_1z^2+B_1z+D_1,\qquad
g(z)=A_2z^2+B_2z+D_2.
\]
第二，任一个非零实常数或一次式都不能在非实点为零。若某分量降次但非恒零，它已经排除该零点。若分量有该零点且非恒零，它必须是二次式，并因实系数同时有共轭根 \(\bar z\)。

第三，因而每个非恒零分量都是同一个实二次式
\[
(t-z)(t-\bar z)=t^2-2\Re(z)t+|z|^2
\]
的非零实倍数。若一个分量恒零而另一个非零，此结论仍使三个系数向量沿另一个输出轴共线；若两个分量都恒零，则 \(\mathbf B=0\)，与假设矛盾。两个非恒零分量同样给共线性。这证明 OE.17，包含恒零分量和全部降次情况。

上述证明未丢弃射影无穷点：它本来就是实点，不能代表非零极化面积。若要检查全体射影根，仍需单独检查 \(b=0\)；本稿的实际 \(\mathbf A\ne0\) 还直接说明 \([1:0]\) 不是零点，\(\mathbf D\ne0\) 同理排除 \([0:1]\)。

## OE.6 比值积给严格正判别式：最长行被排除

假设反证 OE.14 有一个非实射影根。由 OE.17 及 \(\mathbf B\ne0\)，存在实数 \(\lambda,\delta\) 使
\[
\mathbf A=\lambda\mathbf B,\qquad
\mathbf D=\delta\mathbf B.
\]
用 OE.16 分别与 \(E_1,E_2\) 点乘，强制
\[
\boxed{
\lambda=\frac{w_1}{w_2\mu_2}\ne0,\qquad
\delta=\frac{w_2}{w_1\mu_1}\ne0,\qquad
\lambda\delta=\frac1{\mu_1\mu_2}.}
\tag{OE.18}
\]
所以整个向量二次式在这个必要共线分支中只能是
\[
Q(a,b)=\mathbf B(\lambda a^2+ab+\delta b^2).
\]
因为 \(\mu_1,\mu_2>2\)，其一元实二次式的判别式满足
\[
\boxed{
1-4\lambda\delta
=1-\frac4{\mu_1\mu_2}>0.}
\tag{OE.19}
\]
实二次式因此只有两个不同的实射影根，不可能具有原假定的非实根。这里没有假设 \(w_1w_2>0\)：无论两权重同号或异号，乘积 \(\lambda\delta=1/(\mu_1\mu_2)\) 都相同。也没有忽略零首项，因为 OE.18 已证明 \(\lambda,\delta\ne0\)。

由此最长行的准确结论是
\[
\boxed{
Z_{31}+Z_{32}=0,\ U_3\ne0
\quad\Longrightarrow\quad
[a:b]\in\mathbb{RP}^1.}
\tag{OE.20}
\]
如果三个系数向量不共线，则已由 OE.17 排除非实根；如果共线，则由 OE.18–19 排除。没有遗漏“一个分量恒零”或“两个分量只是实比例”的情形。

最后，把射影结论与原向量性质明确连接。由 OE.13 的可逆实坐标变换，一个非零 \(U_3\) 的 \([a:b]\) 为实，当且仅当 \((a,b)\) 是非零复标量乘实坐标对，也当且仅当 \(U_3\) 是非零复标量乘实横向向量。等价地，
\[
i\frac p{\sqrt P}\cdot(U_3\times\overline U_3)=0.
\]
合同反而要求此面积非零，因此
\[
\boxed{\text{ONE_ELLIPTIC_CONTRACT 下 }M_{0,3}=0\text{ 不可能。}}
\tag{OE.21}
\]
全三行 \(M_0=0\) 特别要求该最长行零，故这个明确限定分支不能通过总混合首项相消门。

## OE.7 换基、缩放与适用范围

证明使用的 \(a,b\) 是同一 \(U_3\) 经可逆实坐标变换所得；“非实射影点”在任何可逆实换基下不变。共同复缩放 \(U_3\mapsto zU_3\) 仅将向量二次式乘 \(z^2\)，不改变射影根；每个发送种子的复缩放只将对应 \(w_j\) 乘正因子。OE.18 中这些发送因子在 \(\lambda\delta\) 中严格抵消，因此没有利用未授权的幅度选择。发送相干比值的全部允许实自由度 \(\eta_j\) 已保留为 \(\tau_j\)，判别式结论无需固定它们。

已处理的边界包括：\(\mathsf C=0\)、任意符号的 \(\mathsf S,w_j\)、零发送法向比、一个恒零输出分量、非零降次分量、比例分量、满足 \(U_3\cdot U_3=0\) 的接收向量以及射影零/无穷坐标。合同的三频独立、全活跃和非零种子排除 \(\mathsf S=0\)、\(A_j=0\) 等退化；OE.8 排除 \(\chi_j=0\)。本稿没有把这些被合同排除的退化情形误称为一般结论。

当前只得到一条待复核的有限空间首项排除：在 OE.1 的明确几何和两个线性发送种子条件下，最长零行迫使接收也线性极化。未在本稿接纳先前必要门的审查结果；将此结论与其它已接受节点分类连接，须由本阶段根实际比较后进行。

它不排除三个种子全线性、三个面积全非零或其它剩余极化模式；不分类所有三边图或任意模板。因为此限定分支连最长 \(M_0\) 零行都不能成立，这里无需也没有另行判断它的 \(W_0\)、实际整数候选或原方向门。本稿不新增任何真实 NS 时间结论，不把首项排除推广到有限正时间完全相消、其它时刻模板返回、两步再生成、统一迭代或奇性机制。没有实际数据、候选、无限尺度或有限总时间结论。LIMITED BRANCH OBSTRUCTION；NO-CANDIDATE ACCEPTED；NOT CLAY。

## 实际来源与字节

| 来源 | 本次实际阅读与用途 | SHA-256 |
|---|---|---|
| three-edge-compatibility/ONE_ELLIPTIC_CONTRACT.md | 全文；两条几何等式作为直接假设 | e8816e54ced5050ca5e2736f081825237edc828b71096a4a4241f660c330089d |
| net-mixed-cancellation/INDEPENDENT.md | 本人此前完整推导、自核的已接受最终稿；本轮重读第 53–137 行，使用完整 NC.7–8、非单位坐标及 NC.10 缩放 | 25111397d32eef2751a91b1ad1ab6a446794742874b97bf6b0b73b3964d11a58 |

上列哈希已实际核对。未使用本后续其它新推导或新审查补足证明，没有外部定理依赖或文献新颖性声明。本文自身哈希在最终写入与自核之后提供；纳入本阶段接纳仍须非作者实际复核。
