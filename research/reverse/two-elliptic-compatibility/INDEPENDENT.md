# 最低混合行的唯一实部消元与完整 C 原方向双条件

2026-09-08，PRIVATE_CORE。状态：独立有界推导完成，待非作者审查和根比较。

**本轮结果：在合同的两条 β 零几何假设下，完整最低 Z 行可唯一解出两个发送比值的实部，非零发送极化面积仍保留。同一最低 C 行始终非零；它是否沿原 U0 复方向，还必须且只须满足一条明确实三次式和一条有符号面积平衡式。本文给出这些条件及其系数退化分支，不声称它们已经由同一整数几何和全部三行实现。**

本稿未读取本目录 PROOF.md 或任何本项新推导。两条几何等式直接作为合同假设，不预记其它稿件的必要性证明。全部手工符号；未选择实际频率、极化、幅度或时间，没有科学程序、数组、数值求值、扫描、Git、重置信用、外发或发布。

## 1. 实际来源与同一数据的表示

路径相对于 research/reverse/。

| 实际来源及阅读范围 | SHA-256 |
|---|---|
| two-elliptic-compatibility/CONTRACT.md，本轮先全文读取 | ee05b39370f178cac5aebcf3c3046478c848c74b0078ee26edafb3282029ad52 |
| net-mixed-cancellation/INDEPENDENT.md，本连续任务此前全文非作者核验；本轮实际重读第 45–119 行，完整 NC.4–10 相干系数和复缩放 | 25111397d32eef2751a91b1ad1ab6a446794742874b97bf6b0b73b3964d11a58 |

这些文件内部列出的其它来源不自动记为本轮实读。本文直接从已接受完整 NC.7–9 继续手核，没有调用新的原解时间结论。

固定最低频率 p=p0，两个较高频率 q_j=p_j，j=1,2，记
\[
P=|p|^2<Q_1<Q_2,\quad Q_j=|q_j|^2,\quad
c_j=p\cdot q_j\ne0,\quad d_j=P-Q_j<0,\quad
\Delta_j=PQ_j-c_j^2>0.
\tag{TEI.1}
\]
三个实整数频率独立。直接假设
\[
8c_j^2=-4P^2+PQ_j+2Q_j^2,\qquad
Q_j/4<P<\frac{1+\sqrt{33}}8Q_j.
\tag{TEI.2}
\]
共同最低种子写为 U0=z0U，其中 z0≠0，U 为非零实横向向量。以下保留实际发送种子 V_j=U_j；把实际 Z_0j、C_0j 的共同接收因子 z0² 去掉，记为 Z_j、C_j。NC.10 保证这一操作不改变最低零行，也不改变 C_01+C_02 属于 C U0 的方向条件。

标准实基及坐标为
\[
e_j=q_j-\frac{c_j}{P}p,\quad
f_j=p-\frac{c_j}{Q_j}q_j,\quad n_j=p\times q_j,
\]
\[
U=u_je_j+v_jn_j,\qquad
V_j=x_j\bigl(f_j+(\xi_j+i\theta_j)n_j\bigr).
\tag{TEI.3}
\]
u_j、v_j 为实数，u_jx_j≠0；x_j 可以为复数。发送极化面积非零准确要求 θ_j≠0。事实上，采用固定有向面积
\[
\mathfrak h_j=\frac1{2i}q_j\cdot(\overline V_j\times V_j),
\]
因 q_j·(f_j×n_j)=−Δ_j，有
\[
\boxed{\mathfrak h_j=-\Delta_j|x_j|^2\theta_j\ne0.}
\tag{TEI.4}
\]
ξ_j、θ_j 不是独立协方差条目，而是同一个发送种子的确定性复比值。

## 2. β 零边的完整系数化简

暂略下标 j。沿用 λ_±=P+Q±2c、E_±=4P+Q±4c、Λ=λ_+λ_-、Ω=E_+E_-。由 TEI.2 直接得到
\[
\Lambda=\frac32P(2P+Q),\quad
\Omega=3(4P-Q)(2P+Q),\quad
H=4P^2-PQ+Q^2-4c^2=\frac32P(4P-Q).
\tag{TEI.5}
\]
它们严格为正。另有
\[
\lambda_\sigma E_\sigma
=3(2P+Q)(Q+2\sigma c),\qquad
Q^2-4c^2=\frac P2(4P-Q)>0.
\]
所以两个 h_σ=(Q+2σc)/(λ_σE_σ) 均等于 1/[3(2P+Q)]，从而
\[
\boxed{\beta=0,\quad
\alpha=\frac{2(5P+4Q)}{3(2P+Q)}>0,}
\]
\[
\boxed{
\chi=\frac{4cd(2P+Q)H}{Q\Lambda\Omega}
=\frac{4cd}{3Q(2P+Q)}\ne0,\qquad
\kappa=\frac{8cd}{3Q(2P+Q)}=2\chi.}
\tag{TEI.6}
\]
χ 与 c 的符号相反；不能把两边权重一律取正。

令 L=2Δ³/(P²Q)>0，w=v/u 为实。完整 NC.7–8 给
\[
\boxed{
Z_j=iL_j u_j^2|x_j|^2
\left[\chi_je_j+
\bigl(2\chi_jw_j+\alpha_j\xi_j\bigr)n_j\right].}
\tag{TEI.7}
\]
这里仅因 β=0，Z 中的发送虚相干消去；它没有使发送种子线性或使 Z_j 为零。

同一个发送种子满足
R=Re(x bar y)=|x|²ξ、I=Im(x bar y)=−|x|²θ。完整 NC.9 因此为
\[
\boxed{
C_j=\frac{4i\Delta_j^3d_j}{P^2Q_j^2\Lambda_j}
u_j^2|x_j|^2
\left[c_jd_je_j+
\bigl(Q_j(P+Q_j)\xi_j+2c_jPw_j
+2ic_jQ_j\theta_j\bigr)n_j\right].}
\tag{TEI.8}
\]
相干虚部的正 2icQθ 号来自同一个规定共轭，未删掉反馈。TEI.7–8 均为全部正负根及双有序 Leray 项已合并后的完整系数。

## 3. 单位基、共享最低方向与两个完整行

定义
\[
\ell_j=\sqrt{\Delta_j/P},\quad E_j=e_j/\ell_j,\quad
N_j=n_j/(\sqrt P\,\ell_j).
\]
令
\[
\mathsf C=E_1\cdot E_2,\quad
\mathsf S=N_1\cdot E_2,\quad
\mathsf C^2+\mathsf S^2=1.
\]
三频独立给 𝖲≠0，且
\[
E_2=\mathsf CE_1+\mathsf SN_1,\quad
N_2=-\mathsf SE_1+\mathsf CN_1.
\]
同一个实 U 的坐标写为
\[
a=U\cdot E_1\ne0,\quad
t=\frac{U\cdot E_2}{U\cdot E_1}\in\mathbb R\setminus\{0\},
\]
\[
A_1=a,\quad A_2=at,\qquad
B_1=\frac{a(t-\mathsf C)}{\mathsf S},\quad
B_2=\frac{a(\mathsf Ct-1)}{\mathsf S},
\tag{TEI.9}
\]
其中 A_j=U·E_j、B_j=U·N_j。零或无穷 t 会使最低某条边失活，已被合同排除；没有把两条边的接收方向独立化。

定义保留发送投影模方的实非零权重及实变量
\[
k_j=\frac{L_j|x_j|^2\chi_j}{\ell_j}\ne0,\qquad
r=\frac{k_2}{k_1}\in\mathbb R\setminus\{0\},
\]
\[
\eta_j=\frac{\sqrt P\,\alpha_j}{\chi_j}\xi_j,\qquad
\nu_j=\frac{2Q_j}{\sqrt P}\theta_j\ne0,
\]
\[
\sigma_j=\frac{d_j}{P}<0,\qquad
\rho_j=\frac{2d_j(P+Q_j)}{P(5P+4Q_j)}<0.
\tag{TEI.10}
\]
sign r=sign(c1c2)，发送整体复相位不进入这些行。TEI.7–8 精确成为
\[
\boxed{
Z_j=ik_j\left[A_j^2E_j+
\bigl(2A_jB_j+\eta_jA_j^2\bigr)N_j\right],}
\tag{TEI.11}
\]
\[
\boxed{
C_j=ik_j\left[\sigma_jA_j^2E_j+
\bigl(2A_jB_j+\rho_j\eta_jA_j^2
+i\nu_jA_j^2\bigr)N_j\right].}
\tag{TEI.12}
\]
例如 C 的平面系数与 Z 的平面系数之比为 d/P；实发送项的比例是 ρ_j，接收反馈仍为 2A_jB_j。iν_j 是保留下来的发送面积项。

## 4. 最低 Z 零行的唯一发送实部

Z1+Z2 除去公共 i 后为实向量。E1、E2 实独立，所以其为零当且仅当与两个 E 的点积都为零。由 TEI.11，
\[
\frac{(Z_1+Z_2)\cdot E_2}{ik_1a^2}
=-\mathsf C+2t+\mathsf S\eta_1+rt^2,
\]
\[
\frac{(Z_1+Z_2)\cdot E_1}{ik_1a^2}
=1+r\bigl[2t+(-\mathsf C-\mathsf S\eta_2)t^2\bigr].
\]
因此得到完整充要式
\[
\boxed{
Z_1+Z_2=0\iff
\eta_1=\frac{\mathsf C-2t-rt^2}{\mathsf S},\qquad
\eta_2=\frac{-\mathsf C+2/t+1/(rt^2)}{\mathsf S}.}
\tag{TEI.13}
\]
相应原发送实部唯一为
\[
\boxed{\xi_j=
\frac{2c_jd_j}{\sqrt P\,Q_j(5P+4Q_j)}\,\eta_j.}
\tag{TEI.14}
\]
𝖲、r、t、χ_j 均非零，α_j 严格正，所以本合同内没有零线性系数、漏解或额外自由的发送实部分支。𝖢、η_j、ξ_j 可以为零；证明没有除以它们。

对给定共同实 U、发送 x_j≠0 及 θ_j≠0，这一唯一实部解不改变 |x_j|² 或面积 TEI.4。它也不因两高种子之间的交叉点积产生新的失活：一个面积非零的复横向种子的实、虚部实独立，若再同时横向于另一个非平行实频率，两者会被限制在一条实直线上，矛盾。因此 TEI.13 确实给该固定几何和这些符号数据下最低零行的充分解；它不意味着两个较高 M0 行也为零，更不是实际参数选择或整数实例。

## 5. 同一最低 C 行的原方向：两条精确实条件

定义
\[
\Gamma_j=2-\sigma_j-\rho_j,\qquad
\delta=\rho_2-\rho_1.
\tag{TEI.15}
\]
在 TEI.13 的最低零行上，令
\[
\boxed{
\mathcal F(t)=
\Gamma_1(t-\mathsf C)
+r\Gamma_2t^2(\mathsf Ct-1)
+\delta t(1+rt).}
\tag{TEI.16}
\]
对固有双线性交替形式 ω_p(U,X)=p·(U×X)，有
ω_p(U,E_j)=−√P B_j、ω_p(U,N_j)=√P A_j。把 TEI.12 代入并使用 TEI.13，直接得到
\[
\boxed{
\omega_p(U,C_1+C_2)
=i\sqrt P\,k_1a^3
\left[\frac{\mathcal F(t)}{\mathsf S}
+i\bigl(\nu_1+rt^3\nu_2\bigr)\right].}
\tag{TEI.17}
\]
实部计算可先保留为
(2−σ1)(t−𝖢)+ρ1(𝖢−2t−rt²)
+rt²[(2−σ2)(𝖢t−1)+ρ2(−𝖢t+2+1/(rt))]；
逐项整理恰为 TEI.16。没有只检查 C 的某个坐标。

因为 U 非零而 ω_p 在复二维横向平面非退化，完整方向条件为
\[
\boxed{
C_1+C_2\in\mathbb C U
\iff
\mathcal F(t)=0,\qquad
Q_1\theta_1+rQ_2t^3\theta_2=0.}
\tag{TEI.18}
\]
这里已假设且仅假设最低 Z 行使用 TEI.13。两个条件分别是完整行列式的实、虚要求，不能以 Z 中的 β 零为由删去第二条。

面积条件还可写成不含发送坐标模方的固有形式：
\[
\boxed{
\sum_{j=1}^2
\frac{c_jd_j}{Q_j(2P+Q_j)}
(U\cdot q_j)^3\mathfrak h_j=0.}
\tag{TEI.19}
\]
它由 TEI.4、10 直接代入得到，公共常数不影响零式。特别地，各量非零使
\[
\boxed{
\operatorname{sgn}(\mathfrak h_1\mathfrak h_2)
=-\operatorname{sgn}(rt)
=-\operatorname{sgn}\!\left[
c_1c_2(U\cdot q_1)(U\cdot q_2)\right].}
\tag{TEI.20}
\]
符号不满足时，最低 C 的原方向立即失败；满足符号仍须 TEI.18 的准确幅度关系及实方程。

此外最低 C 行在本合同中始终非零，不需要方向条件。由 TEI.12，(C1+C2)/i 的虚部为
\[
k_1\nu_1A_1^2N_1+k_2\nu_2A_2^2N_2.
\]
两个 N 实独立，两个系数各自非零，所以该虚部不为零。这在去掉共同接收相位的表示中证明完整 C1+C2≠0；恢复 z0² 后仍成立。因此最低 W0 分量非零，但它本身不支付原方向 TEI.18。

## 6. 实方向方程的零系数及降次分支

为不隐藏可能为零的消元分母，置无量纲实数 ζ_j=Q_j/P，故 1<ζ1<ζ2<4。由 TEI.10，
\[
\rho(\zeta)=\frac{2(1-\zeta^2)}{5+4\zeta}<0,\qquad
\Gamma(\zeta)=1+\zeta-\rho(\zeta)
=\frac{3(1+\zeta)(1+2\zeta)}{5+4\zeta}>0.
\]
直接通分给
\[
\delta=
-\frac{2(\zeta_2-\zeta_1)
[4\zeta_1\zeta_2+5(\zeta_1+\zeta_2)+4]}
{(5+4\zeta_1)(5+4\zeta_2)}<0.
\tag{TEI.21}
\]
定义
\[
\mathcal A=\Gamma_1+\delta,\qquad
\mathcal B=\Gamma_2-\delta.
\]
这两个量严格为正。对 1<ζ<4，
ρ(ζ)+2=2[ζ(4−ζ)+6]/(5+4ζ)>0，
所以
𝒜=1+ζ1+ρ2−2ρ1>0；𝓑>0 则立即由 Γ2>0、δ<0 得到。

TEI.16 等价于
\[
\boxed{
\mathcal F(t)=N(t)+rD(t),\quad
N(t)=\mathcal A t-\Gamma_1\mathsf C,\quad
D(t)=t^2(\Gamma_2\mathsf Ct-\mathcal B).}
\tag{TEI.22}
\]
准确分支为：

- D(t)≠0：实方向条件当且仅当 r=−N(t)/D(t)，该值仍须非零且符合同一发送模方给定的 sign r=sign(c1c2)。若 N=0 而 D≠0，所需 r=0 被合同排除。
- D(t)=0、N(t)≠0：任何允许发送权重都不能满足实方向。
- D(t)=N(t)=0：实方向对当前 t 不再约束非零 r，但面积条件、TEI.13 和其它行均须保留；不能错误除以 D。

这最后一个退化分支可写清为
\[
\boxed{
\mathsf C\ne0,\qquad
t=\frac{\mathcal B}{\Gamma_2\mathsf C},\qquad
\mathsf C^2=\frac{\mathcal A\mathcal B}{\Gamma_1\Gamma_2}.}
\tag{TEI.23}
\]
Γ2−Γ1=(ζ2−ζ1)−δ>0，故
𝒜𝓑=Γ1Γ2+δ(Γ2−Γ1)−δ²；
结合 𝒜、𝓑>0，TEI.23 右侧严格在 (0,1) 内。这只是可核的退化几何条件，不是证明合同整数几何已经实现它。

若 𝖢=0，D(t)=−𝓑t² 非零，唯一实方向关系为
\[
\boxed{t=\frac{\mathcal A}{r\mathcal B}.}
\tag{TEI.24}
\]
此时 rt>0，所以 TEI.20 进一步要求两高面积符号相反。实方程从三次降为 t(𝒜−r𝓑t)，但 t=0 失活根不属于合同。

没有其它恒零多项式遗漏：𝖢≠0 时 TEI.16 的三次系数 rΓ2𝖢 非零；𝖢=0 时 𝒜、𝓑、r 均非零，降次式也不恒零。最低 Z 消元中的可能零实部、C 方向中的 D=0、𝖢=0 和所有允许权重符号均已保留。

## 7. 准确产出与尚未解决部分

在同一固定合同数据内，最低 Z 零行与 TEI.13–14 双向等价。在该零行上，完整最低 C 与原 U0 复平行当且仅当 TEI.18 的实方向式与非零面积平衡同时成立；该 C 本身严格非零。TEI.20 给即时符号障碍，TEI.22–24 列出实方程全部零分母及降次分支。

这是实际的共享实部消元和完整方向条件，超出仅重述负实射线或幅度循环。它没有证明所有剩余分支无解，也没有以符号条件代替实例。虽然对给定合法几何及其余符号量最低 Z 的实部解唯一存在，最低 C 方向的联合条件、两个较高接收的完整 M0 行、同一整数几何的实际实现、其它接收方向及共同模板幅度仍须另核。

两个发送面积始终通过同一种子的 ξ+iθ 与投影模方保留，没有强度平均或自由协方差。U0 的两个邻边基共享一个实方向，发送种子也始终是同一组三对数据。没有把 β 零当作发送线性、完整 Z 零或 C 虚相干消失。

本稿仅为有限空间首项的精确代数，不新增真实 NS 时间、来源比、模板再生成或跨代误差结论。未来若连接原解，须再次明确同一数据的 SOURCE_BRIDGE 预算。统一迭代、同一初值无限尺度、无限维跨代控制、有限总时间及奇性均未支付。没有实际参数、候选或旧失败证据修复。

SHARED LOWEST-ROW ELIMINATION AND EXACT DIRECTION CONDITIONS；HIGHER ROWS OPEN；NO-CANDIDATE；NOT CLAY。
