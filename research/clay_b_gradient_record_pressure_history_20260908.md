# 梯度纪录序列的压力时间项：已控尾部与中间尺度

2026-09-08。GPH，PRIVATE_CORE，内部原结构检查。沿用 [GRC](clay_b_gradient_record_compactness_20260908.md) 的同一周期 NS 原解、固定正龄 a、原黏性及真实移动参考系，不另造解族。

本轮完成三项核算：时间累计压力 Hessian 的空间振荡受控；兼容性使其源演化中的黏性项可以统一估计；固定物理远场和足够早的完整非线性历史可以剥离。但平均对称应变的时间模量仍未得到，非零仿射来源仍未排除。没有新的无条件临界估计。

## 1. 时间累计量只剩一个空间常矩阵

沿用 GRC 的 \(r_n=N_n^{-1/2}\)、\(L_n=r_n^{-1}\)、\(v_n,G_n,\pi_n\)，并记
\[
 H_n=\nabla^2\pi_n,\quad f_n=\operatorname{tr}(G_n^2),\quad
 H_n^0=\operatorname{STF}H_n,\quad
 P_{n,I}=\int_I H_n^0(s)\,ds,\quad M_n(I)=\int\psi P_{n,I}.
 \tag{GPH.1}
\]
STF 表示对称迹零部分。固定径向 \(\psi\ge0\)，支于 \(B_1\)，积分为1。I 为固定过去柱内长度 h 的时间段；只讨论实际存在于该柱的充分大 n。目标是 \(M_n(I)\) 的一致短时间趋零，而非每个 n 单独的光滑性。

令 \(F_{n,I}=\int_I f_n\)，则 \(\|F_{n,I}\|_\infty\le h\)，且
\(P_{n,I}=\operatorname{STF}D^2\Gamma_{L_n}*F_{n,I}\)。
固定 \(R_0\ge1\)。将源切成 \(B_{4R_0}\) 内的近源与 \(B_{2R_0}\) 外的远源，平滑过渡。周期二阶 Riesz 算子的 L2 界与胞尺度无关，故近源输出的 L2 范数不超过 \(ChR_0^{3/2}\)。远源输出减去其在0处的值，用完整差核 \(Cd_{L_n}^{-4}\) 积分，得到 \(B_{R_0}\) 上的 \(Ch\) 界。再减去实际 \(\psi\)-平均，得
\[
 \|P_{n,I}-M_n(I)\|_{L^2(B_{R_0})}
 \le C_{\psi,R_0}h.
 \tag{GPH.2}
\]
近源 L2 算子包括接触项；远源差核包括全部周期副本。这个证明不要求源有时间连续性。它是经典奇异积分振荡估计的直接应用，不认领新颖性。

但空间常矩阵恰是 GRC 尚缺的部分。GRC.21 与完整核绝对值界只给
\[
 |M_n(I)|\le
 \min\{2+C_{\nu,\psi}h,\ C_\psi h(1+\log L_n)\}.
 \tag{GPH.3}
\]
这不是统一的 \(o(1)\)。GPH.2 中减常矩阵只是空间振荡估计，不是允许删除二次压力的 NS 规范变换，也不是压力 p 本身的 BMO 界。

## 2. 原 Poisson 源的完整演化

本节暂省下标 n。设 \(S=\operatorname{sym}G\)、\(\mathcal L=\partial_s+v\cdot\nabla-\nu\Delta\)。由 \(\mathcal LG=-G^2-H\) 逐项微分，
\[
 \mathcal L f=-2\operatorname{tr}G^3-2S:H
 -2\nu\sum_k\operatorname{tr}((\partial_kG)^2).
 \tag{GPH.4}
\]
最后一项有符号，不是 \(-2\nu|\nabla G|^2\)。梯度兼容性及无散性给
\[
 \sum_k\operatorname{tr}((\partial_kG)^2)
 =\partial_i\partial_j(GG^\top)_{ij}.
 \tag{GPH.5}
\]
证明：展开右端，含 \(\partial_iG_{ik}=\partial_k\operatorname{div}v\) 的项为零；其余为
\(\sum_{i,j,k}(\partial_jG_{ik})(\partial_iG_{jk})\)，交换混合偏导后即左端。这不依赖矩阵正定或舍弃零点。

取固定光滑矩阵核 \(K=\operatorname{STF}(D^2\Gamma_L*\psi)\)，令
\(\mathcal A(s)=\int K f=\int\psi\,\operatorname{STF}H\)。
两次周期分部积分得到逐分量精确公式
\[
 \begin{aligned}
 \mathcal A'={}&\int(v\cdot\nabla K)f+\nu\int(\Delta K)f
 -2\int K\operatorname{tr}G^3-2\int K\,S:H\\
 &-2\nu\int(\partial_i\partial_jK)(GG^\top)_{ij}.
 \end{aligned}
 \tag{GPH.6}
\]
这是移动坐标里的固定核演化。参考系加速的线性压力 Hessian 为零，已经保留在原方程中；不能再向 GPH.6 重复添加一个卷积物质导数交换子。

因 \(\Delta K=-\operatorname{STF}D^2\psi\) 且 \(\|D^2K\|_1\le C_\psi\)，两项黏性贡献满足
\[
 \left|\nu\int\Delta K f
 -2\nu\int\partial_i\partial_jK(GG^\top)_{ij}\right|
 \le C_\psi\nu.
 \tag{GPH.7}
\]
这里 \(|G|\le1\)，近处由 \(\psi\) 光滑化，远处的核四阶导数为 \(Cd_L^{-5}\)，故常数不依赖 L。若改用 \(K_{\rm far}=(1-\chi_R)K\)，其中 \(2\le R\ll L\)，全部截止导数也只产生 \(C_\psi\nu R^{-2}\)。因此长度 h 的远区黏性累计为 \(O_\psi(\nu hR^{-2})\)。

输运和三次项目前只得到
\(\int d_L|\nabla K|+\int|K|\le C_\psi(1+\log L)\) 的粗界。
压力反馈则完整保留为
\[
 \int K_{ab}S:H
 =-\int(\partial_iK_{ab})G_{ij}\partial_j P,
 \tag{GPH.8}
\]
P 是规范周期压力。用到 \(\partial_iG_{ij}=0\)；压力梯度可减一个空间常向量，但真实梯度差不能删除。此次移导没有给这个反馈的统一时间预算，也没有证明它与输运、三次项的有符号组合抵消。GPH.7 是可估计项的细化，不是正耗散或临界增益。

## 3. 固定物理远场确实可以剥离

以下用原变量 \(G(t,x)=\nabla u(t,x)\)，令
\(D_a=\int_a^{T_*}\|G(t)\|_2^2dt<\infty\)。
固定小 \(\rho>0\)，取围绕真实 \(X_n(t)\) 的平滑远源截止，在距离小于 \(\rho\) 为零、大于 \(2\rho\) 为一。若 \(r_n<\rho/2\)，在 \(\psi\) 的支集内，远源与观察点分离至少 \(\rho/2\)。原完整周期 Hessian 核在这里不超过 \(C\rho^{-3}\)；接触项不参与。

原源 \(f=\operatorname{tr}G^2\) 满足 \(\|f(t)\|_1\le\|G(t)\|_2^2\)。由 \(H_n=r_n^4H\)、\(ds=r_n^{-2}dt\)，任意实际时间集合 J 都有
\[
 \int_J\left|\int\psi H_n^{\rm far}\right|ds
 \le C_\psi\rho^{-3}r_n^2
 \int_{t(J)}\|G(t)\|_2^2dt
 \le C_\psi\rho^{-3}r_n^2D_a\longrightarrow0.
 \tag{GPH.9}
\]
这里甚至可以取完整左端历史。没有微分移动截止，所以没有漏掉 \(X_n'\) 的边界项。

必须先固定 \(\rho\)。若令 \(\rho=r_nR\)，右侧变成 \(CL_nR^{-3}D_a\)，便不能继续称作趋零。另一方面，在固定放大半径 R 内，平滑平均核和 \(|f_n|\le1\) 给近源长度 h 累计不超过 \(C_\psi h(1+\log R)\)。于是尚未受控的范围是
\[
 r_nR\lesssim |z-X_n(t)|\lesssim\rho.
 \tag{GPH.10}
\]
固定 \(\rho\) 时，原空间外半径不变，放大外半径 \(\rho/r_n\) 趋于无穷。随后令 \(\rho\downarrow0\)，才能把剩余范围限制到任意小的原空间邻域；不能交换这一顺序。这里只定位可能的剩余贡献，没有证明它实际集中、非零或消失。

## 4. 完整固定历史的梯度核尾

为使用原能量，先不用减中心速度的 v，而在固定坐标写
\[
 \begin{aligned}
 U_n(y,s)&=r_nu(x_n+r_ny,t_n+r_n^2s),&
 Y_n(s)&=(X_n(t)-x_n)/r_n,\\
 \sigma_n&=(a-t_n)L_n^2,&
 \sup_s\|U_n(s)\|_2^2&\le L_n E_a,\quad
 E_a=\sup_{a\le t<T_*}\|u(t)\|_2^2.
 \end{aligned}
 \tag{GPH.11}
\]
全部空间范数使用未归一化周期测度。对原完整投影 mild 式微分，再沿 \(Y_n(s)\) 评价，得到
\[
 \begin{aligned}
 G_n(0,s)={}&
 [e^{\nu(s-\sigma_n)\Delta}\nabla U_n(\sigma_n)](Y_n(s))\\
 &-\int_{\sigma_n}^{s}
 [\mathcal J_{L_n,\nu}(s-\tau)*(U_n\otimes U_n)(\tau)](Y_n(s))\,d\tau,\\
 \mathcal J_{L,\nu}(\tau)&=\nabla e^{\nu\tau\Delta_L}\mathbb P_L\operatorname{div}.
 \end{aligned}
 \tag{GPH.12}
\]
这里只移动评价点，没有把变均值场的全胞能量当成 \(L_nE_a\)。完整压力在 Leray 核中，不能删去原非线性历史。
对每个固定 n，近 \(\tau=s\) 时可先把一个空间导数落在光滑的 \(U_n\otimes U_n\) 上，使用周期速度核的 \(L^1\) 界 \(C[\nu(s-\tau)]^{-1/2}\)，再移回导数以解释 GPH.12。该步不提供关于 n 一致的近对角小量；下文的无穷范数积分只用于分离于顶端的旧尾。

全空间核可写为热核二阶导数加上从 \(\nu\tau\) 到无穷的热核四阶导数积分。Gaussian 导数界给
\[
 |\mathcal J_{\mathbb R^3,\nu}(x,\tau)|
 \le C(|x|^2+\nu\tau)^{-5/2},\qquad
 \|\mathcal J_{L,\nu}(\tau)\|_\infty
 \le C[(\nu\tau)^{-5/2}+L^{-5}].
 \tag{GPH.13}
\]
第二式由绝对周期化得到；五次幂副本和在三维可和。这是 [BI §2/§5](clay_b_fixed_history_mild_preflight_20260906.md) 的速度核多微分一次，不把旧 mild 方法改称新机制。

初值项至多 \(r_n^2\|G(a)\|_\infty\)。对固定 H、\(s\in[-H,0]\)、\(2H\le A<-\sigma_n\)，旧历史部分满足
\[
 \left|\int_{\sigma_n}^{-A}
 [\mathcal J_{L_n,\nu}(s-\tau)*(U_n\otimes U_n)(\tau)](Y_n(s))\,d\tau\right|
 \le CE_a\left[\nu^{-5/2}L_n A^{-3/2}
 +(T_*-a)L_n^{-2}\right].
 \tag{GPH.14}
\]
积分使用 \(s-\tau\ge A-H\ge A/2\)，周期修正的长度不超过 \((T_*-a)L_n^2\)。
因此，取
\[
 A_n=L_n^{2/3+\eta},\quad0<\eta<4/3,
 \qquad A_n\to\infty,\quad r_n^2A_n=L_n^{-4/3+\eta}\to0,
 \tag{GPH.15}
\]
初值及更早的尾部一致趋零。它只把中心梯度的来源压到一个增长的归一化窗口；该窗口的非线性贡献没有消失。不能将增长窗口之外的尾小性改说成固定窗口之外的尾小性，也不能据此排除非零仿射历史。

## 5. 两个压力规范接口均未取得其前提

[Fernández-Dalgo–Lemarié-Rieusset，v1 Theorems 1–2](https://arxiv.org/html/2001.10436v1) 在三维要求速度的时空加权平方可积，空间权为 \((1+|x|)^{-4}\)，才将压力力的剩余部分限制为空间常向量的时间导数。GRC 的线性增长界不保证这一条件：非零线性场在远处的径向积分发散。有限周期项分别有此可积性，不代表扩张极限继承统一预算。

[Cobb，v1 Theorem 4.1、Remark 4.2](https://arxiv.org/html/2105.03257v1) 保留速度 \(L^2_tL^\infty_x\) 及低频时间连续性，并用低频消失条件识别投影方程。这里不能用梯度有界替代速度假设。未采用 v2 的 bounded Euler 定理作为 NS 输入，也不把 Hessian 的空间振荡控制误称压力的 BMO 规范。

这两项只用于审查准入条件，不移植未满足假设的定理。[AH](clay_b_affine_reference_pressure_20260908.md) 已包含有源压力尺度递推、仿射参照抵消和未控调和尾；本轮没有重做其局部反例，也没有据此否定所有仿射方法。

## 6. 判断与后续限制

原结构核算没有闭合 GRC 的时间模量目标。可以保留 GPH.2、7、9、14 的准确范围；不能把空间振荡界、可积黏性项、增长窗口尾或固定物理远场消失合称“压力已受控”。

按 GRC 的停止条件，停止仅凭现有 \(|G_n|\le1\)、能量和定性迹，继续改写该平均压力时间项的具体入口。不再新增相邻对数估计、同义低频条件或宽仿射例子来增加研究计数。原问题仍可由新的实质动力学输入重开；这不是不可能性定理。

下一步回到同一任意初值原解的临界控制问题，先核对旧稿，再选择能直接约束中间尺度贡献、或绕开此强紧性缺项的不同机制。新的具体替代目标尚未选定，不能把这个选择要求写成已有估计。仍须保留原正龄、完整历史、压力与边界，不能用额外假设替代一般 NS 量词。

主任务全文读 GRC、BI、AH，直接推导所写核与源公式；两位协作者分别独立核源演化、历史尾，另一位核空间振荡与外部适用范围。主任务实际读两篇外部定理的陈述，另读 Cobb §4 的证明；没有重审它们全部上游依赖。实际成稿审读范围另记检查点。普通定向查询不是 Deep Research 或充分查新。

一般 NS / Clay 仍 OPEN / NOT CLAY。TG 仍为最后独立冻结；没有新独立小节、release、交接、发布、读者文件、翻译、recap、仿真、DGX 或科学附图。仅私人研究记录与参与式 AI 核查，非真人同行评审。
