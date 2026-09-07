# 外部压力 Hessian 的能量界与静态锐性见证

PRIVATE_CORE。2026-09-07。DERIVATION_DRAFT；待另一次独立审查，不是已冻结成果或动力学候选。

结论先行：只凭固定总能量，\(d(\rho)\gg\rho^{4/5}\) 能保证 \(\rho^4H_{\rm ext}\to0\)。\(d/\rho\to\infty\) 不足以保证这一点。以下用固定光滑无散外环形状给出同阶压力和所需探针符号的静态见证。它没有实现同一 NS 解中的外场生成、输运或持留。

## 1. 完整周期压力分解

记 \(V=(2\pi)^3\)，采用归一化速度范数
\[
 \|u\|_2^2=V^{-1}\int_{\mathbb T^3}|u|^2dx,
 \qquad E_0=\|u_0\|_2.
\]
对固定初值的无外力真实光滑解，\(\|u(t)\|_2\le E_0\)。以下所有核卷积则使用 Lebesgue 测度，因而显式保留 \(V\) 因子。

周期 Green 分布满足
\[
 -\Delta G=\delta_0-V^{-1},\qquad \int G=0.
\]
完整压力为
\[
 p=\partial_i\partial_jG*(u_i u_j),
 \qquad -\Delta p=\partial_i\partial_j(u_i u_j).
 \tag{1}
\]
这与完整 Leray 投影相容；Fourier 中的非零压力系数为
\(-k_i k_j\widehat{u_i u_j}(k)/|k|^2\)。特别地，(1) 前面没有额外负号。

以 \(r(z)\) 表示到原点的周期距离。取 \(0<d<1/4\)，令
\(F_{ij}^{\rm ext}=\mathbf1_{r\ge d}u_i u_j\)。定义
\[
 p_{\rm ext}=\partial_i\partial_jG*F_{ij}^{\rm ext}.
\]
由于该应力与原点距离至少 \(d\)，原点附近压力光滑，且
\[
 (H_{\rm ext})_{ab}
 =\int_{r(z)\ge d}
 \partial_a\partial_b\partial_i\partial_jG(-z)
 u_i(z)u_j(z)\,dz.
 \tag{2}
\]
硬截断应力的分布导数已包含在定义中；(2) 是将全部微分留在核上的写法，不曾丢弃边界项。\(p=p_{\rm int}+p_{\rm ext}\) 是源项的精确线性分解；两部分不因此成为独立的 NS 解。

## 2. 严格周期核界

令 \(\Phi(z)=1/(4\pi|z|)\)。在 \(|z|\le1\) 上，\(Q_G=G-\Phi\) 光滑。一个直接可验证的定义是
\[
 Q_G(z)=\int_0^1\left[\sum_{n\ne0}K_{\mathbb R}(s,z+2\pi n)-V^{-1}\right]ds
 +\int_1^\infty[K_{\mathbb T}(s,z)-V^{-1}-K_{\mathbb R}(s,z)]ds,
\]
其中
\(K_{\mathbb R}(s,z)=(4\pi s)^{-3/2}e^{-|z|^2/(4s)}\)，
\(K_{\mathbb T}=\sum_nK_{\mathbb R}(s,z+2\pi n)\)。短时段中非零像点的距离一致有正下界，长时段中周期非零 Fourier 模态指数衰减、自由热核各阶导数可积。因此该积分可逐阶微分。完整论证也已写于 `../next-concentration/DERIVATION_DRAFT.md` 的 Green 核段落。

记四阶核张量
\(\mathcal K(z)_{abij}=\partial_a\partial_b\partial_i\partial_jG(z)\)，定义
\[
 C_G=\sup_{z\ne0}r(z)^5\|\mathcal K(z)\|_F<\infty.
 \tag{3}
\]
其有限性来自：原点附近 \(\nabla^4\Phi\) 齐次次数为 \(-5\)，\(\nabla^4Q_G\) 有界；远离原点则是周期紧集上的光滑函数。周期距离在基本立方体边界不可微不影响这里只作权重的上确界。

用 \(\|u\otimes u\|_F=|u|^2\)，(2) 给
\[
 \|H_{\rm ext}\|_F
 \le C_G\int_{r\ge d}r(z)^{-5}|u(z)|^2dz
 \le V C_G d^{-5}e_{\rm ext}^2
 \le V C_G E_0^2d^{-5},
 \tag{4}
\]
其中 \(e_{\rm ext}^2=V^{-1}\int_{r\ge d}|u|^2\)。这是整个周期外部应力的估计，没有把核直接换成全空间核。

若有更精确的能量分布，可保留 (4) 第一项，或对壳层 \(2^jd\le r<2^{j+1}d\) 分组。仅有总能量界时不能额外假设这些壳层能量趋零到所需速率。

## 3. 归一化后的临界距离

内区长度记为 \(\rho\downarrow0\)。由 (4)，
\[
 \|\rho^4H_{\rm ext}\|_F
 \le V C_G E_0^2\frac{\rho^4}{d(\rho)^5}.
 \tag{5}
\]
所以
\[
 \frac{d(\rho)}{\rho^{4/5}}\longrightarrow\infty
 \quad\Longrightarrow\quad \rho^4H_{\rm ext}\longrightarrow0.
 \tag{6}
\]
\(d/\rho\to\infty\) 比 (6) 弱。对 \(d=\rho^\gamma\)、\(0<\gamma<1\)，前者总成立，而 (5) 中的比值为 \(\rho^{4-5\gamma}\)：\(\gamma<4/5\) 时趋零，\(\gamma=4/5\) 时同阶，\(4/5<\gamma<1\) 时该总能量上界甚至不再有界。

这只是由总能量作统一保证的条件。个别真解的外场可能有额外抵消或更小的近场能量，从而在更弱距离条件下也可忽略。下面的锐性只排除从总能量界单独推出这种改进。

## 4. 一次固定的光滑无散外环形状

取
\[
 b=(0,3/2,0),\qquad \varepsilon=1/20,
 \qquad \psi(y)=h(\varepsilon^2-|y-b|^2),
\]
其中 \(h(s)=e^{-1/s}\) 对 \(s>0\)，否则为0。令
\[
 W(y)=\nabla\times(\psi(y)e_2)
 =(-\partial_3\psi,0,\partial_1\psi).
 \tag{7}
\]
该场实值、光滑、紧支撑、无散、均值为零，且不恒为零。其支撑位于
\[
 29/20\le |y|\le31/20,
\]
从而包含在固定外环 \(1<|y|<2\)。记
\[
 J_W=\int|W|^2dy>0,
 \qquad
 p_W^{\mathbb R^3}=\partial_i\partial_j\Phi*(W_iW_j),
 \qquad H_W=\nabla^2p_W^{\mathbb R^3}(0).
\]
因为源项离原点有正距离，这个 Hessian 是普通核积分。

### 非零性与符号的显式检验

四阶 Newtonian 核可直接微分得到
\[
 \partial_{ijkl}\Phi(y)=\frac1{4\pi|y|^5}
 \left[105n_in_jn_kn_l
 -15(\delta_{ij}n_kn_l+\delta_{ik}n_jn_l+\delta_{il}n_jn_k
 +\delta_{jk}n_in_l+\delta_{jl}n_in_k+\delta_{kl}n_in_j)
 +3(\delta_{ij}\delta_{kl}+\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk})\right],
\]
其中 \(n=y/|y|\)。对 \(i,j\in\{1,3\}\)，令 \(s=n_2^2\)，则横向块为
\[
 (\partial_{22ij}\Phi)_{i,j\in\{1,3\}}
 =\frac1{4\pi|y|^5}
 \left[(105s-15)n_\perp\otimes n_\perp+(3-15s)I_2\right].
 \tag{8}
\]
在 (7) 的支撑上，
\[
 1-s\le(1/29)^2<1/100.
\]
因此 \(105s-15>0\)，(8) 中括号的最大特征值不超过
\[
 3-15s+(105s-15)(1-s)
 =-12+105s(1-s)
 \le-12+105/100<-10.
\]
又因 \(W_2=0\)，得到严格符号界
\[
 \eta:=(H_W)_{22}
 \le-\frac{10}{4\pi}\left(\frac{20}{31}\right)^5J_W<0.
 \tag{9}
\]
四阶核在 \(y\mapsto-y\) 下为偶函数，所以 (9) 与 Hessian 积分中的 \(-y\) 一致。

场 (7) 在绕 \(e_2\) 的旋转下协变，因此其压力在该旋转下不变。原点处 Hessian 必为 \(\operatorname{diag}(a,\eta,a)\)。外场在原点邻域为零，压力在那里调和，故 \(2a+\eta=0\)。所以
\[
 H_W=\operatorname{diag}(-\eta/2,\eta,-\eta/2).
 \tag{10}
\]
对前项使用的 \(D=\operatorname{diag}(5,-8,3)\)，
\[
 D:H_W=-12\eta>0.
 \tag{11}
\]
这个符号可以抵消旧探针中的负标量贡献；它不等于匹配整个压力 Hessian。

## 5. 固定能量静态缩放与周期余项

固定 \(e_*>0\)。对充分小的 \(d\)，定义一个瞬时周期场
\[
 v_d(x)=\frac{\sqrt V e_*}{\sqrt{J_W}}\,d^{-3/2}W(x/d).
 \tag{12}
\]
其支撑位于 \(29d/20\le r\le31d/20\)，不碰基本立方体边界，也完全位于 \(r\ge d\)。它仍实值、无散、均值为零，并严格满足
\[
 \|v_d\|_2=e_*.
\]
全空间压力的缩放给
\[
 \nabla^2p_{v_d}^{\mathbb R^3}(0)
 =\frac{Ve_*^2}{J_W}d^{-5}H_W.
 \tag{13}
\]

为保留周期压力，定义
\[
 M_G=\sup_{|z|\le1}\|\nabla^4Q_G(z)\|_F<\infty.
\]
对 \(d<1/4\)，整个应力支撑都在此球内。同一压力差核论证给
\[
 \left\|H_{\rm ext}[v_d]
 -\frac{Ve_*^2}{J_W}d^{-5}H_W\right\|_F
 \le M_G\int|v_d|^2dx
 =M_GVe_*^2.
 \tag{14}
\]
因此周期修正为一个显式常数控制的有界项，主项 \(d^{-5}\) 不会由周期效应消失。具体记 \(c_0=\frac{10}{4\pi}(20/31)^5>0\)。由 (9)、(14)，只要 \(M_Gd^5\le c_0/2\)，便有
\[
 \|H_{\rm ext}[v_d]\|_F\ge |(H_{\rm ext}[v_d])_{22}|
 \ge\frac{Ve_*^2c_0}{2}\,d^{-5}.
\]
所以仅总能量受控的光滑无散场类确实达到 (4) 的距离指数。锐性讨论假定可用能量上界为正；零能量类只有零场。

特别取 \(d=c\rho^{4/5}\)，其中固定 \(c>0\)。此时 \(d/\rho\to\infty\)，但
\[
 \rho^4H_{\rm ext}[v_d]
 \longrightarrow\frac{Ve_*^2}{J_Wc^5}H_W\ne0.
 \tag{15}
\]
其与 \(D\) 的配对为正。若仅希望这个标量极限等于20，可选
\[
 c=\left(\frac{Ve_*^2(-12\eta)}{20J_W}\right)^{1/5}>0.
 \tag{16}
\]
这里没有声称 (16) 同时抵消完整矩阵或任何其他残差分量。

甚至当 \(4/5<\gamma<1\) 时，取 \(d=\rho^\gamma\)，并在 (12) 中用
\(e_\rho=e_*\rho^{(5\gamma-4)/2}\) 替换 \(e_*\)。则外场能量趋零、\(d/\rho\to\infty\)，但 \(\rho^4H_{\rm ext}\) 仍趋于 \((Ve_*^2/J_W)H_W\ne0\)。这再次说明需要能量与距离的联合速率，不能只说“外场能量小”。它仍使用同一个固定形状 \(W\)。

## 6. 与固定内区的静态接口及严格量词

若仅在一个瞬时把前项内场 \(\rho^{-1}U_S(x/\rho)\) 与 (12) 相加，内场支撑半径至多 \(2\rho\)，外场内半径至少 \(29d/20\)。在临界缩放 \(d=c\rho^{4/5}\) 下，两者对充分小 \(\rho\) 支撑不相交。因此应力交叉项逐点为零，压力恰好是两份压力之和，没有遗漏交叉压力。

若 \(0<e_*<E_0\)，该瞬时总场的归一化平方范数为
\[
 e_*^2+\frac{\rho}{V}\int|U_S|^2,
\]
对充分小 \(\rho\) 不超过 \(E_0^2\)。所以仅凭总能量不能排除具有 (11) 正号和同阶大小的外场压力修正。结合 (16) 也只说明旧 \(D\) 探针在瞬时压力层面可以被抵消。

这些场不是已经构造的同一 NS 解。这里证明的是：对每个小尺度，可以在允许的瞬时光滑无散函数类中写出一个场；没有证明存在一个固定初值，使真实解在相应时刻经过全部这些场。没有检查外场自身的动量残差、时间演化、可达性、稳定性或能量耗散历史。不能把这些静态缩放命名为再生或奇性候选。

## 7. 本项增量与标准内容

周期 Green 四阶核的 \(d^{-5}\) 界、Cauchy–Schwarz/能量控制及缩放锐性属于标准核估计内容，本稿不主张新颖性。这里的有界用途是明确：

- 只由总能量保证外场可忽略时，充分且在统一函数类意义下锐的距离尺度是 \(d\gg\rho^{4/5}\)，不是 \(d/\rho\to\infty\)。
- 无散性及完整压力没有消去这一最坏尺度；固定外环形状给出非零、且对旧 \(D\) 探针为正的显式见证。
- 因而前一固定紧支撑候选的失败不能直接延伸到允许真实外场同阶压力修正的合同。至于同一真实 NS 解能否产生并维持这样的外场，本项完全未证。

本稿停止于条件筛选和静态反例。仍为待审草稿，不冻结、提交或发布。
