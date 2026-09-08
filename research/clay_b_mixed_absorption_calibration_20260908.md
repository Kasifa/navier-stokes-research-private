# 混合吸收的系数限制与退化余项

2026-09-08。MA，PRIVATE_CORE。范围内解析结论；一般三维 NS / Clay 仍 OPEN / NOT CLAY。未作新颖性认证或真人同行评审。

原梯度耗散加入后，NE 解族仍要求混合估计的系数随背景幅度增长。这不排除依赖固定临界预算的系数。另一项检查更直接：把压力与输运合并，再用 Young 不等式，会出现加速度平方除以梯度模长的非负余项。这个余项在光滑周期 NS 的一个初始时间窗上可以不可积，即使允许减去任意时间依赖的空间常向量。发散的是这个上界，不是解或原来的带符号配对。

## 1. 将真实原耗散算入 NE 解族

固定未归一化的三维周期胞 T³_(2pi)、黏性 nu>0。记 G_ij=partial_j u_i，q=|G|，B_0=G/q 于 q>0、在 q=0 取零，d(G) 为到秩至多一矩阵集的 Frobenius 距离。定义瞬时量
\[
 P(u)=-\int B_0:(G^2+\nabla^2p),\quad
 Q(u)=\int d(G)^2,\quad
 \mathscr D(u)=\lim_{\kappa\downarrow0}\int\Gamma_\kappa,
 \quad\Gamma_\kappa=\sum_j\left(
 \frac{|\partial_jG|^2}{q_\kappa}
 -\frac{(G:\partial_jG)^2}{q_\kappa^3}\right),\quad
 q_\kappa=\sqrt{q^2+\kappa^2}.
 \tag{MA.1}
\]
对光滑周期 G，分部积分及支配收敛给
\[
 0\le\mathscr D=-\int B_0:\Delta G\le\|\Delta G\|_1.
 \tag{MA.2}
\]
这是包含正则化零集贡献的完整空间耗散，不以非零处的密度替代它。P 是范数方程的联合生产，不是范数净增长。

NE.11 的 U_0、v_0、K、p_v 保持不变；此处显写为
\[
 U_0=\sin y+\sin2z,\quad v_0=(-2\cos y\sin2z,\sin y\cos2z),
 \quad p_v=-\cos2y-\tfrac14\cos4z.
\]
取初值 u_(A,b)=(A U_0,b v_0)，A,b>0。这里 A 是轴向幅度，不是局部能量记号 mathsf A。令 X=cos²y，Y=cos²2z，L=8-8X-8Y+25XY=|K|²。由 NE 的压力和奇偶计算、Delta K=-5K，得到
\[
 q_{A,b}=\sqrt{A^2(X+4Y)+b^2L}>0,\qquad
 P_{A,b}=6A^2b\int\frac{XY}{q_{A,b}},\qquad
 \mathscr D_{A,b}=\int\frac{A^2(X+16Y)+5b^2L}{q_{A,b}},
 \tag{MA.3}
\]
\[
 Q_{A,b}\le50\pi^3b^2,\qquad
 M_{A,b}:=\|u_{A,b}\|_2^2=8\pi^3A^2+10\pi^3b^2.
 \tag{MA.4}
\]
严格正性可直接检查：X+4Y=0 时 X=Y=0，但 L=8。耗散分子中的16来自轴向 sin2z 的二次空间导数，不是4。初值无散、光滑、均值零；NE 的横向热倍数与轴向线性输运扩散构造亦适用于每个固定 b,A。以下反检只使用初始切片。

令 q_0=sqrt(X+4Y)，并在其零点将下面的零分子商定义为零：
\[
 \kappa_0=6\int\frac{XY}{q_0}>0,\qquad
 D_0=\int\frac{X+16Y}{q_0}>0.
 \tag{MA.5}
\]
固定 b，A 趋于无穷时 P_(A,b)/A→b kappa_0，mathscr D_(A,b)/A→D_0。证明：写 sigma=b/A，q_sigma=sqrt(q_0²+sigma²L)，分别用 XY/q_sigma<=XY/q_0、(X+16Y)/q_sigma<=4q_0，以及 5sigma²L/q_sigma<=5sigma sqrt L。后三者可积且最后一项积分趋零；没有假设 1/q_0 可积。

若 delta>0 且非负系数 C_delta(M) 满足这个全族的瞬时混合估计
\[
 P_{A,b}\le\delta\nu\mathscr D_{A,b}
                   +C_\delta(M_{A,b})Q_{A,b},
 \tag{MA.6}
\]
取 b_*=2delta nu D_0/kappa_0，则
\[
 \boxed{\liminf_{A\to\infty}
 \frac{C_\delta(M_{A,b_*})}{A}
 \ge\frac{\kappa_0^2}{200\pi^3\delta\nu D_0}>0.}
 \tag{MA.7}
\]
确实，左侧待吸收差除以 A 趋于 delta nu D_0，而 Q<=50pi³b_*²。这个必要下界不声称最优或充分。它排除幅度无关的统一有限系数；沿所选序列 M 趋于无穷，所以不否定固定母柱 mathsf A+mathsf E+mathsf D<=M 下的 C_delta(M)。

整数频率也须区分。对 u_k(x)=u_(A,b)(kx)，k 为正整数，周期复制给
\[
 P(u_k)=k^2P(u),\quad\mathscr D(u_k)=k^3\mathscr D(u),
 \quad Q(u_k)=k^2Q(u),\quad\|u_k\|_2^2=\|u\|_2^2.
 \tag{MA.8}
\]
所以固定幅度提高频率更有利于耗散，MA.7 的校准相当于 nu 换成 nu k。完整 NS 缩放 k u(k²t,kx) 则令三个瞬时量同乘 k⁴，固定周期胞的速度 L2 平方乘 k²。这里不能套用全空间单份拷贝的体积缩放。

## 2. 压力与输运合并后的准确恒等式

令 a=(u·grad)u+grad p，称为非线性投影加速度；它不是完整的物质加速度。对同一光滑无外力 NS，有
\[
 \partial_tu-\nu\Delta u=-a,\qquad
 N:=G^2+\nabla^2p=\nabla a-u\cdot\nabla G.
 \tag{MA.9}
\]
取空间紧支或周期光滑测试 phi>=0，定义于闭光滑时间段 [t_0,t_1]，F_kappa=q_kappa-kappa。直接从第一式微分并作凸链式法则，得
\[
 \left[\int F_\kappa\phi\right]_{t_0}^{t_1}
 +\nu\int_{t_0}^{t_1}\!\!\int\phi\Gamma_\kappa
 =\int_{t_0}^{t_1}\!\!\int F_\kappa(\phi_t+\nu\Delta\phi)
 +\int_{t_0}^{t_1}\!\!\int a_i\partial_j(\phi B_{\kappa,ij}),
 \quad B_\kappa=G/q_\kappa.
 \tag{MA.10}
\]
若从带输运的 NE 方程出发，使用第二式中的 u·grad G，得到的 -integral q_kappa u·grad phi 恰与原输运项相消。空间常数 kappa 不留下余项，因为 div u=0。两个端点仍保留，截止项也没有消失。MA.10 是原方程的等价分部积分，不是新的先验控制。

固定光滑区间上，kappa→0 的右侧最后项按分布解释为 -integral phi B_0:grad a，不假设 B_0 跨零集具有经典导数。左侧保留 GD 原耗散测度，包括零集缺陷。所有其他项由光滑性及有界收敛取极限。

任意空间常向量 c(t) 可从 a 中相减，因为 integral partial_j(phi B_kappa,ij)=0；这一步没有 c'(t)。逐点有 q_kappa|grad B_kappa|²<=Gamma_kappa，故
\[
 \left|\int(a-c)_i\partial_j(\phi B_{\kappa,ij})\right|
 \le\delta\nu\int\phi\Gamma_\kappa
 +\frac{3}{4\delta\nu}\int\phi\frac{|a-c|^2}{q_\kappa}
 +\int|a-c||\nabla\phi|.
 \tag{MA.11}
\]
证明第一不等式可逐方向展开：Gamma_kappa-q_kappa|grad B_kappa|²=kappa² sum_j(G:partial_jG)²/q_kappa⁵>=0；再用 |div B_kappa|²<=3|grad B_kappa|² 和 Young。它没有给右侧加权平方项的估计。将 a 写成 Leray 投影或 -u_t+nu Delta u，也不自动控制这个退化权；以 MA.10 本身估计它会循环使用待证结论。

## 3. 两个二阶梯度零点排除常向量修补

取明确的光滑周期无散均值零初值
\[
 u^0(x,y,z)=(f(y),g(x),0),\quad
 f(y)=\sin y-\tfrac13\sin3y,\quad
 g(x)=\sin x-\tfrac12\sin2x-\cos x+\tfrac14\cos2x.
 \tag{MA.12}
\]
记 h=f'=cos y-cos3y，k=g'=cos x-cos2x+sin x-sin2x/2。G 仅有 G_12=h、G_21=k，故 -Delta p=2h(y)k(x)。其规范零均值压力可写为
\[
 p=2\sum_{m\in\{1,3\}}e_m\cos(my)
 \left\{\sum_{n\in\{1,2\}}\frac{a_n\cos(nx)}{n^2+m^2}
       +\sum_{n\in\{1,2\}}\frac{b_n\sin(nx)}{n^2+m^2}\right\},
 \quad(e_1,e_3)=(1,-1),\ (a_1,a_2)=(1,-1),\ (b_1,b_2)=(1,-1/2).
 \tag{MA.13}
\]
在两条 z 平行零线上 z_+=(0,0,z)、z_-=(0,pi,z)，G=0，所以对 a^0=(u^0·grad)u^0+grad p，
\[
 a^0(z_\pm)=\pm\tfrac{36}{65}e_1.
 \tag{MA.14}
\]
其中 p_x(0,0)=2[(1/2-1/10)-(1/5-1/13)]=36/65，p_y 两处为零。Taylor 展开给 h(y)=4y²+O(y⁴)，h(pi+s)=-4s²+O(s⁴)，k(x)=3x²/2+x³/2+O(x⁴)。因此在各零线邻域 q 与 x²+dist(y,{0,pi})² 双边可比。

对任意空间常向量 c，至少一条零线的 a^0-c 非零。在其充分小邻域，integral |a^0-c|²/q 具有 integral_0^r dr/r 的发散；第三坐标只是乘以正长度。所以
\[
 \inf_{c\in\mathbb R^3}\int_{\mathbb T^3}
                 \frac{|a^0-c|^2}{|G^0|}=+\infty.
 \tag{MA.15}
\]
q=0 且分子非零时商取正无穷；两者同零时取零。这不是 MA.10 的带符号项发散，该项仍等于对光滑 grad a 的有界矩阵配对。MA.15 本身只是一张初始切片，不能据此声称正龄时空积分发散。

## 4. 平坦化给出真正的初始时空余项发散

将 MA.12 作一个明确可控的光滑修改。取固定 C∞ 截止 chi，0<=chi<=1，于 |s|<=1 为一、|s|>=2 为零。令 epsilon>0 足够小，使 y=0、pi 的两个截止支撑不相交，所有局部坐标按周期延拓。定义
\[
 \widetilde g_\epsilon(x)=g(x)-\chi(x/\epsilon)[g(x)-g(0)],
 \qquad
 \widetilde f_\epsilon(y)=f(y)
 -\sum_{y_*\in\{0,\pi\}}\chi((y-y_*)/\epsilon)[f(y)-f(y_*)].
 \tag{MA.16}
\]
分别减去各自周期均值，得到 f_epsilon,g_epsilon；设 u_epsilon^0=(f_epsilon(y),g_epsilon(x),0)。减常数不改变梯度或压力源，无散性保持。由于原函数在各中心的一、二阶导数为零，函数差 O(epsilon³)、一阶差 O(epsilon²)、二阶差 O(epsilon)，所以 u_epsilon^0→u^0 于 C²。源 tr(G_epsilon²)→tr(G²) 于 H1，且都均值零。非零 Fourier 模上的逆 Poisson 估计给 grad p_epsilon→grad p 于 H2；三维周期 H2 嵌入 C0（可由 sum_(n in Z³)(1+|n|²)^(-2)<infty 直接验证）。因此压力梯度一致收敛。

固定一个足够小的 epsilon，不再取 epsilon 与时间的联合极限。初始 G_epsilon^0 在两处开区 V_+、V_- 恒零。选其中两个正测度、闭包仍在平坦区域内的小盒子，a_epsilon^0=grad p_epsilon 在它们上分别靠近 ±(36/65)e_1。可取其第一分量分别大于 alpha 和小于 -alpha，alpha>0 固定。

此初值具有光滑无散周期 NS 的局部解及规范压力，依据经典光滑局部存在定理；本次仅定向核对 [Tao 254A Notes 1 的 Corollary 40 及其证明](https://terrytao.wordpress.com/2018/09/16/254a-notes-1-local-well-posedness-of-the-navier-stokes-equations/)，不认领该定理或其全篇依赖审计。周期长度由固定坐标缩放处理。

在足够小的 [0,T] 上，光滑性和初始 G=0 给 |G(t,x)|<=C t 于 V=V_+ union V_-，其中可取 C=1+sup_[0,T]||partial_t G||_infty>0；a(t) 一致接近 a(0)，故缩小 alpha 后，两区的第一分量仍分别大于 alpha、小于 -alpha。对任意空间常向量 c（可随 t 改变），若 c_1>=0，用 V_-；若 c_1<0，用 V_+。因此存在 v>0，
\[
 \int_V|a(t)-c|^2\ge v,\qquad
 \int_V\frac{|a(t)-c|^2}{q_\kappa(t)}
 \ge\frac{v}{\sqrt{C^2t^2+\kappa^2}}.
 \tag{MA.17}
\]
这里 v 可取 alpha² min(|V_+|,|V_-|)。于是
\[
 \boxed{\int_0^T\inf_c\int_V
 \frac{|a(t)-c|^2}{|G(t)|}\,dt=+\infty,\qquad
 \int_0^T\inf_c\int_V\frac{|a(t)-c|^2}{q_\kappa(t)}\,dt
 \ge\frac vC\operatorname{arsinh}(CT/\kappa)\longrightarrow+\infty.}
 \tag{MA.18}
\]
这允许逐时任意常向量选择，不要求其连续。若局部 phi 在 V 上有固定正下界，同样结论乘该下界；若 phi 在初始时间线性或更快消失，这个反检不再给时间发散。

同一个光滑解的 sup_[0,T]||Delta G||_1 有限，由 MA.2，原正则化耗散的时间积分一致有界，P 及 MA.10 的其他原始项也都有限。幅度乘任意固定 lambda>0 后仍有平坦区域、分离的初始压力梯度和光滑局部解；可以缩小初始范数，但不可将一列解的存在时段、常数当成自动相同。

MA.18 比单张切片强：它否定这个非负 Young 余项在任意光滑初始时段上自动有限。它不声称任意固定 t_a>0 的 [t_a,T] 积分发散，不声称解有奇性，不排除空间变参考、保留带符号相消或初始时间截止后的估计。

## 5. 结论范围与下一步

MA.7 给出真正计入原耗散后的必要系数；MA.18 给出直接加速度平方余项的光滑解障碍。这两项不同于 NE 已排除的纯 d² 生产界，也不同于 RL 只指出一个余项尚未受控。MA.10–11 只是用于定位问题的标准链式与 Young 恒等式，不另算正面临界控制。

当前仍没有从任意 NS 演化推出指定中心好尺度。原耗散加一个依赖共同临界预算、在缩放下可求和的余项，仍是未证明的目标。下一步不再尝试以 MA.11 的非负加速度平方商直接闭合估计；回到原带符号近场配对，在固定正龄、完整截止与切片保留的合同下，检查空间变参考的导数成本是否能由同一解控制。若只能恢复 C E(r)，应停止此吸收支路并重新比较既有好尺度路线，不能把新的权或参考名称当成增益。

本节为解析工作。有限 Fourier 检查仅验证 MA.12–14 的无散、Poisson、零点和系数；平坦化、局部存在、积分发散与连续参数下界由上述证明负责。无仿真、DGX、科学附图、读者 HTML/PDF、公开摘要或阶段 recap。完整冻结只一次交给固定发布任务作 PRIVATE_ARCHIVE；研究不执行、监督或汇报发布。
