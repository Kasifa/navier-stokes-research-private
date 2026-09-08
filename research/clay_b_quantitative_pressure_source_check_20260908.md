# PF 定量化预检：压力源范数不能随意加强

2026-09-08。QPS，PRIVATE_CORE。内部路线检查，不是新的独立研究小节。局部反检已证明，主问题仍 OPEN / NOT CLAY；没有充分查新或真人同行评审。

这一轮检查一条具体设想：能否把 PF 中极限压力源的受控性质，提前写成原速度的定量强范数估计。答案必须分开说。只给切片速度能量和小形状导数，连减去任意调和函数后的压力源强范数也可以发散。即使补上真实 NS 和整柱能量界，整个母柱的压力源 L2 仍可在底部薄层发散。但这些例子的压力梯度很小，并不否定 PF，也不排除内柱或候选终端的压力控制。

因此停止这一强压力源加强，不把底部薄层继续发展成另一族参数研究。下面保存完整反检和指数，避免以后混淆压力、压力梯度与压力源。没有得到指定中心的联合好尺度或新的跨尺度增益。

## 1. 检查的量词

沿用 PF 的完整梯度 \(G_{ij}=\partial_j u_i\)，以及
\[
 d(G)=\operatorname{dist}_F(G,\{\operatorname{rank}\le1\}),\qquad
 \Theta(G)=d(G)G/|G|^{3/2},\qquad f=\operatorname{tr}(G^2).
 \tag{QPS.1}
\]
零梯度处 Theta 取0，导数在整个空间弱意义下理解。周期胞为 \(\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3\)；球均位于其一个坐标图。以下 \(p\) 是同一速度的均值零规范压力，满足 \(-\Delta p=f\)。静态切片不自行满足时间方程。

固定任意 \(M>0\) 和 \(1\le q\le\infty\)。第一条被检验的估计是：对于所有光滑无散速度，若 \(\|u\|_{L^2(B_1)}\le M\)，则
\[
 \inf_{\Delta h=0\ {\rm in}\ B_1}
 \|f-h\|_{L^q(B_{1/2})}
 \le\omega_M(\|\nabla\Theta\|_{L^2(B_1)}^2),
 \tag{QPS.2}
\]
其中 omega 在0附近有界，更强的版本要求它趋于0。没有预设切片梯度 L2 上界，也不限制调和校正 h 的大小。QPS.2 对每一个 q 都不成立。

## 2. 一个振荡切片同时排除所有强空间指数

固定足够小的 \(A>0\)，使下述所有速度满足 M 上界。对整数 \(n\ge1\)、\(0<\varepsilon\le1/2\)，取
\[
 u_{n,\varepsilon}=A(\sin ny,\varepsilon\sin nx,\cos ny),\qquad
 G_{n,\varepsilon}=An
 \begin{pmatrix}0&\cos ny&0\\\varepsilon\cos nx&0&0\\0&-\sin ny&0\end{pmatrix}
 =:AnK_{n,\varepsilon}.
 \tag{QPS.3}
\]
它光滑、无散、周期且均值零。两非零列正交，奇异值为 \(An,An\varepsilon|\cos nx|,0\)，因此
\[
 |G|=An(1+\varepsilon^2\cos^2nx)^{1/2},\quad
 d=An\varepsilon|\cos nx|,\quad
 \Theta=\sqrt{An}\frac{\varepsilon|\cos nx|K_{n,\varepsilon}}
 {(1+\varepsilon^2\cos^2nx)^{3/4}}.
 \tag{QPS.4}
\]
梯度模从不为零。绝对值余弦是 Lipschitz 函数，故完整弱一阶导数合法；逐项微分给
\[
 \|\nabla\Theta\|_{L^2(\mathbb T^3)}^2\le CA n^3\varepsilon^2,
 \qquad f=2A^2n^2\varepsilon\cos nx\cos ny.
 \tag{QPS.5}
\]
常数与 n、epsilon 无关。对整数 n≥2 取 \(\varepsilon_n=n^{-7/4}\)，则左边至多 \(CA n^{-1/2}\to0\)，但 f 的振幅为 \(2A^2n^{1/4}\to\infty\)。

任意局部调和项也不能消掉这个发散。取固定非零非负 \(\chi\in C_c^\infty(B_{1/2})\)，记 \(c_n=\cos nx\cos ny\)、\(\phi_n=\chi c_n\)。对分布调和 h，有 \(\langle h,\Delta\phi_n\rangle=0\)。利用 \(\Delta c_n=-2n^2c_n\)，两次分部积分精确给
\[
 \int(f-h)\Delta\phi_n=-4A^2n^4\varepsilon_n\int\chi c_n^2,
 \qquad\|\Delta\phi_n\|_{q'}\le C_{\chi,q}n^2.
 \tag{QPS.6}
\]
由余弦平方展开及固定光滑截止的振荡积分，最后积分趋于 \(\tfrac14\int\chi>0\)。Holder 不等式遂给 QPS.2 左边至少 \(c_{\chi,q}A^2n^{1/4}\)。端点 q=1 用 q'=无穷，q=无穷用 q'=1。若余项不在所需空间，左边就是无穷，仍不影响否定。

这个序列的切片梯度 L2 约为 An，没有共同上界。它不属于 PF 切片分类中已选出的梯度有界子列；若直接把它保持成恒定时间场，整柱 E 也会越界，而且那个场不是 NS 解。

## 3. 压力源大不等于压力在方程中的作用大

QPS.3 的规范压力恰为
\[
 p_{n,\varepsilon}=A^2\varepsilon\cos nx\cos ny,\qquad
 \|\nabla p_{n,\varepsilon}\|_2\asymp A^2n\varepsilon.
 \tag{QPS.7}
\]
当 epsilon=n^(-7/4) 时，压力梯度趋于0，压力本身也趋于0。发散的是源和 Hessian 的强范数。该例不排除负阶源控制，也不排除 PF.10 中带有线性梯度项的控制；事实上 \(|f|/|G|\le2An\varepsilon_n\to0\)。不能把不同导数阶次都称作同一种压力障碍。

## 4. 真实整柱反检只发生在底部薄层

为准确判断“补上整柱 A+E 后是否足够”，下面只作一次范围核对。固定 \(\nu>0\)、整数 \(m\ge5\)，在同一标准周期胞上解
\[
 U_\tau-\nu\Delta U+a(U\cdot\nabla)U+\nabla P=0,\quad
 \operatorname{div}U=0,\quad
 U(0)=(\sin y,\varepsilon\sin x,\cos y),\qquad a=A/n.
 \tag{QPS.8}
\]
这里 P 是含系数 a 的方程压力；以下定义 \(\pi=P/a\)，所以 \(-\Delta\pi=\operatorname{tr}((\nabla U)^2)\)。不把 P 与 pi 混用。基准 \(B=e^{-\nu\tau}(\sin y,0,\cos y)\) 是精确解，因为它的对流为零。

所需全时小扰动可直接证明。均值零 Fourier 模上的热算子满足
\[
 \|e^{\nu s\Delta}\mathbb P\operatorname{div}F\|_{H^m}
 \le C(1+(\nu s)^{-1/2})e^{-\nu s}\|F\|_{H^m},\qquad s>0.
 \tag{QPS.9}
\]
证明只需 \(|k|e^{-\nu s|k|^2}\le C(1+(\nu s)^{-1/2})e^{-\nu s}\) 对所有非零整数模成立；Leray 矩阵的算子范数至多1。零模被 div 消去，不要求 F 本身均值零。

写 W=U−B，其温和方程的非线性张量为 \(a(B\otimes W+W\otimes B+W\otimes W)\)，初值为 \(\varepsilon V\)、\(V=(0,\sin x,0)\)。Hm 是乘积代数，且
\[
 \sup_{\tau\ge0}\int_0^\tau
 (1+(\nu(\tau-s))^{-1/2})e^{-\nu s}\,ds<\infty.
 \tag{QPS.10}
\]
积分在有界 tau 上由可积平方根核控制；大 tau 时分为 s≤tau/2 和 s≥tau/2，分别用核的有界性与指数小因子控制。因此在范数 \(\sup_\tau e^{\nu\tau}\|W(\tau)\|_{H^m}\) 的半径 C epsilon 球内，只要固定 a 足够小，Duhamel 映射保持该球并收缩。取 epsilon 也小于固定常数，得到唯一全时温和解，光滑初值及同一方程的局部平滑化使它为经典解。所有常数可依赖 nu、m、周期胞，不依赖 n、epsilon、tau。由同一估计再减去线性项，得
\[
 \|U-B\|_{H^m}\le C\varepsilon e^{-\nu\tau},\qquad
 \|U-B-\varepsilon e^{-\nu\tau}V\|_{H^m}
 \le Ca\varepsilon e^{-\nu\tau}.
 \tag{QPS.11}
\]
不可把右侧改为较慢的任意指数再直接归一化。这里与基准相同的衰减率保证 \(|\nabla U|\ge\tfrac12e^{-\nu\tau}\) 全时成立。

具体地，令 \(D=e^{\nu\tau}\nabla U\)、\(D_0=e^{\nu\tau}\nabla B\)。Hm 嵌入 C2 给 \(\|D-D_0\|_{C^1}\le C\varepsilon\)，而 D0 始终是模长1的秩一矩阵。该紧集的一个固定邻域中，第一奇异值与其余奇异值分离，最佳秩一投影 \(R_1(D)=D P_1(D^TD)\) 光滑，P1 是简单最大特征值的谱投影。故 \(N(D)=D-R_1(D)\) 的 C1 范数至多 C epsilon，因为 N(D0)恒为0。距离 d(D)=|N(D)| 的弱导数由 N 的导数控制，包括 d=0 处。Theta 的半次齐次性随即给
\[
 |\nabla\Theta(\nabla U)|\le C\varepsilon e^{-\nu\tau/2},\qquad
 \int_0^\infty\|\nabla\Theta(\nabla U)\|_2^2d\tau\le C\varepsilon^2.
 \tag{QPS.12}
\]
没有遗漏长时梯度趋零带来的归一化问题。

QPS.11 还给同一实际解的源展开
\[
 f_U=2\varepsilon e^{-2\nu\tau}\cos x\cos y
       +O_{L^\infty}(a\varepsilon e^{-2\nu\tau}).
 \tag{QPS.13}
\]
线性梯度的平方中自项均为零，交叉项是所列主项；其余项由 QPS.11 和基准梯度界控制。取 a 的固定上界更小，主项在 tau∈[1,2] 有一致 L2 下界。均值零规范 pi 的 Fourier 解同时给 \(\|\nabla\pi\|_2\le C\|f_U\|_2\le C\varepsilon e^{-2\nu\tau}\)。

现在对充分大的整数 n 取 \(\varepsilon_n=n^{-3/4}\)，使 a、epsilon 满足上述固定小量条件，从 \(t_{n,*}=-1-n^{-2}\) 启动真实物理解
\[
 u_n(x,t)=A U_n(nx,n^2(t-t_{n,*})),\qquad
 p_n(x,t)=A^2\pi_n(nx,n^2(t-t_{n,*})).
 \tag{QPS.14}
\]
代入方程可逐项核对：时间及黏性项系数 An²，对流系数 A²n，压力梯度系数 A²n，恰对应 a=A/n。无需反向求解。每个解定义在闭 Q1 的一个邻域。

整数周期覆盖保持整胞积分。由 QPS.11–12，单位母柱及整胞全时界给
\[
 \mathsf A(1)+\mathsf E(1)\le C_\nu A^2,\qquad
 \mathsf K(1)\le C_\nu A n\varepsilon_n^2
               =C_\nu A n^{-1/2}\to0.
 \tag{QPS.15}
\]
这里 A、E、K 用 PF 的定义，只将方程黏性允许为固定 nu；取 nu=1 即原 PF 合同。Theta 空间导数的物理缩放因子是 \(\sqrt A n^{3/2}\)，时间积分因子是 n^(-2)。梯度能量积分相应为 A²。A 可固定选得足够小以满足任意给定正的共同能量上界。

但 Q1 底部 \(t\in[-1,-1+n^{-2}]\) 对应 tau∈[1,2]。固定球中 \(\int\cos^2(nx)\cos^2(ny)\to|B_1|/4\)，QPS.13 的一致误差不能消去主项，所以
\[
 \|\operatorname{tr}((\nabla u_n)^2)\|_{L^2(Q_1)}
 \ge c_\nu A^2 n\varepsilon_n=c_\nu A^2n^{1/4}\to\infty,
 \quad
 \int_{t_{n,*}}^\infty\|\nabla p_n(t)\|_2^2dt
 \le C_\nu A^4\varepsilon_n^2\to0.
 \tag{QPS.16}
\]
这只否定整个母柱上的相应统一强 L2 源加强。离底部任何固定正时间后，梯度和源分别受 \(CAn e^{-\nu n^2\sigma}\)、\(CA^2n^2\varepsilon_n e^{-2\nu n^2\sigma}\) 控制并趋零。它不是固定内柱、候选奇异终端或同一初值跨尺度反例。所有解本来就正则；PF 的结论与此完全相容。

## 5. 为什么不能用另一个范数名称掩盖缺口

PF.11–12 只证明修正极限的压力源属于 L2，不给原序列源的强收敛或统一 L2 范数。梯度子式在分布中传递；强速度 L3 只直接控制速度平方及压力振幅，不能任意加两次空间导数。

RS 真正使用的是消去调和压力后，方程的力属于时空 L2。对固定空间截止 chi，源的 L2 是 \(\nabla(-\Delta)^{-1}(\chi f)\in L^2\) 的充分条件，不是必要条件。QPS.7、16 已说明强源发散与压力梯度小可以同时发生。源的负一阶空间拓扑更弱，但仍不能视为基本能量自动给出的输入：若能对任意有限 A、E、K 的一般适当解在内柱直到顶端证明这种力的有限 L2 界，结合每个解有限压力的调和积分和 RS 小幂步骤，就会得到实质性的正则性结论。这项估计未证明。若它只在 K 足够小或小 K 极限成立，仍主要是 PF 的定量化，并未生成一般终端的小 K 尺度。

时间指数也必须保留。设 \(k(t)=\|\nabla\Theta(t)\|_2\)、\(g(t)=\|G(t)\|_2\)。若某个空间 L^(3/2) 余项估计形如 \(C(M)k(t)^\alpha g(t)^b\)，其中 alpha、b≥0 且 alpha+b>0，仅由 k、g∈L²_t 得到的时间指数为 \(2/(\alpha+b)\)。把它经局部椭圆估计转成空间 L3 的压力梯度后，要直接进入现有 L2 力链，需要 alpha+b≤1；二次率只给时间 L1。指数小于1时只能理解为积分幂控制，不能称 Banach 范数估计。

两尺度正性也没有因此改善。对嵌套非负截止，改用 \(\psi=\phi_r-\phi_{\theta r}\ge0\)，确可得到正的熵测度配对，但
\[
 r^{-1}\int\psi\,d\mu_G
 =r^{-1}\int\phi_r\,d\mu_G
   -\theta\,(\theta r)^{-1}\int\phi_{\theta r}\,d\mu_G.
 \tag{QPS.17}
\]
它只保留 theta 倍的内尺度量，正性单独对应 theta^(-1) 的损失，不是严格收缩。AP 原式的两端切片、输运、截止和带符号压力配对都仍在；不能因共同采用 r^(-1) 而把旧差分当作新机制。

## 6. 决定与实际范围

本轮否定的是明确的强源加强，既未否定全部定量 PF 论证，也未否定压力梯度／负阶源的可能控制。旋转横向剪切种子早已出现在旧 R0.70S；本稿不认领种子新颖。定向本地去重由协作者核读该稿相关完整节与 NE 相关节，未做充分文献新颖性检索。

下一步仍须从同一实际 NS 解产生联合 A+E 上界和小 K 尺度。只有真正改进带符号压力—输运估计，给出不同于 AP 原差分、共同伴随、q×d、Young 平方商或变参考核算的明确机制，并得到严格尺度增益或独立不可求和成本，才可接受为一般正则性输入。当前没有选定这样的新命题（NO-CANDIDATE）。不把未证的压力梯度 L2、K 小量、共同速度 L∞ 或初端平移模量放进假设后宣称得到自动输入。

本稿由主任务与 AI 协作者共同推导和审读，具体实际版本另记。没有仿真、DGX、数值证书、科学附图、英文翻译、读者 HTML/PDF、公开摘要或阶段 recap。它作为一次内部路线预检本地保存，不另计完成小节、不建新 release、不重复移交此前冻结包，不检查发布或反向执行。
