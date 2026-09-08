# 周期梯度配对的无散局部化

2026-09-08。内部工具 GL。结论是一个静态空间转换：将周期速度截成紧支无散场后，联合压力生产、完整梯度范数耗散和秩一缺陷的单位体积平均都收敛到原周期值。压力不能直接截断，但其误差可用一个二阶 Fourier 乘子的 L2 恒等式控制。这个转换没有生成 NS 轨道、固定正龄估计或指定中心好尺度。

分类：下列工具引理为 `PROVED`（本地解析推导）；新的终端动力学输入与 Clay 问题仍 `OPEN / NOT CLAY`。无原创性认定或真人同行评审；推导与复核由 AI 辅助完成。不另立独立研究小节、反例计数、release 或发布。

## 1. 精确对象

设 \(u\in C^\infty(\mathbb T^3;\mathbb R^3)\)，环面周期为 \(2\pi\)，\(\operatorname{div}u=0\)、\(\int_{\mathbb T^3}u=0\)。令 \(G=\nabla u\)，规范压力满足 \(-\Delta p=\operatorname{tr}(G^2)\)、\(\int p=0\)。记 \(B(G)=G/|G|\) 于 \(G\ne0\)，\(B(0)=0\)，以及到实秩至多一矩阵集的 Frobenius 距离 \(d(G)\)。定义

\[
 P(u)=-\int B(G):(G^2+\nabla^2p),\qquad
 D(u)=-\int B(G):\Delta G,\qquad Q(u)=\int d(G)^2.
 \tag{GL.1}
\]

积分在相应全周期胞或全空间进行。这里 \(D\) 不是压力上界，也不是只在 \(G\ne0\) 处积分的经典方向耗散。它与下节完整正则化耗散相等。定义与 [MA](clay_b_mixed_absorption_calibration_20260908.md) §1 一致。

取周期向量势 \(\Psi=(-\Delta)^{-1}\operatorname{curl}u\)，其零模置零。Fourier 模逐项给 \(\operatorname{curl}\Psi=u\)。它及任意固定阶导数有界。令 \(R=2\pi N\)、\(N\ge1\)，\(K_R=[-R,R]^3\)。取 \(0\le\chi_R\le1\)，在 \(K_R\) 为一，在 \(K_{R+1}\) 外为零，各固定阶导数对 R 一致有界。这样的截止可由三个一维固定宽度平滑截止相乘构成。

\[
 W_R=\operatorname{curl}(\chi_R\Psi),\qquad
 G_R=\nabla W_R,\qquad
 p_R=(-\Delta_{\mathbb R^3})^{-1}\operatorname{tr}(G_R^2),
 \quad m_R=|K_R|/(2\pi)^3=(2N)^3.
 \tag{GL.2}
\]

Newton 逆取基本解 \((4\pi|x|)^{-1}\)，即 \(-\Delta p_R=\operatorname{tr}(G_R^2)\)。\(W_R\) 光滑、紧支、无散、全空间均值零，在 \(K_R\) 等于 u。所有固定阶空间导数的上界可依赖 u，但不依赖 R。闭截止层 \(L_R=K_{R+1}\setminus\operatorname{int}K_R\) 的体积为 \(O(R^2)\)。

**工具引理。** 对每个固定的上述 u，存在有限常数 \(C_u\)，使所有 \(R=2\pi N\) 满足

\[
 \begin{split}
 |P_{\mathbb R^3}(W_R)-m_RP_{\mathbb T^3}(u)|&\le C_uR^{5/2},\\
 |D_{\mathbb R^3}(W_R)-m_RD_{\mathbb T^3}(u)|&\le C_uR^2,\\
 0\le Q_{\mathbb R^3}(W_R)-m_RQ_{\mathbb T^3}(u)&\le C_uR^2.
 \end{split} \tag{GL.3}
\]

所以三种单位胞平均都收敛。\(C_u\) 依赖固定场及其导数，不是仅由动能给出的常数；没有声称对任意大振幅、变化初值族或原 NS 时间区间一致。

## 2. 完整耗散及零集

对任意本引理中的光滑梯度场 H，令 \(q_\kappa=(|H|^2+\kappa^2)^{1/2}\)、\(B_\kappa=H/q_\kappa\)。链式法则给

\[
 \Delta q_\kappa=B_\kappa:\Delta H+\Gamma_\kappa,
 \quad \Gamma_\kappa=\sum_j\left\{
 \frac{|\partial_jH|^2}{q_\kappa}
 -\frac{(H:\partial_jH)^2}{q_\kappa^3}\right\}\ge0,
 \quad \lim_{\kappa\downarrow0}\int\Gamma_\kappa
 =-\int B(H):\Delta H. \tag{GL.4}
\]

最后一步不使用单调性。周期情形 \(\int\Delta q_\kappa=0\)；紧支 H 情形用紧支光滑函数 \(q_\kappa-\kappa\) 积分分部。随后 \(|B_\kappa|\le1\)、\(\Delta H\in L^1\) 给支配收敛。于是极限非负有限，并保留正则化在零集可能产生的贡献，没有要求 \(B(H)\) 在零集连续或可微。

在 \(K_R\)，GL.1 的耗散被积函数与原周期函数完全相同，积分恰为 \(m_RD(u)\)。其余部分仅在 \(L_R\)，模长不超过 \(|\Delta G_R|\le C_u\)，给 GL.3 第二式。零集没有额外遗漏的边界项，因为比较的是 GL.4 已确定的完整积分，而不是逐点极限密度。

类似地，\(0\le d(G_R)^2\le|G_R|^2\le C_u\) 在截止层成立，直接给 GL.3 第三式。这里没有对距离函数求导。

## 3. 非局部压力误差

写 \(f_R=\operatorname{tr}(G_R^2)\) 并定义

\[
 e_R=f_R+\Delta(\chi_Rp),\qquad
 \operatorname{supp}e_R\subset L_R,
 \quad\|e_R\|_{L^2(\mathbb R^3)}\le C_uR,
 \quad p_R=\chi_Rp+(-\Delta)^{-1}e_R.
 \tag{GL.5}
\]

支撑结论来自内区 \(G_R=G\)、\(\Delta p=-\operatorname{tr}(G^2)\)，以及外区两项同为零。截止层所有项一致有界，其体积为 \(O(R^2)\)，故得到 L2 界。最后的分解是整个 Poisson 方程的精确恒等式：Newton 逆作用于 \(-\Delta(\chi_Rp)\) 等于 \(\chi_Rp\)。没有把 \(p_R\) 直接设成被截断的周期压力。

对 \(e\in C_c^\infty(\mathbb R^3)\)，Hessian Newton 逆的 Fourier 符号是 \(-\xi_i\xi_j/|\xi|^2\)。采用 Frobenius 矩阵范数，Plancherel 给

\[
 \|\nabla^2(-\Delta)^{-1}e\|_2^2
 =\int\frac{\sum_{i,j}\xi_i^2\xi_j^2}{|\xi|^4}
                   |\widehat e(\xi)|^2\,d\xi
 =\|e\|_2^2.
 \tag{GL.6}
\]

这里采用酉归一化傅里叶变换；原点是零测集合。只需要 Hessian 的 L2 界，不要求一般 Newton 势本身属于全空间 L2，也没有调用 Riesz 算子的强 L1 有界性。

GL.5 的修正项与归一化梯度配对时，\(B(G_R)\) 在 \(K_{R+1}\) 外为零，且其 L2 范数不超过 \(|K_{R+1}|^{1/2}\)。因此

\[
 \left|\int B(G_R):\nabla^2(-\Delta)^{-1}e_R\right|
 \le |K_{R+1}|^{1/2}\|e_R\|_2\le C_uR^{5/2}.
 \tag{GL.7}
\]

其余压力项 \(B(G_R):\nabla^2(\chi_Rp)\) 在 \(K_R\) 恰为周期被积函数，在截止层模长有固定 \(C_u\) 界，所以其积分误差为 \(O_u(R^2)\)。惯性项 \(B(G_R):G_R^2\) 同样只需一个截止层 \(O_u(R^2)\) 误差。与 GL.7 合并得到 GL.3 第一式，证明完成。

## 4. 本轮选择及适用边界

GL.3 可用于比较周期场和紧支场的静态梯度配对。旧 AI 的速度 L3 压力功局部化已处理过另一类非局部误差；本引理不把它的速度方向 Lipschitz 性移用到 \(G/|G|\)，而是使用完整耗散积分和有界测试。

把本工具再与单份 NS 初值缩放合用，可能加强 MA 的总动能系数限制。但即使完成那项加强，也只限制初始切片上的系数，不自动排除固定正龄、共同临界 \(\mathsf A+\mathsf E\) 上界下的估计。本轮没有执行后续缩放、构造新解族或声称这一反例已经冻结；不将工具计成新的终端障碍。

本轮定向比较还确认：应变中间特征值、应变波锥约束、负应变锥坏集时间缺口和标量热流三次校正，在既有 SE、负应变锥、LD、HN 中已有记录。它们没有因此成为新的动力学输入；不重开同类文献综述。

当前仍未选出可以闭合联合好尺度的新估计。后续先从真实演化的额外结构选择具体命题，再作推导；不能以静态转换、旧条件判据或重复的初始时间反检取代它。GL 作为可复用的内部空间工具保存，不触发发布、图档、仿真、DGX 或 recap。
