# 一般弱解的局部梯度熵：压力端点与兼容光滑化

2026-09-08，北京时间。WE，PRIVATE_CORE。范围内先验估计与条件正则接口；一般三维 NS / Clay 仍 OPEN / NOT CLAY。没有充分查新，不宣称原创性或真人同行评审。

本轮尚未得到指定中心的尺度衰减，但补上了 SC 留下的一个实际条件：其矩阵变量 Theta 的弱空间导数，可以从一般局部能量弱解的方程本身得到，不必另作 Sobolev 假设。证明仍不给这个导数的自动小量。

关键是对同一个固定弱解作空间卷积。这样梯度仍是梯度，输运交换子在 L1 趋零，局部压力 Hessian 则由散度—旋度补偿和无散扩张控制。它不是把一列不同弱解的梯度偷偷改成强收敛。

## 1. 对象与结论

单位黏性、无外力，\(Q_r=B_r(0)\times(-r^2,0)\)。设分布 NS 解满足
\[
 u\in L^\infty((-1,0);L^2(B_1))\cap L^2((-1,0);H^1(B_1)),
 \quad p\in L^{3/2}(Q_1),\quad\operatorname{div}u=0.
 \tag{WE.1}
\]
本节先验估计不使用局部能量不等式；应用正则判据时另外要求适当性。没有周期、Dirichlet 或终点前光滑条件。记 \(G_{ij}=\partial_j u_i\)、\(q=|G|_F\)、\(P=p-(p)_{B_1}(t)\)，以及
\[
 A=\operatorname*{ess\,sup}_{-1<t<0}\int_{B_1}|u|^2,
 \quad E=\int_{Q_1}|G|^2,\quad D=\int_{Q_1}|P|^{3/2},
 \quad\mathcal R=E^{1/2}+(AE)^{1/2}+E+D^{2/3}.
 \tag{WE.2}
\]
沿用全部实秩至多一矩阵的距离 \(d(G)\)，并定义
\[
 \Theta(G)=d(G)G/|G|^{3/2}\quad(G\ne0),\qquad\Theta(0)=0.
 \tag{WE.3}
\]

**命题 WE-A（局部先验估计，PROVED IN STATED SCOPE）。** 存在只依赖固定内外柱几何和三维标准算子常数的 C，使
\[
 \nabla^2p\in L^1(B_{3/4}\times(-1,0)),\qquad
 \int_{B_{3/4}\times(-1,0)}|\nabla^2p|\le C(E+D^{2/3}),
 \tag{WE.4}
\]
并且
\[
 \Theta(\nabla u)\in L^2((-1/4,0);H^1(B_{1/2})),\qquad
 \operatorname*{ess\,sup}_{-1/4<t<0}\int_{B_{1/2}}|\nabla u|
 +\int_{Q_{1/2}}|\nabla_x\Theta(\nabla u)|^2
 \le C\mathcal R.
 \tag{WE.5}
\]
导数是整个内球上的弱导数。由 \(|\Theta|^2\le q\)，还得到该变量的局部 \(L^\infty_tL^2_x\) 界。这里没有定义一般弱解的经典 \(\nabla(G/q)\)，也没有声称 q 的全部空间导数受控。

## 2. 压力 Hessian 的局部端点估计

先固定几乎每个 t。设 \(c=(u)_{B_1}(t)\)，选固定 \(\chi\in C_c^\infty(B_1)\)，在 \(B_{15/16}\) 为一。令 \(\mathcal A=B_1\setminus\overline{B_{7/8}}\)，
\[
 g=\nabla\chi\cdot(u-c),\qquad
 w=\mathcal B_{\mathcal A}g\in H^1_0(\mathcal A)^3,\qquad
 v=\chi(u-c)-w.
 \tag{WE.6}
\]
w 在环域外作零延拓。因为 u 无散、chi 紧支，\(\int_{\mathcal A}g=0\)。\(\mathcal B_{\mathcal A}\) 是该固定连通光滑环域上的有界线性散度右逆：\(\operatorname{div}w=g\)、\(\|\nabla w\|_2\le C\|g\|_2\)。这是标准 Bogovskii 接口，不声称环域是星形；一般有界 Lipschitz 域的支持保持接口见 [Costabel–McIntosh，导言与§4.3](https://arxiv.org/html/0808.2614v1)。

由 Poincare 及该右逆的界，v 是全空间紧支的无散 \(H^1\) 场，且
\[
 v=u-c\text{ 于 }B_{7/8},\qquad
 \|\nabla v\|_2\le C\|G\|_{L^2(B_1)},\qquad
 \|v\|_3^2\le C\|G\|_{L^2(B_1)}^2.
 \tag{WE.7}
\]
最后一项用全空间 Sobolev 的 L6 界和固定支集体积。均值、右逆和乘法都是固定的连续操作，故 v 可按 t 可测地选取；不另选时间依赖的域或右逆。

令 \(\pi=\mathcal R_i\mathcal R_j(v_i v_j)\)。经典散度—旋度补偿给
\[
 \|\pi\|_{L^{3/2}(\mathbb R^3)}\le C\|v\|_3^2,
 \qquad\|\nabla^2\pi\|_{L^1(\mathbb R^3)}\le C\|\nabla v\|_2^2.
 \tag{WE.8}
\]
第二个界不是 Riesz 在任意 L1 上有界：\(-\Delta\pi=\sum_j\nabla v_j\cdot\partial_jv\)，每个乘积的第一因子无旋、第二因子无散，各乘积的实 Hardy 范数由两个 L2 范数控制，再用 Hardy 到 L1 的二阶 Riesz 界。紧支 H1 的 v 可通过保无散的空间卷积和强 H1 极限取得同一结论。SE.2–4已核对这一标准结构；[Li–Zhang，Theorem 1.2及其s=1证明](https://arxiv.org/html/2106.11852v1)也给相应压力端点。这里采用齐次梯度界，不把其定理陈述中的整个 W1,2 范数误写成相同的齐次公式。

局部 H1 无散速度的压力恒等式为 \(-\Delta p=\operatorname{tr}(G^2)\)。它由空间卷积后的乘积恒等式取强 H1 极限成立，不需要二阶速度导数。因 v=u-c 于内球，\(h=P-\pi\) 在 \(B_{7/8}\) 调和。调和函数内估计和 WE.7–8 给
\[
 \|\nabla^2h(t)\|_{L^1(B_{3/4})}
 \le C\|h(t)\|_{L^{3/2}(B_{7/8})}
 \le C\left(\|P(t)\|_{L^{3/2}(B_1)}+\|G(t)\|_2^2\right).
 \tag{WE.9}
\]
加上近压项并在长度1的时间区间积分，时间 Holder 给 \(\int\|P(t)\|_{3/2}dt\le D^{2/3}\)，于是 WE.4 成立。pi 不必在时空 L^(3/2)；这里确实只需要它在 \(L^1_tL^{3/2}_x\) 的界。

## 3. 固定解的空间卷积与端点交换子

现在 \(H=\nabla^2p\) 已是所需内柱上的 L1 函数。梯度方程在分布意义下为
\[
 \partial_tG+\operatorname{div}(uG)-\Delta G=f,
 \qquad f=-G^2-H\in L^1.
 \tag{WE.10}
\]
这里 div 沿输运指标收缩。微分 NS 所用的乘积恒等式由 u 的局部 H1 光滑化验证；\(uG\)、\(G^2\) 均局部 L1。

取非负、单位积分、支于单位球的光滑空间核 \(\rho\)，\(0<\epsilon<1/48\)，仅在空间卷积，令 \(G_\epsilon=\rho_\epsilon*G=\nabla u_\epsilon\)。在 \(B_{2/3}\times(-1/2,0)\) 上
\[
 \partial_tG_\epsilon+u\cdot\nabla G_\epsilon-\Delta G_\epsilon
 =f_\epsilon+R_\epsilon,
 \quad R_\epsilon=u\cdot\nabla G_\epsilon-(\operatorname{div}(uG))_\epsilon.
 \tag{WE.11}
\]
不能把右侧改成 \(-G_\epsilon^2-\nabla^2p_\epsilon\) 后删除误差，也不把 \(u_\epsilon\) 当成精确 NS 解。

无散度使交换子可精确写成
\[
 R_\epsilon(x,t)=\int\nabla\rho_\epsilon(y)\cdot[u(x,t)-u(x-y,t)]
                       [G(x-y,t)-G(x,t)]\,dy.
 \tag{WE.12}
\]
减去 G(x,t) 所产生的项等于 \(-G(x,t)\operatorname{div}(u*\rho_\epsilon)(x,t)=0\)。空间差分公式和时空 L2 Cauchy 给
\[
 \|R_\epsilon\|_{L^1(K)}
 \le C\|\nabla u\|_{L^2(K^+)}
   \sup_{|y|\le\epsilon}\|G(\cdot-y,\cdot)-G\|_{L^2(K)}
 \longrightarrow0.
 \tag{WE.13}
\]
这里 \(K=B_{2/3}\times(-1/2,0)\)、\(K^+=B_{17/24}\times(-1/2,0)\)。当 x 在 K、\(|y|\le\epsilon<1/48\) 时，差分线段 \(x-sy\)（\(0\le s\le1\)）仍在 \(K^+\) 的空间球内。把更大柱 \(B_{3/4}\times(-1/2,0)\) 上的 G 作局部延拓，只用于这一个固定 G 的 L2 平移连续性，不用延拓定义边界外的方程。核积分 \(\int|y||\nabla\rho_\epsilon(y)|dy\) 与 epsilon 无关。这里直接证明了(2,2)到1的交换子端点，不援引未经核对的弱解重整化结论。

## 4. 时间链式、正耗散与不退缩的顶端

固定 epsilon，完全卷积方程给
\[
 \partial_tG_\epsilon=\Delta G_\epsilon-
       \operatorname{div}(uG)*\rho_\epsilon+f_\epsilon.
 \tag{WE.14}
\]
在固定内球上，右侧属于 \(L^1_tC^k_x\) 对每个固定 k 成立，常数允许依赖 epsilon。因此 \(G_\epsilon\) 有 \(W^{1,1}_tC^k_x\) 代表，可先进行通常的绝对连续时间链式；没有要求 G 原本时间可微。WE.1及WE.4提供整个母柱直到开顶端0的有限积分，不是仅有远离0的局部可积性。

写 \(q_\epsilon=|G_\epsilon|\)，取
\[
 \Phi_\kappa(M)=\sqrt{|M|^2+\kappa^2}-\kappa,
 \quad D_{\epsilon,\kappa}=
     \sum_jD^2\Phi_\kappa(G_\epsilon)
             [\partial_jG_\epsilon,\partial_jG_\epsilon]\ge0.
 \tag{WE.15}
\]
令 \(\phi(x,t)=\eta(x)\zeta(t)\ge0\)，空间支于 \(B_{2/3}\)、在 \(B_{1/2}\) 为一；\(\zeta=0\) 于 \(t\le-1/2\)，\(\zeta=1\) 于 \(t\ge-1/4\)。在 \(\tau<0\) 做链式与空间分部积分，得到
\[
 \begin{split}
 &\int\Phi_\kappa(G_\epsilon(\tau))\phi(\tau)
 +\int_{-1/2}^{\tau}\int\phi D_{\epsilon,\kappa}\\
 &=\int_{-1/2}^{\tau}\int
       \Phi_\kappa(G_\epsilon)(\phi_t+u\cdot\nabla\phi+\Delta\phi)
 +\phi D\Phi_\kappa(G_\epsilon):(f_\epsilon+R_\epsilon).
 \end{split}
 \tag{WE.16}
\]
底部切片由 zeta 为零消去，顶部切片完整保留。对流中的 u 仍是真实弱速度；固定 epsilon 后所需乘积可积，无散度足以分部积分。

因为 \(0\le\Phi_\kappa\le q_\epsilon\)、\(|D\Phi_\kappa|\le1\)，WE.16右侧不超过
\[
 L_\epsilon=\int_K q_\epsilon(|\phi_t|+|\Delta\phi|+|u||\nabla\phi|)
                  +\phi(|f_\epsilon|+|R_\epsilon|),
 \qquad\limsup_{\epsilon\downarrow0}L_\epsilon\le C\mathcal R.
 \tag{WE.17}
\]
四类项依次由 \(C\sqrt E\)、\(C\sqrt{AE}\)、\(C(E+D^{2/3})\) 及趋零交换子控制。界与 tau 和 kappa 无关；没有在0附近引入时间导数发散的截止。

固定 epsilon 后先令 \(\kappa\downarrow0\)。非零矩阵处 \(D_{\epsilon,\kappa}\) 趋于
\(\Gamma_\epsilon=\mathbf1_{\{q_\epsilon>0\}}q_\epsilon|\nabla(G_\epsilon/q_\epsilon)|^2\)。Fatou 保留该正密度，顶部用支配收敛，得到每个合格 tau 的切片界及累计界。再令 \(\tau\uparrow0\)，分别取本质上确界与累计极限，得
\[
 \operatorname*{ess\,sup}_{-1/4<t<0}\int_{B_{1/2}}q_\epsilon(t)\le L_\epsilon,
 \qquad \int_{Q_{1/2}}\Gamma_\epsilon\le L_\epsilon.
 \tag{WE.18}
\]
这里若将两个量相加，上界应为 \(2L_\epsilon\)，不是仍为同一个 L。未声称零集缺陷消失，也不识别这个极限中的带符号零集源；只用非负耗散的下界。

## 5. 识别原弱解的整个弱导数

每个 \(G_\epsilon=\nabla u_\epsilon\) 的行无旋。SC.7–9的兼容性和跨零截断因此给
\[
 \int_{Q_{1/2}}|\nabla\Theta(G_\epsilon)|^2
 \le(2+1/\sqrt2)^2\int_{Q_{1/2}}\Gamma_\epsilon.
 \tag{WE.19}
\]
具体先取 \((F_\epsilon-\delta)_+B_\epsilon\)，\(F_\epsilon=d(G_\epsilon)/\sqrt{q_\epsilon}\)，非零区有 \(q_\epsilon>\delta^2\)，再令 delta 趋零取得全内球弱导数。这一步只用空间兼容性，不要求 \(u_\epsilon\) 满足 NS。

现在才令 epsilon 趋零。同一固定 G 的空间平移连续性给 \(G_\epsilon\to G\) 强 L2；Theta 连续且 \(|\Theta(G_\epsilon)|^4\le|G_\epsilon|^2\)。后者由强 L2 给一致可积性，Vitali 因而给
\[
 \Theta(G_\epsilon)\longrightarrow\Theta(G)\text{ 强 }L^4(Q_{1/2}).
 \tag{WE.20}
\]
结合 WE.18–19的弱 H1 紧性，识别整个内球上的弱空间导数并取得累计界。又 \(q_\epsilon\to q\) 强 L2，可取子列使几乎每个时间切片强 L1 收敛，将 WE.18的切片上界传给 q。两个独立上界相加，常数吸收 \(1+(2+1/\sqrt2)^2\) 等固定因子，得到 WE.5。

取极限的顺序是：固定空间 epsilon，先去范数正则 kappa；再去兼容性截断 delta；最后去空间 epsilon。没有先对不同解取弱梯度极限再对非线性 Theta 使用强连续性，也没有把未定义的弱解 B 的导数设成零。

## 6. 对 SC 的确切补充及仍未闭合的尺度项

若适当弱解定义在 \(\overline{Q_1}\) 的邻域，以上局部结果可以覆盖整个闭柱：取稍大的母柱或有限个紧内柱，保留其有限能量和压力预算。因此 SC-A 中的 \(\Theta(\nabla u)\in L^2_tH^1_x(Q_1)\) 不必再独立假设。

于是对每个有限 M，存在同一个 SC 阈值，使一般局部适当弱解满足
\[
 \mathsf A(1)+\mathsf E(1)+\mathsf D(1)\le M,
 \qquad\int_{Q_1}|\nabla\Theta(\nabla u)|^2<\varepsilon_\Theta(M)
 \quad\Longrightarrow\quad(0,0)\text{ 正则}.
 \tag{WE.21}
\]
积分使用本节取得的弱导数。稍大母柱用于证明其存在和有限性，不进入 SC 的阈值依赖。这里是对已冻结 SC 的新补充，不回改其原有附加条件或审计。小量本身、有效阈值及一般弱解经典Gamma的定义并未因此得到。

令 \(\mathsf K(r)=r^{-1}\int_{Q_r}|\nabla\Theta(\nabla u)|^2\)。单位柱估计按 NS 缩放给
\[
 \mathsf K(r/2)\le C\left\{\mathsf E(r)^{1/2}
 +[\mathsf A(r)\mathsf E(r)]^{1/2}+\mathsf E(r)+\mathsf D(r)^{2/3}\right\}.
 \tag{WE.22}
\]
即使右侧由一个共同 M 控制，也只是有限上界，不是足够小的上界，更不是从 \(\mathsf K(r)\) 到 \(\mathsf K(r/2)\) 的收缩。未归一化积分有限不能消掉 r^(-1)。所以本轮取得弱导数的自动准入，并没有取得指定中心的自动好尺度。

为核查原始动力学问题，对光滑前终端解记 GD 的 \(\mu=\Gamma\,dxdt+\zeta\ge0\)。取空间紧支于方程所在区域的非负光滑 phi 与闭光滑时段 a<b（全周期胞上也可取周期测试），精确局部式仍是
\[
 \left[\int q\phi\right]_a^b+\int\phi\,d\mu
 =\int q(\phi_t+u\cdot\nabla\phi+\Delta\phi)
    -\int\phi B_0:(G^2+H).
 \tag{WE.23}
\]
普通后向热核只消去 \(\phi_t+\Delta\phi\)，不消输运，也不给压力项符号；将极点放在候选顶端时，它还不能在整个后向柱上一致下界。含真实漂移的伴随核若要替代，需要另证所需的统一局部核下界。WE.17使用绝对值只得到WE.22，不能把这些项改写后宣布衰减。

下一步仍需同一真实演化的新增估计。先核查 WE.23的带符号压力—惯性组合是否存在能保留形状耗散的局部抵消，以及截止输运能否一并控制；若采用相对仿射量，必须区分它耗散的是原形状还是相对梯度的方向。RL已经留下的变量系数压力项及GD变轴项不能靠同一Cauchy估计重做。若无可证新结构，保留准确的临界缺口，不把另一个条件判据或有限实验当成全局正则性进展。

## 7. 核查范围

主任务完整读回GD、SC、RL、SE；压力端点使用SE的散度—旋度结构，RL用于避免重做未闭合的变量系数压力估计。普通来源检索核对Li–Zhang的端点定理及s=1证明、Costabel–McIntosh导言和一般Lipschitz域的相应陈述；不宣称全文认证其全部外部依赖。交换子端点在本稿直接证明，没有借来源名称省略端点论证。

没有Deep Research全面综述、新颖性认证、真人同行评审、仿真、DGX、数值证书或科学附图；不生成读者HTML/PDF、公开摘要或阶段recap。审计与冻结清单记录实际审读版本；完整研究只在冻结后一次交固定发布任务作PRIVATE_ARCHIVE，不进行或监督发布。
