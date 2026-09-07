# 压力端点、应变谱耗散与冻结形状的相容性

2026-09-08，北京时间。SE，私有内部研究检查点，尚非独立研究发布。经典输入、范围内推导与下一项探索分开记录。未得到新的临界先验估计，不宣称新颖性或Clay问题完成。

## 1. 本轮选择与去重

TD–TP已经完成两点行列式与第一球谐矩的核查。其有效伸长配对回到既有滤波应变，两个普遍黏性单调性声明均已被光滑NS例否定。本轮不再改变那个量的投影或权重。

我改查完整应变的谱几何与微分相容性。先问：压力是否允许一个实际由基本能量控制的凸谱耗散；再问：这个耗散能否同中间特征值联系，而非只重复条件正则性判据。第二问仍在探索。

已读的最近邻包括：dynamic_strategy_review的中间特征值判据；R0.70Z §8的涡伸长Hardy–BMO配对；pressure_regularity_literature_check的空间压力增益边界；VB的涡量方向及零集预算；PGR的完整应变梯度与压力四次消项。这些稿件不提供本节末尾所需的变形状、局部化动力学估计。这个有限去重不是完整查新。

## 2. 压力Hessian的经典端点，在固定周期胞上怎样使用

固定未归一化的 \(\mathbb T^3_{2\pi}\)，同一个光滑、无散、无外力NS解，\(\nu>0\)。所有推导先在闭光滑区间 \([0,T]\) 上进行。记
\[
 A_{ij}=\partial_j u_i,\quad S=(A+A^\top)/2,\quad
 \Omega=(A-A^\top)/2,\quad H=\nabla^2p,
 \quad Y=\|A\|_2^2,\quad E=\tfrac12\|u\|_2^2.
 \tag{SE.1}
\]
压力取周期零均值规范，\(-\Delta p=f=\operatorname{tr}(A^2)\)。关键不是对任意L1输入应用Riesz变换，而是
\[
 f=\sum_j\nabla u_j\cdot\partial_j u,
 \qquad \operatorname{curl}\nabla u_j=0,\quad
 \operatorname{div}\partial_j u=0,\quad \int f=0.
 \tag{SE.2}
\]
由散度—旋度补偿，得到固定胞上的经典估计
\[
 \|f\|_{\mathcal H^1(\mathbb T^3)}\le C Y,
 \qquad \|H\|_1\le C_HY,
 \qquad \int_0^T\|H\|_1dt\le C_HE(0)/\nu.
 \tag{SE.3}
\]
这里 \(\mathcal H^1\) 是实Hardy空间，不是Sobolev \(H^1\)。对本节只需第二个不等式。常数只依赖固定胞和范数约定，不依赖终点的高阶范数。

为说明周期接口而非直接搬用全空间结论，写出标准局部证明。若 \(F\) 无散、\(b\) 周期光滑，\(g=F\cdot\nabla b\)，对支集在半径 \(r<r_0<\pi\) 球内的归一化光滑测试核分部积分，减去球平均 \(b_{B_r}\)，得
\[
 |\phi_r*g(x)|\le C\fint_{B_r(x)}|F|\frac{|b-b_{B_r}|}{r}
 \le C\big[M(|F|^{3/2})\big]^{2/3}
        \big[M(|\nabla b|^{3/2})\big]^{2/3}.
 \tag{SE.4}
\]
第二步使用三维 \(W^{1,3/2}\to L^3\) 的球上Sobolev–Poincaré及Hölder。再以空间L2–L2配对和最大算子的L4/3有界性积分，得到 \(C\|F\|_2\|\nabla b\|_2\)。固定胞上的大尺度测试由 \(\|g\|_1\) 控制。周期局部最大函数与原子Hardy范数的标准等价于是给SE.2的第一界。

剩下使用周期二阶Riesz变换的Hardy到L1有界性。其原子证明保留零模：小球均值零原子在两倍球内用L2有界性，在外部用核一阶差 \(C r/d^4\) 积分；胞尺度原子直接用L2。压力的零模设为零，核中的局部对角项也是L1有界项。这些是标准Hardy空间接口，本稿不重新证明原子分解定理本身。对SE.2按j求和，用Cauchy–Schwarz即得SE.3。最后一步使用 \(E(T)+\nu\int_0^T Y=E(0)\)。

这不是新的压力正则性结果。[CLMS研讨会原稿](https://www.numdam.org/item/SEDP_1989-1990____A16_0.pdf) XIV-3的Theorem 2、Corollary 3已给全空间对应结论；XIV-4给分部积分与最大函数证明。[Li–Zhang Theorem 1.2](https://arxiv.org/html/2106.11852v1)也明确给压力二阶导数的Hardy估计。原稿还登记了有初始梯度测度条件的梯度L1控制，故不能把下文的低阶范数界称为此前未知的突破。

## 3. 完整应变方程与凸谱链式法则

令 \(L=\partial_t+u\cdot\nabla-\nu\Delta\)。原NS给
\[
 LS=-S^2-\Omega^2-H=-N.
 \tag{SE.5}
\]
对 \(\varepsilon>0\) 设
\[
 \Phi_\varepsilon(S)=\operatorname{tr}\sqrt{S^2+\varepsilon^2I}-3\varepsilon,
 \quad Q_\varepsilon=S(S^2+\varepsilon^2I)^{-1/2},
 \quad d_\varepsilon=\sum_kD^2\Phi_\varepsilon(S)[\partial_kS,\partial_kS].
 \tag{SE.6}
\]
这些是在实对称矩阵空间上的光滑函数，\(\|Q_\varepsilon\|_{op}\le1\)。完整链式法则为
\[
 L\Phi_\varepsilon=-Q_\varepsilon:N-\nu d_\varepsilon,
 \qquad \frac d{dt}\int\Phi_\varepsilon+\nu\int d_\varepsilon
       =-\int Q_\varepsilon:N.
 \tag{SE.7}
\]
没有去掉压力，没有把惯性项假设为负。

以下明确其耗散。取S的任意正交特征基，特征值 \(\lambda_1\le\lambda_2\le\lambda_3\)，令 \(h_\varepsilon(z)=\sqrt{z^2+\varepsilon^2}\)。对实对称B，
\[
 D^2\Phi_\varepsilon(S)[B,B]
 =\sum_i\frac{\varepsilon^2 B_{ii}^2}{(\lambda_i^2+\varepsilon^2)^{3/2}}
 +2\sum_{i<j}
 \frac{h_\varepsilon'(\lambda_i)-h_\varepsilon'(\lambda_j)}{\lambda_i-\lambda_j}
 |B_{ij}|^2\ge0.
 \tag{SE.8}
\]
重根处差商按 \(h_\varepsilon''\) 连续延拓。简单谱时由特征值二阶扰动公式 \(\lambda_i''=2\sum_{j\ne i}|B_{ij}|^2/(\lambda_i-\lambda_j)\) 得出；一般谱由矩阵函数的连续性取极限。结果在重根子空间换基下不变。

源项有一个真实可积上界。S²与−Ω²半正定，故
\[
 |Q_\varepsilon:S^2|+|Q_\varepsilon:\Omega^2|\le |A|^2,
 \qquad |Q_\varepsilon:H|\le\sqrt3|H|.
 \tag{SE.9}
\]
SE.3于是控制SE.7右端的绝对时间积分；这一步不需要未知的涡量BMO系数。

## 4. 零特征值不能直接删去

令 \(\Phi(S)=\operatorname{tr}|S|\)，\(Q_0=\operatorname{sign}_0 S\)，其在零特征子空间为零。\(\Phi_\varepsilon\to\Phi\) 一致，\(Q_\varepsilon\to Q_0\) 逐点。固定闭光滑区间内，源项受可积函数控制，且 \(|\partial_t\Phi_\varepsilon|\le\sqrt3|\partial_tS|\)。因此 \(d_\varepsilon dxdt\) 有唯一非负测度极限
\[
 \mu=\frac{-Q_0:N-L\Phi(S)}{\nu}.
 \tag{SE.10}
\]
唯一性来自分布链式方程的极限；逐时 \(\int d_\varepsilon\le C_T\) 也排除光滑时间端点的聚集。

在开集 \(\det S\ne0\) 上，矩阵绝对值光滑，SE.8局部一致趋于
\[
 d_{\pm}=4\sum_k\sum_{\lambda_i>0>\lambda_j}
       \frac{|(\partial_kS)_{ij}|^2}{\lambda_i-\lambda_j}.
 \tag{SE.11}
\]
同号特征子空间内部的项为零，特征值幅度的对角导数也不在此密度中。由此严格有
\[
 \mu=\mathbf1_{\{\det S\ne0\}}d_{\pm}\,dxdt+\zeta,
 \qquad \zeta\ge0,\quad \operatorname{supp}\zeta\subset\{\det S=0\}.
 \tag{SE.12}
\]
特别注意：这里的零谱集合可有正体积。\(\zeta\) 可能含秩二开放集上的普通绝对连续耗散，并非必然是一个奇异测度。本节不声称已把零谱集合内部所有密度进一步分类。

写 \(\mathcal N(t)=\int\operatorname{tr}|S|\)，得到完整等式和上界
\[
 \mathcal N(T)+\nu\mu(\mathbb T^3\times(0,T))
 =\mathcal N(0)-\int_0^T\int Q_0:N,
\]
\[
 \boxed{\mathcal N(T)+\nu\int_0^T\int_{\det S\ne0}d_{\pm}
                 +\nu\zeta(\mathbb T^3\times(0,T))
 \le\mathcal N(0)+(1+\sqrt3C_H)E(0)/\nu.}
 \tag{SE.13}
\]
固定光滑初值的 \(\mathcal N(0)\) 有限。对有限候选终点可以令 \(T\uparrow T_*\) 控制非负累计量，不假定终点光滑延拓或强迹。

因此本轮确实取得一个能在候选终点前使用的经典型谱耗散预算，不仅是一条含未知右端的形式恒等式。但它不控制同号块的形状变化，也不控制中间特征值的临界时间范数。全空间NS缩放下，\(\mathcal N\) 及耗散的时空积分都按 \(\lambda^{-1}\) 变化；这里只比较齐次性，不把固定胞当成缩放不变空间。

## 5. 一项实际相容性计算：中间特征值与单频应变空间的距离

耗散只管谱子空间变化，是否能借助“应变来自同一个无散速度”的限制得到额外信息？先做冻结形状的严格计算，不预设其动态版本成立。

对单位n定义实单频应变子空间
\[
 \mathcal V_n=\{n\otimes a+a\otimes n:a\perp n\}.
 \tag{SE.14}
\]
系数中的1/2可吸收入a。对实迹零对称矩阵B，记 \(\Pi_n=I-n\otimes n\)，其正交投影与距离为
\[
 P_n B=n\otimes(\Pi_n Bn)+(\Pi_n Bn)\otimes n,
 \quad \operatorname{dist}(B,\mathcal V_n)^2
 =|B|^2-2\{n\cdot B^2n-(n\cdot Bn)^2\}.
 \tag{SE.15}
\]
若B的特征值为 \(b_1\le b_2\le b_3\)，花括号是支撑在 \([b_1,b_3]\) 上概率分布的方差，至多 \((b_3-b_1)^2/4\)。证明可用 \((x-b_1)(b_3-x)\ge0\) 后减去均值平方；等号由两端各半达到，即 \(n=(e_1+e_3)/\sqrt2\)。由于迹零，
\[
 \boxed{\inf_{|n|=1}\operatorname{dist}(B,\mathcal V_n)^2
       =|B|^2-\tfrac12(b_3-b_1)^2=\tfrac32 b_2^2.}
 \tag{SE.16}
\]
所以实应变波锥 \(\bigcup_n\mathcal V_n\) 恰是迹零对称矩阵中的中间特征值为零者。这是速度应变的空间约束，不是Euler时空微分包含里的另一种波锥。

由此还能直接证明一个定量冻结形状引理。设B固定且 \(b_2\ne0\)，\(a\in L^2(\mathbb T^3)\) 为实零均值标量，\(R\in L^2\) 为实对称矩阵场，且
\(S=aB+R=\operatorname{sym}\nabla u\)、\(\operatorname{div}u=0\)。则
\[
 \boxed{\|a\|_2\le\sqrt{2/3}\,|b_2|^{-1}\|R\|_2.}
 \tag{SE.17}
\]
证明：每个非零Fourier模上 \(\widehat S(k)\) 属于 \(\mathcal V_{k/|k|}\) 的复化空间。施加 \(I-P_{k/|k|}\)，再用SE.16，得到 \(\sqrt{3/2}|b_2||\widehat a(k)|\le|\widehat R(k)|\)；Parseval求和，a的零模为零。若R=0，则a=0。引理在任意固定时刻成立，不含新的NS演化假设。

## 6. 实际局部化：截断误差没有消失

取光滑截断 \(0\le\eta\le1\)，支撑在局部坐标球 \(B_{2r}\)，在 \(B_r\) 上为1，\(|\nabla\eta|\le C/r\)。令c为空间常向量（可取 \(B_{2r}\) 上u的平均），用完整周期Leray投影构造
\[
 v=P_{df}\{\eta(u-c)\},\quad
 \operatorname{sym}\nabla v=\eta S+E_\eta,
\]
\[
 E_\eta=\operatorname{sym}((u-c)\otimes\nabla\eta)
       -\nabla^2\Delta^{-1}((u-c)\cdot\nabla\eta),
 \qquad \|E_\eta\|_2\le C r^{-1}\|u-c\|_{L^2(\operatorname{supp}\nabla\eta)}.
 \tag{SE.18}
\]
逆Laplacian作用的源均值为零，因为它是 \(\operatorname{div}(\eta(u-c))\)。第二项一般遍及整胞，但其完整L2界成立，不能只保留局部第一项。v只是用于空间相容性估计的辅助无散场，不宣称它自身满足NS方程。

若在截断支集上写 \(S=s(x)B+R(x)\)，B仍固定且 \(b_2\ne0\)，设 \(\theta=|\operatorname{supp}\eta|/(2\pi)^3<1\)，则
\[
 \boxed{\|\eta s\|_2\le
 \frac{\sqrt{2/3}}{|b_2|\sqrt{1-\theta}}
 \left(\|\eta R\|_2+C r^{-1}\|u-c\|_{L^2(\operatorname{supp}\nabla\eta)}\right).}
 \tag{SE.19}
\]
证明不能假设 \(\eta s\) 零均值。令 \(a=\eta s-\fint\eta s\)，对SE.18去零模后应用SE.17，得到 \(\|a\|_2\le\sqrt{2/3}|b_2|^{-1}\|\eta R+E_\eta\|_2\)。另一方面，支集的体积分数给 \(\|a\|_2^2\ge(1-\theta)\|\eta s\|_2^2\)。二式合并即得结论。

选c为上述球平均，Poincaré只能将误差进一步估成 \(C\|A\|_{L^2(B_{2r})}\)，没有得到一个随r趋零自动改善的相对系数。SE.19因而是一个完整、真实的局部化估计，而不是高应变区域已经受到控制。

## 7. 尚未完成的真正问题

SE.13和SE.17不能直接相接。前者只估计跨正负特征子空间的变化；后者的R要求控制整个矩阵偏离同一个固定形状B。同号子空间内部的幅度比例变化未受SE.11约束。把B取成随x变化的 \(S/|S|\) 后，SE.17的Fourier证明不再成立。空间截断也不保留应变的全局微分相容性，不能删除截断余项。

下一项探索限定为这个区别：在 \(\lambda_2(S)\ge\delta|S|>0\) 的高应变区域，检验是否能由完整动力学控制SE.19中的形状余项与边界误差；\(\delta>0\) 是分区参数，不是假定全解处于该区域。局部化第一步SE.18–19已经完成，不在下一轮重新推导。还需单独估计 \(0<\lambda_2<\delta|S|\) 的贡献。需要时再阅读一般微分约束测度的原著，不从检索摘要移植定理，更不能把仅控制正负子空间误认作控制全部形状。

允许探索未证的困难估计；当前没有证明上述高应变区的动力学控制，也没有证明它不可能。不能把L1梯度、有限谱耗散或冻结形状刚性单独升级为任意初值正则性。这里没有新反例、数值仿真、DGX计算或科学附图。

此为内部推导检查点，不新增release，不重复交接已经发送的TD–TP包。后续在完成这个研究小节及实际文件审查后再作完整科学冻结。推导与复核由AI任务完成，不是人类同行评审；审查范围另记。
