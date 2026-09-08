# 同一原解的能量界与固定形状的离开时间占比

2026-09-08，PRIVATE_CORE。合同后主推导，待独立推导和非作者审查。积分与时间占比都在固定重标坐标中，不是普通物理时间比例。

## 1. 周期胞的真实能量缩放

u₀ 在原解之前已经固定。令 U*=||u₀||_(L²(T³))，使用未归一化 Lebesgue 测度。光滑、周期、无外力、黏性一的完整 NS 给

\[
\frac12\frac{d}{dt}\int_{\mathbb T^3}|u|^2
+\int_{\mathbb T^3}|\nabla u|^2=0.
\tag{LO.1}
\]

由动量与 u 配对即可验证：周期对流项等于 ∫div(u|u|²/2)=0，压力项等于 ∫div(pu)=0，黏性分部积分给耗散；没有使用旧 NON-NS 负对照的能量路径。

令 τ=T*−t、d=τ^(2/5)、F=τ^(3/5)u(t,dy)。取基本胞 Cτ=[−π/d,π/d]³，并由 dx=d³dy 得

\[
\int_{C_\tau}|F(s,y)|^2dy
=\tau^{6/5}d^{-3}\int_{\mathbb T^3}|u(t,x)|^2dx
=\|u(t)\|_2^2\le U_*^2.
\tag{LO.2}
\]

这正是旧外尺度的能量临界缩放，而不是假定局部重标能量无条件受控。s≥log100 时 d<1，B* 包含在 Cτ 内，故 ||F||_(L²(B*))≤U*。不必对移动胞求时间导数。

记 M=||V||_(L²(B*))>0、D=U*+M>0、

\[
e(s)=\|F(s)-V\|_{L^2(B_*)},\qquad 0\le e(s)\le D.
\tag{LO.3}
\]

这里不要求 e 小，也不把 U* 当作可调参数。若 u₀=0，U*=0 仍允许使用以下全部非除法估计。

## 2. 固定测试的完整动量预算

固定任意允许 χ≥0、χ≢0，φ=χeθ、Ψ=curlφ，定义

\[
Q=16b_2\int_{B_*}\chi r(z-3/2)h'(\sigma)h''(\sigma)dy>0,
\quad\sigma=(1/20)^2-r^2-(z-3/2)^2.
\tag{LO.4}
\]

为使推导不依赖正在审查的新稿，这里重新核所需结构。在整个 B*，r,z−3/2>9/400，距第二壳中心小于 √2/40+1/400<1/20，所以 0<σ<1/2，h'、h''>0，V=√b₂w eθ。纯方位对流的旋度方位分量为 −b₂∂z(w²/r)=16b₂r(z−3/2)h'h''，故 Q>0。

φ、Ψ 都紧支撑且光滑，div Ψ=0。固定形状的 V、(y·∇)V、ΔV 是纯方位场，它们的旋度与 φ 垂直，所以对应动量线性测试为零。完整方程在真实 s 区间为

\[
F_s+\tfrac35F+\tfrac25(y\cdot\nabla)F
-\kappa(s)\Delta F+(F\cdot\nabla)F+\nabla P=0,
\quad\kappa=e^{-s/5}.
\]

取 m(s)=∫F·Ψ=∫(F−V)·Ψ。紧支撑分部积分、真实 divF=0 和 divΨ=0 给

\[
\begin{split}
m'(s)=-Q
&+\int E\cdot\left[\tfrac35\Psi+\tfrac25(y\cdot\nabla)\Psi
                    +\kappa\Delta\Psi\right]\\
&+\int(E\otimes V+V\otimes E+E\otimes E):\nabla\Psi,
\qquad E=F-V.
\end{split}
\tag{LO.5}
\]

取 (∇Ψ)_ij=∂jΨ_i。漂移的正 3/5 来自 −3/5+3(2/5)。压力精确配对为零，无论它来自哪一壳或周期远场。黏性保留正的 κ∫E·ΔΨ。非线性固定项为 −∫curl((V·∇)V)·φ=−Q。

定义有限常数

\[
J=\|\Psi\|_2>0,\quad G=\sup_{B_*}|\nabla\Psi|_F,
\quad H=\|\tfrac35\Psi+\tfrac25(y\cdot\nabla)\Psi\|_2
          +\|\Delta\Psi\|_2,
\]
\[
C=1+H+G(2M+D)>0.
\tag{LO.6}
\]

J>0 可由 Q>0 和固定非线性配对推出，不能将一个 curl 为零的测试当作正探针。κ≤1，故只需局部速度误差即可得

\[
|m'(s)+Q|\le H e(s)+G(2Me(s)+e(s)^2)\le C e(s).
\tag{LO.7}
\]

第二步使用同一原解全域能量给出的 e≤D；完整 E⊗E 未丢弃。端点不是近邻端点，无需 e 小，直接由 LO.2 得

\[
|m(s)|\le JU_*.
\tag{LO.8}
\]

## 3. 时间积分与占比必要界

在任意实际光滑区间 [s₀,s₁]、s₀≥log100，记 ℓ=s₁−s₀>0。积分 LO.7 的上侧给

\[
m(s_1)-m(s_0)\le-Q\ell+C\int_{s_0}^{s_1}e(s)ds.
\]

两个实际端点由 LO.8 付出至多 2JU*，因此

\[
\boxed{\int_{s_0}^{s_1}e(s)ds
\ge\max\left\{0,\frac{Q\ell-2JU_*}{C}\right\}.}
\tag{LO.9}
\]

这不要求原解在区间内始终接近 V。对任意符号容限

\[
0\le\delta<\min\{D,Q/C\},\qquad
\mathcal B_\delta=\{s\in[s_0,s_1]:e(s)>\delta\},
\tag{LO.10}
\]

e 连续，故该集合可测。以 |·| 表示 s 的 Lebesgue 测度，LO.3 给

\[
\int e\le\delta\ell+(D-\delta)|\mathcal B_\delta|.
\]

与 LO.9 结合得

\[
\boxed{
|\mathcal B_\delta|\ge
\max\left\{0,
\frac{(Q-C\delta)\ell-2JU_*}{C(D-\delta)}\right\}.}
\tag{LO.11}
\]

只除已证正的 C 和 D−δ。这里没有把 e 的时间平均换成逐时小性，也没有把高频导数控制藏进测度估计。时间集合可以有任意多连通分支。

若同一原解在全部 0≤t<T* 光滑，固定任意 s₀≥log100 后可令 s₁→∞。这是假设实际存在到 T* 的条件结论，不是新延拓定理。于是

\[
\liminf_{s_1\to\infty}\frac1\ell\int_{s_0}^{s_1}e(s)ds\ge Q/C>0,
\]
\[
\boxed{\liminf_{s_1\to\infty}
\frac{|\mathcal B_\delta|}{\ell}
\ge\frac{Q/C-\delta}{D-\delta}>0.}
\tag{LO.12}
\]

常数可依赖这个固定初值、固定旧 V 和固定 χ，不是跨数据族的统一阈值。没有选择 δ 的数值。若终端实际光滑存在假设不足，只保留有限区间 LO.9–11。

## 4. 物理时间解释与边界

重标时间满足 ds=dt/(T*−t)。因此 LO.11 的分子时间测度在物理坐标中是

\[
|\mathcal B_\delta|
=\int_{\{t\in[t_0,t_1]:e(-\log(T_*-t))>\delta\}}
\frac{dt}{T_*-t},
\quad
\ell=\log\frac{T_*-t_0}{T_*-t_1}.
\tag{LO.13}
\]

它不是普通 dt 的比例。LO.12 排除该固定形状在终端全部对数时间上平均接近，也排除其足够小邻域占满渐近时间密度；相邻访问之间不能总以可忽略的对数时间纠正测试量。

这并不限制再进入次数，不给近邻累计对数时间的绝对有限上界；近邻仍可能占一个正但不足一的比例。它也不排除不同非定常形状组成的动态路线、任意快速调制、别的外尺度或局部结构。原解可能根本从未接近 V，本定理不保证到达或生成。

全过程保持同一个固定初值及其实际能量，不把不同解、时间窗口或外场重置后拼接。未用 Euler 替代黏性 NS，未证明弱解的时间迹、无限尺度再生成、统一余项、有限总时间奇性或全局正则。没有科学程序、数组、数值选参或修复旧失败；不声称文献新颖性。NO-CANDIDATE；NOT CLAY。
