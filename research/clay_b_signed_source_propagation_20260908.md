# 带符号源的传播：压力交换子与原子抵消的边界

2026-09-08。SP，PRIVATE_CORE，INTERNAL CHECK / OPEN / NOT CLAY。本轮执行 LT.17 的具体测试，不另计独立研究小节或 release。完成的是完整时间交换式、一个带实际畸变时钟的抵消界，以及旧真实 NS 解族上的响应反检；没有得到新的无条件临界控制。这些恒等式和经典工具的适配不构成新颖性认证。

## 1. 压力穿过传播时，必须保留双时间项

固定未归一化 \(2\pi\) 三维环面、\(\nu>0\)，同一无外力光滑周期 NS 解存在于 \([0,T)\)，\(T<\infty\)。先在任意 \(0<a\le s\le t\le b<T\) 计算。令
\[
 L=\partial_t+u\cdot\nabla-\nu\Delta,\quad
 G=\nabla u,\quad A=G^2,\quad f=\operatorname{tr}A,\quad
 Q^*=\nabla^2\Delta^{-1},\quad H=-Q^*f,\quad N=A-Q^*f.
 \tag{SP.1}
\]
\(Q^*\) 的非零 Fourier 符号为 \(m(k)=k\otimes k/|k|^2\)，零模为0。它沿用 IDC 的符号；不要和 \(\nabla^2(-\Delta)^{-1}\) 混用。由无散性逐分量分部积分，\(\int A_{ij}=0\)，故 \(\int f=0\)、\(\int N=0\)，且点态 \(\operatorname{tr}N=0\)。

记 \(S(t,s)=S^u(t,s)\) 为同一实际漂移的逐分量齐次传播。它保持常数、均值及逐分量线性关系，但不自动保持源的原散度—旋度乘积表示。定义
\[
 C_\tau=[u(\tau)\cdot\nabla,Q^*].
\]
因为 \([\Delta,Q^*]=0\)，对固定光滑输入 g，差值的初始为零且
\[
 L_t\{S(t,s)Q^*g-Q^*S(t,s)g\}=-C_tS(t,s)g.
\]
于是准确地有
\[
 [S(t,s),Q^*]g
 =-\int_s^t S(t,\tau)C_\tau S(\tau,s)g\,d\tau .
 \tag{SP.2}
\]
常向量漂移不贡献交换子。\(C_\tau1=0\)，其输出的空间均值和矩阵迹均为零；这些事实不删除非零频率。

令
\[
 Z(t)=\int_a^tS(t,s)A(s)\,ds,\qquad
 z(t)=\operatorname{tr}Z(t)=\int_a^tS(t,s)f(s)\,ds .
\]
将 SP.2 代入原完整响应，保留时间顺序后得到
\[
 \begin{aligned}
 \mathcal D_{a,t}
 &=\int_a^tS(t,s)N(s)\,ds=Z(t)-Q^*z(t)+E(t),\\
 E(t)&=\int_a^t\!\int_s^t
       S(t,\tau)C_\tau S(\tau,s)f(s)\,d\tau ds\\
     &=\int_a^tS(t,\tau)C_\tau z(\tau)\,d\tau,\qquad
 G(t)=S(t,a)G(a)-\mathcal D_{a,t}.
 \end{aligned}
 \tag{SP.3}
\]
交换响应 E 前是正号，原初值项不能删除。两个时间积分不是额外的尺度收益：NS 缩放下 \(Cz\) 和 N 均按四阶密度缩放，积分后的 E 与 G 都按二阶缩放。

终端也不能逐项偷换：TG 的线性引理适用于原 \(A,f,N\in L^1_{t,x}\)，故 Z、z、完整 \(\mathcal D\) 有强 L1 终端迹。但是 \(Q^*\) 不在一般 L1 上有界，不能据此给 \(Q^*z\) 和 E 各自强 L1 迹。它们的分布极限可由 SP.3 识别，单项端点范数尚未控制。全文没有将这些场替换为另一条 NS 轨道。

## 2. 可自证的交换子界仍有未付成本

对周期 Green Hessian 的非对角核 \(K_{ij}\)，光滑 u、g 满足安全的差分表达
\[
 (C_ug)_{ij}(x)=
 \int_{\mathbb T^3}[u(x)-u(y)]\cdot\nabla K_{ij}(x-y)
                         [g(y)-g(x)]\,dy .
 \tag{SP.4}
\]
两个差使对角附近成为可积的 \(O(|x-y|^{-2})\)。可先用频率正则化推导，再利用 \(C_u1=0\) 减去 g(x) 后取极限。若删除第二个差，就必须保留分布正则化或其对角修正；不能把剩下的三次奇性当成绝对可积核。

为不借用未读的端点交换子定理，给一个直接 Fourier 上界。采用归一化系数，令
\[
 M(u)=\sum_{\ell\ne0}|\ell|\,|\widehat u(\ell)|.
\]
频率表达为
\[
 \widehat{C_ug}(k)
 =\mathrm i\sum_\ell(\widehat u(\ell)\cdot(k-\ell))
           [m(k-\ell)-m(k)]\widehat g(k-\ell).
 \tag{SP.5}
\]
对 \(n=k-\ell\)，若 \(|\ell|\ge|n|/2\)，使用 m 有界；否则沿线段用
\(|\nabla m|\le C/|n|\)。含 n=0 或 k=0 的情形也给
\[
 |n|\,|m(n)-m(n+\ell)|\le C|\ell|,\qquad
 \|C_ug\|_2\le CM(u)\|g\|_2 .
 \tag{SP.6}
\]
最后一步是离散 \(\ell^1*\ell^2\) Young 不等式。因此
\[
 \|[S(t,s),Q^*]g\|_2
 \le \min\!\left\{2,C\int_s^tM(u(\tau))\,d\tau\right\}\|g\|_2 .
 \tag{SP.7}
\]
这里的2来自 S 的 L2 收缩及 \(Q^*\) 的 Plancherel 算子范数1。M 不含常速度，却至少控制 \(\|\nabla u\|_\infty\)，比基本能量已有输入强得多；它的时间积分具有临界缩放。

实际 f 只有已知的时间—空间 L1 预算，不能直接充当 SP.6 的 L2 输入。使用 LT 的旧 Nash \(1\to2\) 界，只能写出
\[
 \|E(t)\|_2\le C\int_a^t M(u(\tau))
 \int_a^\tau\{V^{-1/2}+[\nu(\tau-s)]^{-3/4}\}
                         \|f(s)\|_1\,ds\,d\tau,\quad V=(2\pi)^3.
 \tag{SP.8}
\]
闭前终端光滑区间上右端有限，但没有由能量、Hardy 或原形状耗散支付其临界成本。旧 MPS.6–8 已核过逐壳核差并无额外频率小因子；本轮不重复认领该观察，也不把这里更强的 M 成本说成一切可能方法的必要代价。

## 3. 零均值抵消确实保留，但收益带实际时间尺度

这里直接证明一个充分界，不将一般纯输运的 Hardy 定理自动移植到周期输运扩散。写
\[
 \gamma(\sigma)=\|\operatorname{sym}G(\sigma)\|_{\infty,\mathrm{op}},
 \qquad
 \mathcal A_{s,t}=\int_s^t
       \exp\!\left[-2\int_s^\rho\gamma(\sigma)d\sigma\right]d\rho .
 \tag{SP.9}
\]
\(\mathcal A\) 是本节的有效扩散时间，不是 PF 的局部动能 \(\mathsf A\)。
取光滑终端测试 \(\eta\)，令 \(h(s)=S(t,s)^*\eta\)，则
\(h_s+u\cdot\nabla h+\nu\Delta h=0\)。
对后向算子 \(L^*_{\rm back}=\partial_s+u\cdot\nabla+\nu\Delta\)，
\[
 L^*_{\rm back}|h|^2=2\nu|\nabla h|^2,\qquad
 L^*_{\rm back}|\nabla h|^2
 =-2\nabla h\cdot\operatorname{sym}G\,\nabla h
       +2\nu|\nabla^2h|^2 .
\]
由于 \(\partial_s\mathcal A_{s,t}=2\gamma(s)\mathcal A_{s,t}-1\)，
后向最大值原理作用于
\(|h|^2+2\nu\mathcal A_{s,t}|\nabla h|^2\)，给
\[
 \|\nabla S(t,s)^*\eta\|_\infty
 \le(2\nu\mathcal A_{s,t})^{-1/2}\|\eta\|_\infty .
 \tag{SP.10}
\]
矩阵测试逐分量求和，采用 Frobenius 模，得到相同论证。一般有界测试通过保持幅值的光滑逼近获得。

若 g 支于注入半径内的 \(B_\ell(x_c)\)，且整胞均值为零，L1 对偶中减去 h(s,x_c)，再用 L1 收缩，得到
\[
 \boxed{\quad
 \|S(t,s)g\|_1
 \le\min\!\left\{1,\frac{\ell}{\sqrt{2\nu\mathcal A_{s,t}}}\right\}
                        \|g\|_1 .\quad}
 \tag{SP.11}
\]
这保留了小支撑、零均值输入的真实抵消。它不提供指定中心核下界，也没有声明实际 N 的原子长度均比扩散长度小。

固定 s<T，可以延到候选终端：
\[
 \mathcal A_{s,T}\ge
 \delta\exp\!\left[-2\int_s^{s+\delta}\gamma\right]>0
 \qquad(0<\delta<T-s).
 \tag{SP.12}
\]
因此无需先证明 \(\int_s^T\gamma<\infty\)。TG 的零源、有界初值辅助问题给强 L2 终端；任意 L1 初值再由有界光滑逼近及收缩得到
\(S(\cdot,s)g\in C([s,T];L^1)\)。令 t 趋于 T，SP.11 仍成立。只用
\(\mathcal A_{s,t}\ge(t-s)e^{-2\int_s^t\gamma}\) 的粗界会掩盖这一点。

如已选定可测、时间—空间绝对可和的零均值分解
\(N(s)=\sum_j\lambda_j(s)a_j(s)\)，每个小原子支于半径 \(\ell_j(s)<\pi\) 的球且 \(\|a_j(s)\|_1\le1\)，则
\[
 \|\mathcal D_{a,T}\|_1\le
 \int_a^T\sum_j|\lambda_j(s)|
 \min\!\left\{1,\frac{\ell_j(s)}{\sqrt{2\nu\mathcal A_{s,T}}}\right\}ds .
 \tag{SP.13}
\]
需要全胞大原子时，对该项只用因子1。此式的前提明确包含所选分解和可测可和性，不以未构造的最优分解作证明。经典 Hardy 预算只给无权系数总量一类控制；本轮没有给出实际源的加权长度分布。

在 NS 重标度下，\(\ell\) 除以 r、\(\mathcal A\) 除以 \(r^2\)，所以 SP.11 的比值不变。还缺 \(s\uparrow T\) 时 \(\mathcal A_{s,T}/(T-s)\) 与源原子尺度的关系，以及源响应除以 r 后的小量。固定起点的正时钟不是临界尺度的统一下界。

## 4. 同一真实解族没有把完整响应自动变成二次

使用 NE.16 的旧周期解族，记
\[
 \alpha(s)=e^{-5\nu s},\quad U_0=\sin y+\sin2z,\quad
 v_0=(-2\cos y\sin2z,\ \sin y\cos2z),\quad
 p_v=-\cos2y-\tfrac14\cos4z,
\]
\[
 u_\epsilon=(U_\epsilon,\epsilon\alpha v_0),\quad
 p_\epsilon=\epsilon^2\alpha^2p_v,\qquad
 (\partial_s-\nu\Delta_\perp+\epsilon\alpha v_0\cdot\nabla_\perp)
                  U_\epsilon=0,\quad U_\epsilon(0)=U_0 .
 \tag{SP.14}
\]
NE 已证明这是真实无外力光滑 NS。全部矩阵输入与 x 无关，故真实传播也保持 x 无关；原漂移的 \(U_\epsilon\partial_x\) 在这里精确消失，而非被擅自近似。

写 \(\bar U=e^{-\nu s}\sin y+e^{-4\nu s}\sin2z\)。由 NE 的统一高阶估计，
\(U_\epsilon-\bar U=O_{C^k}(\epsilon)\) 于每个固定有限时间段。完整源有
\(N_\epsilon=\epsilon N_1+O_{C^k}(\epsilon^2)\)，其中 N1 只有第一行，且
\[
 (N_1)_{12}
 =\alpha\{e^{-\nu s}\sin2y\sin2z+
                  e^{-4\nu s}\cos y(1+\cos4z)\}.
 \tag{SP.15}
\]
压力没有被删除：本族没有一阶压力，横向完整源块精确为
\(2\epsilon^2\alpha^2(\cos2y-\cos4z)\operatorname{diag}(1,-1)\)。

因为 \(N_0=0\)，响应的一阶项为
\(D_1(a,t)=\int_a^te^{\nu(t-s)\Delta_\perp}N_1(s)ds\)。
其第12分量的实 \(\cos y\) 系数是
\[
 J(a,t)=
 \frac{e^{-\nu t}(e^{-8\nu a}-e^{-8\nu t})}{8\nu}>0\quad(t>a),\qquad
 \widehat{(\mathcal D^\epsilon_{a,t})_{12}}(0,1,0)
 =\tfrac{\epsilon}{2}J(a,t)+O_{\nu,T}(\epsilon^2).
 \tag{SP.16}
\]
最后使用归一化复 Fourier 系数。令
\(R_D=\mathcal D^\epsilon-\epsilon D_1\)，它初值为0，满足
\[
 (\partial_t-\nu\Delta_\perp+\epsilon\alpha v_0\cdot\nabla_\perp)R_D
 =N_\epsilon-\epsilon N_1
       -\epsilon^2\alpha v_0\cdot\nabla_\perp D_1 .
\]
右端在固定高阶空间范数中为 \(O(\epsilon^2)\)；微分能量、Gronwall 和 Sobolev 嵌入给
\(\|R_D\|_{C_tC_x^k}\le C_{\nu,T,k}\epsilon^2\)。常数可依赖固定背景、周期、\(\nu,T,k\)，不依赖 epsilon，且可对 \(0\le a\le t\le T\) 统一。

任取固定 \(0<a<t_0\le t\le t_1\le T\)，J 有严格正下界；Fourier 系数由 L1 范数控制，故小 epsilon 时完整响应有一致的一阶 L1 下界。另一方面，以 \(\nabla(U_\epsilon e_1)\) 作精确秩一比较，
\[
 \int_a^t\!\!\int d(G_\epsilon)^2
 \le50\pi^3\epsilon^2\int_a^te^{-10\nu s}ds.
 \tag{SP.17}
\]
因此 \(\|\mathcal D_{a,t}\|_1\le C\int_a^t\int d(G)^2\) 这种无初值、耗散、背景耦合或其他补偿的纯二次界，对该共同光滑族不成立。C 即使依赖固定背景和共同光滑上界，也不能消除阶数差。

反检范围必须保留：D1 只有第一行，本身秩至多一。它不否定扣除该方向的投影、参考补偿或原耗散吸收，也不是一阶压力交换子的反例。所有轨道都光滑，不构成奇性。本段是将旧 NE 轨道代入新待检表达式，不另计独立成果。

## 5. 下一项只检查还未支付的实际配对

本轮不继续把零均值、双时间积分或一般 Hardy 有界性本身当作临界增益。下一项具体转向 SP.10 中被全空间最大应变粗估掉的实际配对，而非再优化同一个指数。对标量伴随 h、反时 \(\tau=t-s\)，精确梯度能量式为
\[
 \frac d{d\tau}\|\nabla h(t-\tau)\|_2^2
 +2\nu\|\nabla^2h(t-\tau)\|_2^2
 =2\int \nabla h\cdot\operatorname{sym}G\,\nabla h .
 \tag{SP.18}
\]
下一问题是：在同一实际 NS 轨道上，原梯度形状耗散和兼容性是否能控制这个配对，并保留足以用于源响应的尺度信息。

标准 Hölder、三维插值和 Young 只把右端控制为
\(\delta\nu\|\nabla^2h\|_2^2+
 C_\delta\nu^{-3}\|G\|_2^4\|\nabla h\|_2^2\)；
\(\nabla h\) 的周期均值为零，故可用齐次插值。基本能量没有支付 \(\int\|G\|_2^4dt\)，不能重做此步便算进展。拟检验必须保留原零集耗散、截止和时间端点，不能把任意参考的相对耗散换成原耗散；VR 已显示这种替换会遗漏径向项。候选测试已经具体选定，新的控制尚未证明。

## 6. 实际来源、审读和保存范围

主任务全文读 NE、IDC、VR，重读 TG 的线性引理与 Fourier 强迹段，定向读 MPS 1–155、SN 1–90、LK 180–末以及旧 physical-adjoint-shear 全文作范围去重。LT 为本轮起点，已核其冻结哈希。A 独立核时间交换子、零模、差分核和 Fourier 界；B 独立核有效时钟、Bernstein、L1 抵消及候选终端极限；C 全文读 NE、LT并独立算真实响应及余项。最终主稿实际审读另记检查点。全部为参与式 AI 核查，不是真人同行评审。

两项普通检索后，主任务定向读 [Bernicot–Keraani，arXiv:1204.6008v1](https://arxiv.org/html/1204.6008v1) 的导言、Theorem1/Corollary1、几何引理、Theorem2证明及输运应用相关段：经典全空间体积保持双 Lipschitz 组合的 BMO/Hardy 成本可以是 \(\log K\)。因此不能把本稿粗指数估计说成必然最优。没有据此认证周期黏性推广、随机流表示或原 NS 的畸变控制，也没有采用该文未审查的其他结果。未做 Deep Research、全面查新或第三方 PDF 归档。

仅保存内部推导和检查点；无仿真、DGX、数值证书、科学附图、HTML/PDF、翻译、新recap、release或发布交接。既有 TG 独立冻结与一次移交不变，不检查发布或反向执行。
