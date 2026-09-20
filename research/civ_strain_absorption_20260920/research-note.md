# 平均应变的耗散吸收：两个候选的有界检验

2026-09-20。PRIVATE_CORE / INTERNAL_CHECKPOINT / OPEN / NOT CLAY。

本轮从 `e268a9e06f668864c450a84b6864c03b73812a4c` 续接，只比较两个明确候选，选择高角模耗散作完整推导。结果是一个有条件、带完整注入项的高模能量不等式，没有得到新的无条件临界控制。各向异性分量权重在初筛后停止。这里记录精确缺口，不新增独立研究章节、冻结包或发布交接，也不判断一般正则性的真伪或正反路线的成功概率。

## 1. 对象与候选选择

沿用 [上一轮笔记](../civ_feedback_20260920/research-note.md) CF.14–15。固定正黏性、同一无外力周期解、同一允许初值；把周期场提升到空间，在绕固定轴旋转不变的局部球 \(\Omega=B_R((0,0,z_0))\) 内工作。旋转平均 \(\Pi\) 是局部协变平均，不是 Leray 投影，也不假定任意旋转保持方形周期胞。

令 \(v=\Pi u\)、\(w=u-v\)、\(q=p-\Pi_{\rm scalar}p\)。下列等式只在终点前光滑时间区间成立；延伸到疑似奇异终点所需的一致可积性必须另证。原余项方程是已核输入，不计作本轮新结果：

\[
w_t-\nu\Delta w+(v\cdot\nabla)w+(w\cdot\nabla)v
 +(I-\Pi)\operatorname{div}(w\otimes w)+\nabla q=0.
\tag{SA.1}
\]

| 候选 | 要检验的增益 | 本轮处理 |
| --- | --- | --- |
| A：协变高角模耗散 | 以角频谱隙吸收平均场的不利应变 | 选定并完整保留跨模、压力及截止项推导 |
| B：\(D=\operatorname{diag}(1,1,s^h)\) 分量权重 | 平衡经向导数并利用权重阻尼 | 初筛揭示旋流与内部压力缺口，不继续扩展 |

以下使用 CF.2 的地方，都额外假定当前平均场满足那里指定的结构界；没有从一般无力解推出这些界，也没有断言它已满足 CIV 定理的其余假设。

## 2. 候选 A：协变角模的精确谱隙

固定整数 \(N\ge2\)。令 \(P_H\) 保留圆柱**分量**的 \(|m|\ge N\) 模，\(z_H=P_Hw\)，\(\ell=w-z_H\)，\(q_H=P_H^{\rm scalar}q\)。实场的正负复模成对保留，低模为 \(1\le |m|<N\)。

第 \(m\) 模的分量记为 \((a_r,a_\theta,a_z)e^{im\theta}\)。对 Cartesian 向量求角导数，必须同时微分柱坐标基矢，得到二次型

\[
Q_m=|im a_r-a_\theta|^2+|a_r+im a_\theta|^2+m^2|a_z|^2
=\frac{(m+1)^2}{2}|a_r+i a_\theta|^2
 +\frac{(m-1)^2}{2}|a_r-i a_\theta|^2+m^2|a_z|^2.
\tag{SA.2}
\]

所以 \(m=1,a_\theta=i a_r,a_z=0\) 有零角耗散；\(m=-1\) 有对应共轭极化。这是水平平移向量的柱坐标表达。不能把标量 \(m^2/r^2\) 谱隙直接套到整个非轴对称向量余项，也不能由 \(\Pi w=0\) 推出正的 \(r^{-2}\) Poincaré 界。

取实值、旋转不变的 \(\chi\in C_c^\infty(\Omega)\)，允许光滑依赖时间。逐圈 Parseval 给出

\[
D_H:=\int\chi^2|\nabla z_H|^2
\ge (N-1)^2\int\frac{\chi^2|z_H|^2}{r^2}.
\tag{SA.3}
\]

先在 \(r>0\) 推导，再由光滑性和非负积分极限处理轴线；未在轴上额外施加未知边界条件。

## 3. 高模局部能量：保留真实注入

协变投影与 Laplacian、时间微分以及对应的梯度、散度交换。轴对称 \(v\) 使两个平均场线性项保持角模。因此

\[
(z_H)_t-\nu\Delta z_H+(v\cdot\nabla)z_H+(z_H\cdot\nabla)v
 +P_H\operatorname{div}(w\otimes w)+\nabla q_H=0.
\tag{SA.4}
\]

三个向量场 \(w,z_H,\ell\) 均无散。因为 \(\chi\) 旋转不变，\(\chi^2z_H\) 仍在高模空间，能量配对时可移去非线性项前的 \(P_H\)。分解 \((w\cdot\nabla)w=(w\cdot\nabla)z_H+(w\cdot\nabla)\ell\)，得到

\[
\frac12 E_H'+\nu D_H
=-\int\chi^2(z_H\otimes z_H):S(v)+T_H+B_H,
\qquad E_H=\int\chi^2|z_H|^2,
\tag{SA.5}
\]

\[
T_H=-\int\chi^2z_H\cdot(w\cdot\nabla)\ell
=-\int\chi^2(z_H\otimes z_H):\nabla\ell
 -\int\chi^2z_H\cdot(\ell\cdot\nabla)\ell,
\tag{SA.6}
\]

\[
B_H=\frac12\int(\partial_t\chi^2+\nu\Delta\chi^2+u\cdot\nabla\chi^2)|z_H|^2
 +\int q_H z_H\cdot\nabla\chi^2.
\tag{SA.7}
\]

约定 \((\nabla v)_{ij}=\partial_jv_i\)，\(S(v)=(\nabla v+\nabla v^T)/2\)。输运截止速度是完整的 \(u=v+w\)，不是仅 \(v\)。压力只化为局部边界通量，没有消失。\(T_H\) 没有确定符号。

令

\[
\sigma_-(v)=\max(0,-\lambda_{\min}(S(v))),\qquad
\Lambda_\chi(t)=\operatorname*{ess\,sup}_{\{\chi\ne0\}}r^2\sigma_-(v).
\]

由 SA.3 逐时有

\[
-\int\chi^2(z_H\otimes z_H):S(v)
\le\frac{\Lambda_\chi(t)}{(N-1)^2}D_H.
\tag{SA.8}
\]

若固定 \(0<\eta<1\) 且 \(\Lambda_\chi\le\eta\nu(N-1)^2\)，则

\[
\frac12E_H'+(1-\eta)\nu D_H\le T_H+B_H.
\tag{SA.9}
\]

这是真实动态的、带注入项的不等式，不是无条件衰减。若支撑上 \(r\le R_\chi\)，左侧耗散另控制 \((1-\eta)\nu(N-1)^2E_H/R_\chi^2\)。固定黏性的 NS 抛物缩放保持无量纲比 \(r^2\sigma_-/\nu\)。

## 4. CIV 粗界给出的充分门槛会移动

在 CF.2 的结构假设下，\(s=-t\in(0,1)\)、固定 \(0<h<1/2\)，有上包络 \(\|S(v)(-s)\|_\infty\le C s^{-1-h}\)。此上包络不可积，不意味着实际应变积分必发散。

在每个二进时间窗 \(I_j=(-s_j,-s_j/2)\) 内固定 \(\chi_j,N_j\)，取 \(\operatorname{supp}\chi_j\subset\{r\le c\sqrt{s_j}\}\cap\Omega\)。于是

\[
\Lambda_{\chi_j}(t)\le c^2 C2^{1+h}s_j^{-h},\qquad
N_j-1\ge\left(\frac{c^2 C2^{1+h}}{\eta\nu}\right)^{1/2}s_j^{-h/2}
\tag{SA.10}
\]

是保证吸收的一种充分选择。沿用 CIV 单位黏性归一化时取 \(\nu=1\)；显示固定 \(\nu\) 只是保留耗散系数，结构常数须按所选归一化解释，不能逐尺度改变黏性。

SA.10 不说实际应变必达粗界，也不说实际角频必须如此增长。它说：仅凭当前输入保证吸收，得到的门槛趋向无穷，未控低角模区随之扩大。提高阈值带来的高模能量下降只是模式改归低区，不能当成物理耗散。这里没有把 \(N(t)\) 当作可无代价微分的投影；移动空间截止时 SA.7 的时间项同样必须保留。

## 5. 没有闭合的项，具体缺在哪里

即便只估计 SA.6 第一项，令
\(K_\ell(t)=\|\nabla\ell\|_{L^2(\operatorname{supp}\chi)}\)、
\(F_\chi(t)=\int|\nabla\chi|^2|z_H|^2\)。将 \(\chi z_H\) 零延拓，用三维 GN 与 Young 得

\[
\begin{aligned}
\left|\int\chi^2(z_H\otimes z_H):\nabla\ell\right|
&\le K_\ell\|\chi z_H\|_4^2\\
&\le C K_\ell E_H^{1/4}(D_H+F_\chi)^{3/4}\\
&\le\varepsilon\nu D_H+\varepsilon\nu F_\chi
 +C_\varepsilon\nu^{-3}K_\ell^4 E_H.
\end{aligned}
\tag{SA.11}
\]

原能量类仅保证梯度平方的时间可积性，不保证这里的四次方可积。角频低不等于完整空间频率低：径向和轴向振荡没有随角模截断而消失。把 \(\int K_\ell^4dt\) 再列为假设，只是重新引入未知临界控制，不是本轮得到的动态增益。

SA.6 第二项保留低模向高模的非线性注入；SA.7 保留压力及三次边界通量。固定窗口上的可积性也不能自动给出随窗口缩小仍一致的尺度归一界。本轮没有证明这些有符号配对存在抵消，也没有证明抵消不可能。

因此没有从 SA.9 推出全余项的临界范数，更没有推出 PF 在同一指定中心、共同有限 \(M\) 下原 \(\mathsf A,\mathsf E,\mathsf K\) 的好尺度。高模谱隙本身不能填上这个缺口。

## 6. 候选 B：分量权重为何没有胜出

在同样的光滑区间，取固定旋转不变截止，\(a=s^{2h}\)、\(D=\operatorname{diag}(1,1,s^h)\)、\(M_D=D^2\)、\(Z=Dw\)。这里矩阵 \(M_D\) 与 PF 的有限常数 \(M\) 无关。由 SA.1 测试 \(\chi^2M_Dw\) 得

\[
\begin{aligned}
\frac12\frac d{dt}\int\chi^2|Z|^2+\nu\int\chi^2|\nabla Z|^2
 +\frac hs\int\chi^2|Z_z|^2
={}&-\int\chi^2M_Dw\cdot(w\cdot\nabla)v+\mathcal P_D+\mathcal B_D,\\
\mathcal P_D={}&(a-1)\int\chi^2q\,\partial_zw_z,\\
\mathcal B_D={}&\frac12\int(\nu\Delta\chi^2+u\cdot\nabla\chi^2)|Z|^2
 +\int qM_Dw\cdot\nabla\chi^2.
\end{aligned}
\tag{SA.12}
\]

\(D\) 空间常数且与协变平均交换，平均投影项仍消去；\(M_Dw\) 却不再无散，因此产生内部压力项。正的时间权阻尼来自 \(a'=-2hs^{2h-1}\)。

完整应变密度是

\[
\begin{aligned}
M_Dw\cdot(w\cdot\nabla)v={}&(\partial_rv_r)Z_r^2+(v_r/r)Z_\theta^2+(\partial_zv_z)Z_z^2\\
&+(\partial_rv_\theta-v_\theta/r)Z_rZ_\theta\\
&+(s^{-h}\partial_zv_r+s^h\partial_rv_z)Z_rZ_z
 +s^{-h}(\partial_zv_\theta)Z_\theta Z_z.
\end{aligned}
\tag{SA.13}
\]

CF.2 只将经向 \(r\)–\(z\) 交叉系数平衡至 \(Cs^{-1}\)。两个旋流系数仍允许 \(Cs^{-1-h}\)，所以不能说全部应变已降至 \(C/s\)。即使额外无旋流，用轴向阻尼吸收交叉项也会留下 \(C^2|Z_r|^2/(2hs)\)，并无现成小常数或终端可积性。

压力方面必须使用较好的基本估计，而不能夸大退化损失。无散性给

\[
\mathcal P_D=(1-a)\int\chi^2q\,\operatorname{div}_H w_H,
\quad
|\mathcal P_D|\le\varepsilon\nu\int\chi^2|\nabla_Hw_H|^2
 +\frac{C(1-a)^2}{\varepsilon\nu}\int\chi^2q^2.
\tag{SA.14}
\]

这里 \(w_H=(w_1,w_2)\) 表示水平分量，不是第 2 节的高模 \(z_H\)。SA.14 没有必要的 \(s^{-2h}\) 损失，但原能量/适当弱解输入不提供终端 \(L^2_{t,x}\) 压力控制。局部压力还含平均场—余项混合源与谐和余项；不能当作纯 \(w\otimes w\) 的全局周期 Riesz 变换并删去局部边界信息。

此外，时间权正项已满足

\[
\int_{-s_0}^{0}h s^{2h-1}\|\chi w_z(t)\|_2^2dt
\le\frac{s_0^{2h}}2\sup_{-s_0<t<0}\|\chi w_z(t)\|_2^2.
\tag{SA.15}
\]

它本身不是新增临界控制，退化的加权梯度也不能替代 PF 完整梯度耗散。本轮不继续候选 B。

## 7. 文献去重与结论边界

[Liu–Zhang，2305.05272v1](https://arxiv.org/html/2305.05272v1) 已对指定的大角模初值族建立全空间无力 NS 稳定性；所需剖面、分量缩放及模和控制不能移除。[Liu–Liu–Zhang，2406.05329v1](https://arxiv.org/html/2406.05329v1) 在圆柱域对另一指定高模族给出结果，也有明确结构与小量条件。因此“角频够高时耗散增强”不是本轮新机制；这些定理不直接覆盖此处任意局部余项。所核范围是主定理、相关假设和公式，不是两篇全文证明的独立验收。第二篇题名中的各向异性黏性不同于候选 B 的时间退化度量。

本地旧稿中的速度方向角向耗散、两点球面矩和标量加权熵，分别不是本轮的柱坐标模谱隙或矩阵权恒等式。有限查重不等于全面新颖性证明。

这轮实际回答了：高角模能否吸收平均应变——在 SA.8 的明确条件下可以；现有输入能否把它闭合成真实全解的临界控制——没有。具体缺失为不断扩大的低模区控制、SA.6 的有符号跨模通量估计，以及 SA.7 的尺度一致局部压力/输运控制。

下次不能把 SA.3、SA.9 或再命名的 \(K_\ell^4\) 假设计作新进展。若续接本候选，先针对 SA.6 的实际有符号配对证明可由原输入推出的统一界，并同时处理低模及边界；当前没有已选定、已能闭合该步骤的估计。一般 B 仍开放，亦未证明 B 自动推出全空间 A。反向的固定热补全残差由其任务独占，本轮没有读取其恢复索引、计算其残差、运行仿真或变更发布。
