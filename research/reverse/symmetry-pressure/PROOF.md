# 双对称周期压力与原点应变：主推导

2026-09-08。PRIVATE_CORE。按 CONTRACT 作手工解析推导；作者自读完成，待独立推导及非作者审查，不先作最终接纳。未读本合同独立稿。合同已披露先验群作用和周期核预检，以及正式推导前纠正的压力前号。

结论范围：存在两份允许初值，在原点同一邻域都为零，却有不同的混合压力 Hessian 和真实 NS 解的原点应变初始导数。这个特定局部资料不能决定该导数；不是再生成、长期增长或奇性结论。

## 1. 完整方程和对称原点的精确接口

固定 ν>0，T³=(R/2πZ)³；压力零均值，
\[
 u_t+(u\cdot\nabla)u=\nu\Delta u-\nabla p,
 \quad\nabla\cdot u=0,
 \quad-\Delta p=\partial_i\partial_j(u_i u_j).
 \tag{SP.1}
\]
令 \(\mathcal G=\{P,-P:P\text{ 为坐标置换矩阵}\}\)，共十二个互异矩阵。这些都是正交整数矩阵，因而是本固定环面的合法自同构。对场的作用是
\[
 (T_Sv)(x)=S v(S^Tx),\qquad S\in\mathcal G.
 \tag{SP.2}
\]
允许类 X 正是这些作用的不动点中的光滑、实值、无散、零均值场。

SP.1 对 \((u,p)\mapsto(T_Su,p(S^Tx))\) 协变；链式法则直接保持输运、散度和 Laplacian，且正交变换保持零均值。局部光滑唯一性因此保证：从 X 出发的同一真实解在其已有经典窗内仍属 X。这里没有把非线性投影到某个支撑或极化子空间。所需完整局部唯一解在第5节单独支付。

中心奇性给 \(u(0,t)=0\)。记 \(A_{ij}(t)=\partial_j u_i(0,t)\)、\(H_{ij}(t)=\partial_{ij}p(0,t)\)。对每个 P，\(A=PAP^T\)。置换在三个对角位置及六个有序非对角位置分别传递，故 A 的对角相同、非对角相同；无散使其对角为零。以 \(\beta=A_{12}\) 记之：
\[
 A=\beta(J-I),\qquad A^2=\beta^2(J+I),
 \tag{SP.3}
\]
其中 J 是全一矩阵。此处 \((J-I)^2=J+I\) 使用 J²=3J。原点梯度形状是已有运动学接口，不计新结论。

零均值压力的 Poisson 唯一性给 \(p(Px,t)=p(x,t)\)，故 H 也有共同对角 α 和共同非对角 h。取 SP.1 的散度，
\[
 \operatorname{tr}H=-\operatorname{tr}(A^2)=-6\beta^2,
 \qquad \alpha=-2\beta^2.
 \tag{SP.4}
\]
这一步只锁定对角，并没有确定 h。

在全域记 A(x,t)=∇u(x,t)。直接对 SP.1 求导得到
\[
 (\partial_t+u\cdot\nabla)A
   =-A^2-\nabla^2p+\nu\Delta A.
 \tag{SP.5}
\]
它与旧 AE.10–11 的单位黏性微分结构一致，此处保留任意固定 ν。原点输运项因 u(0,t)=0 消失，但黏性项保留。令 \(c(t)=(\Delta\partial_2u_1)(0,t)\)，则
\[
 \boxed{\beta'(t)=-\beta(t)^2-h(t)+\nu c(t).}
 \tag{SP.6}
\]
β、c、h 都来自同一真实解；没有声称 h 或 c 是 β 的函数。Miller §3.1 的全空间瞬时积分不作为这里的周期压力公式。

## 2. 周期 Green 核和一个不会被周期修正消去的观测

记 V=(2π)³，G 为零均值周期 Green 分布，\(-\Delta G=\delta_0-V^{-1}\)。以下卷积用 Lebesgue 测度：
\[
 p_v=\partial_i\partial_jG*(v_i v_j).
 \tag{SP.7}
\]
这是正号；其 Fourier 系数为 \(-k_i k_j\widehat{v_i v_j}(k)/|k|^2\)。在源支撑离原点有正距离时，
\[
 (\nabla^2p_v(0))_{ab}
 =\int\partial_a\partial_b\partial_i\partial_jG(-x)
             v_i(x)v_j(x)\,dx.
 \tag{SP.8}
\]
所有微分留在核上，没有删去应力导数或边界项。

旧 exterior-pressure/PROOF §1–2 已给完整周期入口及
\[
 G(x)=\Phi(x)+Q(x),\qquad
 \Phi(x)=\frac1{4\pi|x|},\quad Q\in C^\infty(B_1).
 \tag{SP.9}
\]
其热核分解保留全部周期像项：短时非零像点离 B₁ 有正距离，长时周期非零频率指数衰减，自由热核各阶导数可积，故 Q 逐阶光滑。这里只用其四阶导数在较小闭球有界，不重复旧距离指数或能量锐性。G 在本群下不变，特别为偶分布：变换后的核满足同一个零均值 Poisson 定义，唯一性给出相等。因此四阶核亦为偶函数。

置 \(e=(1,1,1)/\sqrt3\)，\(D_e=e\cdot\nabla\)。在轴上 \(x=\rho e\)、ρ>0，直接对 \(\Phi((\rho+s)e)=(4\pi(\rho+s))^{-1}\) 作四次 s 导数：
\[
 D_e^4\Phi(\rho e)=\frac{24}{4\pi\rho^5}>0.
 \tag{SP.10}
\]
固定较小闭球上的 \(M=\sup|D_e^4Q|<\infty\)。先选充分小的符号 ρ，使 \(24/(4\pi\rho^5)>2M\)；若 M=0，仅需 ρ 在该球内。这样 \(D_e^4G(\rho e)>0\)。再由连续性，在轴点附近选一个固定 y，使
\[
  y_1,y_2,y_3>0\text{ 且两两不同},\quad
  |y|<1/2,\quad D_e^4G(y)>0.
 \tag{SP.11}
\]
正且两两不同的点在该邻域存在，因为有限个坐标相等平面不含开球。于是十二点 \(Sy\)、S∈G，均互異：正置换之间由坐标不同区分，负置换的全部坐标为负。它们也都非零且在基本立方体内部。

这一步先用完整 G 支付符号非零性，再固定 y。不是把周期核替换为 Φ，也没有求 M、ρ、y 的数值或把选择族解释为动力学。

## 3. 无散局部场及严格局部化误差

取一个固定的非零、非恒定、实值径向 \(\varphi\in C_c^\infty(B_1(\mathbb R^3))\)，令
\[
 W(\xi)=\nabla\varphi(\xi)\times e
       =\nabla\times(\varphi(\xi)e).
 \tag{SP.12}
\]
W 实值、光滑、紧支撑、无散，每一分量积分为零。径向性使
\[
 \int\partial_i\varphi\,\partial_j\varphi\,d\xi
      =m\delta_{ij},\qquad
 m=\tfrac13\int|\nabla\varphi|^2>0.
\]
故其完整应力积分及能量为
\[
 \int W\otimes W\,d\xi=m(I-e\otimes e),
 \qquad J_W=\int|W|^2=2m>0.
 \tag{SP.13}
\]
这个矩阵等式可由反对称叉乘矩阵相乘直接核清；不是把逐点应力替换为各向同性。

对尚待一次固定的 ε>0，定义局部周期场
\[
 v_\varepsilon(x)=\varepsilon^{-3/2}
 W((x-y)/\varepsilon).
 \tag{SP.14}
\]
先限制 ε 小于一个固定正的几何上界 ε₀，使十二个球 \(B_\varepsilon(Sy)\) 彼此不相交、离原点有正距离、闭包在基本立方体内部。这由有限集的正最小距离及边界距离可得。SP.14 在基本立方体外延拓为周期场；因支撑远离边界，延拓光滑。它仍无散、零均值，且 \(\int|v_\varepsilon|^2=J_W\)。

记实对称矩阵
\[
 K_e(x)_{ij}=D_e^2\partial_i\partial_jG(x).
\]
在所用源邻域 \(\Delta G=V^{-1}\)，所以
\[
 \operatorname{tr}K_e=D_e^2\Delta G=0,
 \qquad e^TK_e e=D_e^4G.
 \tag{SP.15}
\]
SP.8、核的偶性及 x=y+εξ 换元给
\[
 L_\varepsilon:=e^T\nabla^2p_{v_\varepsilon}(0)e
   =\int K_e(y+\varepsilon\xi)_{ij}W_i(\xi)W_j(\xi)\,d\xi.
 \tag{SP.16}
\]
定义该固定无奇点邻域上的连续模
\[
 \omega_y(\varepsilon)
   =\sup_{|z-y|\le\varepsilon}\|K_e(z)-K_e(y)\|_F
       \longrightarrow0.
\]
由 \(\|W\otimes W\|_F=|W|^2\)，完整局部化误差为
\[
 |L_\varepsilon+mD_e^4G(y)|
       \le J_W\omega_y(\varepsilon).
 \tag{SP.17}
\]
主项来自 SP.13–15 的矩阵收缩：
\(m[\operatorname{tr}K_e-e^TK_e e]=-mD_e^4G(y)\)。利用 SP.11，选并固定一个 \(0<\varepsilon<\varepsilon_0\)，满足
\[
 J_W\omega_y(\varepsilon)<\tfrac12 mD_e^4G(y).
 \tag{SP.18}
\]
于是
\[
 L_\varepsilon<-\tfrac12 mD_e^4G(y)<0.
 \tag{SP.19}
\]
ε 的存在只用完整 K_e 的连续性；ρ、y、ε 至此全部固定。误差是严格不等式，不是数值近似、形式 δ 源或未支付的高阶余项。

## 4. 精确群作用不会相消所需混合分量

用这份已固定的 v=vε 定义一个固定初值
\[
 b(x)=\sum_{S\in\mathcal G}T_Sv(x).
 \tag{SP.20}
\]
对 R∈G，\(T_RT_S=T_{RS}\)，群重排即得 \(T_Rb=b\)。因此 b 同时置换等变且中心奇。每项仍光滑、实值、无散、零均值；有限求和亦然。它在原点一个固定共同球内为零。

各项支撑两两不相交，因此对每个 x，完整二次应力恰有
\[
 b\otimes b=\sum_{S\in\mathcal G}(T_Sv)\otimes(T_Sv).
 \tag{SP.21}
\]
所有交叉应力逐点为零，是已付的支撑事实，不是相位或能量近似。压力对给定应力线性，故 \(p_b=\sum_S p_{T_Sv}\)。Poisson 协变与零均值唯一性进一步给
\[
 p_{T_Sv}(x)=p_v(S^Tx),\qquad
 H_b=\sum_{S\in\mathcal G}S H_v S^T.
 \tag{SP.22}
\]
因 \(S^Te=e\) 或 −e，
\[
 e^TH_b e=12\,e^TH_v e=12L_\varepsilon<0.
 \tag{SP.23}
\]
不能用一般“对称化保留非零性”代替这条定向观测等式；本例恰通过它排除了群抵消。

b 在原点邻域为零，因此 p_b 在该邻域调和。H_b 又为置换不变矩阵，其对角相同且迹零，故对角为零；以 \(h_b=(H_b)_{12}\) 记共同非对角，\(H_b=h_b(J-I)\)。于是
\[
 2h_b=e^TH_b e=12L_\varepsilon,
 \qquad\boxed{h_b=6L_\varepsilon<0.}
 \tag{SP.24}
\]
现在取 a≡0。a,b∈X，在原点同一开球完全相同，全部有限阶甚至全部局部速度资料一致；但 \(h[a]=0\ne h[b]\)。这回答合同的唯一有限比较命题为否，只在已构造的零局部资料类上给一个差异。未证明任意局部资料类、任意大小或正负两号可实现。

## 5. 两份固定初值各自的完整 NS 解与严格时间余项

对已经固定的光滑 b，所有 Wiener 范数
\[
 \|b\|_{A_q}=\sum_k(1+|k|)^q|\widehat b(k)|
\]
均有限。实际全文复核的 SOURCE_ATTRIBUTION_LEMMA §2、4 给完整 Fourier–Leray 双线性热估计
\[
 \|e^{\nu s\Delta}B(f,g)\|_{A_q}
 \le(\nu s)^{-1/2}\|f\|_{A_q}\|g\|_{A_q}.
\]
令 B₁=∥b∥A₁>0，取其解析充分窗 \(T=\nu/(256B_1^2)>0\)。半径 2B₁ 的 mild 映射收缩常数至多1/2，得到完整无限维唯一解。该来源的 tame 权重及可积热核卷积级数把每个高阶范数延至同一已有窗；空间高阶连续性与方程再给时间正则。没有取趋零高阶窗的交，也没有使用 Galerkin 模型。B₁、T 是严格定义的解析常数，未求数值，未声称跨数据统一。a≡0 给唯一零解 u^a。

第1节的几何协变和唯一性现适用于这两条实际分支，保证 u^b 的双对称保持。所有 Fourier 模、负频率、黏性及压力由完整方程持续演化；SP.21 只在初始时刻成立，之后不作支撑分离假设。

在初始原点邻域，a=b=0，因此两条解的初始 β、c 都为零。SP.6 给
\[
 (\beta_b-\beta_a)'(0)=-h_b=:d>0.
 \tag{SP.25}
\]
光滑解在闭局部窗上连续于任意 A_q；SP.7 的零阶压力乘子和空间导数使 h 连续，c 及 β² 亦连续。因此这是真实时间导数，不只是静态数据的形式代入。更明确，令
\[
 f(t)=-\beta_b(t)^2-h_b(t)+\nu c_b(t),\qquad f(0)=d.
\]
由 β_a≡0，
\[
 \beta_b(t)-\beta_a(t)=dt+r(t),\qquad
 r(t)=\int_0^t[f(s)-d]ds,
 \quad |r(t)|\le t\sup_{0\le s\le t}|f(s)-d|=o(t).
 \tag{SP.26}
\]
所以存在依赖这份固定数据和 ν 的 \(0<\delta\le T\)，使所有 \(0<t\le\delta\) 有
\[
 \beta_b(t)-\beta_a(t)\ge\tfrac12dt>0.
 \tag{SP.27}
\]
黏性在初始比较中因共同局部资料为零而恰不贡献；SP.26 完整保留正时间的 νc_b 和压力反馈。没有假设 b 的零邻域在正时间保持，没有给未认证的显式 δ 或长期符号。

## 6. 接纳范围、来源与停止处

SP.24 与 SP.25–27 合在一起，说明两种精确对称没有使“原点一个邻域的全部初始速度”足以决定原点应变初始演化。任何以这些相同局部资料和相同 ν 为全部输入、对 X 中所有允许解适用的单值闭合都会给相同初始导数，与本比较矛盾。

这不反驳带全域压力、额外外部资料或特定轨道假设的闭合，也不证明应变长期增长；β 的一个正小窗不是奇性。两份固定数据的解只作比较，不拼接、不轮换，不替换此前原物理数据，更不把符号构造家族的所有尺度安到一份初值的时间历史上。实际第二代供给、动态剖面更新及全部无限过程仍未支付。NO-CANDIDATE / NOT CLAY。

直接本地依赖是 exterior-pressure/PROOF §1–2 的完整周期 Green 正则分解，以及 reconnection-preflight/SOURCE_ATTRIBUTION_LEMMA §2、4 的完整局部唯一解；根本轮均实际全文读。AE 原稿第1–153行、双对称预检两稿和其所列 Miller §3.1 只作来源及去重，原点形状与一般梯度公式在这里直接重核。根只定向读过 Miller 的陈述/定位上下文，不声称本轮全文阅读其证明。没有导入 Euler 爆破、全空间 Biot–Savart 或受限投影模型。

本证明未运行科学程序、读取数组、选择数值初值/时刻或产图，不需要严格数值证书。局部化误差 SP.17–18 和时间余项 SP.26 是不同的解析支付。独立稿、两份非作者审查及根最终比较尚待完成；主稿自读不替代它们。完成此精确接口后，不追加静态场或符号变体来凑机制。
