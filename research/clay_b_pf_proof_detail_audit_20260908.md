# PF 条件准则的证明细节复核

2026-09-08。PFA，PRIVATE_CORE。既有证明的补充核验，不新增定理、小节成果或发布编号。一般三维 NS 仍 OPEN / NOT CLAY。

本轮检查 PF 中两个容易遗漏的环节：逐时间切片选择是否足以控制极限的压力源，以及能量类弱方程是否允许小幂测试。结论是：在原来列明的条件内，下面的论证可以闭合，未发现必须撤回 PF 的错误。这不是全体依赖的独立重新认证，也不产生任意演化上的好尺度。

冻结原稿不改。本文补充 [PF](clay_b_pressure_free_shape_criterion_20260908.md) §3–5，使用 [SC](clay_b_shape_dissipation_compactness_20260908.md) 的空间分类和 [RS](clay_b_rank_one_squared_compactness_20260908.md) 的小幂论证。[WE](clay_b_weak_gradient_entropy_20260908.md) 的整个球上弱导数存在仍是既有输入；此次读取不等于重新独立认证其全部上游论证。

## 1. 固定共同子列之后，才逐片选择

记 \(B=B_{3/8}\)、\(J=(-1/2,0)\)、\(G_n=\nabla u_n\)、\(\Theta_n=d(G_n)G_n/|G_n|^{3/2}\)，零点取零，\(m_n(t)=(\Theta_n)_{B}(t)\)。沿用 PF 的局部 Leray 分解 \(u_n=v_n+h_n\) 及共同动能、梯度耗散上界 M。先由两项时空强收敛取同一子列，使
\[
 \sum_n\int_J\bigl(\|v_n(t)-v(t)\|_{L^2(B)}^2
       +\|\Theta_n(t)-m_n(t)\|_{L^6(B)}^2\bigr)dt<\infty.
 \tag{PFA.1}
\]
于是两项在几乎每个时间切片趋零。对这个已经选定的子列应用 Fatou，得到 \(\liminf_n\|G_n(t)\|_2^2<\infty\) 几乎处处；再排除所有 n 的能量切片、空间 Sobolev 切片和调和校正空间界的可数个零测例外。

固定剩余的 t，选取依赖 t 的子列，使 \(\sup_n\|G_n(t)\|_2=L_t<\infty\)。进一步由内域上 h_n 的统一 C2 界，取 \(h_n(t)\to H_t\) 强 C1，从而
\[
 u_n(t)\to U_t=v(t)+H_t\text{ 强 }L^2(B),\quad
 G_n(t)\rightharpoonup\nabla U_t\text{ 弱 }L^2(B),\quad
 \|U_t\|_2^2\le M,\quad\|\nabla H_t\|_\infty\le K(M).
 \tag{PFA.2}
\]
U_t、H_t 无散度，H_t 调和。L_t 不需要统一，也不需要令 H_t 等于 h_n 的时间弱*极限。

由 \(\|\Theta_n\|_4^4\le\|G_n\|_2^2\)，均值 m_n 有界；再取 \(m_n\to C\)，故 \(\Theta_n\to C\) 强 L6。

若 C=0，则
\[
 \|d(G_n)\|_2^2\le\|\Theta_n\|_4^2\|G_n\|_2\to0,
 \qquad\|\operatorname{cof}G_n\|_1
       \le\|G_n\|_2\|d(G_n)\|_2\to0.
 \tag{PFA.3}
\]
二阶子式可写为
\[
 \partial_a U_i\,\partial_b U_j-\partial_b U_i\,\partial_a U_j
 =\partial_a(U_i\partial_b U_j)-\partial_b(U_i\partial_a U_j).
 \tag{PFA.4}
\]
分布配对中的速度强 L2、梯度弱 L2，故子式传极限，得到 \(\operatorname{rank}\nabla U_t\le1\)。这不是非凸距离的弱下半连续性论证。

若 C≠0，则在测度趋零的例外集之外，令 \(B_n=\Theta_n/|\Theta_n|\to B_*=C/|C|\)，有
\[
 |G_n|=|\Theta_n|^2/d(B_n)^2.
 \tag{PFA.5}
\]
若 \(d(B_*)=0\)，则 \(|G_n|\to\infty\) 于测度，与切片 L2 界的 Chebyshev 估计矛盾。因此 d(B_*)>0，反演给 G_n 于测度收敛至常矩阵 G_*。切片 L2 界使其强 L1 收敛：对 \(E_n=\{|G_n-G_*|>\eta\}\)，
\[
 \|G_n-G_*\|_1\le\eta|B|
 +(L_t+|G_*||B|^{1/2})|E_n|^{1/2}.
 \tag{PFA.6}
\]
先 n→∞ 再 η↓0。由分布极限唯一性，\(\nabla U_t=G_*\)，U_t 空间仿射。这里仍允许 \(|G_n|^2\) 的集中缺陷，没有证明梯度强 L2 紧性。

## 2. 最终压力源界不使用切片梯度常数

秩一且迹零时 \((\nabla U_t)^2=0\)。仿射分支用球心为零的恒等式
\[
 \int_B|Lx+c|^2=|B||c|^2+|B|R^2|L|^2/5,
 \qquad |\operatorname{tr}(L^2)|\le|L|^2,
 \tag{PFA.7}
\]
得到 \(|\beta_t|:=|\operatorname{tr}((\nabla U_t)^2)|\le C_0(M)=5M/(|B|R^2)\)。写 V=∇v、Z_t=∇H_t，则
\[
 |\operatorname{tr}(V^2)|
 \le C_0(M)+K(M)^2+2K(M)|V|.
 \tag{PFA.8}
\]
违反此式的集合只由可测的 V 和固定常数定义；几乎每个时间切片的违反集零测，Tonelli 给时空违反集零测。不需要可测地选择 H_t、C 或分类标签。由于 V∈L2，PFA.8 给 \(\operatorname{tr}(V^2)\in L^2(B\times J)\)。这个标量控制不是 V∈L4，也不是原速度序列压力源的统一 L2 控制。

## 3. 小幂测试的合法极限顺序

PF §4 的调和压力校正给出的实际方程是
\[
 w_t-\Delta w+w\cdot\nabla w=F,\qquad
 \operatorname{div}w=0,\qquad
 w\in L^\infty_tL^2_x\cap L^2_tH^1_x,\quad F\in L^2.
 \tag{PFA.9}
\]
这里只在固定内柱使用它；不把 w 当成无外力 NS 解，也不另假设分量适当性或重整化性质。记一个分量 a=w_i、s=(a−ℓ)_+、ℓ≥1。设
\[
 \beta_\delta(s)=\sqrt{s+\delta}-\sqrt\delta,\quad
 B_\delta(s)=\int_0^s\beta_\delta(r)\,dr,\quad
 \Psi_\delta(s)=(s+\delta)^{3/4}-\delta^{3/4}.
 \tag{PFA.10}
\]
选择固定内域空间截止及底部时间截止 ζ；不在趋近顶端0时另加时间截止。先限制到任意严格内部顶时 τ<0，固定 δ>0，对整个分量方程作时空卷积，再测试 \(\beta_\delta((a_\epsilon-\ell)_+)\zeta^2\)。阈值处可对凸原函数 \(B_\delta((a-\ell)_+)\) 作光滑凸逼近，用其导数测试；不是把凹平方根本身当作凸函数。最后使用 Sobolev 函数在常值水平集上的梯度为零。

关键是先把对流项解释为函数 N=w·∇w∈L5/4，而不是直接把 w⊗w∈L5/3 与奇异测试梯度配对。固定 δ，局部去卷积有
\[
 N_\epsilon\to N\text{ 强 }L^{5/4},\qquad
 \beta_\delta((a_\epsilon-\ell)_+)
       \to\beta_\delta(s)\text{ 强 }L^5.
 \tag{PFA.11}
\]
第二项由平方根的1/2-Hölder界和 a_ε→a 强 L5/2 得到。因此非线性乘积收敛；F 项同样由强 L2 及测试函数强 L2 通过。固定 δ 的扩散链式法则由空间 H1 强逼近通过，时间原函数由卷积方程导出，不预设弱解已有强顶端迹。

去卷积之后，\(N_i\beta_\delta(s)=w\cdot\nabla B_\delta(s)\)。该乘积可积，因为
\[
 \frac{1+1/2}{10/3}+\frac12=\frac{19}{20}<1.
 \tag{PFA.12}
\]
对无散度 w 作空间分部积分，保留 \(w\cdot\nabla(\zeta^2)\,B_\delta(s)\)；空间逼近的乘积极限使用相同的可积余量。

再令 δ↓0。对 s>0 有与 δ、ℓ 无关的精确界
\[
 \frac{\beta_\delta(s)^2}{\beta_\delta'(s)}
 =\frac{2\sqrt{s+\delta}\,s^2}
       {(\sqrt{s+\delta}+\sqrt\delta)^2}
 \le2s^{3/2},\quad
 \beta_\delta'(s)|\nabla s|^2
 =\frac89|\nabla\Psi_\delta(s)|^2.
 \tag{PFA.13}
\]
所以扩散交叉项的 Young 余项被 \(C\int s^{3/2}|\nabla\zeta|^2\) 控制。正扩散给 Ψ_δ 的弱 H1 紧性；其极限为整个区域上的 s^{3/4}，无需删除阈值集。时间原函数单调趋于 \((2/3)s^{3/2}\)。取几乎处处的顶端切片 τ，经 Fatou 和弱下半连续性，得到
\[
 \|s^{3/4}\zeta\|_{V^2}^2
 \le C_\zeta\left(\int s^{3/2}
            +\int |w|s^{3/2}+\int |F|s^{1/2}\right).
 \tag{PFA.14}
\]
V2 为局部 L∞L2 与空间梯度 L2 的能量范数；全部积分在同一父柱。右边界与内部顶时 τ 无关，故可取本质上确界及 τ↑0。对负分量使用 a=−w_i，漂移仍为同一个无散度 w。这里把原稿“任意顶端切片”的弱解论证明确解释为几乎处处切片，已足够得到结论。

## 4. 三次提升及传回原解

若父柱 w∈L^β、β≥10/3，令 N_β=∫|w|^β。PFA.14 右边三项依次不超过常数乘
\[
 N_\beta\ell^{3/2-\beta},\qquad
 N_\beta\ell^{5/2-\beta},\qquad
 \|F\|_2 N_\beta^{1/2}\ell^{1/2-\beta/2}.
 \tag{PFA.15}
\]
能量空间到 L10/3 的抛物 Sobolev 估计作用于 s^{3/4}ζ。在 a>2ℓ 的内柱集合上，左边至少为常数乘 \(\ell^{3/2}|\{a>2\ell\}|^{3/5}\)。于是得到弱端点
\[
 \alpha(\beta)=\min\{\tfrac53(\beta-1),\tfrac53(\beta/2+1)\}.
 \tag{PFA.16}
\]
层蛋糕积分只取严格小于 α 的强指数。三个固定内柱上依次为
\[
 10/3\to15/4\to9/2\to21/4,
 \qquad \alpha=35/9,\ 55/12,\ 65/12.
 \tag{PFA.17}
\]
校正 k 有界，因此 v=w−k 也属于 L21/4。缩小柱上的 Hölder 估计给 \(r^{-2}\int_{Q_r}|v|^3\le C_v r^{1/7}\to0\)。最后先固定 r、再取 n：v_n 强 L3，h_n 统一有界，给 \(\limsup_n r^{-2}\int_{Q_r}|u_n|^3\le4C_v r^{1/7}+C(M)r^3\)。无需 h_n 时间强收敛或原压力强紧性。

所用外部接口仍是 [Kwon v3](https://arxiv.org/html/2104.03160v3) 的局部 Leray 分解和速度小量正则性，分别见 Lemma 2.5 与 Theorem 1.4。后者取两个指数均为3。把 Q_r 缩放至 Q_2 后，速度 L3 范数的三次方为 \(4r^{-2}\int_{Q_r}|u_n|^3\)，从而推出各原解中心正则。本文没有把调和校正的时间光滑性作为文献结论使用。

## 5. 审查范围与下一步边界

基准提交为 `7c216e458e478f6bfd51529d886e4ba1f55f5e57`。主任务实际全文读取 PF（173行）、SC（219行）、RS（219行）、WE（222行），独立复算本文的分类、阈值极限及指数。两位协作者分别独立重证空间分类和弱小幂模块；均参与本文论证，不称完全非作者或真人同行评审。最终版本的审读回执另记。

本轮主任务实际核读 Kwon v3 的 Definition 1.1、Theorem 1.4、Definition 2.1、Remarks 2.2–2.3、Definition 2.4、Lemma 2.5 陈述及证明、Remarks 2.6–2.7、§4 全部。未在本轮重新逐行审查其§3及引用的外部缺陷测度引理，不称整篇或全部依赖重新认证。未做充分新颖性检索。

这次完成的是既有条件准则的内部证明细化，不是新的无条件临界估计。PF 的联合条件仍是同一尺度上的 A+E≤M 和 K<ε_PF(M)。M 随尺度增大而阈值未知时，K趋零本身也不足以套用；有限总耗散同样不保证指定中心出现合法好尺度。

不继续把条件准则的相邻审计、压力导数改名或初始时反例变体计作新成果。下一项动力学候选仍未选定；下一次实质研究应先明确同一实际前终端解上的目标估计、所有尺度和已有输入，再检验是否获得联合好尺度、严格尺度增益或独立不可求和成本。允许探索未证估计，但在证明闭合前不把它当作已付输入。没有仿真、DGX、图档、新发布、网页制作或发布监督。
