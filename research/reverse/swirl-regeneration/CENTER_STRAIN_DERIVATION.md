# 固定旋流涡核中心的第一代应变

2026-09-07。PRIVATE_CORE。独立解析推导，待根代理另审；不提交或冻结。本稿已实读 `CONTRACT.md`、`CENTER_STRETCH_CONTRACT.md` 与 `INDEPENDENT_DERIVATION.md`，始终使用同一个固定初值和尺度。下述常数为解析界与独立手算，不声称新增数值计算证书。

结论：全空间中心应变确为所猜测的 \(g_0\operatorname{diag}(1,-2,1)/5\)。完整周期修正有足以处理已固定 \(\delta=1/100\) 的严格界，不需要事后缩小初值。由此得到真实方程初始导数中的中心轴向应变为负；正时间余项及其独立审查仍由根代理另行完成。

## 1. 固定对象、完整压力及第一代身份

记
\[
 \varepsilon=1/20,\quad b=(0,3/2,0),\quad z=y-b,
 \quad c(r)=2h'(\varepsilon^2-r^2),\quad g(r)=c(r)^2,
\]
其中 \(h(s)=e^{-1/s}\) 对 \(s>0\)，否则为0。令
\[
 A=\begin{pmatrix}0&0&1\\0&0&0\\-1&0&0\end{pmatrix},
 \quad P=\operatorname{diag}(1,0,1),
 \quad W(y)=c(|z|)Az.
\]
这里 \(A^2=-P\)，且 \(Az\cdot z=0\)。径向系数沿旋流输运不变，因此
\[
 (W\cdot\nabla)W=-g(|z|)Pz,
 \qquad B_{\mathbb R^3}(W,W)=P_L[g(|z|)Pz].
 \tag{1}
\]
压力按完整约定恢复：若 \(f=gPz\)，则
\(B=f-\nabla p\)、\(\Delta p=\nabla\cdot f\)。等价地
\(-\Delta p=\partial_i\partial_j(W_iW_j)\)。后文中心 Hessian 的符号均按此约定计算。

固定
\[
 J_W=\int_{\mathbb R^3}|W|^2dy>0,
 \quad \delta=1/100,
 \quad a(x)=\delta^{-1}J_W^{-1/2}W(x/\delta),
 \quad x_c=\delta b.
\]
其支撑为中心 \(x_c\)、半径 \(\delta\varepsilon\) 的球，远离周期边界，并有
\[
 \int_{\mathbb T^3}|a|^2dx=\delta.
 \tag{2}
\]
本稿所有能量积分使用未归一化 Lebesgue 测度。

这里确有 \(n=P_MB(a,a)=B(a,a)\)，而不是在中心悄悄删掉 \(P_M\)。一种直接核验是：\(f(z)=g(|z|)Pz\) 的 Fourier 变换在每个非零频率沿 \(P\xi\)；\(P\xi=\xi-\xi_2e_2\) 与 \(\xi\times e_2\) 正交。缩放和平移只改变标量系数，不改变这一正交关系。完整 Leray 投影减去的纵向分量也与 \(\xi\times e_2\) 正交。因此在所有非轴向周期 Fourier 模态上 \(P_TB(a,a)=0\)；轴向模态的 \(P_T\) 按定义为零。零模也为零，故所述身份成立。它同前一独立推导的轴向旋度论证一致。

## 2. 径向 Fourier 积分给中心完整投影

以下先把中心平移到 \(z=0\)。对标量径向 \(g\)，使用
\[
 \widehat g(\xi)=\int_{\mathbb R^3}e^{-i\xi\cdot z}g(|z|)dz=G(\kappa),
 \qquad \kappa=|\xi|,
\]
以及逆变换系数 \((2\pi)^{-3}\)。\(g\) 为光滑紧支撑径向函数，所以 \(G\) 及各阶导数快速衰减，且 \(G'(0)=0\)。因而下列 Fourier 积分绝对可积，\(G'(\kappa)/\kappa\) 在零频的表观奇性有光滑延拓。

由 \(\widehat{z_jg}=i\partial_{\xi_j}\widehat g\)，
\[
 \widehat f_i=i\frac{G'(\kappa)}\kappa(P\xi)_i,
\]
\[
 \widehat{(P_Lf)}_i
 =i\frac{G'(\kappa)}\kappa
 \left[(P\xi)_i-\xi_i\frac{\xi^TP\xi}{\kappa^2}\right].
 \tag{3}
\]
这里使用了完整全空间 Leray 矩阵，未用未投影的 \(f\) 代替非线性。

球面二、四阶矩为
\[
 \int_{S^2}n_in_j\,d\sigma=\frac{4\pi}{3}\delta_{ij},
\]
\[
 \int_{S^2}n_in_jn_kn_l\,d\sigma
 =\frac{4\pi}{15}
 (\delta_{ij}\delta_{kl}+\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk}).
 \tag{4}
\]
这些常数可以初等核对：奇数次数的混合矩由变号对称性为零；极角积分给 \(\int n_1^4=4\pi/5\)，再由 \(\int n_1^2=4\pi/3\) 和交换另外两个坐标得到 \(\int n_1^2n_2^2=4\pi/15\)。无须引用未核验的张量表示定理。

对 (3) 作一次空间微分，并用 (4)，得到
\[
 \nabla(P_Lf)(0)
 =-\frac{4\pi}{15(2\pi)^3}
 [3P-\operatorname{tr}(P)I]
 \int_0^\infty\kappa^3G'(\kappa)d\kappa.
\]
分部积分的两端边界均为零：无穷端由快速衰减，零端由 \(\kappa^3G(\kappa)\to0\)。所以径向积分为
\(-3\int_0^\infty\kappa^2G(\kappa)d\kappa\)。又由 Fourier 反演，
\[
 g_0:=g(0)=\frac{4\pi}{(2\pi)^3}
 \int_0^\infty\kappa^2G(\kappa)d\kappa>0.
\]
因此精确地
\[
 \nabla B_{\mathbb R^3}(W,W)(b)
 =\frac{g_0}{5}[3P-\operatorname{tr}(P)I]
 =\frac{g_0}{5}\operatorname{diag}(1,-2,1).
 \tag{5}
\]
这是径向光滑结构下的完整压力投影结果。它依赖 \(g\) 的中心值，但不依赖其余径向细节的数值积分；不把该结论推广到非径向匹配。

作为符号检查，\(\nabla f(0)=g_0P\)，所以实际全空间压力 Hessian 为
\[
 \nabla^2p_W^{\mathbb R^3}(b)
 =\frac{g_0}{5}\operatorname{diag}(4,2,4).
 \tag{6}
\]
其迹为 \(2g_0=\nabla\cdot f(0)\)，与 \(\Delta p=\nabla\cdot f\) 完全一致。

## 3. 周期 Green 四阶像和的合法性

令周期均值为零的 Green 分布 \(G_{\mathbb T}\) 满足
\[
 -\Delta G_{\mathbb T}=\delta_0-(2\pi)^{-3},
 \qquad \Phi(z)=\frac1{4\pi|z|}.
\]
为避免与本节的 Green 记号混淆，第2节的 \(G(\kappa)\) 只表示径向 Fourier 变换。

对 \(|z|\le1\)，严格有
\[
 \nabla^4(G_{\mathbb T}-\Phi)(z)
 =\sum_{m\in\mathbb Z^3\setminus\{0\}}
 \nabla^4\Phi(z+2\pi m).
 \tag{7}
\]
这个等式不能靠一个发散的未微分点电荷级数推出。可使用已经定义好的热核差：
\[
 G_{\mathbb T}-\Phi
 =\int_0^1\left[\sum_{m\ne0}K_{\mathbb R}(s,z+2\pi m)-(2\pi)^{-3}\right]ds
\]
\[
 \hspace{18mm}
 +\int_1^\infty[K_{\mathbb T}(s,z)-(2\pi)^{-3}-K_{\mathbb R}(s,z)]ds.
\]
作四阶空间微分后，常数背景项精确为零，两个时间段拼成全部非零像点的积分。对任何 \(w\ne0\)，Gaussian 的尺度变换 \(s=|w|^2\sigma\) 给
\[
 \int_0^\infty|\partial^\alpha K_{\mathbb R}(s,w)|ds
 \le C_\alpha|w|^{-5},\qquad |\alpha|=4.
\]
这里 \(C_\alpha\) 是一个有限 Gaussian 积分：零时间端指数衰减，无穷端为可积幂次。又因 \(|z+2\pi m|>5|m|\) 且 \(\sum_{m\ne0}|m|^{-5}<\infty\)，非零像点与时间积分可绝对交换，得到 (7)。

因此 (7) 保留完整周期 Green 定义及其中的均匀背景。它只说明该背景经过本问题实际需要的四阶微分后消失，不是把周期 Poisson 方程改成没有背景的方程。

## 4. 不依赖数值求和的严格常数

第四阶 Newtonian 导数的展开含系数105的一项、系数15的六项和系数3的三项。由 \(|n_i|\le1\) 和 \(|\delta_{ij}|\le1\)，每个分量满足
\[
 |\partial_{abij}\Phi(w)|\le\frac{105+6\cdot15+3\cdot3}{4\pi|w|^5}
 =\frac{204}{4\pi}|w|^{-5}.
\]
四阶张量共有 \(3^4=81\) 个分量。因此
\[
 \|\nabla^4\Phi(w)\|_F
 \le\frac{9\cdot204}{4\pi}|w|^{-5}
 =\frac{459}{\pi}|w|^{-5}<153|w|^{-5},
 \tag{8}
\]
其中只用了初等界 \(\pi>3\)。

当 \(|z|\le1\)、\(m\ne0\) 时，
\[
 |z+2\pi m|\ge2\pi|m|-1>5|m|.
\]
再按 \(j=\|m\|_\infty\) 分壳，第 \(j\) 壳有
\((2j+1)^3-(2j-1)^3=24j^2+2\) 个格点，且 \(|m|\ge j\)。所以
\[
 \sum_{m\ne0}|m|^{-5}
 \le24\sum_{j\ge1}j^{-3}+2\sum_{j\ge1}j^{-5}
 <24\cdot\frac32+2\cdot\frac54=\frac{77}{2}.
\]
最后一个严格界来自单调积分比较
\(\sum_{j\ge1}j^{-p}<1+\int_1^\infty x^{-p}dx\)，而不是有限截断近似。

定义与前文一致的四阶张量 Frobenius 常数
\[
 M_G=\sup_{|z|\le1}
 \|\nabla^4(G_{\mathbb T}-\Phi)(z)\|_F.
\]
由 (7)–(8)，
\[
 M_G<\frac{153}{5^5}\frac{77}{2}
 =\frac{11781}{6250}<2.
 \tag{9}
\]
本界覆盖全部81个分量和全部像点，没有未经认证的数值尾部。

## 5. 已固定尺度的中心应变及修正

全空间缩放给
\[
 \nabla B_{\mathbb R^3}(a,a)(x_c)
 =\delta^{-4}J_W^{-1}\nabla B_{\mathbb R^3}(W,W)(b)
 =c_*\operatorname{diag}(1,-2,1),
\]
\[
 c_*:=\frac{\delta^{-4}g_0}{5J_W}>0.
 \tag{10}
\]
周期与全空间的原始对流在支撑附近一致，差别全部来自压力。对压力 Hessian 的差，所有 \(x_c-z\) 都满足 \(|x_c-z|\le\delta\varepsilon<1\)。用应力的完整 Green 差公式，
\[
 \nabla n(x_c)=c_*\operatorname{diag}(1,-2,1)+E,
 \qquad \|E\|_F\le M_G\int|a|^2dx=M_G\delta<2\delta.
 \tag{11}
\]
其中 \(E\) 是负的压力 Hessian 差，故为实对称矩阵；它的迹为零，因为两个压力在中心附近满足同一个 Poisson 方程。张量收缩使用 \(\|a\otimes a\|_F=|a|^2\)，没有另外漏乘分量计数。

还须证明 (11) 对已经固定的 \(\delta\) 足够。对 \(0<s\le\varepsilon^2<1/2\)，\(h''(s)>0\)，所以 \(c(r)\) 随 \(r\) 不增，\(g(r)\le g_0\)。从而
\[
 J_W=\int_{|z|\le\varepsilon}g(|z|)(z_1^2+z_3^2)dz
 \le g_0\int_{|z|\le\varepsilon}|z|^2dz
 =\frac{4\pi}{5}\varepsilon^5g_0.
 \tag{12}
\]
因此
\[
 c_*\ge\frac{\delta^{-4}}{4\pi\varepsilon^5}
 =\frac{8\cdot10^{13}}{\pi}>2\cdot10^{13},
 \tag{13}
\]
其中用了 \(\delta=1/100\)、\(\varepsilon=1/20\) 及初等界 \(\pi<4\)。没有评价极小的 \(g_0\) 或 \(J_W\)；两者的共同尺度在严格不等式中抵消。

由 (11)–(13)，周期第一代场在涡核中心的轴向应变满足
\[
 e_2^T\operatorname{sym}\nabla n(x_c)e_2
 =-2c_*+E_{22}<-2c_*+2\delta<0.
 \tag{14}
\]
两个横向对角应变也保持正号。这里仅确定指定中心的初始第一代应变，不声称其全域符号一致。

## 6. 供真实解中心拉伸检验使用的接口

记 \(c_0=c(0)>0\)，则 \(g_0=c_0^2\)，
\[
 \nabla a(x_c)=\delta^{-2}J_W^{-1/2}c_0A,
 \quad \operatorname{sym}\nabla a(x_c)=0,
 \quad \omega_a(x_c)=2\delta^{-2}J_W^{-1/2}c_0e_2.
\]
特别地
\[
 |\omega_a(x_c)|^2=4\delta^{-4}J_W^{-1}g_0=20c_*.
 \tag{15}
\]
黏性的中心对称梯度也须实际检查。对于径向 \(c\)，
\[
 \Delta[c(r)Az]=(c''(r)+4c'(r)/r)Az.
\]
括号在原点有光滑径向延拓，所以其中心梯度仍是标量乘反对称矩阵 \(A\)。因此
\(\operatorname{sym}\nabla\Delta a(x_c)=0\)，而不是因为删去了黏性。

若 \(u\) 是由本固定 \(a\) 产生的完整光滑真实解，令
\(\mathsf S(u)=\operatorname{sym}\nabla u\)、
\(\Pi=\omega^T\mathsf S(u)\omega\)，则在初始时刻
\[
 \Pi(0)=0,\qquad
 \partial_tu(0)=\Delta a+n,
\]
\[
 \Pi'(0)=\omega_a(x_c)^T\mathsf S(n)(x_c)\omega_a(x_c)
 =20c_*[-2c_*+E_{22}]<0.
 \tag{16}
\]
求导产生的两个 \(\partial_t\omega\) 项因 \(\mathsf S(a)(x_c)=0\) 精确为零；没有预设这些涡量导数本身很小。

式 (16) 是完整方程的初始导数接口。本稿不另行声称已支付正时间的 \(\Pi(t)=t\Pi'(0)+O(t^2)\) 常数；真实解局部存在、严格余项和独立审查由根代理按当前合同完成。

## 7. 适用范围

本推导只涉及指定同一旋流初值、固定尺度 \(\delta\)、固定中心、完整周期压力和完整黏性方程。它否定的是这个中心最初正拉伸的解释，不排除其他位置、较晚时间、非径向形变、同一解的新结构或一般奇性。

全空间投影计算仅作为已经认证周期修正的主项。没有重选初值尺度、改黏性、改变环面或把单次中心压缩解释为长期动力学方向。没有宣称新颖性或超出这个有界合同的结论。
