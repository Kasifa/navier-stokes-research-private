# 缩母球内平均场与高角模的混合压力

2026-09-22。PRIVATE_CORE / PROVED IN STATED SCOPE / CONDITIONAL / OPEN / NOT CLAY。

本节利用不可压缩性，把平均场与高模的混合压力源写成单散度。零 Dirichlet 压力得到一个额外的角频因子 \(1/N\)；结合已有向量角谱隙，其内球截止功不超过外球耗散的一个小系数。实际压力的调和差另作估计：在每个二进时间窗缩小母球，已有条件平均梯度界足以使高模调和通量趋零。完整 \(w\otimes w\) 压力、外球与内截止的差以及低模动力学仍未解决。

这里不是一般正则性结果，也不宣称这些椭圆方法具有新颖性。HP 的固定母球结论不被改写；本节重新计算变化母球的所有尺度因子。

## 1. 同一实际解与每窗参数

在固定局部提升母柱
\(\mathcal Q_0=B_{2b_0}(0)\times(-T,0)\)
取同一固定正黏性、周期、无外力 NS 解，沿用 HP 的能量类、可积压力和终点前光滑性。轴与指定中心不变。令 \(v=\Pi u\)、\(w=u-v\)，使用已定义的协变角平均与投影。

固定 \(\kappa\ge8\)，取 \(b=\kappa R\le b_0\)，在
\[
J_R=(-R^2,-R^2/2)\subset(-T,0)
\]
上固定一个整数 \(N\ge2\)，\(z=P_{\ge N}w=P_{\ge N}u\)。令
\[
\begin{split}
S_R&=\operatorname*{ess\,sup}_{t\in J_R}
 \|\nabla v(t)\|_{L^\infty(B_b)},\\
M_0&=\operatorname*{ess\,sup}_{-T<t<0}
 \|u(t)\|_{L^2(B_{2b_0})},\\
P_*&=\|p\|_{L^{3/2}(\mathcal Q_0)}
  +C\|u\|_{L^3(\mathcal Q_0)}^2.
\end{split}
\tag{MP.1}
\]
\(M_0,P_*<\infty\) 来自同一实际解的固定母柱资格；并非任意解族的共同常数。\(S_R\) 是完整 Cartesian 一阶梯度，在每个终点前紧窗有限。它不是 SA 的最负应变，不能用较弱的不利应变条件直接替代。

## 2. 不遗漏平均压力的实际分解

取 \(0\le\eta_R\le1\) 径向光滑截止，在 \(B_b\) 上为一，支于 \(B_{2b}\)。对零延拓张量定义全空间 Riesz 压力
\[
q_{ww}=\mathcal R_i\mathcal R_j(\eta_R w_iw_j),
\qquad
q_{vv}=\mathcal R_i\mathcal R_j(\eta_R v_iv_j).
\tag{MP.2}
\]
另令 \(q_{\rm mix}\in H^1_0(B_b)\) 为逐时唯一弱解
\[
-\Delta q_{\rm mix}
=2\partial_i v_j\,\partial_jw_i
=2\partial_j[(\partial_i v_j)w_i]
=2\operatorname{div}((w\cdot\nabla)v).
\tag{MP.3}
\]
求和采用 Cartesian 指标。恒等式使用 \(\operatorname{div}v=\operatorname{div}w=0\)；特别是
\(\partial_j\partial_i v_j=0\)。
因此不是把 \(w\) 的导数藏在一个未经控制的 \(L^2\) 源里：右端确实是 \(L^2\) 向量场的散度。

由原压力 Poisson 方程，
\[
H_{0,R}=p-q_{ww}-q_{vv}-q_{\rm mix},
\qquad \Delta H_{0,R}=0\quad\hbox{in }B_b.
\tag{MP.4}
\]
\(q_{vv}\) 必须保留在这个未投影分解中；若省略它，差一般不调和。径向截止、轴对称协变张量 \(v\otimes v\) 和 Riesz 压力算子的旋转协变性，使 \(q_{vv}\) 是轴对称标量，故 \(Q_Nq_{vv}=0\)。

球上的 Dirichlet Laplacian 与旋转交换；\(v\) 为协变零角模。因此
\[
q_D:=Q_Nq_{\rm mix}\in H^1_0(B_b),\qquad
-\Delta q_D=2\operatorname{div}((z\cdot\nabla)v),\qquad Q_Nq_D=q_D.
\tag{MP.5}
\]
这些是同一真实压力的分解恒等式，不要求真实压力满足零边值：
\[
\boxed{Q_Np=Q_Nq_{ww}+q_D+H_N,\qquad H_N=Q_NH_{0,R}.}
\tag{MP.6}
\]
实际边界和周期远场完整留在 \(H_{0,R}\)；零边值只是选取局部椭圆解的方法。

## 3. 混合压力的单散度与角频增益

记 \(S(t)=\|\nabla v(t)\|_{L^\infty(B_b)}\)。测试 MP.5 得
\[
\|\nabla q_D\|_{L^2(B_b)}\le2S(t)\|z\|_{L^2(B_b)}.
\]
标量高角模的逐圈 Poincaré 界给
\[
\|q_D\|_2\le\frac bN\|\nabla q_D\|_2,
\qquad
\boxed{\|q_D\|_2\le\frac{2b}N S(t)\|z\|_2.}
\tag{MP.7}
\]
弱测试合法，因为 \((z\cdot\nabla)v\in L^2\)，源属于 \(H^{-1}\)。标量谱隙是 \(N\)；向量谱隙仍是已有 SA 的 \(N-1\)，两者不能混用。

令径向 \(\chi_R\) 支于 \(B_R\)，\(\|\nabla\chi_R^2\|_\infty\le C_\chi/R\)，并记
\(D_a(t)=\int_{B_a}|\nabla z|^2\)。
已审向量角谱隙在整个同心球给
\[
\|z\|_{L^2(B_a)}\le\frac a{N-1}D_a^{1/2}.
\]
这不要求球面零边值；轴上的结论按 SA 的非负积分极限解释。于是
\[
\begin{split}
R^{-1}\left|\int q_Dz\cdot\nabla\chi_R^2\right|
&\le \frac{C_\chi bS(t)}{NR^2}
 \|z\|_{L^2(B_b)}\|z\|_{L^2(B_R)}\\
&\le C_\chi\kappa^2
 \frac{R S(t)}{N(N-1)^2}\sqrt{D_bD_R}\\
&\le C_\kappa\frac{R S(t)}{N(N-1)^2}D_b.
\end{split}
\tag{MP.8}
\]
与 \(\nu D_b/R\) 比较，系数为
\[
\delta_{R,N}=\frac{C_\kappa R^2S_R}{\nu N(N-1)^2}.
\]
若同一个固定 \(N\) 在整个 \(J_R\) 满足
\(N^2\ge C_0R^2S_R/\nu\)，则
\[
\boxed{
R^{-1}\int_{J_R}\left|\int q_Dz\cdot\nabla\chi_R^2\right|dt
\le \frac{4C_\kappa}{C_0N}\,
 \frac{\nu}{R}\int_{J_R}D_b(t)\,dt.}
\tag{MP.9}
\]
\(C_\kappa\) 依赖固定 \(\kappa\) 和截止轮廓，不依赖 \(N,R\)。未满足该阈值时只能保留 MP.8 中的加权时间积分。

**MP.9 不是内截止吸收。** 右端是外球 \(B_{\kappa R}\) 的耗散；原 SA.5 左侧是 \(\int\chi_R^2|\nabla z|^2\)。即使相对系数趋零，也未证明归一外球耗散共同有界，不能宣称实际混合通量必趋零。

## 4. 变化母球的调和差范数

对全 \(q_{\rm mix}\) 用 MP.3 弱测试、普通 Dirichlet Poincaré 和有限体积 Hölder：
\[
\|\nabla q_{\rm mix}(t)\|_2\le2S_RM_0,\qquad
\|q_{\rm mix}(t)\|_{L^{3/2}(B_b)}
 \le Cb^{1/2}\|q_{\rm mix}(t)\|_2
 \le Cb^{3/2}S_RM_0.
\]
这里用了每个旋转不变球上 \(w=(I-\Pi)u\) 的 \(L^2\) 正交收缩。时间积分得到
\[
\|q_{\rm mix}\|_{L^{3/2}(B_b\times J_R)}
\le Cb^{3/2}S_RM_0|J_R|^{2/3}.
\tag{MP.10}
\]
这只是一窗的估计，不声称全末段可积。MP.7 对 \(q_D\) 有额外 \(1/N\)，但 MP.10 估计的是未投影的 \(q_{\rm mix}\)，不能偷用这个额外因子。

角平均的 \(L^3\) 收缩和三角不等式给
\(\|v\|_3\le\|u\|_3,\ \|w\|_3\le2\|u\|_3\)。
全空间 Calderón–Zygmund 界对 MP.2 只使用 \(\|\eta_R\|_\infty\le1\)，不引入截止导数。因此
\[
\|H_{0,R}\|_{L^{3/2}(B_b\times J_R)}
\le P_*+Cb^{3/2}S_RM_0|J_R|^{2/3}.
\tag{MP.11}
\]
右端第一项在所有 \(R\) 间一致；第二项完整保留母球和时间尺度。

将 HP.6–8 的直接球谐估计应用于未投影且在整个球调和的 \(H_{0,R}\)，输出高模 \(H_N\)。不需要 \(Q_N\) 在 \(L^{3/2}\) 或 \(L^\infty\) 上的一致有界性。由于 \(|J_R|=R^2/2\)，
\[
\begin{split}
\Phi^{\rm harm}_{R,N}
&:=R^{-1}\int_{J_R}\left|\int H_Nz\cdot\nabla\chi_R^2\right|dt\\
&\le Cb^{-2}M_0R^{1/6}(4R/b)^N
 \|H_{0,R}\|_{L^{3/2}(B_b\times J_R)}\\
&\le C(4/\kappa)^N
 \left[\kappa^{-2}M_0P_*R^{-11/6}
 +\kappa^{-1/2}M_0^2R S_R\right].
\end{split}
\tag{MP.12}
\]
只有调和项带这一指数因子，不能乘到 MP.9 或 \(Q_Nq_{ww}\) 上。

## 5. 条件平均梯度界下的结论

现在才额外使用已有 CF.2 的完整分量界，包括旋流的一阶界。光滑轴对称性给 \(v_r=v_\theta=0\) 于轴；径向微积分用 \(\partial_rv_r,\partial_rv_\theta\) 控制连接项 \(v_r/r,v_\theta/r\)。因此全部 Cartesian 一阶梯度满足
\[
S_R\le C_{\rm grad} R^{-2-2h},\qquad 0<h<1/2,
\tag{MP.13}
\]
因为整个 \(J_R\) 上 \(-t\asymp R^2\)。这不是仅从 \(\sigma_-\) 得到的界，也不是一般无力解自动具有的结构。

取固定足够大的 \(K\)，令
\(N_R=\max(2,\lceil K R^{-h}\rceil)\)。
明确取 \(K^2\ge C_0C_{\rm grad}/\nu\)，其中 \(C_{\rm grad}\) 含固定结构及几何常数，使 MP.9 的完整梯度阈值成立。于是混合压力截止功的外球耗散相对系数为 \(O(N_R^{-1})\)，而
\[
\Phi^{\rm harm}_{R,N_R}
\le C\,2^{-K R^{-h}}
 \left(R^{-11/6}+R^{-1-2h}\right)\longrightarrow0.
\tag{MP.14}
\]
两者是不同结论：一个相对外球耗散小，另一个绝对趋零。

每窗 \(N_R\) 固定；它不能在整个 \((-R^2,0)\) 上凭 MP.13 保证有限门槛，更不授权忽略跨窗口改模和时间截止项。取不同阈值仍是同一实际解的分析，不是换初值或黏性。

## 6. 尚未证明的下一步

MP.6 中完整的 \(Q_Nq_{ww}\) 仍未控。它包括低低、高低和高高源，不能把 \(w\) 等同于 \(z\)，也不能由某个有限低角带直接消除所有高角压力。输运与 CM 有符号交换、低模增长、轴附近原速度控制同样保留。

MP.9 还需要把外球量纳入合法的嵌套截止估计；不能把不同球或不同角阈值的能量直接相减。有限总耗散不足以保证这里的 \(\nu R^{-1}\int D_b\) 一致有界。即便当前压力的两个子项得到明确界，也没有导出原 PF 的共同有限 \(M\) 与好尺度。

本节直接证明了所列分解和椭圆界。它依赖经典 Dirichlet 弱解、Poincaré、Calderón–Zygmund 及 HP 已证明的球谐尾，未宣称新的正则性定理或原创性。下一项研究须处理尚存的实际二次压力/局部化耦合，而不是给相同未知临界范数另起名字。

## 7. 有限查重范围

旧 BV.2 已有全周期混合压力的导数重组；YT 的水平矩形 Dirichlet 测试已有单散度的弱能量界。它们不是本节的球域高角模组合，也不因换成角频而失去方法上的重合。

[Liu–Zhang 的大 Fourier 角模论文](https://arxiv.org/html/2305.05272v1) Proposition 3.1 给角模逆算子的加权估计，§4 在压力项中区分零模与非零模相互作用。主任务实际核读 (3.7)–(3.9) 的假设/陈述以及 (4.30)–(4.32) 的分解与消去；没有重审其证明全文，也不把其全空间加权结论直接用作本节球域 Dirichlet 定理。此次查重仅确认基础机制已有先例，不认证本地组合的新颖性。
