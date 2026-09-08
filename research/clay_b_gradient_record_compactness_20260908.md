# 梯度纪录缩放：除中心应变外的强紧性

2026-09-08。PRIVATE_CORE，内部提取命题与路线检查。上一轮 SVG 完成有符号指数矩核算，没有临界新估计。本轮保留同一原 NS 解，检查梯度纪录缩放是否可以避免速度缩放的常向量退化。

结论分两层：实际缩放序列的涡量、梯度空间差，以及减去中心对称应变后的速度具有强紧性；剩余中心应变目前只有时间弱星紧性。单位梯度可能留在这一剩余部分，不能直接传给古老极限。即使补上时间紧性，线性增长的非零仿射古老解仍未被排除。本轮不是新的正则性判据或 Clay 结果，不认领经典工具的新颖性。

## 1. 同一解的纪录点和移动参考系

固定 \(\Omega=(\mathbb R/2\pi\mathbb Z)^3\)、\(\nu>0\)，u 为同一个任意光滑无散初值的无外力 NS 解，在 \([0,T_*)\) 光滑，\(T_*<\infty\)。固定 \(0<a<T_*\)。若梯度在终端前无界，可选首次达到逐增阈值的纪录点，使
\[
 N_n=\max_{a\le t\le t_n}\|\nabla u(t)\|_\infty
 =|\nabla u(x_n,t_n)|\longrightarrow\infty,
 \quad t_n\uparrow T_*,\quad r_n=N_n^{-1/2}.
 \tag{GRC.1}
\]
矩阵用 Frobenius 范数。若梯度反而一致有界，标准光滑 Hm 能量估计和局部延拓接口即可继续解；这里不以梯度纪录的存在替代该经典接口的假设。

在原解上解 \(X_n'(t)=u(X_n(t),t)\)、\(X_n(t_n)=x_n\)，选择其周期提升；令 \(c_n(t)=u(X_n(t),t)\)。置
\[
 t=t_n+r_n^2s,\qquad
 v_n(y,s)=r_n[u(X_n(t)+r_ny,t)-c_n(t)],
 \quad G_n=\nabla_yv_n,\quad\omega_n=\operatorname{curl}_yv_n.
 \tag{GRC.2}
\]
空间周期尺度 \(L_n=r_n^{-1}\) 趋于无穷，过去长度 \((t_n-a)/r_n^2\) 趋于无穷。任意固定 \(B_R\times[-H,0]\) 最终都包含在实际区间内。

直接微分得原黏性的完整 NS 方程
\[
 \partial_sv_n+(v_n\cdot\nabla)v_n-\nu\Delta v_n+\nabla\pi_n=0,
 \quad\operatorname{div}v_n=0,
 \quad
 \pi_n=r_n^2p(X_n+r_ny,t)+r_n^3c_n'(t)\cdot y.
 \tag{GRC.3}
\]
这里 \(c_n'=D_tu(X_n,t)=\nu\Delta u(X_n,t)-\nabla p(X_n,t)\)。压力线性项来自参考系加速，不能删除或称作周期常数规范；其 Hessian 为零。

纪录界及沿线段积分给
\[
 v_n(0,s)=0,\quad |G_n|\le1,\quad |G_n(0,0)|=1,
 \quad |v_n(y,s)|\le|y|,\quad |\omega_n|\le\sqrt2.
 \tag{GRC.4}
\]
这确实给每个固定移动柱的局部能量与耗散上界。它不提供全空间有界速度或全空间有限能量。

## 2. 涡量的强紧性包括纪录顶端

curl 消去完整压力，包括参考系线性项：
\[
 (\partial_s+v_n\cdot\nabla-\nu\Delta)\omega_n=G_n\omega_n.
 \tag{GRC.5}
\]
固定 R、H，取 \(\chi\in C_c^\infty(B_{R+1})\)，在 \(B_R\) 为1；取时间截止 \(\eta\)，在 \(s_0=-H-1\) 附近为0，在 \([-H,0]\) 为1。令 \(Z=\eta\chi\omega_n\)，空间零延拓到全空间。采用 \((\operatorname{div}F)_i=\partial_kF_{ik}\)，逐分量计算得
\[
 (\partial_s-\nu\Delta)Z_i=\partial_kF_{ik}+f_i,\quad Z(s_0)=0,
 \quad F_{ik}=-Z_i v_{n,k}-2\nu\eta\omega_{n,i}\partial_k\chi,
 \tag{GRC.6}
\]
\[
 f=\eta\chi G_n\omega_n
   +\eta(v_n\cdot\nabla\chi+\nu\Delta\chi)\omega_n
   +\eta'\chi\omega_n.
 \tag{GRC.7}
\]
特别是截止 Laplacian 项为正号。GRC.4 使 F、f 一致有界且空间紧支撑；常数只依赖固定柱、截止及黏性，不需要压力或 G 的时间连续性。

记全空间热核为 \(h_\nu(\tau)\)。Duhamel 以 \(\partial_kh_\nu*F_{ik}\) 和 \(h_\nu*f_i\) 表示 Z。对 \(0<\alpha<1\)，直接 Gaussian 微分给
\[
 \begin{aligned}
 \|\delta_z\nabla h_\nu(\tau)\|_1
 &\le C\min\{(\nu\tau)^{-1/2},|z|(\nu\tau)^{-1}\},\\
 \|\nabla h_\nu(\tau+d)-\nabla h_\nu(\tau)\|_1
 &\le C\nu^{-1/2}\min\{\tau^{-1/2},d\tau^{-3/2}\}.
 \end{aligned}
 \tag{GRC.8}
\]
第一式插值后时间积分有限，给 \(C_\alpha|z|^\alpha\)。第二式在 \(\tau=d\) 分割积分，再加长度 d 的新增时间段，给 \(C\sqrt d\)。零阶热势类似给空间 \(C_\alpha|z|^\alpha\) 和时间 \(C_\alpha d^{\alpha/2}\)；也可先得到 \(Cd[1+|\log d|]\)。所有积分只用实际过去，比较的是同一源时刻的两个核，不比较 F 在相邻时刻的值。因此
\[
 \sup_n\|\omega_n\|_{C^\alpha_{\rm par}(B_R\times[-H,0])}
 \le C_{\alpha,\nu,R,H}.
 \tag{GRC.9}
\]
顶端 s=0 包含在此估计内，不需要统一正向延拓窗。按整数柱对角选列，得到涡量在所有这些紧柱上一致收敛，并在更低 Hölder 指数下强收敛。

## 3. 完整周期 Biot–Savart 的空间差

虽然 v 的空间均值随参考系改变，梯度的周期 div–curl 恒等式仍为
\[
 (G_n)_{ij}=\epsilon_{iab}
 (\partial_j\partial_a\Gamma_{L_n})*\omega_{n,b},
 \quad -\Delta\Gamma_L=\delta_0-(2\pi L)^{-3}.
 \tag{GRC.10}
\]
\(\epsilon_{iab}\) 为 Levi-Civita 符号。旧 [BL §2](clay_b_critical_euler_compactness_20260906.md) 的周期 Green 构造给 \(\Gamma_L(z)=L^{-1}\Gamma_1(z/L)\)。固定比例的原点邻域内，\(K_{ja,L}=\partial_j\partial_a\Gamma_L\) 等于 Euclidean 主值核、接触项 \(-\delta_{ja}\delta_0/3\)，以及大小 \(O(L^{-3})\) 的光滑修正。远离原点的光滑性与缩放还给
\[
 |\nabla K_{ja,L}(z)|\le C d_L(z,0)^{-4}.
 \tag{GRC.11}
\]
这用完整周期核，不对三次幂周期像级数逐项取绝对值。

记 \(D_n(y,s)=G_n(y,s)-G_n(0,s)\)。固定 \(|y|\le R_0\)，再选 \(R>2R_0\) 和 \(\chi_R=1\) 于 \(B_R\)、支于 \(B_{2R}\)。对充分大 n，在远源 \(1-\chi_R\) 上沿 y 线段比较 GRC.10 的核。由 GRC.11 及 \(|\omega_n|\le\sqrt2\)，
\[
 \sup_{|y|\le R_0,s}|D_n^{\rm far}(y,s)|
 \le C R_0\int_{d_{L_n}(z,0)\ge R}d_{L_n}(z,0)^{-4}dz
 \le C R_0/R.
 \tag{GRC.12}
\]
周期接缝不产生边界项。该尾估计不依赖扩张胞总能量。

先固定 R。近源涡量在紧柱强收敛且有一致空间 \(C^\alpha\) 界，因此对应 Euclidean 奇异积分一致收敛。可直接验证这一点：把主值积分分成距离小于 \(\delta\) 与其余部分；前者利用核球面零均值和 Hölder 差界为 \(C\delta^\alpha\)，后者由一致收敛控制，再先后令 n、\(\delta\) 取极限。接触项对梯度差的贡献为
\[
 -\tfrac13\epsilon_{ijb}[\omega_{n,b}(y,s)-\omega_{n,b}(0,s)],
 \tag{GRC.13}
\]
也强收敛，不能漏掉。周期光滑修正的近源贡献至多 \(CR^3L_n^{-3}\)，在固定 R 下趋零。

最后令 R 趋于无穷，用 GRC.12 得到：\(D_n\) 在每个固定闭古老柱上是一致 Cauchy 列。没有交换远场截断与扩张胞极限。

## 4. 仅余中心对称应变的时间弱星部分

设
\[
 S_n(s)=\operatorname{sym}G_n(0,s),\quad
 A_n(s)=\operatorname{skew}G_n(0,s),\quad
 w_n(y,s)=v_n(y,s)-S_n(s)y.
 \tag{GRC.14}
\]
\(S_n\) 对称、迹零、模长至多1，而
\((A_n)_{ij}=-\epsilon_{ijb}\omega_{n,b}(0,s)/2\) 已由 GRC.9 强紧。于是
\[
 \nabla w_n=D_n+A_n,\qquad w_n(0,s)=0.
 \tag{GRC.15}
\]
沿空间线段积分后，\(w_n\) 在每个紧柱强收敛于 \(C([-H,0];C^1(B_R))\)；这里指速度及一阶空间导数的一致范数，不声称时间可微。再选子列可使 \(S_n\rightharpoonup^*S\) 于每个有限过去区间的 \(L^\infty_s\)。这证明本轮的提取命题。

减去时变线性应变不是 NS 对称变换；不能把 w 单独称为 NS 解。单位归一化可能全部处在 \(S_n(0)\)。虽然可再选 \(S_n(0)\) 的矩阵极限，但弱星极限 S 未必有0处左迹，不能将两者识别。这里隔离的是强紧性尚缺的五个时间函数，没有将 NS 化成闭合的五维常微分方程。

## 5. 传递方程时的压力范围

令 \(v=Sy+w\)，再选子列 \(S_n^2\rightharpoonup^* B\)。由于 w 强收敛，非线性的交叉项通过弱强配对传递；纯仿射项满足
\[
 \operatorname{div}[(S_ny)\otimes(S_ny)]=S_n^2y.
 \tag{GRC.16}
\]
因此非线性散度的缺陷为
\[
 (B-S^2)y=\nabla\!\left[\tfrac12y^\top(B-S^2)y\right].
 \tag{GRC.17}
\]
矩阵对称，但其迹一般不为零；这项二次势不一定调和。对紧支撑无散测试函数，该项及每个原压力梯度都消失，因而 v 满足分布的投影 NS 方程。空间 Poincaré 引理将无旋分布剩余项写为压力梯度，得到某个允许时间分布的压力 p，使 v 满足分布 NS。

也可先在每个 n 的压力中加入 \(\tfrac12y^\top(S_n'+S_n^2)y\)，得到 w 方程，其余项只对 S_n 线性。极限重建 v 时减去 \(\tfrac12y^\top(S'+S^2)y\)。其中 S' 可能只是时间分布，其二次势因 \(\operatorname{tr}S'=0\) 而调和。两种表述相容，不能把它们混成“所有缺陷都为调和压力”。

此处没有证明压力属于局部 \(L^{3/2}\)，没有传递 suitable 局部能量不等式，也没有得到全空间 bounded-mild 或光滑古老解。分布方程及局部 Lipschitz 空间界，不足以套用旧 BI/BJ 的有界 mild 刚性问题。

## 6. 不能从宽局部界补出剩余时间紧性

下面只是宽局部假设的精确 NS 检验，不是同一固定周期原解的反例。令
\[
 D=\operatorname{diag}(1,-1,0),\quad
 J=\begin{pmatrix}0&-1&0\\1&0&0\\0&0&0\end{pmatrix},\quad
 F_n(s)=e^{s/n}\cos(ns),\quad
 Q_n(s)=aF_n(s)D+cJ,
 \tag{GRC.18}
\]
其中 \(s\le0\)、\(a>0,c\ge0,2(a^2+c^2)=1\)。因为 \(DJ+JD=0\)，
\(Q_n'+Q_n^2=aF_n'D+(a^2F_n^2-c^2)\operatorname{diag}(1,1,0)\) 对称。故
\[
 v_n^{\rm aff}=Q_n(s)y,\qquad
 p_n^{\rm aff}=-\tfrac12 y^\top(Q_n'+Q_n^2)y
 \tag{GRC.19}
\]
是任意正黏性下的精确无外力全空间 NS 解。它们在中心为零、梯度模长至多1，且仅在s=0达到历史峰1；涡量恒为 \((0,0,2c)\)。然而
\[
 Q_n(0)-Q_n(-\pi/n)
 =a(1+e^{-\pi/n^2})D\longrightarrow2aD\ne0.
 \tag{GRC.20}
\]
所以局部速度和梯度没有顶端时间等度连续性。快速项由压力中的二次调和势 \(-aF_n'(y_1^2-y_2^2)/2\) 承担，Poisson 源及涡量界不能控制它。

取 \(c=0\) 时，减应变场全为零；时间弱星极限也为零，但终端单位梯度不消失于原序列。取 \(a=c=1/2\) 时，涡量非零且恒定，仍有同一应变振荡障碍。所有这些仿射场都非周期、无限能量；不能据此断言实际周期纪录序列发生该退化。即使采用时间常矩阵的仿射解，宽线性增长古老类的全零刚性也不成立；新增时间紧性不是完整正则性出口。

## 7. 同一周期来源中仍需估计的具体量

取固定光滑径向 \(\psi\ge0\)，支于 \(B_1\)，积分为1；令 \(\overline S_n=\int\psi\operatorname{sym}G_n\)。\(\overline S_n-S_n=\int\psi\operatorname{sym}D_n\) 已强时间紧。对真实梯度方程积分，得
\[
 \overline S_n'=B_n-\int\psi\nabla^2\pi_n,
 \quad B_n=\nu\int\Delta\psi\operatorname{sym}G_n
 +\int(v_n\cdot\nabla\psi)\operatorname{sym}G_n
 -\int\psi\operatorname{sym}(G_n^2),
 \quad |B_n|\le C_{\nu,\psi}.
 \tag{GRC.21}
\]
因此剩余时间紧性要求控制同一序列的平均压力 Hessian 在缩短时间段上的有符号积分，而非仅有每个 n 的光滑性。加速线性压力不影响这个量。

规范周期压力的 Poisson 源为 \(f_n=\operatorname{tr}G_n^2\)，\(|f_n|\le1\)。其平均 Hessian 的核为 \(\nabla^2\Gamma_{L_n}*\psi\)。近源平滑后有固定上界，远源的绝对值估计只有
\[
 \left|\int\psi\nabla^2\pi_n\right|
 \le C_\psi(1+\log L_n).
 \tag{GRC.22}
\]
这是由三次幂核在 \(1\lesssim|z|\lesssim L_n\) 积分得到的粗界，不是实际发散下界。其迹由 \(-\int\psi f_n\) 已受控；未闭合部分是对称迹零方向。源的周期零均值不能在这个估计中自动消去所有角向贡献。本轮没有由原时间演化证明更强的抵消或连续模量。

[TG](clay_b_strong_gradient_terminal_trace_20260908.md) 的强梯度 L1 迹同样保留缩放损失。若 \(\Omega_G(m)=\sup_{t\in[a,T_*]}\sup_{|E|\le m}\int_E|G(t)|\)，则 \(\Omega_G(m)\to0\)，但
\[
 \sup_{-H\le s\le0}\int_{B_R}|G_n(s)|
 \le r_n^{-1}\Omega_G(|B_R|r_n^3).
 \tag{GRC.23}
\]
移动中心不影响此空间模量。这里的原能量耗散指 \(\int|G|^2\)，不是 \(\int|\nabla G|^2\)。沿用 TG.12 的 \(\Theta(G)=d(G)G/|G|^{3/2}\)（零点取零），有 \(\Theta(G_n)=r_n\Theta(G)\)、\(\nabla_y\Theta(G_n)=r_n^2\nabla_x\Theta(G)\)，右端均在 GRC.2 的原坐标取值。因此 \(\int|G_n|^2\) 及 \(\int|\nabla_y\Theta(G_n)|^2\) 的时空积分，分别等于对应移动柱上原积分的 \(r_n^{-1}\) 倍；有限总量不使它们自动趋零。因此局部共同上界已得，小形状耗散仍未得。

同一原解的完整左端关系也须保留。令 \(\sigma_n=(a-t_n)/r_n^2\)，则
\[
 -\sigma_n/L_n^2=t_n-a\longrightarrow T_*-a>0,
 \quad\|v_n(\sigma_n)\|_\infty\le2r_n\|u(a)\|_\infty\to0,
 \quad\|G_n(\sigma_n)\|_\infty\le r_n^2\|G(a)\|_\infty\to0.
\]
但 \(\sigma_n\to-\infty\)，不能将移动左端的小量传成极限在固定古老时刻、或在无限过去的消失条件。这是沿用 BH/BI 所强调的同源历史区别，不是重新完成了一次历史排除。

## 8. 本轮判断与下一项

GRC.9–15 是本轮实际完成的正面提取结果：没有直接控制完整压力，也能证明涡量及去中心应变后的强紧性。GRC.21 明确了剩余模式对应的真实压力量。它们不是一般三维正则性估计；仿射分支的来源限制与剩余时间紧性必须同时解决，不能将“补一个时间模量”说成已接近 Clay 证明。

下一轮只围绕 GRC.21 的同一周期压力时间积分作一次原结构核算，并同时判断所得约束能否排除、而非仅保留非零仿射历史。不得再把宽仿射类的例子当作同一原解反例，也不预设该核算能闭合。若只是 GRC.21 的等价改写、对数粗界或额外条件，则停止此具体入口，不继续以版本递增替代研究判断。

主任务全文读 BH、BL、BM，复用已核 TG；三位协作者分别核旧 BI/BJ 去重、热核顶端模块、周期差核及仿射压力/弱极限模块。未重审旧外部局部存在、全部 mild 理论或新颖性；实际成稿审读另记检查点。两条普通定向网页查询只定位到已有古老解文献，例如 [Koch–Nadirashvili–Seregin–Šverák](https://arxiv.org/abs/0709.3599)，不作为未读证明的新输入，也未使用 Deep Research。

一般 NS / Clay 仍 OPEN / NOT CLAY。无新独立小节、release、重复交接、网页、PDF、译文、recap、仿真、DGX 或科学附图；保留 TG 最后独立冻结状态。全部为私人研究记录和 AI 辅助核查，非真人同行评审。
