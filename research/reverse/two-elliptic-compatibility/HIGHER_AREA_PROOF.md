# 最长完整零行迫使两个非零面积同号

2026-09-08，PRIVATE_CORE。根手工推导，待独立推导与非作者审查。本文把两个独立点积都保留；结论为完整零行的必要面积门，不是零行充分性。

## HA.1 明确域与完整系数

固定独立整数三频 p,q,r，P=|p|²>Q=|q|²、P>R=|r|²，p·q、p·r 非零。U⊥p 为面积非零接收；V⊥q 为非零线性极化发送；W⊥r 的面积非零。各所需投影非零。以 q、r 在 p 横向平面的单位投影 E_q,E_r 及正定向 N_s=phat×E_s 表示，E_r=C E_q+S N_q、N_r=-S E_q+C N_q，S≠0。

发送使用 F_s（p 在 s 横向平面的单位投影）及 Ntilde_s=shat×F_s=-N_s。写
\[
V=b_q(F_q+vNtilde_q),\quad v\in\mathbb R,
\qquad W=b_r(F_r+(s+i t)Ntilde_r),\quad t\in\mathbb R\setminus\{0\}.
\]
b_q,b_r 非零。令 a=U·E_q≠0，omega=U·N_q/a，zeta=U·E_r/a=C+S omega=x+iy。面积非零保证 y≠0。

沿用完整 NC 的单位基 chi,kappa,alpha,beta，eta_s=2(Delta_s/P)^(3/2)|b_s|²>0。对于当前 P>Q、P>R，两个 chi 非零，
\[
\mu=\kappa_q/\chi_q>2,\qquad
\rho=\kappa_r/\chi_r>2.
\tag{HA.1}
\]
还需一个完整系数恒等式。对任意非正交互异长度边，置 K=4P²-PQ-2Q²+8c²。已付系数给
\[
\beta=-\frac{4cdK}{\Lambda\Omega},\quad
\chi=\frac{4cd(2P+Q)H}{Q\Lambda\Omega},\quad
\kappa=\frac{4cdP}{Q\Lambda},
\]
而直接多项式展开有 P Omega-2(2P+Q)H=QK。因此
\[
\boxed{\beta=2\chi-\kappa,\qquad
\beta/\chi=2-\kappa/\chi\quad(\chi\ne0).}
\tag{HA.2}
\]
前一式不除 chi，在 chi=0 时仍成立；本证明最长行使用后一式时 chi_r 已非零。

## HA.2 两个完整点积

定义实数
\[
b=\frac{\eta_r\chi_r}{\eta_q\chi_q}\ne0,\quad
h=\sqrt{P/Q}\,\alpha_q v/\chi_q,\quad
A=(1-\mu)C-hS,
\]
\[
g=\sqrt{P/R}\,\alpha_r s/\chi_r,\quad
j=\sqrt{P/R}\,\beta_r t/\chi_r,
\quad B=(1-\rho)C+gS,\quad J=jS.
\tag{HA.3}
\]
完整 Z(p;q)+Z(p;r)=0 沿 E_r 和 E_q 的两个点积恰为
\[
\boxed{b\zeta^2+\mu\zeta+A=0,}
\tag{HA.4}
\]
\[
\boxed{1+b\rho\zeta+b(B-iJ)\zeta^2=0.}
\tag{HA.5}
\]
这里共同除数是 i eta_q a² chi_q。为核后一式，接收在 r 基的法向比为 (C zeta-1)/(S zeta)，发送 W 的完整法向系数为
\[
\kappa_r\frac{C\zeta-1}{S\zeta}
-\sqrt{P/R}\alpha_rs+i\sqrt{P/R}\beta_rt.
\]
点乘 E_q 时 N_r·E_q=-S；连同 chi_r C 平面项，正好得到 HA.5。没有删除其中虚相干，也没有将该点积换成模长或自由相位条件。E_q,E_r 独立，若对给定全部系数同时满足 HA.4–5，它们确实是该完整行的等价检测；下文只推必要后果。

## HA.3 非实根和另一点积的虚部

由 HA.4 的实虚部，
\[
x=-\frac\mu{2b}\ne0,\quad
D=|\zeta|^2=\frac A b>0,\quad
bA>\frac{\mu^2}4>1.
\tag{HA.6}
\]
因此 A、b、D 均非零。将 HA.5 除以 zeta²，对虚部计算
\[
-\frac{2xy}{D^2}-\frac{b\rho y}{D}-bJ=0.
\]
代入 HA.6 后得到准确恒等式
\[
\boxed{\frac Jy=\frac{\mu-b\rho A}{A^2}.}
\tag{HA.7}
\]
因为 rho>2、mu>2 且 bA>mu²/4，
\[
\mu-b\rho A<\mu-\rho\mu^2/4
=\mu(1-\rho\mu/4)<0.
\tag{HA.8}
\]
所以 J/y<0，尤其 J≠0。

另一方面 y=S Im omega，HA.2–3 给
\[
\frac Jy
=\sqrt{P/R}(2-\rho)\frac{t}{\operatorname{Im}\omega}.
\tag{HA.9}
\]
前面的正平方根及 2-rho<0 与 HA.8 合并，强迫 t/Im omega>0。

使用固定单位有向面积
\[
\mathfrak h_U=i\widehat p\cdot(U\times\bar U)
=2|a|^2\operatorname{Im}\omega,
\qquad
\mathfrak h_W=i\widehat r\cdot(W\times\bar W)=2|b_r|^2t,
\]
得到
\[
\boxed{\mathfrak h_U\mathfrak h_W>0.}
\tag{HA.10}
\]
向量整体非零复相位和不同邻边正定向实基不会改变这个符号；S 的符号在 J/y 中已消去。若改用旧的非单位面积规范，两个额外比例均为正，符号结论不变。未使用 U·U≠0，故复各向同性接收没有漏掉。

## HA.4 最低原方向条件留下的必要几何号

回到原仅最短种子线性的三边合同 p0,p1,p2，按长度递增。若完整总 M0=0，则最长接收以 q=p0、r=p1 满足本文假设，因此两个高种子面积必须同号。

若还要求最低完整 C 行沿原 U0 方向，已接纳最低行的有符号面积条件给
\[
\operatorname{sgn}(\mathfrak h_1\mathfrak h_2)
=-\operatorname{sgn}(w\tau),
\]
其中 tau 是同一最低实接收在两个单位投影方向的非零实投影比，w 是实际发送权重比，sign w=sign(c01 c02)。所以还必须 w tau<0。

最低实方向多项式可以沿用已接纳符号，写为
\[
F(\tau)=\tau(L-wM\tau)
+C_0(wA_2\tau^3-A_1)=0,
\tag{HA.11}
\]
其中 A1,A2,L,M 均正，C0 是最低两个单位投影的余弦。在 w tau<0 时，第一个括号 L-wM tau>0，第二个括号 wA2 tau³-A1<0。故 HA.11 必须有 C0≠0 且 sign C0=sign tau。于是
\[
\boxed{c_{01}c_{02}C_0<0.}
\tag{HA.12}
\]
特别最低投影正交 C0=0 的方向子域，不能同时满足总 M0=0 与最低 C 原方向；此前正交投影下单独最低行仍可解，这两句话并不矛盾。

本推论没有声称所有最低三次实根满足 w tau>0；这样的存在分支即使另证，也不能代表全部根。这里只剔除面积异号的最低行分支，将可能共同过门的分支收窄到同号面积、w tau<0 及严格几何号 HA.12。没有证明这个子域整体为空，未选择任何实际数据。

## HA.5 边界与范围

本最长行域要求两个发送都短于接收，其中恰一个线性、另一个面积非零。它不直接排除全线性或全面积非零类型，也不能把 HA.8 用在另发送比接收更长且 rho 未知的中间行。所有除数 a、zeta、eta、chi、b、A、y 均在前文支付非零；C、s、v、B 可以为零，未被作分母。

完整零行意味着 HA.4–5，但负判别式或面积同号单独都不是其充分条件。本文未检 HA.5 的实部与原三边共享系数的其余相容性，也没有支付三个 C 方向、共同幅度、平移或其它模板变换。没有新实际原解时间、无限维误差、有限两步机制、统一迭代、单初值无限尺度、有限总时间、奇性或全局正则性结论。

源依赖：已接受 net-mixed-cancellation/INDEPENDENT.md 的完整 NC、three-edge-compatibility/MAX_RECEIVER_RATIO.md、two-elliptic-compatibility/acceptance.json 绑定的最低行接口。根在本连续任务已实际全文读这些科学文本并完成相应手核，HA.1–12 是本次新手工推导，待独立核验。未运行科学程序、数值、数组或实际选参。PRIVATE_CORE；NO-CANDIDATE；NOT CLAY。
