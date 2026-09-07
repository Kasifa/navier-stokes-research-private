# Laplacian 谱偏离：黏性不保证单调改善，临界费用不能只由动能统一支付

2026-09-07（Asia/Shanghai）。内部来源接口与解析检验 MSD，不是新科学发布冻结。

本节检查一个有明确原著依据的候选：利用应变接近 Laplacian 特征函数时的涡量伸长消去，获得任意大数据控制。所用零恒等式已经在本地 R0.70X 第4节证明过，不计为新发现。这里的新检查只针对“黏性自动改善谱偏离”和“基本动能统一支付这一临界费用”这两步。

结论是两步均不能直接成立。一个真实、全局光滑、无外力 NS 两频热剪切已足够：谱偏离先增后减；保持初始动能、黏性、观察时间和环面不变，临界费用仍能随频率趋于无穷。每条固定初值解的费用却始终有限。这不反驳文献的条件正则性判据，更不是奇点例子。

## 1. 来源与周期接口

本轮核读 [Miller, arXiv:2407.02691v2](https://arxiv.org/html/2407.02691v2) 的定义、第3节恒等式、第5节模型/原方程区别，以及第6节近特征函数判据及证明。官方版本页列 v2 为2026-04-13，journal reference 为 Pure Appl. Analysis 8 (2026), 247–270，DOI 10.2140/paa.2026.8.247；出版社页面本轮未取得，不声称另外核读了出版版。[版本记录](https://arxiv.org/abs/2407.02691)

原文空间是 \(\mathbb R^3\)，取 \(\nu=1\)。以下在固定未归一化环面 \(\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3\) 上直接证明所需接口，保留 \(\nu>0\) 和环面 Sobolev 常数，不移植全空间的数值阈值。体积记为 \(V=(2\pi)^3\)。

对实、光滑、无散 \(u\)，记 \(S=\operatorname{sym}\nabla u\)、\(\omega=\nabla\times u\)。已有的运动学恒等式为

\[
 \langle-\Delta S,\omega\otimes\omega\rangle
 =-\langle-\Delta u,(\omega\cdot\nabla)\omega\rangle=0.
 \tag{MSD.1}
\]

第一步对称化并在环面分部积分。再用
\((\omega\cdot\nabla)\omega=(\nabla\times\omega)\times\omega+
\nabla(|\omega|^2/2)\) 和 \(\nabla\times\omega=-\Delta u\)：叉积项逐点正交，梯度项与无散 \(-\Delta u\) 的全域配对为零。它只在完整全域配对下成立，不是被积函数逐点为零，也不能不计边界项地搬到移动球。

R0.70X 的 \(S(v)\) 指由涡量 \(v\) 通过 Biot–Savart 得到的应变；取 \(v=\omega\) 正好得到 MSD.1。旧记号不同不构成新恒等式。新核读的论文把该消去用于不同的模型与条件判据。

## 2. 谱偏离对应的费用是什么

对 \(S\ne0\)，定义三个谱矩及无量纲偏离：

\[
 P=\|S\|_2^2,\qquad M_1=\|\nabla S\|_2^2,\qquad
 M_2=\|-\Delta S\|_2^2,\qquad
 \delta=1-\frac{M_1^2}{PM_2},\qquad
 \inf_{\rho\in\mathbb R}\|-\rho\Delta S-S\|_2^2=\delta P.
 \tag{MSD.2}
\]

由 Cauchy–Schwarz，\(0\le\delta<1\)。零均值的非零应变有 \(M_1,M_2>0\)。极小式来自直接配方：
\(M_2\rho^2-2M_1\rho+P\)，极小点 \(\rho=M_1/M_2\)。
\(S=0\) 时将偏离与极小费用均定义为0。偏离为0意味着应变只占一个 Laplacian 特征值，但没有保证这种谱约束沿 NS 演化保持。

对完整无外力 NS，在其任意光滑区间，MSD.1 允许把伸长配对写为
\(\langle S+\rho\Delta S,\omega\otimes\omega\rangle\)。
Hölder 和零均值周期 GN 估计给出
\(\|\omega\|_4^2\le C\|\omega\|_2^{1/2}\|\nabla\omega\|_2^{3/2}\)。
取 MSD.2 的极小值，再用 Young 保留一半黏性项，得到

\[
 \frac12\frac d{dt}\|\omega\|_2^2
 +\frac{\nu}{2}\|\nabla\omega\|_2^2
 \le C\nu^{-3}\delta^2P^2\|\omega\|_2^2,
 \qquad
 \mathcal J(T):=\int_0^T\delta(t)^2P(t)^2\,dt.
 \tag{MSD.3}
\]

这重现文献 \(q=2,p=4\) 的机制，但用本地周期常数和任意 \(\nu\)。若候选有限首次奇点前 \(\mathcal J(T_*)<\infty\)，Gronwall 控制涡量 \(L^2\)，标准周期 \(H^1\) 延拓排除该首次奇点。这里的费用有限性是假设，不是已经由基本能量得出的结论。

基本能量实际给出
\(\int_0^T P(t)\,dt\le E_0/(2\nu)\)，其中
\(E_0=\|u(0)\|_2^2/2\)，因为 \(\|\nabla u\|_2^2=2P\)。
它本身不是 \(\mathcal J\) 的上界；下面用真实 NS 解检验能否有只依赖这些低阶固定数据的统一补充界。

## 3. 固定动能的精确原 NS 解

固定 \(E_0>0,\nu>0\)，取任意整数 \(N\ge1\)，令
\(a_0=4\sqrt{E_0/(5V)}\)。定义

\[
 u_N(t,x)=
 \left(
 a_0e^{-\nu N^2t}\cos(Nx_2)
 +\frac{a_0}{2}e^{-4\nu N^2t}\cos(2Nx_2),
 \ 0,\ 0
 \right),\qquad p_N=0.
 \tag{MSD.4}
\]

该场实、零均值、无散；由于仅第一分量非零且不依赖 \(x_1\)，
\((u_N\cdot\nabla)u_N=0\)。两模态分别满足热方程，因此 MSD.4 是完整无外力 NS 的全局光滑解，不是截断 ODE、被迫路径或数值近似。

两个余弦正交且平方积分为 \(V/2\)，故
\(\|u_N(0)\|_2^2/2=5Va_0^2/16=E_0\)，与 \(N\) 无关。
令 \(\tau=\nu N^2t\)、\(a=Va_0^2N^2/4=(4/5)E_0N^2\)。
只需 \(S_{12}=S_{21}=\partial_2u_{N,1}/2\)，便得到

\[
 \begin{aligned}
 P&=a(e^{-2\tau}+e^{-8\tau}),\\
 M_1&=aN^2(e^{-2\tau}+4e^{-8\tau}),\\
 M_2&=aN^4(e^{-2\tau}+16e^{-8\tau}).
 \end{aligned}
 \tag{MSD.5}
\]

这也给出精确的全时间基本预算
\(\int_0^\infty P(t)\,dt=E_0/(2\nu)\)：这里不是靠违反能量约束产生大临界费用。

## 4. 纯黏性演化也会暂时增大谱偏离

置 \(r=e^{-6\tau}\)，由三个谱矩直接消去公共因子：

\[
 \delta(\tau)=
 1-\frac{(1+4r)^2}{(1+r)(1+16r)}
 =\frac{9r}{(1+r)(1+16r)},\qquad
 \frac{d\delta}{dr}
 =\frac{9(1-16r^2)}{(1+17r+16r^2)^2}.
 \tag{MSD.6}
\]

由于 \(dr/d\tau=-6r<0\)，\(\delta\) 在
\(0\le\tau<(\log4)/6\) 严格上升，此后严格下降，并且

\[
 \delta(0)=\frac9{34},\qquad
 \max_{\tau\ge0}\delta(\tau)=\frac9{25},\qquad
 \tau_{\max}=\frac{\log4}{6},\qquad
 \lim_{\tau\to\infty}\delta(\tau)=0.
 \tag{MSD.7}
\]

因此“黏性必然让这一谱偏离单调减小”已被真实原 NS 解否定。最终趋于一个主导热模态，与中间时刻的单调性是不同命题。本节没有反驳更弱的平均改善、其它谱距离或包含流动额外信息的估计。

## 5. 临界费用的精确频率增长

把 MSD.5–6 代入 \(\mathcal J\)，并使用 \(dt=d\tau/(\nu N^2)\)：

\[
 \mathcal J_N(T)=
 \frac{1296}{25}\frac{E_0^2N^2}{\nu}
 \int_0^{\nu N^2T}
 \frac{e^{-16\tau}}{(1+16e^{-6\tau})^2}\,d\tau.
 \tag{MSD.8}
\]

此式包含了同一条实际解的全部时间；没有把不同解片段拼接。
被积函数严格正，可被 \(e^{-16\tau}\) 支配。令

\[
 I_\infty=\int_0^\infty
 \frac{e^{-16\tau}}{(1+16e^{-6\tau})^2}\,d\tau
 \in(0,1/16),\qquad
 \frac{\mathcal J_N(T)}{E_0^2N^2/\nu}
 \longrightarrow\frac{1296}{25}I_\infty>0
 \quad(N\to\infty).
 \tag{MSD.9}
\]

这里固定 \(T>0,E_0>0,\nu>0\) 及环面，故上限 \(\nu N^2T\to\infty\)。
于是不存在一个仅依赖这些固定参数、对所有光滑初值统一有效的有限
\(\mathcal J(T)\) 上界。初始高阶范数随 \(N\) 增长，没有保持它们固定。

对每个固定 \(N\)，MSD.8 的全时间费用却是有限的，且解始终光滑。因此这一例子完全符合 MSD.3 的条件延拓判据。它只拒绝“初始动能统一支付该临界费用”的尝试；不拒绝依赖完整光滑初值的先验界，不证明或暗示奇点，也不涉及 \(N\to\infty\) 给出同一初值爆破。

## 6. 本次检验留下什么

本轮核查了原著并找到旧公式的准确对应，随后把两项自动闭合设想落实为可直接判断的真解检验。没有发现任意大数据正则性所需的新动力学上界。

Miller 的另一个结果是删去特定项后模型方程的全局正则性；完整 NS 保留
\(P_{st}((u\cdot\nabla)S+S^2+\tfrac34\omega\otimes\omega)\)。
该余项在高一阶能量中的配对仍需控制，模型结论不能用于代替它。本文没有证明它的符号或累计费用，也不因上述热剪切是平面解就把整体研究目标缩小为平面流。

当前应停止这两个已失败的自动闭合，不重复做两频热例的调参、再绘同一曲线，或把已知条件判据换名。若再使用这个来源，必须先给出超出谱偏离单调性和动能支付的具体原 NS 输入，并完成局部去重；目前没有接受这样的候选。

G、R216–R217、一般终端缺口和一般三维正则性仍 OPEN / NOT CLAY。本记录不声称新颖性，不创建科学 release，不重发 FA；无仿真、DGX、科学附图或读者页面。审查与有限复算的实际范围见配套 audit/checks。
