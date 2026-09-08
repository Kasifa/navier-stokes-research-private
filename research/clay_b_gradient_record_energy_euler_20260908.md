# 梯度纪录的能量尺度：非零 Euler 极限与退化分支

2026-09-08。私有研究记录。**LOCAL PROOF / CONDITIONAL DICHOTOMY / OPEN / NOT CLAY。**

梯度纪录可以直接给能量尺度上的空间梯度界，并使速度在包含纪录时刻的
闭时间柱上强紧。但这不保证梯度峰值留在极限中。下面把这个区别写清：
速度与梯度的比率有正下界时，得到非零 Euler 极限和终端能量原子；
比率趋零时，所有这类 Euler 极限都为零。两支都没有排除 NS 奇点。

尺度及主要压力工具来自 [BL](clay_b_critical_euler_compactness_20260906.md)，
终端测度来自 [BM](clay_b_euler_rigidity_energy_atom_20260906.md)。
本次增加的是梯度纪录选择下的闭顶端核算和比率分支，不宣称新颖性。
文献筛选没有提供能消除这些缺项的新估计；不继续把同一尺度改写成新路线。

## 1. 同一原解、纪录时刻与准确缩放

固定无外力、黏性 \(\nu>0\) 的光滑三维周期 NS 解，原胞为
\(\mathbb T^3=(-\pi,\pi]^3\)，压力取原胞零均值。固定
\(0<a<T_*<\infty\)，原解在 \([a,T_*)\) 光滑；不假设终端正则性。
令 \(G=\nabla u\)，矩阵范数为 Frobenius 范数。考察纪录序列
\[
 t_n\uparrow T_*,\qquad
 N_n=\max_{a\le t\le t_n}\|G(t)\|_\infty
     =|G(x_n,t_n)|\longrightarrow\infty,\qquad
 E=\sup_{a\le t<T_*}\|u(t)\|_2^2<\infty.
\tag{GRE.1}
\]
这是 [GRC](clay_b_gradient_record_compactness_20260908.md) 的同源选择，
不是另选初值。以下舍去有限项使 \(N_n\ge1\)。定义
\[
 \ell_n=N_n^{-2/5},\quad A_n=N_n^{3/5},\quad L_n=\ell_n^{-1},\qquad
 W_n(y,s)=A_n^{-1}u(z_n+\ell_n y,t_n+s/N_n),\quad
 \Pi_n(y,s)=A_n^{-2}p(z_n+\ell_n y,t_n+s/N_n).
\tag{GRE.2}
\]
空间中心 \(z_n\) 暂时任意，每个 \(n\) 固定，不作加速坐标变换，
也不减去中心速度。取 \(z_n=x_n\) 时才有中心单位梯度。
实际时间区间为 \(\sigma_n=N_n(a-t_n)\le s\le0\)，\(\sigma_n\to-\infty\)。
链式法则及 \(A_n/(N_n\ell_n)=1\) 给完整周期方程
\[
 \partial_sW_n+\operatorname{div}(W_n\otimes W_n)+\nabla\Pi_n
   =\nu_n\Delta W_n,\qquad
 \nu_n=\nu N_n^{-1/5}\longrightarrow0,\qquad
 \operatorname{div}W_n=0,\quad \int_{\mathbb T^3_{L_n}}\Pi_n=0.
\tag{GRE.3}
\]
因为 \(A_n^{-2}\ell_n^{-3}=1\)、\(\ell_n/A_n=N_n^{-1}\)，
\[
 \sup_{\sigma_n\le s\le0}\int_{\mathbb T^3_{L_n}}|W_n|^2\le E,
 \qquad |\nabla W_n|\le1,\qquad
 z_n=x_n\ \Longrightarrow\ |\nabla W_n(0,0)|=1.
\tag{GRE.4}
\]
于是每个固定 \(B_R\times[-H,0]\) 上的梯度平方积分至多
\(|B_R|H\)。这比 BL.3 的额外局部梯度条件强，但只在纪录时刻之前成立。
不能把顶端换回 \(T_*\)，或把此界用于 \((t_n,T_*)\)。
全胞完整历史另有
\[
 \int_{\sigma_n}^0\!\!\int|\nabla W_n|^2
   =N_n^{1/5}\int_a^{t_n}\!\!\int|G|^2,\qquad
 \nu_n\int_{\sigma_n}^0\!\!\int|\nabla W_n|^2
   =\nu\int_a^{t_n}\!\!\int|G|^2.
\tag{GRE.5}
\]
没有从有限总耗散得到未加权的全历史小量。

## 2. 全域速度、规范压力和包含顶端的紧性

在原胞的速度最大点取球。若最大值为 \(M\)，梯度不超过 \(N_n\)，
则在半径 \(M/(2N_n)\) 内速度至少为 \(M/2\)，只要球不超过固定
注入半径。超过时改取一个固定小球，得到 \(M\le C E^{1/2}\)。
两种情形合并给
\[
 \|u(t)\|_\infty\le C(E^{1/2}+E^{1/5}N_n^{3/5}),\qquad
 \sup_{\sigma_n\le s\le0}\|W_n(s)\|_\infty
 \le C(E^{1/5}+E^{1/2}N_n^{-3/5})\le K(E).
\tag{GRE.6}
\]
常数只依赖固定原胞；\(E=0\) 时不存在 GRE.1 的序列。
这是峰点球形式的插值上界，没有给速度的正下界。

对每个非零周期频率，规范压力乘子为
\(-k_i k_j/|k|^2\)，零频率为零。Parseval 直接给与胞长无关的界
\[
 \|\Pi_n(s)\|_{L^2(\mathbb T^3_{L_n})}
 \le C\|W_n(s)\otimes W_n(s)\|_2
 \le C K(E)E^{1/2}.
\tag{GRE.7}
\]
这用的是完整周期压力，不是减去任意时间常数后的局部压力。

固定空间截止 \(\chi\) 后，将 \(\chi W_n\) 零延拓。
GRE.3、GRE.4、GRE.6、GRE.7 使其时间导数在
\(L_s^\infty H_y^{-1}\) 一致有界：非线性与压力在局部 \(L^2\)，
黏性项一次分部后用局部梯度界，全部 \(\nabla\chi\) 项保留。
\(\nu_n\le\nu\)，故常数可以依赖 \(\nu,E,\chi\)，不依赖 \(n\)。
取单位质量光滑核 \(\rho_\delta\)，空间 Lipschitz 界与上述导数界给
\[
 \|\chi W_n-\rho_\delta*(\chi W_n)\|_\infty\le C\delta,
 \qquad
 \|\rho_\delta*(\chi W_n)(s)-\rho_\delta*(\chi W_n)(t)\|_\infty
 \le C|s-t|\delta^{-5/2}.
\tag{GRE.8}
\]
这里 \(0<\delta\le1\)，\(\|\rho_\delta\|_{H^1}\le C\delta^{-5/2}\)。
当 \(|s-t|\le1\) 时取 \(\delta=|s-t|^{2/7}\)，得到固定球上统一的时间
\(2/7\) 模量；较大时间差直接用一致速度界。
由空间 Lipschitz 界、有限网格和对角子列法，
\[
 W_n\longrightarrow W\quad\hbox{在每个 }B_R\times[-H,0]\hbox{ 上一致},
 \qquad |\nabla W|\le1,\quad |W|\le K(E),\quad
 \|W(s)\|_{L^2(\mathbb R^3)}^2\le E\quad(s\le0).
\tag{GRE.9}
\]
最后一项先在固定球传递，再令球半径增大，适用于每个时刻。
\(E\) 只是共同上界，没有断言扩张胞的全域能量强收敛。
这里没有梯度一致收敛。时间指数不是最优性主张。

## 3. 极限方程、压力规范和全空间能量

BL.10--17 的完整周期近远场分解可用于 GRE.9：在固定球上先截断
\(W_n\otimes W_n\)，局部强 \(L^2\) 和 Euclidean 压力乘子传递近源；
周期光滑修正不超过 \(CL_n^{-3}E\)，距离大于 \(R\) 的源不超过
\(CR^{-3}E\)。先固定 \(R\) 令 \(n\to\infty\)，再令 \(R\to\infty\)。
因此 \(\Pi_n\) 局部强 \(L^2\) 收敛到唯一规范代表
\[
 \Pi=\partial_i\partial_j(-\Delta)^{-1}(W_iW_j),\qquad
 \|\Pi(s)\|_2\le C K(E)E^{1/2},\qquad
 \partial_sW+\operatorname{div}(W\otimes W)+\nabla\Pi=0.
\tag{GRE.10}
\]
压力范数逐时几乎处处成立，足够用于以下时间积分。没有未定仿射压力。
黏性在固定柱的动量弱式中趋零，且
\(\nu_n\int_{B_R\times[-H,0]}|\nabla W_n|^2\le\nu_n|B_R|H\to0\)。
把原光滑局部能量等式传极限，得到 Euler 的局部能量等式。
三次输运与压力乘速度由上述强收敛传递；闭顶端局部能量项由 GRE.9
传递。故对任意固定紧支撑光滑 \(\eta\)、\(s<t\le0\)，
\[
 \frac12\int |W(t)|^2\eta-\frac12\int|W(s)|^2\eta
 =\int_s^t\!\!\int\left(\frac{|W|^2}{2}+\Pi\right)W\cdot\nabla\eta.
\tag{GRE.11}
\]
也可先在开时间域取得分布等式，再用局部时间连续性与可积通量延至端点。

取 \(0\le\eta_R\le1\)，在 \(B_R\) 等于一、支撑于 \(B_{2R}\)，
\(|\nabla\eta_R|\le C/R\)。全域速度和规范压力界给
\[
 \left|\int_s^t\!\!\int\left(\frac{|W|^2}{2}+\Pi\right)
 W\cdot\nabla\eta_R\right|
 \le \frac{C}{R}\int_s^t\big(K(E)E+\|\Pi\|_2\|W\|_2\big)d\tau
 \le\frac{C K(E)E|t-s|}{R}.
\tag{GRE.12}
\]
令 \(R\to\infty\)，得到全空间能量在所有有限时间对上守恒，包括顶端。
这是本次由纪录选择导出的全域速度界的结果，不把旧 BL 的局部等式直接说成全局守恒。

## 4. 比率的两个子列分支

定义纪录时刻的比率
\[
 M_n=\|u(t_n)\|_\infty,\qquad \kappa_n=M_nN_n^{-3/5}.
\tag{GRE.13}
\]
它有统一上界。任一纪录序列可选子列使 \(\kappa_n\to\kappa\ge0\)。
不能用整个历史的速度最大值替换 \(M_n\)：相应时刻可能在缩放中逃向
\(-\infty\)，旧 [BJ](clay_b_record_time_history_preflight_20260906.md)
已有的有界倍增窗口也是额外条件。

若 \(\kappa>0\)，取 \(\kappa_0>0\) 使该子列 \(\kappa_n\ge\kappa_0\)。
令 \(z_n\) 为同一 \(t_n\) 的速度最大点，GRE.9 给
\(|W(0,0)|\ge\kappa_0\)，因而 Euler 极限非零。
空间及时间连续性还给某个固定小柱上的 \(L^3\) 正下界。
但新中心不保证 \(|\nabla W_n(0,0)|=1\)。在原变量中，
\[
 r_n=\frac{M_n}{2N_n}\le C N_n^{-2/5}\longrightarrow0,\qquad
 \int_{B_{r_n}(z_n)}|u(t_n)|^2
 \ge\frac{\pi}{24}\frac{M_n^5}{N_n^3}
 \ge\frac{\pi}{24}\kappa_0^5.
\tag{GRE.14}
\]
球在原胞坐标内对充分大 \(n\) 成立。BM.5 的终端测度
\(|u(t)|^2dx\rightharpoonup^*\mu_*\) 对固定 \(\nu>0\) 同样成立：
固定截止的黏性、耗散和三次/压力通量均时间可积。
选 \(z_n\to z_*\)，先用任意固定小球截止传递终端测度，再缩球，得到
\(\mu_*(\{z_*\})\ge(\pi/24)\kappa_0^5>0\)。这是条件必要性，
这里是终端动能测度的原子，不是终端速度的原子；没有原子的存在性构造或排除定理。

若 \(\kappa_n\to0\)，则对任意空间中心序列，GRE.9 的极限都有
\(W(\cdot,0)=0\)。GRE.11--12 的能量守恒于是给 \(W\equiv0\)。
进一步，对每个固定 \(H>0\)，
\[
 \sup_{-H\le s\le0}\|W_n(s)\|_{L^\infty(\mathbb T^3_{L_n})}
 \longrightarrow0.
\tag{GRE.15}
\]
否则选过去值大于固定 \(\varepsilon>0\) 的空间时间点，改在该空间点
居中，时间仍以 \(t_n\) 为顶端。全部界不变，顶端全域速度仍趋零。
过去时刻在 \([-H,0]\) 有收敛子列，GRE.9 将峰值传给零 Euler 极限，矛盾。
这只证明速度衰减；在原梯度中心的单位导数并未传递。
\(\nu_n\to0\) 不提供统一的空间 \(C^1\) 紧性。

## 5. 对路线选择的含义

本次得到的不是一般正则性，而是对旧 Euler 绕行的更明确判断：

| 当前已证明 | 仍未证明 |
|---|---|
| 纪录选择直接给局部梯度界、闭顶端速度紧性和规范压力 | 单位梯度在极限中保留 |
| 正比率子列给非零有限能量 Euler 与终端原子 | 该原子不存在，或所有纪录都有正比率 |
| 零比率子列的所有有限过去窗口速度趋零 | 零速度极限排除原序列的梯度纪录 |

非零有限能量 Euler 本身不矛盾：BM 已核实 Gavrilov 的光滑紧支撑
定常流属于宽极限类；它不代表该流可由同一固定 NS 来源产生。
[BN](clay_b_periodic_no_atom_endpoint_20260906.md) 的无原子估计仍有额外
强可积性，[BO](clay_b_energy_atom_dissipation_20260906.md) 的原子耗散
下界仍趋零。这里没有消除这两项限制。

因此停止仅用现有能量、纪录上界再改写这一 Euler 尺度。
任何下一候选都须明确改善同一原解的梯度非退化或原子排除之一，
不能重新假设正比率、全局无原子或 Euler 全零刚性。
新的无条件机制尚未选定。本轮不生成新独立 release；TG 仍为最后独立冻结。
推导与复核均为 AI 辅助内部工作，不是外部真人同行评审。
