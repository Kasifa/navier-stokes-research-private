# 一个线性发送下的较高完整接收行：必要实二次门

2026-09-08，PRIVATE_CORE。根手工推导，待非作者审查。独立于尚待最终审查的最低行消元；不使用其存在或方向结论。只用已接纳完整 NC 映射和任意 P>Q 的 kappa/chi>2 引理。

## HP.1 固定数据与单位方向

令 p,q,r 为独立整数三频，P=|p|²>|q|²=Q，R=|r|² 与 P 不同，p·q、p·r 均非零。q、r 之间是否非正交不为本行所需。接收 U⊥p 的有向极化面积非零；q 处发送 V=z Vreal，z≠0、Vreal 非零实横向，r 处发送 W 非零。所有边投影 U·q、U·r、V·p、W·p 非零。原仅最短线性三边合同的两个较高行均满足这一域，那里 W 还有非零面积。

对 s=q,r，记 Delta_s=P|s|²-(p·s)²>0，
\[
E_s=\frac{s-(p\cdot s)p/P}{\sqrt{\Delta_s/P}},\quad
N_s=\frac p{\sqrt P}\times E_s,
\]
\[
F_s=\frac{p-(p\cdot s)s/|s|^2}{\sqrt{\Delta_s/|s|^2}},\quad
\widetilde N_s=\frac s{|s|}\times F_s=-N_s.
\]
写发送 V=b_q(F_q+omega_q Ntilde_q)，W=b_r(F_r+omega_r Ntilde_r)，其中 b_q,b_r≠0，omega_q 为实，omega_r 可以为完整复数。没有丢掉 W 的相干项。

置 C=E_q·E_r、S=N_q·E_r，则 C²+S²=1、S≠0，E_r=C E_q+S N_q。令
\[
a=U\cdot E_q\ne0,\quad
\zeta=\frac{U\cdot E_r}{U\cdot E_q},\quad
\omega=\frac{U\cdot N_q}{U\cdot E_q},\qquad
\zeta=C+S\omega.
\tag{HP.1}
\]
U 的面积非零等价于 Im omega≠0，故 Im zeta≠0，特别 zeta≠0。这个复比值由同一 U 决定。

## HP.2 对完整另发送方向取点积

沿用已接纳单位基完整系数 chi_s,kappa_s,alpha_s,beta_s，并令
\[
\eta_s=2(\Delta_s/P)^{3/2}|b_s|^2>0,
\quad h_q=\sqrt{P/Q}\,\alpha_q\omega_q\in\mathbb R.
\]
完整线性发送项为
\[
Z(p;q)=i\eta_q a^2
\{\chi_qE_q+(\kappa_q\omega-h_q)N_q\}.
\tag{HP.2}
\]
因为 P>Q、p·q≠0，已付 MAX 比值给 chi_q≠0 和
\[
\mu=\kappa_q/\chi_q>2.
\tag{HP.3}
\]
另发送的完整 Z(p;r) 包含其所有实虚相干，但其法向恰沿 N_r，因此
\[
Z(p;r)\cdot E_r=i\eta_r\chi_r a^2\zeta^2.
\tag{HP.4}
\]
这里仅在这个准确点积中 N_r·E_r=0；没有删除完整行的法向要求，也没有把 W 线性化。即使 chi_r=0，HP.4 仍成立。

若完整向量 Z(p;q)+Z(p;r)=0，对 E_r 点乘并除以非零 i eta_q a² chi_q，得到
\[
\boxed{b\zeta^2+\mu\zeta+A=0,}
\quad
b=\frac{\eta_r\chi_r}{\eta_q\chi_q},\quad
A=(1-\mu)C-\frac{h_q}{\chi_q}S\in\mathbb R.
\tag{HP.5}
\]
eta_q、eta_r 是实际发送投影模方给定的正数，不是独立于共享种子的自由通道幅度。

## HP.3 非实接收比值支付的严格门

若 chi_r=0，则 b=0，HP.5 是 mu zeta+A=0；mu>2、A 实，与 Im zeta≠0 矛盾。因此完整零行必有 chi_r≠0。

设 zeta=x+iy，y≠0。HP.5 的虚部给
\[
2bx+\mu=0.
\]
故 x≠0，并且
\[
\boxed{x=-\frac\mu{2b},\qquad
|\zeta|^2=\frac A b,\qquad
bA>\frac{\mu^2}4>1.}
\tag{HP.6}
\]
第二式由实部 b(x²-y²)+mu x+A=0 代回得到；第三式来自 y²=A/b-mu²/(4b²)>0。等价地，该完整点积的实二次式判别式严格负：
\[
\mu^2-4bA<0.
\tag{HP.7}
\]
这些关系还给 sign x=-sign b、sign A=sign b；A=0、Re zeta=0、非负判别式以及另边 chi=0 都排除完整零行。C=0 或 h_q=0 可以出现，未被预先当分母；如两者同零则 A=0，本门即排除。

反过来，若 b≠0 且 bA>mu²/4，二次式确有两个非实共轭根；但这只判定这个点积可为零，不判定它们是给定 U 的实际比值，更不支付完整法向零行。因此 HP.6–7 在本数据任务中只作为必要门使用。

## HP.4 对剩余三边类型的准确用途

在原仅最短种子线性的合同中，令 p=p_i、q=p_0、r=p_k，i,k 为两个较高指标且 i≠k。每行都有 P_i>P_0，故 HP.3 对两行成立。若总 M0=0，两行分别必须通过 HP.5–7，且两个 b_i 来自同一 U0 与相互发送的 Ui、Uk，不能分别调节。

特别，中间接收来自最长发送的 chi_12 必须非零。由 NC 的完整公式，非正交、互异长度、正分母及其余非零因子给
\[
\chi_{12}=0\iff
H(P_1,P_2,c_{12})=4P_1^2-P_1P_2+P_2^2-4c_{12}^2=0.
\]
所以此几何零面无法满足该明确类型的中间完整零行。这只是一个准确排除子面，未排除全部整数几何或全部极化。

对最长接收的另边，P_2>P_1 已直接保证 chi_21≠0；仍须付负判别式和同一种子实比值的约束。最低行的条件即使以后证明可以满足，也不能代替这两行门。

未给实际整数实例，未证明两高行共同无解或完整三边可解。本文只有限空间首项的必要条件，没有新原解时间、NS 来源比、有限两步机制、跨代误差、单初值无限尺度、有限总时间、奇性或全局正则性结论。无科学程序、数组、数值求值、实际参数选择、扫描或旧失败证据修复。待非作者审查；NO-CANDIDATE；NOT CLAY。

## 已用来源

根在本连续研究此前实际全文读过并接纳 net-mixed-cancellation/INDEPENDENT.md 的 NC 完整相干映射（SHA 25111397d32eef2751a91b1ad1ab6a446794742874b97bf6b0b73b3964d11a58）和 three-edge-compatibility/INDEPENDENT.md 的单位基换算。three-edge-compatibility/MAX_RECEIVER_RATIO.md 由根手工证明，已获独立非作者审查并冻结；本轮只在其 P>Q 原范围使用。HP.1–7 为本次手工推导；未调用本目录尚在审查的新消元结果或未读科学稿件。
