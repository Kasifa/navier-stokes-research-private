# 两点涡量行列式：共同梯度消项及其加权演化

2026-09-07。PRIVATE_CORE。TD，内部探索中的解析记录；不是已冻结的研究小节。下列恒等式在明确的光滑范围内成立，所需的新动力学估计仍待证明。EXPLORATORY / PROVED IN STATED SCOPE / FULL GOAL OPEN / NOT CLAY。

## 1. 对象、范围与已有工作的关系

固定 \(\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3\)，考虑无外力、黏度 \(\nu>0\) 的原 Navier–Stokes 光滑解。所有推导先限制在一个闭光滑时间区间 \(I\) 上；不预先保证这些量在潜在奇异时刻前有一致界。记
\[
 A_{ij}=\partial_j u_i,\quad S=(A+A^\top)/2,\quad
 \omega=\operatorname{curl}u,\qquad
 (\partial_t+u\cdot\nabla-\nu\Delta)\omega=A\omega .
 \tag{TD.1}
\]
\(\operatorname{tr}A=0\)，且在同一点 \(A\omega=S\omega\)。以下共同矩阵与间距的消项使用完整的 \(A\)，不能只将 \(S\) 作用于另一点的涡量。

设 \(a=\omega(x),b=\omega(y)\)，在近对角局部坐标中取
\[
 r=y-x,\quad W=a\times b,\quad \Theta=W\cdot r,\quad
 \bar A=(A_x+A_y)/2,\quad \delta A=A_y-A_x,\quad \delta u=u_y-u_x,
\]
\[
 R_A=-\tfrac12[(\delta A a)\times b]+\tfrac12[a\times(\delta A b)],
 \qquad V_{\rm trap}=\delta u-\bar A r.
 \tag{TD.2}
\]
裸向量 \(y-x\) 不是全环面上的单值光滑周期函数。后文仅在 \(|r|<2R<\pi\) 的局部提升中使用它，\(x\) 周期，\(y=x+r\) 按周期评价；截断支集远离坐标接缝。\(W\) 本身才在整个 \(\mathbb T^3\times\mathbb T^3\) 上周期。

这不是从零开始的两点路线。physical_space_annular_increment_note.md §1–3 已有有符号伸长核和交换两点得到的双增量；r070a_moving_annular_balance_note.md §3，尤其式(3.3)–(3.8)，已对完整三次核分解输运、伸长、黏性和移动截断的时间导数。本次抽出 \(\Theta\) 的共同梯度消项，并计算一个平方加权量。它是旧完整恒等式内部的结构细化，尚无新颖性结论。

## 2. 两种扩散算子，不能漏掉交叉项

先在原来的独立 \(x,y\) 坐标定义
\[
 L_{\rm ind}=\partial_t+u_x\cdot\nabla_x+u_y\cdot\nabla_y
                  -\nu(\Delta_x+\Delta_y).
\]
线性代数恒等式
\[
 (Ma)\times b+a\times(Mb)=(\operatorname{tr}M\,I-M^\top)(a\times b)
\]
给出
\[
 L_{\rm ind}W=-\bar A^\top W+R_A .
 \tag{TD.3}
\]
因此仅取 \(|W|^2\) 没有消去共同应变；反应项含 \(-W\cdot\bar S W\)，没有一般符号。

因为 \(L_{\rm ind}r=\delta u\)，乘积公式给
\[
 L_{\rm ind}\Theta
 =r\cdot R_A+W\cdot V_{\rm trap}
  +2\nu\{\operatorname{div}_xW-\operatorname{div}_yW\}
 =r\cdot R_A+W\cdot V_{\rm trap}
  +2\nu\{b\cdot\operatorname{curl}a+a\cdot\operatorname{curl}b\}.
 \tag{TD.4}
\]
共同项 \(-r\cdot\bar A^\top W+W\cdot\bar Ar\) 精确抵消。这里的散度是在原独立坐标中取的。特别地，
\[
 \Theta(x,x)=0,\qquad
 (L_{\rm ind}\Theta)(x,x)=4\nu\omega\cdot\operatorname{curl}\omega.
\]
这不矛盾：独立两点 Laplacian 与限制到对角线不是可交换操作。

沿线段对 \(u(x+\sigma r)\) 用梯形积分余项，得到
\[
 V_{\rm trap}
 =-\tfrac12\int_0^1\sigma(1-\sigma)
          D^3u(x+\sigma r)[r,r,r]\,d\sigma,\qquad
 |V_{\rm trap}|\le \tfrac1{12}|r|^3\sup_{[x,y]}|D^3u|.
 \tag{TD.5}
\]
尺度因子不是免费导数控制；\(\delta A=O(|r|\sup|D^2u|)\) 仍含二阶速度导数。

另定义共同平移导数及同步算子
\[
 D_j=\partial_{x_j}+\partial_{y_j},\qquad
 L_{\rm syn}=\partial_t+u_x\cdot\nabla_x+u_y\cdot\nabla_y-\nu\sum_jD_j^2.
\]
在 \((x,r)\) 坐标中，\(D_j=\partial_{x_j}\)，输运为
\(u(x)\cdot\nabla_x+\delta u\cdot\nabla_r\)。由
\(L_{\rm syn}=L_{\rm ind}-2\nu\sum_j\partial_{x_j}\partial_{y_j}\) 及 \(D_jr=0\)，
\[
 \boxed{L_{\rm syn}\Theta
 =r\cdot R_A+W\cdot V_{\rm trap}
 -2\nu r\cdot\sum_j(\partial_j a\times\partial_j b).}
 \tag{TD.6}
\]
这是原 NS 的另一条精确恒等式，不是修改物理扩散。最后的交叉梯度源必须保留。

## 3. 加权平方量及去除内截断

固定 \(0<R<R_0\)，其中 \(R_0<\min(1,\pi/4)\)。取非负、非增的光滑径向截断 \(\chi_R(r)=\chi(|r|/R)\)，等于1于 \(|r|\le R\)，支集在 \(|r|<2R\)。对 \(0<s<1\) 定义
\[
 K_{s,R}(r)=\chi_R(r)|r|^{-5-2s},\qquad
 \mathcal A_{s,R}=\int_{\mathbb T^3}\int_{|r|<2R}K_{s,R}\Theta^2\,dr\,dx,
 \quad
 \mathcal D_{s,R}=\iint K_{s,R}\sum_j|D_j\Theta|^2 .
 \tag{TD.7}
\]
在 \(I\) 上，Taylor 展开给 \(W=O(|r|)\)，\(\Theta,D_j\Theta=O(|r|^2)\)。TD.6右端也是 \(O(|r|^2)\)：交叉梯度在对角线为 \(p\times p=0\)。所以本节积分的近零径向主阶是 \(\int_0^{2R}\rho^{1-2s}d\rho\)，对 \(s<1\) 有限。

先排除 \(|r|<\varepsilon\)，乘 \(\Theta K_{s,R}\) 后分部积分，再令 \(\varepsilon\downarrow0\)。共同导数满足 \(D_jK_{s,R}=0\)，没有扩散核导数。空间输运在 \((x,r)\) 坐标散度为零，内截断产生的输运项为 \(O(\varepsilon^{2-2s})\)；各时间导数在闭光滑区间受相同可积主界控制。得到
\[
 \boxed{\begin{aligned}
 \tfrac12\mathcal A_{s,R}'+\nu\mathcal D_{s,R}
 ={}&\iint K_{s,R}\Theta
 \left\{r\cdot R_A+W\cdot V_{\rm trap}
 -2\nu r\cdot\sum_j(\partial_j a\times\partial_j b)\right\}\\
 &+\tfrac12\iint\Theta^2\,\delta u\cdot\nabla_rK_{s,R}.
 \end{aligned}}
 \tag{TD.8}
\]
固定 \(R\) 是此式的假设；若之后选择随时间变化的 \(R\)，必须另加 \(\frac12\iint\Theta^2\partial_tK_{s,R(t)}\)，不能将固定尺度结论直接搬用。

两个容易产生错误增益的地方：

- \(\delta u\cdot r=r^\top\bar S r+O(|r|^4)\)。共同应变通过权重输运重新出现，TD.4的点态抵消不使TD.8单调。
- \(\mathcal D_{s,R}\) 只控制共同平移方向。不能未经证明每个固定 \(r\) 的 \(x\) 均值为零就用 Poincaré 控制 \(\mathcal A_{s,R}\)。

直接使用独立扩散并拆成若干无内截断积分也不安全。一般 \(\nabla_{x,y}\Theta=O(|r|)\)，所以其加权平方的形式主阶为 \(\int\rho^{-1-2s}d\rho\)，不保证有限。对应的核 Laplacian 和黏性源可能需要先合并消去对角奇性。本节同步公式避免了这种非法拆分，但没有消去交叉梯度源。

## 4. 与实际周期涡量伸长的接口

设 \(Y=\|\omega\|_2^2,\ Z=\|\nabla\omega\|_2^2\)，范数不除以胞体积。周期均值速度不影响 \(A\)。令周期 Green 函数满足
\(-\Delta G=\delta_0-(2\pi)^{-3}\)，则
\[
 u-\langle u\rangle=\operatorname{curl}(G*\omega),\qquad
 A_{i\ell}=\epsilon_{ijk}(\partial_\ell\partial_jG)*\omega_k .
 \tag{TD.9}
\]
MP记录 clay_b_expanding_torus_local_energy_20260907.md §2 已给出截断基本解加光滑周期余项的构造；在这里固定 \(L=2\pi\)，近原点 \(G=\Gamma+H\)，\(\Gamma=(4\pi|r|)^{-1}\)，\(H\) 光滑。将 \(\nabla^2G\) 分成 \(\chi_R\nabla^2\Gamma\) 与完整余核 \(B_R\)。接触项被同一个近场分布保留，故 \(B_R\) 是普通核，且
\[
 \|B_R\|_{L^2(\mathbb T^3)}\le C R^{-3/2}.
\]
证明：内球的 \(H\) 导数有界；外部的奇异部分为 \(O(|r|^{-3})\)，其平方积分从 \(R\) 起为 \(O(R^{-3})\)；其余固定胞区域光滑。不使用非绝对收敛的周期副本级数。

将TD.9与 \(a_i a_\ell\) 收缩。欧氏 Hessian 的各向同性项及接触项均含 \(\epsilon_{i\ell k}a_i a_\ell=0\)，剩下
\[
 \mathcal V=\int\omega\cdot S\omega=\mathcal V_{\rm near}+\mathcal V_{\rm rem},
 \quad
 \mathcal V_{\rm near}
 =-\frac{3}{4\pi}\iint\chi_R\frac{(a\cdot r)\Theta}{|r|^5},
 \quad
 |\mathcal V_{\rm rem}|\le C R^{-3/2}Y^{3/2}.
 \tag{TD.10}
\]
这是经典几何 Biot–Savart 核的周期近场分解，不是新的核表示。最后的余核涵盖远场、周期修正和全部固定胞区域。

Cauchy 不等式直接给
\[
 |\mathcal V_{\rm near}|\le C_s R^sY^{1/2}\mathcal A_{s,R}^{1/2},
 \qquad C_s=O(s^{-1/2})\quad(s\downarrow0),
 \tag{TD.11}
\]
因为互补积分被 \(Y\int_{|r|<2R}|r|^{-3+2s}dr\) 控制。更重要的是，同一个径向截断在交换两点后不变，\((x,r)\mapsto(x+r,-r)\) 保持局部积分域和测度，并有 \(\Theta\mapsto\Theta\)。因此保留旧记录的双增量得到
\[
 \mathcal V_{\rm near}
 =\frac{3}{8\pi}\iint\chi_R\frac{(r\cdot(b-a))\Theta}{|r|^5},
 \qquad
 |\mathcal V_{\rm near}|
 \le C_s R^{1+s}Z^{1/2}\mathcal A_{s,R}^{1/2}.
 \tag{TD.12}
\]
后一个界使用 \(\|\omega(\cdot+r)-\omega\|_2\le |r|\|\nabla\omega\|_2\)，互补积分为
\(\iint\chi_R|r\cdot(b-a)|^2|r|^{-5+2s}\le C_sR^{2+2s}Z\)。它连接了新平方量与真实 enstrophy 方程
\(\frac12Y'+\nu Z=\mathcal V\)，但没有给出 \(\mathcal A_{s,R}\) 的先验界。

## 5. 黏性组合：一个严格但有限的否定结果

把TD.8中的全部黏性贡献写为
\[
 \mathcal H_{s,R}
 =\mathcal D_{s,R}
 +2\iint K_{s,R}\Theta\,r\cdot
                   \sum_j(\partial_j a\times\partial_j b).
 \tag{TD.13}
\]
先检验遗漏零模的风险。取单模 \(\omega=(\cos kz,\sin kz,0)\)，其中 \(z=x_3\)，正整数 \(k\)，并记 \(h=r_3\)。它是零均值无散周期涡量，有光滑周期速度原像。此时
\[
 \Theta=h\sin(kh),\quad D_j\Theta=0,\quad
 r\cdot\sum_j(\partial_j a\times\partial_j b)=k^2\Theta,\qquad
 \mathcal H_{s,R}=2k^2\mathcal A_{s,R}>0.
 \tag{TD.14}
\]
因此同步耗散自身不能控制整个平方量；交叉项并非可随意抛弃的误差。

但完整 \(\mathcal H_{s,R}\) 也不总非负。取以下无外力、\(p=0\) 的真实周期NS解：
\[
 \begin{aligned}
 u(t,z)&=\left(-\alpha(t)\cos z+\tfrac{\beta(t)}2\cos2z,\
                   -\alpha(t)\sin z-\tfrac{\beta(t)}2\sin2z,\ 0\right),\\
 \omega(t,z)&=(\alpha(t)\cos z+\beta(t)\cos2z,\
                    \alpha(t)\sin z-\beta(t)\sin2z,\ 0),\\
 \alpha(t)&=e^{-\nu t},\qquad \beta(t)=\tfrac12e^{-4\nu t}.
 \end{aligned}
 \tag{TD.15}
\]
速度无散、均值为零；\(u_3=0\) 且只依赖 \(z\)，故 \(u\cdot\nabla u=0\)，而 \(\partial_tu=\nu\Delta u\)。这不是一般热流冒充NS，而是可直接代回原方程的全局光滑剪切解。令 \(\langle\cdot\rangle_z=(2\pi)^{-1}\int_0^{2\pi}\cdot\,dz\)，叉积计算给
\[
 \Theta=h\{q-2\alpha\beta\sin(h/2)\cos(3z+3h/2)\},\qquad
 q=\alpha^2\sin h-\beta^2\sin2h,
\]
\[
 \langle\Theta^2\rangle_z
 =h^2\{q^2+2\alpha^2\beta^2\sin^2(h/2)\}.
 \tag{TD.16}
\]
这里 \(R_A=0\)，\(W\cdot V_{\rm trap}=0\)。权重输运的积分也为零：\(\delta u\) 水平，\(\Theta^2\) 只依赖 \(z,h\)，径向权重的水平导数关于对应水平分离坐标为奇函数。因此TD.8恰为 \(\mathcal A'=-2\nu\mathcal H\)。直接微分TD.16，在 \(t=0\) 得
\[
 -\frac1{2\nu}\partial_t\langle\Theta^2\rangle_z
 =h^2 B(h),\qquad
 B(h)=2\sin^2h+\tfrac12\sin^22h
          +\tfrac52\{\sin^2(h/2)-\sin h\sin2h\},
\]
\[
 B(h)=(1-\cos h)P(\cos h),\qquad
 P(c)=2c^3-3c^2-3c+\tfrac{13}{4}.
 \tag{TD.17}
\]
在 \(c\in[\sqrt3/2,1]\) 上，\(P'(c)=6c^2-6c-3<0\)，且
\(P(\sqrt3/2)=(4-3\sqrt3)/4<0\)。故 \(B(h)<0\) 当 \(0<|h|\le\pi/6\)。对任意 \(0<s<1\)、上述非负径向截断以及 \(0<R\le\pi/12\) 且 \(R<R_0\)，
\[
 \boxed{\mathcal H_{s,R}(0)
 =(2\pi)^3\int K_{s,R}(r)\,h^2B(h)\,dr<0,\qquad
 \mathcal A_{s,R}'(0)>0.}
 \tag{TD.18}
\]
近零 \(h^2B(h)=O(h^4)\)，积分收敛；截断在内球为1，严格负的集合有正测度。这个解析例只排除了TD.13的普遍非负性。该解的总涡量伸长恒为零；它不构成爆破，也没有排除带有独立可控误差的估计、其他几何量或全部两点方法。

此外，梯度差、梯形余项及权重输运仍须合并估计。TD.5的高阶导数上界不能用“多出几个 \(r\)”代替时间可积性证明；既有单点 \(|\omega||\nabla(\omega/|\omega|)|^2\) 预算也没有自动控制TD.7中的四次涡量权重。是否得到临界范围内的额外控制是研究问题，不是本记录的结论。

## 6. 实际伸长核只选择第一球谐分量

TD.18中，一个不产生伸长的解也能使 \(\mathcal A\) 增长。这提示先区分真正参与TD.10配对的角向成分，而不是继续对整个 \(\Theta\) 寻找单调性。

对固定 \(x,\rho>0\)，在单位球面上令 \(n=r/\rho\)，记归一化平均 \(\langle f\rangle_{\mathbb S^2}=(4\pi)^{-1}\int_{\mathbb S^2}f\,dS\)，定义
\[
 m(x,\rho)=\langle n\Theta(x,\rho n)\rangle_{\mathbb S^2},\qquad
 (\Pi_1\Theta)(x,\rho n)=3n\cdot m(x,\rho).
 \tag{TD.19}
\]
因为 \(\langle n_i n_j\rangle=\delta_{ij}/3\)，\(\Pi_1\) 是 \(L^2(\mathbb S^2)\) 到第一球谐空间的正交投影。从TD.10直接得到
\[
 \boxed{\mathcal V_{\rm near}
 =-3\int_{\mathbb T^3}\int_0^{2R}
       \chi(\rho/R)\rho^{-2}a(x)\cdot m(x,\rho)\,d\rho\,dx.}
 \tag{TD.20}
\]
所以把TD.10中的 \(\Theta\) 换为 \(\Pi_1\Theta\) 不改变近场伸长。其余角向分量对这一配对严格为零。这是核本身给出的投影，不是正则性假设或任意权重选择。

定义
\[
 \mathcal A^{(1)}_{s,R}
 =\iint K_{s,R}|\Pi_1\Theta|^2\le\mathcal A_{s,R}.
 \tag{TD.21}
\]
TD.11仍以 \(\mathcal A^{(1)}\) 替换 \(\mathcal A\) 成立。相反，TD.12的两点交换会移动投影的中心，不能未经证明把其中的 \(\mathcal A\) 换为 \(\mathcal A^{(1)}\)。Taylor首项
\(\Theta(x,\rho n)=\rho^2 n\cdot\{a\times[(\nabla\omega)n]\}+O(\rho^3)\)
关于 \(n\) 为偶函数，故 \(\Pi_1\Theta=O(\rho^3)\)。这只改善了光滑函数的近对角阶数，没有提供高阶导数的先验界。

下一步的具体计算是对TD.6作 \(\Pi_1\) 投影，保留相对输运与投影的不交换项，再检查黏性源及其与TD.20的配对。这里尚未推导该投影动力学，也未证明投影后黏性组合具有一般符号；不能从共同导数与投影可交换，推出整个方程可交换。未完成的吸收估计保持OPEN，不因困难就宣布整个路线不可行。

## 7. 普通范数对照：没有隐藏的临界增益

缩放只作维数核验，不在固定环面上宣称任意连续伸缩都是同域对称。把周期胞及截断同时缩放，\(u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t)\)、\(R_\lambda=R/\lambda\)，则
\[
 \Theta_\lambda(x,r,t)=\lambda^3\Theta(\lambda x,\lambda r,\lambda^2t),
 \quad
 Y_\lambda=\lambda Y,\quad Z_\lambda=\lambda^3Z,\quad
 \mathcal A_{s,R/\lambda}[u_\lambda]
       =\lambda^{5+2s}\mathcal A_{s,R}[u],\quad
 \mathcal V_\lambda=\lambda^3\mathcal V.
 \tag{TD.22}
\]
TD.8各项次数均为 \(7+2s\)；TD.11、TD.12和余核界各项次数为3。这种齐次一致不是已经控制了一个临界量。

进一步，原平方量可被普通范数控制，但该上界只恢复标准伸长估计。以下取 \(0<s<1/2\)，不声称端点。因为涡量周期平均为零，Sobolev、平移差估计和 \(L^2\)–\(L^6\) 插值给
\[
 \|\omega\|_6^2\le CZ,\qquad
 \|\delta_r\omega\|_3^2
 \le\|\delta_r\omega\|_2\|\delta_r\omega\|_6
 \le C\min\{|r|Z,\sqrt{YZ}\}.
 \tag{TD.23}
\]
使用 \(|\Theta|\le |r||\omega(x)||\delta_r\omega(x)|\) 及空间 Hölder，
\[
 \mathcal A_{s,R}
 \le CZ\int_0^{2R}\rho^{-1-2s}
                     \min\{\rho Z,\sqrt{YZ}\}\,d\rho
 \le C_sY^{1/2-s}Z^{3/2+s}.
 \tag{TD.24}
\]
若 \(Y=0\)，涡量为零而结论平凡。否则 \(Z>0\)，把积分在
\(\ell=\sqrt{Y/Z}\) 分开，并分别延长到 \((0,\ell)\)、\((\ell,\infty)\)，最后一步由
\(\int_0^\ell\rho^{-2s}d\rho=\ell^{1-2s}/(1-2s)\) 和
\(\int_\ell^\infty\rho^{-1-2s}d\rho=\ell^{-2s}/(2s)\) 得到。

在TD.10、12中仅为估计瞬时 \(\mathcal V\) 选择
\(R=\min(R_0/2,\ell)\)，不用这个选择去求导TD.8。由TD.24得到
\[
 |\mathcal V|\le C_{s,R_0}Y^{3/4}Z^{3/4}.
 \tag{TD.25}
\]
当 \(R=\ell\) 时两个尺度幂直接匹配；当 \(R=R_0/2\le\ell\) 时近场不增，远场由 \(Y\le Z\) 控制。Young不等式随即只给
\(\frac12Y'+\frac{\nu}{2}Z\le C_{s,R_0}\nu^{-3}Y^3\)。
因此，不保留TD.20所选几何成分而仅使用普通 \(H^1\) 上界，并没有推进正则性。这不否定投影后的新动力学估计；它明确了该估计必须比什么更强。

## 8. 文献与证据范围

经典背景为 Constantin–Fefferman, *Direction of Vorticity and the Problem of Global Regularity for the Navier–Stokes Equations*, Indiana Univ. Math. J. 42 (1993), 775–789，[期刊条目](https://iumj.org/article/3627/)。本轮搜索结果核到题名、作者和页码，直接打开条目返回502；没有因此声称重新逐式读完原论文。TD.9–12在本地从Green核独立推导，依赖的周期Green构造已实际重读MP §2；也实际重读了上列R0.69T §1–3和R0.70A §3的相关公式。局部去重不是全球新颖性审查。

这些计算由AI研究任务完成，并由同模型协作者进行分项独立推导；不是人类同行评审。最终文件的实际审读范围另记于audit。无PDE仿真、数值证书、DGX任务或科学附图。本轮尚处内部探索，不增加发布版本或成果计数，也没有产生公开稿。
