# 跨模交换与圆柱环带上的能量类估计

2026-09-22。PRIVATE_CORE / PROVED IN STATED SCOPE / OPEN / NOT CLAY。

从 `45f845182115c047e061c98ede3cc673298a1c38` 继续。这里不重算已核角模谱隙或 SA.9 条件吸收，而直接处理 SA.6 的实际交换。得到两点：标量加权不能免费消除内部交换；远离轴线时，有限低角带宽确实允许把四次梯度系数改为带显式 \(N/R\) 因子的平方系数。后者只解决固定环带的一个估计问题，没有得到终端尺度一致性或一般正则性。

## 1. 相同输入和可检验问题

沿用 [SA 笔记](../civ_strain_absorption_20260920/research-note.md) 的同一局部光滑无力 NS 解、固定正黏性、固定周期提升与旋转不变球。令 \(u=v+w\)、\(v=\Pi u\)，固定角阈值 \(N\ge2\)，\(z=P_Hw\)、\(\ell=P_Lw\)，\(P_L=I-\Pi-P_H\)，\(q=p-\bar p=q_H+q_L\)。所有投影都是关于固定轴的协变角投影。终点前光滑性不自动给终端统一界。

先检验 \(E_H+\alpha E_L\) 中的真实符号抵消，再检验有限角带宽能否改善 SA.11。两项结束条件分别是完整交换恒等式、以及常数显式依赖 \(N,R\) 的估计。没有将未知临界范数加入已有输入。CIV 的结构界只用于后面的条件尺度比较，本节不调用其正则性定理；也不假设原解满足精确核心或一致 \(C^3\) 余项。

## 2. 低高模的精确交换与边界

令 \(a=\chi^2\)，\(\chi\) 为旋转不变紧支截止，可光滑依赖时间。定义 \(E_L=\int a|\ell|^2\)、\(D_L=\int a|\nabla\ell|^2\)，高模同理，且 \(A_L=\int a(\ell\otimes\ell):S(v)\)。低模方程与测试给

\[
\frac12E_L'+\nu D_L=-A_L+T_L+B_L,
\quad T_L=-\int a\ell\cdot(w\cdot\nabla)z,
\tag{CM.1}
\]

\[
B_L=\frac12\int(a_t+\nu\Delta a+u\cdot\nabla a)|\ell|^2
 +\int q_L\ell\cdot\nabla a.
\tag{CM.2}
\]

与 SA.6 的 \(T_H=-\int az\cdot(w\cdot\nabla)\ell\) 相加，利用 \(\operatorname{div}w=0\) 得

\[
T_H+T_L=C_\chi,
\qquad C_\chi=\int(\ell\cdot z)w\cdot\nabla a.
\tag{CM.3}
\]

\(\int a\ell\cdot z=0\) 不意味着 \(C_\chi=0\)。虽然 \(\partial_\theta a=0\)，系数 \(w_r\partial_ra+w_3\partial_3a\) 一般仍依赖角度，不能用低高正交删除。

对任何仅依时间的 \(C^1\) 权 \(\alpha\)，完整恒等式为

\[
\begin{aligned}
\frac12(E_H+\alpha E_L)'+\nu(D_H+\alpha D_L)
={}&-A_H-\alpha A_L+(1-\alpha)T_H+\alpha C_\chi\\
&+B_H+\alpha B_L+\frac{\alpha'}2E_L.
\end{aligned}
\tag{CM.4}
\]

若置 \(X=T_H-C_\chi/2\)，内部交换为 \((1-\alpha)X\)。只有等权 \(\alpha=1\) 能在没有额外信息时精确去掉它。这时旋转不变权下的速度、梯度、平均应变正交给 \(E_H+E_L=E_w\)、\(D_H+D_L=D_w\)、\(A_H+A_L=A_w\)，并且

\[
B_H+B_L+C_\chi=B_w.
\tag{CM.5}
\]

这里压力交叉项确实为零，因为与 \(\nabla a\) 点乘保持相应标量角模；完整输运的交叉项却正是 \(C_\chi\)。因此等权只恢复原来的全余项局部能量，不新增高模控制。

若在 \(E_L>0\) 处依解选择 \(\alpha'=-2(1-\alpha)X/E_L\)，则 \(1-\alpha\) 含因子 \(\exp(\int2X/E_L\,dt)\)。现有输入不控制该有符号积分，也不保证权正、有界或在 \(E_L\to0\) 时无退化。这只否定无需新估计的标量权消项，不否定另有真正的动态抵消。

## 3. 圆柱环带：平方梯度系数成立

现在固定 \(0<c<C<\infty\) 和 \(R>0\)，要求

\[
\operatorname{supp}\chi\subset\{cR<r<CR\},
\tag{CM.6}
\]

且截止在经向 \((r,x_3)\) 平面紧支。它是避开轴线的圆柱环带条件；仅有球壳 \(|x|\sim R\) 不够。

记 \(K_\ell=\|\nabla\ell\|_{L^2(\operatorname{supp}\chi)}\)，\(F_H=\int|\nabla\chi|^2|z|^2\)。在圆柱正交框架中，完整梯度矩阵是

\[
G=\begin{pmatrix}
\partial_r\ell_r&r^{-1}(\partial_\theta\ell_r-\ell_\theta)&\partial_3\ell_r\\
\partial_r\ell_\theta&r^{-1}(\partial_\theta\ell_\theta+\ell_r)&\partial_3\ell_\theta\\
\partial_r\ell_3&r^{-1}\partial_\theta\ell_3&\partial_3\ell_3
\end{pmatrix}.
\tag{CM.7}
\]

它的 Frobenius 范数就是 \(|\nabla\ell|\)，这些框架分量仍具有 \(1\le|m|<N\) 带宽；若改写成固定 Cartesian 矩阵，角频会有固定移位，不能误称带宽完全不变。角向有限维 Cauchy–Schwarz 给

\[
\sup_\theta|G(r,\theta,x_3)|\le C_0\sqrt N\,
\|G(r,\cdot,x_3)\|_{L^2_\theta}.
\tag{CM.8}
\]

设 \(b(r,x_3)=\|\chi z(r,\cdot,x_3)\|_{L^2_\theta}\)。不对高模 \(z\) 使用有限带宽。Hilbert 范数弱导数满足
\(|\nabla_{r,3}b|\le\|\nabla_{r,3}(\chi z)\|_{L^2_\theta}\)。零延拓到经向平面后，二维 Ladyzhenskaya 给 \(\|b\|_4^2\le C\|b\|_2\|\nabla b\|_2\)。用 \(dx=r\,dr\,d\theta\,dx_3\) 和 CM.6 比较权重，得到

\[
\left|\int\chi^2(z\otimes z):\nabla\ell\right|
\le C_{c,C}\sqrt{\frac NR}\,K_\ell E_H^{1/2}(D_H+F_H)^{1/2}
\le\varepsilon\nu(D_H+F_H)
 +C_{\varepsilon,c,C}\frac{N}{\nu R}K_\ell^2E_H.
\tag{CM.9}
\]

具体权重因子是：角积分后有 \(R\)，而梯度低模的二维 \(L^2\)、\(b\) 的二维 \(L^2\) 及其梯度各贡献 \(R^{-1/2}\)，最终为 \(R^{-1/2}\)。所有截止导数已显式放在 \(F_H\)；常数不隐藏 \(N,R,\nu\) 或截止导数。

这是固定环带上不同于 SA.11 的有效估计：系数只需梯度平方可积，不要求四次可积。它不代表对任意参数逐点都比 SA.11 更小，也不覆盖轴线。

## 4. 低模注入不能省略

令 \(F_L=\int|\nabla\chi|^2|\ell|^2\)。对 SA.6 第二项，把角向有限带宽只用于 \(\ell\)，然后分别对 \(\|\chi z\|_{L^2_\theta}\)、\(\|\chi\ell\|_{L^2_\theta}\) 作二维插值，得

\[
\left|\int\chi^2z\cdot(\ell\cdot\nabla)\ell\right|
\le C_{c,C}\sqrt{\frac NR}\,K_\ell(E_HE_L)^{1/4}
\big[(D_H+F_H)(D_L+F_L)\big]^{1/4}.
\tag{CM.10}
\]

因而完整交换满足

\[
|T_H|\le\varepsilon\nu(D_H+D_L+F_H+F_L)
 +C_{\varepsilon,c,C}\frac{N}{\nu R}K_\ell^2(E_H+E_L).
\tag{CM.11}
\]

CM.11 引入了低模能量和耗散，不能只放回高模方程就声称全部被其左侧吸收。若放入正权耦合能量，还须保留 CM.4 的低模平均应变、\(C_\chi\)、压力及全部截止项。

角频选择还给一个精确局部事实：令 \(a_<\) 保留 \(|m|<\lceil N/2\rceil\) 的 \(\ell\)，\(b_>=\ell-a_<\)，则 \(P_H[(a_<\cdot\nabla)a_<]=0\)，且

\[
P_H[(\ell\cdot\nabla)\ell]
=P_H[(\ell\cdot\nabla)b_>+(b_>\cdot\nabla)a_<].
\tag{CM.12}
\]

柱坐标连接项也只相加角频，故没有遗漏模式偏移。至少一个输入接近阈值，但这项选择本身没有给出新的终端积分界；把导数转移到 \(z\) 时还必须计算新的截止项，不能把 CM.12 直接当作 \(N^{-1}\) 的动态小量。

## 5. 缩尺度检验与未闭合条件

固定 \(N,R\) 时，\(K_\ell^2\) 可由原能量类控制。若沿 SA.10 的条件 CIV 尺度，在每个二进窗固定 \(R_j\asymp\sqrt{s_j}\)、\(N_j\asymp s_j^{-h/2}\)，则该系数的时间积分为

\[
\Gamma_j=C\frac{N_j}{\nu R_j}\int_{I_j}K_{\ell,j}^2dt.
\tag{CM.13}
\]

逐窗一致界仍需 \(\int_{I_j}K_{\ell,j}^2dt\lesssim\nu R_j/N_j\)。普通总耗散有限不给这个衰减率；即使另有 \(R_j^{-1}\int K_{\ell,j}^2\le M\)，也只得到 \(\Gamma_j\lesssim N_jM/\nu\)。若用 Gronwall 贯穿所有窗口，还需要相应系数之和有限，而非仅逐窗有界。空间截止费用及换模、换窗的处理都未自动消失。

整个中心球无法用一个 CM.6 环带覆盖。继续分解趋近轴线的环带，会出现各自的 \(R^{-1}\) 费用，不能用本式直接完成 PF 的共同常数好尺度。以上是现有估计的具体缺口，不是无力演化不可能有更强控制的证明。

## 6. 来源、范围与下一项

推导使用经典角向有限维估计、Hilbert 范数链式不等式及二维插值。[Liu–Liu–Zhang 2406.05329v1 §3](https://arxiv.org/html/2406.05329v1) 已有柱坐标角变量分离与各向异性插值；主任务核读 Lemma3.1、Corollary3.1 及证明、Lemma3.2 陈述和定义域。这不是本文环带式的直接定理引用，也不主张一个新机制。已有被动剪切模相位及热流正规形检查不重复执行。

本阶段只接纳 CM.1–13 明示范围内的计算：没有终端临界界、统一低模控制、原解的 PF 好尺度或一般 B 结论。所有恒等式保留实际有符号项，局部插值不能代替这些项的终端动态估计。

按持续授权，保存与审查本阶段后继续一个不同输入来源的问题：将 SA.7 压力分为局部二次源与母球内调和部分，检验调和部分的高角模衰减能否在已有压力可积性下获得尺度一致的边界通量控制。它只可能处理压力的一部分，不能预记为完整闭合；不重开已停止的分量权重、剪切初始层或反向残差检验。
