# 最长完整零行的面积同号律及最低方向的必要几何门

2026-09-08，PRIVATE_CORE。独立有界推导完成，待分开的非作者审查和根比较。

**结果：严格最长且极化面积非零的接收种子，面对一个线性较短发送和一个面积非零较短发送时，完整两项 Z 总行为零强制接收与后者的有向面积同号。本文给出两个独立完整点积、全部实虚条件及一个系数严格正的面积恒等式。若同时要求本合同的最低 Z 零行与最低 C 原方向，则最低变量必须满足 r_min t_min<0，且进一步必须有 r_min C_min<0。它们只是必要门；整数几何、两个较高完整行的共同实现及机制仍未解决。**

本稿从先锁合同及已接纳 NC、MAX、最低行接口自行推导，未读取 HIGHER_AREA_PROOF.md、HIGHER_ROW_PROJECTION.md 或本轮其它高行推导、审查。没有调用最低行某一存在分支作为全部根的代表。全部手工符号；没有科学程序、数组、数值求值、实际频率或种子选参、扫描、Git、重置、外发或发布。

## 1. 实际来源与最长行的同一组三种子

路径相对于 research/reverse/。

| 实际来源及阅读范围 | SHA-256 |
|---|---|
| two-elliptic-compatibility/HIGHER_AREA_CONTRACT.md，本轮先全文读取 | 25b207f2212904a1bd58a430f8d39d1d93c3bc9a28e957a260316975b41e5f4f |
| two-elliptic-compatibility/CONTRACT.md，本轮全文读取 | ee05b39370f178cac5aebcf3c3046478c848c74b0078ee26edafb3282029ad52 |
| net-mixed-cancellation/INDEPENDENT.md，本轮实际重读第 44–119 行，完整 NC.4–10 | 25111397d32eef2751a91b1ad1ab6a446794742874b97bf6b0b73b3964d11a58 |
| three-edge-compatibility/MAX_RECEIVER_RATIO.md，本轮首次全文读取，实际手核所用 b−2 恒等式 | ff52531d6e1b5563c99504aba8e6b6e4e5afce77b76e7e286e74d397c3d610c5 |
| two-elliptic-compatibility/INDEPENDENT.md，本连续任务此前全文逐式审查；本轮实际重读第 120–338 行的最低方向、面积及实三次式接口 | 9a39799e39b9ec40e4ae61e86f3b0dda0dabc0885dcbea17febd91b868524da9 |

文件内部转引的其它来源不自动记作本轮实读。以下最长行面积律本身不需要最低两条 β 零几何；最后与最低接口比较时才使用原合同的该附加假设。

取同一三频中
\[
p=p_2,\qquad q_0=p_0,\qquad q_1=p_1,\qquad
P=|p|^2>Q_1>Q_0>0,\quad Q_j=|q_j|^2.
\tag{HA.1}
\]
令 W=U2 为最长接收种子，V0=U0 为线性发送，V1=U1 为另一个面积非零发送。固定有向面积约定
\[
\mathfrak h(V;q)=\frac1{2i}q\cdot(\overline V\times V).
\]
原假设为
\[
\mathfrak h(W;p)\ne0,\qquad
\mathfrak h(V_0;q_0)=0,\qquad
\mathfrak h(V_1;q_1)\ne0.
\tag{HA.2}
\]
三频实独立，全部非正交，三条边活跃，负模是同一组三种子的共轭。没有按接收行重新指定任何种子。

对 j=0,1，记
\[
c_j=p\cdot q_j\ne0,\quad
d_j=P-Q_j>0,\quad
\Delta_j=PQ_j-c_j^2>0,
\]
\[
e_j=q_j-\frac{c_j}{P}p,\quad
f_j=p-\frac{c_j}{Q_j}q_j,\quad n_j=p\times q_j,
\]
\[
\ell_j=\sqrt{\Delta_j/P},\qquad
E_j=e_j/\ell_j,\qquad N_j=n_j/(\sqrt P\,\ell_j).
\tag{HA.3}
\]
每组 E_j、N_j 是有向实标准正交基，\(E_j\times N_j=p/\sqrt P\)。表示完整种子为
\[
W=A_jE_j+B_jN_j,\qquad
V_j=X_j\bigl(f_j+(\xi_j+i\theta_j)n_j\bigr),
\tag{HA.4}
\]
其中 A_j、B_j、X_j 可以为复数，ξ_j、θ_j 为实数；活跃性给 X_j≠0。线性发送的复比值为实，故 θ0=0；另一发送 θ1≠0。由同一个基的叉积，
\[
\mathfrak h(V_j;q_j)=-\Delta_j|X_j|^2\theta_j,\qquad
\mathfrak h(W;p)=\sqrt P\,\operatorname{Im}(\overline {A_j}B_j).
\tag{HA.5}
\]
接收面积非零特别保证 A0、A1 非零。这也可由非零面积种子的实、虚部独立、不能同时横向于另一非平行实频率直接看出。

## 2. 完整系数中发送虚相干的精确比例

暂略边下标。沿用
\[
\lambda_\pm=P+Q\pm2c,\qquad E_\pm^{\rm root}=4P+Q\pm4c,
\]
\[
\Lambda=(P+Q)^2-4c^2>0,\qquad
\Omega=(4P+Q)^2-16c^2>0,
\]
\[
H=4P^2-PQ+Q^2-4c^2=d(4P-Q)+4\Delta>0.
\]
这里 \(E_\pm^{\rm root}\) 是 NC 根分母，与单位向量 E_j 不同。令
\[
h_\pm=\frac{Q\pm2c}{\lambda_\pm E_\pm^{\rm root}},\quad
\alpha=2-d(h_++h_-),\quad \beta=-d(h_+-h_-),
\]
\[
\kappa=\frac{4cdP}{Q\Lambda},\qquad
\chi=\frac{4cd(2P+Q)H}{Q\Lambda\Omega},\qquad
b=\frac{\kappa}{\chi}.
\tag{HA.6}
\]
由 P>Q、c≠0、H>0，χ、κ 非零且同号。设
\[
K=4P^2-PQ-2Q^2+8c^2
=Q^2+7Qd+4d^2+8c^2>0.
\]
MAX 的展开给
\[
P\Omega-2(2P+Q)H=QK,\qquad
b-2=\frac{QK}{(2P+Q)H}>0.
\tag{HA.7}
\]
为核发送虚相干，独立展开
\[
\lambda_\sigma E_\sigma^{\rm root}
=(P+Q)(4P+Q)+8c^2+6\sigma c(2P+Q).
\]
以共同分母 ΛΩ 通分，得到
\[
h_+-h_-=\frac{4cK}{\Lambda\Omega},\qquad
\beta=-\frac{4cdK}{\Lambda\Omega}.
\]
因此关键精确恒等式是
\[
\boxed{\frac{\beta}{\chi}=2-b<0.}
\tag{HA.8}
\]
特别地，两条最长接收边的 β 均非零；不能将最低逆向边的 β 零条件搬到这里。上述过程未除以 α，以下亦不预设 α 非零。

定义固定实权重和完整复发送系数
\[
L_j=\frac{2\Delta_j^3}{P^2Q_j}>0,\qquad
k_j=\frac{L_j|X_j|^2\chi_j}{\ell_j}\ne0,
\]
\[
\gamma_j
=\frac{\sqrt P}{\chi_j}
\bigl(\alpha_j\xi_j-i\beta_j\theta_j\bigr)
=\frac{\sqrt P\,\alpha_j}{\chi_j}\xi_j
+i\sqrt P(b_j-2)\theta_j.
\tag{HA.9}
\]
γ0 是实数，但 γ1 的虚部必须保留。代入完整 NC.7–8，并用 \(u_j=A_j/\ell_j\)、\(v_j=B_j/(\sqrt P\,\ell_j)\)，得
\[
\boxed{
Z_{2j}
=ik_j\left[A_j^2E_j+
\bigl(b_jA_jB_j+\gamma_jA_j^2\bigr)N_j\right].}
\tag{HA.10}
\]
这是完整两根、双有序 Leray 项合并后的两向量分量。R=|X|²ξ、I=−|X|²θ 的共轭号已被 HA.9 保留；没有强度平均或删掉虚相干。

## 3. 两个独立完整点积与非实接收比

取接收平面中的几何旋转
\[
\mathsf C=E_0\cdot E_1,\quad
\mathsf S=N_0\cdot E_1,\quad
E_1=\mathsf CE_0+\mathsf SN_0,\quad
N_1=-\mathsf SE_0+\mathsf CN_0 .
\]
三频实独立给 \(\mathsf S\ne0\)，且 \(\mathsf C^2+\mathsf S^2=1\)。定义
\[
\tau=\frac{A_1}{A_0}
=\mathsf C+\mathsf S\frac{B_0}{A_0},
\qquad
\mathfrak r=\frac{k_1}{k_0}\in\mathbb R\setminus\{0\}.
\]
于是
\[
\frac{B_0}{A_0}=\frac{\tau-\mathsf C}{\mathsf S},\qquad
\frac{B_1}{A_0}=\frac{\mathsf C\tau-1}{\mathsf S}.
\tag{HA.11}
\]
写 \(\tau=\tau_R+i\tau_I\)、\(T=|\tau|^2\)。HA.5 给
\[
\boxed{
\tau_I\ne0,\qquad
\mathfrak h(W;p)
=\frac{\sqrt P\,|A_0|^2}{\mathsf S}\tau_I .}
\tag{HA.12}
\]
所以 τ 有限非零，T>0，没有零投影或无穷坐标分支隐藏在后面的除法中。\(\mathfrak r\) 已由同一发送种子及几何固定，不能按此行另调。

将 HA.10 的完整总和依次与 E1、E0 作双线性点积，分别除以非零量 \(ik_0A_0^2\)，得到
\[
\boxed{
\frac{(Z_{20}+Z_{21})\cdot E_1}{ik_0A_0^2}
=\mathfrak r\tau^2+b_0\tau+(1-b_0)\mathsf C+\mathsf S\gamma_0,}
\tag{HA.13}
\]
\[
\boxed{
\frac{(Z_{20}+Z_{21})\cdot E_0}{ik_0A_0^2}
=1+\mathfrak r\left[
b_1\tau+\bigl((1-b_1)\mathsf C-\mathsf S\gamma_1\bigr)\tau^2
\right].}
\tag{HA.14}
\]
E0、E1 在实及复横向平面均独立，故完整总行为零当且仅当这两个复式同时为零。第一式是实系数二次式；第二式包含 γ1 的完整发送虚相干。只核第一式不能推出本轮面积关系。

## 4. 完整零行的实虚条件及严格正面积恒等式

假设 HA.13–14 同时为零。因 γ0 实且 τ_I≠0，第一式的虚部给
\[
\boxed{\tau_R=-\frac{b_0}{2\mathfrak r}.}
\tag{HA.15}
\]
其完整实部随后等价于
\[
(1-b_0)\mathsf C+\mathsf S\gamma_0=\mathfrak rT .
\tag{HA.16}
\]
特别地，该实二次式的判别式为
\[
b_0^2-4\mathfrak r\bigl((1-b_0)\mathsf C+\mathsf S\gamma_0\bigr)
=-4\mathfrak r^2\tau_I^2<0.
\]
这是接收面积非零对应的严格分支，并非只凭二次式“可能有复根”作判断。

第二式除以 \(\mathfrak r\tau^2\ne0\)，完整等价于
\[
\mathsf S\gamma_1
=(1-b_1)\mathsf C+\frac{b_1}{\tau}
+\frac{1}{\mathfrak r\tau^2}.
\tag{HA.17}
\]
它的实部必须保留：
\[
\boxed{
\mathsf S\frac{\sqrt P\,\alpha_1}{\chi_1}\xi_1
=(1-b_1)\mathsf C
+\frac{b_1\tau_R}{T}
+\frac{\tau_R^2-\tau_I^2}{\mathfrak rT^2}.}
\tag{HA.18}
\]
虚部使用 HA.9、15 得
\[
\boxed{
\mathsf S\sqrt P(b_1-2)\theta_1
=-\tau_I\left(\frac{b_1}{T}
+\frac{2\tau_R}{\mathfrak rT^2}\right)
=-\tau_I\frac{b_1\mathfrak r^2T-b_0}{\mathfrak r^2T^2}.}
\tag{HA.19}
\]
在固定共享坐标及 HA.2 的域内，HA.15、16、18、19 四个实条件也反向恢复 HA.13–14；但只取其中的符号后不再充分。

由 τ_I≠0 和 HA.15，
\[
\mathfrak r^2T
=\frac{b_0^2}{4}+\mathfrak r^2\tau_I^2
>\frac{b_0^2}{4}.
\]
因 b0>2、b1>2，
\[
\boxed{
J:=b_1\mathfrak r^2T-b_0
>\frac{b_1b_0^2}{4}-b_0
=b_0\left(\frac{b_0b_1}{4}-1\right)>0.}
\tag{HA.20}
\]
于是 HA.19 中除 τ_I 和 \(\mathsf S\) 外的相关因子均有已证严格符号。结合两个有向面积式 HA.5、12，得到精确关系
\[
\boxed{
\mathfrak h(V_1;q_1)
=
\frac{\Delta_1|X_1|^2}
{P|A_0|^2(b_1-2)}
\frac{J}{\mathfrak r^2T^2}
\mathfrak h(W;p).}
\tag{HA.21}
\]
等号右端乘面积的系数严格为正。因此必要同号律为
\[
\boxed{\mathfrak h(U_1;p_1)\,\mathfrak h(U_2;p_2)>0.}
\tag{HA.22}
\]
本式来自两个完整点积共同施加的约束，不是单边符号，也不声称任意同号面积就能使该行归零。HA.16、18 等准确实部和 HA.21 的幅度关系仍需由同一组三种子同时满足。

## 5. 非零量、复缩放与未延拓的接收域

最长行所用除法的全部因子为 P、Q_j、Δ_j 的正幂、Λ_j、Ω_j、H_j、χ_j、\(\ell_j\)、k0、A0、\(\mathsf S\)、\(\mathfrak r\)、τ、T 及 b1−2。它们分别由非平行非正交、严格长度排序、发送活跃、接收面积非零和 HA.7 保证非零。没有除以 \(\mathsf C,\alpha_j,\xi_j,\gamma_0\)；它们若为零仍按原式核验。HA.15 还强制 τ_R≠0，所以纯虚 τ 不是被遗漏的额外解。

若 θ1=0、τ_I=0、\(\mathsf S=0\) 或接收长度不严格较大，已离开本次同号律的假设。尤其没有把 HA.20 的严格正性延拓到中间接收面对较长发送的边；那里没有由 P>Q 得到的两个 b_j>2 保证，且归一化中的 H、χ 是否为零也须另分支核验。本稿不以最长行结论替代中间完整行。

任意种子乘非零复标量时，面积乘其模方。接收 W 的非零复缩放使该最长总行乘同一个接收平方因子，保持这一行零性；发送各自仅改变单位模相位也保持这一行。同号律因此不依赖这些相位。HA.21 对接收缩放保持一致，因为接收面积与 |A0|² 同步缩放。若独立改变发送投影模方，一般不保持原零行，必须同步改变 \(\mathfrak r\) 并重新核 HA.13–14；不能把发送模方缩放误作完整行的无条件对称。不同邻边坐标来自同一向量，负模共轭也没有重选自由。

## 6. 与最低完整 C 方向比较：只得到新的必要门

这一节另外假设同一数据还满足最低完整 Z 零行，且最低 C 总行沿原 U0 复方向。使用原合同的两条最低 β 零几何和已接纳 TEI.18–24。此节统一记 \(P_i=|p_i|^2\)、\(c_{ij}=p_i\cdot p_j\)。写 U0=z0R0，其中 R0 是非零实横向向量；下标 min 的量全部在 p0 的接收平面定义，不能与上述最长行的 τ、\(\mathfrak r,\mathsf C\) 混同。

最低的两个发送单位投影方向为
\[
E_{0j}
=\frac{p_j-(c_{0j}/P_0)p_0}{\ell_{0j}},\quad
\ell_{0j}=\sqrt{(P_0P_j-c_{0j}^2)/P_0}>0,
\]
\[
t_{\min}
=\frac{R_0\cdot E_{02}}{R_0\cdot E_{01}}\in\mathbb R\setminus\{0\},
\quad
\mathsf C_{\min}=E_{01}\cdot E_{02}.
\]
最低的固定权重比 r_min 按 TEI.10 保留同一发送种子的投影模方，满足 sign r_min=sign(c01c02)，不能视为新的可调幅度。TEI.20 的完整方向面积条件给
\[
\operatorname{sgn}(\mathfrak h(U_1;p_1)\mathfrak h(U_2;p_2))
=-\operatorname{sgn}(r_{\min}t_{\min}).
\]
由 HA.22，必须有
\[
\boxed{
r_{\min}t_{\min}<0,\qquad
c_{01}c_{02}(R_0\cdot p_1)(R_0\cdot p_2)<0.}
\tag{HA.23}
\]
这是面积符号的必要条件；最低面积的准确幅度等式 TEI.19 仍须保留。

同一最低实方向式为
\[
\mathcal F_{\min}(t)
=r_{\min}\Gamma_2\mathsf C_{\min}t^3
-r_{\min}\mathcal Bt^2+\mathcal At-\Gamma_1\mathsf C_{\min},
\tag{HA.24}
\]
这里最低系数准确为
\[
\sigma_j=\frac{P_0-P_j}{P_0},\qquad
\rho_j=\frac{2(P_0-P_j)(P_0+P_j)}{P_0(5P_0+4P_j)},
\]
\[
\Gamma_j=2-\sigma_j-\rho_j,\quad
\delta=\rho_2-\rho_1,\quad
\mathcal A=\Gamma_1+\delta,\quad
\mathcal B=\Gamma_2-\delta .
\]
TEI.21–22 已证 \(\Gamma_1,\Gamma_2,\mathcal A,\mathcal B>0\)。它们和最长的 b_j 不同。设
\[
\varepsilon=\operatorname{sgn}r_{\min},\qquad
R=|r_{\min}|>0,\qquad t_{\min}=-\varepsilon s,\quad s>0.
\]
将这一必要半轴代入完整三次式，不除以 N 或 D，得到
\[
0=
-\mathsf C_{\min}(R\Gamma_2s^3+\Gamma_1)
-\varepsilon(R\mathcal Bs^2+\mathcal As).
\]
所以该半轴上的实方向根必须且仅须满足准确标量式
\[
\boxed{
-\varepsilon\mathsf C_{\min}
=\frac{R\mathcal Bs^2+\mathcal As}
{R\Gamma_2s^3+\Gamma_1}>0.}
\tag{HA.25}
\]
右端的分子、分母均严格正。得到仅依赖固定几何号的另一必要门
\[
\boxed{r_{\min}\mathsf C_{\min}<0.}
\tag{HA.26}
\]
由于
\[
\mathsf C_{\min}
=\frac{c_{12}-c_{01}c_{02}/P_0}{\ell_{01}\ell_{02}},
\]
HA.26 等价于
\[
\boxed{
c_{01}c_{02}\left(c_{12}-\frac{c_{01}c_{02}}{P_0}\right)<0.}
\tag{HA.27}
\]
因此若固定几何不满足此严格号，最长完整 Z 零行和最低完整 Z 零行加最低 C 原方向不能同时成立。特别地，最低投影正交 \(\mathsf C_{\min}=0\) 被这一联合要求排除。这是联合条件的局部排除，不是原几何域整体排除。

HA.25 没有证明每个符号合格几何都能取得这样的 s；同号门不能代替三次式的准确根。该式直接使用完整 F，故最低 D=N=0、重根和其它中间系数关系没有被除法删除。某个 rt>0 的最低根只对应与 HA.22 不相容的面积支，不能用它的存在或失败代表 rt<0 的全部根。

## 7. 结论边界

本轮闭合的是：最长完整两项 Z 零行的四个实条件 HA.15、16、18、19，正系数面积关系 HA.21 及同号必要律 HA.22；与最低完整方向条件同时施加时，新增 HA.23、26、27 的必要号，以及 HA.25 的剩余准确实方程。

面积同号或联合几何号本身不充分保证最长行归零，仍须保留完整四个实条件。未解决中间行、同一整数几何的共同存在、三完整行的同时相消、三个 C 的共同模板条件、任何实际种子实例或再生成。两非零面积同号也不等于同一协方差或同一极化方向。全部坐标继续属于同一三频及同一组三种子。

没有新的真实 NS 时间、SOURCE_BRIDGE 来源比、短窗余项或跨代误差结果，没有候选或旧失败证据修复。NO-CANDIDATE；ALL-ROW REALIZATION OPEN；NOT CLAY。
