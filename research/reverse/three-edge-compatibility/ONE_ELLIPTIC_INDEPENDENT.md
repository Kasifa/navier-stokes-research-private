# 两线性发送下最长接收行的非实射影根：独立排除

2026-09-08，PRIVATE_CORE。状态：独立手工推导完成，待非作者审查和根实际比较。

**结论：在 ONE_ELLIPTIC_CONTRACT 明确假设的两条几何等式及其余合同条件下，若发送种子 U1、U2 线性极化，而最长接收种子 U3 的极化面积非零，则完整 Z31+Z32 必不为零。因此这组显式假设下不能满足全部 M0=0；无需先决定 W0。**

本稿把两条几何等式直接作为假设，不预先接纳它们在其它推导中作为“必要门”的证明。没有读取 ONE_ELLIPTIC_ANALYSIS.md 或本目录 INDEPENDENT.md，没有借用另一路本项结果。下面直接从已接受的完整 NC.7–8 推导两个共享接收坐标的实系数齐次二次分量，并作显式消元；零分量、降次、首坐标零和可能负的通道权重均保留。没有实际新数据、频率、极化、幅度或时间选择。

## 1. 合同、实际来源和共同数据

本轮实际阅读全文合同，并重读已接受完整相干公式。路径相对于 research/reverse/。

| 来源与实际阅读范围 | SHA-256 |
|---|---|
| three-edge-compatibility/ONE_ELLIPTIC_CONTRACT.md，本轮全文；两条几何等式直接作为假设 | e8816e54ced5050ca5e2736f081825237edc828b71096a4a4241f660c330089d |
| net-mixed-cancellation/INDEPENDENT.md，本连续任务此前全文非作者审查；本轮实际重读第 50–119 行，NC.4–10 的标准基、完整相干和与复缩放 | 25111397d32eef2751a91b1ad1ab6a446794742874b97bf6b0b73b3964d11a58 |

此前本审查人已审过三边主稿的共享坐标系统；本次不使用尚未读取或尚待审的三边独立必要门。来源内部的其它读取记录不冒记为本轮实读。

将最长频率写为 p=p3，两发送频率写为 q_j=p_j，j=1,2。记
\[
P=|p|^2,\quad Q_j=|q_j|^2<P,\quad
c_j=p\cdot q_j\ne0,\quad
\Delta_j=PQ_j-c_j^2>0,\quad d_j=P-Q_j>0.
\tag{OEI.1}
\]
三个实整数频率线性独立，三边全部活跃，负模为原种子的规定共轭。直接假设
\[
8c_j^2=-4Q_j^2+PQ_j+2P^2,\qquad
\frac P4<Q_j<\frac{1+\sqrt{33}}8P,
\quad j=1,2.
\tag{OEI.2}
\]
仍保留 Q1<Q2；下面的最长行论证并不需要利用两个叶长度的排序。

接收为同一个 U=U3，发送为实际 V_j=U_j。每条边采用
\[
e_j=q_j-\frac{c_j}{P}p,\qquad
f_j=p-\frac{c_j}{Q_j}q_j,\qquad n_j=p\times q_j,
\]
\[
U=u_je_j+v_jn_j,\qquad V_j=x_jf_j+y_jn_j.
\tag{OEI.3}
\]
活跃性保证 u_jx_j≠0。由于每个 V_j 是非零复标量乘非零实向量，实基中的比值
\[
\zeta_j=\frac{y_j}{x_j}\in\mathbb R
\tag{OEI.4}
\]
成立；x_j 本身仍可有任意复相位。U 不被假定为线性极化，其两组坐标始终属于同一个向量。

## 2. 完整相干系数和关键比值 b_j>2

暂略 j 下标，沿用
\[
\lambda_\pm=P+Q\pm2c,\quad E_\pm=4P+Q\pm4c,
\quad\Lambda=\lambda_+\lambda_-,\quad\Omega=E_+E_-,
\]
\[
h_\pm=\frac{Q\pm2c}{\lambda_\pm E_\pm},\quad
\alpha=2-d(h_++h_-),\quad
\kappa=\frac{4cdP}{Q\Lambda},
\]
\[
H=4P^2-PQ+Q^2-4c^2,\quad
L=\frac{2\Delta^3}{P^2Q}>0,\quad
a=\frac{4cd(2P+Q)H}{Q\Lambda\Omega}.
\tag{OEI.5}
\]
各频率分母非零。P>Q 给 H=d(4P−Q)+4Δ>0，所以 a、κ 均非零且与 c 同号。

因 x\bar y=|x|²ζ 为实，完整 NC.7–8 精确化为
\[
\boxed{
Z_{3j}=iL_j|x_j|^2
\left[a_ju_j^2e_j+
\bigl(\alpha_j\zeta_ju_j^2+\kappa_ju_jv_j\bigr)n_j\right].}
\tag{OEI.6}
\]
这仍是 G_++G_- 的完整和，两个完整混合根内的双有序项、Leray 和发送共轭已包含在已接受系数中。接收的 u_j²、u_jv_j 是复二次项；反馈 κ_j 没有被删除。发送整体相位只留下 |x_j|²，实发送相干 ζ_j 保留。

定义本稿的几何比值
\[
b_j=\frac{\kappa_j}{a_j}.
\tag{OEI.7}
\]
它不是其它稿件在额外叶零关系下定义的含发送比值的系数。由 OEI.2，逐项得到
\[
\Lambda=\frac32Q(P+2Q),\qquad
\Omega=3(4P^2+2PQ+3Q^2),
\]
\[
H=\frac32(2P^2-PQ+2Q^2),\qquad
\Delta=\frac{(4Q-P)(Q+2P)}8.
\tag{OEI.8}
\]
因此
\[
\boxed{
b=\frac{P\Omega}{(2P+Q)H}
=\frac{2P(4P^2+2PQ+3Q^2)}
{(2P+Q)(2P^2-PQ+2Q^2)}.}
\tag{OEI.9}
\]
分母展开为 4P³+3PQ²+2Q³，故
\[
\boxed{
b-2=\frac{4Q(P^2-Q^2)}
{4P^3+3PQ^2+2Q^3}>0.}
\tag{OEI.10}
\]
这里仅用同一固定几何的符号等式与 0<Q<P，没有求值或挑选频率。因此两条实际通道都满足 b1>2、b2>2。

## 3. 同一接收平面上的两个完整二次分量

置
\[
\ell_j=|e_j|=\sqrt{\Delta_j/P},\qquad
E_j=e_j/\ell_j,\qquad
N_j=n_j/(\sqrt P\,\ell_j).
\]
每对 (E_j,N_j) 是同一实平面 p⊥ 的正交单位基，且 p×E_j=√P N_j。记
\[
C=E_1\cdot E_2,\qquad S=N_1\cdot E_2,\qquad C^2+S^2=1.
\]
三频独立保证 S≠0。因此
\[
E_2=CE_1+SN_1,\qquad N_2=-SE_1+CN_1.
\tag{OEI.11}
\]
没有要求 C≠0，也没有限定 S 的符号。

对同一个复接收向量 U，采用两个实线性泛函给出的坐标
\[
s=U\cdot E_1,\qquad t=U\cdot E_2.
\]
它们组成合法的复线性坐标，并有
\[
U\cdot N_1=\frac{t-Cs}{S},\qquad
U\cdot N_2=\frac{Ct-s}{S}.
\tag{OEI.12}
\]
这两式同时用于两条通道，没有独立选择邻边极化。

将 OEI.6 改写到单位基，定义
\[
k_j=\frac{L_j|x_j|^2a_j}{\ell_j}\in\mathbb R\setminus\{0\},
\qquad
\eta_j=\frac{\sqrt P\,\alpha_j\zeta_j}{a_j}\in\mathbb R.
\tag{OEI.13}
\]
各 k_j 的符号为 c_j 的符号，不假定两个 k 同号。若记 s_j=U·E_j、t_j=U·N_j，则
\[
\boxed{
\frac{Z_{3j}}i=k_j
\left[s_j^2E_j+
\bigl(b_js_jt_j+\eta_js_j^2\bigr)N_j\right].}
\tag{OEI.14}
\]
η_j 是同一实际发送种子的相干量，不是逐边重选的数据。下面的论证对其任意实值均成立，因而无需假设实际发送形状可以自由实现所有 η_j。

设
\[
r=\frac{k_2}{k_1}\in\mathbb R\setminus\{0\},\qquad
\mathcal A=(1-b_2)C-\eta_2S,\qquad
\mathcal B=\eta_1-\frac{b_1C}{S}.
\tag{OEI.15}
\]
将 OEI.11–12 完整代入两条 OEI.14，得到
\[
\boxed{Z_{31}+Z_{32}=ik_1
\bigl[f(s,t)E_1+g(s,t)N_1\bigr],}
\tag{OEI.16}
\]
其中两个实系数齐次二次多项式为
\[
\boxed{f(s,t)=s^2+rb_2st+r\mathcal A t^2,}
\]
\[
\boxed{
g(s,t)=\mathcal B s^2+
\frac{b_1-rb_2C}{S}st+
\frac{r(1-C\mathcal A)}{S}t^2.}
\tag{OEI.17}
\]
第二式的 t² 系数使用
S²+b2C²+η2CS=1−C𝒜；交叉项使用 N2 的 −S 分量。两种发送相位均已通过完整协方差约去，接收坐标仍是复数。因此 f、g 的系数确为实数，而不是把接收比值当成实数。

## 4. 极化面积与非实射影图

定义接收极化面积
\[
\mathfrak h(U)=\frac1{2i}p\cdot(\bar U\times U)\in\mathbb R.
\]
若 s=0，则 U=(t/S)N1，非零 U 已是复标量乘实向量，故其面积为零。合同的面积非零因此排除首坐标零；这也是被排除的射影无穷点，而非未经说明的相除。

现在 s≠0，令 z=t/s。由 OEI.12，
\[
U=s\left[E_1+\frac{z-C}{S}N_1\right],\qquad
\boxed{\mathfrak h(U)=\frac{\sqrt P\,|s|^2}{S}\Im z.}
\tag{OEI.18}
\]
所以面积非零当且仅当 z 非实。尤其 t 也非零；t=0 对应另一条实方向。除以 s² 只是同一齐次二次方程的射影表示，不是选择或更换实际初值。

因此待检验的完整零行等价于 f(1,z)=g(1,z)=0，而合同要求 Im z≠0。

## 5. 共同非实根的显式消元和判别式矛盾

先不除以任何多项式系数，记
\[
K=C+S\mathcal B.
\]
由 OEI.17 直接相减得到恒等式
\[
\boxed{
S\bigl(g-\mathcal B f\bigr)
=t\left[(b_1-rb_2K)s+r(1-\mathcal A K)t\right].}
\tag{OEI.19}
\]
若 s,t 均非零且 f=g=0，便有
\[
(b_1-rb_2K)+r(1-\mathcal A K)z=0.
\tag{OEI.20}
\]
两项系数均为实数。对于非实 z，实一次式只能在两个系数同时为零时成立。因此共同非实根必要地要求
\[
b_1-rb_2K=0,\qquad 1-\mathcal A K=0,
\]
\[
\boxed{
K=\frac{b_1}{rb_2}\ne0,\qquad
\mathcal A=\frac{rb_2}{b_1}.}
\tag{OEI.21}
\]
这里只除以已保证非零的 r、b1、b2；没有除以 𝒜、𝓑、C 或任何可能为零的二次分量。

OEI.21 同时使 OEI.19 的右侧恒为零，故 g=𝓑f；这说明可能的非实共同因子确实只能出现在两个分量成比例的分支，包括 g 恒零的情形。但此时
\[
f(1,z)=1+rb_2z+r^2\frac{b_2}{b_1}z^2.
\tag{OEI.22}
\]
其二次系数严格为正，判别式为
\[
\boxed{
\mathcal D_f
=r^2b_2^2-4r^2\frac{b_2}{b_1}
=r^2\frac{b_2}{b_1}(b_1b_2-4)>0,}
\tag{OEI.23}
\]
因为 b1>2、b2>2。因此 f(1,z) 的两个根均实，不能容纳假设的非实 z，矛盾。

这个证明没有仅由“两个实二次多项式共享非实根”省略边界；OEI.19 的显式消元先处理了全部系数，再由真实判别式结束。

## 6. 零多项式、降次和符号边界

上述消元可逐项核对所有允许边界：

- f(s,t) 的 s² 系数恒为 1，故 f 不可能恒零。如果 𝒜=0，f(1,z)=1+rb2z 是非零实一次式，不能有非实根；它也与共同非实根必要的 OEI.21 直接矛盾。rb2≠0，所以 f 不会进一步降成常数。
- g 可以恒零；OEI.19–21 从未除以 g 或 𝓑，仍强制同一个判别式矛盾。如果 g(1,z) 降为非零一次式或常数，它本身即不能有非实根。一般二次情形已由同一消元覆盖。
- 首坐标 s=0 和 t=0 都对应实射影方向，极化面积为零，故不能属于当前合同。没有丢失非实射影无穷根。
- r 可以为任意非零实数，最终只通过 r² 进入判别式；两个 c 的符号不同不构成漏洞。C、𝒜、𝓑、η_j 或 α_j 可以为零，证明均未以它们为分母。消元中的 S、r、b_j 均非零；标准化所需的 a_j、k_j、x_j、ℓ_j 及射影坐标 s、t 的非零性已分别说明，其余频率分母由合同几何支付。
- U·U 可以为零，整个证明未使用双线性自点积分母。接收面积非零也未被替换为某个单螺旋或线性极化假设。

尤其，两个分量成比例并不自动产生共同非实根；本合同恰使其剩余实二次因子的判别式严格为正。这是本次排除的核心。

## 7. 实际结论与未付范围

综上，合同两条显式几何等式下的最长接收行满足
\[
\boxed{
\mathfrak h(U_3)\ne0,\quad U_1,U_2\text{ 线性极化}
\quad\Longrightarrow\quad Z_{31}+Z_{32}\ne0.}
\tag{OEI.24}
\]
因 M0_3=(Z31+Z32)/6，全部 M0=0 已经在这一接收频率失败。其它接收行不能跨 Fourier 频率取消它；无须用单边非零替代总和，也不必先判定 W0。

这排除的是本合同直接列出的几何假设和极化分支。本稿不把未读、待审的“跨组必要门”预先接纳；若以后要将 OEI.24 用于更大的“恰一个面积非零”分类，必须另行付清相应几何必要性的证明与审查。没有扩张到两个或三个面积非零、等长、正交、失活或线性相关频率。

全部结果是完整有限空间首项的精确代数。没有新增真实原解的时间结论、来源比下界、模板返回或再生成排除；没有接受实际整数实例、初值或时间。一个固定初值的无限尺度、统一迭代、跨代无限维余项、有限总时间、奇性及全局正则性均未支付。没有使用或修复旧失败数值证据。

全部工具只作文本读取、写入与 SHA-256；无科学程序、数组、数值求值、扫描、Git、重置信用、图档或外发。本文自身哈希在全文自核停改后另行提供。

CONDITIONAL ONE-ELLIPTIC LONGEST-ROW OBSTRUCTION；NO-CANDIDATE；NOT CLAY。
