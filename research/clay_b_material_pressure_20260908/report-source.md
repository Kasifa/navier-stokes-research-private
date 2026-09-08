# 压力的物质导数：恒等式成立，新的临界控制尚未得到

2026-09-08。面向本研究的内部方法选择。PRIVATE_CORE；LITERATURE / LOCAL IDENTITY CHECK / NO NEW CRITICAL INPUT / OPEN / NOT CLAY。

本轮检查压力随流动的变化能否补上当前正则性论证的缺口。结论是：原 NS 的精确重写成立，但直接估计没有给出所需的时间可积性；已有的沿流压力增益也有额外输入，不能当成能量类的自动结论。这是一次内部资格检查，不是新研究小节、正则性判据或文献穷尽性结论。

范围限固定正黏性、三维周期无力 NS。主稿保留两端切片、压力规范和局部测试项；不将 Euler、弱耗散模型、静态速度族或随机表示替换为原问题。沿用当前研究问题：是否能在同一候选终端生成足以应用已有条件准则的尺度，或证明真正的尺度增益、独立不可求和成本。本轮没有取得这些结果。

## 1. 同一光滑解上的压力演化

在 \(\Omega=(\mathbb R/2\pi\mathbb Z)^3\) 和闭光滑时间段 \([a,b]\) 上，
\[
u_t+u\cdot\nabla u+\nabla p=\nu\Delta u,\qquad
\nabla\cdot u=0,\qquad \nu>0,\qquad \int_\Omega p(t)=0.
\]
设 \(D_t=\partial_t+u\cdot\nabla\)、\(\mathcal R_{ij}=R_iR_j\)。非零 Fourier 模态上 \(R_i\) 的乘子取 \(-\mathrm i k_i/|k|\)，零模取零。因此
\[
p=\mathcal R_{ij}(u_i u_j),\qquad
\mathbb P=I+(\mathcal R_{ij})_{ij},\qquad
a=\mathbb P(u\cdot\nabla u)=u\cdot\nabla u+\nabla p.
\tag{MPS.1}
\]
重复指标求和。此处 \(a\) 是非线性投影项，**不是**完整物质加速度 \(D_tu=\nu\Delta u-\nabla p\)。

由 \(u_t-\nu\Delta u=-a\) 和乘积法则，
\[
(\partial_t-\nu\Delta)(u_i u_j)
=-u_i a_j-u_j a_i-2\nu\,\partial_k u_i\partial_k u_j.
\]
\(\mathcal R_{ij}=\mathcal R_{ji}\)，且与时间导数和 Laplacian 交换，故
\[
(\partial_t-\nu\Delta)p
=-2\mathcal R_{ij}\bigl(u_i a_j+
\nu\,\partial_k u_i\partial_k u_j\bigr).
\tag{MPS.2}
\]
另一方面，由 \((D_t-\nu\Delta)u=-\nabla p\)，同样得到
\[
\begin{split}
(D_t-\nu\Delta)p
={}&[u\cdot\nabla,\mathcal R_{ij}](u_i u_j)
-2\nu\mathcal R_{ij}(\partial_k u_i\partial_k u_j)\\
&-2\mathcal R_{ij}(u_i\partial_j p).
\end{split}
\tag{MPS.3}
\]
这里 \([A,B]=AB-BA\)。将交换子展开并使用
\(u\cdot\nabla(u_i u_j)=u_i(u\cdot\nabla u_j)+u_j(u\cdot\nabla u_i)\)，
即可从 MPS.3 返回 MPS.2。两式不是两个独立控制机制。

每个 Riesz 输出及交换子的空间积分都为零；左端
\(\int_\Omega D_tp=\partial_t\int_\Omega p+\int_\Omega u\cdot\nabla p=0\)。
没有遗漏平均漂移。若改为 \(p+c(t)\)，左端必须增加 \(c'(t)\)；
不能在估计中无说明地改变压力规范。速度均值由原方程守恒。

## 2. 已有能量控制与逐壳交换项

以下界的常数可依赖固定周期胞、截止和黏性，不依赖光滑终点的高阶范数。
为书写 Sobolev 界，可作一次常速 Galilean 归一化，使速度均值为零；
这不限制原始数据。令 \(M=\sup_t\|u(t)\|_2\)、\(g(t)=\|\nabla u(t)\|_2\)。
基本能量控制 \(M\) 和 \(\int_a^b g^2\)，并给 \(u\in L^{10/3}_{t,x}\)。
Riesz 的 \(1<q<\infty\) 有界性给
\[
p\in L^{5/3}_{t,x},\qquad
\nabla p,\ a\in L^{5/4}_{t,x}.
\tag{MPS.4}
\]
后一个界直接从 \(\nabla p=(\mathbb P-I)(u\cdot\nabla u)\)、
\(a=\mathbb P(u\cdot\nabla u)\) 和 \(1/(10/3)+1/2=4/5\) 得到。
这些界不控制 \(u_i\partial_jp\) 或 \(u_i a_j\) 的时间—空间 \(L^1\)：
对应的 Hölder 倒数之和是 \(3/10+4/5=11/10>1\)。
这只指出当前估计不足，不构造实际乘积不可积的 NS 解。

交换项本身有能量类中的分布解释。定义
\(C=[u\cdot\nabla,\mathcal R_{ij}](u_i u_j)\)，则
\[
C=\operatorname{div}(up)
-\mathcal R_{ij}\partial_\ell(u_\ell u_i u_j)
\in L_t^{10/9}W_x^{-1,10/9}.
\tag{MPS.5}
\]
因为 \(up,u^{\otimes3}\in L^{10/9}_{t,x}\)，且周期 Riesz 在该指数有界。
这是整个周期域的负阶通量界；它不自动给出足以闭合局部尺度递推的尾项小量或严格增益。
固定分离内外球的远压导数界仍可由速度能量估计，常数依赖分离距离，不能将其说成完全不可控。
\(D_tp=\partial_tp+\operatorname{div}(up)\) 也可作为分布定义，
但这不使 MPS.3 右侧每个光滑乘积自动拥有弱解极限。
向一般能量弱解传递 MPS.2–3 时仍需正则化与缺陷检查，本轮没有完成或使用这种传递。

为检查核差的尺度，取非零高频壳 \(P_j\)，乘子为固定光滑环带截止
\(\psi(2^{-j}k)\)。固定两个分量指标 \(i,\ell\)，记 \(T_j=R_iR_\ell P_j\)；
这里 \(j\) 只表示频率壳，不作求和。
用全空间 Schwartz 核 \(K_j\) 周期化表示该算子。对任意光滑周期 \(F\)，
\[
[u\cdot\nabla,T_j]F(x)
=\int_{\mathbb R^3}
(u(x)-u(x-h))\cdot\nabla K_j(h)\,F(x-h)\,dh.
\tag{MPS.6}
\]
先把差写在 \(\nabla F(x-h)\) 前，再对 \(h\) 分部积分即得；
核导数外的散度项由 \(\nabla\cdot u=0\) 消失。
周期延拓的 \(u,F\) 允许沿全空间线段使用
\(u(x)-u(x-h)=\int_0^1 h\cdot\nabla u(x-sh)\,ds\)。
频率缩放给
\[
\int_{\mathbb R^3}|h|\,|\nabla K_j(h)|\,dh\le C.
\]
对 \(1\le r,p,q\le\infty\)、\(1/r=1/p+1/q\)，Minkowski、Hölder 和平移不变性因此给
\[
\|[u\cdot\nabla,T_j]F\|_r
\le C\|\nabla u\|_p\|F\|_q.
\tag{MPS.7}
\]
此处无额外 \(2^{-j}\)。选择 \(F=u_i u_\ell\)、\(p=2,q=3,r=6/5\)，得
\[
\|[u\cdot\nabla,T_j](u_i u_\ell)\|_{6/5}
\le C\|\nabla u\|_2\|u\|_6^2\le Cg(t)^3.
\tag{MPS.8}
\]
右端仅由能量给出 \(\int(g^3)^{2/3}=\int g^2<\infty\)，不足以推出时间 \(L^1\)。
这还是逐壳界，不能再无损地对所有壳求和。
MPS.7–8 只否定“核差中有一个距离因子，所以自动得到正的尺度幂”这一推断；
它们不否定更细的带符号抵消或多线性结构。

## 3. 换成物质压力导数后，局部伯努利式仍有余项

令 \(e=|u|^2/2\)、\(Q=e+p\)、\(\omega=\nabla\times u\)。
既有 [BE 记录](../clay_b_bernoulli_energy_gate_20260907.md) 从原方程给
\((D_t-\nu\Delta)Q=p_t-\nu|\omega|^2\)。取 \(C^1\) 权重 \(\phi\)、原函数 \(\Phi'=\phi\)
和光滑周期时空测试 \(\eta\)，链式法则和分部积分给完整式
\[
\begin{split}
[\!\int_\Omega\eta\Phi(Q)]_a^b
&+\nu\int_a^b\!\!\int_\Omega
\eta\{\phi(Q)|\omega|^2+\phi'(Q)|\nabla Q|^2\}\\
&=\int_a^b\!\!\int_\Omega
\Phi(Q)(\eta_t+u\cdot\nabla\eta+\nu\Delta\eta)
+\int_a^b\!\!\int_\Omega\eta\phi(Q)p_t.
\end{split}
\tag{MPS.9}
\]
若将最后一项写成沿流导数，准确结果是
\[
\begin{split}
\int_a^b\!\!\int_\Omega\eta\phi(Q)p_t
={}&\int_a^b\!\!\int_\Omega\eta\phi(Q)D_tp\\
&+\int_a^b\!\!\int_\Omega p\phi(Q)u\cdot\nabla\eta
+\int_a^b\!\!\int_\Omega\eta p\phi'(Q)u\cdot\nabla Q .
\end{split}
\tag{MPS.10}
\]
即使取全域 \(\eta=1\)，最后的非线性项也没有消失。
代入 MPS.3 还留下非局部压力反馈及黏性交叉项；本轮没有证明它们与 MPS.9 的耗散形成新的有利组合。
因此不能仅凭沿流导数比普通时间导数更自然，就宣称压力时间功已被控制。

## 4. 文献和已有记录：什么可用，什么不能移植

本轮使用已获授权的 Deep Research 作有界资格检查，非通用综述或原创性检索。
按“旧路线去重、原始来源定点核读、推导与适用范围复核、保存记录”推进。
计划工具不可用；未更换模型、开新用户任务或委派成稿。原始来源的准入判断由主任务完成。

最贴近的新定位是 [Isett，arXiv 1307.0565v9，2022-08-11](https://arxiv.org/html/1307.0565v9)：
对象是时间上一致空间 Hölder 的周期 Euler 流。Theorem 1.5 在指数大于 \(1/3\) 时给物质压力导数连续性。§4 区别真正压力频带和由截断速度生成的压力增量；§5.1 的高—高作用求和仍使用该指数条件。这些不是只凭 NS 能量成立的结论。主任务读了相关陈述及这两节证明，但没有核验全部上游引理，故不作为本稿的新外部定理依赖。

另一个题目含 Navier–Stokes 的近邻是
[Colombo–De Rosa，SIAM J. Math. Anal. 52(1)，2020](https://epubs.siam.org/doi/10.1137/19M1259900)：
原刊摘要限定耗散 \((-\Delta)^\alpha\)、\(0<\alpha<1/2\)，并假定一致空间 Hölder。
标准 Laplacian 对应 \(\alpha=1\)，不在该范围。本轮仅读摘要及出版信息，不调用其未读证明。

以下为统一的来源—主张台账；“已读”只指列明范围。

| 来源、版本与访问 | 本轮支持的主张 | 仍缺的证据／处理 |
|---|---|---|
| Isett，上述 v9；arXiv；访问 2026-09-08；主任务实读 Theorem 1.5 的共同假设和陈述、§4 全部、§5.1 全部 | 沿流压力增益的具体对象、额外输入及频率求和边界 | 未重审 §2 全部上游估计或全篇；未向黏性 NS 移植 |
| Colombo–De Rosa，上述原刊；2020-01-14 在线；访问 2026-09-08；摘要、元数据 | “含 NS 的标题”并不表示适用标准三维黏性问题 | 全文未读；只作范围排除 |
| [Tran–Yu，2018，Cambridge 章节的作者机构页](https://research-portal.st-andrews.ac.uk/en/publications/regularity-of-navier-stokes-flows-with-bounds-for-the-velocity-gr/)；访问 2026-09-08；摘要、元数据 | 有效压力、流线速度梯度的条件方法为既有文献 | 章节证明未读；本地 pressure quotient 已覆盖对应方向 |
| [Tran–Yu–Dritschel，2021，JFM 911 A18](https://doi.org/10.1017/jfm.2020.1033)；2021-01-25 在线；访问 2026-09-08；摘要、导言片段 | 速度—压力相关性有直接文献近邻 | 本轮未读 §3–4 证明；[R073U 中文报告 §6](../r073u_report-source.md) 已记录该碰撞，不重命名为新方向 |
| [BE](../clay_b_bernoulli_energy_gate_20260907.md)，2026-09-07；主任务全文 | MPS.9 的基础关系、普通时间压力项尚在 | BE 的状态一形式反例不是所有 NS 轨道补偿的否定 |
| [LP](../clay_b_leray_paid_budget_20260907.md)，2026-09-07；主任务全文，另一审读者全文 | 完整投影返回 NS；已有协方差源的 \(L^{4/3}\) 界不是临界输入 | 不重读全部随机表示原著；平均标签逆矩阵与虚速度不能自动当作已知 |
| BG、BT、BU、AG、MA；见配套审查记录中的文件名与范围；专项审读者核查，主任务不将未全文复读稿件作为新证明依赖 | 凸熵、Bernoulli 和加速度重写已有记录 | 不把伴随原子、非 NS 时间族、初端反例扩大为原 NS 终端结论 |

检索先围绕 pressure–transport / Bernoulli / material derivative / Riesz commutator，
再按具体缺口定位 Isett 的 coarse scale flow。也检查了现有压力正则性、压力相关性、随机表示和张量记录。
宽泛命中中与可压缩、数值离散或其他方程有关的来源未采用。
Constantin 作者 PDF xlnsF 的 URL 被打开以定位来源，但尚未定点审读其页面；
LP §6 已明确引用同一方法，因此未开展重复原著读取。
Isett v3 的导言初读后，以 arXiv 当前标明的 v9 校正版本；未沿用旧版的时代性问题状态。
没有把有限关键词未命中当作新颖性证据。

停止检索的理由是：当前对象的来源、输入边界、与旧路线的重合及本地代数缺口均已明确；
继续查询同义词不太可能改变准入判断。尚无足以向前证明的新具体估计。
这不等于所有相关文献已读完，也不等于所有压力方法均不可能成功。

## 5. 当前决定与后续限制

MPS.2–3、MPS.5–10 是本轮直接核算；不认领这些标准重写和交换核估计的新颖性。
新的内容是把这个候选的合法对象、可得范数、弱解乘积问题和不能自动移植的文献条件放在同一记录中。
没有取得无条件临界输入，没有生成联合好尺度，没有正则性或奇性结论。

停止将普通压力时间导数换成物质导数后直接作绝对值估计的支线；
不继续用相邻初端构造、频率变体或改名权重来填补结果数量。
如再进入压力方向，须先提出不同于 MPS.2–10 和既有 AP/MA 的具体带符号估计，
说明同一解上的全部端点、局部尾项、所需输入及其能否由原方程得到。
若仅假定一致 Hölder、小形状耗散或未证压力梯度的临界控制，则仍是条件研究，不准标为一般正则性进展。
当前新的动力学候选仍未选定。

本轮无仿真、DGX、数值证书或科学附图；无读者 HTML/PDF、英文翻译、累计 recap 或发布动作。
仅保存私有研究记录，不另建 release 或移交消息。既有 QPS/EWT 内部记录、EWP 独立冻结及其一次移交保持原样。
主稿由 AI 辅助推导、核对与撰写；配套审查明确实际读稿范围，不是真人同行评审。
