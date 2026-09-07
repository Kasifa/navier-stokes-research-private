# 同一固定初值的中心涡量拉伸：独立全文审查

2026-09-07。PRIVATE_CORE。结论：**PASS FOR THE STATED DRAFT CONTRACT — 指定固定中心、指定初始正时间窗内的负拉伸项成立。** 这是未冻结草稿的独立审查，不是一般 NS 结论或将来最终稿的预先认证。

审查者 `driver_contract_review` 不是根代理的 CENTER_STRETCH_PROOF_DRAFT 作者，也不是 Pascal 的 CENTER_STRAIN_DERIVATION 作者。已全文读取这两份稿件和 CENTER_STRETCH_CONTRACT；独立重推下列关键步骤。复用的 LOCAL_REMAINDER_DRAFT、固定初值几何推导及已冻结 exterior-pressure/PROOF 均已由本审查者实读、实审；周期 Green 的热核基础还见此前实读的 next-concentration/PROOF。另一作者的中心应变推导只承担它声明的初始导数接口，本报告另核完整正时间余项，不把同一稿件的转述计作新的独立证明。

所有新常数复核均为解析手算。本次没有运行新的科学数值或整数核验程序，没有把手算包装成新证书；末尾 SHA-256 的计算仅核对输入版本。

## 1. 四阶周期像和的绝对交换

先前已确定的零均值周期 Green 热核公式不能在未经微分时改写成普通点电荷级数。这里实际只需要其四阶导数，可以合法交换。

对任一四阶多重指标 α，自由热核的导数具有形式

\[
\partial^\alpha K_{\mathbb R}(s,w)
=s^{-7/2}P_\alpha(w/\sqrt s)e^{-|w|^2/(4s)},
\]

其中 Pα 是固定有限次数多项式，常系数已吸收在其中。令 s=|w|²σ，则绝对时间积分为 |w|⁻⁵ 乘以方向 n=w/|w| 及 σ 的积分。|n|=1 时，多项式可统一受 C(1+σ⁻²) 控制；σ 接近零时有指数衰减，无穷端受可积的 σ⁻⁷/² 控制。因此

\[
\int_0^\infty|\partial^\alpha K_{\mathbb R}(s,w)|ds
\le C_\alpha|w|^{-5}
\]

的常数可对方向统一选取。

在闭单位球上，非零像点距离至少 (2π−1)|m|，而 ∑_{m≠0}|m|⁻⁵ 收敛。于是非零像点和全时间积分的绝对和有一致可积上界。对原热核差作四阶微分后，短时、长时两段可合并，再逐像积分，严格得到

\[
\nabla^4Q_G(z)=\sum_{m\ne0}\nabla^4\Phi(z+2\pi m),
\qquad |z|\le1.
\]

均匀背景项的四阶空间导数恰为零；没有把背景从周期 Poisson 方程移除。该等式也不要求未微分的 Green 像和绝对收敛。原点处 Φ 的奇性已经在 Q_G 中相消，右端所有像点始终远离零点。

## 2. 全部张量分量的 M_G<2

已核四阶 Newton 导数公式的一项 105、六项 −15 和三项 3，逐分量绝对系数和为 204。各方向余弦和 Kronecker 符号的绝对值均至多 1。因此每个分量受 204/(4πr⁵) 控制，而完整四阶张量有 3⁴=81 个分量，Frobenius 范数因子为 √81=9：

\[
\|\nabla^4\Phi(w)\|_F
\le\frac{459}{\pi}|w|^{-5}<153|w|^{-5}.
\]

这里没有将单一分量的界误用于整个张量。由 π>3，|z+2πm|>5|m|。按 j=||m||∞ 分壳，格点数精确为 (2j+1)³−(2j−1)³=24j²+2，且 |m|≥j。单调积分比较给

\[
\sum_{m\ne0}|m|^{-5}
\le24\sum_{j\ge1}j^{-3}+2\sum_{j\ge1}j^{-5}
<24\cdot\frac32+2\cdot\frac54=\frac{77}{2}.
\]

故完整张量及全部周期像满足

\[
M_G<\frac{153\cdot77}{2\cdot5^5}
=\frac{11781}{6250}<2.
\]

各界对闭单位球一致，取上确界不会丢掉已有的固定常数间隙。该上界是解析不等式，没有有限截断或未经认证的数值尾项。它补充当前新检验的显式界，不要求更改此前冻结证明中同一 M_G 的定义。

## 3. 径向 Fourier 中心投影与压力符号

在涡核相对坐标 z=0，令 P=diag(1,0,1)、f(z)=g(|z|)Pz，g=c²，c=2h'(ε²−|z|²)。由反对称旋转矩阵 A 的 A²=−P 及 Az·z=0，原始对流为 −gPz，因此完整全空间非线性确为 P_Lf。

若径向 Fourier 变换为 G(κ)，则 fhat=iG'(κ)Pξ/κ。再作一次空间微分产生另一个 i，中心梯度的共同径向符号为负。球面二、四阶矩分别给 P/3 与 (2P+tr(P)I)/15，所以

\[
\nabla P_Lf(0)
=-\frac{4\pi}{15(2\pi)^3}
[3P-\operatorname{tr}(P)I]
\int_0^\infty\kappa^3G'(\kappa)d\kappa.
\]

光滑紧支撑径向 g 保证 Fourier 变换快速衰减，G'/κ 在零点有光滑延拓；上述积分绝对收敛。分部积分与反演给共同因子 3g0，其中 g0=g(0)>0。故

\[
\nabla B_{\mathbb R^3}(W,W)(b)
=\frac{g_0}{5}\operatorname{diag}(1,-2,1).
\]

根代理稿以“未投影梯度为 g0P”确定共同径向常数的方法，与这个显式负号计算一致。另核压力符号：B=f−∇p、Δp=div f，因此 Hess p=(g0/5)diag(4,2,4)，迹为 2g0，正好等于中心 div f。没有把原始径向对流代替 Leray 后的场。

这些旋转球面平均只用于全空间主项。固定环面没有被假定具有全部连续旋转对称；后面的 Q_G 界保留它的影响。

## 4. 固定 δ 上的完整周期符号

尺度仍为原合同的 δ=1/100，未重新选择初值。中心 x_c=δb，压力比较核的参数 x_c−x 满足 |x_c−x|≤δε<1。完整周期与全空间非线性的原始对流相同，梯度之差恰为负的压力 Hessian 差。故

\[
\nabla B_T(a,a)(x_c)
=C_*\operatorname{diag}(1,-2,1)+E,
\qquad \|E\|_F\le M_G\int|a|^2<2\delta.
\]

这里 C*=δ⁻⁴g0/(5JW)，∫|a|²=δ 使用未归一化 Lebesgue 积分；没有漏乘或误加周期体积因子。张量收缩用 ||a⊗a||F=|a|²，已包含全部指标求和。E 是压力 Hessian 差的负号，故为实对称矩阵；单个 E22 的绝对值受同一 Frobenius 界控制。

对 0<s≤ε²<1/2，有 h''(s)>0。因此 g(|z|)≤g0，直接积分给

\[
J_W\le g_0\int_{B_\varepsilon}|z|^2dz
=\frac{4\pi}{5}\varepsilon^5g_0,
\]

继而

\[
C_*\ge\frac{\delta^{-4}}{4\pi\varepsilon^5}
=\frac{8\cdot10^{13}}\pi>2\cdot10^{13}.
\]

π<4 的使用方向正确。极小的 g0 与 JW 没有被分别浮点求值；其共同尺度在严格商界中抵消。固定 δ 的周期误差 <2δ=1/50，足以保留中心轴向负应变的严格符号，无需事后缩小支撑。

## 5. 黏性、初始涡量及 Π'(0)

初始中心梯度为 δ⁻²JW⁻¹/²c(0)A，A 为绕 e2 的反对称矩阵，故 S(a)(x_c)=0。对径向 c，逐分量计算

\[
\Delta[c(r)Az]=(c''(r)+4c'(r)/r)Az.
\]

括号在 r=0 有光滑径向延拓，其中心梯度仍为标量乘 A。因此 sym∇Δa(x_c)=0 是完整黏性项的结构性消失，不是采用无黏方程。

初始涡量为 2c(0)δ⁻²JW⁻¹/²e2，故 |ω0|²=20C*。对固定空间点 x_c 的 Π=ωᵀSω 求时间导数，两项含 S(a) 的涡量时间导数项在 0 精确为零。真实 NS 方程 u_t(0)=Δa+B_T(a,a) 因而给

\[
\Pi(0)=0,\qquad
\Pi'(0)=20C_*[-2C_*+E_{22}]
\le-L_*,
\]

其中 L*=20C*(2C*−2δ)>0。无须假定 ω_t 很小，也没有使用只满足压力 Poisson 方程的假路径。

该时间导数在固定 x_c 处取值；本合同未追踪一个随流移动的涡核中心，也没有将 Π 的负号直接当作含输运、黏性的全部局部涡量模长变化率。

## 6. A6 构造仍对应同一完整原解

令 A6=||a||A6、M6=2A6、T6=min{1/100,1/(256A6²)}。原已审 LOCAL_REMAINDER_DRAFT 的输出频率热核估计和权重次乘性同样适用于指标 6，双线性 Duhamel 常数仍为 2√T6；半径 2A6 球上的压缩常数至多 1/2。高阶 Volterra 与插值论证也在这一共同 T6 上适用。

A6≥A4 保证 T6≤T0。由此前已证明的光滑解唯一性，A6 构造与 A4 构造在重叠区间相同，并非另选了一个解。全部 Fourier 模态、Leray 投影、黏性与非线性通道仍保留。

令 D6=M6+M6²。由完整方程直接得到

\[
\|u_t\|_{A_4}\le D_6,
\qquad
\|u_{tt}\|_{A_2}\le H_6:=D_6(1+2M_6).
\]

后一式的 Δu_t、B(u_t,u)、B(u,u_t) 三项分别由 D6、D6M6、M6D6 控制。压力导数已经包含在完整 B 中，未另行删除。

## 7. 欧氏/Frobenius 常数与 Π'' 余项

需要使用 Fourier 系数的向量/张量范数，不能逐分量粗估后漏掉维数常数。对实频率 k 和复向量 v，叉乘矩阵的欧氏算子范数为 |k|，所以 |k×v|≤|k||v|。梯度的单模张量为 iv⊗k，Frobenius 范数为 |v||k|；对称化是该范数下的压缩。因此由绝对和的三角不等式，严格有

\[
\|\operatorname{curl}f\|_{L^\infty(\mathrm{Euclidean})}
\le\|f\|_{A_1},\qquad
\|S(f)\|_{L^\infty(F)}\le\|f\|_{A_1}.
\]

不存在额外的 √2、√3 或 3 因子。故 ω、S 在整个区间分别受 M6 控制，其一阶时间导数受 D6 控制，二阶受 H6 控制。

实际二次求导为

\[
\Pi''=2\omega_{tt}^TS\omega
+2\omega_t^TS\omega_t
+4\omega_t^TS_t\omega
+\omega^TS_{tt}\omega.
\]

矩阵算子范数不超过 Frobenius 范数，四项的上界相加恰为

\[
|\Pi''|\le
2H_6M_6^2+2D_6^2M_6+4D_6^2M_6+H_6M_6^2
=K_*:=3M_6^2H_6+6M_6D_6^2.
\]

u 的真实时间正则性与空间 A2 界使固定点的这些导数及积分余项合法。K*>0 且有限，因此 Tcomp=min{T6,L*/K*}>0。完整积分余项给

\[
\Pi(t)\le-L_*t+\frac{K_*}{2}t^2
\le-\frac{L_*}{2}t<0,
\qquad0<t\le T_{\rm comp}.
\]

端点方向和系数 1/2 正确。该窗口的 A6 尚未数值计算，不被报告为某个具体数值时间长度；但其所有常数有固定定义及有限、正的解析证明。

## 8. 结论、未解决项及绑定

合同内未发现阻断错误。独立应变稿支付初始中心投影与周期修正；根代理稿另外支付同一完整解的正时间控制，二者适用范围没有混同。

本结果只说明指定初值在固定中心 x_c 的初始指定时间窗中，涡量拉伸项 Π 为负。它不证明其他点没有正拉伸，不证明该中心以后不能翻转，不证明跟随运动中心的同一结论，不证明全域涡量或能量单调性、普遍不拉伸、长期压缩或一般正则性。也不接受再生成成功、统一迭代、一个固定初值的无限尺度、无限维迭代误差或有限时奇性。

未将小 L² 数据误用为临界小数据条件，未改 δ、黏性、环面或截止形状，未自动增加 Taylor 阶。本文件保持当前未冻结状态，不修改被审稿，不生成发布或 git 操作。AI 独立复核不等同于人类同行评审或形式证明认证。

以下 SHA-256 绑定实际输入与已使用的依赖；其中前两项是当前待审合同和根代理草稿，第三项是另一作者的中心应变推导。旧证明只在本报告明确使用的范围内复用，不因绑定而改写已冻结内容。

| 实际输入 | SHA-256 |
| --- | --- |
| research/reverse/swirl-regeneration/CENTER_STRETCH_CONTRACT.md | `4502487b1379740ea169e1e5d5f5faffd5e7c1d8ecd225dfd19516be7c574280` |
| research/reverse/swirl-regeneration/CENTER_STRETCH_PROOF_DRAFT.md | `1eaf197ab6c8b443792cefadfbaac3d96bad3771a281fded32ca2d15d5c92283` |
| research/reverse/swirl-regeneration/CENTER_STRAIN_DERIVATION.md | `65dcbe9cbafffc13289cb774426f6e18bf7edab230bb03324a7ea894f01c3bcc` |
| research/reverse/swirl-regeneration/CONTRACT.md | `c887d8cc20495f0cf2e80585e66f92663f82c605f923194d49df5dda44bc9e12` |
| research/reverse/swirl-regeneration/INDEPENDENT_DERIVATION.md | `1ee6495178a4d6def57e733765ae0b778a3c90abf3456c352776c77e6db39581` |
| research/reverse/swirl-regeneration/LOCAL_REMAINDER_DRAFT.md | `c0346e98e776e7a5526727fde1572f1fc543d66b8fd3c31450ca791ea7297f8c` |
| research/reverse/swirl-regeneration/REMAINDER_REVIEW.md | `0c73fb914be4e3d17886dfe4d3a0d6240f7c7a7f42066c4d6d39dfbc63684a77` |
| research/reverse/exterior-pressure/PROOF.md | `50df7a60076567acac9cbad6588132c3e0f49e77f84f17ee68e740a8a32478b9` |
| research/reverse/next-concentration/PROOF.md | `fafadaecc7972111cd6d55e5cfa5ede746f306353f8b953266dc37d37a39a7f1` |
