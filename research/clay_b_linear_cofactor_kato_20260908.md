# 线性秩一偏离的耗散与压力的一阶生产

2026-09-08，北京时间。LK，PRIVATE_CORE。范围内解析证明与具体估计的反例；一般三维 NS 正则性仍 OPEN / NOT CLAY。不宣称新颖性、最优常数或真人同行评审。

本节得到线性余子式偏离量的完整 Kato 型方程。新增正耗散控制余子式方向，零集贡献也能保留为非负测度。惯性源可精确估为偏离量的平方，不必使用整个梯度乘偏离量的粗界。

但压力不满足相同的二次控制。一个光滑、无散、周期初值族在整胞内产生一阶压力作用；这个阶数差能保持到共同的短时间区间，甚至固定正年龄子区间。它否定的是不含初值或背景项的特定二次压力估计，不是一般 NS 正则性，也不是一条固定解的奇异终端结论。

## 1. 线性商、适用域与旧输入

固定未归一化的 \(\mathbb T^3_{2\pi}\) 和 \(\nu>0\)。u 为同一光滑、无外力、不可压 NS 解；先在闭光滑区间计算。记
\[
 A_{ij}=\partial_j u_i,\quad Q=|A|_F,\quad B=A/Q\ (Q>0),\quad
 J=\operatorname{adj}A,\quad H=\nabla^2p,\quad
 L=\partial_t+u\cdot\nabla-\nu\Delta,
 \quad LA=-A^2-H.
 \tag{LK.1}
\]
沿用 GD 的 \(d=\operatorname{dist}_F(A,\{\operatorname{rank}\le1\})\)。定义
\[
 \mathcal T(A)=J/Q,\qquad k(A)=|\mathcal T(A)|=|J|/Q\quad(Q>0),
 \qquad \mathcal T(0)=0,\quad k(0)=0.
 \tag{LK.2}
\]
CD 的奇异值比较给 \(d/\sqrt2\le k\le d\) 和 \(k\le Q/\sqrt3\)。k 与 d 线性等价，不是 CD 的平方商。\(\mathcal T\) 在 Q>0 光滑、一次齐次且全局 Lipschitz；k 还在 J=0 处有范数的非光滑性。

旧输入是
\(G=\mathbf1_{\{Q>0\}}Q|\nabla B|^2\)、
\(\nu\int G\le\mathcal B_A\)、\(\sup_t\int Q\le\mathcal B_A\)，其中
\(\mathcal B_A=\int Q(0)+(1+C_H)E_0/\nu\)、\(E_0=\|u(0)\|_2^2/2\)。压力接口为 \(\|H(t)\|_1\le C_H\|A(t)\|_2^2\)，不是一般 L1 源的 Riesz 有界性。初始梯度成本不删去。

## 2. 正耗散与可控的负余项

在 \(Q|J|>0\) 令 \(e=J/|J|\)，\(\Pi_{e^\perp}V=V-(e:V)e\)。范数链式给
\[
 Lk+\nu P_k=-Dk_A[A^2+H]-\nu R,
 \quad P_k=\frac1{Q|J|}\sum_j|\Pi_{e^\perp}\partial_jJ|^2
           =k|\nabla e|^2,
 \quad R=e:\sum_jD^2\mathcal T_A[A_j,A_j].
 \tag{LK.3}
\]
这里 \(A_j=\partial_jA\)。正项来自范数 Hessian；它尚未包含零集测度。

一次齐次性给 \(D^2\mathcal T_A[A,V]=0\)。写
\(A_j=(\partial_jQ)B+V_j\)、\(V_j=Q\partial_jB\)，则 \(A:V_j=0\)，并有
\[
 D^2\mathcal T_A[A_j,A_j]
 =\frac{2\operatorname{adj}V_j}{Q}-\frac{J|V_j|^2}{Q^3}.
 \tag{LK.4}
\]
这是完整分母求导后的式子，不是删去径向导数。对任意矩阵 V，\(|\operatorname{adj}V|\le|V|^2/\sqrt3\)，故
\[
 \boxed{|R|\le\sqrt3\,G.}
 \tag{LK.5}
\]
这项负部控制现已证明，不是对 k 的预设凸性。\(R\) 本身没有固定符号。

## 3. 惯性二次，压力仍可线性

在 \(Q|J|>0\)，完整矩阵空间中的导数为
\[
 Dk_A[V]=\frac{e:DJ_A[V]}Q-\frac{|J|(A:V)}{Q^3},\qquad
 DJ_A[V]=AV+VA-(\operatorname{tr}V)A-\operatorname{tr}(AV)I
 \quad(\operatorname{tr}A=0).
 \tag{LK.6}
\]
它满足 \(|Dk_A|\le C\)。只有 \(A^2+H\) 的迹为零；单独拆惯性与压力时保留 \((\operatorname{tr}V)A\)。

由 CD 的 \(DJ_A[A^2]=-(\det A)I\)，
\[
 Dk_A[A^2]=-\frac{(\det A)\operatorname{tr}J}{|J|Q}
           -\frac{|J|(A:A^2)}{Q^3}.
\]
若奇异值为 \(s_1\ge s_2\ge s_3\)，则
\(|\det A|\le Q(s_2^2+s_3^2)/2=Qd^2/2\)。再用
\(|\operatorname{tr}J|\le\sqrt3|J|\) 与 CD 的
\(|A^2|\le(\sqrt3+3)Qd\)，得到
\[
 \boxed{|Dk_A[A^2]|\le C d^2\le2C k^2,\qquad
        |Dk_A[H]|\le C|H|.}
 \tag{LK.7}
\]
第一式是精确微分后的改进；直接用 \(|Dk||A^2|\) 只能给粗界 \(CQd\)。第二式给压力总积分控制，尚不能把它改成相对偏离量的二次估计。

## 4. 一参数正则化保留两类零点

设 \(h(A)=k(A)^2=|J|^2/Q^2\) 于 Q>0，\(h(0)=0\)。h 二次齐次、球面光滑，满足 \(|Dh|\le CQ\)、\(|D^2h|\le C\)；所以延拓属于全局 \(C^{1,1}\)。此外 \(h=|\mathcal T|^2\)、\(|D\mathcal T|\le C\)，给 \(|Dh|^2\le Ch\)。因此固定 \(\delta>0\) 时
\[
 k_\delta=(h+\delta^2)^{1/2}-\delta\in C^{1,1},\qquad
 |Dk_\delta|\le C,\qquad 0\le k-k_\delta\le\delta.
 \tag{LK.8}
\]
界 \(|D^2k_\delta|\le C/\delta\) 保证固定参数下的合法二阶链式。h 在原点的梯度为零，\(Dk_\delta(0)=0\)。光滑 A 的各空间导数在 \(A=0\) 集合上几乎处处为零；可逐分量沿坐标线使用零水平集的导数性质，再由 Fubini 得到。因此固定 \(\delta\) 的复合没有被漏掉的 Q=0 奇异测度。

在 Q>0 设 \(s_\delta=(|\mathcal T|^2+\delta^2)^{1/2}\)。完整链式为
\[
 \begin{aligned}
 Lk_\delta&=-Dk_\delta[A^2+H]-\nu(\Pi_\delta+R_\delta),\\
 \Pi_\delta&=\sum_j\left(\frac{|\partial_j\mathcal T|^2}{s_\delta}
 -\frac{(\mathcal T:\partial_j\mathcal T)^2}{s_\delta^3}\right)\ge0,\\
 R_\delta&=\frac{\mathcal T}{s_\delta}:\sum_jD^2\mathcal T[A_j,A_j],
 \qquad |R_\delta|\le\sqrt3 G.
 \end{aligned}
 \tag{LK.9}
\]
密度在 Q=0 处按几乎处处零值解释。J=0、Q>0 时 \(\Pi_\delta\) 不能删去，那里仍可有 \(|D\mathcal T\nabla A|^2/\delta\)。

令 \(R_0=R\) 于 \(Q|J|>0\)，其余取零。G 支配给 \(R_\delta\to R_0\) 强 L1。源项的极限导数 \(Dk_0\) 在 J=0 处取零，其余取 LK.6；这是正则化的源项选择，不是声称 k 在 J=0 可微。源项亦强 L1 收敛。积分 LK.9、使用 \(k_\delta(T)\ge0\)，有
\(\nu\int\Pi_\delta\le C\mathcal B_A\)。

于是完整方程唯一决定非负测度极限 \(\Pi\)。在 \(Q|J|>0\) 的紧子集上经典收敛，故
\[
 \boxed{
 Lk=-Dk_0[A^2+H]-\nu R_0-\nu\Pi,\qquad
 \Pi=\mathbf1_{\{Q|J|>0\}}P_k\,dxdt+\rho,
 \quad\rho\ge0,\quad\operatorname{supp}\rho\subseteq\{J=0\}.}
 \tag{LK.10}
\]
Q=0 包含在 J=0 中，可能贡献进入同一 \(\rho\)，而非被排除。这里不保留一个未经控制的有符号 Q 缺陷；理由是固定参数的 \(C^{1,1}\) 链式及 \(R_\delta\) 的强 L1 收敛，而不是任意合并两种弱极限。

固定闭光滑区间还有
\(\int\Pi_\delta(t)\le C\|\Delta A(t)\|_1+\sqrt3\int G(t)
\le C'\|\Delta A(t)\|_1\)，排除光滑时段端点聚集。候选奇异终点处不预设光滑迹。最终得到
\[
 \boxed{\nu\int P_k+\nu\rho\le C\mathcal B_A,
 \qquad Lk+\nu P_k+\nu\rho\le C(d^2+|H|+\nu G).}
 \tag{LK.11}
\]
后一式为分布不等式，P_k 在其定义域外取零。Lk 具有有限测度范数；同 CD 的固定测试论证，\(k(A(t))dx\) 有唯一有限非负弱测度终端迹。它不是 d 的强迹，也没有证明排除集中或 GD.11。

## 5. 方向耗散没有自动补上幅度导数

在原点附近取相容速度
\(u=(M x_2,\epsilon x_3+x_3^2/2,0)\)，\(M>0\)。令 \(z=\epsilon+x_3>0\)，则
\[
 A=M E_{12}+zE_{23},\quad J=MzE_{13},\quad
 Q=\sqrt{M^2+z^2},\quad k=Mz/Q,
 \quad P_k=0,\quad G=M^2/Q^3.
\]
直接求导得
\[
 \frac{|\nabla\sqrt k|^2}{P_k+G}
 =\frac{M^3}{4z(M^2+z^2)}\longrightarrow\infty
 \quad(M=1,\ x=0,\ \epsilon\downarrow0).
 \tag{LK.12}
\]
因此不存在对所有相容梯度成立的统一点态控制
\(|\nabla\sqrt k|^2\le C(P_k+G)\)。该局部场等于
\(\operatorname{curl}(\epsilon x_3^2/2+x_3^3/6,0,Mx_2^2/2)\)；将势乘以固定局部截断再取 curl，便得到保持该邻域导数的光滑周期无散初值。

若该邻域跨越 z=0，则 k 含 \(|z|\)，\(|\nabla\sqrt k|^2\) 具有 \(1/|z|\) 不可积性，故该初始切片的 \(\sqrt k\notin H^1_{loc}\)。这不是对所有正时间累计估计的否定；零集 Kato 测度不能被直接当作这项发散的普通梯度密度。

较弱的 \(|\nabla k|^2/Q\le C G\) 仍成立：写 k=Qh_1(B)、\(h_1(B)=|\operatorname{adj}B|\le d/Q\)，利用 GD 行无旋控制和 \(h_1\) 的球面 Lipschitz 界即可得到。它只继承旧估计，没有将分母 Q 改成 k，也没有新增临界时间范数。

## 6. 整胞压力生产是一阶量

以下是一个新的、明确写出的初值族；不假定其 Fourier 支撑在非线性演化中封闭。固定 \(M>0\)、\(0<\alpha<1\)，用坐标 \((x,y,z)\)，设
\[
 g(y)=1-\alpha\cos y>0,\quad
 \psi_\epsilon=M\cos y+\epsilon g(y)\cos(x+y),\quad
 u_{\epsilon,0}=(\partial_y\psi_\epsilon,-\partial_x\psi_\epsilon,0)
 =\bar u_0+\epsilon v_0.
 \tag{LK.13}
\]
这些初值光滑、周期、无散、均值零，且任意固定阶 Sobolev 范数在 \(0<\epsilon\le1\) 上统一有界。\(\bar A_{12}=-M\cos y\) 是逐点秩至多一的背景，所以
\(d(A_{\epsilon,0})\le\epsilon|\nabla v_0|\)。

由 \(\Delta p=-\operatorname{tr}(A^2)\)，均值零压力满足
\(H_{\epsilon,0}=\epsilon H_1+\epsilon^2H_2\)，其中 H_2 是固定光滑矩阵场，且
\[
 \begin{aligned}
 \Delta p_1&=2M\cos y\,g(y)\cos(x+y),\\
 p_1={}&-\frac M5\cos(x+2y)-M\cos x+\frac{M\alpha}2\cos(x+y)\\
       &+\frac{M\alpha}{20}\cos(x+3y)+\frac{M\alpha}4\cos(x-y),
 \qquad H_1=\nabla^2p_1.
 \end{aligned}
 \tag{LK.14}
\]
在 \(\cos y\ne0\)、\(\cos(x+y)\ne0\) 的几乎处处点，二维块的行列式给
\(Dk_0(A_{\epsilon,0})[H_1]\to\operatorname{sgn}(\cos(x+y))H_{1,12}\)。完整导数的分母项趋零，不能仅凭忽略分母来断言此极限。

H_1 的混合导数中，\((x+y)\) 模式系数为 \(-M\alpha/2\)，其余模式与 \(\operatorname{sgn}(\cos(x+y))\) 的整胞配对为零。使用 \(\int|\cos(x+y)|=16\pi^2\) 和统一 Dk 界的支配收敛，得到
\[
 W_\epsilon(0):=-\int Dk_0(A_{\epsilon,0})[H_{\epsilon,0}],
 \qquad \boxed{\frac{W_\epsilon(0)}\epsilon\longrightarrow8\pi^2M\alpha>0.}
 \tag{LK.15}
\]
但 \(\int k^2\le\int d^2\le\epsilon^2\|\nabla v_0\|_2^2\)。这已经否定统一初值类上的整胞界 \(W\le C\int d^2\) 或 \(C\int k^2\)。它比任意矩阵的点态检查更具体，但尚需下面的实际时间论证。

## 7. 阶数差延续到共同的固定时间窗

背景有精确原 NS 演化
\(\bar u(t)=(-M e^{-\nu t}\sin y,0,0)\)，压力为零。固定整数 \(m\ge5\)。标准周期局部强解理论与统一初值 \(H^m\) 界，给所有充分小 \(\epsilon>0\) 一个共同光滑区间 \([0,T_1]\) 及统一 \(H^m\) 界。这里只需局部理论，不调用任意三维全局正则性，也不依赖二维全局定理。

记 \(w_\epsilon=(u_\epsilon-\bar u)/\epsilon\)，压力商为 \(\pi_\epsilon=p_\epsilon/\epsilon\)。它满足
\[
 \partial_tw_\epsilon+\bar u\cdot\nabla w_\epsilon
 +w_\epsilon\cdot\nabla\bar u+\epsilon w_\epsilon\cdot\nabla w_\epsilon
 +\nabla\pi_\epsilon=\nu\Delta w_\epsilon,
 \qquad w_\epsilon(0)=v_0.
 \tag{LK.16}
\]
把输运写成 \(u_\epsilon\cdot\nabla w_\epsilon\)，对该差分方程作 \(H^m\) 能量估计，压力与无散测试正交。Leibniz 展开、最高阶输运的积分消去和 \(H^m\hookrightarrow W^{1,\infty}\) 给
\[
 \frac d{dt}\|w_\epsilon\|_{H^m}^2+2\nu\|\nabla w_\epsilon\|_{H^m}^2
 \le C_m(\|u_\epsilon\|_{H^m}+\|\bar u\|_{H^{m+1}})
        \|w_\epsilon\|_{H^m}^2.
\]
因此 \(w_\epsilon\) 的 \(C_tH^m\) 界也统一，不是先除以 \(\epsilon\) 再假设误差受控。

令 w 是 LK.16 去掉 \(\epsilon w_\epsilon\cdot\nabla w_\epsilon\) 后的线性化解，初值仍为 \(v_0\)，压力记作 \(\pi_1\)。对 \(r_\epsilon=w_\epsilon-w\) 在 \(H^{m-1}\) 作能量估计，唯一外源为 \(-\epsilon w_\epsilon\cdot\nabla w_\epsilon\)，其该范数至多 \(C\epsilon\)。初始误差零，故
\[
 \|w_\epsilon-w\|_{C([0,T_1];H^{m-1})}\le C\epsilon,
 \quad
 \left\|\frac{H_\epsilon}{\epsilon}-H_1(t)\right\|_{C([0,T_1];H^{m-2})}
 \le C\epsilon,\qquad H_1(t)=\nabla^2\pi_1(t).
 \tag{LK.17}
\]
第二式使用均值零压力方程
\(\Delta\pi_\epsilon=-2\operatorname{tr}(\bar A\nabla w_\epsilon)
-\epsilon\operatorname{tr}((\nabla w_\epsilon)^2)\)，及周期 Fourier 乘子 \(\nabla^2\Delta^{-1}\) 的 \(H^{m-2}\) 有界性。\(H^{m-2}\hookrightarrow C^0\)，所以压力收敛足以用于下文。共同时间和常数可依赖 \(\nu,M,\alpha,m\)，但不依赖 \(\epsilon\)。

唯一性保证 \(u_\epsilon\)、w 均保持与 z 无关且第三分量为零；这只用于该族。设 \(b(t)=\partial_xw_2(t)\)。起点
\(b(0)=g(y)\cos(x+y)\)，其零集上 \(|\partial_xb(0)|\ge1-\alpha\)。由 \(C_tC^1_x\) 连续性，可取共同的 \(T_0\in(0,T_1]\)，使每个 \(t\in[0,T_0]\) 的 b 零集仍为正则水平集，因而体积测度为零。具体地，先把零点限制到 \(|\cos(x+y)|<1/2\) 的条带，再保持该条带上 \(|\partial_xb|\) 的正下界；不是假设任意长时间的零集结构不变。

对几乎处处的时空点，\(\bar A_{12}(t)\ne0\)、\(b(t)\ne0\)。二维块计算和 LK.17 给
\[
 \frac{W_\epsilon(t)}\epsilon\longrightarrow
 W_1(t):=-\int\operatorname{sgn}(b(t))H_{1,12}(t),
 \quad W_1(0)=8\pi^2M\alpha.
\]
W_1 在零时刻连续：在起点非零 b 的几乎处处点使用符号函数的收敛，其余由统一压力界支配。再次缩小固定 \(T_0\)，可令 \(W_1(t)\ge4\pi^2M\alpha\) 于该区间。

因此对任意固定 \(0\le a<b\le T_0\)，支配收敛给
\[
 \boxed{
 \int_a^b W_\epsilon(t)\,dt=\epsilon(c_{a,b}+o(1)),
 \quad c_{a,b}=\int_a^bW_1(t)\,dt>0,
 \qquad \int_a^b\!\!\int d(A_\epsilon)^2\le C\epsilon^2.}
 \tag{LK.18}
\]
末式仅用同一时刻的 \(\bar A(t)\) 秩至多一及统一 \(\nabla w_\epsilon\) 界；\(k^2\le d^2\) 给相同结论。时间窗不随 \(\epsilon\) 缩短，可以取 \(a>0\)。所以没有仅依赖这些固定参数与共同光滑范数上界的有限 C，使
\(\int_a^bW_\epsilon\le C\int_a^b\int d^2\) 对该族普遍成立。

这项否定针对不额外包含初值项、线性背景耦合项或其他补偿项的上述二次估计；常数 C 仍允许依赖固定背景参数。\(\int k(0)\) 本来可以是一阶量；加入它的估计没有被本例否定。这里改变初值并研究共同局部区间，不是一条固定解趋近奇异终点的反例，更不构成奇性或全局几何方法的不可行性结论。

## 8. 对后续路线的约束

正面结果是 LK.10–11 的线性缺陷正测度耗散、受控负余项和惯性二次源。新增项只控制余子式方向；直接幅度提升失败，压力相对二次吸收也在实际原 NS 的共同时间窗上失败。已有能量与 Hardy 接口仍控制压力总 L1，不能写成“压力完全失控”。

GD.11 的临界 d 范数仍未得到。下一步不再尝试仅以 k² 为源的自主标量闭合，也不再重复一次齐次熵或改权重。应先把本例中一阶的压力传递作为线性化演化的一部分，写清它如何作用于秩一背景的横向偏离，再检验与真实涡伸长的联合估计是否有不同于裸压力吸收的抵消。任何依赖背景梯度的系数都须显式保留；局部扰动稳定性不能冒充任意初值的全局控制。这是下一项问题，不是本节已证答案。

局部理论的外部接口定向核对了 [Tao 原稿 v4，第5节 Theorem 5.1](https://arxiv.org/html/1108.1165v4)：均值零周期数据的局部存在、唯一性、光滑保持和稳定性，源文使用单位周期与黏性归一；本文保留固定 \(2\pi\)、\(\nu\) 的常数依赖。上面的高阶差分和一阶压力极限另行写出，不以该文稳定性标题代替证明。该来源已用于旧 BTS，本轮不是新文献发现或全面 Deep Research／原创性审查。没有审查全文其他定理或归档第三方 PDF。

主任务和两位参与推导的 AI 审读者复算，实际版本及范围另记。没有 PDE 仿真、数值证书、DGX、科学附图或读者 HTML/PDF；不触发大里程碑回顾。新完整内容保持私有，不请求网站／本地读者或公开计数。
