# 零梯度角区中的压力配对：线性缺陷界不成立

2026-09-08。EWP，PRIVATE_CORE。范围内解析反例；一般三维 NS / Clay 仍 OPEN / NOT CLAY。未作充分查新，不宣称原创性、期刊价值或真人同行评审。

本节检验上一节留下的具体候选，而不是压力绝对值范数的加强版。结论是否定的：即使使用同一光滑无散速度自身的归一化梯度和规范压力，原整胞联合源也不能仅由梯度 L2 范数乘秩一偏离 L2 范数控制。

构造来自带零梯度角区的旋流。一个趋于零的真实无散应变，在这些角区决定归一化梯度的方向，却只增加很小的非归一化成本。压力 Hessian 保留对数主项，原带符号配对不再像纯径向旋流那样消失。所有内外截断层和周期压力均保留。

## 1. 精确目标与结论

固定普通体积的三维环面 T³_(2pi)。对光滑、无散、均值零的周期速度 u，令
\[
G=\nabla u,\quad q=|G|_F,\quad
d(G)=\operatorname{dist}_F(G,\{\operatorname{rank}\le1\}),
\quad B_0(G)=\begin{cases}G/q&q>0,\\0&q=0.\end{cases}
\tag{EWP.1}
\]
p 是唯一零均值周期解 \(-\Delta p=\operatorname{tr}(G^2)\)，H=grad²p。候选为：存在仅依赖固定周期胞的有限 C，使上述所有 u 满足
\[
|I(u)|\le C\|G\|_2\|d(G)\|_2,
\qquad I(u)=\int B_0(G):(G^2+H).
\tag{EWP.2}
\]
这里包含合法 NS 初始切片，不预设 B0 在零梯度集连续。

**命题 EWP-A（本地证明）。** 存在一族这样的 u_delta，delta→0，以及正的固定常数，使
\[
|I(u_\delta)|\ge c\log(1/\delta),\qquad
\|G_\delta\|_2\le C\sqrt{\log(1/\delta)},\qquad
0<\|d(G_\delta)\|_2\le C.
\tag{EWP.3}
\]
所以 EWP.2 不成立。其反例比值至少按 sqrt(log(1/delta)) 发散。这不是奇性构造；不同 delta 对应不同光滑初值。第8节说明，把量词改成所有局部光滑 NS 解的严格正时刻也不能恢复这条统一估计，但不声称时间具有统一正下界。

## 2. 固定角函数，不随 delta 缩窄

以下先在 T²_(2pi) 的小圆盘内计算，所有范数和积分暂为二维。第7节统一沿 z 延拓。

取 alpha=pi/100。固定光滑 pi-周期函数 beta，0≤beta≤1，在
\(E=\{\operatorname{dist}(\theta,\pi\mathbb Z)\le\alpha\}\)
恰为1，在距 pi Z 至少2alpha处为0，两者之间严格介于0与1。可用标准平坦光滑阶跃连接；其支撑测度至多8alpha。令 b=1−beta，并取唯一光滑 pi-周期解
\[
w''+w=b,\qquad a=-b.
\tag{EWP.4}
\]
存在性无需新的边值定理：只含偶数模态的 Fourier 系数给 \(w_{2n}=b_{2n}/(1-4n^2)\)，分母均非零，系数快速衰减。w 为实光滑函数，a 恰在 E 为零。Parseval 给
\[
\|w'\|_2\le\tfrac23\|\beta\|_2,\qquad
\int w=2\pi-\int\beta,
\]
\[
M:=\int wb=\int(w^2-|w'|^2)
\ge2\pi-2\int\beta-\tfrac49\|\beta\|_2^2
\ge2\pi-\tfrac{176}{9}\alpha>0.
\tag{EWP.5}
\]
最后使用 Cauchy–Schwarz 下界 \(\int w^2\ge(\int w)^2/(2\pi)\)。M 与角函数固定，不依赖 delta；不需要额外假定 w 逐点正。

## 3. 实际无散速度与所有截断层

固定 0<R<pi/8。取径向光滑 cutoff chi，chi(s)=0 于 s≤1、chi(s)=1 于 s≥2；取 eta(r)=1 于 r≤R、eta(r)=0 于 r≥2R。令 0<delta<R/16，并定义紧支流函数
\[
\Psi_\delta(r,\theta)=-r w(\theta)\chi(r/\delta)\eta(r),
\qquad v_\delta=(\partial_y\Psi_\delta,-\partial_x\Psi_\delta).
\tag{EWP.6}
\]
内圆盘上函数为零，故原点没有极坐标非光滑性；外缘平滑截止，随后按周期延拓。v_delta 光滑、无散、均值零。

在 2delta<r<R 上，记 e_r、e_theta 为同一点的正交极坐标基，有
\[
v_\delta=-w'e_r+w e_\theta,\qquad
S_\delta:=\nabla v_\delta
=\frac{a(\theta)}r e_r\otimes e_\theta.
\tag{EWP.7}
\]
确实，径向导数为零，角导数为 −(w''+w)e_r；因此主环梯度秩至多一，并在 E 中严格为零。

内层 delta<r<2delta 的速度是一个固定光滑场在 x/delta 上的缩放，梯度为 delta^−1 倍固定函数；外层 R<r<2R 完全固定。因此
\[
\|S_\delta\|_2^2=\|a\|_{L^2_\theta}^2\log(R/(2\delta))+O(1),
\qquad\|d(S_\delta)\|_2\le C.
\tag{EWP.8}
\]
内外层都包含在 O(1) 中，不被当成零。主环中的 d 则确实为零。

## 4. 全周期压力的对数主项

令 f_delta=tr(S_delta²) 为基场压力源。由主环 S_delta²=0 和上面的精确缩放，存在固定光滑紧支函数 F_in、F_out，使
\[
f_\delta(x)=\delta^{-2}F_{\rm in}(x/\delta)+F_{\rm out}(x),
\quad \operatorname{supp}F_{\rm in}\subseteq\{1\le r\le2\},
\quad\operatorname{supp}F_{\rm out}\subseteq\{R\le r\le2R\}.
\tag{EWP.9}
\]
内源的总质量不是零。利用无散性，tr(S²)=div((v·grad)v)，在2delta圆周积分，EWP.7 给
\[
m:=\int F_{\rm in}=\int_0^{2\pi}a w\,d\theta=-M,
\qquad \int F_{\rm out}=M,\qquad c_0=-m/(2\pi)>0.
\tag{EWP.10}
\]
这也核对了整个周期压力源均值零。

记 Gamma 为 −Delta 的零均值周期 Green 函数。在足够小的圆盘中
\(\Gamma(x)=-(2\pi)^{-1}\log r+S(x)\)，S 光滑。一个直接构造是先截断平面对数基本解，其 −Delta 等于 delta_0 加光滑余项；减去目标常数后的余项均值零，可由 Fourier 级数解出光滑修正。这里只对远离极点的核求经典导数。

令 H_delta^b 为 v_delta 的规范压力 Hessian，并设
\[
\mathcal A_\delta=\{4\delta<r<R/2\},\quad
L_\delta=\log(R/(8\delta)),\quad
K(\theta)=I_2-2e_r\otimes e_r.
\]
则作为全胞 L1 函数有
\[
H_\delta^b=c_0\mathbf1_{\mathcal A_\delta}\frac{K(\theta)}{r^2}
 +E_\delta,\qquad\|E_\delta\|_1\le C.
\tag{EWP.11}
\]
证明分三区。主环内 y 位于内源的2delta圆盘，核的均值展开给
\[
\left|\nabla^2(\Gamma*f_{\rm in,\delta})(x)-m\nabla^2\Gamma(x)\right|
\le C\delta/r^3+C\delta.
\tag{EWP.12}
\]
积分时 delta integral_(4delta)^(R/2) r^−2 dr 一致有界。外源距主环有固定距离，其 Hessian 有界；Green 光滑修正亦如此。

在 r<4delta 内，不删去核的分布局部项。周期 Fourier 乘子直接给 \(\|\nabla^2(-\Delta)^{-1}f\|_2\le\|f\|_2\)，其中常模取零。内源 L2 为 O(delta^−1)，这个圆盘的面积平方根为 O(delta)，所以内圈 Hessian 的 L1 为 O(1)。在 r≥R/2 上内源核距极点有固定下界，质量范数固定，故 L1 也为 O(1)；外源的整个压力是固定光滑函数。三区合并即为 EWP.11。它不是对截断的 log 势直接求二阶导数，未遗漏截断分布项。

## 5. 在零梯度角区使用同一速度的方向

取另一个固定径向光滑截止 eta_p，等于1于r≤R，等于0于r≥2R。令
\[
V=\big(\partial_y(xy\eta_p),-\partial_x(xy\eta_p)\big),
\quad u_\delta=v_\delta+\delta V,
\quad A=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\tag{EWP.13}
\]
V 本身光滑、无散、均值零；r<R 时 V=(x,−y)，grad V=A。以下 G_delta=grad u_delta，B0 完全由这个总速度定义，不另选独立矩阵测试。

距离函数是1-Lipschitz，故
\[
\|d(G_\delta)\|_2\le C,\qquad
\|G_\delta\|_2^2=\|a\|_2^2 L_\delta+O(1).
\tag{EWP.14}
\]
在 E 与主环的交集，G_delta=delta A，故 d 的范数严格为正。

总规范压力记为 p_delta，H_delta=grad²p_delta。两份源的差为
\(2\delta\operatorname{tr}(S_\delta\nabla V)+\delta^2\operatorname{tr}((\nabla V)^2)\)。仍只使用 Fourier L2 乘子与有限体积 Cauchy–Schwarz，得到
\[
\|H_\delta-H_\delta^b\|_1
\le C\delta\|S_\delta\|_2+C\delta^2
=O(\delta\sqrt{L_\delta})=o(1).
\tag{EWP.15}
\]
没有对任意 L1 源使用 Riesz 的 L1 有界性，也不需要额外 Hardy 输入。

## 6. 真正的压力配对保留对数

在主环上，定义角函数
\[
F(s)=\int_0^{2\pi}
\frac{a e_r\otimes e_\theta+sA}{|a e_r\otimes e_\theta+sA|}:K(\theta)\,d\theta,
\qquad s>0.
\tag{EWP.16}
\]
分母不为零：rank(sA)=2，而另一个矩阵秩至多一。被积函数绝对值不超过 sqrt2。a≠0 时，s→0 的归一化极限与 K 正交；a=0 时，它等于 A/|A|。支配收敛因此给
\[
F(s)\longrightarrow J:=\int_E\frac A{|A|}:K(\theta)\,d\theta
=-\sqrt2\int_E\cos(2\theta)\,d\theta
=-2\sqrt2\sin(2\alpha)<0.
\tag{EWP.17}
\]
因为主环中 s=delta r≤delta R/2，F(delta r)=J+o(1) 在整个主环一致成立。这里只使用极限定义，不假设平坦角边界有某种未证明的收敛速率。

EWP.11、15与|B0|≤1在全胞给
\[
\int B_0(G_\delta):H_\delta
=c_0\int_{4\delta}^{R/2} F(\delta r)\frac{dr}{r}+O(1)
=c_0J L_\delta+o(L_\delta).
\tag{EWP.18}
\]
这是同一个总速度、同一个规范压力和同一个 B0 的全空间积分。核心和外区的贡献已由 E_delta 控制，不能再引入一个未计的对数抵消。

二维无散梯度是迹零2×2矩阵，Cayley–Hamilton 给 G²=−det(G)I2，所以
\[
B_0(G):G^2=0
\tag{EWP.19}
\]
处处成立，包括零点按定义取零。惯性项不会抵消 EWP.18。由于 c0J 非零，结合 EWP.14 就证明二维的 EWP.3。

## 7. 提升到原三维周期问题

取三维速度 (u_delta,1(x,y),u_delta,2(x,y),0)，沿 z 周期不变。它仍光滑、无散、均值零；三维规范压力等于二维规范压力。梯度增加一个零行和零列，d 不变。

三维整胞配对为二维的2pi倍，两个 L2 范数各乘 sqrt(2pi)，所以反例比值完全不变。特别地，三维配对的主项是 2pi c0 J L_delta，不能漏掉这项体积因子。

所得族的速度 L2 本身也一致有界；增长的是梯度 L2。每个 delta 都给合法的光滑 NS 初值，不将极限 delta=0 的角场当作光滑解，也不要求实际后续轨道保持这个静态形式。未用仿真、数值极限拟合或任意不相容矩阵。

## 8. 只写严格正时间不能绕过反例

这里仅调用 [Tao，arXiv:1108.1165v4，Theorem 5.1](https://arxiv.org/html/1108.1165v4#S5) 的经典周期局部光滑理论，按固定黏性重标常数。该接口已在 SRG 中核读，不依赖大数据全局存在。

须处理 B0 的零集不连续性。对任意光滑初值 u0，设 Z={grad u0=0}、H0 为初压 Hessian、J0=integral_Z |H0|。光滑函数在其零集的几乎每个密度点各阶空间导数为零：否则第一个非零 Taylor 齐次多项式会使零集在该点不具有密度1。因此梯度方程在 Z 上几乎处处给 grad u_t(0)=−H0。

对从 u0 出发的局部光滑解，空间支配收敛给
\[
\lim_{t\downarrow0}I(u(t))=I(u_0)-J_0.
\tag{EWP.20}
\]
H0≠0 的零梯度点上 B0趋于−H0/|H0|；H0=0 处配对趋零。其余位置直接连续，全部被积函数由共同短光滑窗上的 q²+|H| 支配。

另从 −u0 出发一条独立解。初始 H0 不变，其同一极限为 −I(u0)−J0；这不是把 −u(t) 错当成原方程的解。右侧两个 L2 范数在初端连续。因此如果 EWP.2 对所有这样的解的严格正时刻成立，则
\[
|I(u_0)|+J_0
=\max\{|I(u_0)-J_0|,|-I(u_0)-J_0|\}
\le C\|G_0\|_2\|d(G_0)\|_2,
\tag{EWP.21}
\]
与已构造的静态族矛盾。正时间的反检时刻可以随 delta 趋近初始时刻；没有固定共同正龄窗口或单解奇异终端结论。

## 9. 本族的原黏性成本更大

这一范围不能只凭猜测说明。对总梯度 G_delta，取 Phi_kappa(G)=sqrt(|G|²+kappa²)−kappa，定义完整静态成本
\[
\Lambda_\delta=\lim_{\kappa\downarrow0}
\int\sum_jD^2\Phi_\kappa(G_\delta)
[\partial_jG_\delta,\partial_jG_\delta]
=-\int B_0(G_\delta):\Delta G_\delta\ge0.
\tag{EWP.22}
\]
先对每个 kappa 分部积分，再由 |Delta G_delta| 支配取极限。该定义包含完整零集贡献，不只是 q>0 上的经典密度。

内层的 Delta G 为 O(delta^−3) 的固定缩放，面积 O(delta²)；主环的该导数为固定角函数乘 r^−3，外层固定。探针光滑且幅度 delta，故 Lambda_delta≤||Delta G_delta||1≤C/delta。下界取远离 beta 支撑、a=−1 的固定角扇区及 4delta<r<8delta，并把 delta 进一步限制为小于 R/64。此处 B0 是归一化的 −e_r tensor e_theta+delta r A，delta r≤8delta²，所以角导数范数一致有正下界，q≥c/r。于是
\[
\frac c\delta\le\Lambda_\delta\le\frac C\delta,
\qquad
\frac{|I(u_\delta)|}{\nu\Lambda_\delta}
=O_\nu\bigl(\delta\log(1/\delta)\bigr)\longrightarrow0
\quad(\nu>0\text{ 固定}).
\tag{EWP.23}
\]
下界用了非零区域 q|grad B0|²≥c/r³ 的积分；非负正则化的其余部分不会抵消它。二维提升到三维仅乘共同2pi因子。本族不构成原黏性吸收的反例；这也不是所有场的吸收定理，更不是实际时间累计控制。

## 10. 排除范围和后续问题

这一族直接排除 EWP.2，而不只是其压力L1加强版。全局兼容秩一逼近、一般 Hardy 能量界或忽略角区的小应变，都不能用来证明这条已被否定的结论。对 beta=0 且不加探针的纯径向旋流，极坐标基下梯度只有非对角项、规范压力 Hessian 为对角项，原配对恰消失；此前绝对值范数的反例本身并不够。仅有 J=0 本身不能推出加探针后的全配对精确为零。本节的非零对数结论保留了零角区和同速度探针。

本节不排除带原梯度耗散、径向或角向导数成本的估计，也不证明这些解有正涡伸长或奇性。PF 条件正则出口和 SRG 均未被推翻；任意演化的指定中心好尺度仍未得到。不能把逐点/逐时控制失败理解成所有时间累计控制失败。

下一步从实际演化检验含原完整 mu_G 耗散的时间累计式；EWP.22–23 的静态成本已完成，不另起一节重复核算。先在 EWP 的同一解上区分小内核快速扩散时段与外尺度时段，写出原梯度模长平衡中的完整两切片和压力项，核对对数源能持续多久；不把静态对数下界直接乘以固定时间，也不默认同一个固定正龄窗口。不重新提出已经排除的不含耗散 q×d 源界，不将 MA 已失败的加速度平方余项重新引入。若只重现已有累计预算而无新严格尺度增益，应如实记录并重新选择动力学输入。

构造由 variable_reference_check 提出开楔改造，主任务与其独立推导，good_scale_route_comparison 核查周期压力及角函数。最终实际文件审查另记。普通文献与本地去重用于区分旧 LK/NE 的 d² 障碍和本目标；没有采用新检索结果中的定理，未作全面查新。纯解析研究，无 DGX、仿真、科学图、新英文翻译或读者HTML/PDF；完整成果保持私有。
