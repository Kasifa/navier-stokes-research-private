# 秩一偏离的余子式演化：完整方程与零集

2026-09-08，北京时间。CD，PRIVATE_CORE。范围内解析恒等式与估计；一般三维 NS 正则性仍 OPEN / NOT CLAY。不宣称新颖性、最优常数或真人同行评审。

本节完成 GD 下一步提出的动力学检查。余子式平方商与原来的平方偏离量等价，在非零秩一矩阵和重奇异值处可以光滑求导。它的全局演化仍有零集测度，不能直接删去。该测度可由已有完整梯度熵控制。

所得时间信息是整胞积分及固定光滑空间测试积分的有界变差，从而存在一个弱测度终端迹；没有得到临界时空范数。还有一个具体限制：即便速度梯度满足无散与行无旋相容性，归一化后的黏性密度也可以为负。因此，完整演化式不能直接作为一个具有非负耗散的标量方程使用。

## 1. 同一个梯度与同一个偏离量

固定未归一化的 \(\mathbb T^3_{2\pi}\)、\(\nu>0\)。u 是同一无外力、不可压 NS 解，先在闭光滑区间 \([0,T]\) 计算。沿用 GD：
\[
 A_{ij}=\partial_j u_i,\quad Q=|A|_F,\quad B=A/Q\ (Q>0),\quad
 H=\nabla^2p,\quad L=\partial_t+u\cdot\nabla-\nu\Delta,
 \quad LA=-A^2-H.
 \tag{CD.1}
\]
设 \(d=\operatorname{dist}_F(A,\{\operatorname{rank}\le1\})\)、\(\tau=d/Q\)，并记
\[
 J=\operatorname{adj}A=(\operatorname{cof}A)^\top,\quad
 P=|J|_F^2,\quad f(A)=\frac{P}{Q^3}\ (Q>0),\qquad f(0)=0.
 \tag{CD.2}
\]
这里 P 是标量，不是谱投影。cofactor 采用对行列式的逐元素导数约定。d 的比较集合包含所有秩至多一的矩阵，不额外要求迹零。

若奇异值平方为 \(a\ge b\ge c\ge0\)，则 \(Q^2=a+b+c\)、\(d^2=b+c\)、\(P=ab+ac+bc\)。
由 \(a(b+c)\ge b^2+c^2\) 及 \(b^2+bc+c^2\ge0\)，得到
\[
 \boxed{\frac12\frac{d^2}{Q}\le f\le\frac{d^2}{Q},\qquad f\le\frac Q3.}
 \tag{CD.3}
\]
第一组不等式分别等价于 \(2P\ge Q^2(b+c)\) 与 \(P\le Q^2(b+c)\)；末式由 \(ab+ac+bc\le(a+b+c)^2/3\) 得到。Q=0 时按连续延拓解释。

f 在整个 \(Q>0\) 矩阵域光滑，包括非零秩一矩阵和重奇异值；它不是与 d 等价的线性偏离量，而是与 \(d^2/Q\) 等价。在原点它连续、全局 Lipschitz，但一般不可微。不能将一个分母光滑的表达式理解为全矩阵空间都光滑。

## 2. 伴随矩阵的完整演化

记 \(q_2=\operatorname{tr}(A^2)\)、\(A_k=\partial_kA\)。迹零条件给
\[
 J=A^2-\tfrac12q_2I,\qquad
 \Delta p=-q_2=2\operatorname{tr}J.
\]
这些是 PGR 已经使用的代数接口，不计作新的控制。直接使用 L 的乘积法则，先得
\[
 \begin{aligned}
 LJ={}&-2A^3-HA-AH-2\nu\sum_k A_k^2\\
 &+\left[\operatorname{tr}(A^3)+\operatorname{tr}(AH)
       +\nu\sum_k\operatorname{tr}(A_k^2)\right]I.
 \end{aligned}
\]
由 \(A^3=\tfrac12q_2A+(\det A)I\)、\(\operatorname{tr}(A^3)=3\det A\)，于是
\[
 \boxed{LJ=-q_2A+(\det A)I-HA-AH+\operatorname{tr}(AH)I
 -2\nu\sum_k\left[A_k^2-\tfrac12\operatorname{tr}(A_k^2)I\right].}
 \tag{CD.4}
\]
黏性乘积项是矩阵平方，不是 \(A_k^\top A_k\)，没有预先确定的矩阵正号。

若要单独标出惯性和压力，需要使用完整矩阵空间中的微分。对任意变分 V，在迹零 A 处有
\[
 DJ_A[V]=AV+VA-(\operatorname{tr}V)A-\operatorname{tr}(AV)I.
 \tag{CD.5}
\]
只有总变分 \(A^2+H\) 的迹为零；\(A^2\) 与 H 各自一般不是。因而
\(-DJ_A[A^2]=(\det A)I\)，而
\(-DJ_A[H]=-AH-HA-q_2A+\operatorname{tr}(AH)I\)。这与 CD.4 一致，不在拆项时漏掉 \((\operatorname{tr}V)A\)。

J=0 于某一点并不使 CD.4 的压力和空间导数项自动为零。这里没有证明整个秩一梯度类在 NS 下不变，也没有由一个点态生成项断言该类必定不变性失败。

## 3. 平方商的方程保留归一化项

在 Q>0，令 \(E=A^2+H\)、\(N=LJ\)。由
\(LP=2J:N-2\nu\sum_k|\partial_kJ|^2\) 及
\(LQ=-B:E-\nu Q|\nabla B|^2\)，可将商的每项写为
\[
 \begin{aligned}
 Lf={}&\frac{2J:N}{Q^3}+\frac{3P}{Q^4}B:E
       -\frac{2\nu}{Q^3}\sum_k|\partial_kJ|^2
       +\frac{3\nu P}{Q^3}|\nabla B|^2\\
 &-\frac{12\nu P}{Q^5}|\nabla Q|^2
       +\frac{12\nu}{Q^4}\sum_k(J:\partial_kJ)\partial_kQ.
 \end{aligned}
 \tag{CD.6}
\]
N 中仍包含 CD.4 的所有项。等价的链式表达为
\[
 Lf=-Df_A[E]-\nu\mathcal H_f,\qquad
 \mathcal H_f=\sum_kD^2f_A[A_k,A_k],\qquad
 Df_A[V]=\frac{2J:DJ_A[V]}{Q^3}-\frac{3P(A:V)}{Q^5}.
 \tag{CD.7}
\]
CD.6 与 CD.7 只在 Q>0 作为经典式成立。后文另行证明全域分布式，不能将零点代入商。

cofactor 是二次多项式，故 \(|DJ_A[V]|\le C Q|V|\)。结合 \(|J|\le Qd\)、\(d\le Q\)，CD.7 给 \(|Df_A|\le C\tau\)。其中 C 为固定维数常数，不依赖解或 T。

对迹零 A，取最佳秩一逼近 \(A=M+R\)，其中 \(|R|=d\)、\(|M|\le Q\)。因为 \(M^2=(\operatorname{tr}M)M\) 且 \(|\operatorname{tr}M|\le\sqrt3d\)，有
\(|A^2|\le(\sqrt3+3)Qd\)。因此完整矩阵微分的拆项满足
\[
 \boxed{|Df_A[A^2]|\le C d^2\le C Qf,\qquad
        |Df_A[H]|\le C\tau|H|.}
 \tag{CD.8}
\]
常数在最后一步可以增大。惯性源对该平方缺陷是二次的，压力源只有一阶的 \(\tau\)。这两项没有统一有利符号。

## 4. 用同一个正则化控制零集

以下论证不依赖选取奇异向量。设
\[
 f_\epsilon(A)=\frac{|\operatorname{cof}A|^2}{(Q^2+\epsilon^2)^{3/2}},\qquad
 \Phi_\epsilon(A)=\sqrt{Q^2+\epsilon^2}-\epsilon.
\]
在十维空间令 \(Z=(A,s)\)，并定义
\(G(Z)=|\operatorname{cof}A|^2/|Z|^3\)。G 在 \(Z\ne0\) 光滑，是一次正齐次函数。单位球紧致给 \(DG\) 和切向 Hessian 的统一界。Euler 恒等式给 \(D^2G(Z)Z=0\)，所以对任意 X，
\[
 |D^2G(Z)[X,X]|
 \le\frac K{|Z|}\left(|X|^2-\frac{(Z\cdot X)^2}{|Z|^2}\right).
\]
取 \(s=\epsilon>0\)、\(X=(V,0)\)，得到关键的逐点支配：
\[
 \boxed{|D^2f_\epsilon(A)[V,V]|
 \le K D^2\Phi_\epsilon(A)[V,V].}
 \tag{CD.9}
\]
K 只依赖固定多项式与维数。该证明同时给 \(Df_\epsilon\) 一致有界，以及 \(f_\epsilon\to f\) 一致，误差至多 \(C\epsilon\)。在 Q>0 有经典导数收敛；在 A=0，\(Df_\epsilon(0)=0\)。因此定义 \(Df_0=0\) 于 A=0，其余取 Df，仅用于全域源项。后文全域源项上界中的 \(\tau\) 也只在 Q=0 处取零；这不删除链式测度。

沿光滑 A，记 \(\mu_\epsilon^f=\sum_kD^2f_\epsilon(A)[A_k,A_k]\,dxdt\)。CD.9 给
\(|\mu_\epsilon^f|\le K\mu_\epsilon^A\)，右侧正是 GD 的非负 Frobenius 正则化密度。GD.4–5 的源项与能量上界保证统一有限质量。由链式方程与源项的支配收敛，\(\mu_\epsilon^f\) 的分布极限唯一，记为 \(\mu_f\)。正负支配的极限给
\[
 \boxed{Lf=-Df_0[A^2+H]-\nu\mu_f,\qquad
        |\mu_f|\le K\mu_A.}
 \tag{CD.10}
\]
在 \(Q>0\) 的紧子集上直接通过经典极限；其余测度只能支撑在零集。故
\[
 \mu_f=\mathbf1_{\{Q>0\}}\mathcal H_f\,dxdt+\sigma_f,
 \quad \operatorname{supp}\sigma_f\subseteq\{Q=0\},
 \quad |\sigma_f|\le K\zeta_A.
 \tag{CD.11}
\]
这里 \(\sigma_f\) 可以有符号，未证明其为零。固定闭光滑区间上，GD 的
\(\int\mu_\epsilon^A(t)\le\|\Delta A(t)\|_1\) 一致成立；右侧有界，排除时间端点聚集。该论证不假设候选奇异终点处已有光滑迹。

## 5. 积分的有界变差与弱测度终端迹

沿用 GD 的
\(E_0=\|u(0)\|_2^2/2\)、\(\mathcal B_A=\int Q(0)+(1+C_H)E_0/\nu\)，以及已冻结的固定周期压力接口 \(\|H(t)\|_1\le C_H\|A(t)\|_2^2\)。初始梯度成本保留；不对一般 L1 源声称 Riesz 变换 L1 有界。

对每个光滑 T，CD.8–11 和 GD.5 给
\[
 |Lf|(\mathbb T^3\times(0,T))
 \le C\int_0^T\!\!\int(d^2+\tau|H|)+\nu K\mu_A
 \le C\mathcal B_A.
\]
式中的 \(\mu_A\) 表示同一时空区间的质量。设 \(m(t)=\int f(A(t))\)，全域输运与 Laplacian 积分为零，因此
\[
 \boxed{0\le m(t)\le\mathcal B_A/3,\qquad
        \operatorname{Var}_{(0,T)}m\le C\mathcal B_A.}
 \tag{CD.12}
\]
当 \(T\uparrow T_*<\infty\) 时仍有统一界，m 具有有限单侧终端极限。这不是说 \(\partial_tf\) 是时空有限测度：Lf 中还包括输运和扩散。也没有证明 f 的强 L1 终端迹、矩阵 A 的迹、或临界范数有界。相似的整胞质量变差也可由 GD 的 Q 方程推出；CD.12 不应夸大为新临界时间机制。

更准确地，对每个固定光滑周期测试函数 \(\phi\)，分布意义下有
\[
 \frac d{dt}\int\phi f=\int\phi\,Lf+\int fu\cdot\nabla\phi
                         +\nu\int f\Delta\phi.
 \tag{CD.13}
\]
第一项由有限测度控制。第二项由 \(f\le Q/3\)、\(u\in L^\infty_tL^2_x\)、\(Q\in L^2_tL^2_x\) 及有限 \(T_*\) 控制，第三项由 \(m\le\mathcal B_A/3\) 控制。故每个固定测试积分均有统一有限变差和终端左极限；这里的界依赖 \(\|\phi\|_{C^2}\)、\(T_*\)、\(\nu\) 与已有初值常数。

由于 \(f\ge0\) 且质量统一有界，紧周期胞上的弱星紧性与光滑测试的稠密性给唯一有限非负测度 \(\eta_*\)，使 \(f(A(t))\,dx\stackrel{*}{\rightharpoonup}\eta_*\) 当 \(t\uparrow T_*\)。这是真实的弱时间迹结论；未证明 \(\eta_*\) 对体积测度绝对连续，也没有排除质量集中，不能将它写成强 L1 收敛或正则性。

## 6. 相容速度梯度也没有点态黏性正号

下面只检验 CD.7 的 \(\mathcal H_f\)，不检验 Lf 总符号。在原点附近取
\(u=(x_1+x_2x_3,-x_2-x_1x_3,0)\)。它等于
\(\operatorname{curl}(0,0,\psi)\)，其中
\(\psi=x_1x_2+(x_1^2+x_2^2)x_3/2\)。原点处
\(A_0=\operatorname{diag}(1,-1,0)\)、\(A_3=E_{12}-E_{21}\)、\(A_1=-E_{23}\)、\(A_2=E_{13}\)。
沿三条矩阵直线直接计算，
\[
 \begin{aligned}
 f(A_0+tA_3)&=\frac{(1-t^2)^2}{[2(1+t^2)]^{3/2}},\\
 f(A_0+tA_1)=f(A_0+tA_2)&=\frac{1+t^2}{(2+t^2)^{3/2}},\\
 \mathcal H_f(0)&=-\frac7{2\sqrt2}+\frac1{4\sqrt2}+\frac1{4\sqrt2}
                 =-\frac3{\sqrt2}<0.
 \end{aligned}
 \tag{CD.14}
\]
取光滑截断 \(\chi\) 紧支撑于周期胞内部且在原点邻域为一，用 \(\operatorname{curl}(0,0,\chi\psi)\) 即可得到光滑周期、无散、均值零的初值，并保持上述点的全部导数。它可作为局部光滑原 NS 解的初值。

这不是任意不相容矩阵的例子，也不是全域黏性积分、总时间导数或 NS 奇点的反例。它只排除“归一化商在所有真实速度梯度上自带逐点非负黏性密度”的说法。CD.9–11 的有符号控制正好保留了这个事实。

## 7. 本节没有得到什么，下一步检查什么

CD.3 使 f 继承 GD.14 的 \(2/p+3/r=3\) 空间插值线；再用 \(f\le Q/3\) 与 \(Q\in L^2_tL^2_x\)，上述范数的直接插值仍只能达到指数和至少 \(5/2\)。GD.11 要求的线是 \(2/p+3/r=2\)，并且对象是 d，不是 f。上述积分 BV 与弱测度迹没有排除局部集中，也没有弥补这项差别。

压力式 \(H=2\nabla^2\Delta^{-1}\operatorname{tr}J\) 中逆 Laplacian 作用于均值零周期源，它只重写了非局部项；不能据此将 \(\tau|H|\) 点态改成 \(Cd^2\)，或自动得到带退化权的奇异积分界。PGR 中压力与惯性的旧四次抵消也不是 CD.7 的正耗散。没有证明这些未列出的估计一概不可能，只是本节尚未得到。

下一步仍保留 GD 的 d 与临界目标，优先检查线性余子式商 \(k=|J|/Q\)，它由 CD.3 满足 \(d/\sqrt2\le k\le d\)。这是拟检验对象，不是已接受的新估计。应先处理 \(J=0\) 与 \(Q=0\) 的非光滑链式项，识别可保留的正耗散，检验剩余负项能否由已有熵控制，再明确压力成本。只有得到超出已有亚临界范数的控制，才可能用于 GD.11；不另扫权重、不预设秩一类不变，也不把 k 的重命名当成果。

本节由主任务与两位参与推导的 AI 审读者复算；具体实际文件审读范围另列。普通检索仅用了两项余子式／秩一关键词查询，没有采用检索结果中的数学定理，也未作全面 Deep Research、原创性认证或新原著证明审查。已有压力接口和条件延拓按 GD 及其冻结来源继承。没有仿真、DGX、数值证书、科学附图、第三方 PDF 或读者 HTML/PDF；无需大里程碑回顾。完整材料保持私有。
