# 两高行剩余完整分量的四实条件

2026-09-08，PRIVATE_CORE。根手工推导，待独立推导和非作者审查。本文直接以同一组种子及已经为零的两个高投影为假设，重新从完整 NC 映射推剩余条件；不把前一阶段尚待最终接纳的消元稿当作无条件已证定理。

## FR.1 同一数据与直接假设

固定原仅最短线性三边域：独立整数三频 p0,p1,p2，P0<P1<P2，全部非正交，最低两条 beta=0，三个种子为
\[
U_0=zR,\quad z\ne0,\quad R\in p_0^\perp\cap\mathbb R^3\setminus\{0\},
\]
\[
U_i=a_i\{E_{i0}+(s_i+i y_i)N_{i0}\},\qquad
 a_i\ne0,\quad s_i,y_i\in\mathbb R,\quad y_i\ne0,
\quad i=1,2.
\tag{FR.1}
\]
E_ik 是 pk 在 pi 横向平面的单位投影，N_ik=phat_i×E_ik，Deltaik=PiPk-cik²>0。R·E01、R·E02 非零。负模由同一组共轭确定。直接假设最低完整 Z 零行和最低完整 C 非零原方向条件均成立，不声称每份原数据都满足它们。

对 {i,j}={1,2}，设
\[
C_i=E_{i0}\cdot E_{ij},\quad S_i=N_{i0}\cdot E_{ij}\ne0,
\]
\[
t_i=\frac{U_i\cdot E_{ij}}{U_i\cdot E_{i0}}
=C_i+S_i(s_i+i y_i)=X_i+iY_i,
\quad Y_i=S_i y_i\ne0,\quad M_i=|t_i|^2>0.
\tag{FR.2}
\]
同一高种子的两个平面投影为 a_i 与 a_it_i。令
\[
\mu_i=\kappa_{i0}/\chi_{i0}>2,\quad
\eta_{ik}=2(\Delta_{ik}/P_i)^{3/2}|U_k\cdot E_{ki}|^2>0,
\]
\[
b_i=\frac{\eta_{ij}\chi_{ij}}{\eta_{i0}\chi_{i0}},\quad
v_{0i}=\frac{R\cdot N_{0i}}{R\cdot E_{0i}}\in\mathbb R,
\]
\[
B_i=(1-\mu_i)C_i-
\sqrt{P_i/P_0}\frac{\alpha_{i0}}{\chi_{i0}}v_{0i}S_i.
\tag{FR.3}
\]
chi_i0 非零由 Pi>P0 与已接纳 MAX 比值支付；chi_ij 暂不除。第二个直接假设是两个指定高投影为零，即由完整 NC 各自沿 E_ij 点乘得到
\[
b_it_i^2+\mu_it_i+B_i=0.\tag{FR.4}
\]
这只是一份直接点积假设，不先宣布完整高行已经为零。

由于 t_i 非实，FR.4 排除 b_i=0（否则是非零实一次式），因此 chi_ij≠0。其虚部和实部给
\[
X_i\ne0,\quad b_i=-\frac{\mu_i}{2X_i},\quad
B_i=b_iM_i,\quad M_i>X_i^2>0.
\tag{FR.5}
\]
这些是本证明内重新支付的除法依据。

## FR.2 另一发送的实际复比值及相干

接收 i 的另一高发送 U_j，必须从其原表示换到发送基 E_ji,N_ji。因为
\[
E_{ji}=C_jE_{j0}+S_jN_{j0},\quad
N_{ji}=-S_jE_{j0}+C_jN_{j0},
\]
它的实际发送复比值为
\[
\omega_{ji}=\frac{U_j\cdot N_{ji}}{U_j\cdot E_{ji}}
=\frac{-S_j+C_j(s_j+i y_j)}{C_j+S_j(s_j+i y_j)}
=\frac{C_jt_j-1}{S_jt_j}.
\tag{FR.6}
\]
因此
\[
\boxed{\operatorname{Re}\omega_{ji}
=\frac{C_j-X_j/M_j}{S_j},\qquad
\operatorname{Im}\omega_{ji}=\frac{y_j}{M_j}.}
\tag{FR.7}
\]
第二式不是 Y_j/M_j：它先用 Y_j=S_jy_j 抵消了换基中的 S_j。实际发送模方也为 |a_j|²M_j。这三个量全部属于同一个 U_j，不能分别作为自由相干或强度。

现在 chi_ij 已非零，可以定义实系数
\[
\rho_i=\kappa_{ij}/\chi_{ij},\quad
\gamma_i=\sqrt{P_i/P_j}\,\alpha_{ij}/\chi_{ij},\quad
\delta_i=\sqrt{P_i/P_j}\,\beta_{ij}/\chi_{ij},
\]
\[
G_i=(1-\rho_i)C_i+
\gamma_iS_i\frac{C_j-X_j/M_j}{S_j},\qquad
J_i=\delta_iS_i\frac{y_j}{M_j}.
\tag{FR.8}
\]
这些量均为实数，不预先给中间行套 rho_i>2。当前非正交互异长度使 kappa_ij≠0，故 rho_i 实际非零；本推导不对它再作除法。gamma_i、delta_i、G_i 不预设非零，若相应实际系数为零仍用原式。

## FR.3 另一完整点积及四实剩余式

完整 NC 的有向单位基形式是：接收复平方乘发送模方，法向包含接收 kappa 比值、负的发送实相干和正 i 倍的发送虚相干。沿 E_i0 取第二点积，使用 N_ij·E_i0=-S_i，精确得到
\[
\boxed{
\frac{(Z_{i0}+Z_{ij})\cdot E_{i0}}
{i\eta_{i0}a_i^2\chi_{i0}}
=1+b_i\rho_it_i+b_i(G_i-iJ_i)t_i^2.}
\tag{FR.9}
\]
接收在 ij 边的法向比是 (C_i t_i-1)/(S_i t_i)；代入后 kappa 项给正的 b_i rho_i t_i，余项给 G_i-iJ_i，故发送虚相干并未删掉。E_ij 与 E_i0 独立，FR.4 与 FR.9 同时为零才是完整该行的等价检测。

将 FR.9 除以 t_i²，写 t_i^{-1}=(X_i-iY_i)/M_i。其实部为
\[
\boxed{
\mathcal R_i=
\frac{2X_i^2-M_i}{M_i^2}
+\frac{b_i\rho_iX_i}{M_i}+b_iG_i=0.}
\tag{FR.10}
\]
虚部为 -2XiYi/Mi²-bi rho_i Yi/Mi-bi Ji=0。除以非零 -bi Yi，再用 FR.5，得
\[
\boxed{
\mathcal I_i=
\delta_i\frac{y_j/y_i}{M_j}
+\frac{\rho_i}{M_i}
-\frac{4X_i^2}{\mu_iM_i^2}=0.}
\tag{FR.11}
\]
于是，在 FR.1–5 的直接同数据假设下，完整两高行同时为零，当且仅当
\[
\boxed{\mathcal R_1=\mathcal I_1=
\mathcal R_2=\mathcal I_2=0.}\tag{FR.12}
\]
这四个式子的系数已经全部明写，不能把它们的名字误当作已经求零或已经存在共同实例。

## FR.4 共同面积正负没有额外调参自由

最低方向的已接纳面积式使用相同单位基给
\[
y_2=k y_1,\qquad
k=-\frac{\sqrt{P_1/P_2}}{w\tau^3}\ne0,
\]
其中 tau=(R·E02)/(R·E01)，w 是实际最低发送权重比。因此 FR.11 中 y2/y1=k、y1/y2=1/k，均固定。

若前置投影消元已经固定 y_i² 和共同最低幅度，那么 M_i、X_i、b_i、G_i 也固定。FR.10–11 在同时翻转 y1,y2 时完全不变；实际高种子会发生相应共轭比值变化，但其固定 a_i 不变、所有共享发送换基均依 FR.6 同步变化。故在这两个共同符号候选中，一支通过 FR.12 当且仅当另一支也通过，没有可逐行再调的四个面积符号。

此陈述不把两个有向面积改成正强度。相对号 k 必须保留；若任意单独翻转一边，最低方向及 FR.11 一般改变。前置消元是否可以由某组固定几何、R、a_i 实现，仍是另外的问题。

## FR.5 精确 beta 零排除与中间比值带的必要门

为保留可能为零的 beta，直接从 NC 的共同分母计算：
\[
\beta=-\frac{4cdK}{\Lambda\Omega},\quad
P\Omega-2(2P+Q)H=QK,
\quad K=4P^2-PQ-2Q^2+8c^2.
\]
结合 chi、kappa 定义，得到不除 chi 的恒等式 beta=2chi-kappa；在当前 chi_ij≠0 域，
\[
\delta_i=\sqrt{P_i/P_j}(2-\rho_i).
\tag{FR.13}
\]
若 beta_ij=0，则 rho_i=2、delta_i=0，FR.11 成为
\[
\mathcal I_i=
\frac{2\mu_iM_i-4X_i^2}{\mu_iM_i^2}>0,
\]
因为 mu_i>2、Mi>Xi²。故任何一条该高交互边的 beta 零，都不能通过完整高行。在原排序，最长侧已由 rho_21>2 自动 beta_21≠0；中间侧 beta_12=0 是新的明确禁用子面。它不同于已由第一点积排除的 chi_12=0 子面，不能混为一条几何式。

若完整两高行都为零，最长行有 rho_2>2、delta_2<0。FR.11 的后两项满足
\[
\frac{\rho_2}{M_2}-\frac{4X_2^2}{\mu_2M_2^2}
>\frac{\rho_2-4/\mu_2}{M_2}>0.
\]
因此 y1/y2>0，两高面积同号。这里给出直接从 FR.11 的证明，不依赖尚待审的另一面积稿。

中间行的 rho_1 不预先大于 2。如果
\(4/\mu_1\le\rho_1<2\)，delta_1>0，而 y2/y1>0，使 FR.11 第一项正；其后两项之和也严格正，因为 Mi>Xi²。因此同样不可能为零。rho_1=2 已被上一段排除。必要条件为
\[
\boxed{\rho_1<4/\mu_1\quad\text{或}\quad\rho_1>2.}
\tag{FR.14}
\]
这里 mu_1=kappa_10/chi_10>2，rho_1=kappa_12/chi_12，chi_12≠0 仍为前提。负的 rho_1 属于第一个允许域；本文未排除它，也未给允许域内共同可解性。这个区间排除是必要几何门，不是任何时间的 NS 奇性结论。

## FR.6 准确结论与尚未支付的工作

FR.12 在明确的同种子直接前提下，是两个完整高行的四实等价式。若另把前置共享面积/幅度消元作为最终已审条件接入，则可用它恢复原未知量，连同最低条件获得完整总 M0=0 且最低 C 非零原方向的条件代数接口。接入时必须核输入最终字节及其固定数据量词，不能提前宣布前一阶段所有后续已接纳。

本文没有证明任何实际固定几何、R、a_i 使前置条件及四式共同成立，也没有证明全部无解。其它两个 C 原方向和共同模板幅度还未检查；最低 C 非零与总 M0 零即使成立，也只有限空间首项，不等于真实第一代两步供给、原解再生成或奇性。

非零分母包括 S_i、t_i、a_i、eta_i0、chi_i0、chi_ij、b_i、Y_i、y_i、Mi 及 mu_i，均已由直接域或 FR.4–5 支付。C_i、s_i、alpha_ij、beta_ij、G_i 没有被用作分母，相应可能零支按原式保留；rho_i 的非零由当前 kappa_ij≠0 给出。固定正黏性环面的 Fourier–Leray 完整空间映射保留；本文没有新时间核估计或无限维误差预算。

根本连续任务已实际全文读已接纳 NC、MAX、最低接口及当前前置投影文本。本文的 FR.1–14 是本次手工推导，尚待独立推导、分开非作者审查及最终比较；没有借未读新稿补证。无科学程序、数组、数值求值、实际选参、扫描、图档或旧失败修复。PRIVATE_CORE；NO-CANDIDATE；NOT CLAY。
