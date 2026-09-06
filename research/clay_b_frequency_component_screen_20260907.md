# 稀疏频率权重的计数障碍与单分量接口核验

日期：2026-09-07（Asia/Shanghai）。基线：2971a8d943ccd6282b72aedc1cf74bcb397cfdb7。

这是一次限定两个来源的内部数学核验，不是科学发布冻结或投稿稿件。FS.1–FS.5 给出可独立检查的计数与函数估计反例；FS.6–FS.7 记录另一个接口的假设边界。独立复核状态见同目录 audit 文件。G、R216–R217 的真实 NS 输入及一般三维正则性仍为 OPEN / NOT CLAY。

## 1. 问题与来源

本轮选择 Ri 的 arXiv:2508.19590v1 与 Yu 的 arXiv:2606.08352v1；Kang–Nguyen 的 arXiv:2206.02490v1 是后者的必要依赖，不是第三个候选。

[Ri 原文](https://arxiv.org/html/2508.19590v1)声称用稀疏 Fourier 权重证明全局正则性。核验的对象是该版本实际写出的估计，不接受标题作为已证事实。以下沿用其 (1.4)、(2.2)–(2.3)、(3.1)、(3.8) 的定义。关键位置是 (3.12) 后、(3.13) 前的未编号求和链。原始 PDF 的印刷页 5、8、12、13 已与 HTML 对照；计数问题不是转换造成的。

全部 Fourier 定义在 \(\mathbb R^3\)。采用酉 Fourier 变换，令
\[
 \widehat{\Delta_j f}=\mathbf1_{\{2^{j-1}\le|\xi|<2^j\}}\widehat f,
 \qquad \widehat{f^s}=\mathbf1_{\{|\xi|\ge s\}}\widehat f,
 \qquad f_{n,n+1}=f^n-f^{n+1}.
\]
这里的整数阈值 \(n,k\) 不等于 dyadic 层号 \(j\)。

## 2. FS.1：正权重的平均与最大值等价

先取任意固定实数序列 \(a_j\ge1\)，\(j\ge1\)，并令 \(a_j=1\) 对 \(j\le0\)。定义
\[
 b(j)=2^{-j-1}\sum_{i=1}^{j}2^i a_i,\quad
 j_0(k)=\lceil\log_2 k\rceil+1,\quad
 A(n)=\sum_{k=1}^{n}b(j_0(2k)),\quad
 M=\sup_{j\ge1}a_j,\quad K=\sup_{n\ge1}\frac{A(n)}n.
\]
允许 \(M,K=+\infty\)。则
\[
 \frac14 M\le K\le M.
 \tag{FS.1}
\]

证明。对每个 \(j\ge3\)，令 \(n_j=2^{j-2}\)。恰有 \(2^{j-3}=n_j/2\) 个整数满足
\(2^{j-3}<k\le2^{j-2}\)。这些整数全部满足 \(j_0(2k)=j\)。正性与 \(b(j)\ge a_j/2\) 给出
\[
 \frac{A(n_j)}{n_j}\ge\frac12 b(j)\ge\frac14a_j.
\]
低层由 \(A(1)=b(2)=a_1/4+a_2/2\) 覆盖。因此 \(K\ge M/4\)。
若 \(M<\infty\)，则 \(b(j)\le M(1-2^{-j})\le M\)，故 \(A(n)\le Mn\)。
若 \(M=\infty\)，下界已经给出 \(K=\infty\)，上界按扩展实数理解。证毕。

特别地，存在固定 \(C<\infty\) 使所有 \(n\) 满足 \(A(n)\le Cn\)，当且仅当 \(a\) 有界。只要求对 \(n\ge n_0\) 成立也不改变结论：有限个小 \(n\) 的值有限。

## 3. FS.2：原文的稀疏集合不能消去重数

Ri 的权重在 \(j=i+2^{2^m}\)、\(-m\le i\le m\)、\(m\in\mathbb N\) 时为 \(\log_2j\)，其余为 1。取中心层
\(J_m=2^{2^m}\)，则 \(a_{J_m}=2^m\)。代入上一节得到
\[
 n_m=2^{J_m-2},\qquad
 \frac1{n_m}\sum_{k=1}^{n_m}b(j_0(2k))
 \ge 2^{m-2}\longrightarrow+\infty.
 \tag{FS.2}
\]

这否定了原文在 (3.12) 后使用的 \(A(n)\le3n\)，也否定把 3 改成任何固定常数的修补。每个固定 \(n_0\) 都会被上述序列越过。此处是对所有 \(m\) 的符号证明，没有构造巨大浮点数或用有限枚举替代极限。

原求和按满足条件的整数 \(k\) 计数。若 \(S\) 是层号集合，正确的重排是
\[
 \sum_{\substack{k\le n\\j_0(2k)\in S}}b(j_0(2k))
 =\sum_{\ell\in S}m_\ell(n)b(\ell),\qquad
 m_\ell(n)=\#\{k\le n:j_0(2k)=\ell\}.
\]
不能把右侧估成 \(|S|\max_\ell b(\ell)\)。在 \(n=n_j\) 时，单个层的重数已为 \(n/2\)。即使完全接受原文 Lemma 3.2 对层号集合大小的估计，FS.2 仍成立。

把整数 \(k\) 改成 dyadic 阈值会改变原文 (3.11)–(3.12) 的恒等式及最终 Sobolev 权重；把 \(S\) 改成整数原像集合则不再有原来的基数估计。二者都不是原证明的无代价修正。

## 4. FS.3：均匀正平均与缩放致小不能兼得

定义
\[
 D(f)^2=\sum_{j\in\mathbb Z}2^j\|\Delta_jf\|_2^2,\qquad
 \|f\|_{X_a}^2=\sum_{j\in\mathbb Z}2^ja_j^{-2}\|\Delta_jf\|_2^2.
\]
在这些环带上 \(|\xi|\le2^j\le2|\xi|\)（边界零测），所以
\(\|f\|_{\dot H^{1/2}}\le D(f)\le\sqrt2\|f\|_{\dot H^{1/2}}\)。
若 FS.1 的 \(K<\infty\)，则 \(M<\infty\)，对任意 \(\lambda>0\) 与 \(f_\lambda(x)=\lambda f(\lambda x)\) 有
\[
 \|f_\lambda\|_{X_a}
 \ge M^{-1}D(f_\lambda)
 \ge M^{-1}\|f_\lambda\|_{\dot H^{1/2}}
 =M^{-1}\|f\|_{\dot H^{1/2}}>0
 \quad(f\ne0).
 \tag{FS.3}
\]
最后一个等号可由 \(\widehat f_\lambda(\xi)=\lambda^{-2}\widehat f(\xi/\lambda)\) 直接换元得到。

因此，对这一个固定的正对角权重族，不能同时要求整数截断平均有统一常数，又要求每个非零临界场经 NS 缩放后任意小。这里没有排除其他非线性抵消、依赖解的权重或不同求和方法；那些方法的常数与新增项需另行证明。

原文 Lemma 2.1 在任意固定光滑时间段上选取依赖该段的缩放，并不因“依赖时间段”本身就循环。本轮拒绝的是 FS.2 已直接否定的平均估计，不把另一处未经否定的紧集缩放论证误列为错误。

## 5. FS.4：光滑无散场上的函数估计反例

对 Ri 的权重，记
\[
 \mathcal B_a(f)=\sum_{k=1}^{\infty}b(j_0(k))\|\nabla f^{k/2}\|_2^2.
\]
固定任意 \(n_0\in\mathbb N\) 和有限 \(c\ge0\)。原文 (3.13) 需要的普遍函数估计具有形式
\[
 \mathcal B_a(f)\le c\|\nabla f\|_2^2+
 6\sum_{r\ge n_0}r\|\nabla f_{r,r+1}\|_2^2.
\]
该估计对一般实值、无散、Schwartz 场不成立。

构造如下。选 \(n=n_m\ge n_0\)，在开环带 \(n<|\xi|<n+1\) 内选一对以 \(\xi_0,-\xi_0\) 为中心的小球。取非零、实值、偶对称的光滑紧支函数 \(\varphi\)，支撑在这对球内。选常向量 \(e\)，使
\[
 \widehat f(\xi)=\varphi(\xi)
 \left(I-\frac{\xi\otimes\xi}{|\xi|^2}\right)e
\]
不恒为零。它的逆变换实值、无散且为 Schwartz 场。令 \(\|\nabla f\|_2=1\) 仅是方便的归一化。

对所有 \(1\le r\le n\)，偶数项 \(k=2r\) 的尾部包含全部 \(f\)，故
\[
 \mathcal B_a(f)\ge A(n),\qquad
 \sum_{r\ge n_0}r\|\nabla f_{r,r+1}\|_2^2=n.
 \tag{FS.4}
\]
由 FS.2 选择 \(m\) 使 \(A(n)>c+6n\)，便得到严格反例。
更一般地，\(\mathcal B_a(f)/(\|\nabla f\|_2^2+\sum_{r\ge1}r\|\nabla f_{r,r+1}\|_2^2)\)
沿此族无界，因其至少为 \(n(1+n)^{-1}2^{m-2}\)。

没有利用任意强迫来实现这个场，也没有声称它产生奇点。

## 6. FS.5：反例在真实 NS 的短时间内持续

FS.4 不是必须避开的“非动力学数据”。对每个固定反例初值 \(f\) 和任意 \(\nu>0\)，存在真实的无强迫 \(\mathbb R^3\) NS 局部光滑解，且同一严格函数不等式在某个正时间段内仍失败。

先检查连续性。对 \(j\ge1\)，Ri 的 \(a_j\le C(1+j)\)，所以 \(b(j)\le C(1+j)\)。由 Tonelli，
\[
 \mathcal B_a(g)=\int |\xi|^2 W(|\xi|)|\widehat g(\xi)|^2\,d\xi,\qquad
 W(s)=\sum_{1\le k\le2s}b(j_0(k)).
\]
当 \(s\ge1/2\)，\(W(s)\le Cs(1+\log(e+s))\)；当 \(s<1/2\)，\(W(s)=0\)。因此
\[
 |\xi|^2W(|\xi|)\le C(1+|\xi|^4),\qquad
 |\xi|^2\lfloor|\xi|\rfloor\le C(1+|\xi|^4).
 \tag{FS.5}
\]
这些非负乘子定义的二次型在 \(H^2\) 上连续。具体地，乘子 \(m(\xi)\le C(1+|\xi|^2)^2\) 时，两值之差的绝对值不超过
\(C(\|g\|_{H^2}+\|h\|_{H^2})\|g-h\|_{H^2}\)。
固定 \(c,n_0\) 的右端也具有此连续性。

为明确这里只用局部存在性，可在 \(C([0,T];H^4)\) 中使用 mild 方程
\[
 u(t)=e^{\nu t\Delta}f-
 \int_0^t e^{\nu(t-s)\Delta}\mathbb P\nabla\cdot(u\otimes u)(s)\,ds.
\]
\(H^4(\mathbb R^3)\) 是乘法代数，热半群与 Leray 投影满足
\(\|e^{\nu t\Delta}\mathbb P\nabla\cdot F\|_{H^4}
\le C(\nu t)^{-1/2}\|F\|_{H^4}\)。
积分核的积分为 \(2\sqrt{T/\nu}\)；取 \(T\) 足够小，在半径 \(2\|f\|_{H^4}\) 的球上得到压缩映射。实值、无散性质保留，得到 \(u\in C_tH^4\subset C_tH^2\)；方程又给出 \(\partial_tu\in C_tH^2\)。Sobolev 嵌入保证这是局部经典解。这里重述标准局部构造，不主张该构造的新颖性。

FS.4 在 \(t=0\) 的严格差值与 \(H^2\) 连续性给出某个 \(\tau>0\)，使同一不等式对所有 \(0<t<\tau\) 失败。寿命可依赖整个高频初值并随 \(m\) 缩短；没有统一寿命或全局光滑结论。此处只否定 (3.13) 的解无关估计，不否定 NS 全局正则性，也没有给出周期域或固定单一初值的多尺度爆破解。

## 7. FS.6：单分量正则出口仍需支付两个输入

[Yu v1](https://arxiv.org/html/2606.08352v1) 的 Theorem 2.1 在 \(\Phi(1)=A+E+C+D\le M\) 和 \(C_3(1)\) 小时给出正则半径。其对数、幂次改进明确依赖 Assumptions 7.3、8.3、8.5；本轮不把这些条件当成已证稳定性。

局部 suitable 解、\(\nu=1\)，取后向柱体 \(Q_R(z_*)\)，令
\[
 C(R)=R^{-2}\int_{Q_R}|u|^3,\qquad
 D(R)=R^{-2}\int_{Q_R}|p-(p)_{B_R}(t)|^{3/2},\qquad
 C_e(R)=R^{-2}\int_{Q_R}|u\cdot e|^3.
\]
[Kang–Nguyen v1](https://arxiv.org/html/2206.02490v1) Theorem 1.3、Remark 1.1(5) 的局部 suitable 分支，取 \((p,q)=(3,3)\) 并固定 velocity-only 阈值 \(\varepsilon_W\)，已经给出
\[
 C(R)+D(R)\le M,\qquad
 C_e(R)\le\varepsilon_{KN}(M,\varepsilon_W)^3
 \quad\Longrightarrow\quad
 u\in L^\infty(Q_{\delta_{KN}(M,\varepsilon_W)R/2}).
 \tag{FS.6}
\]
证明这一代入：将压力减去 \((p)_{B_R}(t)\)，这是合法的纯时间规范；把固定常方向 \(e\) 旋转成第三轴，再平移和 NS 缩放到单位柱体。缩放后的分量 \(L^3\) 范数恰为 \(C_e(R)^{1/3}\)。定理先给出更小柱体的全速度临界小性，velocity-only epsilon regularity 再给上述内部半径。常数只涉及固定 \(M,\varepsilon_W\)；不把 local-energy 分支的远场数据依赖混入这个结论。

因此 Yu Theorem 2.1 的裸正则结论由已有定理在更弱的 \(C+D\le M\) 假设下直接覆盖；这不是说其所有结构结论都已有，也不是对该论文全部依赖的独立认证。

若能在一个指定候选奇点处找到 \(R_n\downarrow0\)、固定 \(M_0\) 和各尺度各自恒定的 \(e_n\in S^2\)，使 \(C(R_n)+D(R_n)\le M_0\) 且 \(\liminf C_{e_n}(R_n)=0\)，则某一尺度已足够直接排除该奇点。并不需要先证明 G。但本轮没有从一般能量产生这两个输入。

## 8. FS.7：方向平均与调和商都不是免费的临界小性

对任意 \(v\in\mathbb R^3\)，旋转不变性与球面面积公式给出
\(\fint_{S^2}|v\cdot e|^3\,de
=|v|^3\frac12\int_{-1}^{1}|s|^3\,ds=|v|^3/4\)。
Tonelli 于是给出
\[
 \fint_{S^2}C_e(R)\,de=\frac14 C(R),\qquad
 \int h\,u\cdot\nabla\chi=-\int\chi\,u\cdot\nabla h.
 \tag{FS.7}
\]
第一个恒等式只保证某方向的常数因子改善，不能单独推出趋零。第二个恒等式只用无散性及紧支测试函数；即使 \(h\) 空间调和，右端通常仍非零。故调和压力商不同于纯时间 pressure gauge，不能直接删除 G 的局部压力功。

Yu Theorem 5.1 的调和商紧性保留为来源工具。Lemma 8.2 在定制测试半范数的对偶中给出弱压力兼容性；水平无散测试场属于该半范数的核，需按商空间理解。它没有提供局部弱强稳定性。Assumption 8.5 所假设的 \(\|u-V\|_{L^3}\lesssim C_3^\gamma\) 仍需处理底部数据、cutoff、压力与比较流界；把它改名不能支付这些项。

## 9. 本轮结论与下一步

FS.1–FS.5 是限定正权重方法的明确障碍及真实 NS 短时函数估计反例。FS.6–FS.7 是已有定理的代入、初等恒等式和来源边界，不是新正则性定理。未核验这些局部观察是否已有人发表，也未做广泛新颖性检索。

本轮没有选定新的证明候选。两来源筛查到此结束，不继续为相同缺口反复增加版本。G 和 R216–R217 的关键输入未减少。

下一步只允许一个有退出条件的接口测试：检查 Yu Lemma 8.2 的测试空间能否与真实 NS 的局部能量差测试相容，并把所有时间导数、二阶空间导数、底部项及尺度常数显式写出。同时保留并估计该引理没有控制的 \(\nabla_h\langle P\rangle_\zeta\) 与 \(p^{\mathrm{rem}}\)，不能把商空间控制当成完整压力项已付。先与既有弱迹/对偶测试障碍去重。若只能对光滑固定测试成立，或仍须假设临界小量、比较流强界或 Assumption 8.5，则记为不能导入；不启动 shadowing 证明、仿真或新发布。只有得到减少已命名缺口的真实 NS 动态不等式，才升级为证明候选。

本记录不触发发布；最近的完整科学冻结及其一次交接不变。研究任务不读取发布状态、队列或 CI，不承担部署或验收。本轮无仿真、DGX、科学绘图或新读者 PDF。
