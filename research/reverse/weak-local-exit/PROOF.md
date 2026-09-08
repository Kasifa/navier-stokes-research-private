# 从局部速度 L² 误差得到固定外形状的持留上界

2026-09-08，PRIVATE_CORE。合同后的主推导；独立推导和非作者审查完成前不接纳。以下只使用既有光滑 NS 原解的方程。L² 是强范数条件，不是仅有弱收敛。

## 1. 固定输入和全测试支撑的符号

沿用合同的 T*、重标坐标、B*、V 和 b₂。所有积分为 y 的未归一化 Lebesgue 积分。记 a=3/5、b=2/5、κ(s)=e^(−s/5)；a、b 是坐标系数，不是新初值或旧外壳权重。

\[
F_s+aF+b(y\cdot\nabla)F-\kappa\Delta F
 +(F\cdot\nabla)F+\nabla P=0,\qquad\operatorname{div}F=0.
\tag{WL.1}
\]

取任意一份事先固定 χ∈C_c^∞(B*)，χ≥0 且不恒零，不在本文指定函数实例。令

\[
\phi=\chi e_\theta,\qquad \Psi=\operatorname{curl}\phi.
\tag{WL.2}
\]

B* 的闭包远离轴线，故这两函数可光滑地零延拓，均紧支撑于 B*，且 div Ψ=0；不要求 χ 轴对称，也不要求 φ 无散。

在 B* 上，r 和 ζ=z−3/2 均大于 1/40−1/400=9/400。到第二壳中心的距离小于 √2/40+1/400<1/20。因此

\[
0<\sigma=(1/20)^2-r^2-\zeta^2<(1/20)^2<1/2.
\]

这个球与另外两壳支撑分离，V=√b₂ w e_θ，w=2r h'(σ)。旧柱坐标公式在整个球直接给出

\[
e_\theta\cdot\operatorname{curl}((V\cdot\nabla)V)
=b_2[-\partial_z(w^2/r)]
=16b_2r\zeta h'(\sigma)h''(\sigma)>0.
\tag{WL.3}
\]

其中 h'=e^(−1/σ)σ^(−2)>0、h''=e^(−1/σ)σ^(−4)(1−2σ)>0。定义

\[
Q_\chi=\int_{B_*}\chi\,16b_2r\zeta h'(\sigma)h''(\sigma)\,dy>0.
\tag{WL.4}
\]

严格正性来自整个测试支撑上的符号和非零非负 χ；没有把旧单点 q* 当作同一个积分常数。Qχ 有限，不给未经验证的数值。

## 2. 压力消去与真实弱测试恒等式

固定观察量

\[
m(s)=\int_{B_*}F(s,y)\cdot\Psi(y)\,dy.
\tag{WL.5}
\]

测试支撑须位于原解当前的重标局部坐标域；这是合同前提。F 光滑，所以可直接微分 m。紧支撑使全部分部积分无边界项。完整周期压力贡献为 −∫∇P·Ψ=∫P div Ψ=0，不要求 P 小或只由局部 V 产生。

取张量约定 (∇Ψ)_ij=∂jΨ_i。完整方程给

\[
m'(s)=\int F\cdot H_\kappa
 +\int(F\otimes F):\nabla\Psi,
\quad
H_\kappa=(3b-a)\Psi+b(y\cdot\nabla)\Psi+\kappa\Delta\Psi.
\tag{WL.6}
\]

这里 3b−a=3/5=a。对流分部积分使用真实 div F=0；E 的导数没有出现在 WL.6 中。黏性项保留为 κ∫F·ΔΨ，而不是令 κ=0。

V 在 B* 是轴对称纯方位速度。curl V、curl((y·∇)V) 和 curl ΔV 均是经向向量，与 eθ 正交。因而 curl 的分部积分以及紧支撑给

\[
\int V\cdot\Psi=0,\qquad
\int V\cdot H_\kappa=0
\quad\hbox{对每个实际 }\kappa,
\tag{WL.7}
\]

\[
\int(V\otimes V):\nabla\Psi
=-\int((V\cdot\nabla)V)\cdot\operatorname{curl}\phi
=-Q_\chi.
\tag{WL.8}
\]

例如漂移项可先写成 −∫[aV+b(y·∇)V]·Ψ 再取 curl；χ 不轴对称不会改变经向与方位的逐点正交。以上只在测试支撑内使用 V 的形状，不把整个 V 当作 NS 轨道。

## 3. 仅以 L² 控制全部余项

在 B* 上令 E=F−V，定义有限常数

\[
J_\chi=\|\Psi\|_2,\quad M=\|V\|_2,\quad
G_\chi=\sup_{B_*}|\nabla\Psi|_F,
\]
\[
H_\chi=\|a\Psi+b(y\cdot\nabla)\Psi\|_2
       +\|\Delta\Psi\|_2,
\quad
L_\chi=1+H_\chi+G_\chi(2M+1)>0.
\tag{WL.9}
\]

Ψ 不恒零：若 Ψ=0，WL.8 会强迫 Qχ=0，与 WL.4 矛盾。因此 Jχ>0。各测试范数可依赖已经固定的 χ，不声称它们对任意缩窄支撑统一。

s≥log100 保证 0<κ≤1。若 ||E||₂≤ε≤1，Cauchy–Schwarz 和 Frobenius 张量估计给

\[
\left|\int E\cdot H_\kappa\right|\le H_\chi\varepsilon,
\]
\[
\left|\int[F\otimes F-V\otimes V]:\nabla\Psi\right|
\le G_\chi(2M\varepsilon+\varepsilon^2)
\le G_\chi(2M+1)\varepsilon.
\tag{WL.10}
\]

展开中保留 E⊗V、V⊗E 和 E⊗E。无需 E 的一至三阶导数、时间导数或压力误差估计。于是

\[
|m(s)|\le J_\chi\varepsilon,\qquad
m'(s)\le-Q_\chi+L_\chi\varepsilon.
\tag{WL.11}
\]

## 4. 有界条件定理和适用范围

对上述任意预先固定 χ，取符号范围

\[
0<\varepsilon\le\min\{1,Q_\chi/(2L_\chi)\}.
\tag{WL.12}
\]

若同一光滑原解的重标速度在整个区间 [s₀,s₁]、s₀≥log100 中持续满足

\[
\|F(s,\cdot)-V\|_{L^2(B_*)}\le\varepsilon,
\tag{WL.13}
\]

则 m'≤−Qχ/2，同时 |m|≤Jχε。积分得到

\[
-2J_\chi\varepsilon\le m(s_1)-m(s_0)
\le-\tfrac12Q_\chi(s_1-s_0),\qquad
\boxed{s_1-s_0\le4J_\chi\varepsilon/Q_\chi.}
\tag{WL.14}
\]

ε=0 时，若区间正长则 m 恒零与 WL.6–8 矛盾，因此精确保持同样不可能。对有限开区间，可在其任意紧子区间使用同一界；不假设未知奇性端点处的时间迹。

这项条件结论把旧固定坐标、固定形状的空间邻域从 C³ 降为局部速度 L²。即使扰动含未控高阶导数，固定紧支撑动量测试仍迫使有限时间离开。它不是任意调制轨道定理，也不限制离开后的再进入次数或累计停留。没有从 L² 范数给出逐点涡量符号，没有推广到仅弱 L² 收敛或未付时间迹的弱解。

未选择实际 χ、ε、进入时刻、频率或新初值，未作科学程序、数组、求值或扫描。未证明原解到达这个邻域、其它非定常形状被排除、局部供给可迭代、全局正则或奇性；旧失败证据不变。已有外壳、重标方程和 q 公式的来源仍归旧文本，本项不主张文献新颖性。NO-CANDIDATE；NOT CLAY。
