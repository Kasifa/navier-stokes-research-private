# 最低零行与非零原方向输出的条件普遍可解性

2026-09-08，PRIVATE_CORE。独立有界补充，待分开的非作者审查及根比较。

**结果：对每个满足本合同的固定几何，以及事先给定的两个非零发送平面投影复系数，确实存在一个共同实最低接收方向和两个面积非零的发送复比值，使完整最低 Z 行为零，并使同一最低 C 行成为非零原方向输出。可以始终取到两发送有向面积符号相反的一支。因此这些最低行条件不能单独排除该类型。此结论只条件量化固定几何，不证明整数几何已经实现，也不解决两个较高接收行。**

本文未读本目录 PROOF.md、任何新主稿或新审查。只从本人已形成的 INDEPENDENT.md 继续手核。该局部输入仍按待最终审查的状态引用；若它后续修正，本补充须同步复核。没有实际频率、种子、幅度或时间实例；没有科学程序、数组、数值求值、扫描、Git、重置、外发或发布。

## 1. 实际来源及准确量词

路径相对于 research/reverse/。

| 来源及实际阅读范围 | SHA-256 |
|---|---|
| two-elliptic-compatibility/LOWEST_FEASIBILITY_CONTRACT.md，本轮先全文读取 | 7b08814a9fb5e06705d717c660cfa7efdf3e312e481c6fb296e226586c6bbf8a |
| two-elliptic-compatibility/INDEPENDENT.md，本连续任务前一轮全文自核，本轮实际重读第 100–296 行，包含 TEI.8–21 及 TEI.22 的引入 | 9a39799e39b9ec40e4ae61e86f3b0dda0dabc0885dcbea17febd91b868524da9 |
| two-elliptic-compatibility/CONTRACT.md，本连续任务前一轮实际全文重读，作为本合同直接沿用的几何域 | ee05b39370f178cac5aebcf3c3046478c848c74b0078ee26edafb3282029ad52 |
| net-mixed-cancellation/INDEPENDENT.md，此前已全文非作者核验，前一轮实际重读第 45–119 行的 NC.4–10；本补充沿用其完整系数和接收复二次、发送模方缩放 | 25111397d32eef2751a91b1ad1ab6a446794742874b97bf6b0b73b3964d11a58 |

未把来源内部再列出的文件自动记为本轮实读。

固定一个满足合同的三频几何。沿用 p 为最低频率、q1、q2 为两个较高频率，
\[
P=|p|^2<Q_1<Q_2,\quad
c_j=p\cdot q_j\ne0,\quad d_j=P-Q_j<0,\quad
\Delta_j=PQ_j-c_j^2>0.
\]
三频实独立、全部非正交，并满足两条直接假设
\[
8c_j^2=-4P^2+PQ_j+2Q_j^2,\qquad
Q_j/4<P<\frac{1+\sqrt{33}}8Q_j.
\tag{LF.1}
\]
结论不要求先证明此整数几何域非空。

合同事先给定的两个发送平面投影复系数在本稿记为 x1、x2，均非零。这样避免与 TEI 中的接收单位基坐标 A_j 混淆。它们是固定基
\[
f_j=p-\frac{c_j}{Q_j}q_j,\qquad n_j=p\times q_j
\]
中沿 f_j 的系数。待求种子仅写成
\[
V_j=x_j\bigl(f_j+(\xi_j+i\theta_j)n_j\bigr),
\qquad \xi_j\in\mathbb R,\quad\theta_j\in\mathbb R\setminus\{0\}.
\tag{LF.2}
\]
x_j 的模方及复相位全程保持给定值。若给定投影用单位基系数或点积表示，先作固定几何决定的非零实尺度转换；例如 V_j·p=Δ_jx_j/Q_j，故给定此点积同样唯一固定 x_j，不增加自由量。待求 U 是一个共同非零实向量，U⊥p；最低实际种子可以为 U0=z0U，z0 为任意非零复标量。下文先去掉 Z、C 中共同接收因子 z0²。

本稿证明的量词是：对上述每个固定几何和每组给定 x1、x2，存在 U、ξ1、ξ2、θ1、θ2，满足两条最低行条件。它不把发送复比值或发送面积也视为事先给定量。

## 2. 固定权重、共同方向与完整方程

沿用
\[
e_j=q_j-\frac{c_j}{P}p,\quad
\ell_j=\sqrt{\Delta_j/P},\quad
E_j=e_j/\ell_j,\quad N_j=n_j/(\sqrt P\,\ell_j),
\]
\[
\mathsf C=E_1\cdot E_2,\qquad
\mathsf S=N_1\cdot E_2,\qquad
\mathsf C^2+\mathsf S^2=1,\quad\mathsf S\ne0.
\]
特别是允许 𝖢=0；三频独立仅排除 𝖲=0。方向坐标为
\[
U=a\left(E_1+\frac{t-\mathsf C}{\mathsf S}N_1\right),
\qquad a\in\mathbb R\setminus\{0\}.
\tag{LF.3}
\]
由 E2=𝖢E1+𝖲N1，
\[
A_1=U\cdot E_1=a,\quad A_2=U\cdot E_2=at,\quad
B_1=U\cdot N_1=\frac{a(t-\mathsf C)}{\mathsf S},\quad
B_2=U\cdot N_2=\frac{a(\mathsf Ct-1)}{\mathsf S}.
\]
允许方向准确对应有限实 t≠0。t=0 会使第二个接收投影为零；无穷方向意味着第一个接收投影为零。LF.3 只是一条实射影直线的坐标表示，不是在两边分别选择接收向量，a 也不进入待解方向方程。

完整 β 零化简给
\[
L_j=\frac{2\Delta_j^3}{P^2Q_j}>0,\quad
\chi_j=\frac{4c_jd_j}{3Q_j(2P+Q_j)}\ne0,\quad
\alpha_j=\frac{2(5P+4Q_j)}{3(2P+Q_j)}>0.
\]
定义
\[
k_j=\frac{L_j|x_j|^2\chi_j}{\ell_j}\ne0,\qquad
r=k_2/k_1\ne0,\qquad \operatorname{sgn}r=\operatorname{sgn}(c_1c_2).
\tag{LF.4}
\]
r 已被几何与给定 x_j 固定，后文始终不把它当作新增可调幅度。

记
\[
\eta_j=\frac{\sqrt P\,\alpha_j}{\chi_j}\xi_j,\quad
\nu_j=\frac{2Q_j}{\sqrt P}\theta_j,\quad
\sigma_j=\frac{d_j}{P},\quad
\rho_j=\frac{2d_j(P+Q_j)}{P(5P+4Q_j)}.
\]
TEI.11–12 的全部正负根及双有序项给出
\[
Z_j=ik_j\left[A_j^2E_j+
(2A_jB_j+\eta_jA_j^2)N_j\right],
\]
\[
C_j=ik_j\left[\sigma_jA_j^2E_j+
(2A_jB_j+\rho_j\eta_jA_j^2+i\nu_jA_j^2)N_j\right].
\tag{LF.5}
\]
因此在任何有限 t≠0 上，完整最低零行唯一决定
\[
\eta_1=\frac{\mathsf C-2t-rt^2}{\mathsf S},\qquad
\eta_2=\frac{-\mathsf C+2/t+1/(rt^2)}{\mathsf S},
\]
\[
\xi_j=\frac{2c_jd_j}{\sqrt P\,Q_j(5P+4Q_j)}\eta_j.
\tag{LF.6}
\]
所有分母非零；η_j 或 ξ_j 可以为零，不构成退化损失。

置
\[
\Gamma_j=2-\sigma_j-\rho_j,\quad
\delta=\rho_2-\rho_1,\quad
\mathcal A=\Gamma_1+\delta,\quad
\mathcal B=\Gamma_2-\delta.
\]
在 LF.6 上，同一完整 C 的方向条件准确为
\[
\mathcal F(t)=
r\Gamma_2\mathsf Ct^3-r\mathcal Bt^2+\mathcal At-\Gamma_1\mathsf C=0,
\]
\[
Q_1\theta_1+rQ_2t^3\theta_2=0.
\tag{LF.7}
\]
这是完整复行列式的两个实条件；β=0 没有删去第二个面积条件。

后面的存在性用到 Γ1、Γ2、𝒜、𝓑 均严格正。为独立核清正性，令 ζ_j=Q_j/P，于是 1<ζ1<ζ2<4，并有
\[
\rho(\zeta)=\frac{2(1-\zeta^2)}{5+4\zeta}<0,\quad
\rho(\zeta)+2=\frac{2[\zeta(4-\zeta)+6]}{5+4\zeta}>0,
\]
\[
\Gamma(\zeta)=\frac{3(1+\zeta)(1+2\zeta)}{5+4\zeta}>0,\quad
\delta=-\frac{2(\zeta_2-\zeta_1)
[4\zeta_1\zeta_2+5(\zeta_1+\zeta_2)+4]}
{(5+4\zeta_1)(5+4\zeta_2)}<0.
\]
所以
\[
\mathcal A=1+\zeta_1+\rho_2-2\rho_1
>\zeta_1-1-2\rho_1>0,\qquad
\mathcal B=\Gamma_2-\delta>0.
\tag{LF.8}
\]

## 3. 对每个固定非零权重总有合法实根

先设 𝖢≠0。LF.7 为真正的实三次式，首项系数 rΓ2𝖢 非零，常数项 −Γ1𝖢 也非零。因而实根存在，且零不是根。更精确地，令 ε=sgn r∈{−1,1}，在 s≥0 上考察同一个多项式 𝓕(εs)。有
\[
\mathcal F(0)=-\Gamma_1\mathsf C,\qquad
\lim_{s\to+\infty}\frac{\mathcal F(\varepsilon s)}{s^3}
=|r|\Gamma_2\mathsf C.
\tag{LF.9}
\]
这两个非零符号相反。因此存在一个有限 s*>0 使 𝓕(εs*)=0。这里仅用实多项式连续性：由非零首项控制，可取某个有限右端点使符号改变；中间值定理给有限开区间中的根。没有以无穷投影作为根，也没有数值搜索。

记 t*=εs*，得到
\[
\boxed{\mathcal F(t_*)=0,\quad t_*\in\mathbb R\setminus\{0\},
\quad rt_*>0.}
\tag{LF.10}
\]
这对 r 的正负两种符号及 𝖢 的正负两种符号均成立。论证不要求根单重，也不要求另外两个根为实数，更不要求三次式判别式非零；所有重根和中间系数特殊关系均被覆盖。

若 𝖢=0，则完整实方程准确降为
\[
\mathcal F(t)=t(\mathcal A-r\mathcal Bt).
\]
其零投影根 t=0 被排除；由 LF.8，另一个根
\[
\boxed{t_*=\frac{\mathcal A}{r\mathcal B}}
\tag{LF.11}
\]
为有限非零实数，且 rt*=𝒜/𝓑>0。此时二次系数 −r𝓑 非零，没有再降为恒零或仅剩禁用零根的分支。

所以在全部合同域内，预先固定 r 以后仍总有一个合法根满足 rt*>0。没有为了获取该根修改发送投影模方。

## 4. 面积、共享种子与非零完整输出

对第 3 节得到的 t*，使用 LF.3 定义同一个接收方向，使用 LF.6 唯一确定 ξ1、ξ2。取任意符号变量 θ2∈R∖{0}，并定义
\[
\boxed{\theta_1=-\frac{rQ_2t_*^3}{Q_1}\theta_2.}
\tag{LF.12}
\]
这些是解析存在式，不是实际极化或幅度选参。所有乘除因子均非零，所以 θ1、θ2 都非零，且精确满足 LF.7 的面积方程。由于 rt*>0，
\[
\theta_1\theta_2
=-\frac{Q_2}{Q_1}(rt_*)t_*^2\theta_2^2<0.
\]
按同一个有向面积约定，
\[
\mathfrak h_j=\frac1{2i}q_j\cdot(\overline V_j\times V_j)
=-\Delta_j|x_j|^2\theta_j\ne0,
\quad
\boxed{\mathfrak h_1\mathfrak h_2<0.}
\tag{LF.13}
\]
因此不是用零面积或强度平均来满足复方向，发送仍为两个面积非零的确定性种子。若另有预先给定的面积符号或面积数值，必须重新核 LF.7；本合同没有这些附加约束。

LF.2 此时定义了各一个完整 V_j。它们在两高种子相邻边的坐标，必须从这两个已定向量换基得到，不能在那里重新指定投影或相干比值。最低 U 也仅是 LF.3 的同一向量。

所有三条边仍活跃。最低两条边一方面有 U·q_j=ℓ_jA_j≠0，另一方面有 V_j·p=Δ_jx_j/Q_j≠0。对两个较高种子之间的边，面积非零说明每个 V_j 的实、虚部为 q_j⊥ 中的两个实独立向量；若 V_j 又与另一非平行实频率正交，其实、虚部都会落在两个实横向平面的交线上，矛盾。因此它们与另一较高频率的交叉点积也非零。这只验证合同活跃域，没有验证两个较高接收的行方程。

由 LF.6，完整 Z1+Z2=0。由 LF.7、12 和完整行列式等价，C1+C2∈C U。还须单独核其非零性：LF.5 给
\[
\operatorname{Im}\frac{C_1+C_2}{i}
=k_1\nu_1A_1^2N_1+k_2\nu_2A_2^2N_2.
\tag{LF.14}
\]
N1、N2 实独立，而两个系数均非零，故该实向量不为零，从而 C1+C2≠0。此证明没有把单边非零直接当成总行非零，而使用了保留面积项的独立法向。

于是存在 λ∈C∖{0} 使 C1+C2=λU。恢复最低接收相位后，
\[
Z_{01}+Z_{02}=z_0^2(Z_1+Z_2)=0,\qquad
C_{01}+C_{02}=z_0^2\lambda U=z_0\lambda U_0\ne0.
\tag{LF.15}
\]
负频率按同一组种子的复共轭固定；不存在按边另选负模的自由度。

## 5. 全部分支及这项存在性没有支付的条件

本证明没有把旧消元中的零分母分支删除。若写
\[
N(t)=\mathcal At-\Gamma_1\mathsf C,\qquad
D(t)=t^2(\Gamma_2\mathsf Ct-\mathcal B),
\quad \mathcal F(t)=N(t)+rD(t),
\tag{LF.16}
\]
则固定 r 的完整分支仍是：

- D≠0：根满足 r=−N/D；r 保持 LF.4 的给定值。N=0、D≠0 不会给允许根，因为那将要求 r=0。
- D=0、N≠0：不是根。
- D=N=0：是任意当前非零 r 的实方向根，但仍必须按 LF.12 或完整面积关系保留面积条件。

后一共同零条件仍精确为
\[
\mathsf C\ne0,\quad
t=\frac{\mathcal B}{\Gamma_2\mathsf C},\quad
\mathsf C^2=\frac{\mathcal A\mathcal B}{\Gamma_1\Gamma_2}.
\tag{LF.17}
\]
若这样的根落在 rt>0 半轴，它可直接用作第 3 节的根；若落在另一半轴，LF.9 仍另给一个 rt>0 的根。无须排除此退化几何，也无须证明它已有整数实现。对于任意其它合法实根，面积条件仍可由 LF.12 满足；其面积乘积符号一般为 −sgn(rt)，故 rt<0 的根若存在，对应两面积同号。本文只保证至少有一条 rt>0、两面积反号的支路，不声称穷尽或排除其它实根。

𝖢=0 的降次、r 正负、零或无穷投影、η_j 与 ξ_j 可为零、三次重根及 D=N=0 分支均已明确保留。合同中 c_j、d_j、x_j、α_j、χ_j、𝖲 非零且 𝒜、𝓑 正，因而它们为零的情况属于合同外，不能用作合法解或额外障碍。

这项条件普遍可解性说明：最低完整 Z 零行与最低完整 C 原方向，在允许调整共同实接收方向和两个发送复比值时，不能单独排除本合同的两面积非零类型。它并不说任意事先给定完整发送种子或任意事先给定接收方向都可行。

两个较高接收的完整 M0 行、其它两个 C 方向、共同模板幅度、同一整数几何的存在以及整组三行的相容性仍未解决。构造出的同一组三种子若用于后续行，必须原样使用，不能把本存在族的不同成员拼成同一原解的不同代。没有新增真实 NS 时间、SOURCE_BRIDGE 余项、再生成、有限两步候选或无限尺度结论，也不追认旧失败证据。

LOWEST ROW CONDITIONALLY FEASIBLE FOR EVERY FIXED ADMISSIBLE GEOMETRY AND FIXED NONZERO SENDER PROJECTIONS；HIGHER ROWS OPEN；NO-CANDIDATE；NOT CLAY。
