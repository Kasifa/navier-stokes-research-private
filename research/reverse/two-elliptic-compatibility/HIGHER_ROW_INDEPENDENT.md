# 较高完整行的实二次投影门与两行共享权重

2026-09-08，PRIVATE_CORE。独立有界推导，待非作者审查及根实际比较。

**结果：面积非零的接收面对一个较短线性发送及另一个完整复发送时，沿后一个发送的频率投影，得到一条准确实二次必要式。其二次系数为零时该完整行不能为零；否则接收非实比值须具有非零实部，并满足严格负判别式和明确权重符号。对原三边数据，两高行权重还须分别等于一个共享数据系数乘另一行接收比值的模方。本文不给完整行充分性，也不预判两高行联合无解。**

本稿先全文读取已锁定 HIGHER_ROW_CONTRACT.md，未读 HIGHER_ROW_PROJECTION.md 或其审查，也未读本项目新主稿或新审查。没有以在审最低行补充作为输入。全部为手工符号，没有科学程序、数组、数值求值、实际频率/种子/幅度/时间选择、扫描、Git、重置、外发或发布。

## 1. 实际来源与一般接收域

路径相对于 research/reverse/。

| 实际来源与阅读范围 | SHA-256 |
|---|---|
| two-elliptic-compatibility/HIGHER_ROW_CONTRACT.md，本轮先全文读取 | 5ee395fc46c92b9161bafec1fdf9e690456526e9038b7c1efed540ffff56b1ad |
| net-mixed-cancellation/INDEPENDENT.md，此前全文非作者核验，本轮重读第 45–119 行 NC.4–10 完整映射与复缩放 | 25111397d32eef2751a91b1ad1ab6a446794742874b97bf6b0b73b3964d11a58 |
| three-edge-compatibility/MAX_RECEIVER_RATIO.md，本轮全文读取并手核其比值恒等式 | ff52531d6e1b5563c99504aba8e6b6e4e5afce77b76e7e286e74d397c3d610c5 |
| two-elliptic-compatibility/CONTRACT.md，本连续任务此前全文实读，仅用于第 6 节原三边假设和符号对应 | ee05b39370f178cac5aebcf3c3046478c848c74b0078ee26edafb3282029ad52 |

来源文内提到的其它新旧稿件没有自动算作本轮实读。MAX 源文保留形成时的审查状态文字；本稿直接核用它给出的显式恒等式，不从该状态文字推断本项结论。

固定实独立频率 p、q、r，接收频率为 p，线性发送频率为 q，另一个面积非零的发送频率为 r。设
\[
P=|p|^2>Q=|q|^2>0.
\]
两条所需接收边均非正交、非平行且活跃；不另假设 P 与 |r|² 的大小或不等。接收 U⊥p 的极化面积非零。两个发送分别为 V⊥q、W⊥r，其中 V 线性、W 面积非零；负模按同一组三种子取共轭。

对发送频率 s∈{q,r}，定义
\[
Q_s=|s|^2,\quad c_s=p\cdot s\ne0,\quad
d_s=P-Q_s,\quad \Delta_s=PQ_s-c_s^2>0,
\]
\[
\Lambda_s=(P+Q_s)^2-4c_s^2>0,\quad
\Omega_s=(4P+Q_s)^2-16c_s^2>0,
\]
\[
H_s=4P^2-PQ_s+Q_s^2-4c_s^2,\quad
L_s=\frac{2\Delta_s^3}{P^2Q_s}>0,
\]
\[
\chi_s=\frac{4c_sd_s(2P+Q_s)H_s}{Q_s\Lambda_s\Omega_s},
\qquad
\kappa_s=\frac{4c_sd_sP}{Q_s\Lambda_s}.
\tag{HI.1}
\]
α_s、β_s 为 NC.6 的实系数，后文不需要将它们除掉。

## 2. 同一接收比值与两个完整发送

取实基
\[
e_s=s-\frac{c_s}{P}p,\quad
f_s=p-\frac{c_s}{Q_s}s,\quad n_s=p\times s,
\]
\[
\ell_s=\sqrt{\Delta_s/P},\qquad
E_s=e_s/\ell_s,\qquad N_s=n_s/(\sqrt P\,\ell_s).
\]
令
\[
\mathsf C=E_q\cdot E_r,\quad
\mathsf S=N_q\cdot E_r,\quad
\mathsf C^2+\mathsf S^2=1,\quad\mathsf S\ne0,
\]
于是 E_r=𝖢E_q+𝖲N_q、N_r=−𝖲E_q+𝖢N_q。三频独立排除 𝖲=0，但允许 𝖢=0。

对同一复接收 U，置
\[
a=U\cdot E_q,\qquad t=\frac{U\cdot E_r}{U\cdot E_q}.
\tag{HI.2}
\]
面积非零保证 a≠0：若 a=0，则 U 只沿实方向 N_q，面积为零。并且
\[
U\cdot N_q=\frac{a(t-\mathsf C)}{\mathsf S},\quad
U\cdot E_r=at,\quad
U\cdot N_r=\frac{a(\mathsf Ct-1)}{\mathsf S}.
\]
采用同一有向面积
\[
\mathfrak h_U=\frac1{2i}p\cdot(\overline U\times U),
\]
由 E_q×N_q=p/√P 精确得到
\[
\boxed{\mathfrak h_U=
\frac{\sqrt P\,|a|^2}{\mathsf S}\operatorname{Im}t\ne0.}
\tag{HI.3}
\]
因此 t 为有限非实数，特别是 t≠0。这里没有把两个邻边上的接收比例独立化。

线性发送可唯一写为
\[
V=x_q(f_q+\rho n_q),\qquad
x_q\in\mathbb C\setminus\{0\},\quad \rho\in\mathbb R.
\]
另一发送保留完整比值
\[
W=x_r\bigl(f_r+(\xi+i\theta)n_r\bigr),\qquad
x_r\in\mathbb C\setminus\{0\},\quad
\xi\in\mathbb R,\quad\theta\in\mathbb R\setminus\{0\}.
\tag{HI.4}
\]
x_q、x_r 为实际发送投影复系数，均不新选；|x_s|² 也不新调。ρ 可以为零。对 W 有 Re(x_r bar y_r)=|x_r|²ξ、Im(x_r bar y_r)=−|x_r|²θ，发送面积为 −Δ_r|x_r|²θ≠0。

定义正权重
\[
\mu_s=\frac{L_s|x_s|^2}{\ell_s}>0
\]
和接收坐标 A_s=U·E_s、B_s=U·N_s。完整 NC.7–8 转成单位基为
\[
Z(p;q)=i\mu_q\left[
\chi_qA_q^2E_q+
\{\kappa_qA_qB_q+\sqrt P\,\alpha_q\rho A_q^2\}N_q\right],
\]
\[
Z(p;r)=i\mu_r\left[
\chi_rA_r^2E_r+
\{\kappa_rA_rB_r+
\sqrt P(\alpha_r\xi-i\beta_r\theta)A_r^2\}N_r\right].
\tag{HI.5}
\]
这是对接收复二次、对发送实际协方差完整的映射。第二式在 χ_r=0 时仍合法；尚未除以 χ_r。

## 3. 较短线性边的严格比值与投影实二次式

因为 P>Q，在线性发送边有
\[
H_q=(P-Q)(4P-Q)+4\Delta_q>0.
\]
所以 χ_q、κ_q 均非零、同号。记
\[
b=\frac{\kappa_q}{\chi_q}
=\frac{P\Omega_q}{(2P+Q)H_q}.
\]
直接重展 MAX 比值恒等式：
\[
P\Omega_q-2(2P+Q)H_q
=QK,\qquad K=4P^2-PQ-2Q^2+8c_q^2
=Q^2+7Q(P-Q)+4(P-Q)^2+8c_q^2>0.
\]
故
\[
\boxed{b>2.}
\tag{HI.6}
\]
这不使用原合同最低 β 零几何，c_q 的正负也不影响该比值。

定义实际有符号平面权重、实发送方向系数及几何实常数
\[
k_q=\mu_q\chi_q\ne0,\qquad
k_r=\mu_r\chi_r\in\mathbb R,\qquad
\lambda=k_r/k_q\in\mathbb R,
\]
\[
\eta=\frac{\sqrt P\,\alpha_q\rho}{\chi_q}\in\mathbb R,\qquad
\tau=(1-b)\mathsf C+\eta\mathsf S\in\mathbb R.
\tag{HI.7}
\]
λ 可以为零或任一符号；它含两个实际发送投影模方，不能替换为独立正幅度。

沿 E_r 投影 HI.5。第一条边给
\[
\frac{Z(p;q)\cdot E_r}{ik_qa^2}
=\mathsf C+b(t-\mathsf C)+\eta\mathsf S
=bt+\tau.
\]
第二条边的全部法向项精确消失，因为 N_r·E_r=0，因而
\[
\frac{Z(p;r)\cdot E_r}{ik_qa^2}=\lambda t^2.
\]
得到准确等价
\[
\boxed{
(Z(p;q)+Z(p;r))\cdot E_r=0
\iff \lambda t^2+bt+\tau=0.}
\tag{HI.8}
\]
沿实际频率 r 作点积只多出非零实因子 ℓ_r，因为 Z 总在 p⊥ 内。β_r、ξ、θ 在这个特定投影中未出现，是实几何正交的结果；它们仍在完整映射的另一分量中。这里没有把 W 改成线性发送或删去它的实际协方差。

## 4. 零系数、非实比值与全部判别式分支

完整高行若为零，必须通过 HI.8，并且 t 满足 HI.3。下面是此投影门的精确分类。

若 λ=0，则 b>2 使 HI.8 只允许 t=−τ/b∈R，与接收面积非零矛盾。因此
\[
\boxed{\chi_r=0\ \Longrightarrow\ Z(p;q)+Z(p;r)\ne0.}
\tag{HI.9}
\]
该结论在本文域内无需除以 χ_r。按 HI.1，c_r≠0、分母正，χ_r=0 等价于 d_rH_r=0；特别包含另一发送等长 |r|²=P，以及不等长但 H_r=0。若另有 P>|r|²，则同样的正性保证 χ_r≠0。c_r=0 属于当前合同外，而非未处理的合法零边。

以下设 λ≠0，写 t=X+iY、Y≠0。HI.8 的虚部与实部分别给
\[
2\lambda X+b=0,\qquad
Y^2=\frac{4\lambda\tau-b^2}{4\lambda^2}.
\]
所以
\[
\boxed{
\lambda\tau>\frac{b^2}{4},\qquad
\operatorname{Re}t=-\frac b{2\lambda}\ne0,\qquad
(\operatorname{Im}t)^2=\frac{4\lambda\tau-b^2}{4\lambda^2}.}
\tag{HI.10}
\]
这些等价于给定实际 t 非实且满足此一个投影方程。相应两个形式根为
\[
t=-\frac b{2\lambda}
\ \pm\ i\,\frac{\sqrt{4\lambda\tau-b^2}}{2|\lambda|}.
\tag{HI.11}
\]
当接收 U 已固定时，必须检验它的实际 t 是否等于其中一根；不得在同一数据中另选 U 来替它过门。

记实判别式 𝒟=b²−4λτ，则：

- 𝒟<0：该二次式恰有两个共轭非实根，但还须匹配实际 t 及完整另一分量。
- 𝒟=0：只有重实根，面积非零接收不通过。
- 𝒟>0：两个实根，面积非零接收也不通过。

这里 b≠0，故即使 λ=0 也不出现恒零多项式。τ=0 或 λτ≤0 时均不能通过；τ、η、ρ、α_q、𝖢 的可能零值无须被约去。𝖢=0 时 τ=η𝖲，分类仍原样有效；若此时 η=0，也就不能通过。t 的实部为零同样不能通过，因为 HI.8 的虚部直接为 bY≠0。

通过投影还强制
\[
\boxed{
|t|^2=\tau/\lambda>0,\qquad
\operatorname{sgn}\tau=\operatorname{sgn}\lambda,\qquad
\operatorname{sgn}(\operatorname{Re}t)=-\operatorname{sgn}\lambda.}
\tag{HI.12}
\]
实际权重符号准确为 sgn λ=sgn(χ_r/χ_q)。正负 λ 都已保留，没有把发送模方为正误当成完整系数也为正。

## 5. 尚未通过的另一完整分量

为明确必要而非充分，在未除以 χ_r 的形式下，另一点积准确为
\[
\begin{aligned}
\frac{(Z(p;q)+Z(p;r))\cdot N_r}{ik_qa^2}
={}&-\mathsf S+
\mathsf C\left[\frac{b(t-\mathsf C)}{\mathsf S}+\eta\right]\\
&+\frac{\mu_r}{k_q}
\left[
\frac{\kappa_r t(\mathsf Ct-1)}{\mathsf S}
+\sqrt P(\alpha_r\xi-i\beta_r\theta)t^2
\right].
\end{aligned}
\tag{HI.13}
\]
即使 HI.8–12 全部成立，HI.13 仍必须为零。另一发送的完整复相干、它在实际共享数据中的 ξ、θ，以及实际接收 t，都保留在这里。E_r、N_r 构成 p⊥ 的实基，故同时满足 HI.8 与 HI.13 才是这一完整行的零条件；本文没有解出 HI.13。

## 6. 原三边数据中的两高行：权重并非独立

现在只作原合同的符号对应。固定同一 p0、p1、p2，平方长度 P0<P1<P2；同一 U0 线性，U1、U2 面积非零，全部所需边非正交活跃。对接收 i∈{1,2} 取线性发送 q=p0、另一发送 r=pj，其中 {i,j}={1,2}。因此每条线性发送边都满足 Pi>P0，HI.6 的 b_i>2 同时适用。

以下所有频率和种子保持同一数据，不调用最低行是否可解。记
\[
\Delta_{ij}=P_iP_j-(p_i\cdot p_j)^2,\qquad
\ell_{ij}=\sqrt{\Delta_{ij}/P_i},
\]
χ_ij 为接收 i、发送 j 的 HI.1 系数。实际发送 f 坐标由 NC.5 精确确定：
\[
x_{ij}=\frac{P_j}{\Delta_{ij}}(U_j\cdot p_i),\qquad
\mu_{ij}\chi_{ij}
=\frac{2P_j\sqrt{\Delta_{ij}}}{P_i^{3/2}}
\chi_{ij}|U_j\cdot p_i|^2.
\tag{HI.14}
\]
于是两行各自的实际权重为
\[
\boxed{
\lambda_i=
\frac{P_j\sqrt{\Delta_{ij}}\chi_{ij}}
{P_0\sqrt{\Delta_{i0}}\chi_{i0}}\,
\frac{|U_j\cdot p_i|^2}{|U_0\cdot p_i|^2}.}
\tag{HI.15}
\]
接收比值为
\[
\boxed{
t_i=\sqrt{\frac{\Delta_{i0}}{\Delta_{ij}}}\,
\frac{U_i\cdot p_j}{U_i\cdot p_0}\notin\mathbb R.}
\tag{HI.16}
\]
这里分母均非零。线性发送实比值也由同一 U0 固定：
\[
\rho_i=
\frac{U_0\cdot(p_i\times p_0)}
{P_0(U_0\cdot p_i)}\in\mathbb R.
\tag{HI.17}
\]
若 U0=z0R 且 R 为实向量，z0 在此比值中严格消去。因此两行的 η_i、τ_i 分别由这个相同 R 和各自实基得到，不能独立指定。

为了显式展示交叉依赖，定义只使用当前同一数据的实系数
\[
\mathcal K_i=
\frac{P_j\sqrt{\Delta_{ij}}\chi_{ij}}
{P_0\sqrt{\Delta_{i0}}\chi_{i0}}\,
\frac{\Delta_{ij}}{\Delta_{j0}}\,
\frac{|U_j\cdot p_0|^2}{|U_0\cdot p_i|^2}.
\tag{HI.18}
\]
由 HI.16 在另一行的模方关系，得到恒等式
\[
\boxed{\lambda_1=\mathcal K_1|t_2|^2,\qquad
\lambda_2=\mathcal K_2|t_1|^2.}
\tag{HI.19}
\]
这不是增加两个独立幅度变量。K_i 中的投影模方来自已定 U0、Uj；K_i 的符号由 χ_ij/χ_i0 决定。若另行对种子作自由缩放，这些量必须按同一实际向量同时更新，不能仅修改 λ_i。

若两个高行都通过各自的投影门，则 λ_i≠0，且每行满足
\[
\lambda_i t_i^2+b_it_i+\tau_i=0,\quad
b_i^2-4\lambda_i\tau_i<0,\quad
|t_i|^2=\tau_i/\lambda_i.
\]
结合 HI.19 得到进一步必要恒等式
\[
\boxed{\lambda_1\lambda_2=
\mathcal K_1\tau_2=\mathcal K_2\tau_1.}
\tag{HI.20}
\]
它仍须与两个实际复 t_i、两条负判别式和两个 HI.13 同时成立；单独满足 HI.20 并不充分。

在本原排序中，χ_10、χ_20、χ_21 都非零；因为它们的接收严格较长。另边 χ_12 则不可预设非零：由于 P1<P2 且 c12≠0，
\[
\boxed{\chi_{12}=0\iff H_{12}=0
\quad\Longrightarrow\quad Z_{10}+Z_{12}\ne0.}
\tag{HI.21}
\]
这是一个明确条件障碍，但本文未证明原最低 β 零几何必然使 H12=0，也未证明它必不为零。若 H12≠0，仍应按实际符号与判别式检验，不据此预判联合矛盾。

## 7. 交付范围

HI.8 是完整高行沿后一个发送投影的精确实二次式；HI.9–12 完整保留另边平面系数为零、降次、非实接收比值、零实部、重根及判别式和权重符号。HI.13 写明尚未解决的另一完整分量。HI.15–20 在原三边数据中给出两高行的实际共享权重依赖，超出独立变量计数。

本文没有用最低行的在审可解性当作已通过输入，也没有为两高行另选线性 U0、发送模方或复相干。原整数几何共同实现性、两高行完整相容、整组三行、原 C 方向和共同模板幅度仍未解决。没有新增真实 NS 时间、余项、来源比例、再生成或候选接纳；旧失败证据没有得到修复或追认。

COMPLETE HIGHER-ROW PROJECTION GATES AND SHARED WEIGHT NECESSITIES；FULL HIGHER ROWS OPEN；NO-CANDIDATE；NOT CLAY。
