# 拉伸—压力联合演化：有符号入口的限定检验

2026-09-22。PRIVATE_CORE / CLASSICAL IDENTITIES / NO NEW DYNAMIC BOUND / OPEN / NOT CLAY。内部选题记录，不是独立研究小节。

## 1. 要检验什么

上一完整合成没有取得原 PF 共同好尺度。本轮只检验一个不同的动力学入口：同一真实无外力周期解上，拉伸率与横向转动的联合演化，能否提供由原输入支付的一侧时间控制，而不是再加强谐和压力尾。最终仍要证明任意允许初值的正则性；若选择全局出口，至少必须从原解得到候选终点前统一的涡量 L2 界，不能把它或等价的净生产正部当假设。

固定正黏性 ν、固定周期域及同一初值，取任意固定正龄 a 和光滑前终端窗 [a,T]，T<T*。已知输入是原动能、累计速度梯度平方、既有 SE 的压力 Hessian 时空 L1 界，以及固定 a 的光滑数据。待支付的唯一新步骤是下列有符号压力与黏性余项的联合控制，常数不得含未知终端高阶范数。先测试固定系数组合是否具有代数消去；没有得到这种消去便不继续扫描等价权重。

## 2. 不除涡量的实际方程

记 G=∇u、S=sym G、Ω=skew G、H=∇²p、L=D_t−νΔ、b=Sω。由
\[
LG=-G^2-H,\quad LS=-S^2-\Omega^2-H,\quad L\omega=S\omega,
\quad \Omega\omega=0
\]
及 Laplacian 乘积法则，直接得到
\[
Lb=-H\omega-2\nu\sum_j(\partial_jS)(\partial_j\omega).
\tag{SH.1}
\]
S²ω 精确抵消，但完整黏性交叉项存在。此式处处合法，不要求 ω 远离零。

令 P(t)=∫ω·Sω，全域周期积分给
\[
P'=\int|S\omega|^2-\int\omega^\top H\omega
-4\nu\sum_j\int[(\partial_jS)\omega]\cdot\partial_j\omega
-2\nu\sum_j\int(\partial_j\omega)^\top S(\partial_j\omega).
\tag{SH.2}
\]
压力的两次分部积分只能给
\[
\int\omega^\top H\omega
=-\int\nabla p\cdot(\omega\cdot\nabla)\omega
=\int p\,\operatorname{tr}[(\nabla\omega)^2],
\tag{SH.3}
\]
不是 ∫p|∇ω|²。正项 ∫|Sω|² 在 SH.2 中重新出现，不能把 SH.1 的抵消当作其耗散。

周期椭圆估计和 Sobolev 插值给
\[
\left|\int\omega^\top H\omega\right|+\|S\omega\|_2^2
\le C\|\omega\|_4^4
\le C\|\omega\|_2\|\nabla\omega\|_2^3.
\tag{SH.4}
\]
这里 ω 的均值为零。原能量并没有控制最右侧时间积分。黏性混合项常规界也仍含 ∥ω∥∞、∥S∥∞ 和 ∥∇ω∥²₂；正龄紧窗上的有限性不等于趋近 T* 的一致界。

## 3. 方向变量的完整黏性费用

只在 ρ=|ω|>0 处，令 ξ=ω/ρ、α=ξᵀSξ、β=(I−ξξᵀ)Sξ、v=Sξ、y=|v|²。β 是应变诱导的方向变化部分，不是相对应变特征架的角速度。再记
\[
g=\nabla\log\rho,\quad k=|\nabla\xi|^2,\quad
T_j=\partial_jS,\quad\eta_j=\partial_j\xi,\quad
R=\sum_jT_j(\eta_j+g_j\xi),\quad
\mathscr L=L-2\nu g\cdot\nabla .
\]
用同一乘积法则，
\[
\mathscr L\xi=\beta+\nu k\xi,\qquad
\mathscr Lv=(-\alpha+\nu k)v-H\xi-2\nu R.
\tag{SH.5}
\]
设 h∥=ξᵀHξ、h⊥=(I−ξξᵀ)Hξ，则
\[
\begin{split}
\mathscr L\alpha&=|\beta|^2-\alpha^2-h_\parallel+V_\alpha,\\
V_\alpha&=2\nu k\alpha-4\nu\sum_j\eta_j\cdot T_j\xi
-2\nu\sum_j\eta_j\cdot S\eta_j
-2\nu\sum_jg_j\,\xi^\top T_j\xi,\\
\mathscr Ly&=-2\alpha y-2\alpha h_\parallel-2\beta\cdot h_\perp+V_y,\\
V_y&=2\nu ky-4\nu v\cdot R-2\nu\sum_j|T_j\xi+S\eta_j|^2 .
\end{split}
\tag{SH.6}
\]
固定 c 时，F_c=y+cα² 的精确式为
\[
\begin{split}
\mathscr LF_c={}&-2(1+c)\alpha^3+2(c-1)\alpha|\beta|^2\\
&-2[(1+c)\alpha h_\parallel+\beta\cdot h_\perp]\\
&+V_y+2c\alpha V_\alpha-2c\nu|\nabla\alpha|^2 .
\end{split}
\tag{SH.7}
\]
在 α>0 区域，−1≤c≤1 给有利的无黏三次符号；c>−1 才保留 α² 控制。但横向压力系数永远是−2，c=−1 仅去掉纵向项并丢失拉伸平方控制。这里排除的是这个固定系数的直接代数消去，不是证明原 NS 动力学不能产生其它相关性。

虽然 0≤F_c≤C_c|S|²（c>−1）给已知时空积分，它不支付 |S||H|、k|S|² 或含 ∇S、∇ξ、g 的混合项。SE 的 ∫|H| 界缺少此处的应变权重。限定到 α>0 还需处理截断；固定正龄不排除 ρ=0。不得将 SH.5–7 任意延拓穿过零集，或直接积分漂移后丢掉其散度。SH.1–3 的无分母式保留为全域合法接口。

## 4. 查重后的决定

[Galanti–Gibbon–Heritage 1997，§3(34)–(52)](https://arxiv.org/html/chao-dyn/9709003v1) 已有完整黏性方向与拉伸方程，不仅是 Euler 公式。其 β 记号与本文不同。主任务实际阅读该完整章节、§2相关式(24)–(33)及§5开头的额外近似声明；不把后文固定参数近似用于原 NS 证明。

[Gibbon–Holm–Kerr–Roulstone，§2 Theorem 1](https://arxiv.org/html/nlin/0512034v4) 给 Euler 四元数 Riccati 及其直接证明。主任务已读该段，不将它直接移作正黏性正则性结论。没有全面复审两篇论文，也不宣称本稿恒等式新颖。

本地 TP.14 的完整三因子演化已有滤波版本；把算子形式上换成恒等算子可直接得到 SH.2 的结构。这不是令其零质量滤波半径趋零，因为那个极限不是恒等算子。PGR.5–9 已说明一项真有符号压力四次关系代回原方程后零和；GP.4 已说明净伸长预算的有限性与同轨道统一 H1 控制等价。这些都没有被本轮支付，不能再次当作未知新入口。

本轮结果是停止两个具体延长方式：不将 b 或 P 的旧演化重写作为新时间估计，不继续扫描 F_c 的固定权重。更广的压力—拉伸联合动力学仍开放；没有一般不可能性证明。下一题须另有实际时空结构输入，不能仅给剩余配对新名称。

复核范围另记：主任务直接核全部公式；参与式 AI 分别重推 SH.1–4 和 SH.5–7。没有科学数值、反例构造、DGX、论文、网页或发布冻结。本记录不计作一般 B 已闭合一步。
