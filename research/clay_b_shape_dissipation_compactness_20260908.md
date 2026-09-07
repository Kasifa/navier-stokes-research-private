# 形状耗散的小量判据：秩一与仿射两种极限

2026-09-08，北京时间。SC，PRIVATE_CORE。局部条件命题；一般三维 NS 仍 OPEN / NOT CLAY。没有充分查新，不宣称原创性或真人同行评审。

这一节把 GD 的全梯度形状耗散接到局部正则判据上。关键不是证明小耗散极限一定秩一——这个说法不成立——而是保留秩一和空间仿射两种切片，并证明它们共同给出可控制的压力。

新得到的是“受控尺度上的形状耗散足够小，则中心正则”。没有证明任意演化必然出现这种尺度。最后单独核算有限总耗散为何仍不足以排除指定中心的尺度集中。

## 1. 对象、附加条件与结论

单位黏性、无外力，\(Q_r=B_r(0)\times(-r^2,0)\)。与 RS 相同，\((u,p)\) 是 \(\overline{Q_1}\) 的某个时空邻域上的局部适当弱解：局部能量类、\(p\in L^{3/2}\)、分布 NS、无散度及局部能量不等式。记
\[
 \mathsf A(r)=r^{-1}\operatorname*{ess\,sup}_{-r^2<t<0}\int_{B_r}|u|^2,
 \quad\mathsf E(r)=r^{-1}\int_{Q_r}|\nabla u|^2,
 \quad\mathsf D(r)=r^{-2}\int_{Q_r}|p-(p)_{B_r}(t)|^{3/2}.
 \tag{SC.1}
\]
本节 \(G_{ij}=\partial_j u_i\)，\(q=|G|_F\) 是完整梯度的模，不是应变模。令
\[
 d(G)=\operatorname{dist}_F(G,\{\text{全部实秩至多一矩阵}\}),\qquad
 \Theta(G)=\begin{cases}d(G)G/q^{3/2},&q>0,\\0,&q=0.\end{cases}
 \tag{SC.2}
\]
这是同一梯度的连续矩阵函数；不选定轴或奇异向量。其模为 \(F=d/\sqrt q\)，且
\[
 |\Theta|^2=d^2/q,\qquad |\Theta|^4\le q^2.
 \tag{SC.3}
\]
零处分式取0。第二个不等式给能量类中自动成立的 \(\Theta\in L^4\) 零阶界，但不自动给它的弱导数。

**命题 SC-A（局部证明，PROVED IN STATED SCOPE / CONDITIONAL）。** 对每个有限 \(M>0\)，存在 \(\varepsilon_\Theta(M)>0\)，使以下条件蕴含 \((0,0)\) 正则：
\[
 \mathsf A(1)+\mathsf E(1)+\mathsf D(1)\le M,\quad
 \Theta(\nabla u)\in L^2((-1,0);H^1(B_1)),\quad
 \int_{Q_1}|\nabla_x\Theta(\nabla u)|^2<\varepsilon_\Theta(M).
 \tag{SC.4}
\]
这里是整个球上的弱空间导数，包括梯度为零的集合；不是只在非零集合写一个形式表达式。一般适当弱解的版本明确保留这个附加 Sobolev 条件，不要求终点前光滑。正则仍指速度在某个后向内柱本质有界；没有有效阈值或半径模量。

**推论 SC-B（光滑前终端形状耗散）。** 对满足同一适当性与 M 上界、并在开柱 \(Q_1\) 内光滑的解，令 \(B=G/q\) 于 \(q>0\)，以及
\[
 \Gamma=\mathbf1_{\{q>0\}}q|\nabla_x B|^2.
 \tag{SC.5}
\]
存在 \(\varepsilon_\Gamma(M)>0\)，使 \(\int_{Q_1}\Gamma<\varepsilon_\Gamma(M)\) 蕴含中心正则。光滑性不要求跨过顶端0。此结论允许首次候选奇点的前终端解；不将 SC.5 的经典写法自动扩张到所有适当弱解。

## 2. 为什么不能只保留秩一，以及跨零的导数

固定 \(a>0\)，局部精确 NS 解
\[
 u=a(x_1,-x_2,0),\qquad p=-a^2(x_1^2+x_2^2)/2
 \tag{SC.6}
\]
具有恒定秩二梯度、\(d^2=a^2\)，但 \(\Gamma=0\)。其 \(\mathsf A(1)=8\pi a^2/15\)、\(\mathsf E(1)=8\pi a^2/3\)、\(\mathsf D(1)=C_p a^3\)，其中 \(C_p\) 是固定正有限常数。选取足够小且固定的 a，可满足任意所给正 M。常值解序列就否定“小形状耗散必迫使秩一极限”。它是正则解，不是小耗散正则性的反例，也不具有全空间有限能量或周期边界。

现在证明 SC-B 如何进入 SC-A。以下计算仅在光滑 G 的 \(q>0\) 上进行。取 \(\tau=d(G)/q=d(B)\)。梯度每一行无旋，给 GD.6 的兼容性估计
\[
 \tau^2|\nabla q|^2\le2q^2|\nabla B|^2.
 \tag{SC.7}
\]
具体地，行向量满足 \(b_i\times\nabla q=q\operatorname{curl}b_i\)；平方求和后左边为 \(\nabla q^{T}(I-B^TB)\nabla q\)。其最小特征值是 \(1-s_1(B)^2=\tau^2\)，右边至多为 \(2q^2|\nabla B|^2\)。这里 \(|B|_F=1\)；没有把不可压缩性当成全部兼容条件。

距离函数的 Lipschitz 性给 \(|\nabla\tau|\le|\nabla B|\) 几乎处处。由 \(F=\sqrt q\tau\)，得到
\[
 |\nabla F|\le(1+1/\sqrt2)\sqrt q|\nabla B|,\qquad
 |\nabla(FB)|\le C_0\sqrt q|\nabla B|,
 \quad C_0=2+1/\sqrt2.
 \tag{SC.8}
\]
这一步与 GD 的标量 F 估计相容，但保留矩阵方向，才能识别非零仿射分支。

为跨过 \(q=0\)，取 \(\Theta_\delta=(F-\delta)_+B\)，零处定义0。其非零集合满足 \(q>\delta^2\)，故对光滑 G 是合法的局部 Lipschitz 复合。\(|\Theta_\delta-\Theta|\le\delta\)，而乘积法则及 SC.8 给整个球上的几乎处处界 \(|\nabla\Theta_\delta|\le C_0\sqrt\Gamma\)。先在离顶端正距离的柱上计算，再用同一有限积分取极限；弱 Sobolev 紧性与下半连续性给
\[
 \Theta\in L^2_tH^1_x(Q_1),\qquad
 \int_{Q_1}|\nabla\Theta|^2\le C_0^2\int_{Q_1}\Gamma.
 \tag{SC.9}
\]
SC.3 控制零阶项。弱导数在整个球上得到，不漏掉零集或截断边界。因而可取 \(\varepsilon_\Gamma=\varepsilon_\Theta/C_0^2\)。这不需要全局 Hardy 压力界；该全局界只在 GD 的实际总耗散估计中使用。

## 3. 小导数极限：逐时间切片分类

反设 SC-A 不成立。固定 M，选中心均非正则的适当解序列，满足同一上界和附加 Sobolev 条件，而 \(\int|\nabla\Theta_n|^2\to0\)。如 RS.4–5，固定 \(P_n=p_n-(p_n)_{B_1}(t)\)，在 \(B_R\times J\)、\(R=3/4\)、\(J=(-3/4,0)\) 上取子列，使
\[
 u_n\to u\text{ 强 }L^2\text{、强 }L^3,\quad
 G_n\rightharpoonup G=\nabla u\text{ 弱 }L^2,\quad
 P_n\rightharpoonup P\text{ 弱 }L^{3/2}.
 \tag{SC.10}
\]
依据是局部能量插值、方程给出的 \(\partial_tu_n\in L^{3/2}_tW^{-1,3/2}_x\) 一致界及 Aubin–Lions。极限保留局部能量类、分布 NS 和开柱内适当性；不要求它在正时间延拓。弱 L^(3/2) 压力乘强 L3 速度足以传递局部能量不等式中的压力项。

令 \(m_n(t)=(\Theta_n)_{B_R}(t)\)。空间 Sobolev–Poincaré 给
\[
 \|\Theta_n-m_n\|_{L^2(J;L^6(B_R))}\longrightarrow0.
 \tag{SC.11}
\]
取一个共同子列，使 SC.10 的强 L2 和 SC.11 同时在几乎所有时间切片强收敛。对该子列，Fatou 给
\[
 \int_J\liminf_n\|G_n(t)\|_{L^2(B_R)}^2\,dt\le M.
 \tag{SC.12}
\]
因此在几乎每个固定 t，可再取一个依赖该 t 的子列，使梯度切片 L2 有界。不能把 Fatou 说成所有切片上整个序列一致有界，也不需要找到同时适用于所有 t 的第二个子列。

固定这样的 t。由 SC.3，\(\Theta_n(t)\) 在 L4 有界，故均值有界；再取子列 \(m_n(t)\to C\)，其中 C 是常矩阵。SC.11 给 \(\Theta_n(t)\to C\) 强 L6。此处及以下只在这个切片子列上推论：

**C 为零。** 由 \(d_n^2=|\Theta_n|^2q_n\) 和 Hölder，
\[
 \|d_n(t)\|_2^2\le\|\Theta_n(t)\|_4^2\|q_n(t)\|_2\longrightarrow0.
 \tag{SC.13}
\]
同时 \(u_n(t)\to u(t)\) 强 L2、梯度切片 L2 有界。RS.6–7 的子式论证逐空间成立：\(|\operatorname{cof}G_n|\le|G_n|d_n\) 使余子式趋于0于 L1，子式的散度形式则传给 \(\nabla u(t)\)。所以 \(\operatorname{rank}G(t,x)\le1\) 几乎处处。没有使用梯度强收敛或非凸距离的弱下半连续性。

**C 非零。** 在 \(\Theta_n\ne0\) 上，方向 \(B_n=\Theta_n/|\Theta_n|\) 趋于 \(B_*=C/|C|\) 于测度，且反演公式为
\[
 q_n=\frac{|\Theta_n|^2}{d(B_n)^2},\qquad G_n=q_n B_n.
 \tag{SC.14}
\]
若 \(d(B_*)=0\)，则 SC.14 迫使 \(q_n\to\infty\) 于测度，违背该切片的 L2 有界性。故 \(d(B_*)>0\)，连续反演给 \(G_n\to G_*:=|C|^2B_*/d(B_*)^2\) 于测度。L2 有界再给弱 L2 极限是该常矩阵；也可先用一致 L1 可积性传分布极限。因此 \(\nabla u(t)=G_*\)，\(u(t,x)=G_*x+c(t)\) 几乎处处于整个连通球。

两种情况只证明如下结论，已经足够：对几乎每个 t，极限速度的空间切片或者梯度几乎处处秩至多一，或者在整个 \(B_R\) 仿射。它们可以在时间上切换。不宣称 \(\Theta_n\) 本身在时空强收敛到 \(\Theta(G)\)，不选取可测方向函数，也不从小耗散直接宣布 \(B\) 全域常值。

## 4. 两种切片共同给出受控的二次压力

在秩一切片上，\(\operatorname{tr}G=0\) 给 \(G^2=0\)。在仿射切片上，\(\operatorname{tr}(G^2)\) 空间恒定。直接定义可测函数
\[
 \beta(t)=|B_R|^{-1}\int_{B_R}\operatorname{tr}(G(x,t)^2)\,dx.
 \tag{SC.15}
\]
于是 \(\operatorname{tr}(G^2)=\beta(t)\) 几乎处处于 \(B_R\times J\)。不需要可测地标记两种分支。

极限满足 \(\operatorname*{ess\,sup}_t\int_{B_R}|u(t)|^2\le M\)。对于任意仿射切片 \(u=G_*x+c\)，球心为0给精确恒等式
\[
 \int_{B_R}|G_*x+c|^2
 =|B_R||c|^2+\frac{|B_R|R^2}{5}|G_*|_F^2.
 \tag{SC.16}
\]
故在该分支 \(|\beta|\le|G_*|^2\le5M/(|B_R|R^2)\)；另一分支 \(\beta=0\)。因此 \(\beta\in L^\infty(J)\)。这一步使用速度的切片能量上界，不能以累计梯度耗散代替。

局部 H1 的无散度速度经空间光滑化给分布压力恒等式 \(-\Delta P=\operatorname{tr}(G^2)=\beta(t)\)。令
\[
 p_0(x,t)=-\beta(t)|x|^2/6,\qquad P_h=P-p_0.
 \tag{SC.17}
\]
于是 \(P_h\) 逐时调和；\(p_0\) 及其所需空间导数在固定球上有界。它们不必时间光滑。

取 \(I=(-1/2,0)\)，令 \(h=\int_{-1/2}^t\nabla P_h(x,s)\,ds\)、\(v=u+h\)。调和内估计使 h 及全部空间导数在 \(B_{2/3}\times I\) 有界；\(\operatorname{div}h=\Delta h=0\)。分布方程为
\[
 \operatorname{div}v=0,\qquad
 v_t-\Delta v+v\cdot\nabla v=\mathcal F,
 \quad\mathcal F=h\cdot\nabla v+u\cdot\nabla h-\nabla p_0\in L^2.
 \tag{SC.18}
\]
这里仅积分调和压力梯度；如果把全部 \(\nabla P\) 放入 h，会失去无散度校正。新增的 \(-\nabla p_0\) 有界，不要求 \(\beta'\) 存在。

RS.12–16 的小幂测试现在原样适用于 SC.18：\(e=1/2\)，保留正扩散项及 \(\int|v|w^{3/2}\) 截止项，\(|v|^{3/2}|\nabla v|\) 的 Hölder 指数和19/20小于1，\(\mathcal F\in L^2\) 足够控制力项。先固定顶时 \(\tau<0\) 再去光滑化，使用与 \(\tau\) 无关的父柱界，最后趋于0；无需未来延拓。

三个固定内柱上的严格强可积性提升仍是 \(10/3\to15/4\to9/2\to21/4\)，相应弱端点是 \(35/9,55/12,65/12\)。这给
\[
 u\in L^{21/4}(Q_{1/4}),\qquad
 C_u(r):=r^{-2}\int_{Q_r}|u|^3\le K_u r^{1/7}\longrightarrow0.
 \tag{SC.19}
\]
依赖的是 RS 已写出的 O'Leary 小幂适配，不是直接援引其压力梯度定理，也不是断言任意 L2 外力 NS 解有界。

## 5. 把小量传回原适当解

如 RS.17，固定 \(\xi\in C_c^\infty(B_{3/4})\)、在 \(B_{1/2}\) 为一，令 \(\pi_n=\mathcal R_i\mathcal R_j(\xi u_{n,i}u_{n,j})\)、\(\pi=\mathcal R_i\mathcal R_j(\xi u_i u_j)\)、\(q_n^{\mathrm h}=P_n-\pi_n\)。这处上标区分调和余压和 SC.14 的梯度模。强速度 L3 给 \(\pi_n\to\pi\) 强 L^(3/2)，\(q_n^{\mathrm h}\) 在 \(B_{1/2}\) 调和且一致有界于时空 L^(3/2)。

极限 \(\pi\) 不一定调和，正确的是 \(\pi-p_0\) 调和。分解为
\[
 P_n=(\pi_n-\pi)+(\pi-p_0)+q_n^{\mathrm h}+p_0.
 \tag{SC.20}
\]
两个调和部分按 RS.18 给归一化压力积分 \(K(M)r\) 的界；二次部分给
\[
 r^{-2}\int_{Q_r}|p_0|^{3/2}
 \le C\|\beta\|_\infty^{3/2}r^6.
 \tag{SC.21}
\]
这里 \(|p_0|^{3/2}\) 的空间因子为 \(|x|^3\)，空间积分为 O(r6)，时间长度 r² 与外面的 r^(-2) 抵消。没有假设调和部分时间 L∞。

先固定 \(r<1/4\) 再令 n 趋于无穷，SC.19–21 给
\[
 \limsup_n r^{-2}\int_{Q_r}(|u_n|^3+|P_n|^{3/2})
 \le K_u r^{1/7}+K(M)(r+r^6).
 \tag{SC.22}
\]
选一个足够小且固定的 r，再选足够大的 n，即低于无外力单尺度 CKN 阈值。该接口见 [Gustafson–Kang–Tsai，Theorem 2.2](https://arxiv.org/html/math/0607114v1)。对定义在中心邻域的原适当解应用它，中心正则，与反设矛盾。SC-A 得证，SC.9 随即给 SC-B。没有交换两个极限，或用某个随半径变化的未知阈值作普适阈值。

## 6. 仍未得到的指定中心好尺度

通常的 NS 缩放为 \(u_r(y,s)=r u(x_0+ry,t_0+r^2s)\)。于是 \(G_r=r^2G\)、\(d_r=r^2d\)、\(\Theta(G_r)=r\Theta(G)\)、\(B_r=B\)，并且
\[
 \int_{Q_1}|\nabla_y\Theta(G_r)|^2
 =r^{-1}\int_{Q_r(z_0)}|\nabla_x\Theta(G)|^2,\qquad
 \int_{Q_1}\Gamma_r=r^{-1}\int_{Q_r(z_0)}\Gamma.
 \tag{SC.23}
\]
因此 SC-B 的逆否命题只说：若中心奇异，则在每个同时满足 \(\mathsf A(r)+\mathsf E(r)+\mathsf D(r)\le M\) 的合格前终端尺度上，\(\int_{Q_r}\Gamma\ge\varepsilon_\Gamma(M)r\)。没有证明存在任意小的共同 M 合格尺度。

即使所有这些尺度都有共同 M，有限的未归一化总耗散仍不与上述线性 r 下界矛盾。以几何半径 \(r_j=\theta^j r_0\)、\(0<\theta<1\) 为例，\(\sum_j r_j<\infty\)。而且嵌套柱的积分一般不能当作不重叠区域的积分相加。

可相加的独立空间时间壳也必须先另证下界。例如 RS 的 \(d^2\) 在外尺度有 \(\int_{Q_r}d^2\ge\epsilon r\)，内尺度有 \(\mathsf E(\theta r)\le M\)，才可相减得到
\[
 \int_{Q_r\setminus Q_{\theta r}}d^2\ge(\epsilon-M\theta)r.
 \tag{SC.24}
\]
取足够小的固定 \(\theta\) 可使其为正；这些真正互不重叠的壳下界仍按 r 求和有限。对于 \(\Gamma\)，\(\mathsf E\) 不提供相应内柱上界；不能把 SC.24 的减法照搬。有限非负测度的这些可能性只是说明仅有这些积分上下界不构成矛盾，不是在构造奇异 NS 解。

GD 的 \(\int\Gamma<\infty\)、SG 的加权全应变梯度界、LK 的线性余子式测度控制都没有在这里变成超出其原范围的新估计。尤其 LK 的弱测度终端迹不是强梯度迹，也不排除所需的尺度集中。这一节关闭的是“形状耗散小量如何导致局部正则”的紧性环节，不是“任意演化为何产生小量”的动力学环节。

下一问题应固定为：能否从同一真实 NS 演化的局部形状熵方程得到跨尺度衰减或独立的、不可求和的集中成本，并同时控制 A、E、D？应先写出全部输运、截止与压力项，核对缩放和符号；若有尚未控制的临界项，就保留为开放输入。不能把 SC 的另一次条件改写或有限尺度实验当作这个动力学证明。

## 7. 依赖与核查范围

本稿实际使用并完整核对 GD 的兼容性与跨零论证，以及 RS 的紧性、梯度子式、小幂测试和压力转移。SG 与 LK 全文用于判断既有总量的准确范围，不把其不同矩阵方向或权重混入 SC.5。源文件与确切审读版本由审计、清单绑定；历史冻结文件不修改。

外部正则性、Sobolev、Aubin–Lions、Riesz 与调和内估计沿用 RS 已列来源。本轮再次核对 GKT 定义2.1及定理2.2。小幂方法见 [O'Leary 1998，§2](https://ejde.math.txstate.edu/Volumes/1998/12/Oleary.pdf)，本轮沿用前节实际审读的适配，不重复计为新一轮 PDF 全文审计。参与式 AI 推导与审读不等于真人同行评审；有界检索不能证明原创性。

没有仿真、DGX、数值证书或科学附图；不生成读者 HTML/PDF、公开摘要或阶段 recap。完成包只在审读和冻结后一次移交固定发布任务作 PRIVATE_ARCHIVE，不进行或监督发布。
