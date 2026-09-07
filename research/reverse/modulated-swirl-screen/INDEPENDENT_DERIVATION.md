# 平移、转轴和缩放纯方位形状的独立推导

2026-09-08，PRIVATE_CORE。结论：**在合同 MS.1 的精确开时空管假设下，MS.2 成立，因而该精确局部形状族不能在非空开时间区间内成为真实 NS 轨道。**

本作者未读本目录根代理的 PROOF，也未参与其正文写作。以下由合同、旧 JOINT_TEST_PROOF §6 及 RESCALED_EXIT_REVIEW 的边界独立重推。只作解析，不运行数值程序、读取新数组、选择参数或修改初值；根正文的最终非作者审查仍另作，本文不预先替它签核。

## 1. 坐标、形状和精确局部意义

严格使用合同右手基
\[
e_z=e_2,\quad e_r(\theta)=(\cos\theta,0,-\sin\theta),\quad
e_\theta(\theta)=(-\sin\theta,0,-\cos\theta).
\]
所以 \(e_r\times e_\theta=e_z\)，\(\partial_\theta e_r=e_\theta\)。
写 \(y=r e_r+z e_z\)，令
\[
\zeta=z-\frac32,\quad
s=\frac1{400}-r^2-\zeta^2,\quad
w(r,z)=2r h'(s).
\]
由 \(W=\operatorname{curl}_y(\psi e_z)\)，
\[
W=w e_\theta,\qquad
\Omega:=\operatorname{curl}_y W=F e_r+G e_z,
\]
\[
F=-w_z=4r\zeta h''(s),\qquad
G=\frac1r(rw)_r=4h'(s)-4r^2h''(s).
\tag{ID.1}
\]
这些函数不依赖 \(\theta\)。测试圆 \(r_*=1/40,z_*=61/40\) 满足
\(r_*>0\)、\(s_*=1/800>0\)，在旧球内部并远离轴，圆柱微分不存在轴上奇性。

在选定周期提升的开时空管内使用
\[
y=Q(t)^T(x-c(t))/\ell(t),\qquad u=A(t)Q(t)W(y).
\]
这里是完整总速度的局部精确恒等式，不是只写某个分量或叠加项。
开时空管保证在每个测试点附近能同时取空间导数和**固定物理 x**的时间导数。
若只有移动圆周上或单个时刻的速度取值，下面的时间导数代入便没有依据。

## 2. 固定物理 x 的旋度时间导数

定义体坐标中的全部调制速度
\[
S=Q^TQ'\in\mathfrak{so}(3),\quad Sv=\omega\times v,\qquad
b=Q^Tc'/\ell,\qquad a_\ell=\ell'/\ell.
\]
\(\omega,b,a_\ell\) 在每个固定时刻均与 y 无关；不对它们作小性、符号或统一大小假设。
由 \(Q'=QS\)、\((Q^T)'=-SQ^T\)，固定 x 求导得到
\[
y_t\big|_x=-Sy-b-a_\ell y.
\tag{ID.2}
\]
任意时刻的 proper rotation 与缩放给
\[
\operatorname{curl}_x u=\frac A\ell Q\Omega(y).
\]
在固定 x 处对这条等式求时间导数，并使用空间/时间微分交换，得到完整公式
\[
\begin{aligned}
Q^T\operatorname{curl}_x u_t
=\frac A\ell\bigg[
&\left(\frac{A'}A-a_\ell\right)\Omega
+S\Omega-(Sy\cdot\nabla_y)\Omega\\
&-(b\cdot\nabla_y)\Omega
-a_\ell(y\cdot\nabla_y)\Omega
\bigg].
\end{aligned}
\tag{ID.3}
\]
只需 \(A,\ell,c,Q\) 为 C¹、\(A,\ell>0\)；没有出现二阶调制导数。

直接对“移动点上的方位旋度等于零”求导会混入点与方向的运动，
不能据此删掉 ID.3。ID.2–3 先完成固定物理点求导，之后才代入 \(y_\theta\)，
已经保留转轴、平移和伸缩产生的所有输运项。

## 3. 平移和转轴项的整圆平均

对任意在 y 上恒定的向量 v，轴对称经向场 \(\Omega=F e_r+G e_z\) 满足
\[
e_\theta\cdot(v\cdot\nabla)\Omega
=\frac F r(v\cdot e_\theta).
\tag{ID.4}
\]
因为 \(v\cdot\nabla=v_r\partial_r+(v_\theta/r)\partial_\theta+v_z\partial_z\)，
只有 \(\partial_\theta(F e_r+G e_z)=F e_\theta\) 对方位分量有贡献。
故平移项的方位分量为
\[
-e_\theta\cdot(b\cdot\nabla)\Omega
=-\frac F r(b\cdot e_\theta).
\tag{ID.5}
\]

对转轴项，令 \(\omega_r=\omega\cdot e_r,\omega_z=\omega\cdot e_z\)。
右手基给
\[
e_\theta\cdot S\Omega=\omega_zF-\omega_rG,\qquad
e_\theta\cdot Sy=\omega_zr-\omega_rz.
\]
径向和轴向对 \(\Omega\) 求导均不产生方位分量，因而
\[
e_\theta\cdot\big[S\Omega-(Sy\cdot\nabla)\Omega\big]
=(\omega\cdot e_r)\left(\frac{zF}{r}-G\right).
\tag{ID.6}
\]
这里用的是体坐标 \(z\)，**不是**球心偏移 \(\zeta\)：
旋转 \(Sy\) 围绕所定义的坐标原点，球心运动也已包含在完整公式中。
沿 \(e_z\) 的自转项 \(\omega_zF\) 精确抵消；其余转轴项一般不逐点为零。

\(\Omega\) 与 \((y\cdot\nabla)\Omega=(r\partial_r+z\partial_z)\Omega\)
均为经向场，因此 ID.3 中的幅度变化及伸缩项的方位分量逐点为零。
合并剩余项，
\[
(Qe_\theta)\cdot\operatorname{curl}_x u_t
=\frac A\ell
\left[
(\omega\cdot e_r)\left(\frac{zF}{r}-G\right)
-\frac F r(b\cdot e_\theta)
\right].
\tag{ID.7}
\]
在同一 \(r,z\) 的完整圆周上，F、G不随角变化，且
\[
\int_0^{2\pi}e_r(\theta)\,d\theta
=\int_0^{2\pi}e_\theta(\theta)\,d\theta=0.
\]
所以 ID.7 的整圆平均精确为零。没有用调制速度小或舍弃大项；
用到的是完整圆周与第一角谐波相消。

## 4. 黏性、完整压力及对流源项

黏性没有被置零。旋度与 Laplacian 交换，给
\[
Q^T\operatorname{curl}_x(-\Delta_xu)
=-\frac A{\ell^3}\Delta_y\Omega,
\]
而轴对称经向场的向量 Laplacian 为
\[
\Delta_y\Omega
=(\partial_r^2+r^{-1}\partial_r+\partial_z^2-r^{-2})F\,e_r
+(\partial_r^2+r^{-1}\partial_r+\partial_z^2)G\,e_z.
\tag{ID.8}
\]
故其方位配对逐点为零；这是黏性1的完整项在所选分量上的结构消去。

真实周期压力可来自管外任意速度，局部恒有
\(\operatorname{curl}_x\nabla_xp=0\)。这使用完整压力的梯度结构，
不需压力轴对称、局域化或近似；管外压力贡献未删除。

在固定时刻，局部空间协变性给
\[
(u\cdot\nabla_x)u
=\frac{A^2}{\ell}Q[(W\cdot\nabla_y)W].
\]
纯方位轴对称 W 的对流为
\[
(W\cdot\nabla)W=-\frac{w^2}{r}e_r,\qquad
\operatorname{curl}_y[(W\cdot\nabla)W]
=q(r,z)e_\theta,
\]
\[
q(r,z)=-\partial_z(w^2/r)
=16r\zeta h'(s)h''(s).
\tag{ID.9}
\]
因此其物理旋度方位分量是 \(A^2\ell^{-2}q(r,z)\)，不是 \(A^2/\ell\)：
第二个逆尺度来自外层旋度。

由 ID.7–9，可得比平均式更完整的点公式
\[
\begin{aligned}
&(Qe_\theta)\cdot
\operatorname{curl}_x\mathcal R(t,c+\ell Qy)\\
&\quad=\frac{A^2}{\ell^2}q(r,z)
+\frac A\ell\left[
(\omega\cdot e_r)\left(\frac{zF}{r}-G\right)
-\frac F r(b\cdot e_\theta)
\right].
\end{aligned}
\tag{ID.10}
\]
所有量均在同一物理时刻取值。这一公式没有省去任何调制导数或压力/黏性项；
已经为零的项由前面的精确结构给出。

## 5. 测试圆、正号和真实解矛盾

在测试圆上，
\[
r=\zeta=\frac1{40},\quad
s=\frac1{400}-\frac1{1600}-\frac1{1600}=\frac1{800},
\]
所以
\[
q(r_*,z_*)=\frac1{100}h'(1/800)h''(1/800)=q_*.
\]
对 \(0<s<1/2\)，
\[
h'(s)=e^{-1/s}s^{-2}>0,\qquad
h''(s)=e^{-1/s}s^{-4}(1-2s)>0,
\]
因此 \(q_*>0\)，无需求其数值。
ID.10 对整圆平均，第一谐波精确消去，得到
\[
\boxed{\;
\frac1{2\pi}\int_0^{2\pi}(Qe_\theta)\cdot
\operatorname{curl}_x\mathcal R(t,c+\ell Qy_\theta)\,d\theta
=\frac{A(t)^2}{\ell(t)^2}q_*>0.
\;}
\tag{ID.11}
\]
这正是合同 MS.2。

对真实无外力 NS 解，\(\mathcal R=0\) 于其光滑存在区间，左端必须为零。
任取非空开区间 J 内的时刻即有矛盾。因此不存在满足合同全部前提的精确局部调制轨道。
不需要 J 的最小长度、统一幅度下界或调制速度上界；每个时刻的 \(A,\ell>0\) 已足够。

## 6. 周期与时间范围

本证明只在合同允许的局部周期提升中求导。可将原周期解提升到 \(\mathbb R^3\)，
沿给定 \(c+\ell Qy_\theta\) 的各局部开邻域计算并按同一提升配对。
任意 proper rotation 的 curl/Laplacian 协变性是局部欧氏恒等式，
不要求 \(Q\mathbb Z^3=\mathbb Z^3\)，也没有把变换后的全空间场当成另一份全环面 NS 解。

若某组调制不能提供合同要求的开时空管/相容周期提升，则它不满足 MS.1 的前提；
本推导不额外替它建立全域周期拼接。管外速度任意，但总速度必须在测试管内精确等于所给式子。
不添加平移速度 \(c'\)、经向场或背景应变到 u；它们若作为实际速度项加入，已是不同合同。

单时刻经过这个空间形状并未被排除：仅有一个快照不能确定 ID.3 的时间导数，
真实动力学可以立即产生超出该形状族的运动。本文不控制近似轨道的持留时间、
再次进入、其它时刻或带经向分量的非定常剖面。
尤其 \(C^3\) 小误差不等于误差恒零；若另议近似调制族，
调制速度与误差的乘积须另立余项合同，本稿不作这种延伸。

旧 RESCALED_EXIT_REVIEW 针对固定重标剖面的一个 C³邻域及单次连续持留；
其明确未覆盖平移/转轴。本文新增的箭头是**精确形状、任意C¹有限维调制**
在整圆平均中的动量障碍，不将旧持留时间结论自动搬来。
它不证明原固定初值达到此族，也不证明全局性、奇性、统一再生或有限总时间机制。
无新颖性、完整研究冻结或发布声明。

## 7. 实际输入绑定

| 实际读取范围（路径相对 research/reverse/） | SHA256 |
|---|---|
| modulated-swirl-screen/CONTRACT.md，全文 | 147e3a624a620f71792f9610fa779c09ed5d877c791fda922d0ca445ab41cf02 |
| exterior-pressure/JOINT_TEST_PROOF.md，§6及结论边界 | 9d0100f62ec6ef25ef2552348120d2b7b1e802aba49167bf4115edad02a3cd91 |
| exterior-pressure/RESCALED_EXIT_REVIEW.md，全文 | d9b29618ec836e0d3ea3a63fde0888db59add6b289dc7900c84a0e748601a0d6 |

没有读取本目录根 PROOF，未读取上述文档链接的计算数组或运行程序。
所有符号、尺度及小整数恒等式在本文手推列出；工具仅用于文本读取、SHA与写本文件。

