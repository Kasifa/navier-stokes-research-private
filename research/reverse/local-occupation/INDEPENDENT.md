# 固定初值能量下的局部误差积分与重标时间离开占比

2026-09-08，PRIVATE_CORE。独立有界手工推导，待非作者审查。先全文读本目录 CONTRACT.md，随后只读其指定的旧 exterior-pressure 原输入。本项未读 weak-local-exit 的新主稿、独立稿或审查，也未读 local-occupation/PROOF.md。

合同如实披露根曾先行手工预检能量保持及有界观察量路线。本作者只得到这份合同和旧输入，未得到预检的具体公式、常数或本项主稿。本人有早先源桥接、代数接口及后续范围审查经历，不称全课题盲推导。

本文证明：同一初值的全域能量给整个扩张周期胞的未归一化 L² 范数上界，从而同时控制局部误差、二次项及两时间端点。对每个真实光滑重标区间，得到局部形状误差的积分下界，以及在一个明确符号 delta 范围内离开 delta 邻域的时间测度下界。不假设整个区间接近形状；黏性保留为显式可积预算。

## LOI.1 实际阅读与固定对象

路径相对 research/reverse/，散列均由本轮实际文件取得。旧源内部转引没有自动计作本轮实读；未打开旧科学程序、计算数组或运行输出。

| 来源与本轮实际范围 | SHA-256 |
|---|---|
| local-occupation/CONTRACT.md，先全文读 | 368fc878d7f35223b5ebe96dee84cd99b33573cb9ba0208e7e795c0214bd1485 |
| exterior-pressure/RESCALED_EXIT_PROOF.md，全文，固定坐标、球与完整重标方程 | e96f1bce6d2076d560191211e208bd43f33e0db2d5c21de8abc6dfd31b361e78 |
| exterior-pressure/JOINT_TEST_PROOF.md，第 1–36、128–151 行，完整第 1、6 节及开头测度约定 | 9d0100f62ec6ef25ef2552348120d2b7b1e802aba49167bf4115edad02a3cd91 |
| exterior-pressure/PROOF.md，第 1–95 行，尤其第 1 节原环面体积、归一化能量约定 | 50df7a60076567acac9cbad6588132c3e0f49e77f84f17ee68e740a8a32478b9 |

上述第 1、6 节中使用的旧路径是 NON-NS 负对照，本文不把它当作真实原解。只沿用它固定的局部形状以及已明确的方位对流旋度公式。

设 u 为单位黏性、无外力、三维 2π 环面上同一固定光滑初值 u0 的真实光滑 NS 解。只在它实际存在的 \(0\le t<T_*=1/100\) 范围内讨论。定义
\[
\tau=T_*-t,\quad s=-\log\tau,\quad d=\tau^{2/5},
\quad
F(s,y)=\tau^{3/5}u(t,\tau^{2/5}y).
\tag{LOI.1}
\]
保留旧 \(s\ge\log100\)、\(y_*=(1/40,61/40,0)\)、
\(B_*=B_{1/400}(y_*)\)。在该球上固定
\[
V=\sqrt{b_2}\,W,\quad b_2>0,\qquad
W=w(r,z)e_\theta,\quad
w=2r h'(\sigma),
\]
\[
r=\sqrt{y_1^2+y_3^2},\quad z=y_2,\quad
\zeta=z-\frac32,\quad
\sigma=\left(\frac1{20}\right)^2-r^2-\zeta^2.
\tag{LOI.2}
\]
圆柱基绕 e2 轴取右手方向，旧约定在 \(y_3=0,y_1>0\) 时 \(e_\theta=-e_3\)。小球远离轴线，故这些向量场在其邻域光滑。h 是旧源已固定的光滑函数，不在本项重新选择。

以下所有局部和周期胞 L² 范数均用未归一化 Lebesgue 测度。固定任意合同允许、但不选实际函数的
\[
0\le\chi\in C_c^\infty(B_*),\quad \chi\not\equiv0,
\qquad \phi=\chi e_\theta,\quad \Psi=\operatorname{curl}\phi .
\tag{LOI.3}
\]
测试固定于 y 坐标，不随时间、原解或误差改变。它紧支撑、光滑且无散。

## LOI.2 整个周期胞的能量缩放

记原周期胞 \(Q=(-\pi,\pi)^3\)，重标胞
\(Q_s=\tau^{-2/5}Q\)。其体积是
\[
|Q_s|=(2\pi)^3\tau^{-6/5}.
\]
对整个胞直接换元 \(x=\tau^{2/5}y\)，得到精确等式
\[
\int_{Q_s}|F(s,y)|^2\,dy
=\tau^{6/5}\tau^{-6/5}\int_Q|u(t,x)|^2\,dx
=\int_Q|u(t,x)|^2\,dx .
\tag{LOI.4}
\]
因此不是假设局部能量自动保持，而是先核整个周期胞的测度及振幅指数恰好抵消。若使用按胞体积归一化的均值范数，则左侧还要除随时间增大的 \(|Q_s|\)，那是另一量，不能与 LOI.4 混用。

同一原初值的真实光滑能量恒等式给
\[
\int_Q|u(t)|^2+
2\int_0^t\int_Q|\nabla_xu(\xi)|^2\,dx\,d\xi
=\int_Q|u_0|^2 .
\]
定义有限非负常数
\[
H=\left(\int_Q|u_0|^2\right)^{1/2}.
\tag{LOI.5}
\]
若沿用旧 exterior-pressure/PROOF 的归一化记号
\(E_0^2=(2\pi)^{-3}\int_Q|u_0|^2\)，则准确为
\(H=(2\pi)^{3/2}E_0\)，没有漏掉体积因子。

固定 \(B_*\Subset Q\)，而 \(\tau\le1/100<1\)，故在所有本合同时间 \(B_*\Subset Q_s\)。于是
\[
\|F(s)\|_{L^2(B_*)}\le H.
\]
令
\[
v_*=\|V\|_{L^2(B_*)},\quad M=H+v_*,
\quad E(s,y)=F(s,y)-V(y),\quad e(s)=\|E(s)\|_{L^2(B_*)},
\]
则
\[
\boxed{0\le e(s)\le M.}
\tag{LOI.6}
\]
这一上界不要求任何时刻接近 V，也不使用局部或全域高阶导数上界。它始终来自同一初值 H，不能每段另选能量常数。

## LOI.3 整个固定球上的正方向作用

旧公式
\[
\operatorname{curl}((W\cdot\nabla)W)\cdot e_\theta
=16r\zeta h'(\sigma)h''(\sigma)
\tag{LOI.7}
\]
不只在 y* 有意义。对整个 B*，有
\[
r>\frac1{40}-\frac1{400}>0,\qquad
\zeta>\frac1{40}-\frac1{400}>0,
\]
且
\[
|y-\tfrac32e_2|
<\frac{\sqrt2}{40}+\frac1{400}<\frac1{20}.
\]
因此 \(0<\sigma<(1/20)^2<1/2\)。旧 h 满足
\(h'(\sigma)>0\)、\(h''(\sigma)>0\) 于这个区间。这里仅重核已固定球与旧函数的符号，没有选择新点、函数或实际参数。

所以由任意固定非负非零 chi 定义的常数
\[
\boxed{\Gamma
=16b_2\int_{B_*}\chi\,r\zeta h'(\sigma)h''(\sigma)\,dy>0}
\tag{LOI.8}
\]
严格正且有限。紧支撑积分分部给等价的真实动量测试
\[
\Gamma=\int_{B_*}(V\cdot\nabla)V\cdot\Psi\,dy
=-\int_{B_*}(V\otimes V):\nabla\Psi\,dy,
\tag{LOI.9}
\]
其中约定 \((A\otimes B):\nabla\Psi
=\sum_{i,j}A_iB_j\partial_j\Psi_i\)。

chi 不必轴对称。事实上对任意这样的 chi，
\[
\Psi=-\partial_z\chi\,e_r+
\left(\partial_r\chi+\frac{\chi}{r}\right)e_z
\]
没有方位分量；chi 的方位导数不产生额外分量。V、\((y\cdot\nabla)V\) 和 \(\Delta V\) 都是轴对称纯方位向量，因而
\[
\int V\cdot\Psi=0,\qquad
\int\left(\frac35V+\frac25(y\cdot\nabla)V
-\nu(s)\Delta V\right)\cdot\Psi=0,
\quad \nu(s)=e^{-s/5}.
\tag{LOI.10}
\]
特别这些零式并非略去黏性。Γ>0 还保证 \(v_*>0\)、\(\Psi\not\equiv0\)。

## LOI.4 完整弱测试与所有误差项

直接从原 NS 方程和 LOI.1 微分，或核对旧重标方程，得到
\[
F_s+\frac35F+\frac25(y\cdot\nabla)F
-e^{-s/5}\Delta F+(F\cdot\nabla)F+\nabla P=0,
\quad \operatorname{div}F=0,
\tag{LOI.11}
\]
其中 \(P=\tau^{6/5}p(t,\tau^{2/5}y)\)。没有用 Euler 方程替代它。

设
\[
J(s)=\int_{B_*}F(s)\cdot\Psi\,dy,\qquad
\mathcal L_s\Psi=\frac35\Psi+\frac25(y\cdot\nabla)\Psi
+e^{-s/5}\Delta\Psi .
\]
紧支撑无散测试使全部真实压力严格消去：
\(\int\nabla P\cdot\Psi=-\int P\operatorname{div}\Psi=0\)。
这包括全域和周期压力，不依赖任何局部压力近似。B* 固定且在胞内部，测试在边界附近恒零，没有移动胞边界项。

漂移积分分部使用
\[
\int(y\cdot\nabla F)\cdot\Psi
=-\int F\cdot(3\Psi+y\cdot\nabla\Psi).
\]
结合完整对流分部，准确有
\[
J'(s)=\int F\cdot\mathcal L_s\Psi
+\int(F\otimes F):\nabla\Psi.
\tag{LOI.12}
\]
用 LOI.9–10 后，这是带固定符号的恒等式
\[
\boxed{J'(s)=-\Gamma+\mathcal R(s),}
\]
\[
\begin{split}
\mathcal R(s)={}&\int E\cdot
\left(\frac35\Psi+\frac25(y\cdot\nabla)\Psi\right)
+e^{-s/5}\int E\cdot\Delta\Psi\\
&+\int(E\otimes V+V\otimes E+E\otimes E):\nabla\Psi .
\end{split}
\tag{LOI.13}
\]
两个交叉项按有序次序全部保留，没有把一个未知二次项当作一阶小误差，也没有要求 e 整窗很小。所有 E 的导数均转给固定测试。

## LOI.5 固定常数、两端点与误差积分下界

用欧氏向量范数及 Frobenius 矩阵范数定义固定测试常数
\[
p_*=\|\Psi\|_2,\qquad
b_*=\|\nabla\Psi\|_{L^\infty(B_*),F},\qquad
d_*=\|\Delta\Psi\|_2,
\]
\[
a_*=\left\|\frac35\Psi+
\frac25(y\cdot\nabla)\Psi\right\|_2+2b_*v_*,
\qquad C_*=a_*+b_*M .
\tag{LOI.14}
\]
所有范数有限。Γ>0 和 LOI.9 给
\[
0<\Gamma\le b_*v_*^2,
\]
所以 \(b_*>0,v_*>0\)，进而 \(M>0,a_*>0,C_*>0\)；
\(d_*=0\) 则允许，下面不用它作分母。

Cauchy–Schwarz 分别控制两个真实交叉项，得到
\[
\boxed{|\mathcal R(s)|
\le a_*e(s)+b_*e(s)^2+d_*e^{-s/5}e(s).}
\tag{LOI.15}
\]
这里 \(2b_*v_*e\) 来自两项各自的界，而非在原恒等式中将两有序项认作同一项。

对任何实际光滑闭区间 \(s_0<s_1\)、\(s_0\ge\log100\)，记
\(\ell=s_1-s_0\)。积分 LOI.13 保留两个实际端点：
\[
\Gamma\ell=J(s_0)-J(s_1)+\int_{s_0}^{s_1}\mathcal R(s)\,ds.
\tag{LOI.16}
\]
由同一全域能量，分别有
\[
|J(s_k)|\le p_*\|F(s_k)\|_{L^2(B_*)}\le p_*H,\quad k=0,1.
\]
故两端点总预算为 2p*H，没有将时间导数、末端值或初端值设小。亦可保留更紧的实际两端点范数，但本文不需要这样做。

完整黏性贡献由 LOI.6 直接给
\[
d_*\int_{s_0}^{s_1}e^{-s/5}e(s)\,ds
\le5d_*M(e^{-s_0/5}-e^{-s_1/5}).
\]
定义非负显式预算
\[
\mathcal B_{01}
=2p_*H+5d_*M(e^{-s_0/5}-e^{-s_1/5}).
\tag{LOI.17}
\]
于是先有保留二次项的必要条件
\[
\boxed{\Gamma\ell\le\mathcal B_{01}
+\int_{s_0}^{s_1}\{a_*e(s)+b_*e(s)^2\}\,ds.}
\tag{LOI.18}
\]
再用已证全域界 \(e^2\le Me\)，而非整窗近邻假设，得
\[
\boxed{\int_{s_0}^{s_1}e(s)\,ds
\ge\frac{[\Gamma\ell-\mathcal B_{01}]_+}{C_*},}
\qquad [x]_+=\max\{x,0\}.
\tag{LOI.19}
\]
这就是所求线性时间积分误差下界。短区间右侧可能为零，仍是正确必要条件；没有声称每个时刻的误差都有正下界。

## LOI.6 离开 delta 邻域的有限区间测度

令固定标量函数
\[
G_*(x)=a_*x+b_*x^2,\qquad x\ge0.
\]
它严格递增。由 \(M\ge v_*>0\)、\(a_*\ge2b_*v_*\) 和
\(\Gamma\le b_*v_*^2\)，有
\[
G_*(M)>\Gamma>0 .
\]
因此定义完全符号化的阈值
\[
\boxed{\delta_*=
\frac{\sqrt{a_*^2+4b_*\Gamma}-a_*}{2b_*},\qquad
0<\delta_*<M,\quad G_*(\delta_*)=\Gamma.}
\tag{LOI.20}
\]
没有给 chi、delta 或初值选择实际值；这只是任意固定合同数据的明确容限范围。所有分母已付非零。

对任意符号 \(0\le\delta<\delta_*\)，设
\[
\mathcal O_\delta(s_0,s_1)
=\{s\in[s_0,s_1]:e(s)>\delta\}.
\]
实际光滑性使 e 连续，集合可测；等号 e=delta 属于补集，不漏掉边界。因 \(0\le e\le M\)，逐个区域估计给
\[
\int_{s_0}^{s_1}G_*(e(s))\,ds
\le G_*(\delta)\ell+
\{G_*(M)-G_*(\delta)\}|\mathcal O_\delta|.
\tag{LOI.21}
\]
代入 LOI.18，得到
\[
\boxed{
|\mathcal O_\delta(s_0,s_1)|
\ge
\frac{[(\Gamma-G_*(\delta))\ell-\mathcal B_{01}]_+}
 {G_*(M)-G_*(\delta)} .}
\tag{LOI.22}
\]
分母严格正，斜率 \(\Gamma-G_*(\delta)\) 严格正。该式比先线性化 e² 再分区保留更多信息，仍只用同一能量及固定测试，没有引入新的形状假设。

若 delta=delta*，上述斜率为零，仅有平凡非负测度界；delta>delta* 时本证明不给正的长时间占比。delta≥M 时由 e≤M 可知集合为空，不能继续误用正分母式。H=0 也不破坏推导：M=v*>0、b*>0，全部式子仍成立。chi=0 被原合同排除，不能通过它把 Gamma 与阈值一并退化后声称结论。

## LOI.7 若原解在所有 t<T* 光滑

只有在同一固定初值原解确实在全部 \(0\le t<T_*\) 光滑时，才能令 \(s_1\to\infty\)。这不是本稿证明的存在或正则性结论。固定任一允许 s0，LOI.17 满足
\[
0\le\mathcal B_{01}\le2p_*H+5d_*M e^{-s_0/5},
\]
右侧与 s1 无关。因此 LOI.19 给
\[
\boxed{\liminf_{s_1\to\infty}
\frac1{s_1-s_0}\int_{s_0}^{s_1}e(s)\,ds
\ge\frac{\Gamma}{C_*}>0.}
\tag{LOI.23}
\]
对每个固定 \(0\le\delta<\delta_*\)，LOI.22 给
\[
\boxed{\liminf_{s_1\to\infty}
\frac{|\mathcal O_\delta(s_0,s_1)|}{s_1-s_0}
\ge
\vartheta_\delta:=
\frac{\Gamma-G_*(\delta)}
 {G_*(M)-G_*(\delta)}>0 .}
\tag{LOI.24}
\]
因 Gamma<G*(M)，还有 \(\vartheta_\delta<1\)，与时间占比的定义一致。于是近邻集合的上极限占比至多 \(1-\vartheta_\delta\)，但其累计重标时间仍可能无限。本式不限制访问次数或每次持续时间的组合，也不判定每一长区间之外的轨道结构。

如果原解只已知光滑到小于 T* 的某个时间，LOI.19、22 仅用于实际存在的有限区间；不能越过未知存在区间作上述极限。

## LOI.8 对数时间、物理时间及准确范围

由 \(t=T_*-e^{-s}\) 有
\[
dt=(T_*-t)\,ds,\qquad ds=\frac{dt}{T_*-t}.
\]
因此 LOI.19 的积分是
\[
\int_{t_0}^{t_1}
\|F(s(t))-V\|_{L^2(B_*)}\frac{dt}{T_*-t},
\]
而离开占比的分子是
\[
\int_{t_0}^{t_1}
\mathbf1_{\{e(s(t))>\delta\}}\frac{dt}{T_*-t},
\quad
\ell=\log\frac{T_*-t_0}{T_*-t_1}.
\tag{LOI.25}
\]
它不是普通物理时间 dt 的占比或积分界，不能删除该权重。固定物理时间总长度有限不与正的重标长时间占比矛盾。

本结果沿用固定旧坐标、固定 V、固定紧支撑测试以及同一初值的能量。没有全窗近邻假设，没有额外高阶导数或任意衰减条件；漂移、完整黏性、全部二次误差、两端点以及全域压力的精确消去都已写出。这里允许反复进出，只约束这些区间中的积分误差与离开测度。

它不证明近邻累计时间有绝对有限上界，不限制再进入次数，不覆盖任意快速平移、旋转或其它动态形状调制，不排除一般 NS 奇性或证明正则性。弱解时间迹、不同初值族、跨代统一余项、同一初值无限尺度及真实再生成仍不是本稿结论。没有从旧 NON-NS 负对照转而接受一条真实候选，也没有修复旧失败。

全部工作为手工符号、文本及哈希元数据；未选择实际函数、频率、初值、时间、容限或测试实例，未执行科学程序、数组、数值求值、扫描、Git、发布、重置或外部消息。本稿只写本独占文件，最终全文自读、复核来源字节后报告 SHA 并停改。

CONDITIONAL LOCAL ERROR INTEGRAL AND LOG-TIME EXIT FRACTION；FIXED DATUM AND TEST；NO-CANDIDATE；NOT CLAY。
