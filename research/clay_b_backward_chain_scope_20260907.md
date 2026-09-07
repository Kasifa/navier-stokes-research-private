# 反向集中链：时间求和成立，但能量不能替代临界控制

2026-09-07。PRIVATE_CORE。基线为 PGR 科学提交 d58abdd9390ef8ced52f1807a956a663853f7680，治理 HEAD f06682e85c9dfbe74e2f4df2573f63f82e7b4549。

本次有界检验得到一个明确的否定结果：固定能量和黏性不能给所有光滑周期 NS 解一个统一的平方根时间总速度界。证明直接使用已有 FA 解族，不是新构造。另将集中链的时间求和写成一个假设完整的初等引理。两项结果都没有给单个固定初值的新正则性控制。

分类：PROVED COROLLARY / CONDITIONAL CHAIN LEMMA / SCALAR NON-NS EXAMPLE / NO-CANDIDATE FOR UNCONDITIONAL CLOSURE / OPEN / NOT CLAY。不声称新颖性、最优性、投稿价值或真人同行评审。

## 1. 本次只检验一个文献接口

[Tao, arXiv:1908.04958v2](https://arxiv.org/abs/1908.04958v2)，命题 3.1(ii)、(iv)–(v)，研究黏性一、全空间经典解，预设时间一致的空间 L3 上界。反向集中链及平方根时间总速度估计均带这个上界的常数。此次新增阅读为 (iv)–(v) 的证明段；不是将它们无证明移植到周期域，也不认证全文。原文阅读细节另见审查记录。

具体检验：能否保持时间链论证所需的统一常数，将总速度估计的临界范数依赖换成固定能量、固定黏性？下面在当前周期原方程中给出否定答案。其余周期移植问题不因这一答案而视作完成。

## 2. 不能仅依赖能量的平方根时间界

固定未归一化的 \(\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3\)、\(\nu>0\)、\(E_0>0\)。完整方程为
\[
 \partial_tu+\mathbb P\operatorname{div}(u\otimes u)=\nu\Delta u,
 \qquad \operatorname{div}u=0,
 \qquad \tfrac12\|u(0)\|_2^2=E_0 .
 \tag{BCS.1}
\]
初值实、光滑、零均值。不存在有限常数 \(B(E_0,\nu)\)，使所有这些解在其光滑寿命内的所有正时间区间 \(I\) 上满足
\[
 \int_I\|u(t)\|_\infty\,dt\le B(E_0,\nu)|I|^{1/2}.
 \tag{BCS.2}
\]

证明沿用 [FA.10–13、16–17](clay_b_frequency_activation_20260907.md) 的真实解，不把第一 Picard 项当作原解。该来源已给出非零实 Schwartz 无散种子 \(F\)，以及扩大环面 \(\mathbb T_N^3\) 上的解 \(U_N\)，其中
\[
 W_N=d_N\sum_{\ell\in\mathbb Z^3}F(\cdot+2\pi N\ell),
 \quad d_N\to d>0,
 \quad U_N(0)=W_N,
 \quad \varepsilon_N=\nu N^{-1/2},
 \quad \|U_N(\tau)-W_N\|_{H^3}\le C\tau
 \tag{BCS.3}
\]
对足够大 dyadic \(N\) 及 \(0\le\tau\le\tau_*\) 成立，\(C,\tau_*>0\) 与 \(N\) 无关；同窗 \(H^5\) 范数一致有界。扩大环面范数未作体积平均。FA.12、AJ.6–8 的格点和给 \(H^3\to L^\infty\) 的一致常数，不使用随边长退化的 Poincaré 常数。

选择固定 \(y_*\) 使 \(dF(y_*)\ne0\)，记 \(v_*=|dF(y_*)|>0\)。Schwartz 周期化在该点收敛，故增大 \(N_0\) 可使 \(|W_N(y_*)|\ge3v_*/4\)。由 BCS.3 和上述一致嵌入，固定一个 \(0<\tau_s\le\tau_*\)，使
\[
 |U_N(\tau,y_*)|\ge v_*/2=:c_*>0
 \quad(0\le\tau\le\tau_s,\ N\ge N_0).
 \tag{BCS.4}
\]
这里先固定种子、能量、黏性和 \(\tau_s\)，再令 \(N\) 增大，不能让该正常数随 \(N\) 消失。

FA 的精确变换为
\[
 u^{(N)}(t,x)=N^{3/2}U_N(N^{5/2}t,Nx),
 \quad p^{(N)}(t,x)=N^3P_N(N^{5/2}t,Nx),
 \quad I_N=[\tau_sN^{-5/2}/4,\tau_sN^{-5/2}/2].
 \tag{BCS.5}
\]
空间映射是从固定环面到扩大环面的双射，黏性回到固定 \(\nu\)，初始能量恰为 \(E_0\)。完整非线性、压力和所有 Fourier 相互作用均保留。该窗是严格正时间窗，但其起点趋零。取 \(x_N=y_*/N\)，由 BCS.4 得
\[
 \int_{I_N}\|u^{(N)}(t)\|_\infty\,dt
 \ge \frac{c_*\tau_s}{4}N^{-1},
 \qquad
 \frac{\int_{I_N}\|u^{(N)}(t)\|_\infty\,dt}{|I_N|^{1/2}}
 \ge \frac{c_*\sqrt{\tau_s}}2 N^{1/4}\longrightarrow\infty .
 \tag{BCS.6}
\]
这证明 BCS.2 不成立。与此同时，FA.17 给
\[
 \nu\int_0^{\tau_sN^{-5/2}}\|\nabla u^{(N)}(t)\|_2^2\,dt
 \le C\nu\tau_sN^{-1/2}\longrightarrow0 .
 \tag{BCS.7}
\]
所以仅增加“该短窗的总耗散很小”也不能恢复同一个统一界。

这不否定常数依赖完整初值、初始高阶范数或正的固定成熟时间的估计；也没有在一个固定解的终端附近构造这些窗口。量词是每个 \(N\) 有不同的光滑初值，不是一个初值包含所有尺度。这里没有证明 BCS.2 对任意一条固定解失效，更没有构造奇点。BCS.6 是 FA/AJ 工具的直接推论，不重复计为新的尺度机制。

## 3. 时间链中能够独立证明的部分

本节是纯解析引理，不假设或证明 NS 必产生这种链。令 \(L\ge1\) 为有限整数，\(t_0>\cdots>t_L\)，\(r_i>0\)（\(0\le i<L\)），\(a>0\)、\(0<\alpha\le\beta\)，\(0<\delta\le\alpha\)，且
\[
 \alpha r_i^2\le t_i-t_{i+1}\le\beta r_i^2,
 \qquad J_i=[t_i-\delta r_i^2,t_i],
 \qquad g(t)\ge a/r_i\quad\text{a.e. on }J_i .
 \tag{BCS.8}
\]
设 \(g\ge0\) 可测，\(S=\int_{t_L}^{t_0}g<\infty\)，\(D=t_0-t_L\)。由 \(\delta\le\alpha\)，每个 \(J_i\subset[t_{i+1},t_i]\)，它们内部不交。因此 \(S>0\)，并且
\[
 a\delta\sum_{i=0}^{L-1}r_i\le S,
 \qquad D\le\beta\sum_{i=0}^{L-1}r_i^2,
 \qquad \max_{i<L}r_i\ge\frac{a\delta D}{\beta S}.
 \tag{BCS.9}
\]
最后一式来自 \(\sum r_i^2\le(\max r_i)\sum r_i\)。这是至少一个大尺度，不是末端尺度或最小尺度的正下界。如果另有 \(S\le B\sqrt D\)，可得某个 \(r_i\ge a\delta\sqrt D/(\beta B)\)。如果还有度量空间中的点 \(x_i\) 满足 \(d(x_i,x_{i+1})\le Kr_i\)，三角不等式给
\[
 d(x_0,x_L)\le \frac{KS}{a\delta}.
 \tag{BCS.10}
\]
这些结论保留全部常数。点态阈值本身不保证 BCS.8 的持留区间；\(S<\infty\) 也不保证 \(S\le B\sqrt D\)。二者均须由原方程另外证明。若已有持留长度 \(\delta_0r_i^2\)，应取 \(\delta=\min(\delta_0,\alpha)\)，而不是未经检查宣布原来的较长区间不交。本节不声称恢复文献中每一个显式常数幂次。

## 4. 即使平方根时间模成立，计数本身也不是排奇点证明

给一个严格标量例子，明确不是 NS 解。取 \(r_i=2^{-i}\)、\(t_i=\sum_{j=i}^{\infty}r_j^2=\tfrac43r_i^2\)、\(\alpha=\beta=1\)、\(\delta=1/2\)，令 \(g=a/r_i\) 于 \(J_i\)，其余处为零。区间内部不交，且
\[
 \int_0^{t_n}g(t)\,dt=2a\delta r_n<\infty,
 \qquad g(t)\le \frac{2a}{\sqrt3}\,t^{-1/2}\quad(t>0).
 \tag{BCS.11}
\]
因此对任何时间区间 \(I\subset(0,t_0)\)，
\[
 \int_I g(t)\,dt\le \frac{4a}{\sqrt3}|I|^{1/2},
 \tag{BCS.12}
\]
但仍有无限多个尺度和集中事件。证明 BCS.12 只用 \(t^{-1/2}\) 单调及 \(\int_0^h t^{-1/2}dt=2\sqrt h\)。端点的定义不影响积分。\(g\) 在累积端无界，不满足“在含端点的闭区间上经典光滑”这种额外假设；本例不反驳在固定光滑紧时间段内链有限，也没有给速度场、压力或 NS 初值。它只说明时间求和不能替代完整 PDE 的空间传播与终端论证。

## 5. 本轮决定和下一项边界

本轮否定的是 BCS.2 这个精确的能量级替换，不是所有同轨道动态控制。FA 的初值族在越来越早的时间集中，这一点不能用“窗口正时间”掩盖。BCS.8–12 整理了链的计算条件，也没有减少任意固定初值的未知终端控制。此次文献接口筛选未产生新的无条件闭合候选。

下一次只允许一个明确的原方程检验：先从已登记的 bounded-total-speed 来源中核对一般能量解实际得到的时间模及初值/成熟历史依赖，判断在固定正龄区间是否还留有未核查的、可推导的新动态约束。先完成这项范围核对，不能自动换指数、换范数、重新做集中包或把标量链升级为 NS 定理；若仍需要未控临界量，记录 NO-CANDIDATE 并停止这一接口，不开展相邻变体。尚未认证该下一项来源有可用增益。

一般光滑初值三维周期正则性、G、R216–R217 和一般终端缺口均 OPEN / NOT CLAY。全文和证据只作私有研究材料；没有科学附图、仿真、DGX 作业、公开读者文件或累计 recap。
