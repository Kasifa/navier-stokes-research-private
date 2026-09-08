# 固定外形状的一次连续局部 L² 持留界

2026-09-08，PRIVATE_CORE。独立有界手工证明，待非作者审查和根比较。

**合同及形成历史。** 本次先全文读取 CONTRACT.md。合同已披露根在锁定正式合同前预检过紧支撑旋度测试及分部积分的路径；本稿没有收到其具体新公式或常数，未读本目录 PROOF.md、review 或另一新推导。这里的独立性仅针对本项正式推导，不冒称根在合同前没有数学预检。

**结论。** 在同一旧固定形状 V、固定球 B* 和固定重标坐标中，只需真实速度扰动在整个一次连续区间的局部 L² 范数小，便可给出显式有限持留界。压力精确消去；黏性和漂移保留；完整二次误差按 L² 范数的平方支付。没有假设扰动的空间导数或时间导数小。

本证明只针对既已固定初值的实际光滑 NS 解及其实际存在区间，不构造新初值，不选择一个实际测试 χ、误差 ε 或进入时间。全部为一般手工符号与文本/哈希操作；无科学程序、数组、数值求值、扫描、Git、发布或外部消息。

## 1. 实际来源和旧固定输入

路径相对于 research/reverse/。三份文本本轮均实际全文读取；表中列明使用段落，内部转引不计为本轮实读。

| 来源与使用范围 | SHA-256 |
|---|---|
| weak-local-exit/CONTRACT.md，先全文读取 | 2eba0d26399480d98c1d29e288b0f1726b33ca14dc103092936e20749689664f |
| exterior-pressure/RESCALED_EXIT_PROOF.md，全文；使用第 1、3 节的完整重标方程与旧局部形状，以及第 5 节范围 | e96f1bce6d2076d560191211e208bd43f33e0db2d5c21de8abc6dfd31b361e78 |
| exterior-pressure/JOINT_TEST_PROOF.md，全文；使用第 1 节 V、b2 的固定定义和第 6 节右手柱坐标计算 | 9d0100f62ec6ef25ef2552348120d2b7b1e802aba49167bf4115edad02a3cd91 |

JOINT_TEST 的辅助路径已明确不是 NS 解。本文只使用其中已定义的静态 V 和 b2>0，不把该路径作为真实原解。旧权重没有在本稿重新选择或数值化。

令 u 是合同的同一条黏性 1、无外力、三维 2π 环面上的真实光滑解。在其实际存在且 0≤t<T*=1/100 的区间设
\[
\tau=T_*-t,\quad s=-\log\tau,\quad d=\tau^{2/5},
\quad F(s,y)=\tau^{3/5}u(T_*-\tau,dy).
\]
完整周期压力重标为 \(P(s,y)=\tau^{6/5}p(T_*-\tau,dy)\)。为核清系数，将 \(u=\tau^{-3/5}F\) 代入原方程：时间导数为
\(\tau^{-8/5}\{F_s+(3/5)F+(2/5)(y\cdot\nabla)F\}\)，
黏性项为 \(\tau^{-7/5}\Delta F\)，对流和压力梯度都带 \(\tau^{-8/5}\)。于是正是旧源的完整方程
\[
F_s+\frac35F+\frac25(y\cdot\nabla)F
-\nu(s)\Delta F+(F\cdot\nabla)F+\nabla P=0,
\quad \operatorname{div}F=0,\quad \nu(s)=e^{-s/5}.
\tag{WLI.1}
\]
只在 s≥log100 的实际存在区间使用它；因而
\[
0<\nu(s)\le\nu_*:=100^{-1/5}.
\]
这不是把黏性系数置零。以下所有空间量都在 y 坐标中，测试球和测试函数不随 s 移动。

旧固定球为
\[
y_*=(1/40,61/40,0),\qquad
B_*=B_{1/400}(y_*).
\tag{WLI.2}
\]
它处于重标周期域的内部坐标图中。由于 d≤1，重标基本周期胞只会扩张；B* 的闭包已位于 (-2,2)³ 内，紧支撑测试可在该胞中延拓为零，不产生周期胞边界项。

## 2. 在整个 B* 上重新核正号

绕 e2 轴使用旧右手柱坐标
\[
r=\sqrt{y_1^2+y_3^2},\quad z=y_2,\quad
\zeta=z-\frac32,\quad
\varsigma=\frac1{400}-r^2-\zeta^2.
\]
在 y3=0、y1>0 处为 er=e1、eθ=−e3、ez=e2。对 B* 中每一点，径向距离的 Lipschitz 性及球半径给
\[
\frac9{400}<r<\frac{11}{400},\qquad
\frac9{400}<\zeta<\frac{11}{400}.
\]
故
\[
0<\frac{79}{80000}<\varsigma<\frac1{400}<\frac12.
\tag{WLI.3}
\]
下界来自 \(r^2+\zeta^2<2(11/400)^2\)。同样的非严格坐标界在闭包上仍给严格正的 \(\varsigma\) 下界。特别地，整个闭球位于第二旧外壳的内部，且不接触柱坐标轴。其它两壳在此为零，故这里确有
\[
V=\sqrt{b_2}\,w(r,z)e_\theta,\quad
w=2r h'(\varsigma),\quad h(v)=e^{-1/v}\ (v>0).
\tag{WLI.4}
\]

直接微分旧函数：
\[
h'(v)=e^{-1/v}v^{-2}>0,\qquad
h''(v)=e^{-1/v}v^{-4}(1-2v)>0\quad(0<v<1/2).
\]
纯轴对称方位速度的对流是
\[
(V\cdot\nabla)V=-b_2\,\frac{w^2}{r}e_r.
\]
在右手基中，其旋度的方位分量为
\[
\boxed{
\operatorname{curl}((V\cdot\nabla)V)\cdot e_\theta
=-b_2\partial_z(w^2/r)
=16b_2r\zeta h'(\varsigma)h''(\varsigma)>0
\quad\text{在整个 }B_*.}
\tag{WLI.5}
\]
这里 \(\partial_z\varsigma=-2\zeta\)，所以对流前面的负号和该导数负号相乘得到正号。WLI.3–5 重新支付整个球上的符号，未把旧中心一点的正数直接当作全球正号。

## 3. 任意固定 χ 的紧支撑无散测试

固定合同允许的任意
\[
0\le\chi\in C_c^\infty(B_*),\quad \chi\not\equiv0,\qquad
\phi=\chi e_\theta,\quad \psi=\operatorname{curl}\phi.
\tag{WLI.6}
\]
没有在本文选取一个实际 χ。由于支撑离轴，φ、ψ 都是光滑紧支撑场，且 divψ=0。即使 χ 依赖方位角，也准确有
\[
\boxed{\psi=-\partial_z\chi\,e_r+
(\partial_r\chi+\chi/r)e_z.}
\tag{WLI.7}
\]
方位导数没有给出新的方位分量；该式也可由
\(\nabla\chi\times e_\theta+\chi\operatorname{curl}e_\theta\)
逐项核出。因此 ψ 处处垂直于 eθ。

定义固定严格正积分
\[
\boxed{
Q_\chi=
16b_2\int_{B_*}\chi\,r\zeta
h'(\varsigma)h''(\varsigma)\,dy>0.}
\tag{WLI.8}
\]
正性来自 WLI.5 和非负非零光滑 χ；有限性来自紧支撑上的已知光滑性。利用紧支撑旋度分部积分，
\[
\int_{B_*}(V\cdot\nabla)V\cdot\psi\,dy=Q_\chi.
\tag{WLI.9}
\]
特别地 ψ 不可能恒为零，因而 \(N_\chi:=\|\psi\|_{L^2(B_*)}>0\)。

V、(y·∇)V 和 ΔV 在 B* 都是纯方位向量。具体地，
\[
(y\cdot\nabla)V=\sqrt{b_2}(r\partial_r+z\partial_z)w\,e_\theta,
\]
\[
\Delta V=\sqrt{b_2}
(\partial_r^2+r^{-1}\partial_r+\partial_z^2-r^{-2})w\,e_\theta.
\]
由于 ψ 为经向，准确有
\[
\int V\cdot\psi=\int (y\cdot\nabla)V\cdot\psi
=\int\Delta V\cdot\psi=0.
\tag{WLI.10}
\]
积分均在 B*。这些是固定 V 的结构恒等式，不是对实际 F 的方位或轴对称假设。

## 4. 真实动量恒等式及仅 L² 的余项

令 E=F−V，并定义固定测试量
\[
J(s)=\int_{B_*}F(s,y)\cdot\psi(y)\,dy
=\int_{B_*}E(s,y)\cdot\psi(y)\,dy.
\tag{WLI.11}
\]
真实解光滑，故 J 在实际区间上可微。压力在完整方程中精确消去：
\[
\int_{B_*}\nabla P\cdot\psi
=-\int_{B_*}P\operatorname{div}\psi=0.
\]
这对来自整个周期解的真实压力成立，不假设外壳或任何局部场独立演化，也不需要局部压力大小的估计。

将 WLI.1 与 ψ 配对，使用 WLI.9–10，再对所有含 E 的空间导数分部积分，得到
\[
\boxed{\begin{split}
J'(s)={}&-Q_\chi
+\int_{B_*}E\cdot
\left\{\frac35\psi+\frac25(y\cdot\nabla)\psi
+\nu(s)\Delta\psi\right\}\,dy\\
&+\int_{B_*}
(V\otimes E+E\otimes V+E\otimes E):\nabla\psi\,dy.
\end{split}}
\tag{WLI.12}
\]
采用 \((\nabla\psi)_{ij}=\partial_j\psi_i\)。这条恒等式保留两项不同的线性对流作用和全部二次作用，没有把它们直接合成一个有序非线性项。

为逐项核清线性系数，漂移分部积分给
\[
-\frac25\int(y\cdot\nabla)E\cdot\psi
=\frac25\int E\cdot\{3\psi+(y\cdot\nabla)\psi\};
\]
与 \(-\frac35\int E\cdot\psi\) 合并后的系数为 +3/5。黏性先在动量恒等式中移到右侧，再两次分部积分，准确留下 \(+\nu(s)\int E\cdot\Delta\psi\)。非线性则由 divF=divV=0 给
\[
-\int(F\cdot\nabla)F\cdot\psi
=\int F\otimes F:\nabla\psi,\qquad
\int V\otimes V:\nabla\psi=-Q_\chi.
\]
紧支撑保证这些操作无边界项。它们对光滑真实解合法，但估计不需要任何 E 的导数上界。

全部向量范数取欧氏范数，矩阵范数取 Frobenius 范数；以下为明确固定常数：
\[
\begin{split}
L_\chi={}&\frac35\|\psi\|_2+
\frac25\|(y\cdot\nabla)\psi\|_2+
\nu_*\|\Delta\psi\|_2\\
&+2\|V\|_{L^\infty(B_*)}\|\nabla\psi\|_2,
\qquad
B_\chi=\|\nabla\psi\|_{L^\infty(B_*)}.
\end{split}
\tag{WLI.13}
\]
本节无下标的 L² 范数均在 B*。这些常数有限，并且 Lχ>0，因为其第一项含 Nχ>0。

两项线性交叉应力各自用 Cauchy–Schwarz 控制；二次项使用 \(|E\otimes E|_{\rm F}=|E|^2\)。故完整余项满足
\[
\boxed{
|J'(s)+Q_\chi|
\le L_\chi\|E(s)\|_2+
B_\chi\|E(s)\|_2^2.}
\tag{WLI.14}
\]
这里没有 \(E_s,\nabla E,\Delta E\) 或更高导数，也没有隐藏的扰动 L∞ 假设。黏性由正的 \(\nu_*\|\Delta\psi\|_2\) 项明确支付。

## 5. 端点误差与一次连续持留定理

设真实光滑解实际存在于闭区间 [s0,s1]，s0≥log100，并连续满足
\[
\|F(s)-V\|_{L^2(B_*)}\le\varepsilon
\quad\text{对每个 }s\in[s_0,s_1],
\qquad \varepsilon\ge0.
\tag{WLI.15}
\]
如果
\[
d_\chi(\varepsilon):=
Q_\chi-L_\chi\varepsilon-B_\chi\varepsilon^2>0,
\]
则 WLI.14 给 \(J'(s)\le-d_\chi(\varepsilon)\)。
另一方面，两个时间端点都必须按 WLI.11 付误差：
\[
|J(s_\ell)|\le N_\chi\varepsilon\quad(\ell=0,1),
\qquad
J(s_1)-J(s_0)\ge-2N_\chi\varepsilon.
\]
积分真实动量式得到
\[
-2N_\chi\varepsilon
\le J(s_1)-J(s_0)
\le-d_\chi(\varepsilon)(s_1-s_0).
\]
因此
\[
\boxed{
s_1-s_0\le
\frac{2N_\chi\varepsilon}
{Q_\chi-L_\chi\varepsilon-B_\chi\varepsilon^2}.}
\tag{WLI.16}
\]
没有假设 J 的起点为零，也没有丢掉任一端点误差。

例如可用只含已定义有限量的明确阈值
\[
\boxed{
\varepsilon_\chi=
\min\left\{1,\frac{Q_\chi}{2(L_\chi+B_\chi)}\right\}>0.}
\]
分母非零由 Lχ>0 支付。对所有符号 \(0\le\varepsilon\le\varepsilon_\chi\)，有
\(L_\chi\varepsilon+B_\chi\varepsilon^2\le Q_\chi/2\)，从而
\[
\boxed{s_1-s_0\le\frac{4N_\chi}{Q_\chi}\,\varepsilon.}
\tag{WLI.17}
\]
这是对任意事先固定 χ 的条件定理，没有实际选取 χ、ε 或进入时刻。ε=0 时上界为零，表示真实解不可能在正长度区间内恰等于该固定局部 V。若误差超出阈值而 WLI.16 的分母也不能证明为正，本稿不给持留结论。

对未闭合的持留区间，可在其中任意两个实际存在的端点上使用同一界。因此在上述误差条件下，一次连续持留区间不可能具有无限 s 长度；这不需要弱解时间迹或任何新的延拓定理。

## 6. 与旧 C³ 结论的差别及准确范围

新增的是实际空间假设的下降：旧定理在一点通过涡量微分支付 C³ 误差；本稿通过紧支撑无散动量测试，把所有扰动空间导数转移到固定测试，得到局部速度 L² 的线性加二次预算。测试函数可以有有限的一至三阶导数，但没有对扰动要求这些导数小。

这里保留完整重标黏性、漂移、周期压力、非线性 E⊗E 及两个时间端点。χ 不要求轴对称；真实 F 更不要求轴对称或纯方位。旧 V 和 b2 仅是已固定的比较形状，未使用旧 NON-NS 辅助路径作为真实轨道。全 B* 的非线性正号已经由 WLI.3–5 独立重新核清。

结论只约束这个固定形状、固定重标坐标和固定球中的一次连续小 L² 持留。它不能控制离开后的再进入次数、累计停留时间、任意快速调制的小误差轨道或其它非定常结构。也没有将定理推广到弱解：弱时间迹、局部能量、正则化及额外可测性问题不在本合同内。

不能由离开该邻域推出奇性或正则性；没有新 NS 候选、实际参数选择、无限尺度或有限总时间结论，没有补修旧失败证据。NO-CANDIDATE；NOT CLAY。

本稿在最终停改前逐式手核、实际全文自读并复核三份来源字节，随后报告 SHA。
