# 终端 Fourier 通量：能量缺口与弱时间入口

2026-09-07（Asia/Shanghai）。基准：7b2bf2152d8de82bba2048bbdce2ca2373f37c20。
内部证明接口筛选。CLASSICAL TOOLS / ACTUAL NS IDENTITY / CONDITIONAL / OPEN / NOT CLAY。

完整目标仍是任意光滑散度零周期初值的无外力三维 NS 全局光滑性。本轮检查的候选是：弱时间通量估计能否由已付能量生成，进而消去首次候选终点的能量缺口。先写清原始同一 NS 解的终端 Fourier 账本，再核单个文献入口。不把“能量没有损失”改名为“没有奇点”。

## 1. 原始解的端点缺口

固定 \(\nu>0\)、\(\Omega=(\mathbb R/2\pi\mathbb Z)^3\) 和 \(T<\infty\)。同一无外力解 \(u\) 在 \([0,T)\) 光滑，属于 \(L^\infty_tL^2_x\cap L^2_tH^1_x\)，并取标准弱连续 \(L^2\) 延拓的端点 \(u(T)\)。这里不假设强左迹。令
\[
 E(t)=\tfrac12\|u(t)\|_2^2\ (t<T),\quad
 g(t)=\|\nabla u(t)\|_2^2,\quad
 E_-:=E(0)-\nu\int_0^Tg(t)\,dt,\quad
 \delta:=E_--\tfrac12\|u(T)\|_2^2\ge0 .
 \tag{TF.1}
\]
光滑区间的能量等式给 \(E(t)\to E_-\)。非负性来自弱下半连续性，而非假定终端能量等式。

取实偶光滑低通 \(S_Q\)，Fourier 符号为 \(\chi(2^{-Q}k)\)，其中 \(0\le\chi\le1\)，近原点等于 1、紧支撑。记
\[
 e_Q=\tfrac12\|S_Qu\|_2^2,\quad
 d_Q=\|\nabla S_Qu\|_2^2,\quad
 \Pi_Q=\int_\Omega S_Q(u\otimes u):\nabla S_Qu\,dx,\qquad
 e_Q'=-\nu d_Q+\Pi_Q .
 \tag{TF.2}
\]
这是流入低频部分的符号约定。\(S_Q\) 与微分交换且自伴；压力与无散测试的配对为零。固定 \(Q\) 只有有限个 Fourier 模态，非线性由 \(L^\infty_tL^2_x\) 保证时间可积，弱连续端点使 TF.2 的积分式一直成立到 \(T\)。

## 2. 只能先断言 \(C^1\) 时间测试极限

对每个 \(\phi\in C^1([0,T])\)，TF.2 给
\[
 \int_0^T\Pi_Q\phi
 =e_Q(T)\phi(T)-e_Q(0)\phi(0)-\int_0^Te_Q\phi'
   +\nu\int_0^Td_Q\phi
 \longrightarrow-\delta\,\phi(T).
 \tag{TF.3}
\]
证明：两端有限能量场的 Fourier 截断在 \(L^2\) 收敛；内部 \(e_Q\to E\) 由 \(e_Q\le E\) 支配；\(\nabla S_Qu\to\nabla u\) 在 \(L^2_{t,x}\)，故 \(d_Q\to g\) 在 \(L^1_t\)。最后使用绝对连续延拓 \(E(t)=E(0)-\nu\int_0^t g\)，其在 \(T\) 的左极限为 \(E_-\)，而 TF.3 的实际端点是 \(\|u(T)\|_2^2/2\)。两者之差恰为 \(-\delta\)。

这不是声称 \(\Pi_Qdt\) 有一致总变差或在有限测度空间弱星收敛；此处的收敛只对上述 \(C^1\) 测试成立。紧含于 \((0,T)\) 的分布测试看不到这个端点项。每个严格早于 \(T\) 的光滑时刻，\(\Pi_Q(t)\to0\)，也不允许交换时间积分与 \(Q\to\infty\)。

Hilbert 空间的弱收敛加范数收敛、以及 TF.3 取 \(\phi=1\)，给出
\[
 \delta=0
 \ \Longleftrightarrow\
 u(t)\to u(T)\ \text{强 }L^2\ (t\uparrow T)
 \ \Longleftrightarrow\
 \lim_{Q\to\infty}\int_0^T\Pi_Q\,dt=0,
 \qquad
 \liminf_{Q\to\infty}\int_0^T|\Pi_Q|\,dt\ge\delta .
 \tag{TF.4}
\]
绝对通量趋零是充分条件；没有证明它是强左迹的必要条件。TF.4 没有把强 \(L^2\) 左迹升级成光滑延拓，也没有将全局端点量 \(\delta\) 自动识别为 suitable 局部能量缺陷测度。

## 3. 一个真实但有条件的弱时间入口

[Cheskidov–Luo，arXiv:1802.05785v2，Theorem 1.1、Proposition 4.1](https://arxiv.org/html/1802.05785v2#S4) 包含 \(p=\infty,\beta=2\) 的入口：额外 \(u\in L^{2,\infty}_tB^0_{\infty,\infty}\) 足以消除绝对积分通量。这里 \(L^{2,\infty}\) 是弱 \(L^2\)，不是时间 \(L^\infty\)。原文同时允许 \(\mathbb R^3\) 与 \(\mathbb T^3\)。

以下只独立重算这个入口，不声称复证整个参数区域。使用固定非齐次 dyadic 分解 \(u_r\)、\(\lambda_r=2^r\)、\(r\ge-1\)，与低通采用相容的光滑滤波。定义
\[
 f(t)=\sup_{r\ge-1}\|u_r(t)\|_\infty,\quad
 K=\sup_{a>0}a\,|\{t:f(t)>a\}|^{1/2}<\infty,\quad
 M=\sup_r\operatorname*{ess\,sup}_{t}\|u_r(t)\|_2<\infty,\quad
 h_r(t)=\lambda_r^2\|u_r(t)\|_2^2,\quad
 b_r=\int_0^Th_r .
 \tag{TF.5}
\]
\(K<\infty\) 是新增假设；\(M<\infty\)、\(\sum_rb_r<\infty\) 才是能量类已经给出的量。非齐次最低频费用由 \(T\|u\|_{L^\infty_tL^2_x}^2\) 控制。

沿用标准 CCFS 通量估计（当前原文 Proposition 3.2）。对其卷积用加权 Hölder，再用 \(\|u_r\|_3^3\le\|u_r\|_2^2\|u_r\|_\infty\)，得到
\[
 |\Pi_Q(t)|
 \le C\sum_{r\ge-1}2^{-2|r-Q|/3}\lambda_r\|u_r(t)\|_2^2f(t).
 \tag{TF.6}
\]
这是被明确继承的调和分析输入，不把本节当作 CCFS 全部通量证明的新认证。

令 \(L=\lambda_Q\)、\(A_Q=\{f>L\}\)。分布函数界 \(|\{f>a\}|\le K^2a^{-2}\) 给
\[
 \int_{A_Q}f^{8/5}\le C K^2L^{-2/5},\qquad
 \int_{A_Q^c}f^{8/3}\le C K^2L^{2/3}.
 \tag{TF.7}
\]
第一式的层蛋糕公式包含 \(L^{8/5}|\{f>L\}|\) 的边界项；第二式可用 \(f\mathbf1_{f\le L}\) 的分布上界。两式都是不等式，不把截断分布函数积分误写成缺少边界项的等式。

对 TF.6 每个 \(r\) 的时间积分，分别按 \(h_r^{3/8}\) 和 \(h_r^{5/8}\) 分解后使用 Hölder：
\[
 \begin{aligned}
 \int_{A_Q}\lambda_r\|u_r\|_2^2f
 &\le C M^{5/4}K^{5/4}
       (\lambda_r/\lambda_Q)^{1/4}
       \left(\int_{A_Q}h_r\right)^{3/8},\\
 \int_{A_Q^c}\lambda_r\|u_r\|_2^2f
 &\le C M^{3/4}K^{3/4}
       (\lambda_Q/\lambda_r)^{1/4}
       \left(\int_{A_Q^c}h_r\right)^{5/8}.
 \end{aligned}
 \tag{TF.8}
\]
例如第一式使用精确乘积
\(\lambda_r\|u_r\|_2^2=h_r^{3/8}\|u_r\|_2^{5/4}\lambda_r^{1/4}\)，时间共轭指数为 \(8/3,8/5\)。第二式共轭指数为 \(8/5,8/3\)。

两个频率比值都不能统一写成不超过 1；它们分别在一个方向增长，但可吸收到原有距离核。因此
\[
 \int_0^T|\Pi_Q|\,dt
 \le C M^{5/4}K^{5/4}
       \sum_r2^{-5|r-Q|/12}b_r^{3/8}
   +C M^{3/4}K^{3/4}
       \sum_r2^{-5|r-Q|/12}b_r^{5/8}
 \longrightarrow0 .
 \tag{TF.9}
\]
因为 \(b\in\ell^1\)，两种幂序列都有界并趋零；与固定 \(\ell^1\) 核卷积后仍趋零。可先分割有限个低层与其余尾部证明，不需要未经控制地交换两重极限。\(K=0\) 或 \(M=0\) 时 \(u=0\) 几乎处处，结论直接成立。

由 TF.4，这个额外弱时间假设确实使 \(\delta=0\)。本重算保留了层蛋糕边界项和剩余频率因子；不依据 HTML 中的简写或符号问题宣布文献定理无效。

## 4. 基本能量尚未支付这个入口

周期 Bernstein 直接给
\[
 \sup_r\lambda_r^{-1/2}\|u_r(t)\|_\infty
 \le C\left(\sum_r\lambda_r^2\|u_r(t)\|_2^2\right)^{1/2},
 \qquad
 u\in L^2_tB^{-1/2}_{\infty,\infty}.
 \tag{TF.10}
\]
最低频如上保留。TF.5 所需却是零阶 Besov 的弱 \(L^2_t\) 控制。弱化时间范数并不由 TF.10 自动补齐这半阶空间差距；这里仅指出该已知能量—Bernstein 推导没有给出 \(K<\infty\)，不声称构造了真实 NS 反例或证明所有动态方法均不可能。

这一差距与项目已有 R071M 的能量/Onsager 分辨一致，不计作本轮新发现。一般能量没有因此消去 \(\delta\)，更没有得到指定中心的好尺度。已知的 \(L^1_tL^\infty_x\) 也不能直接当成这个弱 \(L^2_t\) 假设。

## 5. 本轮决定

本轮新增的本地接口是原始同一 NS 解的 TF.3–4，而非此前正原子条件下的共同伴随通量；随后核明一个未在本地实读过的弱时间来源。结果明确了绝对积分通量、终端能量缺口和强左迹之间的方向，未证明其中的缺口为零。

候选没有得到从已付预算到 \(K<\infty\) 的新动态推导，因此停止以此作为无条件闭合路线。保留一般光滑初值的完整目标；G、R216–R217、终端缺口的一般消失及一般正则性仍 OPEN。不得再把普通尺度望远镜、相同 Besov 条件、强迹等价改写或本轮复核当成新进展。

这不是新颖性、投稿价值或 Clay 结论，不是新的科学发布冻结。没有仿真、DGX、科学附图或读者文件；不产生发布交付。
