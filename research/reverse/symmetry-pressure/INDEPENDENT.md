# 双对称类的局部速度资料与周期压力：独立证明

2026-09-08。PRIVATE_CORE。**独立稿，待非作者审查。合同命题的否定见证及真实初始演化接口已在下文闭合；NO-CANDIDATE / NOT CLAY。**

本稿先全文读本目录 CONTRACT.md，形成时没有读取本目录 PROOF.md 或以后主审。根在合同前的有限群与周期核预检、临时压力前号的纠正，均已由合同披露；本稿不是全盲预注册。合同第3节随后澄清未求值常数与数值证书的区别，我已全文重读修订后的合同并绑定最终字节。

我写过本项历史预检、纯支撑独立稿和旧 SBI，并参与过其它非作者审查。这些身份不构成本项第三路证明。以下使用一个本身置换等变的局部无散场，作两端分离的奇性配对；不采用旧外环的实际参数，也不将某个未核的群平均视为非零。

## SPI.1 固定对象与准确结论

固定任意 \(\nu>0\)，固定 \(\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3\)，无外力。令 \(X\) 是合同的光滑、实值、无散、零均值初值类，并对每个坐标置换 \(P\) 要求
\[
 a(Px)=Pa(x),\qquad a(-x)=-a(x).
 \tag{SPI.1}
\]
压力采用唯一零均值规范
\[
 -\Delta p_a=\partial_i\partial_j(a_i a_j),\qquad
 h[a]=\partial_1\partial_2p_a(0).
 \tag{SPI.2}
\]

下面证明存在 \(a,b\in X\)，二者在原点一个共同邻域内都为零，但
\[
 h[a]=0,\qquad h[b]>0.
 \tag{SPI.3}
\]
各自的同数据完整 NS 解在一个共同正窗口内满足
\[
 \beta_b(t)-\beta_a(t)=dt+r(t),\qquad
 d=-h[b]<0,\qquad \frac{|r(t)|}{t}\longrightarrow0,
 \quad \beta_c(t)=\partial_2u^c_1(0,t).
 \tag{SPI.4}
\]
这只给一个共同局部资料类的否定见证，不是所有局部资料类、任意压力值或两种符号的实现。全部参数只通过严格存在性不等式固定，不选实际数字初值、频率或时刻。

## SPI.2 双对称下的真实张量与梯度方程

先对任何属于该类的实际经典解核清结构。对正交整数矩阵 \(R=\pm P\)，令
\[
 u^R(x,t)=R\,u(R^Tx,t),\qquad p^R(x,t)=p(R^Tx,t).
 \tag{SPI.5}
\]
\(R\) 是固定标准环面的自同构，保测度、Euclidean Laplacian、散度以及完整对流作用。链式法则直接把完整 NS 方程变成同一个固定 \(\nu\) 的方程。压力 Poisson 方程及零均值规范也保持。若初值满足 SPI.1，则 \(u^R\) 与 \(u\) 有同一个初值；下文所用完整局部解的唯一性保证两者相同。由零均值压力的唯一性，还有 \(p(Rx,t)=p(x,t)\)。

因此 \(u(0,t)=0\)。记
\[
 A(x,t)=\nabla u(x,t),\quad A_{ij}(x,t)=\partial_j u_i(x,t),\qquad
 A(t)=A(0,t),\qquad
 H(x,t)=\nabla^2p(x,t),\qquad H(t)=H(0,t).
\]
对所有置换 \(P\)，有 \(AP=PA\) 和 \(P^THP=H\)。指标对在置换下只有对角、非对角两类，所以 \(A\) 的全部对角项相同，全部非对角项相同。散度为零使对角项为零。定义
\[
 S=
 \begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix},
 \qquad A=\beta S,\qquad S^2=2I+S.
 \tag{SPI.6}
\]
这个矩阵结构已有文献与本地入口；这里仅在当前环面规范下核对，不作新颖性声明。旧 Miller 记号的 \(\lambda=-\beta\)。

完整梯度微分不涉及除以 \(|u|\)。逐项对 NS 求 \(\partial_j\)，得到
\[
 (\partial_t+u\cdot\nabla-\nu\Delta)A_{ij}
 =-(\partial_j u_\ell)(\partial_\ell u_i)-\partial_{ij}p
 =-(A^2)_{ij}-H_{ij}.
 \tag{SPI.7}
\]
由取迹的 Poisson 关系，
\(\operatorname{tr}H=-\operatorname{tr}(A^2)=-6\beta^2\)。
压力 Hessian 的对角项也全相同，故
\[
 H=-2\beta^2I+hS,\qquad h=\partial_{12}p(0,t).
 \tag{SPI.8}
\]
压力的共同非对角项并未由迹决定。

\(\Delta A(0,t)\) 同样与所有置换交换，迹为
\(\Delta\operatorname{div}u(0,t)=0\)，所以记
\[
 \Delta A(0,t)=\gamma(t)S,\qquad
 \gamma(t)=\Delta\partial_2u_1(0,t).
\]
原点是停滞点，SPI.7–8 因而给出精确标量式
\[
 \boxed{\beta'=\nu\gamma-\beta^2-h.}
 \tag{SPI.9}
\]
对称性没有删除 \(\nu\gamma\)，也没有自动支付 \(h\)。这是完整方程的重写，不是闭合增长律。

## SPI.3 一个自身置换等变的局部无散场

令
\[
 e=\frac{(1,1,1)}{\sqrt3},\qquad |e|=1.
\]
这是由坐标置换固定的标准轴方向，不是新的数值初值参数。固定任意非零实径向
\(\psi\in C_c^\infty(B_1(0)\subset\mathbb R^3)\)，不指定实际函数样本。定义
\[
 w(z)=\nabla\partial_e\psi(z)-e\,\Delta\psi(z)
     =\nabla\times\nabla\times(\psi e).
 \tag{SPI.10}
\]
由导数交换，\(\operatorname{div}w=0\)。每分量是紧支撑函数的二阶导数之和，故 \(\int_{\mathbb R^3}w=0\)。该场实值、光滑，支撑在 \(B_1\) 内，且因 \(\psi\) 为偶函数而有 \(w(-z)=w(z)\)。

对于每个坐标置换 \(P\)，径向性给
\[
 \nabla^2\psi(Pz)=P\nabla^2\psi(z)P^T,\qquad
 \Delta\psi(Pz)=\Delta\psi(z),\qquad Pe=e.
\]
代入 SPI.10 得
\[
 w(Pz)=Pw(z).
 \tag{SPI.11}
\]
两次旋度的写法只是定义的等价表达；证明 SPI.11 使用实际 Hessian 变换，未在含反射的置换下误用单次旋度的轴向量符号。

为核清 \(w\) 的非零性及应力矩，定义
\[
 T_{ijkl}=\int_{\mathbb R^3}
          \partial_{ij}\psi\,\partial_{kl}\psi,\qquad
 \kappa=\frac1{15}\int_{\mathbb R^3}(\Delta\psi)^2>0.
 \tag{SPI.12}
\]
\(\kappa>0\)：否则 \(\Delta\psi=0\)，分部积分给 \(\nabla\psi=0\)，再由紧支撑得 \(\psi=0\)，矛盾。

两次分部积分使 \(T\) 关于四个指标完全对称。径向性使其四次齐次型 \(T(v,v,v,v)\) 只依赖 \(|v|\)，所以由多项式极化
\[
 T_{ijkl}=\kappa
   (\delta_{ij}\delta_{kl}+\delta_{ik}\delta_{jl}
                       +\delta_{il}\delta_{jk}).
 \tag{SPI.13}
\]
系数由 \(\sum_{i,j}T_{iijj}=\int(\Delta\psi)^2=15\kappa\) 核定。这是 Euclidean 局部种子的积分恒等式，不是假定整个环面具有任意旋转对称，也没有执行张量数组计算。

记 \(M=\int w\otimes w\)。SPI.13 分别给
\[
 \begin{aligned}
 \int(\nabla\partial_e\psi)\otimes(\nabla\partial_e\psi)
    &=\kappa(I+2e\otimes e),\\
 \int(\nabla\partial_e\psi)\,\Delta\psi&=5\kappa e,\\
 \int(\Delta\psi)^2&=15\kappa .
 \end{aligned}
\]
完整展开两个交叉项，于是
\[
 \boxed{M=\kappa(I+7e\otimes e),\qquad
        J:=\int|w|^2=10\kappa>0.}
 \tag{SPI.14}
\]

## SPI.4 两端奇性配对及精确交叉应力

对待固定的符号 \(\eta\in(0,1/2)\)，先在 \(\mathbb R^3\) 定义
\[
 v_\eta(y)=\eta^{-3/2}
 \left[w\!\left(\frac{y-e}{\eta}\right)
       -w\!\left(\frac{y+e}{\eta}\right)\right].
 \tag{SPI.15}
\]
两块支撑分别在 \(B_\eta(e)\)、\(B_\eta(-e)\)，严格分离，且全部落在
\[
 1-\eta\le |y|\le1+\eta.
 \tag{SPI.16}
\]
所以两个块的二次交叉应力逐点为零，不是估计为小。由于 \(w\) 为偶函数且 \(Pe=e\)，
\[
 v_\eta(-y)=-v_\eta(y),\qquad
 v_\eta(Py)=Pv_\eta(y).
 \tag{SPI.17}
\]
它无散、实值、光滑、紧支撑、积分为零，并有
\[
 \int|v_\eta|^2=2J=20\kappa.
 \tag{SPI.18}
\]
这里不需要对不同置换像的重叠作假设，因为每一个局部块已经具有所需置换等变性。

## SPI.5 自由空间主项的严格非零界

只为比较周期核的局部主部，定义
\[
 \Phi(y)=\frac1{4\pi|y|},\qquad
 K(y)_{abij}=\partial_a\partial_b\partial_i\partial_j\Phi(y)
 \quad(y\ne0).
\]
相应自由空间压力为
\(p^E_{v_\eta}=\partial_i\partial_j\Phi*(v_{\eta,i}v_{\eta,j})\)；
该正号与 \(-\Delta\Phi=\delta_0\) 一致。由于源远离原点，原点 Hessian 是普通核积分，没有局部奇异积分或 delta 项。

由 SPI.15 的支撑分离、\(K\) 的偶性和 \(w\) 的偶性，精确有
\[
 H^E_\eta:=\nabla^2p^E_{v_\eta}(0)
       =2\int K(e+\eta z):(w(z)\otimes w(z))\,dz.
 \tag{SPI.19}
\]
冒号只收缩应力指标 \(i,j\)，输出保留 \(a,b\)。没有漏掉两端之一，也没有把压力源线性化。

核的四阶公式为
\[
 K_{abij}(y)=\frac1{4\pi|y|^5}
 \bigl[105n_an_bn_in_j
 -15(\delta_{ab}n_in_j+\delta_{ai}n_bn_j+\delta_{aj}n_bn_i
       +\delta_{bi}n_an_j+\delta_{bj}n_an_i+\delta_{ij}n_an_b)
 +3(\delta_{ab}\delta_{ij}+\delta_{ai}\delta_{bj}
                              +\delta_{aj}\delta_{bi})\bigr],
 \quad n=y/|y|.
 \tag{SPI.20}
\]
这与实际读取的旧周期外压来源中的 Newtonian 主核一致。在 \(y=e\) 上，
\[
 K(e):I=0,\qquad
 K(e):(e\otimes e)=\frac{-12I+36e\otimes e}{4\pi}.
 \tag{SPI.21}
\]
第一式是原点外 \(\Delta\Phi=0\)；第二式逐项收缩 SPI.20，分别得到 \(105e\otimes e\)、\(-15I-75e\otimes e\)、\(3I+6e\otimes e\)。

故 SPI.14 给主项
\[
 H_*:=2K(e):M
 =\frac{14\kappa}{4\pi}(-12I+36e\otimes e)
 =\mu_*S,\qquad
 \boxed{\mu_*=\frac{42\kappa}{\pi}>0.}
 \tag{SPI.22}
\]
指定混合分量为正；不是仅用整个矩阵范数非零替代。

为了严格支付局部化误差，定义有限常数
\[
 C_5=\sup_{|y-e|\le1/2}\|\nabla K(y)\|_F<\infty,\qquad
 J_1=\int |z|\,|w(z)|^2\,dz<\infty.
\]
此紧球远离原点。均值定理和完整张量 Cauchy–Schwarz 给
\[
 \boxed{\|H^E_\eta-H_*\|_F\le2\eta C_5J_1.}
 \tag{SPI.23}
\]
因此可以并从此固定一个符号 \(\eta\in(0,1/2)\)，满足
\[
 2\eta C_5J_1\le\mu_*/4.
 \tag{SPI.24}
\]
正右端与有限左端系数保证存在性，不除以可能为零的误差常数。于是
\[
 (H^E_\eta)_{12}\ge3\mu_*/4>0.
 \tag{SPI.25}
\]
没有未估的 \(O(\eta)\)，也没有数值评价 \(C_5,J_1,\eta\)。

## SPI.6 完整周期修正及一份固定比较数据

周期 Green 分布按旧来源固定为
\[
 -\Delta G=\delta_0-(2\pi)^{-3},\quad \int_{\mathbb T^3}G=0,
 \qquad G=\Phi+Q_G\quad (0<|x|\le1),
 \tag{SPI.26}
\]
其中 \(Q_G\) 在 \(|x|\le1\) 光滑。实际读取的 exterior-pressure §2 已给周期热核减自由热核的积分表示及各阶可微性，故可用其有限常数
\[
 M_Q=\sup_{|x|\le1}\|\nabla^4Q_G(x)\|_F<\infty.
 \tag{SPI.27}
\]
全文压力恢复使用 Lebesgue 卷积：
\[
 p_c=\partial_i\partial_jG*(c_i c_j),\qquad
 \nabla^2p_c(0)=\int\nabla^4G(-x):(c(x)\otimes c(x))\,dx
 \tag{SPI.28}
\]
当 \(c\) 的支撑远离原点时，后一式为普通积分。没有体积归一化因子或额外负号。

保持已经固定的 \(\eta\)，对符号 \(\rho>0\) 定义
\[
 b_\rho(x)=v_\eta(x/\rho)
 \tag{SPI.29}
\]
于基本立方体，并在支撑之外置零后周期延拓。先要求
\[
 \rho(1+\eta)<\min\{1,\pi\}.
 \tag{SPI.30}
\]
支撑因而严格位于周期基本立方体内部，所有边界拼接光滑；它仍有 SPI.1 的全部对称与无散、零均值、实值资格。它在 \(B_{\rho(1-\eta)}(0)\) 上恒零，且
\[
 \int_{\mathbb T^3}|b_\rho|^2\,dx
       =20\kappa\rho^3.
 \tag{SPI.31}
\]
这里的积分未归一化，未把 \((2\pi)^3\) 隐入压力常数。

自由空间四阶核的齐次次数为 \(-5\)，故由 SPI.28 的变量代换，
\[
 \nabla^2p_{b_\rho}(0)=\rho^{-2}H^E_\eta+\mathcal E_\rho,\qquad
 \boxed{\|\mathcal E_\rho\|_F
             \le20\kappa M_Q\rho^3.}
 \tag{SPI.32}
\]
完整二次应力仍由两块之和组成，缩放不重新产生交叉项。周期修正是整个 \(Q_G\) 的贡献，不是只保留有限像点。

现在可以并从此固定一个符号 \(\rho>0\)，同时满足 SPI.30 及
\[
 20\kappa M_Q\rho^5\le\mu_*/4.
 \tag{SPI.33}
\]
所有系数有限且 \(\mu_*>0\)，故这两个严格几何/误差要求相容。由 SPI.25、SPI.32–33，
\[
 \boxed{h[b_\rho]\ge\frac{\mu_*}{2\rho^2}>0.}
 \tag{SPI.34}
\]

最终取 \(a=0\)、\(b=b_\rho\)。二者属于 \(X\)，在同一个开球
\(B_{\rho(1-\eta)}(0)\) 上完全相同，因而全部局部速度导数一致；
但 \(p_a=0\) 而 SPI.34 成立。这证明 SPI.3。

参数固定顺序为：任意非零径向 \(\psi\)，随后按 SPI.24 固定 \(\eta\)，再按 SPI.30、SPI.33 固定 \(\rho\)。以后不使它们随时间变化。局部化极限只用于证明存在这份固定数据；没有把 \(\eta\) 或 \(\rho\) 变化的一族场视为一条实际 NS 轨道。

## SPI.7 各自同数据的完整 NS 局部解

对上述已固定的 \(b\)，所有 Wiener 范数
\[
 \|b\|_{\mathcal A_m}
 =\sum_{k\in\mathbb Z^3}(1+|k|)^m|\widehat b_k|,
 \qquad
 \widehat b_k=(2\pi)^{-3}\int_{\mathbb T^3}b(x)e^{-ik\cdot x}\,dx
\]
均有限。这里不要求有限 Fourier 支撑，也不作 Galerkin 截断。

直接使用本轮实读 SAL §§1–2、§4：对于无散第一输入，完整有序算子
\[
 B(f,g)_k=-i\left(I-\frac{k\otimes k}{|k|^2}\right)
       \sum_{r+s=k}(\widehat f_r\cdot s)\widehat g_s,\quad k\ne0,
 \qquad B(f,g)_0=0
 \tag{SPI.35}
\]
满足
\[
 \|e^{\nu\tau\Delta}B(f,g)\|_{\mathcal A_m}
 \le(\nu\tau)^{-1/2}
          \|f\|_{\mathcal A_m}\|g\|_{\mathcal A_m}.
\]
若 \(\mathcal B=\|b\|_{\mathcal A_1}>0\)，该来源的完整收缩构造给出一个充分窗口
\[
 T_{\rm loc}=\frac{\nu}{256\mathcal B^2}>0
 \tag{SPI.36}
\]
及唯一真实 mild 解
\[
 u^b(t)=e^{\nu t\Delta}b+
       \int_0^te^{\nu(t-s)\Delta}B(u^b(s),u^b(s))\,ds.
 \tag{SPI.37}
\]
这是由已知固定初值的范数定义的解析窗口，不是数值求解或已求值时间证书。

SAL §4 的高阶 tame 权重迭代给同一个窗口上各 \(\mathcal A_m\) 连续性，方程再给时间正则。因此这里特别有
\[
 u^b\in C_t\mathcal A_3\cap C^1_t\mathcal A_1.
 \tag{SPI.38}
\]
更高阶光滑性也由该入口保持。压力按 SPI.2、SPI.28 完整恢复；非零 Fourier 压力系数为
\[
 \widehat p_k=-\frac1{|k|^2}
       \sum_{r+s=k}(k\cdot\widehat u_r)(k\cdot\widehat u_s),
 \quad \widehat p_0=0,
\]
所以这确为同数据无外力 NS，而非仅满足压力 Poisson 的静态族。

零初值 \(a=0\) 的解 \(u^a=0\) 全局光滑，压力为零，不在零范数上使用 SPI.36。二者至少具有共同窗口 \([0,T_{\rm loc}]\)。SPI.5 的实际方程变换及同数据唯一性将两种对称传给各自的整个窗口；没有在任意正时间删除其它频率、二次反馈或改变极化。

## SPI.8 初始应变差及严格时间小量

对 \(c=a,b\)，由 SPI.38，\(\beta_c(t)=\partial_2u^c_1(0,t)\) 在初始端点右侧属于 \(C^1\)。因为两个初值在共同邻域为零，
\[
 \beta_a(0)=\beta_b(0)=0,\qquad
 \gamma_a(0)=\gamma_b(0)=0.
 \tag{SPI.39}
\]
这里 \(\gamma_c=\Delta\partial_2u^c_1(0,t)\)，其初值一致由完整邻域相同支付，不是仅由中心奇性支付。把 SPI.39 代入完整式 SPI.9，
\[
 \boxed{d:=\beta_b'(0+)-\beta_a'(0+)
          =-h[b]+h[a]=-h[b]<0.}
 \tag{SPI.40}
\]
固定正黏性没有被舍弃；其初始贡献在这份比较中精确相同。后续 \(\gamma_c(t)\)、压力和所有作用仍属于真实演化。

令
\[
 r(t)=\int_0^t
   [\beta_b'(s)-\beta_a'(s)-d]\,ds .
 \tag{SPI.41}
\]
则
\[
 \beta_b(t)-\beta_a(t)=dt+r(t),\qquad
 \frac{|r(t)|}{t}
 \le\sup_{0\le s\le t}
       |\beta_b'(s)-\beta_a'(s)-d|
 \longrightarrow0.
 \tag{SPI.42}
\]
因此存在依赖这份固定数据和 \(\nu\) 的
\(\delta\in(0,T_{\rm loc})\)，对 \(0<t<\delta\) 有
\[
 |r(t)|\le\frac{|d|}{2}t,\qquad
 \beta_b(t)-\beta_a(t)\le-\frac{|d|}{2}t<0.
 \tag{SPI.43}
\]
时间小量 SPI.42 与空间局部化误差 SPI.23、周期误差 SPI.32 是三件分别支付的事。没有未经估计的时间 \(O(t^2)\)、显式数值 \(\delta\) 或统一于所有数据的非零窗口。初值在原点邻域为零，不表示正时间仍在该邻域为零；SPI.43 正说明当前局部应变随真实解发生变化。

## SPI.9 来源、独立性与停止范围

本轮实际读取及哈希如下，路径相对于 /Users/kasifa/Documents/Math/navier-stokes-reverse/：

| 来源 | 实际阅读范围 | SHA-256 |
|---|---|---|
| research/reverse/symmetry-pressure/CONTRACT.md | 初读全文；第3节措辞澄清后再次全文读最终合同 | be413616aa81f63f6bf7584c7dc41926fc721f8c845278df4164edc6f39d0124 |
| research/reverse/exterior-pressure/PROOF.md | 本轮全文；只用完整周期 Green、四阶主核与光滑修正入口，不用旧实际外环参数 | 50df7a60076567acac9cbad6588132c3e0f49e77f84f17ee68e740a8a32478b9 |
| research/reverse/reconnection-preflight/SOURCE_ATTRIBUTION_LEMMA.md | 本轮复读第1–114行（§§1–2）及第173–225行（§4） | d22bcca237977647b54ebbe13288c63a24a7c610a52a7c2265f4e3cfe366607a |
| research/reverse/symmetry-pressure-preflight/PREFLIGHT.md | 本人前轮全文自读停改稿，本轮核哈希后沿用历史范围；不是新的独立外文认证 | abf66039c0c6d158d88c3b293c7bffbd93d9ebc043a327fe357dc9f84f867150 |

原点梯度形状、完整梯度方程和周期核的一般非局部性质均有先前来源；本稿不主张外部新颖性。本轮没有新读外部原文，没有科学程序、数组执行、实际数字初值、参数扫描、Git、外部消息或发布。只在此独占稿写入。

闭合的有限结论是：即使保留全部置换等变和中心奇性，原点一个邻域的完整初始速度也不决定指定周期混合压力分量及原点应变的初始时间导数。两个比较数据分别产生各自固定的完整 NS 解，不能拼接、轮换或重置为一条轨道。它不排除非局部闭合、特殊轨道、长期增长律、一般奇性机制，也没有付出第二代供给、统一迭代、固定初值无限尺度、跨代误差或有限总时间。此精确局部闭合检验到此停止，不继续扩展同类静态变体。
