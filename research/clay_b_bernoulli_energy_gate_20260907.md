# 伯努利加权能量：瞬时符号不等于状态耗散

2026-09-07。PRIVATE_CORE。内部候选资格检查，不是新研究发布。分类：LITERATURE / PROVED LOCAL CHECK / NO NEW UNCONDITIONAL ESTIMATE / OPEN / NOT CLAY。

本轮只检查一个具体步骤：伯努利总压产生的带符号瞬时等式，能否直接积分成某个状态能量的单调律？答案分开说：瞬时等式成立；下面一种自然权重对应的微分形式不恰当，因而这种直接积分不成立。这不排除其他状态泛函、补偿项或只沿原NS演化成立的估计。

## BE.1 固定方程、压力规范与已有来源

在 \(\Omega=(\mathbb R/2\pi\mathbb Z)^3\) 上取无外力光滑解
\[
u_t+(u\cdot\nabla)u+\nabla p=\nu\Delta u,\quad \nabla\cdot u=0,\quad \nu>0,\qquad \int_\Omega p=0.
\]
设 \(e=|u|^2/2\)、\(Q=e+p\)、\(\omega=\nabla\times u\)。压力是当前速度的确定二次函数：\(p[u]=R_iR_j(u_i u_j)\)，零频率取零，重复指标求和。

Chae 的 [Localized energy equalities for the Navier–Stokes and the Euler equations，arXiv v5](https://arxiv.org/html/1209.4432v5) Lemma 2.1 已给出下面的标量等式，Theorem 1.1 和周期 Corollary 1.2 讨论总压等值面分区。本文不把这项结构称为新发现。[2023年原刊摘要](https://link.springer.com/article/10.1007/s00033-023-01984-0)还说明：经时间压力规范调整的总压有最大值原理，并产生压力时间导数条件下的正则性判据。该2023来源本轮只读摘要，未审读付费全文。

当前v5 HTML的周期推论所显示的边界符号，与同页Lemma 2.1及Theorem 1.1证明的外法向计算不一致。下面直接从方程重推周期关系；不据HTML断言期刊印刷版有误，也不开展勘误项目。

由点乘速度及压力Poisson方程，
\[
e_t+u\cdot\nabla Q=\nu\Delta e-\nu|\nabla u|^2,
\quad \Delta p=-\partial_i u_j\partial_j u_i,
\quad |\omega|^2=|\nabla u|^2-\partial_i u_j\partial_j u_i.
\]
因此
\[
e_t+\nu|\omega|^2=\nu\Delta Q-u\cdot\nabla Q,
\qquad (\partial_t+u\cdot\nabla-\nu\Delta)Q=p_t-\nu|\omega|^2. \tag{BE.1}
\]
第二式没有消去无符号的 \(p_t\)。积分全域只恢复既有能量等式。

## BE.2 精确的带符号关系及时间余项

取 \(\phi\in C^1(\mathbb R)\)，令 \(\Phi'=\phi\)。周期积分分部及 \(\nabla\cdot u=0\) 给出
\[
\int_\Omega\phi(Q)e_t
=-\nu\int_\Omega\phi(Q)|\omega|^2
-\nu\int_\Omega\phi'(Q)|\nabla Q|^2. \tag{BE.2}
\]
输运项为 \(-\int u\cdot\nabla\Phi(Q)=0\)。若权重在实际总压值域内非负且递增，右端非正；但左端不是自动的状态能量导数。实际有
\[
\frac d{dt}\int_\Omega\Phi(Q)
=-\nu\int_\Omega\bigl[\phi(Q)|\omega|^2+\phi'(Q)|\nabla Q|^2\bigr]
+\int_\Omega\phi(Q)p_t. \tag{BE.3}
\]
最后一项没有由本轮证明得到符号或可用的累计上界。

等值面版本揭示同一个时间问题。设 \(a(t)\) 为 \(C^1\) 函数，在所考察时间邻域内 \(Q(t,x)=a(t)\) 上处处 \(\nabla Q\ne0\)。令 \(D_a(t)=\{Q>a(t)\}\)。其外法向为 \(-\nabla Q/|\nabla Q|\)，故
\[
\int_{D_a(t)}(e_t+\nu|\omega|^2)=-\nu\int_{Q=a(t)}|\nabla Q|,
\]
而Reynolds公式给出的真正移动区域能量导数是
\[
\frac d{dt}\int_{D_a(t)}e
=-\nu\int_{D_a(t)}|\omega|^2-\nu\int_{Q=a(t)}|\nabla Q|
+\int_{Q=a(t)}e\frac{Q_t-a'(t)}{|\nabla Q|}. \tag{BE.4}
\]
不能遗漏最后的边界运动项。在紧环面及上述光滑性下，单时刻的正则性由紧性和连续性延续到充分小时间邻域；这不保证覆盖任意预先指定区间或延续至候选终点。BE.2无需选取正则等值面。

## BE.3 两参数非恰当性检验

考虑光滑、平均零、无散速度空间中的一形式
\[
\alpha_u(v)=\int_\Omega(Q[u]+3)\,u\cdot v.
\]
问题的量词是：是否存在当前速度的 \(C^2\) 泛函 \(F\)，在下述状态 \(u_{1,1}=a+b\) 的某个开邻域满足 \(DF[u](v)=\alpha_u(v)\)，对每个允许的无散、平均零变化 \(v\) 都成立？例如可在平均零无散的 \(H^m\) 空间上表述，整数 \(m\ge3\) 足以使这里的乘积和压力二次映射光滑。若存在，拉回任何光滑二维参数面后的混合偏导必须相等。

取两个实周期无散、平均零场
\[
a=(\sin x\cos y,-\cos x\sin y,0),\qquad b=(0,0,\cos x),
\quad u_{s,r}=sa+rb.
\]
\(s,r\) 是速度参数，不是物理时间。各场均与 \(z\) 无关，\(a\cdot b=0\)，并且
\[
(a\cdot\nabla)a=(\sin x\cos x,\sin y\cos y,0)=-\nabla p_a,
\quad p_a=\tfrac14(\cos2x+\cos2y).
\]
含 \(b\) 的对流交叉项只有第三分量且与 \(z\) 无关，其散度为零。因此压力规范唯一确定
\[
p[u_{s,r}]=s^2p_a,\qquad e[u_{s,r}]=\tfrac12(s^2|a|^2+r^2|b|^2). \tag{BE.5}
\]
令 \(V=|\Omega|\)、\(X=\cos2x\)、\(Y=\cos2y\)。由
\(|a|^2=(1-XY)/2\)、\(|b|^2=(1+X)/2\)，逐变量取平均得
\[
\int_\Omega p_a|a|^2=0,\qquad
K:=\int_\Omega p_a|b|^2=V/16. \tag{BE.6}
\]
这里用到 \(\langle X\rangle=\langle Y\rangle=0\)、\(\langle X^2\rangle=\langle Y^2\rangle=1/2\) 及变量分离，并非有限网格拟合。

在此参数面上，用 \(d\) 表示参数微分，
\[
\alpha=d\!\left(\tfrac12\int_\Omega e^2+3\int_\Omega e\right)
+\int_\Omega p\,de
=d\!\left(\tfrac12\int_\Omega e^2+3\int_\Omega e\right)+Ks^2r\,dr.
\]
所以
\[
d\alpha=2Ksr\,ds\wedge dr=\frac V8sr\,ds\wedge dr\ne0\quad\text{在 }(s,r)=(1,1). \tag{BE.7}
\]
这与 \(d(DF)=0\) 矛盾，排除了任何包含 \(u_{1,1}=a+b\) 的开邻域内、对所有允许变化成立的状态原函数。该计算不依赖权重取负：在 \(s,r\in[1,2]\) 上，\(p\ge-s^2/2\ge-2\)、\(e\ge0\)，故 \(Q+3\ge1\)，且权重导数为1。常数3只用于这个有界局部检验，不声称它对任意大初值或整条NS轨道都使权重非负。

## BE.4 准确的排除范围与决策

BE.7排除的是固定零均值压力规范下 \(DF=\int(Q+3)\,de\) 的普遍微分身份，不是“任何能量泛函都不存在”。只要求 \(DF[u](\mathcal N_\nu[u])=\alpha_u(\mathcal N_\nu[u])\)，其中 \(\mathcal N_\nu\) 是原NS向量场，是更弱且不同的问题；BE.7不否定它。改变为速度依赖的压力规范、增加补偿项、使用其他权重或历史依赖泛函，也都不在本排除结论内。沿单条轨道累计BE.2左端当然可以定义路径积分，但这里没有它的状态表达、统一下界或临界控制。

参数面不是原NS轨道，不是假定闭合的有限模态模型，也不是奇点构造。其作用是对一个普遍状态微分身份提供反证。它不提供固定正年龄的终端反例，不证明所有伯努利方法失败，亦不提供任意候选奇点的覆盖。

本地AG已有的伯努利外壳重写保留压力成本；近期压力文献记录也未供应一般压力时间控制。水平场 \(a\) 及其压力已出现于 `clay_b_pressure_geometry_20260906.md` 的AC.13，不是本轮的新种子。本文的有限增量是明确区分瞬时等值面能量、移动区域能量以及状态一形式，并给出BE.7这一可直接验算的反例。它不是新的正则性判据、新颖性证明或可投稿价值判断。

决策：这个直接累计候选不入列；不再把最大值规范、移动阈值、压力换名或已否定的一形式直接积分当成新推进。一般初值3D无外力周期NS正则性和指定中心好尺度桥仍OPEN / NOT CLAY。下一项技术研究必须说明新增的原NS关系、可独立支付的量及其覆盖范围；当前未选定这样的新候选。仅保存内部证明与审查，不创建release，不发送发布任务，不仿真、不调用DGX、不制作科学图或recap。
