# 分离剪切的扩散重叠：秩一梯度不构成不变类

2026-09-08。SRG，PRIVATE_CORE。范围内解析证明；一般三维 NS / Clay 仍 OPEN / NOT CLAY。未作充分查新，不宣称原创性或真人同行评审。

本节给出一族真实、光滑、无外力的周期 NS 解：初始速度梯度处处秩至多一，在一个预先固定的正时间窗上却具有严格正的秩一偏离。生成的偏离质量是一阶幅度量，初始能量和二次源是二阶幅度量。

机制首先发生在线性热扩散中：两股支撑分离、方向不同的剪切发生重叠。小幅度 NS 与该热轨道的二阶误差不会消去这一现象。这补充了 CD 仅有的点态负黏性例子，说明其有符号黏性测度在真实解上的整胞累计值也可以为负。它不是奇性构造，也不否定任何已冻结的条件正则判据。

## 1. 固定同一解族和量词

固定未归一化的三维环面 T³_(2pi)、黏性 nu>0，以及任意有限的 0<tau<T。以下空间积分都使用普通体积，不除以周期胞体积。先选一个固定的非负光滑周期函数 phi，非零且闭支撑包含于 z=0 附近的闭弧 |z|≤pi/8，令 psi(z)=phi(z−pi)。两者闭支撑严格分离。

例如可将 eta(s)=exp(−1/(1−s²))（|s|<1）、eta=0（|s|≥1）按 phi(z)=eta(8z/pi) 在 (−pi,pi) 内定义后周期延拓。固定这些函数，不令支撑或其间距随幅度参数变化。令
\[
U_0(x,y,z)=(\phi(z)\sin y,\;\psi(z)\sin x,\;0),
\qquad u_{\epsilon,0}=\epsilon U_0,\quad\epsilon>0.
\tag{SRG.1}
\]
使用 CD 的量
\[
G=\nabla u,\quad q=|G|_F,\quad
d(G)=\operatorname{dist}_F(G,\{\operatorname{rank}\le1\}),
\]
\[
f(G)=\frac{|\operatorname{cof}G|^2}{|G|^3}\quad(G\ne0),
\qquad f(0)=0,\qquad m_\epsilon(t)=\int f(\nabla u_\epsilon(t)).
\tag{SRG.2}
\]
f 是一次齐次、非负的全局 Lipschitz 函数，且
\(d^2/(2q)\le f\le d^2/q\le q\)，零点按连续延拓解释。一次齐次与球面上有界的导数给全局 Lipschitz 界；穿过原点的线段分成两段即可。没有对 f 在原点假设经典可微性。

**命题 SRG-A（本地证明）。** 存在 epsilon0>0、c>0、C<∞，依赖 nu、T、tau 和固定 U0，但不依赖 epsilon，使每个 0<epsilon≤epsilon0 的初值 SRG.1 产生 [0,T] 上唯一的光滑周期 NS 解与零均值规范压力，并满足
\[
\operatorname{rank}\nabla u_\epsilon(0,x)\le1\quad\forall x,
\qquad c\epsilon\le m_\epsilon(t)\le C\epsilon
\quad\forall t\in[\tau,T].
\tag{SRG.3}
\]
在一个固定正体积空间集合上，梯度于整个 [tau,T] 都有非零二阶子式。因此这是同一条解在整个固定时间窗上的结论，不是逐时更换初值。epsilon0 可以随 tau→0 变小；不声称一个固定 epsilon 自动覆盖所有任意小的正时间。

## 2. 起点处真正为秩一，而非小偏离

U0 无散、光滑、周期、均值零。梯度为
\[
\nabla U_0=
\begin{pmatrix}
0&\phi\cos y&\phi'\sin y\\
\psi\cos x&0&\psi'\sin x\\
0&0&0
\end{pmatrix}.
\tag{SRG.4}
\]
导数的支撑也包含于各自闭支撑。每个 z 至多有一行非零，所以其秩处处至多一，包括边界和零梯度处。初始 m_epsilon=0、d=0。

同时
\[
(U_0\cdot\nabla)U_0
=(\phi\psi\sin x\cos y,\;\phi\psi\sin y\cos x,\;0)=0.
\tag{SRG.5}
\]
规范初压满足 −Delta p=tr((grad u0)²)=0，故 p_epsilon(0)=0。这个起点事实不意味着后续压力或非线性仍为零，也不把初始秩一类预设为不变。

## 3. 热扩散产生非零二阶子式

记 Phi_t=exp(nu t partial_zz)phi、Psi_t=exp(nu t partial_zz)psi。周期一维热核可写成正高斯的周期和
\[
K_{\nu t}(z)=\frac1{\sqrt{4\pi\nu t}}
\sum_{n\in\mathbb Z}\exp\left[-\frac{(z+2\pi n)^2}{4\nu t}\right]>0.
\tag{SRG.6}
\]
在 t>0 的紧时间窗上该级数及所需空间导数一致收敛；积分为一。与非负非零初值卷积，得到每个 t>0、每个 z 上 Phi_t、Psi_t 严格为正。

线性热轨道为
\[
U(t)=e^{\nu t\Delta}U_0
=e^{-\nu t}(\Phi_t(z)\sin y,\;\Psi_t(z)\sin x,\;0).
\tag{SRG.7}
\]
其 x,y 主二阶子式是
\[
J_{12}(\nabla U(t))
=-e^{-2\nu t}\Phi_t(z)\Psi_t(z)\cos x\cos y.
\tag{SRG.8}
\]
热轨道不是本节的精确 NS 解；这里只把它作为线性首项。固定
\(D=\{|x|\le\pi/6,\ |y|\le\pi/6\}\times\mathbb T_z\)。
由紧致性，存在 j_*>0 使
\[
J_{12}(\nabla U(t,x))\le-j_*
\quad\text{于 }[\tau,T]\times D.
\tag{SRG.9}
\]
其余位置除 cos x cos y=0 的零测平面外，热梯度也有非零该子式。这不是对真实 NS 解宣称全空间几乎处处秩二；后者只需下面的固定 D。

初始各个有符号二阶子式的空间积分为零，后续也符合梯度的零拉格朗日积分约束。例如 SRG.8 的整胞积分因 cos x cos y 为零而消失。子式的绝对值或其平方商可以正，不与 Piola 恒等式矛盾。

## 4. 固定时间窗上的真实 NS 误差

采用标准周期 Leray 投影 P，取整数 m=5，令 X=C([0,T];H^m)，限制为无散、均值零场。周期 Fourier 乘子直接给
\[
\|e^{\nu(t-s)\Delta}P\operatorname{div}F\|_{H^m}
\le C[\nu(t-s)]^{-1/2}\|F\|_{H^m},\qquad s<t.
\tag{SRG.10}
\]
H^m 是乘法代数。因而双线性 Duhamel 算子
\[
\mathcal B(v,w)(t)
=-\int_0^t e^{\nu(t-s)\Delta}P\operatorname{div}(v\otimes w)(s)\,ds
\]
满足
\[
\|\mathcal B(v,w)\|_X
\le K_T\|v\|_X\|w\|_X,\qquad K_T=C_m\sqrt{T/\nu}.
\tag{SRG.11}
\]
积分奇性为可积的 (t−s)^−1/2；强时间连续性由截去积分末端再用该一致界恢复。令 A0=||U0||_Hm，先选 epsilon0 使 4K_T epsilon0 A0≤1/2，并取 0<epsilon≤epsilon0。映射
\(v\mapsto\epsilon U+\mathcal B(v,v)\)
在半径 2epsilon A0 的闭球上映入自身并严格压缩，产生同一无外力 NS 的 mild 解。因此
\[
\|u_\epsilon\|_X\le2\epsilon A_0,\qquad
\|u_\epsilon-\epsilon U\|_X\le4K_TA_0^2\epsilon^2.
\tag{SRG.12}
\]
H5 嵌入 C1，故该误差也在 C([0,T];C1) 为 O_T(epsilon²)。所有常数保留 nu、T 和固定初值形状的依赖，不在 t→0 或无限时间上偷换成统一常数。

上述是高阶小幅度估计的直接证明。光滑数据的唯一性、光滑保持和规范压力采用经典周期局部理论；本轮定向核读 [Tao，arXiv:1108.1165v4，Theorem 5.1 及完整证明](https://arxiv.org/html/1108.1165v4#S5)。结合已有 H5 mild 界，局部光滑解可用唯一性拼接覆盖 [0,T]；高阶正则性由其标准平滑保持结论给出，不假设任意大初值全局存在。固定周期与黏性只改变常数。

对零均值压力，周期 Poisson 方程还给
\[
\|\nabla^2p_\epsilon(t)\|_{H^{m-1}}
\le C\|\nabla u_\epsilon(t)\|_{H^{m-1}}^2
\le C_T\epsilon^2.
\tag{SRG.13}
\]
这里 H^(m−1) 是代数，且二阶 Riesz 在此 Hilbert 空间有界；没有对任意 L1 源使用 Riesz 有界性。特别地，整个 [0,T] 上的 q² 和 |H| 积分都是 O_T(epsilon²)。

## 5. 非线性解确实离开秩一类

由 SRG.12，令 G_epsilon=epsilon grad U+E_epsilon，||E_epsilon||_C0≤C_T epsilon²。二阶子式的二次多项式结构给
\[
J_{12}(G_\epsilon)
=\epsilon^2J_{12}(\nabla U)+O_T(\epsilon^3),
\qquad |G_\epsilon|\le C_T\epsilon.
\tag{SRG.14}
\]
在 SRG.9 的固定时空集合上，将 epsilon0 再缩小一次，有
\[
|J_{12}(G_\epsilon)|\ge\tfrac12j_*\epsilon^2,
\qquad f(G_\epsilon)\ge
\frac{|J_{12}(G_\epsilon)|^2}{|G_\epsilon|^3}
\ge c_*\epsilon.
\tag{SRG.15}
\]
该处梯度非零，分母合法。积分给 SRG.3 下界；f≤q 和 SRG.12 给上界。初始秩至多一与这一后续秩至少二区域属于同一条光滑解，故类 {u:rank grad u≤1处处} 不是周期 NS 的不变类。没有证明真实解后续的第三分量或 det G 恒零，故不宣称该处梯度恰为秩二。

还可由 f 的全局 Lipschitz 和一次齐次性得到更精确的均匀展开
\[
m_\epsilon(t)=\epsilon m_H(t)+O_T(\epsilon^2),
\qquad m_H(t)=\int f(\nabla U(t)),\quad0\le t\le T,
\tag{SRG.16}
\]
其中 m_H(0)=0，t>0 时 m_H(t)>0。固定 [tau,T] 上的下界不依赖于时刻；因此时间积分也有一阶下界。这里只取有限幅度族在同一固定窗口的渐近，不把它冒充一条解的奇异终端渐近。

## 6. 整胞黏性累计可以为负

CD.10–11 的 f 分布方程，对每条上述真实 NS 解成立：
\[
Lf=-Df_0(G):(G^2+H)-\nu\mu_f,
\qquad L=\partial_t+u\cdot\nabla-\nu\Delta.
\tag{SRG.17}
\]
mu_f 为有符号测度，包含 q=0 的余项；Df0 在原点按同一正则化取零。不能先删除零集项再讨论其符号。Df0 全局有界，所以 SRG.12–13 给
\[
\left|\int_0^t\int Df_0(G_\epsilon):(G_\epsilon^2+H_\epsilon)\right|
\le C_T\epsilon^2,\qquad 0\le t\le T.
\tag{SRG.18}
\]
周期积分消去输运和 Laplacian，两个时间片保留，起点 f=0。于是
\[
\nu\mu_{f,\epsilon}(\mathbb T^3\times(0,t))
=-m_\epsilon(t)
-\int_0^t\int Df_0(G_\epsilon):(G_\epsilon^2+H_\epsilon)
\le-c\epsilon+C_T\epsilon^2<0
\tag{SRG.19}
\]
对整个 [tau,T] 的 t 同时成立，最后再次缩小 epsilon0。固定光滑区间上的测度无时间端点原子，按 CD 的正则化逐时上界解释 (0,t)。

这从完整原解证明了整胞累计负性，不只是 CD.14 的某一点负密度，也不是将热轨道当 NS 解。它不意味着能量耗散为负：这里的 mu_f 是非凸缺陷函数的链式黏性测度，GD 的原梯度模长熵耗散和 NS 动能耗散仍非负。已有 GD 预算含一阶的初始 integral q，能容纳这种转移。

## 7. 排除的估计与仍开放的问题

在该族共同有界的光滑初值和解范数范围内，不存在与 epsilon 无关的有限 C，使例如
\[
m_\epsilon(t)+\mathcal D_\epsilon(0,t)
\le C\left[m_\epsilon(0)+\|u_{\epsilon,0}\|_2^2
+\int_0^t\int(|G_\epsilon|^2+|H_\epsilon|)\right],
\qquad\mathcal D_\epsilon\ge0
\tag{SRG.20}
\]
对所有 epsilon 和 t∈[tau,T] 成立。右侧 O(epsilon²)，左侧至少 c epsilon。允许 C 依赖固定 nu、T、tau、U0 和共同上界仍有矛盾；不允许 C 暗中按 epsilon 发散。右侧改成更小的 integral d² 也不能修复此估计。

这个反检不排除加入初始 integral|G|、独立扩散生成项、带符号抵消或其他线性成本的估计；也不排除真正全时间的小形状判据。SRG.3 不说明这些解接近奇性，它们在所论固定窗口内都是小而光滑的。PF 不要求秩一梯度类不变，故本节不推翻 PF。生成二阶子式也不自动给正涡伸长或 enstrophy 净增长。

下一步不再为纯秩一偏离量假定自主非负扩散耗散。一个另行提出、尚未证明的具体压力目标是整胞联合配对 |integral B0:(G²+H)|≤C||G||2||d(G)||2；它允许一阶偏离，而不是被 LK/NE 排除的纯 d² 源。其空间补偿与局部截止成本必须独立检验，不能把本节视为支持该不等式成立的证据。

## 8. 来源、去重与交付范围

主任务本轮全文读取 CD、LK、PGR；此前连续研究中已全文读取 GD/WE/PF/NE/MA/VR，本轮不宣称重新认证全部旧依赖。本节 f 的测度方程继承 CD 的原正则化，不修改旧冻结。按“分离剪切／支撑重叠／秩一不变性”等词检索本地稿件，发现旧 CD 明确保留不变性问题；另定点核对 R0.73A §6，其秩一条目是 Orr–Sommerfeld 状态投影，不是完整速度梯度的秩约束。未发现此构造的本地完成稿不等于绝对原创性。

外部只使用上述经典周期局部理论。两项有界普通查询围绕 NS 速度梯度秩一与热流秩一，未据其结果认领新颖性或采用新定理；不是全面 Deep Research。热核正性、子式、幅度误差和零集处理均在正文给出，有限计算不代替它们。具体独立 AI 审查范围与版本另记。

无 PDE 仿真、DGX、科学附图、新读者 PDF、翻译或网站编辑；科学图清单为空。达到研究冻结条件后，只向固定发布任务移交一次 PRIVATE_ARCHIVE，不请求公开发布，不等待或监控归档结果。
