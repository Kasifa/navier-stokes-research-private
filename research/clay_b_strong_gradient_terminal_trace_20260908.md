# 有限终端的强梯度迹：从可积源到强 W¹,¹ 收敛

2026-09-08。TG，PRIVATE_CORE，PROVED IN STATED SCOPE。这里得到一项真实的终端控制，但仍不是临界正则性估计：同一条光滑周期三维 NS 轨道在趋近任何有限光滑存在端点时，完整速度梯度具有强 L1 左迹，速度具有强 W1,1 左迹。此前只取得弱测度终端迹的线性增长几何缺陷量，在本节范围内也有强 L1 迹。一般三维 NS / Clay 仍 OPEN / NOT CLAY；未认证新颖性或真人同行评审。

关键是保留同一真实漂移，把已经可积的梯度源截成有界源。辅助线性方程有统一最大值界，因而有强 L2 终端迹；L1 收缩再把这个性质传回原梯度。辅助场不要求是速度梯度，也不冒充另一个 NS 解。

## 1. 主结论与已有的压力估计

固定 \(\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3\)、\(\nu>0\)。u 是任意光滑无散周期初值所产生的同一无外力 NS 解，在 \([0,T_*)\) 光滑，\(T_*<\infty\)；不假设它在 \(T_*\) 正则或可延拓。固定任意 \(0<a<T_*\)，记
\[
 G=\nabla u,\qquad H=\nabla^2p,\qquad
 F=-G^2-H,\qquad
 (\partial_t+u\cdot\nabla-\nu\Delta)G=F.
 \tag{TG.1}
\]
矩阵内积、模长均采用 Frobenius 约定，\(G^2\) 是矩阵乘积。沿用 [GD §2](clay_b_gradient_rank_one_defect_20260908.md) 已核的周期 Hardy 压力接口和能量预算：
\[
 \|H(t)\|_1\le C_H\|G(t)\|_2^2,
 \qquad
 \|F\|_{L^1((a,T_*)\times\mathbb T^3)}
 \le(1+C_H)\int_a^{T_*}\|G(t)\|_2^2dt<\infty.
 \tag{TG.2}
\]
这里用的是无散—无旋补偿，不是声称 Riesz 变换在一般 L1 上有界。\(u\in L^2((a,T_*)\times\mathbb T^3)\) 也由固定有限时间和速度能量界得到。

**定理 TG-A。** 存在唯一 \(u_*\in W^{1,1}(\mathbb T^3;\mathbb R^3)\cap L^2\)，\(\operatorname{div}u_*=0\)，使
\[
 u(t)\longrightarrow u_*\quad\text{强 }W^{1,1},\qquad
 G(t)\longrightarrow G_*:=\nabla u_*\quad\text{强 }L^1,
 \quad t\uparrow T_*.
 \tag{TG.3}
\]
将端点赋为这些极限后，\(G\in C([a,T_*];L^1)\)、\(u\in C([a,T_*];W^{1,1})\)。这里不声称 \(G_*\in L^2\)、速度强 L2 收敛、终端光滑、经典延拓或任意局部弱解的同一结论。

## 2. 同漂移线性引理

先证明一个有限维向量值引理。设 \(b,z,f\) 在 \([a,T)\times\mathbb T^3\) 光滑，\(T<\infty\)、\(\operatorname{div}b=0\)，且
\[
 \partial_tz+b\cdot\nabla z-\nu\Delta z=f,
 \qquad b\in L^2_{t,x},\quad f\in L^1_{t,x}.
 \tag{TG.4}
\]
则 z 有强 L1 终端迹。光滑性只要求在每个 \([a,b_0]\)、\(b_0<T\) 上成立；不要求漂移在 T 有点态界。

取固定 \(\vartheta\in C_c^\infty([0,\infty))\)，\(0\le\vartheta\le1\)，在 \([0,1]\) 为1、在 \([4,\infty)\) 为0，令
\[
 f_R=f\,\vartheta(|f|^2/R^2),\qquad
 |f_R|\le2R,\qquad
 \delta_R:=\|f-f_R\|_{L^1_{t,x}}
 \le\int_{\{|f|>R\}}|f|\longrightarrow0.
 \tag{TG.5}
\]
这种截断对向量或矩阵整体光滑，不产生分量范数常数的混淆。令 \(v_R\) 解同一漂移 b 的线性方程，源为 \(f_R\)、初值为 \(z(a)\)。在每个闭前终端区间使用经典线性抛物理论，唯一性将各区间的解拼成 \([a,T)\) 上同一个 \(v_R\)。最大值原理作用于正则化的向量模长，给
\[
 \sup_{a\le t<T}\|v_R(t)\|_\infty
 \le\|z(a)\|_\infty+2R(T-a)=:B_R.
 \tag{TG.6}
\]
该常数不依赖临近 T 的漂移高阶范数。全周期能量测试同时给 \(v_R\in L^2_tH^1_x\)，而 \(b v_R\in L^2_{t,x}\) 由 \(B_R\|b\|_{L^2_{t,x}}\) 控制。此时所有辅助场的源和输运通量都是 L2；原 f 无需提升到 L2。

## 3. 辅助场的强 L2 端点：直接 Fourier 证明

以下不预设 \(v_R(T)\)。固定 R，令 \(P_N\) 为周期 Fourier 的 \(|k|\le N\) 正交投影，\(h_N=(I-P_N)v_R\)。对
\(\partial_tv_R-\nu\Delta v_R=f_R-\operatorname{div}(b v_R)\)
作高频能量测试，Cauchy–Young 给
\[
 \frac d{dt}\|h_N\|_2^2+\nu\|\nabla h_N\|_2^2
 \le\|h_N\|_2^2+\|(I-P_N)f_R\|_2^2
 +\nu^{-1}\|(I-P_N)(b v_R)\|_2^2.
 \tag{TG.7}
\]
输运通量是张量，\(P_N\) 分量作用并与散度交换；这里没有把投影后的输运项错误当成零。Gronwall 得
\[
 \begin{aligned}
 \sup_{a\le t<T}\|(I-P_N)v_R(t)\|_2^2
 \le e^{T-a}\bigl\{&\|(I-P_N)z(a)\|_2^2
 +\|(I-P_N)f_R\|_{L^2_{t,x}}^2\\
 &+\nu^{-1}\|(I-P_N)(b v_R)\|_{L^2_{t,x}}^2\bigr\}
 \longrightarrow0.
 \end{aligned}
 \tag{TG.8}
\]
最后的极限对固定 R 成立，因为每个输入已是整个有限时间柱上的 L2 函数。每个固定 Fourier 系数由方程有可积时间导数，故有唯一终端极限。有限模的连续性与 TG.8 的全时间一致高频尾一起给
\[
 v_R\in C([a,T];L^2).
 \tag{TG.9}
\]
这也是标准能量空间时间连续性结论的一个直接证明，没有假设端点漂移光滑或求解反向热方程。

## 4. L1 收缩把迹传给原场

\(w_R=z-v_R\) 满足同漂移方程，源为 \(f-f_R\)，初值零。对 \(\sqrt{|w_R|^2+\epsilon^2}-\epsilon\) 用凸链式法则，空间积分后输运为零、扩散非正。先固定 \(t<T\) 再令 \(\epsilon\downarrow0\)，得到
\[
 \sup_{a\le t<T}\|z(t)-v_R(t)\|_1\le\delta_R.
 \tag{TG.10}
\]
因此 \(\sup_{t<T}\|v_R(t)-v_S(t)\|_1\le\delta_R+\delta_S\)。由 TG.9，将 t 趋于 T 后同一界仍成立。故 \(v_R\) 在 \(C([a,T];L^1)\) 中为 Cauchy 列，其极限在 \([a,T)\) 恰为原来的 z。这证明 TG.4 的引理，不只证明子列弱收敛。

令 \(b=u,z=G,f=F\)，TG.2 验证引理的全部假设，得到 TG.3 的梯度结论。NS 的周期速度均值守恒。对任意 \(s,t<T_*\)，周期 Poincaré 给
\[
 \|u(t)-u(s)\|_1\le C\|G(t)-G(s)\|_1.
 \tag{TG.11}
\]
故 u 为 W1,1 Cauchy；其极限的弱梯度就是 \(G_*\)，无散性也传到极限。由原速度统一 L2 界与强 L1 子列的几乎处处收敛，Fatou 给 \(u_*\in L^2\)。没有从这里断言速度强 L2 收敛。\(v_R\) 无需满足梯度兼容性，兼容性只对原 G 及其强极限使用。

## 5. 终端几何缺陷测度现在可以识别

记 \(q=|G|\)、\(d(G)=\operatorname{dist}_F(G,\{\operatorname{rank}\le1\})\)。在非零矩阵定义
\[
 R_g(G)=\frac{d(G)^2}{|G|},\qquad
 f_c(G)=\frac{|\operatorname{adj}G|^2}{|G|^3},\qquad
 k_c(G)=\frac{|\operatorname{adj}G|}{|G|},\qquad
 \Theta(G)=\frac{d(G)G}{|G|^{3/2}},
 \tag{TG.12}
\]
在零矩阵全部取零。前三个商分别沿用 GD、[CD §1/§5](clay_b_cofactor_defect_dynamics_20260908.md)、[LK §1](clay_b_linear_cofactor_kato_20260908.md)，\(\Theta\) 沿用 [WE](clay_b_weak_gradient_entropy_20260908.md)。\(q,d,R_g,f_c,k_c\) 是连续、至多线性增长的矩阵函数；\(\Theta\) 连续且 \(|\Theta(G)|^2\le|G|\)。TG.3 给原 G 的一致可积性和依测度收敛，Vitali 因而给
\[
 q(t),d(t),R_g(t),f_c(t),k_c(t)
 \longrightarrow q_*,d_*,R_{g,*},f_{c,*},k_{c,*}\quad\text{各自强 }L^1,
 \qquad \Theta(G(t))\longrightarrow\Theta(G_*)\quad\text{强 }L^2.
 \tag{TG.13}
\]
每个星号表示在 \(G_*\) 上代入相同函数。严格地，对任意趋端点的时间列取几乎处处收敛子列，用线性增长和一致可积性；极限唯一后传回整个时间极限。

所以，在本节同一光滑周期前终端轨道范围内，CD 等旧稿取得的弱终端测度，就是相应的 L1 密度乘体积测度，不再可能带额外奇异浓缩质量。\(D^su_*=0\)，无需再用 Alberti 秩一定理猜测该奇异部分的方向。旧冻结稿保持不变，本节另行加强其当时未闭合的终端边界。

这不排除梯度平方、\(|\nabla\Theta|^2\) 或完整熵耗散在缩小柱中的临界浓缩，也不识别所有零集耗散极限。终端切片的强 L1 迹与时空导数耗散的临界控制是不同命题。

## 6. 仍然缺少的尺度速率

证明给的是固定解依赖的趋零模量：先令 \(R\uparrow\infty\) 使 \(\delta_R\) 小，再在固定 R 下令 \(N\uparrow\infty\)，最后处理有限 Fourier 模的终端连续性。TG.2 的总 L1 上界不给源截断尾 \(\delta_R\) 的统一衰减率；TG.8 也保留实际 \(u v_R\) 的 Fourier 尾，不能藏进一个仅依赖能量的常数。

在 NS 重标度 \(u^{(r)}(y,s)=r u(x_0+ry,T_*+r^2s)\) 下，终端梯度切片的局部 L1 量是
\[
 \int_{B_1}|\nabla_yu^{(r)}(y,0)|dy
 =r^{-1}\int_{B_r(x_0)}|G_*(x)|dx.
 \tag{TG.14}
\]
L1 绝对连续性只使分子趋零，不保证它是 \(o(r)\)。同样，TG.13 不给 PF 所需的 \(r^{-1}\int_{Q_r}|\nabla\Theta|^2\) 小量或共同局部 A/E 上界。这里没有一般正则性结论，强迹也不能被当作光滑重启所需的 H1 速度初值。

下一项具体检验是：能否将同漂移截源论证局部化，明确指定中心、缩小前终端柱上的全部误差项，并从原 NS 结构控制源尾和辅助通量尾的临界速率。先写完整截止及压力项，再判断是否强于现有定性迹；不把单纯的 \(\delta_R\to0\)、任意交换 R 与 r 的顺序或又一个初端例子当作增益。

## 7. 文献与本地重叠范围

最初候选是“终端 BV 迹加 Alberti 秩一结构”。本轮完整读了 [Massaccesi–Vittone 的简短证明](https://arxiv.org/html/1601.02903v1) 的定理、引理及所印证明；它约束的是 BV 导数奇异部分的极向量，并不提供 NS 时间估计。本节最终改用直接 PDE 截源，主证明不依赖该定理，也不依赖尚未证明的 strict BV 收敛。R0.71O 已覆盖一般 Reshetnyak／Young 测度的拓扑区别，不能将这些已有工具重命名为本节的新输入。

另作三条限定检索：`Navier Stokes "W^{1,1}" "continuity"`、`Navier Stokes gradient "L1" "strong continuity"`、`advection diffusion integrable source "L1" "continuity" divergence free`。检索没有在所读结果中定位到本节精确周期梯度终端陈述，但这不是充分查新。[Moerschell–Sorella 的期刊摘要](https://doi.org/10.1016/j.matpur.2025.103777) 区分有界能量类输运—扩散解在 L2 漂移下的唯一性与低于该范围的非唯一性；本次只读摘要，不移植其证明。本节只用闭前终端区间的经典线性解，并已直接证明所需端点性质。Tao 旧原稿的定点文字检索没有给本节精确结论，也不将检索未命中作为新颖性证据。

本地实际读回 GD、WE 全文，CD 的定义和弱测度迹部分、LK 的定义部分；旧压力接口按 GD 已冻结范围使用，不重新认证所有上游外部定理。主任务、ma_freeze_review 和 variable_reference_check 分别核算截源、端点与兼容识别；最终实际版本和独立复核范围另记审查文件。没有仿真、DGX、数值证书或科学附图。完整新材料保持私有，公开摘要、论文、读者版本和发布执行不属于本任务。
