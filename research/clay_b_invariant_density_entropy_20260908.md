# 椭圆不变密度：压力配对的改写与动态代价

2026-09-08。ID，PRIVATE_CORE，内部方法核算，不另计完成研究小节。这里选定并检查一个不同于 AH 常矩阵参考、VR 空间变参考的候选：用归一化梯度生成椭圆伴随密度，再对原梯度范数熵加权。得到的是一个可直接证明的空间构造和完整的光滑动态恒等式；没有得到新的无条件临界估计。一般三维 NS、PF 指定中心联合好尺度仍 OPEN / NOT CLAY。

## 1. 方程、参数与算子约定

在 \(\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3\) 上，取同一无外力光滑 NS 解的闭前终端区间 \(0<a<b<T_*\)，黏性 \(\nu>0\)。不限制其光滑无散原初值大小。令 \(V=(2\pi)^3\)、\(G_{ij}=\partial_j u_i\)、\(H=\nabla^2p\)、\(f=\operatorname{tr}(G^2)\)，故 \(-\Delta p=f\)、\(\int f=0\)。矩阵内积为 Frobenius 内积；\(G^2\) 是矩阵乘法，不是逐项平方。

固定 \(\kappa>0\)、\(0<\alpha\le1\)，定义
\[
 q_\kappa=(|G|^2+\kappa^2)^{1/2},\quad
 \Phi_\kappa=q_\kappa-\kappa,\quad
 B_\kappa=G/q_\kappa,\quad
 \Sigma_\kappa=\operatorname{sym}B_\kappa,\quad
 A=I+\alpha\Sigma_\kappa.
 \tag{ID.1}
\]
\(\Sigma_\kappa\) 对称、迹零且 \(|\Sigma_\kappa|_F\le1\)。以下常数 \(c_*=\sqrt{2/3}\)。对任意单位向量 \(e\)，用 \(|e\otimes e-I/3|_F=c_*\) 得
\[
 (1-\alpha c_*)I\le A\le(1+\alpha c_*)I.
 \tag{ID.2}
\]
它在允许的全部 \(\alpha\) 上一致椭圆。这是空间系数界，不是 NS 正则性结论。

记 \(P_0\) 为删除空间均值。本文统一采用正 Fourier 符号
\[
 QF=\Delta^{-1}\partial_i\partial_jF_{ij},\qquad
 \widehat{QF}(k)=(\widehat k\otimes\widehat k):\widehat F(k)\ (k\ne0),\qquad
 \widehat{QF}(0)=0,
 \tag{ID.3}
\]
其中 \(\widehat k=k/|k|\)。伴随算子 \(Q^*h=\nabla^2\Delta^{-1}P_0h\)，特别是 \(Q^*f=-H\)。对逐点迹零的张量场 \(F\)，Plancherel 给 \(\|QF\|_2\le c_*\|F\|_2\)；一般张量只有常数 1，不能无条件使用 \(c_*\)。

## 2. 密度的构造、非负性与统一空间界

在每个时刻求归一化椭圆伴随密度
\[
 \partial_i\partial_j(A_{ij}\rho)=0,\qquad \fint\rho=1.
 \tag{ID.4}
\]
令 \(T_\kappa h=Q(\Sigma_\kappa h)\)、\(K=I+\alpha T_\kappa\)、\(a_\kappa=Q\Sigma_\kappa\)。ID.4 等价于
\[
 K\rho=1,\qquad \rho-1=-\alpha T_\kappa\rho,\qquad
 \|T_\kappa\|_{2\to2}\le c_*<1.
 \tag{ID.5}
\]
因此 Neumann 级数给唯一 \(L^2\) 密度，均值自动为 1。这里 \(\rho\) 是每时刻的椭圆解，不另外假设它满足某个输运或热方程。利用均值正交，得到比直接逆算子估计更好的界：
\[
 \|\rho\|_2^2=V+\|\rho-1\|_2^2
 \le V+\alpha^2c_*^2\|\rho\|_2^2,
 \qquad
 \|\rho\|_2\le\sqrt{\frac{V}{1-\alpha^2c_*^2}}\le\sqrt{3V}.
 \tag{ID.6}
\]
这个界与 \(u\)、\(t\)、\(\kappa\) 无关；它没有给密度的点态上界或正下界。

为避免将文献中省略的正性证明当成本地已核证明，下面直接证明 \(\rho\ge0\)。设 \(L_Av=A:D^2v\)。周期 Fourier 恒等式给
\[
 \|P_0(\alpha\Sigma_\kappa:D^2v)\|_2
 \le\alpha\|D^2v-\tfrac13(\Delta v)I\|_2
 =\alpha c_*\|\Delta v\|_2.
 \tag{ID.7}
\]
最后的等式是积分恒等式，不是一般 Hessian 的逐点等式。于是 \(P_0L_A:H^2_{\mathrm{mean}\,0}\to L^2_{\mathrm{mean}\,0}\) 由 Neumann 级数可逆。对每个光滑 \(F\ge0\)，解 \(P_0L_Av=P_0F\)。其余差为常数，写成 \(L_Av=F-c\)。光滑系数下的标准椭圆正则性使 \(v\) 光滑；ID.4 的弱伴随关系给 \(c=V^{-1}\int\rho F\)。在 \(v\) 的最大点，ID.2 给 \(L_Av\le0\)，所以 \(c\ge F(x_{\max})\ge0\)。对所有这样的 \(F\) 成立，故 \(\rho\ge0\) 几乎处处。

固定本节的光滑系数，伴随椭圆正则性也使 \(\rho\) 空间光滑；随时间的光滑性可由 ID.5 的逆算子和光滑系数微分取得。本文不声称这些导数有能量一致的界。非负性足够解释以下加权非负耗散，不需要先建立严格正性。

## 3. 压力改写没有小参数收益

以 \(p\) 测试 ID.4，利用 \(H\) 对称，得到
\[
 \int\rho B_\kappa:H=\int\rho\Sigma_\kappa:H
 =\frac1\alpha\int\rho f.
 \tag{ID.8}
\]
右边没有显式 Hessian，却仍是非局部、带符号的二次源配对，不能由这个等式认定压力已经从动力学中消失。

ID.5 给精确一阶展开和余项界
\[
 \rho=1-\alpha a_\kappa+R_{\alpha,\kappa},\qquad
 \|\rho-1\|_2\le\frac{\alpha}{1-\alpha c_*}\|a_\kappa\|_2,\qquad
 \|R_{\alpha,\kappa}\|_2
 \le\frac{\alpha^2c_*}{1-\alpha c_*}\|a_\kappa\|_2,
 \tag{ID.9}
\]
其中 \(\|a_\kappa\|_2\le c_*\sqrt V\)。因为 \(\int f=0\) 且 \(Q^*f=-H\)，
\[
 I_\kappa:=\int B_\kappa:H=-\int f a_\kappa,\qquad
 \left|\frac1\alpha\int\rho f-I_\kappa\right|
 \le\frac{\alpha c_*}{1-\alpha c_*}\|a_\kappa\|_2\|f\|_2.
 \tag{ID.10}
\]
因此在固定光滑时间片、固定 \(\kappa\) 上，\(\alpha\downarrow0\) 恰回到原来的无权压力配对，而不是使它变小。这里用到 \(\|f\|_2\le\|G\|_4^2\)，并非只依赖基本能量的终端界。

## 4. 完整加权熵及权重的时间成本

令 \(L_{\rm NS}=\partial_t+u\cdot\nabla-\nu\Delta\)、\(R_{\rm test}=\partial_t+u\cdot\nabla+\nu\Delta\)。直接对 \(q_\kappa\) 求导：
\[
 L_{\rm NS}\Phi_\kappa+\nu D_\kappa=-B_\kappa:(G^2+H),\qquad
 D_\kappa=\sum_j\left(\frac{|\partial_jG|^2}{q_\kappa}
 -\frac{(G:\partial_jG)^2}{q_\kappa^3}\right)\ge0.
 \tag{ID.11}
\]
乘以 \(\rho\) 并使用 ID.8，所有空间积分均在全环面、所有双积分均在 \([a,b]\times\mathbb T^3\)，有
\[
 \left[\int\rho\Phi_\kappa\right]_a^b+\nu\iint\rho D_\kappa
 =\iint\Phi_\kappa R_{\rm test}\rho
 -\iint\rho B_\kappa:G^2-\frac1\alpha\iint\rho f.
 \tag{ID.12}
\]
不能把 \(B_\kappa:G^2\) 换成 \(\Sigma_\kappa:G^2\)，因为 \(G^2\) 一般不对称。

时间变化由 ID.5 决定，而不是可以自由选取：
\[
 \rho_t=-\alpha K^{-1}Q(\rho\Sigma_{\kappa,t}),\qquad
 \|\rho_t\|_2\le\frac{\alpha c_*}{1-\alpha c_*}
 \|\rho\Sigma_{\kappa,t}\|_2,
 \quad
 \Sigma_{\kappa,t}=q_\kappa^{-1}\operatorname{sym}
 \{G_t-B_\kappa(B_\kappa:G_t)\}.
 \tag{ID.13}
\]
这里使用的是完整的迹零 \(\Sigma_{\kappa,t}\)。\(I-B_\kappa\otimes B_\kappa\) 在 \(\kappa>0\) 时不是正交投影。由 \(G_t=-u\cdot\nabla G+\nu\Delta G-G^2-H\)，其压力部分为
\[
 (\Sigma_{\kappa,t})_H
 =-q_\kappa^{-1}\{H-\Sigma_\kappa(\Sigma_\kappa:H)\}.
 \tag{ID.14}
\]
这一单独部分一般不迹零，不能单独套用 ID.13 中的迹零常数。令 \(\chi=K^{-*}\Phi_\kappa\)，其中 \(K^{-*}=(K^*)^{-1}\)，则
\[
 \int\Phi_\kappa\rho_t=-\alpha\int\rho\Sigma_{\kappa,t}:Q^*\chi,
 \qquad
 \left(\int\Phi_\kappa\rho_t\right)_H
 =\alpha\int\frac\rho{q_\kappa}
 \{H-\Sigma_\kappa(\Sigma_\kappa:H)\}:Q^*\chi.
 \tag{ID.15}
\]
压力重新进入权重的时间导数，没有已证符号或能量一致的小量。空间导数同样必须支付：
\[
 K\partial_j\rho=-\alpha Q(\rho\partial_j\Sigma_\kappa),\qquad
 K\Delta\rho=-\alpha Q\left(\rho\Delta\Sigma_\kappa
 +2\sum_j\partial_j\rho\,\partial_j\Sigma_\kappa\right).
 \tag{ID.16}
\]
因此 ID.6 不能直接控制 ID.12 的权重导数项。本节只定位这些项，不把其绝对值粗估的失败当成所有带符号组合都不可能的证明。

## 5. 指定中心的局部截止项

取任意光滑非负周期 \(\eta(x,t)\)，允许它支撑在指定中心附近的坐标球内，不改选中心。以 \(\eta p\) 测试 ID.4，逐时有
\[
 \int\eta\rho B_\kappa:H
 =\frac1\alpha\int\eta\rho f
 -\frac1\alpha\int\rho p A:D^2\eta
 -\frac2\alpha\int\rho(A\nabla\eta)\cdot\nabla p.
 \tag{ID.17}
\]
于是完整局部熵式是
\[
 \begin{aligned}
 \left[\int\rho\eta\Phi_\kappa\right]_a^b
 +\nu\iint\rho\eta D_\kappa
 ={}&\iint\Phi_\kappa
 \{\eta R_{\rm test}\rho+\rho R_{\rm test}\eta
 +2\nu\nabla\rho\cdot\nabla\eta\}\\
 &-\iint\eta\rho B_\kappa:G^2-\frac1\alpha\iint\eta\rho f\\
 &+\frac1\alpha\iint\rho p A:D^2\eta
 +\frac2\alpha\iint\rho(A\nabla\eta)\cdot\nabla p.
 \end{aligned}
 \tag{ID.18}
\]
只有相应端点的 \(\eta\) 为零，才能删除该端点。对任意 \(p\mapsto p+c(t)\)，新增项是 \(c(t)\alpha^{-1}\int\rho A:D^2\eta=0\)；公式压力规范不变，没有额外 \(c'(t)\)。

三个带 \(\alpha^{-1}\) 的源与边界项应作为整体处理。在形式基准 \(\alpha=0,\rho=1,A=I\) 下，\(\int p\Delta\eta=-\int\eta f\)、\(2\int\nabla\eta\cdot\nabla p=2\int\eta f\)，故分子的零阶部分共同抵消。分别取绝对值会丢失抵消；整个组合仍是原压力配对，不能据小参数认定其小。

全局 \(L^2\) 上界和非负性不提供指定小球上的统一密度正下界。因此不能把左边的加权耗散直接换成原来的无权耗散或 PF 的形状量 \(K(r)\)。本文没有交换 \(\kappa\downarrow0\)、\(\alpha\downarrow0\)、\(b\uparrow T_*\) 或 \(r\downarrow0\)；也没有证明权重乘积下原零集缺陷的极限公式。光滑固定区间上的解依赖常数不能冒充前终端统一控制。

## 6. 文献位置与实际检查范围

这类空间伴随密度属于非散度型椭圆方程的已有理论，不作为新发现。定点检索采用两条查询：`periodic elliptic nondivergence invariant measure Cordes condition invariant density positivity adjoint` 与 `periodic invariant measure nondivergence elliptic equation double divergence normalized positive density`。本地对 Cordes、不变密度、elliptic adjoint 和新源 ID 的检索未找到本候选的同题记录；这只是有界去重，不是充分查新。

[Sprekeler 2024，SIAM J. Numer. Anal.](https://epubs.siam.org/doi/10.1137/23M1580279) 的摘要描述 Cordes 条件下周期系数的唯一 \(L^2\) 不变密度；本次只读到官方 HTML 摘要和元信息，没有认证该刊本证明。[作者的 Cordes/FPK 综述，arXiv:2601.14548v1](https://arxiv.org/html/2601.14548v1) 的第 3 节给相应框架。本次实际读了第 3 节条件、近算子推导、Lemma 3.1 与 Theorem 3.1 的陈述和所印证明；Lemma 3.1 明说省略非负性证明。因此本稿的特定光滑系数构造、常数和非负性使用第 2 节自己的推导，不借未读证明补洞。访问日为 2026-09-08；该 HTML 页首的 v1 日期与内文署期不一致，按给定版本 URL 识别，不据此声称已核所有版本。

数学接口沿用 [WE 原梯度熵](clay_b_weak_gradient_entropy_20260908.md)、[AH 仿射参考](clay_b_affine_reference_pressure_20260908.md)、[VR 变参考](clay_b_variable_reference_check_20260908.md) 和 [PF 条件形状判据](clay_b_pressure_free_shape_criterion_20260908.md)。本轮主任务全文重读了 WE、AH、VR，重新推导本稿。ma_freeze_review 分别复算空间逆算子、迹零常数、压力极限、非负性；variable_reference_check 分别复算时间导数、全局熵和局部截止、压力规范。它们是参与式 AI 交叉核算，不是独立真人审稿或创新性认证；最终稿的实际读回范围另见检查点。

## 7. 结论与下一项有界问题

当前已完成：固定 \(\alpha,\kappa\) 的椭圆密度构造、非负性、统一空间 \(L^2\) 界，以及全部端点和截止项保留的加权熵恒等式。未完成：控制动态权重、局部密度退化、原耗散极限或严格尺度增益。它没有自动产生 PF 联合好尺度，也不是一个新的正则性判据。

下一项先把 ID.12 的 \(\rho_t+u\cdot\nabla\rho\) 合并为物质导数，明确 \([u\cdot\nabla,Q]\) 交换子及扩散乘积项，检查带符号组合是否比本节的分项控制更强。保留同一任意数据 NS 轨道、固定正龄、指定中心与临界尺度。只有实际取得额外动态控制才推进；若仍仅重写原压力且不能处理密度退化，就停止这一直接不变密度支路，不继续增加相邻审计计数。此问题尚未执行，不应写成已有估计。

本记录不新建 release、不重发交接、不执行发布，不修改历史源、图表档案或公开统计。
