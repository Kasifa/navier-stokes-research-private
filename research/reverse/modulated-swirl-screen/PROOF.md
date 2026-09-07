# 调制纯方位外环的角平均动量障碍

2026-09-08，PRIVATE_CORE。根代理解析推导，待非作者复核。合同为同目录 CONTRACT.md 的 MS.1–2；不改变物理初值。以下结论只检查同一个给定光滑 NS 解能否在非空时间区间内精确保持该局部轨道，不要求或断言这种表示曾经到达。

## 1. 固定圆柱几何和原对流源

采用合同的右手基 (e_r,e_θ,e_z)，e_z=e₂，r>0。固定旧外环写为

\[
W=w(r,z)e_\theta,\quad w=2r h'(s),\quad
s=(1/20)^2-r^2-(z-3/2)^2.
\]

因 ∂_θe_r=e_θ、∂_θe_θ=−e_r，其旋度为经向向量

\[
\Omega=\operatorname{curl}_yW
=\Omega_r e_r+\Omega_z e_z,
\quad \Omega_r=-\partial_z w,\quad
\Omega_z=r^{-1}\partial_r(rw).
\tag{MP.1}
\]

经向两系数不依赖 θ。完整对流项及其旋度为

\[
(W\cdot\nabla)W=-\frac{w^2}{r}e_r,\qquad
\operatorname{curl}((W\cdot\nabla)W)
=q(r,z)e_\theta,
\]
\[
q=-\partial_z(w^2/r)
=16r(z-3/2)h'(s)h''(s).
\tag{MP.2}
\]

在 r_*=1/40、z_*=61/40 的完整圆周上，s=1/800，故 q=q_* 为合同中的严格正数。具体地 h′=e^{-1/s}s^{-2}>0，h″=e^{-1/s}s^{-4}(1−2s)>0。该圆周离旧球心为 √2/40<1/20，离轴为正，所有求导均在光滑圆柱邻域内。这里复核了旧单点源项在全角圆周上的同一个数值表达式，没有选另一个诊断点。

## 2. 时间导数必须在固定物理坐标求取

记

\[
y=Q^T(x-c)/\ell,\quad K=Q^TQ',\quad
b=Q^Tc'/\ell,\quad \lambda=\ell'/\ell.
\]

K 为实反对称矩阵，可唯一写成 Kz=κ×z；κ、b 只依赖 t。
在固定 x 求导时

\[
\partial_ty=-b-Ky-\lambda y.
\tag{MP.3}
\]

MS.1 在开时空管恒成立，因此可在其内部同时求空间和时间导数。proper rotation 的旋度变换给

\[
\omega(t,x)=\operatorname{curl}_xu
=\frac A\ell Q\Omega(y).
\]

对上式在固定 x 求导，之后才代入测试圆周，得

\[
Q^T\partial_t\omega
=\left(\frac{A'}\ell-\frac{A\ell'}{\ell^2}\right)\Omega
 +\frac A\ell\{K\Omega-[(b+Ky+\lambda y)\cdot\nabla]\Omega\}.
\tag{MP.4}
\]

这不是沿移动圆周求涡量的全导数；MP.3 中的平移、转轴和尺度输运均保留。C¹ 参数只保证这些系数在每个实际时刻有限，没有使用小性或统一速率界。

## 3. 两个运动项的完整角平均

对固定 r,z，记 b_θ=b·e_θ、κ_r=κ·e_r、κ_z=κ·e_z。因为 Ω 为 MP.1 的轴对称经向场，

\[
[(b\cdot\nabla)\Omega]\cdot e_\theta
=\frac{b_\theta}r\Omega_r.
\tag{MP.5}
\]

只有圆柱基沿 θ 的导数产生方位分量。完整角积分满足 ∫b_θdθ=0，故平移项平均为零，包括任意轴向分量 b_z。

对转轴项，逐项叉积给

\[
(K\Omega)\cdot e_\theta=\kappa_z\Omega_r-\kappa_r\Omega_z,
\quad (Ky)\cdot e_\theta=\kappa_zr-\kappa_rz.
\]

代入同一基微分关系，得到

\[
\{K\Omega-[(Ky)\cdot\nabla]\Omega\}\cdot e_\theta
=\kappa_r\left(\frac z r\Omega_r-\Omega_z\right).
\tag{MP.6}
\]

轴向自转 κ_z 的两项精确相消；其它系数只含 κ_r=κ·e_r。因其全角均值为零，MP.6 的全角均值也为零。不能在单个角点省略这些运动项，结论使用的是完整圆周。

Ω 和 (y·∇)Ω 都没有方位分量；后者因 y=r e_r+z e_z，不沿角方向微分。结合 MP.4–6，即得

\[
\frac1{2\pi}\int_0^{2\pi}
e_\theta\cdot Q^T\partial_t\omega
(t,c+\ell Qy_\theta)\,d\theta=0.
\tag{MP.7}
\]

MP.7 的记号表示先对 ω 作物理时间偏导，再在括号所示点求值；积分中不再对 c、Q 或 y_θ 求导。

## 4. 完整黏性和压力下的残差

对轴对称经向向量，向量 Laplacian 仍为经向：

\[
\Delta\Omega
=\left(\partial_r^2+r^{-1}\partial_r+\partial_z^2-r^{-2}\right)\Omega_r\,e_r
 +\left(\partial_r^2+r^{-1}\partial_r+\partial_z^2\right)\Omega_z\,e_z.
\]

由此

\[
Q^T\operatorname{curl}_x\Delta_xu
=\frac A{\ell^3}\Delta_y\Omega
\tag{MP.8}
\]

的方位分量逐点为零。黏性系数保持原来的1，没有采用 Euler 极限。非线性则满足

\[
Q^T\operatorname{curl}_x((u\cdot\nabla_x)u)
=\frac{A^2}{\ell^2}\operatorname{curl}_y((W\cdot\nabla_y)W).
\tag{MP.9}
\]

完整压力无论由哪一周期胞或外部速度产生，都有 curl_x∇_xp=0。该恒等式只用压力作为标量的局部光滑性，不把非局部压力设为零，也不要求它轴对称。不对环面施加全局任意旋转对称；以上变换仅在已规定的周期提升时空管使用。

将 MP.2、MP.7–9 代入完整物理残差，严格得到

\[
\boxed{
\frac1{2\pi}\int_0^{2\pi}
Qe_\theta\cdot\operatorname{curl}_x\mathcal R
(t,c+\ell Qy_\theta)\,d\theta
=\frac{A^2}{\ell^2}q_*>0.}
\tag{MP.10}
\]

这就是 MS.2。其绝对值还不超过圆周上 |curl_x R| 的上确界，故给一个明确的残差旋度下界。如果 u 是真实无外力 NS 解，则 R 恒为零，矛盾。因此任何同一给定原解都不能在所规定的非空时间区间中满足 MS.1。

## 5. 这个拒绝改变了什么

旧固定形状的 C³ 持留障碍允许小误差，却没有覆盖任意转轴和平移。当前角平均障碍支付任意有限 C¹ 调制速度，但要求整个移动圆周开时空管中的真实总速度精确等于调制模板。两者的假设不同，不将当前结论冒称旧近似持留定理的全面加强。

本结果拒绝“只让原纯方位外环漂移、转轴、变幅或等向缩放，就成为真实轨道”的解释。它不限制仅在一个时刻的纯方位快照：单个快照没有给出 MP.4 所需的时间导数。在其它时刻生成经向速度或更一般形状是允许的；加局部应变、其它速度背景或非零形状误差均超出合同。

尤其不能以调制参数任意为由推到近似轨道。非零误差的运动导数会与调制速率耦合，本文没有这些项的统一界。没有得到近似轨道的有限持留时间、再进入次数、压力再生或稳定性。没有产生新初值或奇性候选；同一初值无限尺度、无限维跨代误差、统一迭代及有限总时间仍 OPEN / NOT CLAY。

## 6. 来源和实际阅读范围

根全文读旧 RESCALED_EXIT_PROOF，并定向读旧外场 PROOF 的 W 定义、JOINT_TEST_PROOF §6 的完整残差旋度与旧独立/包终审的调制边界。旧来源提供形状与 q_*；MP.3–7 是本项手工推导。合同 MS.2 的候选公式曾与 Rawls 交流，不冒称完全盲目独立发现。没有新科学程序、数组、参数扫描、外部定理或新颖性声明。

| 旧来源（相对 research/reverse/） | SHA256 |
|---|---|
| exterior-pressure/PROOF.md | 50df7a60076567acac9cbad6588132c3e0f49e77f84f17ee68e740a8a32478b9 |
| exterior-pressure/JOINT_TEST_PROOF.md | 9d0100f62ec6ef25ef2552348120d2b7b1e802aba49167bf4115edad02a3cd91 |
| exterior-pressure/RESCALED_EXIT_PROOF.md | e96f1bce6d2076d560191211e208bd43f33e0db2d5c21de8abc6dfd31b361e78 |
| exterior-pressure/RESCALED_EXIT_REVIEW.md | d9b29618ec836e0d3ea3a63fde0888db59add6b289dc7900c84a0e748601a0d6 |
| exterior-pressure/FINAL_PACKAGE_REVIEW.md | 959758e9026f6a948b76e516e008bc18d726df9035ec6bf0993dce9b7d19d3a2 |
