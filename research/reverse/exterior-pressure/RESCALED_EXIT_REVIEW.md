# 固定外旋流形状持留障碍：独立复核

2026-09-07。PRIVATE_CORE。结论：PASS，范围为当前合同中的真实 NS 条件定理；不是一般奇性排除、数值时间窗或研究冻结声明。

审查者已全文读取以下四份实际文件。本次未编写持留合同、持留正文或联合负对照正文；此前参与过外场静态推导，所以不把此审查称为完全盲审。缩放、旋度结构和误差常数是在阅读持留正文前独立重算，再与正文逐项比较。AI 独立复核不等于人类同行评审或形式证明验证。

| 依赖文件 | 本次读取版本的 SHA256 |
|---|---|
| `JOINT_TEST_PROOF.md` | `9d0100f62ec6ef25ef2552348120d2b7b1e802aba49167bf4115edad02a3cd91` |
| `PROOF.md` | `50df7a60076567acac9cbad6588132c3e0f49e77f84f17ee68e740a8a32478b9` |
| `RESCALED_EXIT_CONTRACT.md` | `31c9b603144d5b0b5544caecb6de37ab7d04c8d0803b400ad3c5e63396534543` |
| `RESCALED_EXIT_PROOF.md` | `e96f1bce6d2076d560191211e208bd43f33e0db2d5c21de8abc6dfd31b361e78` |

上述版本变化后，本记录不能自动充当新版本的审查。四份文档同属本目录。

## 1. 真实解假设与重标符号

本定理从任意实际存在的黏性1、无外力固定环面光滑解出发。它只从联合负对照中提取固定空间函数 \(V\) 和正数 \(Q\)，没有将联合负对照路径当作真解。

记 \(\tau=T_*-t\)、\(s=-\log\tau\)、\(x=\tau^{2/5}y\)。由
\[
 u(t,x)=\tau^{-3/5}F(s,y),\qquad
 p(t,x)=\tau^{-6/5}P(s,y)
\]
直接得到
\[
 \partial_tu=\tau^{-8/5}
 [F_s+\tfrac35F+\tfrac25(y\cdot\nabla)F],
\]
\[
 \Delta_xu=\tau^{-7/5}\Delta_yF,\quad
 (u\cdot\nabla_x)u=\tau^{-8/5}(F\cdot\nabla_y)F,
 \quad \nabla_xp=\tau^{-8/5}\nabla_yP.
\]
所以正文的重标方程及黏性系数 \(\tau^{1/5}=e^{-s/5}\) 均正确。固定球是否位于重标坐标域内已列为假设；\(s\ge\log100\) 还保证该黏性系数小于1。扩张坐标域上的局部计算不要求把伸缩后的域误认为另一个固定环面。

## 2. 测试球、方向与正源项

测试点和球为
\[
 y_*=(1/40,61/40,0),\qquad B_*=B_{1/400}(y_*).
\]
该点距第二壳中心 \((0,3/2,0)\) 为 \(\sqrt2/40\)，且
\[
 \frac{2}{40^2}<\left(\frac1{20}-\frac1{400}\right)^2.
\]
所以连球的闭包也位于第二壳球内。另有 \(1/40-1/400>0\)，球远离旋转轴，圆柱坐标没有轴上奇性。其余壳在这个邻域恒为零，因此 \(V=\sqrt{b_2}W\) 是局部精确恒等式。

绕 \(e_2\) 轴采用右手圆柱基。在 \(y_*\) 处，\(e_r=e_1,e_z=e_2,e_\theta=-e_3\)。特别地，该点方位旋度就是一个带负号的 Cartesian 分量：
\[
 \Omega_\theta=\Omega\cdot e_\theta
 =\partial_2F_1-\partial_1F_2.
\]
正文中的配对没有一般单位向量展开可能带来的额外 \(\sqrt3\) 常数。

独立核对联合负对照的局部公式：若 \(r=\sqrt{y_1^2+y_3^2}\)、\(z=y_2\)、\(\zeta=z-3/2\)，则
\[
 W=w(r,z)e_\theta,\qquad w=2r h'(\sigma),
 \quad\sigma=(1/20)^2-r^2-\zeta^2.
\]
它的对流项是 \(-w^2/r\,e_r\)，旋度方位分量为
\[
 -\partial_z(w^2/r)=16r\zeta h'(\sigma)h''(\sigma).
\]
在 \(y_*\)，有 \(r=\zeta=1/40\)、\(\sigma=1/800\)，所以
\[
 q_*=(1/100)h'(1/800)h''(1/800)>0.
\]
正号来自 \(h'(\sigma)>0\) 和
\(h''(\sigma)=e^{-1/\sigma}\sigma^{-4}(1-2\sigma)>0\)。\(V\) 的局部幅度是 \(\sqrt{b_2}\)，对流为二次项，因而源项恰为 \(Q=b_2q_*>0\)。联合文档的定义保证 \(b_2\ge1\) 且有限，不需要数值求积来取得其正性。

## 3. 旋度方程、压力与经向结构

对 \(y\cdot\nabla F\) 求旋度给
\(\operatorname{curl}(y\cdot\nabla F)=\Omega+(y\cdot\nabla)\Omega\)。因此 \(3/5\) 与 \(2/5\) 合成正文中的 \(\Omega\) 系数1。压力无论来自哪个外壳或频率，都满足 \(\operatorname{curl}\nabla P=0\)，所以此处是精确消去，不是遗漏未定压力或修改 Leray 投影。

为直接检查正文的经向结构论证，纯轴对称方位速度 \(v(r,z)e_\theta\) 的旋度为
\[
 -\partial_zv\,e_r+\frac1r\partial_r(rv)\,e_z.
\]
它没有方位分量。对一般轴对称经向场 \(A_r(r,z)e_r+A_z(r,z)e_z\)，径向伸缩微分 \(y\cdot\nabla=r\partial_r+z\partial_z\) 不对方位角求导，因而保持经向结构。其向量 Laplacian 为
\[
 (\partial_r^2+r^{-1}\partial_r+\partial_z^2-r^{-2})A_r\,e_r
 +(\partial_r^2+r^{-1}\partial_r+\partial_z^2)A_z\,e_z,
\]
也保持经向结构。由此确认，代入固定 \(V\) 后，线性、伸缩与黏性三个旋度项在 \(y_*\) 的方位配对都严格为零。该结论只需本球内的局部轴对称结构；不要求三个壳的整个并集具有同一轴对称性。

投影方向 \(e_\theta(y_*)=-e_3\) 在时间上固定，因此 \(\partial_s(\Omega\cdot e_\theta)\) 不产生运动基底项。

## 4. C3 控制实际支付的常数

令 \(E=F-V\)。正文范数逐分量控制所有0至3阶 Cartesian 空间导数，所以在 \(y_*\) 有
\[
 |(\operatorname{curl}E)_j|\le2\varepsilon,\quad
 |\partial_k(\operatorname{curl}E)_j|\le2\varepsilon,\quad
 |\Delta(\operatorname{curl}E)_j|\le6\varepsilon.
\]
第三式需要三阶空间导数；仅速度或一阶小扰动无法支付该步。

因为 \(|y_*|_1=31/20\)，线性与黏性总差确为
\[
 \left[2+\frac25\frac{31}{20}\,2+6\right]\varepsilon
 =\frac{231}{25}\varepsilon<10\varepsilon.
\]

对任一个固定 Cartesian 旋度分量，非线性表达式是
\(\partial_a\sum_kF_k\partial_kF_b-\partial_b\sum_kF_k\partial_kF_a\)，共两个偏导、每个三个对流项、每项两个乘积导数。因此共有12个带符号乘积；每项的两个因子各是0至2阶速度导数。

设对应参考因子为 \(A,B\)，有 \(|A|,|B|\le M\)，各自误差至多 \(\varepsilon\)。逐项直接展开给
\[
 |(A+\delta A)(B+\delta B)-AB|
 \le2M\varepsilon+\varepsilon^2.
\]
所以正文的非线性差界
\((24M+12)\varepsilon\) 对 \(\varepsilon\le1\) 成立。这里既包括对流改变，也包括所有乘积导数，不只检查某一领先项。

取 \(L=24M+22\)，总误差不超过 \(L\varepsilon\)。当
\(0<\varepsilon\le\min\{1,Q/(2L)\}\) 时，完整真实旋度方程因而给
\[
 \partial_s\Omega_\theta(s,y_*)\le-Q+L\varepsilon\le-Q/2.
\]
全过程没有使用 \(F_s\) 小或 \(F_s\to0\) 的假设；时间漂移是由真实方程推出的结论。

## 5. 持留上界及量词

管内条件及 \((\operatorname{curl}V)\cdot e_\theta=0\) 给
\(|\Omega_\theta(s,y_*)|\le2\varepsilon\)。在任意连续持留区间 \([s_0,s_1]\) 积分，
\[
 -4\varepsilon\le\Omega_\theta(s_1,y_*)-\Omega_\theta(s_0,y_*)
 \le-\frac Q2(s_1-s_0),
\]
于是 \(s_1-s_0\le8\varepsilon/Q\)。正文的端点方向和常数8均正确。

这是单次连续持留的上界。没有证明离开后不能再进入，也不控制仅在离散时刻接近 \(V\) 的轨迹。如果真实重标解在所有充分大的 \(s\) 都留在该管内，则可取任意长的有限子区间而矛盾。因此正文的“不能最终永远留在该邻域”也成立。

\(M,Q\) 均有严格解析定义，且 \(M<\infty,Q>0\)。本次没有计算其数值，不把这一解析条件定理说成已认证的数值持留时间窗。

## 6. 复核范围与结论

本次实读四份依赖，并实际执行了 Python `fractions.Fraction` 程序，核对测试球包含关系、离轴距离、\(|y_*|_1\)、\(1/800\) 的切断参数、\(1/100\) 的源项系数、\(h''\) 正号、\(231/25<10\) 及重标指数。该程序的10项既有有理检查全部通过。它不是只作手算；源码与原先工具中观察到的确定性输出现已原样保存。为补齐运行证据，仅对同一程序重放一次，保存实际日志，输出与原先观察值逐字节相同，没有增加数学检查或测试计数。首次内联运行未单独保留时间戳，日志对此明确注明；日志中的时间、退出码是本次证据重放的实际工具记录，未回填为首次运行时间。

| 计算证据 | SHA256 |
|---|---|
| `rescaled_exit_review_scalar_checks.py` | `5766581233ef845e993d7910f83684a8d0db30f545185430f758c7263e37b6d7` |
| `rescaled-exit-review-scalars.stdout.txt` | `15588dba3b987d143d2ea1aba3ecc84c37389a6838ba3fa3af45238375208f39` |
| `rescaled-exit-review-scalars.run.json` | `2739e999cc0f4b48875d675e3787b23b333db308d981e5912fc105297cc561b2` |

重放命令为 `python3 research/reverse/exterior-pressure/rescaled_exit_review_scalar_checks.py`，工作目录是反向工作树根目录，运行时为 Python 3.9.6。没有运行新的动力学模拟或扫描；有限常数核算不代替上面的完整推导。

当前正文在声明范围内没有发现数学阻断项，可以作为真实 NS 的有界局部条件定理保留。它的内容是这个指定、固定、未经调制的外旋流形状的小 \(C^3\) 邻域不能被真实重标演化长期占据。

该结论不排除随时间改变的外场、旋转或平移调制后的形状、低阶拓扑中的接近、其他尺度、重新进入该邻域、一般局部浓缩或 NS 奇性。压力能量静态见证本身也没有因此变成一条真实轨道。未证明原创性、人类同行评审通过、投稿价值或全域正则性。
