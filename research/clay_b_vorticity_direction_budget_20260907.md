# 涡量方向预算：初始费用与零集项

2026-09-07（Asia/Shanghai）。基准：f5cf9196fbab0b5b6974a9c45b158f141012a8e9。
内部证明接口补全。CLASSICAL IDENTITY / EXACT NS CHECK / OPEN / NOT CLAY。

我保留任意光滑散度零周期初值、正黏性、无外力的完整目标。本轮不重做 R0.69Q 已完成的局部吸收反检，也不重开 Betchov 或方向相干判据。新增的是跨涡量零点的全局预算核验，以及两个真实光滑周期解的精确检查；不宣称这些经典工具具有新颖性。

## 1. 文献费用没有消失

[Beirão da Veiga–Berselli 2002，作者 PDF，第 350 页 §3](https://people.dm.unipi.it/beiraodaveiga/pdf/hbv-79.pdf) 的式 (3.2) 明确保留初始 \(\|\omega_0\|_1\)，并将方向积分限制在非零集。项目 r071h_literature_audit.md 的对应记录是正确的，不能把它当成“只花初始速度能量”的估计。

[BFG v4，PDF 第 4 页](https://arxiv.org/pdf/1704.05546v4) 的引言展示了一个未写初始涡量项的全空间上界。实际 PDF 和 HTML 均如此，不能只解释成 HTML 转换。下面的反检针对周期命题，不拿周期例直接推翻全空间陈述，也不据此否定 BFG 的主定理。Constantin 1990 原论文正文未取得，不能将问题归因于该原文。上轮 GS 的 curl 推导不使用这个引言上界，故不受影响。

## 2. 光滑周期解的正则化恒等式

令 \(\Omega=(\mathbb R/2\pi\mathbb Z)^3\)，\(u\) 是同一个无外力 NS 解，在闭区间 \([0,T]\) 光滑，\(\nu>0\)。
取欧氏模长、应变和能量
\[
 q=|\omega|,\quad \omega=\nabla\times u,\quad
 S=\tfrac12(\nabla u+\nabla u^\top),\quad
 E(t)=\tfrac12\|u(t)\|_2^2,\quad Q(t)=\|\omega(t)\|_1.
 \tag{VB.1}
\]
\(\xi=\omega/q\) 仅定义在 \(\{q>0\}\)。对 \(\varepsilon>0\) 设
\(r_\varepsilon=(q^2+\varepsilon^2)^{1/2}\)、
\(Q_\varepsilon(t)=\int_\Omega(r_\varepsilon-\varepsilon)\)。
对向量涡量方程用光滑凸函数链式法则，得到
\[
 (\partial_t+u\cdot\nabla-\nu\Delta)(r_\varepsilon-\varepsilon)
 =f_\varepsilon-\nu d_\varepsilon,\qquad
 Q_\varepsilon'(t)+\nu\int_\Omega d_\varepsilon
 =\int_\Omega f_\varepsilon,
 \tag{VB.2}
\]
其中
\[
 f_\varepsilon=\frac{\omega^\top S\omega}{r_\varepsilon},\qquad
 d_\varepsilon=\sum_j\left[
 \frac{|\partial_j\omega|^2}{r_\varepsilon}
 -\frac{(\omega\cdot\partial_j\omega)^2}{r_\varepsilon^3}\right]\ge0.
 \tag{VB.3}
\]
非负性来自 \(r_\varepsilon^2\ge q^2\) 与 Cauchy–Schwarz。
在非零集作正交极分解，逐点有
\[
 d_\varepsilon=
 \frac{q^2}{r_\varepsilon}|\nabla\xi|^2+
 \frac{\varepsilon^2}{r_\varepsilon^3}|\nabla q|^2
 \longrightarrow q|\nabla\xi|^2.
 \tag{VB.4}
\]
这只是非零集上的极限；后一项不能在全空间积分后直接置零。

## 3. 零集上的非负余项

在非零集令 \(f=q\,\xi^\top S\xi\)，在零集令 \(f=0\)。光滑性给
\(|f_\varepsilon|\le q|S|\)、\(f_\varepsilon\to f\)，且
\(Q_\varepsilon\to Q\) 一致。VB.2 提供非负测度
\(d_\varepsilon\,dx\,dt\) 的一致总量界。

更具体地，
\(|Q_\varepsilon'|\le\int_\Omega|\partial_t\omega|\)，故对固定光滑闭区间，
VB.2 给 \(\int_\Omega d_\varepsilon(t)\le C_T\)，独立于 \(\varepsilon\)。
所以弱极限不会在时间端点聚集。由局部链式恒等式的分布极限，该测度极限唯一：
\[
 \mu=\frac{f-(\partial_t+u\cdot\nabla-\nu\Delta)q}{\nu}
 =\mathbf1_{\{q>0\}}q|\nabla\xi|^2\,dx\,dt+\mathfrak z,\qquad
 \mathfrak z\ge0,\quad
 \operatorname{supp}\mathfrak z\subseteq\{q=0\}.
 \tag{VB.5}
\]
说明：在每个紧含于 \(\{q>0\}\) 的开集上，VB.4 的收敛光滑且一致；故 \(\mu\) 在那里正好等于给出的密度。其余限制测度非负并支撑在零集。这也证明方向密度可积。零集不是被删掉，而是由 \(\mathfrak z\) 记录。

记 \(\mathcal Q_T=\Omega\times(0,T)\)，积分恒等式为
\[
 Q(T)+\nu\int_0^T\!\!\int_{\{q>0\}}q|\nabla\xi|^2
       +\nu\mathfrak z(\mathcal Q_T)
 =Q(0)+\int_0^T\!\!\int_\Omega f .
 \tag{VB.6}
\]
端点一致收敛及前述时间边缘一致界使等号对每个光滑端点 \(T\) 成立，不需要假定涡量处处非零。略去非负 \(\mathfrak z\) 才得到通常的方向耗散不等式。

## 4. 实际可支付的上界

周期无散场满足
\(\|\omega\|_2^2=\|\nabla u\|_2^2\)、
\(\|S\|_2^2=\tfrac12\|\nabla u\|_2^2\)。
对于迹零对称矩阵，其最大绝对特征值至多 \(\sqrt{2/3}|S|\)：若该值为 \(m\)，另两特征值平方和至少为 \(m^2/2\)。因此
\[
 \left|\int_\Omega f\right|
 \le\sqrt{\frac23}\,\|q\|_2\|S\|_2
 =\frac1{\sqrt3}\|\nabla u\|_2^2.
 \tag{VB.7}
\]
从 VB.6 和精确能量等式得到
\[
 Q(T)+\nu\left[
 \int_0^T\!\!\int_{\{q>0\}}q|\nabla\xi|^2+\mathfrak z(\mathcal Q_T)\right]
 \le Q(0)+\frac{E(0)-E(T)}{\sqrt3\,\nu}
 \le Q(0)+\frac{E(0)}{\sqrt3\,\nu}.
 \tag{VB.8}
\]
常数没有最优性主张。固定光滑初值的 \(Q(0)\) 有限，因此这是真实 NS 轨道上的无条件预算；若 \(T_*\) 是有限候选终点，可令 \(T\uparrow T_*\) 控制非负累计量，而不假定终端涡量强迹或光滑延拓。

它不等于由 \(E(0)\) 单独支付的预算。两项虽然在全空间 NS 抛物缩放下都按 \(\lambda^{-1}\) 变化，同质性相同并不意味着初始范数相互控制。

## 5. 初始能量固定时，方向耗散仍可任意大

对任意 \(A>0\)、正整数 \(k\)，取
\[
 u(x,t)=Ae^{-\nu k^2t}(\cos kx_3,\sin kx_3,0),\qquad p=0.
 \tag{VB.9}
\]
它散度零，\(u\cdot\nabla u=0\)、\(\Delta u=-k^2u\)，因此是全时光滑的精确 NS 解。
其 \(\omega=-ku\)，涡伸长为零，\(q=Ak e^{-\nu k^2t}>0\)，
\(|\nabla\xi|^2=k^2\)。令 \(V=(2\pi)^3\)，则
\[
 \int_0^T\!\!\int_\Omega q|\nabla\xi|^2
 =\frac{VAk}{\nu}(1-e^{-\nu k^2T}),\qquad
 E(0)=\frac{VA^2}{2},\qquad \mathfrak z=0.
 \tag{VB.10}
\]
固定 \(A,\nu,T>0\)，令 \(k\to\infty\)：左边无界，而 \(E(0)\) 完全不变。所以不存在仅依赖 \(E(0),\nu,T,\Omega\) 的有限统一上界，覆盖全部这些光滑初值。固定 \(k\) 再令 \(A\downarrow0\)，也直接排除齐次的 \(C E(0)\) 上界。

这不排除依赖其他初始导数信息的估计；更不排除固定初值的正则性证明。这里没有任何爆破，不能将反检升级为一般正则性的反例。

## 6. 方向处处局部常值，也可能有模长耗散

再取精确剪切解
\[
 u(x,t)=Ae^{-\nu k^2t}(\sin kx_3,0,0),\qquad p=0,\qquad
 \omega=(0,Ak e^{-\nu k^2t}\cos kx_3,0).
 \tag{VB.11}
\]
在非零条带内 \(\xi\) 为常向量，故方向积分为零，伸长也为零。但是
\(Q(t)=16\pi^2Ak e^{-\nu k^2t}\) 严格下降。
若 \(z_j=(\pi/2+j\pi)/k\)、\(j=0,\ldots,2k-1\)，零集测度为
\[
 d\mathfrak z=
 2Ak^2e^{-\nu k^2t}
 \sum_{j=0}^{2k-1}dx_1\,dx_2\,\delta_{z_j}(dx_3)\,dt .
 \tag{VB.12}
\]
可直接验证：对一维光滑函数 \(g\) 的简单零点，
\(\varepsilon^2(g')^2/(g^2+\varepsilon^2)^{3/2}\) 的质量趋于
\(2|g'|\)，因为
\(\int_{\mathbb R}(1+s^2)^{-3/2}\,ds=2\)。
VB.11 的每个零点均为简单零点，代入即得 VB.12。其总质量为
\[
 \mathfrak z(\mathcal Q_T)
 =\frac{16\pi^2Ak}{\nu}(1-e^{-\nu k^2T})
 =\frac{Q(0)-Q(T)}{\nu}.
 \tag{VB.13}
\]
这给出 VB.6 的精确零集检查：模长衰减全部由零集项承担，不能把非零集模长方程不加修正地积分成全局等式。

## 7. 对完整目标的贡献与限制

本轮补全了已知方向预算在周期光滑解及零点上的合法用法，确认了不可省略的初始费用。它没有增加一项独立于原耗散机制的新能量，也没有改善缩放临界性。方向预算中的伸长配对是 \(q\,\xi^\top S\xi\)，普通涡量平方预算的生产项却是 \(q^2\xi^\top S\xi\)；这一额外幅度尚未受控。

G、R216–R217、一般首次奇点排除仍 OPEN。不得把 VB.8 的非负余项丢掉后反推控制普通伸长，也不得把 VB.10 的光滑反检称为 NS 奇点。旧局部吸收、方向核及两范数近远分裂分支仍按已完成记录去重。

这是内部证明接口补全，不是新颖性或投稿价值结论；没有新科学冻结、发布交付、仿真、DGX 或读者文件。下一步没有已经成立的新动态桥梁，不能仅凭“预算有限”重启同一方向耗散路线。
