# 完整速度梯度偏离秩一的空间控制

2026-09-08，北京时间。GD，PRIVATE_CORE。范围内解析证明、条件性延拓接口；一般三维 NS 正则性仍 OPEN / NOT CLAY。不宣称新颖性、最优常数或真人同行评审。

本轮得到一项明确但尚未临界的控制：完整速度梯度偏离秩一矩阵的程度，除以梯度模长的平方根后，具有无对数损失的空间 H1 预算。关键不只是更换熵函数，而是利用速度梯度每一行无旋这一约束，将原来未控的径向导数与形状导数联系起来。

这个偏离量也能逐点控制真实涡伸长。若它另有一个临界时空范数，就能排除有限时间失去光滑性；但本轮的空间预算没有给出那个范数。以下将已证明的估计、条件出口和缺失输入分开。

## 1. 对象不是应变谱投影

固定未归一化的 \(\mathbb T^3_{2\pi}\)、\(\nu>0\)，u 为同一无外力、不可压 NS 解，先在闭光滑区间 \([0,T]\) 计算。记
\[
 A_{ij}=\partial_j u_i,\quad S=\operatorname{sym}A,\quad
 H=\nabla^2p,\quad \omega=\operatorname{curl}u,\quad
 L=\partial_t+u\cdot\nabla-\nu\Delta,\quad Q=|A|_F.
 \tag{GD.1}
\]
以下 \(B=A/Q\) 只定义在 \(Q>0\)。这里的 Q、B 是完整速度梯度的模长和归一化矩阵，不是 SG 的应变模长与对称矩阵，也不是 R0.70 的涡量协方差。

设 \(\mathcal R_1=\{M\in\mathbb R^{3\times3}:\operatorname{rank}M\le1\}\)。取
\[
 d=d(A)=\operatorname{dist}_F(A,\mathcal R_1),\quad
 \tau=d/Q,\quad F=d/\sqrt Q,\quad R_g=F^2=d^2/Q
 \qquad(Q>0).
 \tag{GD.2}
\]
在 Q=0 处令 d、F、\(R_g\) 为零，不在那里选 B。d 的比较集合不额外要求迹零；主场 A 本身满足 \(\operatorname{tr}A=0\)。若 A 秩一且迹零，则 \(A^2=0\)，其点态涡伸长为零。这里不假设整个秩一梯度类在 NS 演化下保持不变。

## 2. 完整梯度的形状熵，零集仍在

直接微分速度方程，得到
\[
 LA=-A^2-H.
 \tag{GD.3}
\]
继承 SE.2–4、SG.2 已核对的固定周期 Hardy 压力接口
\(\|H(t)\|_1\le C_H\|A(t)\|_2^2\)。没有对任意 L1 源声称 Riesz 变换 L1 有界。设
\[
 E_0=\tfrac12\|u(0)\|_2^2,\qquad
 \mathcal B_A=\int Q(0)+(1+C_H)E_0/\nu.
\]
初始梯度 L1 不能删去或改成只由初始能量支付。

对九维矩阵变量使用 \(\Phi_\epsilon(A)=\sqrt{Q^2+\epsilon^2}-\epsilon\)。其非负 Hessian 密度是
\[
 D_\epsilon=\sum_k\left[
 \frac{|\partial_kA|^2}{\sqrt{Q^2+\epsilon^2}}
 -\frac{(A:\partial_kA)^2}{(Q^2+\epsilon^2)^{3/2}}\right].
\]
源项为 \(-A:(A^2+H)/\sqrt{Q^2+\epsilon^2}\)，绝对值不超过 \(Q^2+|H|\)。在 Q>0 的紧子集上，\(D_\epsilon\) 趋于 \(Q|\nabla B|^2\)。与 SG.6–8 相同的分布极限给唯一非负测度
\[
 \mu_A=\frac{-B_0:(A^2+H)-LQ}{\nu}
 =\mathbf1_{\{Q>0\}}Q|\nabla B|^2\,dxdt+\zeta_A,\quad
 \zeta_A\ge0,\quad \operatorname{supp}\zeta_A\subseteq\{Q=0\},
 \tag{GD.4}
\]
其中源项内 \(B_0=0\) 于 Q=0，其余为 B。固定光滑区间上
\(\int D_\epsilon=-\int[A/\sqrt{Q^2+\epsilon^2}]:\Delta A
\le\|\Delta A\|_1\)，排除时间端点聚集；不删除零集余项。

对每个光滑终点 T，能量等式于是给
\[
 \boxed{\int Q(T)+\nu\int_0^T\!\!\int_{Q>0}Q|\nabla B|^2
       +\nu\zeta_A(\mathbb T^3\times(0,T))\le\mathcal B_A.}
 \tag{GD.5}
\]
由此分别控制 \(\sup_t\int Q(t)\) 和累计耗散，不能将两者的各自上确界相加后仍写成同一个 \(\mathcal B_A\)。当 \(T\uparrow T_*<\infty\) 时只取累计上界，不预设终端强迹或光滑延拓。

## 3. 无旋约束补上一个退化的径向方向

记 \(b_i\) 为 B 的第 i 行。由于 A 的每一行是 \(\nabla u_i\)，在 Q>0 有
\(\operatorname{curl}(Qb_i)=0\)，从而
\[
 b_i\times\nabla Q=Q\operatorname{curl}b_i,\qquad
 \nabla Q^\top(I-B^\top B)\nabla Q
 =Q^2\sum_i|\operatorname{curl}b_i|^2
 \le2Q^2|\nabla B|^2.
 \tag{GD.6}
\]
第二式先对各行使用叉积模长恒等式再求和；最后仅用反对称导数的平方不超过两倍完整导数平方。

令 \(s_1\ge s_2\ge s_3\ge0\) 为 A 的奇异值。对固定单位向量 n，在形如 \(a\otimes n\) 的矩阵中最佳选择为 \(a=An\)，误差平方为 \(Q^2-|An|^2\)。再对 n 最大化，得到
\[
 d^2=s_2^2+s_3^2=Q^2-s_1^2,\qquad
 \tau^2=1-\|B\|_{op}^2,\qquad
 \tau^2|\nabla Q|^2\le2Q^2|\nabla B|^2.
 \tag{GD.7}
\]
这也给最佳秩一逼近 M 满足 \(Q^2=|M|^2+d^2\)。距离到闭集的函数为 1-Lipschitz，因此 \(\tau(B)=\operatorname{dist}(B,\mathcal R_1)\) 可用 Lipschitz 链式法则；无需排除重奇异值，也不求导一个选定的奇异向量。

于 Q>0 几乎处处，
\[
 |\nabla F|
 \le\frac{\tau}{2\sqrt Q}|\nabla Q|+\sqrt Q|\nabla\tau|
 \le(1+1/\sqrt2)\sqrt Q|\nabla B|.
 \tag{GD.8}
\]
于是得到本轮主要空间估计：
\[
 \boxed{
 \sup_{t<T_*}\|F(t)\|_2^2\le\mathcal B_A,\qquad
 \nu\int_0^{T_*}\!\!\int|\nabla F|^2
 \le(1+1/\sqrt2)^2\mathcal B_A.}
 \tag{GD.9}
\]
取上确界时亦可包含初始时刻。因 \(F^2\le Q\)，在有限 \(T_*\) 上这给 \(F\in L^\infty_tL^2_x\cap L^2_tH^1_x\)。

跨零集的步骤不能省略。F 在矩阵空间连续，且 \(F^2\le Q\)。取 \(F_\delta=(F-\delta)_+\)，其非零区域有 \(Q>\delta^2\)，所以它与光滑 A 的复合为合法 Lipschitz 函数，梯度由 GD.8 控制。\(F_\delta\to F\) 强 L2，梯度具有统一时空 L2 界；弱紧性给全域弱梯度及 GD.9。不存在把 B 在 Q=0 的经典导数偷偷设为零的步骤。

GD.9 没有对数损失，但估计的是 \(d/\sqrt Q\)，不是整个 \(\sqrt Q\)。它没有给时间 BV，也没有将已有低阶熵预算变成缩放临界量。

## 4. 偏离量确实控制真实涡伸长

对任意迹零实矩阵 A，用其反对称部分定义 \(\omega_A\)，使 \(\operatorname{skew}A=[\omega_A]_\times/2\)；当 \(\omega_A\ne0\) 时令 \(\xi_A=\omega_A/|\omega_A|\)。有
\[
 \boxed{|S_A\xi_A|\le4d(A)\quad(\omega_A\ne0),\qquad
 |\omega_A\cdot S_A\omega_A|\le4d(A)|\omega_A|^2.}
 \tag{GD.10}
\]
证明分两种情况。若 \(d\ge Q/4\)，则 \(|S_A\xi_A|\le Q\le4d\)。若 \(d<Q/4\)，取上节最佳秩一 M。因 \(\operatorname{tr}A=0\)，
\[
 |\operatorname{tr}M|\le\sqrt3d,\qquad
 |\omega_M|^2=|M|^2-(\operatorname{tr}M)^2\ge Q^2-4d^2.
\]
此外 \(|\omega_A-\omega_M|\le\sqrt2d\)，故
\[
 |\omega_A|\ge\sqrt{Q^2-4d^2}-\sqrt2d>Q/2.
\]
写 M 为 \(a\otimes n\)，则 \(\omega_M=n\times a\)，因此 \(S_M\omega_M=0\)。于是
\[
 |S_A\omega_A|
 \le d|\omega_A|+|M|\sqrt2d
 \le(1+2\sqrt2)d|\omega_A|<4d|\omega_A|.
\]
Q=0 或 \(\omega_A=0\) 的伸长不等式平凡。最佳 M 不必迹零，证明已经支付它的迹误差；常数四不作最优性主张。

## 5. 一个写明条件的临界出口

设 u 从任意光滑无散周期初值出发，在 \([0,T_*)\) 光滑，\(T_*<\infty\)。若对某个
\[
 3/2<r<\infty,\qquad p=\frac{2r}{2r-3},\qquad
 \boxed{\int_0^{T_*}\|d(A(t))\|_r^p\,dt<\infty,}
 \tag{GD.11}
\]
则 u 可光滑延拓过 \(T_*\)。\(r=\infty,p=1\) 也成立。这里是额外假设，不是 GD.9 的结论。

具体地，令 \(Y=\|\omega\|_2^2=\|A\|_2^2\)、\(Z=\|\nabla\omega\|_2^2\)。涡量能量恒等式及 GD.10 给
\[
 \tfrac12Y'+\nu Z=\int\omega\cdot S\omega
 \le4\|d\|_r\|\omega\|_{2r/(r-1)}^2
 \le C_r\|d\|_rY^{1-\alpha}Z^\alpha,\quad
 \alpha=\frac3{2r}\in(0,1).
 \tag{GD.12}
\]
周期涡量的均值为零，故 Sobolev 插值中的常数模可由 Poincaré 吸收。Young 给
\[
 \tfrac12Y'+\tfrac\nu2Z
 \le C_r\nu^{-3/(2r-3)}\|d\|_r^{\,2r/(2r-3)}Y.
 \tag{GD.13}
\]
GD.11 与 Gronwall 给统一 H1 速度界及累计 H2 界。局部强解理论提供只依赖固定黏性、周期胞与该 H1 界的共同存在时间，从趋近 \(T_*\) 的切片重启并用唯一性拼接，即得延拓。\(r=\infty\) 时直接用 \(4\|d\|_\infty Y\)，无需 Young；不在此讨论 \(r=3/2\) 的无小性端点。

这里调用的是标准 H1 强解延拓接口；[Cao–Titi 原稿](https://arxiv.org/html/1005.4463v1) 导言及 Theorem 1 证明开头明确使用同一延拓逻辑，并说明周期情形。我们没有移植该文的单分量条件，也没有声称全文重审其证明。GD.10–13 的 d 估计是上面给出的本地计算，不以文献标题替代证明。

## 6. 空间增量还没有支付临界范数

GD.9 与固定周期 Sobolev 插值给
\[
 R_g=F^2\in L^{1/\theta}_tL^{3/(3-2\theta)}_x,\qquad
 0\le\theta\le1.
 \tag{GD.14}
\]
这条线满足 \(2/p+3/r=3\)，不是梯度量的临界线 2。结合 \(R_g\le Q\) 的基本 \(L^2_tL^2_x\) 预算，所列范数的直接插值仍只有 \(2/p+3/r\ge5/2\)。

真正控制伸长的是 d，而非 \(R_g=d^2/Q\)。例如由 \(d=\sqrt{R_gQ}\)、\(R_g\in L^1_tL^3_x\)、\(Q\in L^2_tL^2_x\)，只得
\(d\in L^{4/3}_tL^{12/5}_x\)，指数和为 \(11/4\)。还可用 \(d\le Q\) 得 \(L^2_tL^2_x\)；这些直接 Hölder 与插值组合仍达不到 GD.11。这个限制只针对已列范数，不是所有 NS 方法的不可行性定理。

也不能把 d 在伸长界中直接替换为 \(R_g\)。对纯代数迹零矩阵
\[
 A_\epsilon=
 \begin{pmatrix}0&0&1\\0&\epsilon&0\\0&0&-\epsilon\end{pmatrix},
 \qquad 0<\epsilon<1/4,
 \tag{GD.15}
\]
有 \(Q^2=1+2\epsilon^2\)、\(d=\epsilon\)、\(\omega=e_2\)、
\(\omega\cdot S\omega=\epsilon\)，而 \(R_g=\epsilon^2/Q\)。因此不存在统一常数将 GD.10 改成 \(C R_g|\omega|^2\)，或把一般点态伸长中的线性 \(\tau\) 换成 \(\tau^2\)。这是矩阵阶数检查，不是周期 NS 解、奇点或终端行为的反例。

## 7. 为什么本轮没有沿可变谱轴继续

最初检验的是 SC 固定轴子式的空间变轴版本。对任意光滑周期对称矩阵测试 M，令
\[
 K_{ij\ell}=\tfrac12\epsilon_{iab}\epsilon_{j\ell d}
             (u_a-c_a)\partial_du_b,\qquad
 \partial_\ell K_{ij\ell}=(\operatorname{cof}A)_{ij},
\]
其中 c 是空间常向量，cofactor 采用
\((\operatorname{cof}A)_{ij}=\partial(\det A)/\partial A_{ij}\)。
代数恒等式 \(\operatorname{sym}(\operatorname{cof}A)
=\operatorname{cof}S+\omega\otimes\omega/4\) 给
\[
 \int M:\operatorname{cof}S+\tfrac14\int\omega\cdot M\omega
 =-\int K_{ij\ell}\partial_\ell M_{ij}.
 \tag{GD.16}
\]
取 \(0\le\chi\le1\) 光滑并紧支撑在 P 可光滑定义的开区内。对 \(M=\chi P\)，右端既有 \(-\int\chi K:\nabla P\)，也有
\(-\int K_{ij\ell}P_{ij}\partial_\ell\chi\)。\(|K|\le|u-c||A|/\sqrt2\)。
在孤立谱线开区，现有 \(\int a|\nabla P|^2\) 只能与未付的
\(\int\chi|u-c|^2|A|^2/a\) 配对；还需 \(\lambda_2=0\) 的谱切换和低幅度截断成本。固定轴的正号不能自动扩展到全空间变轴场。

该恒等式保留为已完成的有限接口计算，不把它另记为临界增益。GD.6–9 则绕开了谱线选择：只使用整个矩阵到秩一集合的距离，利用 Lipschitz 链式处理重奇异值，并明确处理 Q=0。

## 8. 完成边界与下一步

本轮的正面增量是 GD.9 的几何偏离空间预算及 GD.10 的逐点伸长控制。GD.11 是有条件的临界出口，所需的 d 范数仍 OPEN。没有任意初值正则性证明、奇性构造、新颖性认证或大里程碑回顾。

下一步集中在同一 d 的动力学，而非再改一个对数权重：核对原 NS 压力 Hessian 与黏性乘积项怎样产生或耗散偏离秩一的部分，并检验能否得到 GD.11 所需的时间增益。cofactor 的旧静态 Piola 恒等式先去重；不得预设秩一梯度类不变、删去重奇异值／零集项，或把未控制的压力成本藏入常数。困难引理允许继续探索，结论仍以实际证明为准。

原著检索只是一次有界的普通来源核对，不作 Deep Research 全面综述或原创性检索：两项定点查询后仅打开上述 Cao–Titi HTML 的导言和延拓接口片段，其余结果未作为证明输入。既有 SG/SE 的 Hardy 接口按已冻结证明继承。没有仿真、DGX、数值证书、科学附图、第三方 PDF 归档或读者 HTML/PDF；完整成果保持私有。
