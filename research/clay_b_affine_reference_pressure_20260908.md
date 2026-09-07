# 仿射参照与压力 Hessian：尺度递推和剩余项

2026-09-08。AH，PRIVATE_CORE。范围内先验估计、精确恒等式和局部解反检；一般三维 NS / Clay 仍 OPEN / NOT CLAY。不宣称原创性或真人同行评审。

本节得到压力 Hessian 的一个有源尺度递推：调和部分可以收缩，近场梯度能量仍作为临界源出现。仿射参照也有真实的二阶抵消，但不能据此删除压力尾，或把相对梯度的耗散换成原梯度的耗散。这两件事用精确局部 NS 解分别核查。

## 1. 压力 Hessian 的有源尺度递推

单位黏性、无外力，先取 WE.1 的能量类分布解于 \(Q_1=B_1\times(-1,0)\)。本节这一部分不需局部能量不等式或前终端光滑。由 WE.4，Hessian 在已指定内域可积。对 \(0<r\le1/2\) 记
\[
 H=\nabla^2p,\quad G=\nabla u,\quad I_r=(-r^2,0),\qquad
 \mathcal H(r)=r^{-1}\int_{Q_r}|H|,\quad
 \mathsf E(r)=r^{-1}\int_{Q_r}|G|^2.
 \tag{AH.1}
\]
不把 WE 只在内球证明的 Hessian 可积性直接扩大到原母球边界。

将 WE.6–8 的固定均值、cutoff和环域无散扩张按 r 缩放，得到每时刻的紧支无散 \(v_r\)，在 \(B_{7r/8}\) 等于 \(u-(u)_{B_r}\)。令 \(\pi_r=\mathcal R_i\mathcal R_j(v_{r,i}v_{r,j})\)，则
\[
 \int_{I_r}\!\!\int_{\mathbb R^3}|\nabla^2\pi_r|
 \le C\int_{Q_r}|G|^2=C r\mathsf E(r),
 \qquad h_r=p-\pi_r\text{ 在 }B_{7r/8}\text{ 调和}.
 \tag{AH.2}
\]
这里仍使用散度—旋度的实 Hardy 界，不是任意 L1 源的 Riesz 界；扩张误差已由尺度一致的梯度界包含。

对 \(0<\theta\le1/4\)，调和矩阵每个分量的内估计给
\[
 \int_{B_{\theta r}}|\nabla^2h_r(t)|
 \le C_0\theta^3\int_{B_{3r/4}}|\nabla^2h_r(t)|.
 \tag{AH.3}
\]
在 \(I_{\theta r}\subset I_r\) 积分，用三角不等式和 AH.2，再除以 theta r，得到
\[
 \boxed{\mathcal H(\theta r)
 \le C_0\theta^2\mathcal H(r)+C_1\theta^{-1}\mathsf E(r).}
 \tag{AH.4}
\]
常数与 r、theta及解无关，只依赖固定几何与标准算子。中间近压系数是 \(C(\theta^{-1}+\theta^2)\)，在指定 theta 范围内并入 AH.4。空间内缩提供 theta³；时间只使用区间包含，没有额外的 theta² 时间小因子。

固定 theta，使 \(a=C_0\theta^2<1\)，令 \(r_k=\theta^kr_0\)、\(b=C_1/\theta\)。递推给
\[
 \mathcal H(r_k)\le a^k\mathcal H(r_0)
 +b\sum_{j=0}^{k-1}a^{k-1-j}\mathsf E(r_j).
 \tag{AH.5}
\]
若 \(\sup_j\mathsf E(r_j)\le M\)，则右侧不超过 \(a^k\mathcal H(r_0)+bM/(1-a)\)；若 \(\mathsf E(r_j)\) 趋零，则拆成有限头部与任意小的尾部，得到 \(\mathcal H(r_j)\) 趋零。这里传递已有能量小量，没有产生该小量。Hessian 也不控制压力的空间仿射部分，不能代替 SC 中只减空间常数后的 D 条件。

## 2. 最佳常矩阵方向保留原耗散，但只减去一个边界量

以下各节先在闭光滑时段与空间内域计算。记
\[
 q=|G|,\quad B=G/q\ (q>0),\quad B_0=0\ (q=0),\quad
 L=\partial_t+u\cdot\nabla-\Delta,\quad N=G^2+H,
 \qquad Lq+\mu_G=-B_0:N.
 \tag{AH.6}
\]
沿用 GD 的非负测度 \(\mu_G=\mathbf1_{q>0}q|\nabla B|^2dxdt+\zeta_G\)，不删除零集余项。任意空间常量、时间 C1、满足 \(|W|_F=1\) 的矩阵方向 W 给
\[
 e_W=q-W:G\ge0,\qquad
 Le_W+\mu_G=-(B_0-W):N-W':G.
 \tag{AH.7}
\]
这保留原耗散；但时间参照并非无代价。

取固定 \(0\le\eta\in C_c^\infty\)，定义
\[
 F_\eta=\int\eta q,\quad M_\eta=\int\eta G,
 \quad J_\eta=F_\eta-|M_\eta|\ge0,\qquad
 W_0(t)=M_\eta/|M_\eta|\text{ 若 }M_\eta\ne0,\text{ 否则 }0.
 \tag{AH.8}
\]
M 是绝对连续函数，范数链式为 \((|M|)'=W_0:M'\) 几乎处处，包括 M=0 的时刻；此处不微分 W_0，也不产生第二阶时间范数缺陷。由速度方程直接得到
\[
 (M_\eta)_{ij}=-\int u_i\partial_j\eta,\qquad
 (M_\eta)'_{ij}=-\int u_i\partial_j\Delta\eta
 -\int u_i u_k\partial_{jk}\eta-\int p\partial_{ij}\eta.
 \tag{AH.9}
\]
因此对 a<b，原耗散满足精确积分式
\[
 J_\eta(b)-J_\eta(a)+\int_a^b\!\!\int\eta\,d\mu_G
 =\int_a^b\!\!\int (q-W_0:G)(\Delta\eta+u\cdot\nabla\eta)
 -\eta(B_0-W_0):N.
 \tag{AH.10}
\]
不要求 W_0 穿过 M=0 时可微；逐时 \(\int\eta(q-W_0:G)=J_\eta\)。两个非负空间熵缺陷相减可能失去正性，但这里减去的是一阶时间绝对连续范数，没有第二个空间耗散。

对每个空间常矩阵 W 和常向量 c，确切的常系数消项只是
\[
 \int\eta W:G^2=-\int(\partial_k\eta)W_{ij}(u_i-c_i)G_{kj},
 \qquad \int\eta W:H=\int p W_{ij}\partial_{ij}\eta.
 \tag{AH.11}
\]
它们是边界项，不是局部零。全周期胞取 eta=1 时 M=0，J恰等于原来的整胞梯度 L1；局部则只减去了 AH.9 的边界速度量。最佳方向没有自动给新的体积分符号。

## 3. 相对梯度范数漏掉原耗散中的径向变化

设 C(t) 是 C1、迹零的空间常矩阵，H_C(t) 对称，并满足 \(C'+C^2+H_C=0\)。这意味着 \(u_C=Cx\)、\(p_C=x^\top H_Cx/2\) 是精确局部仿射 NS 解。令 R=G-C、delta H=H-H_C，便有
\[
 LR=-R^2-CR-RC-\delta H,\qquad
 L|R|+\mu_R=-D_0:(R^2+CR+RC+\delta H),
 \quad D=R/|R|\text{ 于 }R\ne0,\quad D_0=D\ (R\ne0),\ D_0=0\ (R=0).
 \tag{AH.12}
\]
mu_R有自己的非负零集余项，不能等同于 mu_G。交叉项只去掉 C 的反对称部分：\(|D:(CR+RC)|\le2\|\operatorname{sym}C\|_{op}|R|\)。

若 m=|C|>0、\(|R|\le\theta m\)、theta<1，则于 R非零处
\[
 \Gamma_G\le\frac{|\nabla R|^2}{(1-\theta)m}
 =\frac{|\nabla|R||^2+|R|\Gamma_R}{(1-\theta)m},
 \qquad\Gamma_R=|R||\nabla(R/|R|)|^2.
 \tag{AH.13}
\]
相对方向耗散没有第一项。

这不是任意不相容矩阵的例子。取 y=x2、\(0<\epsilon<1/4\)，
\[
 u=(x_1+f(y,t),-y,0),\quad
 f=\epsilon y+\tfrac\epsilon2e^t(y^2+1),\quad
 p=-\tfrac12(x_1^2+y^2),\quad C=\operatorname{diag}(1,-1,0).
 \tag{AH.14}
\]
直接代入得 \(f_t+f-yf_y=f_{yy}\)，所以是原无外力 NS 精确光滑局部解。于 \(B_{1/4}\times[0,\log2]\)，\(R=sE_{12}\)、\(s=\epsilon(1+e^ty)\in[\epsilon/2,3\epsilon/2]\)，因而
\[
 \Gamma_R=0,\qquad
 \Gamma_G=\frac{2\epsilon^2e^{2t}}{(2+s^2)^{3/2}}>0,
 \qquad G^2+H=0.
 \tag{AH.15}
\]
它可任意接近固定 C，仍不能用 Gamma_R 乘任何有限常数代替 Gamma_G。这里连惯性—压力源都精确抵消；差别来自相对范数漏掉幅值导数。该多项式速度没有全空间有限能量或周期边界，不是奇点或 Clay 反例。

## 4. 保留原耗散的参照抵消：二阶项与相对压力尾

对上一节的精确仿射参照，取 \(m=|C|>0\)、W=C/m、\(\Pi_WZ=Z-(W:Z)W\)、\(N_C=C^2+H_C=-C'\)。在 q>0 有
\[
 Le_W+\mu_G
 =-[B-W-\Pi_WR/m]:N_C
 -(B-W):(CR+RC+R^2+\delta H).
 \tag{AH.16}
\]
这是把 \(W'=-\Pi_WN_C/m\) 的真实时间项保留下来的抵消，不是将参照冻结。

若 \(|R|\le\theta m\)、0<theta<1，沿 C+sR 对归一化映射作 Taylor 展开，得到
\[
 |B-W|\le C_\theta|R|/m,\qquad
 |B-W-\Pi_WR/m|\le C_\theta|R|^2/m^2.
 \tag{AH.17}
\]
故参照项与惯性项之和绝对值不超过
\(C_\theta(1+|N_C|/m^2)|R|^2\)，相对压力项仍为 \(C_\theta |R||\delta H|/m\)。定义 \(\alpha=W:R\)、\(T=R-\alpha W\)，则精确有
\[
 e_W=\frac{|T|^2}{q+m+\alpha},\qquad
 \frac{|T|^2}{2(1+\theta)m}\le e_W
 \le\frac{|T|^2}{2(1-\theta)m}.
 \tag{AH.18}
\]
它只控制横向 T，不控制径向 alpha。AH.8 的最佳平均方向也不自动满足这里的仿射 NS 参照方程，两种选择不能混为同一对象。

在固定时刻，若同一近仿射条件成立于母球 B1，令 chi紧支B1且等于一于B3/4，并记
\[
 -\Delta\delta p=2\operatorname{tr}(CR)+\operatorname{tr}(R^2)=:f_R,
 \quad\delta p=p-p_C,\quad\pi_R=(-\Delta)^{-1}(\chi f_R),
 \quad h_R=\delta p-\pi_R.
 \tag{AH.19}
\]
h_R 在内球调和。普通 L2 椭圆界而非 L1 端点给
\[
 \|\nabla^2\pi_R\|_2\le C_\theta m\|R\|_{L^2(B_1)},\qquad
 \left|\int_{B_{1/2}}(B-W):\nabla^2\pi_R\right|
 \le C_\theta\|R\|_{L^2(B_1)}^2.
 \tag{AH.20}
\]
因此近压力也可二次估计，但剩下的 \(\int(B-W):\nabla^2h_R\) 不能删除。完整 R 的二次界、m的非退化下界与参照速率均非 e_W 自动提供。若把点态近似和有界参照强加到整个时空母柱，已是很强的梯度假设；这里不把它包装成新的无条件正则判据。

## 5. 两个局部压力检查，不能外推成周期奇性

先说明相对调和尾确实能产生一阶源。取 \(C=\operatorname{diag}(1,-1,0)\)、\(Z=\operatorname{diag}(1,1,-2)\)，固定参照 H_C=-C²，令
\[
 D_\epsilon(t)=C+(\epsilon+t)Z,\quad
 u_\epsilon=D_\epsilon(t)x,\quad
 p_\epsilon=-\tfrac12x^\top(Z+D_\epsilon^2)x.
 \tag{AH.21}
\]
该对精确满足无外力 NS。t=0 时 \(|R|^2=6\epsilon^2\)，而
\[
 e_W=\sqrt{2+6\epsilon^2}-\sqrt2,\qquad
 Le_W=\frac{6\epsilon}{\sqrt{2+6\epsilon^2}}>0,
 \qquad\Gamma_G=0.
 \tag{AH.22}
\]
相对压力中固定的迹零 -Z 是二次调和压力的 Hessian，带来一阶源。此例只排除对给定参照、仅凭瞬时近似便让全部源二次化的普遍局部断言；不排除选择更贴合的参照或保留尾项的估计。

即使用最佳平均方向，局部零偏差也不自动保持。令 h=x1 x2 x3、\(u=t\nabla h\)、\(p=-h-t^2|\nabla h|^2/2\)。因 h调和、\(\Delta u=0\)、\((u\cdot\nabla)u=\nabla(|u|^2/2)\)，这是精确光滑局部 NS。对非零非负径向紧支 eta，t>0时
\[
 G=t\nabla^2h,\quad q=\sqrt2\,t|x|,\quad M_\eta=0,
 \quad J_\eta=\sqrt2\,t\int\eta|x|>0,\qquad
 \Gamma_G=\frac{2\sqrt2\,t}{|x|}\ (x\ne0),\quad
 \int_{B_R}\Gamma_G=4\sqrt2\pi tR^2.
 \tag{AH.23}
\]
在t=0，u、G、J全为零，局部谐和压力却能产生梯度。故不含压力或边界源的自治 \(J'\le C(t)J\)、\(C\in L^1\)，不能对所有局部解成立。这个结论不否定含尾项的尺度递推，也不否定全局初边值条件下的唯一性。该速度仍非周期、非全空间有限能量，并不触及 Clay 所需反例。

潜势解构造是经典的：[Wolf原稿导言例子](https://arxiv.org/html/1611.01482v1)直接给出任意谐和空间势与时间系数的同类解，并明确未施加边界条件。本稿只复算其 h=x1 x2 x3、时间系数t下的 J 和 Gamma，不认领这一构造为新结果。

## 6. 对下一步的实际约束

AH.4 是压力子系统的有源收缩，不是全 NS 的收缩。它把压力Hessian的调和尾与近场 E 源分开；对同一解产生 E 或原形状耗散小量的步骤仍缺失。AH.16–20 保留一项合法的条件二阶抵消；AH.15、22–23 则分别阻止丢弃径向导数、相对压力尾与局部边界源。不能据此宣称所有仿射方法不可能。

下一步只针对 WE.23 中真实同解的近场惯性—压力组合及截止输运，写出两尺度的带符号积分预算，判断在 AH.4 已明确的临界 E 源之外，是否能得到可吸收或可求和的误差。保留原 mu_G 或真实弱 grad Theta，不改用未比较的相对 Gamma。共同 A+E+D 上界、任意演化好尺度、有效阈值与 Clay 结论仍未得到；一个条件改写或有限积分不是其证明。

去重完整读回 WE、GD、RL、SN和R0.69H压力Hessian旧稿。SN已经用真实周期解族排除了普遍的整胞二次偏离伸长界；R0.69H已经排除只由局部梯度判断压力符号。本节不重复这些旧结果，也不重新运行旧数值证书。Wolf仅定向读导言与上述例子，未认证全篇及其压力投影理论。其他搜索结果未作为新证明输入；不是Deep Research全面综述或新颖性审查。

没有PDE仿真、DGX、科学附图、数值证书、读者HTML/PDF、公开概要或阶段recap。闭式例子的符号复算不等于连续正则性证书。完整内容只在冻结后一次交固定发布任务作PRIVATE_ARCHIVE，研究任务不进行或监督发布。
