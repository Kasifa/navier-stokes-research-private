# 近场压力与梯度熵：联合源仍有一阶生产

2026-09-08。NE，PRIVATE_CORE。范围内恒等式、经典接口和光滑周期解反检；一般三维 NS / Clay 仍 OPEN / NOT CLAY。没有充分查新或真人同行评审。

把压力与惯性合在一起，并不会自动得到非正源或偏离秩一的平方界。对一个真实的光滑周期 NS 解族，本节算出联合梯度熵生产的非零一阶项，并将其保持到固定正时间区间。另一方面，这个例子的原耗散不为零，因此它没有排除“用原耗散吸收线性生产”的估计。

## 1. 两尺度积分式：先保留全部项

沿用 WE/GD 的完整梯度 G、q=|G|、非零处 B=G/q、零处 B_0=0，以及非负原耗散测度 mu_G。先在单位黏性、无外力、空间内域和闭光滑时段上计算；不把经典方向导数自动赋给一般弱解。

取 AH 的母尺度 0<r<=1/2、rho=theta r，0<theta<=1/4。用 AH.2 的无散扩张 v_r 和压力 pi_r，令
\[
 h_r=p-\pi_r,\qquad
 N_r=(\nabla v_r)^2+\nabla^2\pi_r,
 \quad v_r=u-(u)_{B_r}(t)\text{ 于 }B_{7r/8}.
 \tag{NE.1}
\]
取光滑 0<=phi<=1，空间紧支 B_rho，定义于闭时段 [a,b] 且无需在端点消失，-rho²<=a<b<0；导数满足标准 rho^(-1)、rho^(-2) 界。WE.23 精确变成
\[
 \begin{split}
 &\rho^{-1}\left[\int q\phi\right]_a^b
   +\rho^{-1}\int_a^b\!\!\int\phi\,d\mu_G\\
 &=\rho^{-1}\int_a^b\!\!\int q(\phi_t+\Delta\phi+u\cdot\nabla\phi)
  -\rho^{-1}\int_a^b\!\!\int\phi B_0:N_r
  -\rho^{-1}\int_a^b\!\!\int\phi B_0:\nabla^2h_r .
 \end{split}
 \tag{NE.2}
\]
顶部和底部切片均在式中。除非实际选择 phi(a)=0，不能删除底部；普通热测试也没有删除 u·grad phi。

AH 的调和内估计只给空间 theta³，时间仅作区间限制，故
\[
 \rho^{-1}\left|\int_a^b\!\!\int\phi B_0:\nabla^2h_r\right|
 \le C\theta^2\{\mathcal H(r)+\mathsf E(r)\},\qquad
 \rho^{-1}\left|\int_a^b\!\!\int\phi B_0:N_r\right|
 \le C\theta^{-1}\mathsf E(r).
 \tag{NE.3}
\]
这不是新增的小量。对输运及截止部分，时空 Cauchy 给
\[
 \rho^{-1}\int_a^b\!\!\int_{B_\rho}q(|\phi_t|+|\Delta\phi|+|u||\nabla\phi|)
 \le C\{\sqrt{\mathsf E(\rho)}+
                   \sqrt{\mathsf A(\rho)\mathsf E(\rho)}\}.
 \tag{NE.4}
\]
这里 A(rho)=rho^(-1) esssup_t integral_Brho|u|²，E(rho)=rho^(-1) integral_Qrho|G|²。两个因子分别来自体积 rho⁵ 与时间长度 rho²。用母尺度界替代，只得到 theta^(-1/2)sqrt(E(r)) 和 theta^(-1)sqrt(A(r)E(r))，没有正的 rho 小因子。NE.2–4 是对同一解的精确分项和旧界定位，不是一个全系统收缩。

## 2. Hardy 配对保留了什么，没给出什么

每个平方矩阵分量都有散度—旋度形式
\[
 ((\nabla v_r)^2)_{ij}=\nabla v_{r,i}\cdot\partial_jv_r,
 \qquad \operatorname{curl}\nabla v_{r,i}=0,
 \quad\operatorname{div}\partial_jv_r=0.
 \tag{NE.5}
\]
经典实 Hardy 估计和二阶 Riesz 算子的 Hardy 有界性因此给
\[
 \|N_r(t)\|_{\mathcal H^1(\mathbb R^3)}
 \le C\|G(t)\|_{L^2(B_r)}^2,
 \qquad \int_{\mathbb R^3}N_r(t)=0.
 \tag{NE.6}
\]
这里是实 Hardy 空间，不是 Sobolev H1。紧支无散 H1 扩张先保无散光滑化，再由双线性 L2–L2 界取强 H1 极限。每个乘积的积分为零；压力 Hessian 的零均值也可由 Hardy 可积性及其零模得到。所用散度—旋度、Riesz 和 Hardy–BMO 对偶是经典输入，不认领为新结果。[Li–Zhang 的 Theorem 1.2 及 s=1 证明](https://arxiv.org/html/2106.11852v1)给出压力的对应 Hardy 端点；齐次梯度界按其证明和 WE 的固定无散扩张使用。

选时间可测的空间常矩阵 W(t)，|W|<=1，不要求其时间可微。将 phi(B_0-W) 在球外延为零，定义 beta(t) 为这个整个矩阵测试的全空间 BMO 半范数（各分量之和）。则逐时
\[
 \left|\int\phi(B_0-W):N_r\right|
 \le C\beta(t)\|G(t)\|_{L^2(B_r)}^2.
 \tag{NE.7}
\]
这是经典对偶的直接应用。B_0 有界使 beta 有限，却不使它自动足够小；没有对 B_0 的零集求导。若另外给 beta<=epsilon，近场的这一部分才小于 C epsilon theta^(-1) E(r)。

常矩阵部分仍然不是零。用 phi 的紧支性和无散度，准确地有
\[
 \int\phi W:N_r
 =-\int(\partial_k\phi)W_{ij}(u_i-c_i)G_{kj}
   +\int\pi_r W_{ij}\partial_{ij}\phi,
 \qquad c=(u)_{B_r}(t).
 \tag{NE.8}
\]
这两项与 NE.2 的输运、切片及调和余压一起保留。全周期胞无截止时，常矩阵积分才为零。不能只给 B 在内球的振荡就删除截止过渡层，也不能将扩张环域当成已满足原 NS 的新速度。

单位方向的振荡本身也不是 Theta 的合适替代。取精确热剪切
\[
 u_\lambda(t)=\lambda(e^{-t}\sin y+e^{-4t}\sin2z)e_1,
 \quad p_\lambda=0,\quad\lambda>0.
 \tag{NE.9}
\]
其梯度处处秩至多一，所以 Theta 和其弱梯度恒零。固定球、固定有限时间窗上的 A、E 按 lambda² 缩小，原 mu 按 lambda 缩小；后者由 q_lambda=lambda q_1、x 独立及原范数方程直接得出。可是 B_lambda=B_1，在非零梯度处不随 lambda 改变。

例如在 t=1、以 (0,0,pi/4) 为心的充分小球中，梯度不为零且 B_1 随 z 非恒，故该球上的平均振荡严格为正，不随 lambda 趋零。于是不存在从上述小幅度预算及小 grad Theta 自动推出单位方向小 BMO 的一般趋零模量。这只排除未加幅度权重的推断；这些小幅度解本来光滑，不反驳加权、截幅或局部正则性方法。

## 3. 完整周期压力没有消去一阶联合生产

现在固定未归一化的 T³_(2pi)、nu>0，采用 SN.13 的初值而计算不同于涡伸长的新对象
\[
 I(u)=\int_{\mathbb T^3}B_0:(G^2+\nabla^2p),
 \qquad -\Delta p=\operatorname{tr}(G^2),\quad\int p=0.
 \tag{NE.10}
\]
原梯度熵方程中的生产是 -I，不是 I。正生产不等于梯度范数净增长，因为黏性耗散仍在。

写 s=sin y、c=cos y、S=sin2z、C=cos2z，令
\[
 U_0=\sin y+\sin2z,\quad
 v_0=(-2cS,sC),\quad
 K=\nabla_\perp v_0=
 \begin{pmatrix}2sS&-4cC\\cC&-2sS\end{pmatrix},
 \quad p_v=-\cos2y-\tfrac14\cos4z.
 \tag{NE.11}
\]
取 0<epsilon<=1，初值 u_(epsilon,0)=(U_0,epsilon v_0) 无散、周期、均值零。其完整梯度第一列为零，压力精确为 epsilon² p_v，并且
\[
 q_\epsilon^2=c^2+4C^2+\epsilon^2(8s^2S^2+17c^2C^2),
 \qquad G_\epsilon:\nabla^2p_\epsilon
       =8\epsilon^3sS(\cos2y-\cos4z).
 \tag{NE.12}
\]
分母 q_epsilon 关于 y→-y 为偶，压力分子为奇，所以初始整胞压力配对精确为零。惯性分子为
\[
 G_\epsilon:G_\epsilon^2
 =2\epsilon sS(c^2-4C^2)-6\epsilon c^2C^2,
 \qquad
 \boxed{I(u_{\epsilon,0})=-6\epsilon\int_{\mathbb T^3}
                    \frac{c^2C^2}{q_\epsilon}<0.}
 \tag{NE.13}
\]
零梯度处按 B_0=0 解释，恒等式几乎处处；被消去的奇项可积，因为原配对由 |G|²+|H| 控制。不是将 SN 的 12pi³ 伸长系数直接照抄到归一化积分。

令 X=c²、Y=C²，则 |K|²=8-8X-8Y+25XY 在单位方形的四角取最大值17。由此及 integral_T³ c²C²=2pi³，并用原秩一背景比较 d，得到
\[
 \boxed{-I(u_{\epsilon,0})\ge
          \frac{12\pi^3\epsilon}{\sqrt{5+17\epsilon^2}},\qquad
 \int d(G_{\epsilon,0})^2\le
       \epsilon^2\int|K|^2=50\pi^3\epsilon^2.}
 \tag{NE.14}
\]
故即使在 0<epsilon<=1 的共同光滑有界初值族上，也不存在不含其他项的统一生产界 -I<=C integral d²。常数允许依赖固定背景和共同光滑上界，仍有阶数矛盾。另有 p[-u]=p[u]、I(-u)=-I(u)，因此 I 无普遍单边符号；这仅比较各自合法初值，不能说整条 -u(t) 轨道仍解原 NS。

## 4. 不是只有初始时刻：完整 2.5 维 NS 解族

直接计算
\[
 \operatorname{div}_\perp v_0=0,\quad
 \Delta_\perp v_0=-5v_0,\quad
 v_0\cdot\nabla_\perp v_0=(-2\sin2y,-\sin4z)
                         =-\nabla_\perp p_v.
 \tag{NE.15}
\]
所以取 a(t)=exp(-5nu t)，并令
\[
 u_\epsilon=(U_\epsilon,\epsilon a(t)v_0),\quad
 p_\epsilon=\epsilon^2a(t)^2p_v,\qquad
 (\partial_t-\nu\Delta_\perp)U_\epsilon
       +\epsilon a(t)v_0\cdot\nabla_\perp U_\epsilon=0,
 \quad U_\epsilon(0)=U_0,
 \tag{NE.16}
\]
便得到完整无外力周期 NS。横向方程由 NE.15 精确满足，轴向是线性输运扩散；均值零由周期积分保持。每个有限 T 上漂移光滑有界，空间微分能量估计和 Gronwall 给全阶 Sobolev 界，常数对 epsilon<=1 一致。Galerkin 逼近提供存在性，差分能量给唯一性，Sobolev 嵌入及方程给光滑性。这是经典的 x 独立构造，不认领为一般三维全局正则性。

令 barU=e^(-nu t)sin y+e^(-4nu t)sin2z，W(0)=0，(partial_t-nu Delta)W=-a v_0·grad barU。余项 R_epsilon=U_epsilon-barU-epsilon W 满足
\[
 (\partial_t-\nu\Delta_\perp+\epsilon a v_0\cdot\nabla_\perp)R_\epsilon
 =-\epsilon^2a v_0\cdot\nabla_\perp W,\quad R_\epsilon(0)=0,
 \qquad \|R_\epsilon\|_{C([0,T];C^k)}\le C_{T,k}\epsilon^2.
 \tag{NE.17}
\]
最后一步由任意足够高阶的空间能量估计、吸收黏性和 Sobolev 嵌入得到；没有把整个 U_epsilon 视为热演化，也没有用一列不同弱解的强梯度收敛。

记 barG=grad(barU e_1)、V=grad(W,a v_0)。因压力只有二阶项，联合源的一阶矩阵为 barG V+V barG，且其模长<=2|barG||V|。归一化误差 |B_epsilon-B_bar|<=2|G_epsilon-barG|/|barG| 与这个因子相消。在 barG=0 处，一阶矩阵本身为零，剩余配对 O(epsilon²)；不需要积分 1/|barG|。因此一致于每个固定 [0,T]，
\[
 I(u_\epsilon(t))=-\epsilon\kappa(t)+O_T(\epsilon^2),\qquad
 \kappa(t)=6e^{-10\nu t}\int_{\mathbb T^3}
 \frac{c^2C^2}{\sqrt{e^{-2\nu t}c^2+4e^{-8\nu t}C^2}}
 \ge\frac{12\pi^3}{\sqrt5}e^{-10\nu t}>0.
 \tag{NE.18}
\]
轴向 W 只进入 V 的第一行，不进入这个一阶配对；横向 V=aK。奇项仍在一阶系数中消去，但没有声称正时间的完整压力配对也精确为零。

于是任意固定 0<=t_a<t_b<=T，包括 t_a>0，有
\[
 \int_{t_a}^{t_b}-I(u_\epsilon(t))\,dt
    =\epsilon\int_{t_a}^{t_b}\kappa(t)\,dt+O_T(\epsilon^2),
 \qquad\int_{t_a}^{t_b}\!\!\int d(G_\epsilon)^2=O_T(\epsilon^2).
 \tag{NE.19}
\]
时间窗不随 epsilon 缩短。该解族每个有限时段都光滑，反检的是特定源估计，不是奇性或一般正则性。

## 5. 尚未排除的估计才是下一步

NE.14、19 排除了无其他补偿的纯二次生产界，没有排除 delta mu_G+C_delta d² 或保留切片、输运和压力尾的混合估计：背景热剪切的原方向耗散非零，为 O(1)。把一阶源误报成这些更强结构的反例，会再次改变命题范围。

下一步只检查原 mu_G 能否吸收这个真实线性生产，并给出临界缩放下可求和或趋零的剩余项。必须同时写明共同 A+E+D 的依赖和局部切片、输运、压力尾；若只能得到总量有限或 C E(r)，就记录为未闭合，不继续改写单位方向的 BMO 权重。优先检验兼容梯度的加权空间配对及其退化零集，不替换成相对梯度耗散。NE 没有产生这一混合吸收，也没有产生指定中心的自动好尺度。

本节新增的是联合归一化源的精确反检及其正时间证明，不是重发 SN 的涡伸长结论。NE.2–8 仅定位旧 Hardy 和局部熵接口仍留下的项；原著仅定向读 Li–Zhang 的端点陈述及 s=1 证明，未做全文依赖认证。WE、GD、AH、SN全文与旧R0.70Z§8–9、energy_stress_commutator_note§5、混合压力来源记录作范围去重。

附带标准库Fraction三角多项式检查验证 Euler/热特征值/Poisson/矩阵分子和奇偶恒等式，并拒绝三个错误输入。它没有求解 PDE，没有数值积分或连续正则性认证。没有 DGX、仿真、科学附图、读者HTML/PDF、公开概要或阶段recap。完整内容只在研究冻结后一次交固定发布任务私有归档；不进行、监督或汇报发布。
