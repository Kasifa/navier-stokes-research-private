# 固定 Gaussian 配对的真实波应力连接

2026-09-20，PRIVATE_CORE。Hume 为本稿作者，非原文作者；参与过增长与 CIV 来源审查，收到根的角投影／周期像及本桥任务提示，非盲。只在本合同固定场、固定 φ、固定热时间下作手推；原外部构造及其所述估计为条件输入，不重证整篇存在性。未读本题另两作者形成稿。

**结论。** 对原全空间场的真正非轴对称部分，下面的加权连接成立；首系数由原主应力给出，本文不判断其符号，不据此单独宣布完整 J 或完整残差的首系数。

## 1. 对象与待证式

令 Π 为绕 z 轴旋转的向量协变角平均，\(w=(I-\Pi)u\)，其中 u 是原同一局部化全空间场，时间为 \(1-\tau\)。记 \(A=1/2+h,D=1/2-h,\epsilon=\tau^h,S=g_1*\)，以及
\[
w_\tau(Y)=\lambda_p\tau^A w(\sqrt\tau Y,1-\tau),\quad
\psi=S\phi=\psi_\theta(r,z)e_\theta,\quad
\mathscr D\psi=\partial_r\psi_\theta-\psi_\theta/r.
\tag{WB.1}
\]
ψθ 对 z 偶，ψ 及其固定阶导数在远处有 Gaussian 衰减；轴上的表达取其光滑笛卡尔延拓。原 (7.30) 的主应力第一分量记为 \(T_{0,\theta}(X,\eta)\)。要证
\[
\lim_{\tau\downarrow0}\epsilon^{-1}\int_{\mathbb R^3}
\{S(w_\tau\otimes w_\tau)-(Sw_\tau)\otimes(Sw_\tau)\}:\nabla\phi
=\lambda_p^2\int_{\mathbb R^3}T_{0,\theta}(r^2/2,0)\,\mathscr D\psi\,dY.
\tag{WB.2}
\]
所有积分用通常 Lebesgue 测度；角平均用归一化 Haar，故圆柱积分的 2π 仍包含在右端 dY 中。两个有序 rθ 项合成 \(\mathscr D\psi\)，不是遗漏一个有序项；同样保留两个有序 zθ 项。

## 2. 全域缩至真实可用的 q≈τ 区域

原能量／紧支撑输入给 \(\sup_{t<1}\|u(t)\|_2<\infty\)，Π 是 L² 正交投影。因此
\[
\|w_\tau\|_2\le C\tau^{A-3/4}=C\tau^{-1/4+h}.
\tag{WB.3}
\]
对任意事先固定的有限 N>h，取证明用的 \(L_\tau=(C_N\log(1/\tau))^{1/2}\)，及实径向偶截断 \(\zeta_\tau\)，在 \(|Y|\le L_\tau\) 等于1、在 \(|Y|\ge2L_\tau\) 等于0。它只分割同一积分，不更改 φ、ρ、原场或参数。C_N 足够大时，(WB.3) 与 Gaussian 尾直接给
\[
\int_{|Y|>L_\tau}|w_\tau|^2|\nabla\psi|=O(\tau^N),\qquad
\sup_{Y\in B_1}|S((1-\zeta_\tau)w_\tau)(Y)|=O(\tau^N).
\tag{WB.4}
\]
第二式用 Cauchy–Schwarz 与平移 Gaussian 的 L² 尾，第一式用其上确界；不要求扰动导数小，也不将 q 远离0的区域按有限阶段逐点估计。

在 \(|Y|\le2L_\tau\)，原恒等式 \(q-z_{\rm phys}^2q^{2h}=\tau\) 给 \(s=q/\tau=1+\epsilon^2Y_3^2s^{2h}\)。因 \(2h<1\)，充分小 τ 时唯一正解满足
\[
1\le q/\tau\le2,\quad q/\tau=1+O(\epsilon^2L_\tau^2),\quad
\eta=\epsilon Y_3(\tau/q)^D.
\tag{WB.5}
\]
例如函数 \(s-\epsilon^2Y_3^2s^{2h}\) 在 s≥1 上严格增，且在 s=2 已大于1；其原关系随后给偏差界。于是此处原空间／时间截止恒为1，活动波的重标半径 r 在固定正环带内。每一活动 band 的 Q≈q≈τ；\(S_*\) 及全部固定标签计数只带 \(\log(1/\tau)\) 的固定幂，下文统一记为 \(\mathcal L^P\)。

## 3. 同一最终场、全标签及 curl 的预算

原 (5.35) 允许先固定一个足够高阶段 J，使实现尾乘 τ^A 后在 (WB.5) 区域为 \(O(\tau^\beta)\)，其中 β>h；常数可依 J。Π 与 q、径向截止及此区域交换，故真实 wτ 与该阶段的完整 curl 波之差仍为 \(O(\tau^\beta)\)。这是同一最终实现的比较，不换原 cutoff 序列，不求阶段一致常数。

按原 (9.9)，该阶段完整归一化波 \(w^{[J]}\in W^{1/2}\)，且其与已拼合主横向波 \(w_0\) 之差在 \(W^{0.68}\)。在当前重标下，常数 λp 与 τ/Q 因子有界，故
\[
|w^{[J]}_\tau|\le C\epsilon^{1/2}\mathcal L^P,\quad
|w^{[J]}_\tau-w_{0,\tau}|\le C\epsilon^{0.68}\mathcal L^P.
\tag{WB.6}
\]
此处先合并同一 label／harmonic 的全部项。不同实际标签慢支持相交时，扩展辅助支持互斥；平滑零延拓的 curl／导数亦保留此性质。固定阶段谐波集有限，共同 torus 仅用有界相对覆盖，积分标签数至多固定对数幂，不乘绝对覆盖次数。因此完整原始波张量可替成 \(w_{0,\tau}\otimes w_{0,\tau}\)，加权误差至多
\[
C(\epsilon^{1.18}+\epsilon^{1.36}+\tau^\beta\epsilon^{1/2}+\tau^{2\beta})\mathcal L^P=o(\epsilon).
\tag{WB.7}
\]
截断区域体积的对数因子已吸收。此式完整支付两有序主波×修正、修正平方、全部实际 curl 与实现尾，没有将它们设为0。

## 4. 热平滑后的完整波平方为小阶

仍先用完整固定阶段。每个实际非零谐波为 \(a_{\gamma,m}(Y)e^{ik_\gamma m\Phi_\gamma(Y)}\)。原 (7.9) 及 B_s 的统一正下界给 \(|\nabla_Y\Phi_\gamma|\ge c>0\)；(9.19) 后的固定阶相位导数界给其一、二阶导数至多 \(C\mathcal L^P\)。幅度一阶物理导数由 (9.19) 给
\[
|a_{\gamma,m}|\le C\epsilon^{1/2}\mathcal L^P,\qquad
|\nabla_Ya_{\gamma,m}|\le C\epsilon^{1/2-\kappa_s}\mathcal L^P,
\qquad k_\gamma^{-1}\le C\epsilon^{1/2},\quad\kappa_s=10^{-5}.
\tag{WB.8}
\]
圆柱单位基的导数在该固定正环带有界，截断 \(\zeta_\tau\) 导数亦无反幂损失。用 \(V_\gamma=\nabla\Phi_\gamma/|\nabla\Phi_\gamma|^2\) 对完整空间积分一次分部积分：
\[
\int g_1(Y-X)\zeta_\tau a_{\gamma,m}e^{ik_\gamma m\Phi_\gamma}\,dX
=-\frac1{ik_\gamma m}\int\operatorname{div}_X(g_1(Y-X)\zeta_\tau a_{\gamma,m}V_\gamma)e^{ik_\gamma m\Phi_\gamma}\,dX.
\tag{WB.9}
\]
支持边界的零延拓消除边界项；角方向按周期积分，e^{ikmΦ} 与 ∇Φ 单值，不能仅凭 kp 非零推趋∞。全部标签／谐波求和，连同 (WB.4) 与真实实现尾，得
\[
\|Sw_\tau\|_{L^\infty(B_1)}\le C\epsilon^{1-\kappa_s}\mathcal L^P+C\tau^\beta\mathcal L^P+O(\tau^N)=o(\epsilon^{1/2}).
\tag{WB.10}
\]
因此滤波后完整张量与 ∇φ 的配对为 o(ε)。这里保留不同标签在滤波后的所有交叉乘积；没有沿用原点值支持互斥去删它们。

## 5. 未规定的 zθ 应力：先角平均，再使用奇权重

令 \(\sigma_{ab}=\langle(w_{0,\tau})_a(w_{0,\tau})_b\rangle_\theta\)，仍作实际辅助坐标求值。不同标签交差已由真实支持资格消失；同标签角平均只保留 m 与 −m，因为 kp 是非零整数。保留的共轭相位精确配消，所有其余系数及共轭配对均保留。

实际辅助坐标 Yaux(rphys,t) 不依 zphys；每固定标签系数的物理轴向导数只损失 Q^(−D)，见 (6.24)/(6.29)/(9.19)。换为 ∂Y₃ 多得 \(\sqrt\tau Q^{-D}=O(\epsilon)\)。平滑零延拓与共同 torus 保证换 band／label 时没有跳跃项，故在整个截断区域及连接其 z=0 的线段上
\[
|\sigma_{z\theta}|\le C\epsilon\mathcal L^P,\qquad
|\partial_{Y_3}\sigma_{z\theta}|\le C\epsilon^2\mathcal L^P.
\tag{WB.11}
\]
\(\zeta_\tau\) 对 z 偶而 ∂zψθ 对 z 奇，因而每个 r 的常量 \(\sigma_{z\theta}(r,0)\) 配对为0。由微积分基本定理，剩余积分绝对值至多 \(C\epsilon^2\mathcal L^P\int |z\partial_z\psi_\theta|\,dY=o(\epsilon)\)。实现尾和完整 curl 差已经由 (WB.7) 支付，不必为它们另求 zθ 主系数。原 (7.30) 仅给 rθ/rz 并不妨碍这一步。

## 6. rθ：沿真实径向路径替换 Haar 均值

固定物理 z,t 及适用共同 torus。对每个实际主波标签的角平均乘 \(r\mathscr D\psi\zeta_\tau\) 及正确归一化因子，再减去其辅助 Haar 平均。所得 f 对每个慢 R 的 Haar 均值为0，全部固定 (R,y) 系数导数满足 \(C\epsilon\mathcal L^P\)；权重不依辅助变量，R=rphys/√Q 与 r=rphys/√τ 的比例有界。这里求的是独立 R 系数导数，不能误换成已经沿辅助路径求值的快速物理导数。

实际物理积分恰沿原 (8.5) 的 \(y\mapsto y+M((R')^{d_r}-R^{d_r})v_r\)。置 U=R^{d_r}、\(F(U)=f(R)/(d_rR^{d_r-1})\)、\(L=v_r\cdot\partial_y\)。原 (6.7) 的 Diophantine 界与 (8.10) 给任意固定 p≥1 的有限导数估计，并有完整径向积分身份
\[
\int F(U+u,y+Muv_r)\,du
=(-M^{-1})^p\int\partial_U^pL^{-p}F(U+u,y+Muv_r)\,du,
\quad M^{-1}\le C\epsilon^{\kappa_s}\mathcal L^P.
\tag{WB.12}
\]
紧径向支持的光滑零延拓使每个端点项消失；Haar 零模已经减净。故物理值与 Haar 值的加权径向积分差为 \(O(\epsilon^{1+p\kappa_s}\mathcal L^P)\)。对 z 积分、有限谐波及全部标签求和仍只增对数幂；固定 p=1 已为 o(ε)。不需要把截止余项除以可能为0的 χ′，使用的是 Lemma8.2 证明中的完整径向积分身份。

原 (7.26)–(7.30) 含真实余弦的 1/2、两号标签及平方分割和，精确给
\[
\langle\sigma_{r\theta}\rangle_{\rm aux}
=\lambda_p^2\tau^{2A}q^{-A-1/2}T_{0,\theta}(r_{\rm phys}^2/(2q),\eta),
\quad
\epsilon^{-1}\langle\sigma_{r\theta}\rangle_{\rm aux}
=\lambda_p^2(\tau/q)^{A+1/2}T_{0,\theta}(r^2/(2q/\tau),\eta).
\tag{WB.13}
\]
该式在原活动环带外按0延拓。由 (WB.5)，对每个固定 Y 右端趋于 \(\lambda_p^2T_{0,\theta}(r^2/2,0)\)。原主应力在闭剖面域有界、径向紧支撑，\(\tau/q\le1\)，且 \(\mathscr D\psi\) 可积；因此可用支配收敛。结合 (WB.4)、(WB.7)、(WB.10)–(WB.13) 得 (WB.2)。

## 7. 周期像与结论范围

中心单副本替换完整周期提升时也不删像。原固定支撑 K 紧含周期化基本胞，各非零像到中心测试区域有正距离；在 Y 尺度该距离为 c|n|/√τ（常数可依原支撑／λp）。原 L² 与固定体积给每副本重标 L¹ 至多 \(C\tau^{A-3/2}\)，平方的 L¹ 至多 \(C\tau^{2A-3/2}\)。故全部非零像的 Gaussian 卷积及固定阶导数，由 \(\sum_{n\ne0}e^{-c|n|^2/\tau}\) 乘上述有限负幂界为任意 O(τ^N)。

原始张量中副本支撑互不相交；滤波后各像不再互斥，但完整非中心和指数小、中心和至多多项式，故其所有交叉张量仍为任意 O(τ^N)。先作这一完整周期至单副本替换，才对单副本作 Π 分解；没有将物理环面场假设为全空间轴对称。此结论只为原有固定支撑构造服务，不推广到任意周期场。

本稿支付真实波部分的 τ^h 系数与严格小阶余项；背景、实际均值 m 的全部项及原源项仍由合同其他证明承担。特别不以 (9.11) 的均值动量方程直接读取 J、不预断系数非零、不改变原轨道或创造无力解。SOURCE_INPUT_AUDIT 的“桥待完成”是先前停稿状态，本文是其后独立落盘的实际补证。

## 8. 实读范围与绑定

全文读本合同及自己的已停止 SOURCE_INPUT_AUDIT；复读旧已接受 AXIS_LABEL_SOURCE（78行）、WEIGHTED_ERROR_INDEPENDENT（132行）。原带页标文本实际定向读5135–5280、5472–5635、3950–4260、4277–4462、3595–3717、3090–3145、3380–3440；收口再次读上述核心及3200–3265（支持互斥／共同 torus）。复用此前实际读过的 (5.35)/(5.42) 与 (10.13)/Cor10.6。所需主页为58、63–71、74–76、82–92、106–115及能量段；未重读外部全文，未调用未核外引作新的独立定理。

来源 SHA-256：合同 `1f1f00d70e878cd1eeeebc9064b5882f516a43258014084062a8cf6a4b975145`；SOURCE_INPUT_AUDIT `2d610bab9beac798f905e140565a2d65b2fa0a8937e986d4dcc5f0d1249532a4`；原PDF `0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f`；原文本 `7c8d1e236e6285de297f4d88d05056f3de5a8bdcc6454ddc81b665cf98ae0c26`；AXIS_LABEL_SOURCE `b9a48de47b0def307f5c76822bac28cb788d454f968ec39561708a126b18276d`；WEIGHTED_ERROR_INDEPENDENT `fb7a2f8284f2f1a838306e3a68f9a2ae7cb6cf76a9a63b574d05832eb8f38018`。

本稿只作解析文字推导；科学 worker、数组、FFT、实际参数求值、新图、Git、外发均0。全文自读后停稿，待非作者逐式审查。
