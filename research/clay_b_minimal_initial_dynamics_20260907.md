# 最小初值之后：重启、缩幅与参数响应的实际约束

2026-09-07。PRIVATE_CORE。内部策略与解析检查，不是新科学发布小节。接续已冻结MI／MP／MQ，分类：条件性必要条件、标准扰动论后果、OPEN / NOT CLAY。上一轮完成候选提取；本轮不把提取后的刚性写成已经解决。

## 1. 坏集合保持，最小集合不因此保持

固定未归一化环面 \(\Omega=(\mathbb R/2\pi\mathbb Z)^3\)、单位黏性、无外力、实值零均值无散初值空间 \(X=\dot H^{1/2}_{\rm df,0}\)。沿用MI列明的临界mild局部理论、唯一性、连续依赖、正时间平滑及延拓接口。假设坏集合 \(\mathcal B=\{g\in X:T(g)<\infty\}\) 非空，\(\rho=\inf_{g\in\mathcal B}\|g\|_X>0\)，且这个周期阈值由f达到。令 \(u(t)=S_tf\)、\(T_*=T(f)\)。

自主性与局部唯一性给，对每个 \(0<t<T_*\)，
\[
 T(u(t))=T_*-t,\qquad F(t):=\|u(t)\|_X^2\ge\rho^2.
 \tag{MR.1}
\]
若重启寿命更长或更短，拼接及唯一性都会违反原最大寿命的定义。这保持的是\(\mathcal B\)，不是球面上的极小集合；没有\(F(t)\)上界、单调增长或轨道紧性。MQ的全空间f仅有范数不超过周期阈值，不能直接称为全空间极小初值，更不能由此断言它的每个缩幅初值全局正则。

在正时间光滑段，设 \(D=\|\Lambda^{3/2}u\|_2^2\)、\(C(u)=-\langle\Lambda u,\mathbb P(u\cdot\nabla u)\rangle\)。完整投影配对给
\[
 \tfrac12F'+D=C(u),\qquad
 \int_0^t(C(u)-D)ds=\tfrac12(F(t)-\rho^2)\ge0.
 \tag{MR.2}
\]
这是既有HN半阶能量恒等式。初端积分由临界类的 \(C_tX\cap L^2_t\dot H^{3/2}\) 与三线性界传递；仅对\(t<T_*\)使用，不声称终端积分有限。

若f处的右导数存在，才有\(F'(0+)\ge0\)；若它等于零且二阶展开合法，才有\(F''(0+)\ge0\)。实际f只知属于X，不能默认这些初端导数存在。在正时间接触点\(F(\tau)=\rho^2\)才有\(F'(\tau)=0,F''(\tau)\ge0\)。写 \(b(v)=\Delta v-\mathbb P(v\cdot\nabla v)\)，则
\[
 F''=2\|b(u)\|_X^2+2(u,Db(u)b(u))_X,\quad
 Db(u)h=\Delta h-\mathbb P(h\cdot\nabla u+u\cdot\nabla h).
 \tag{MR.3}
\]
后一配对没有已证有利符号。一般初值变分、热正则化或球面切向扰动不保证仍在\(\mathcal B\)；不能据极小性写任意方向的Euler–Lagrange方程。特别地，\(af\)在\(0<a<1\)时恰由阈值定义保证全局正则，不是坏集合内的竞争者。平移合法，但所得等式只是范数平移不变性。

## 2. 重启与耗散给的是寿命上界

记 \(E=\|u\|_2^2\)、\(Y=\|\nabla u\|_2^2\)。对实际周期Fourier系数作Cauchy–Schwarz，\(F^2\le EY\)。能量等式\(E'=-2Y\)于是给完整恒等式
\[
 E(t)^2+4\rho^4t
 +4\int_0^t[(EY-F^2)+(F^2-\rho^4)]ds=E(0)^2.
 \tag{MR.4}
\]
两个被积余项非负，初端由强L2迹通过。因E单调，\(E_*:=\lim_{t\uparrow T_*}E(t)\)存在；这不是强终端速度迹。对任意\(t<T_*\)，
\[
 \int_t^{T_*}F(s)^2ds\le\frac{E(t)^2-E_*^2}{4},\qquad
 T_*-t\le\frac{E(t)^2-E_*^2}{4\rho^4},\qquad
 T_*\le\frac{E(0)^2}{4\rho^4}\le\frac14.
 \tag{MR.5}
\]
最后一步仅用于这里固定的最低波数1及\(\|f\|_X=\rho\)。这允许有限时间奇性在上界之前发生。它控制的是\(u\in L_t^4\dot H^{1/2}\)，不是临界延拓所需的\(L_t^4\dot H^1\)或轨道\(L_t^\infty X\)。有限时间积分不能由此改成终端有界子列；没有另造标量例或重复旧频率障碍。

## 3. 缩幅全局解的临界费用：可证明的对数必要下界

令\(v_a=S_t(af)\)，\(0<a<1\)。它全局存在，但并未有关于\(a\uparrow1\)的一致临界时空界。设\(w=u-v_a\)、\(x=\|w\|_X^2\)、\(d=\|w\|_{\dot H^{3/2}}^2\)。完整差方程为
\[
 \partial_tw-\Delta w+\mathbb P\big[(v_a\cdot\nabla)w+(w\cdot\nabla)v_a+(w\cdot\nabla)w\big]=0,
 \qquad w(0)=(1-a)f.
 \tag{MR.6}
\]
这里不删除交叉槽或压力投影。标准周期Sobolev乘积界
\(\|gh\|_{\dot H^{1/2}}\le C\|g\|_{\dot H^1}\|h\|_{\dot H^1}\)
用于零均值输入，配合\(\|w\|_{\dot H^1}\le x^{1/4}d^{1/4}\)，给
\[
 \tfrac12x'+d
 \le C_0\|v_a\|_{\dot H^1}x^{1/4}d^{3/4}+C_1x^{1/2}d.
 \tag{MR.7}
\]
乘积界可由半阶Leibniz及\(\dot H^1\hookrightarrow L^6\)、\(\dot H^{1/2}\hookrightarrow L^3\)取得；产品零模被导数消去。自相互作用也可用同一乘积界及\(\|w\|_{\dot H^1}^2\le x^{1/2}d^{1/2}\)核算。取固定\(c_0>0\)使\(C_1c_0\le1/4\)，在\(x^{1/2}\le c_0\)内用Young吸收交叉项的\(d/4\)，得到
\[
 x'+d\le C_2\|v_a\|_{\dot H^1}^4x,
 \quad
 x(t)^{1/2}\le(1-a)\rho
 \exp\!\left(\frac{C_2}{2}\int_0^t\|v_a\|_{\dot H^1}^4ds\right).
 \tag{MR.8}
\]
常数只依赖固定环面和标准乘积常数。实际估计先在\(0<\varepsilon<t<T_*\)积分，以mild类的\(C_tX\)和有限时间范数令\(\varepsilon\downarrow0\)，避免对粗初值直接经典求导。

若MR.8右侧在\(T_*\)严格小于\(c_0/2\)，连续性bootstrap使\(w\)在整个\([0,T_*)\)保持小，且\(\sup x+\int_0^{T_*}d<\infty\)。插值给\(\int_0^{T_*}\|w\|_{\dot H^1}^4\le\sup x\int d<\infty\)。因为全局\(v_a\)在这个有限区间的临界范数有限，u也有有限\(L_t^4\dot H^1\)范数，与标准临界延拓接口矛盾。因此假设的坏f迫使
\[
 J_a:=\int_0^{T_*}\|v_a(t)\|_{\dot H^1}^4dt
 \ge\frac{2}{C_2}\log\frac{c_0}{2(1-a)\rho}
 \quad\text{当右侧为正时}.
 \tag{MR.9}
\]
这是标准扰动论在本问题中的条件性必要后果，不是新爆破解或正则性判据。基本能量仅一致控制\(\int\|v_a\|_{\dot H^1}^2\)，与MR.9相容。已知每个a的全局正则性不提供足以取\(a\uparrow1\)的统一界。

## 4. 实际尝试参数响应，而不是预先禁止未证估计

进一步检查初始共线性是否提供新正量。固定有限观察时间H及紧参数区间\([a_0,a_1]\Subset(0,1)\)。临界mild方程的局部解析依赖可在有限时间分段延续；这里沿用这一标准适定性接口，不声称延到\(a=1\)。令\(z_a=\partial_av_a\)、\(q_a=\partial_a^2v_a\)，则
\[
 \partial_tz_a-\Delta z_a+\mathbb P(v_a\cdot\nabla z_a+z_a\cdot\nabla v_a)=0,\quad z_a(0)=f,
\]
\[
 \partial_tq_a-\Delta q_a+\mathbb P(v_a\cdot\nabla q_a+q_a\cdot\nabla v_a)
 =-2\mathbb P(z_a\cdot\nabla z_a),\quad q_a(0)=0.
 \tag{MR.10}
\]
所有场无散。对固定\(0<t\le H\)定义能量输出空间中的向量
\(V_a=(v_a(t),\sqrt2\nabla v_a|_{(0,t)})\)，其内积为L2终值内积加时空L2内积。相应导数为\(Z_a,Q_a\)。原能量等式及两次参数微分准确给
\[
 \|V_a\|_{\mathcal E_t}^2=a^2\|f\|_2^2,\quad
 \langle V_a,Z_a\rangle_{\mathcal E_t}=a\|f\|_2^2,\quad
 \|Z_a\|_{\mathcal E_t}^2+\langle V_a,Q_a\rangle_{\mathcal E_t}=\|f\|_2^2.
 \tag{MR.11}
\]
有限参数段内解析依赖及\(C_tX\cap L_t^4\dot H^1\)保证这些微分和L2积分合法。二阶配对不能丢掉；实际上它有精确的非正号。令\(W_a=V_a/a\)，则\(\|W_a\|^2=\|f\|_2^2\)、\(\langle W_a,\partial_aW_a\rangle=0\)、\(\langle W_a,\partial_a^2W_a\rangle=-\|\partial_aW_a\|^2\)，所以
\[
 \|Z_a\|_{\mathcal E_t}^2=\|f\|_2^2+a^2\|\partial_aW_a\|_{\mathcal E_t}^2,\qquad
 \langle V_a,Q_a\rangle_{\mathcal E_t}=-a^2\|\partial_aW_a\|_{\mathcal E_t}^2.
\]
得到的是响应的下界，非正配对恰好抵消额外的正响应；不是欲求上界。\(q_a(0)=0\)不让MR.10的源项消失。

取\(0\le h\in C_c^\infty((a_0,a_1))\)，参数积分分部恰给
\[
 \int h\langle V_a,Q_a\rangle da
 =-\int h'\langle V_a,Z_a\rangle da-\int h\|Z_a\|^2da
 =\|f\|_2^2\int hda-\int h\|Z_a\|^2da.
 \tag{MR.12}
\]
代回MR.11，两侧完全抵消，没有得到参数响应的上界。这是一次实际推导失败：能量恒等式描述输出长度，却不控制它对a变化的速度。它不证明原NS不可能有其它参数响应估计，也不把该失败扩张为一般稳定性方法的否定。

## 5. 本轮决定与完整目标

三项自动提升都没有成立：初值最小性不能自动给轨道紧性；耗散重启只给MR.4–5；缩幅全局参考解的比较需要MR.9所揭示的临界费用，参数能量二阶微分也没有消掉这项困难。MR.1–12记录必要条件和一次未闭合的实际尝试，不将“临界费用低于对数增长”另起名字便当作新机制。

空间核心成本同样不能由最小性直接补足。若\(U(y,s)=r u(x_0+ry,t_0+r^2s)\)，则
\[
 \int_{\rm physical\ episode}|\nabla u|^2dxdt
 =r\int_{\rm unit\ episode}|\nabla U|^2dyds.
 \tag{MR.13}
\]
所以每个单位核心即使有固定正耗散，几何收缩尺度上的物理成本仍可求和。最小性不控制移动局部能量式中的输运、压力、中心比较和端点defect；这是已登记的G-C缺口，不重写为新的壳层小节。

本轮不再延伸这三种自动提升，也不重开HN正四次修补、GP净生产、SL标量收缩或旧古代解提取。允许新的非循环未证引理探索的MI准入修订仍有效，不能又变成“先证明困难估计才许研究”。但当前没有选定具有具体新推导机制的下一条刚性引理。下一轮应更换所利用的原NS动力学结构，而不是继续调整这里的范数、重启点或常数。完整周期任意光滑初值目标和一般奇点排除仍OPEN / NOT CLAY。

来源范围：根任务重读MI、MQ及其当前审计／检查点、G、SL、动力学复评、HN、GP和VB相应完整正文；[Rusin–Šverák引言及§3](https://arxiv.org/html/0911.0500v1)明确只极小化初值并保留临界轨道界的缺失，本轮重新核对这些段落。周期标准理论仍按MI接口使用；本稿不把全空间文献当成周期全依赖认证，不作新颖性或高水平发表价值声明。推导与复核为AI辅助，尚无人类同行评审。无仿真、数值证书、DGX、科学图、recap、科学release或发布消息；旧冻结包的一次性交接不变。
