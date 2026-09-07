# 单尺度秩一偏离平方：弱闭合与局部正则判据

2026-09-08，北京时间。RS，PRIVATE_CORE。局部条件命题；一般三维 NS 仍 OPEN / NOT CLAY。不宣称新颖性或真人同行评审。

这一节证明 LD 留下的单尺度候选。在局部能量、耗散和压力有一个给定上界时，梯度偏离秩一矩阵的平方积分足够小，可以排除中心奇点。不再要求候选终点前光滑，也不要求偏离的临界时空 L^(5/2) 范数有限。

这仍不是任意初值的正则性证明。小量阈值依赖所给局部上界，证明不提供可计算的阈值或偏离到正则半径的速率。基本耗散有限，也没有自动给出指定中心所需的小量尺度。

## 1. 精确命题

单位黏性、无外力，记 \(Q_r=B_r(0)\times(-r^2,0)\)。指定 \((u,p)\) 是 \(\overline{Q_1}\) 的某个时空邻域上的局部适当弱解：满足分布 NS、无散度、局部能量不等式，以及局部能量类和 \(p\in L^{3/2}\)。不附加初值、Dirichlet 边界或终点前光滑条件。定义
\[
 \mathsf A(r)=r^{-1}\operatorname*{ess\,sup}_{-r^2<t<0}\int_{B_r}|u|^2,
 \quad \mathsf E(r)=r^{-1}\int_{Q_r}|\nabla u|^2,
 \quad \mathsf D(r)=r^{-2}\int_{Q_r}|p-(p)_{B_r}(t)|^{3/2}.
 \tag{RS.1}
\]
矩阵记为 \(G=\nabla u\)，\(G_{ij}=\partial_j u_i\)，与能量量 \(\mathsf A\) 区分。定义
\[
 d(G)=\operatorname{dist}_F(G,\{\text{所有实秩至多一矩阵}\}),
 \qquad \mathsf H(r)=r^{-1}\int_{Q_r}d(\nabla u)^2.
 \tag{RS.2}
\]
比较集合不另加迹零条件，方向允许随时空变化，不选定共同剪切轴。

**命题（局部证明，PROVED IN STATED SCOPE / CONDITIONAL）。** 对每个有限 \(M>0\)，存在 \(\epsilon(M)>0\)，使
\[
 \mathsf A(1)+\mathsf E(1)+\mathsf D(1)\le M,
 \qquad \mathsf H(1)<\epsilon(M)
 \quad\Longrightarrow\quad (0,0)\text{ 正则}.
 \tag{RS.3}
\]
正则指速度在某个后向内柱本质有界。单位尺度可由通常的 NS 缩放移到任意内柱；本节不另写含黏性的版本。

证明分三件事：梯度子式把秩一约束传给极限；调和压力的时间积分和小幂测试使极限速度达到高于临界指数5的时空可积性；最后把速度及压力的小量传给原近似解。它们各自需要论证，不能用“极限是剪切流”一句代替。

## 2. 紧性不要求梯度强收敛

若 RS.3 不成立，则有一个固定 M 和中心均非正则的适当弱解序列，使所列上界成立、\(\int_{Q_1}d(\nabla u_n)^2\to0\)。从开始就令
\[
 P_n=p_n-(p_n)_{B_1}(t).
\]
减去只依赖时间的函数不改 NS 或局部能量不等式。这个压力规范在后面的较小柱仍保持固定，不把不同半径的均值混用。

能量插值给 \(u_n\) 在 \(Q_1\) 一致有界于 \(L^{10/3}\)。在任意固定内球上，方程
\[
 \partial_tu_n=\operatorname{div}(\nabla u_n-u_n\otimes u_n-P_n I)
 \tag{RS.4}
\]
给 \(\partial_tu_n\) 在 \(L^{3/2}_tW^{-1,3/2}_x\) 一致有界。这里 \(W^{-1,3/2}=(W^{1,3}_0)^*\)；\(u_n\otimes u_n\in L^{5/3}\)、压力在 \(L^{3/2}\)、梯度在 \(L^2\)，固定有限柱上的嵌入正好足够。

使用 \(H^1\Subset L^2\hookrightarrow W^{-1,3/2}\) 的 Aubin–Lions 紧性，取子列得到在例如 \(B_{3/4}\times(-3/4,0)\) 上
\[
 u_n\to u\text{ 强 }L^2\text{ 及强 }L^3,
 \quad \nabla u_n\rightharpoonup\nabla u\text{ 弱 }L^2,
 \quad P_n\rightharpoonup P\text{ 弱 }L^{3/2}.
 \tag{RS.5}
\]
强 L3 由强 L2 与一致 L^(10/3) 插值得到，插值参数为1/6。时间区间一直到开端点0，紧性并不需要弱极限在正时间有延拓。极限保留能量界和分布 NS；局部能量不等式中的 \(P_nu_n\) 用弱 L^(3/2) 与强 L3 传递，耗散用弱下半连续性。故极限在开柱内部仍适当。最终只对原来的适当解应用终点正则判据。

设 G 的奇异值 \(s_1\ge s_2\ge s_3\ge0\)。最佳秩一逼近及余子式的奇异值给
\[
 d(G)^2=s_2^2+s_3^2,
 \quad |\operatorname{cof}G|_F^2=s_1^2s_2^2+s_1^2s_3^2+s_2^2s_3^2
 \le |G|_F^2d(G)^2.
 \tag{RS.6}
\]
因此 \(\|\operatorname{cof}\nabla u_n\|_{L^1}\to0\)。每个二阶子式又满足分布恒等式
\[
 \partial_j u_i\partial_l u_k-\partial_l u_i\partial_j u_k
 =\partial_j(u_i\partial_lu_k)-\partial_l(u_i\partial_ju_k).
 \tag{RS.7}
\]
右端是强 L2 函数与弱 L2 梯度的乘积对固定光滑测试函数的配对，故由 RS.5 收敛到极限子式。结合 RS.6，\(\operatorname{cof}\nabla u=0\) 分布成立；它本来属于 L1，所以几乎处处成立，即 \(\operatorname{rank}\nabla u\le1\)。没有使用非凸 d 的弱下半连续性，也没有假设梯度强收敛。

## 3. 秩一极限的压力在空间上调和

几乎处处，秩至多一的 G 可写成 \(a\otimes b\)，而无散度给 \(a\cdot b=\operatorname{tr}G=0\)。于是 \(G^2=0\)。这里只用逐点代数，不需要可微或可测的奇异向量选择。

对局部 H1、无散度的速度，空间光滑化并取极限可验证
\[
 -\Delta P=\partial_i\partial_j(u_iu_j)
 =\partial_j u_i\partial_i u_j=\operatorname{tr}(G^2)=0
 \quad\text{（分布）}.
 \tag{RS.8}
\]
光滑化后的 H1 强收敛使右端 L1 收敛，乘积 \(u_iu_j\) 也局部 L1 收敛，因而该压力恒等式不要求二阶速度导数。

取固定 \(I=(-1/2,0)\)。由调和函数内估计，对每个非负整数 k，
\[
 \|\nabla P(t)\|_{C^k(\overline{B_{2/3}})}
 \le C_k\|P(t)\|_{L^{3/2}(B_{3/4})}
 \quad\text{a.e. }t\in I.
 \tag{RS.9}
\]
因此压力梯度在较小球上属于 \(L^{3/2}_tC^k_x\)。这不是时空 L^μ、μ>5/3 的条件，不能直接套 O'Leary 的定理1；也不自动给压力的时间光滑性。

令
\[
 h(x,t)=\int_{-1/2}^t\nabla P(x,s)\,ds,\qquad v=u+h.
 \tag{RS.10}
\]
RS.9 及时间 Hölder 给 h 及全部空间导数在固定内柱上一致有界；同时 \(\operatorname{div}h=0\)、\(\Delta h=0\)、\(h_t=\nabla P\)。分布方程精确变为
\[
 \operatorname{div}v=0,\qquad
 v_t-\Delta v+v\cdot\nabla v=F,
 \quad F=h\cdot\nabla v+u\cdot\nabla h\in L^2.
 \tag{RS.11}
\]
v 仍属于局部能量类。F 的 L2 由有界 h、\(\nabla h\) 及原能量界直接控制；不是新的压力或梯度临界估计。下一步只证明 v 的较高可积性，不宣称任意 L2 外力的 NS 解都本质有界。

## 4. 合法的小幂截断：三次提高可积性

以下给出 [O'Leary 1998，§2](https://ejde.math.txstate.edu/Volumes/1998/12/Oleary.pdf) 截断估计在 RS.11 下所需的有限步骤。它是对该证明的明示适配，不是直接援引压力梯度定理或新的 De Giorgi 方法。

固定一个内柱、一个分量 i、\(k\ge1\)，令 \(w=(v_i-k)_+\)。取空间紧支、在父柱底部为零、内柱为一的光滑时空截止 \(\zeta\)，固定小幂 \(e=1/2\)。先在顶时 \(\tau<0\) 计算，空间和时间光滑化 v 与方程，再以 \(\{(v_i-k)_++\delta\}^{e}\zeta^2\) 的相容平滑形式测试；可减去 \(\delta^e\) 使其在低水平区为零。先去掉正则化、再用 Fatou 保留正的扩散项，得到
\[
 \|w^{(e+1)/2}\zeta\|_{V^2}^2
 \le C_\zeta\left\{\int w^{e+1}+\int|v|w^{e+1}
                    +\int|F|w^e\right\}.
 \tag{RS.12}
\]
这里 \(\|f\|_{V^2}^2=\operatorname*{ess\,sup}_t\int|f|^2+\int|\nabla f|^2\)，右端在同一固定父柱积分，常数也包含固定 e。

测试合法性的关键是基础能量类已给 \(v\in L^{10/3}\)、\(\nabla v\in L^2\)，故
\[
 |v|^{1+e}|\nabla v|\in L^1,
 \qquad \frac{1+e}{10/3}+\frac12=\frac{19}{20}<1,
 \qquad |F||v|^e\in L^1.
\]
因此光滑化的非线性项与小幂乘子可用 Hölder 强收敛去极限。对流先写成 \(v\cdot\nabla(w^{e+1}/(e+1))\)，无散度使内部项消失，留下的正是 RS.12 的截止项 \(\int|v|w^{e+1}\)。扩散交叉项用 Young 吸收到 \(\nabla w^{(e+1)/2}\) 项，余项为 \(\int w^{e+1}|\nabla\zeta|^2\)。时间项保留 \(w^{e+1}\) 的切片值。没有以高幂 v 直接测试，也没有假设原弱解满足涡量能量恒等式。

更具体地，先对固定 \(\tau<0\) 令时间光滑化宽度小于其到0的距离，再去掉光滑化。所有右端由到0的同一个父柱范数控制，独立于 \(\tau\)；最后取本质上确界及单调极限 \(\tau\uparrow0\)。每个截止只在较早底部消失，不在0附近引入导数越来越大的截止，因此得到真正覆盖后向顶端的界。

若 \(v\in L^\beta\)、\(\beta\ge10/3\)，令 \(N_\beta=\int|v|^\beta\) 为父柱积分。三个右端分别至多为
\[
 N_\beta k^{e+1-\beta},\qquad
 N_\beta k^{e+2-\beta},\qquad
 \|F\|_2N_\beta^{1/2}k^{e-\beta/2}.
 \tag{RS.13}
\]
最后一项先对 \(\{|v_i|>k\}\) 用 Cauchy，再用水平集估计；这一步只需 F 在 L2。

三维抛物 Sobolev 不等式使 RS.12 左端控制
\(k^{e+1}|\{v_i>2k\}\cap Q_{inner}|^{3/5}\)。将 RS.13 代入，并对负部重复，得到
\[
 v\in L^{\alpha(\beta),\infty}(Q_{inner}),\qquad
 \alpha(\beta)=\min\left\{\frac53(\beta-1),\frac53(\beta/2+1)\right\}.
 \tag{RS.14}
\]
小于 \(\alpha(\beta)\) 的强 Lq 可积性由层蛋糕积分得到；不把弱端点等同于强端点。只用三个嵌套固定内柱即可选择
\[
 \frac{10}{3}\longrightarrow\frac{15}{4}
 \longrightarrow\frac92\longrightarrow\frac{21}{4}>5.
 \tag{RS.15}
\]
三次对应 \(\alpha=35/9,55/12,65/12\)，各箭头目标严格小于该值。可以从 \(B_{2/3}\times I\) 内的 \(Q_{1/2}\) 开始，在 \(Q_{5/12},Q_{1/3},Q_{1/4}\) 依次提高。于是 \(v\)、以及 \(u=v-h\)，在 \(Q_{1/4}\) 属于 L^(21/4)。

特别地，Hölder 给极限速度的尺度衰减
\[
 C_u(r):=r^{-2}\int_{Q_r}|u|^3
 \le C\|u\|_{L^{21/4}(Q_{1/4})}^3r^{3-15/(21/4)}
 =K_u r^{1/7}\longrightarrow0.
 \tag{RS.16}
\]
这里 \(K_u\) 有限就足够。没有把极限在未来延拓，没有在一般 forced-v 方程上使用原始无外力正则性定理。若原来的调和压力弱解本身在候选点邻域定义，RS.16 与调和压力衰减也给该解的通常局部正则性。

## 5. 压力不强收敛，也能向原解传递小量

取固定空间 \(\xi\in C_c^\infty(B_{3/4})\)，在 \(B_{1/2}\) 为一。所有时间限于 I。用标准 Riesz 变换 \(\mathcal R_i\) 定义
\[
 \pi_n=\mathcal R_i\mathcal R_j(\xi u_{n,i}u_{n,j}),\qquad
 \pi=\mathcal R_i\mathcal R_j(\xi u_i u_j),\qquad
 q_n=P_n-\pi_n.
 \tag{RS.17}
\]
RS.5 与 Calderón–Zygmund 界给 \(\pi_n\to\pi\) 强 L^(3/2)(\(\mathbb R^3\times I\))。\(q_n\) 在 \(B_{1/2}\) 上调和，且在该球乘 I 的 L^(3/2) 积分一致有界于某个 K(M)。由于极限满足 RS.8，\(\pi\) 本身也在 \(B_{1/2}\) 上调和；它的该积分同样有限且受 M 控制。

调和函数内估计给任意 \(0<r<1/4\)，
\[
 r^{-2}\int_{Q_r}(|q_n|^{3/2}+|\pi|^{3/2})
 \le Kr\int_I\int_{B_{1/2}}(|q_n|^{3/2}+|\pi|^{3/2})
 \le K(M)r.
 \tag{RS.18}
\]
半径1/2固定，相关几何常数计入 K。时间小区间的积分只放大到 I；没有假设调和部分在时间 L∞，也没有把它设成零。\(q_n\) 的强收敛完全不需要。

从 \(P_n=(\pi_n-\pi)+\pi+q_n\)，先固定 r 再令 n 趋于无穷，得
\[
 \limsup_n r^{-2}\int_{Q_r}|P_n|^{3/2}\le K(M)r,
 \qquad r^{-2}\int_{Q_r}|u_n|^3\longrightarrow C_u(r).
 \tag{RS.19}
\]
注意左侧是从 B1 固定规范化的压力，不是 RS.1 中小球均值版本；应用 CKN 时这一固定时间规范合法。

令 \(\epsilon_{CKN}>0\) 为 [Gustafson–Kang–Tsai，Theorem 2.2](https://arxiv.org/html/math/0607114v1) 记录的无外力单尺度判据阈值。先由 RS.16 选择足够小的固定 r，使 \(C_u(r)+K(M)r<\epsilon_{CKN}/2\)；再由 RS.19 取足够大的 n，使原近似解的
\[
 r^{-2}\int_{Q_r}(|u_n|^3+|P_n|^{3/2})<\epsilon_{CKN}.
 \tag{RS.20}
\]
原近似解都定义在 \(\overline{Q_1}\) 的邻域并且适当，因而它们的中心正则，与选取矛盾。RS.3 得证。r 在 n 之前固定；没有将两个极限交换或把未知的 \(\epsilon(M(r))\) 当作普适常数。

## 6. 意义、文献范围与下一问题

相对于 LD，本节的输入更贴近基本耗散：在一个受控尺度上只需 d² 小量，并允许一般局部适当弱解。证明使用的紧性、梯度子式、调和压力估计、O'Leary 小幂截断及 CKN 转移均有标准来源或明确先例；本节将所需适配写出，不把这种组合自动称为原创结果。

[Kukavica–Rusin–Ziane，Theorem 2.4/2.5](https://arxiv.org/html/1511.02807v1) 已给真正局部的“固定速度三次上界＋压力小量”判据。它是重要的相邻结果，但调和压力的 \(D(r)\to0\) 单独不足以直接使用它：同时变化的速度尺度界会改变其未知阈值。本证明用 RS.16、RS.19 和固定 CKN 阈值明确处理这点。它也不依赖把 NP 的 Dirichlet／内部开集谱判据改写成别的解类。

新结论没有给任意实际 NS 演化的 \(\mathsf H(r)\) 衰减。对于任意给定中心，需要同时控制 \(\mathsf A(r)+\mathsf E(r)+\mathsf D(r)\) 并使 \(\mathsf H(r)<\epsilon(M)\)。仅 \(\int|\nabla u|^2<\infty\) 不能消除 \(r^{-1}\) 因子。既有光滑剪切示例、有限计算和条件临界范数判据也不补上这一步。

下一项优先检查实际动力学能否产生这样的受控小量尺度。先分析本判据的逆否命题在所有中心尺度上究竟给什么必要条件，再检验有限耗散、现有形状熵与尺度集中之间有没有可严格相加的新矛盾；不把条件判据的再次改写计作无条件进展。有效阈值、最小假设和充分查新仍另行开放。

## 7. 实际核查边界

主任务全文读回 LD 及其审计、清单，保留原冻结文件。GKT 本轮实际核对适当解定义、Theorem2.2、压力分解 Lemma3.4 及相邻上下文；不宣称重证 CKN 或全部外部依赖。KRZ 主任务实际核对定义、导言和定理表述，协作者另核其紧性和压力定理证明；不把协作者全文阅读冒记为主任务全文审计。

O'Leary 官方 TeX 本轮实际全文读取；原 PDF 第2页及第4–9页逐页渲染检查，确认定理与截断公式。原文个别排字错误不照抄：时间切片应是 \(w^{e+1}\)，力项换绝对值后是上界而非带符号恒等式。本节重写所需估计。只读 PDF 副本私有保存，未修改或重新导出；原文保存不是对全部参考文献的审计。

本轮是有界原文检索，不是 Deep Research 全面综述。参与推导的两位 AI 审读者与主任务分别核查，实际版本见配套审计；不称为完全非作者或真人同行评审。没有仿真、DGX、数值证书、科学附图、读者 HTML/PDF、公开摘要或网页操作。完成包仅一次交固定发布任务作 PRIVATE_ARCHIVE。
