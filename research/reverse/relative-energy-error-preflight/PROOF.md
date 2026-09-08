# 相对 L² 重建误差及有限环带历史的条件接口

2026-09-09，PRIVATE_CORE。**作者稿，待非作者审查；CONDITIONAL-ERROR-INTERFACE / NO-NEW-PAID-INPUT。** 本文只在同一 a_* 的已有光滑原解区间内手推一条相对能量估计。不构造或评估重建，不认证旧数值门，不主张新颖性。本人是前项耗散尾独立稿及 GENERAL_SOURCE_BRIDGE 作者、旧 OBSERVATION_ERROR 审查者；本题是指定唯一作者推导，不称第二份盲证明或非作者审查。未读本题其它形成稿，包括根的延续范围稿。

## 1. 完整对象及可验证输入

固定 ν=1、无外力标准 2π 三维环面。设同一实值、零均值、无散经典解 u(0)=a_* 已在 [0,Θ] 光滑；Θ 只是已有区间端点，不等同旧观测 T。重建 v 的整窗支持包含于同一个固定有限对称集合 F⊂Z³\{0}，各 Fourier 系数为 C¹([0,Θ])，满足实值共轭及无散条件。所有点积估计使用 Hermitian 长度，物理空间内积为实内积；约定
\[
\langle f,g\rangle_2=(2\pi)^{-3}\int f\cdot g,\quad
\|f\|_2^2=\sum_k|f_k|^2,\quad \|f\|_{A0}=\sum_k|f_k|,\quad
\|R\|_{\dot H^{-1}}^2=\sum_{k\ne0}|k|^{-2}|R_k|^2.
\tag{RE.1}
\]
令 B(f,g)=−𝓟(f·∇g)，其 k≠0 系数为 −i𝓟_k∑_{ℓ+m=k}(f_ℓ·m)g_m，零系数为 0；B 内点积为复双线性。保留完整有序和及周期 Leray，取
\[
R=\partial_tv-\Delta v-B(v,v),\quad e=u-v,\quad
S(v)=\tfrac12(\nabla v+\nabla v^{\mathsf T}),\quad M=\|a_*\|_2.
\tag{RE.2}
\]
R 实值、无散、零均值，且连续并具有固定有限支持，故 RE.1 的对偶范数有定义。若 P_F 投影到 F，则 R=P_FR−(I−P_F)B(v,v)；支持外非线性漏出是完整残差的一部分，不能仅认证 P_FR。压力没有作为动力学项删除，而是包含在 B 的完整 Leray 中。

明确需要给定 d₀≥‖a_*−v(0)‖₂、非负 ε∈L²(0,Θ)、σ∈L¹(0,Θ)，并验证几乎处处
\[
\|R(r)\|_{\dot H^{-1}}\le\varepsilon(r),\qquad
\sup_x\lambda_{\max}[-S(v)(x,r)]\le\sigma(r).
\tag{RE.3}
\]
这里 σ≥0；也可给更粗的 sup_x‖S(v)‖op 上界。因 tr S(v)=0，单侧最大特征值本身非负。固定有限谱/C¹ 只保证这些对象存在，不能自动提供已认证的数值上界；旧数组、采样和成本记录不支付 RE.3。

## 2. 能量身份、权重及零支

准确误差方程为 e_t=Δe+B(v,e)+B(e,v)+B(e,e)−R。设 y=‖e‖₂²、z=‖∇e‖₂²。周期积分与 div v=div e=0 给 ⟨e,B(v,e)⟩₂=⟨e,B(e,e)⟩₂=0；Leray 在无散 e 的内积中自伴消去梯度，亦即压力差的内积为零。剩余项的符号是
\[
\tfrac12 y'+z=-\langle e,S(v)e\rangle_2-\langle e,R\rangle_2
\le\sigma y+\varepsilon\sqrt z
\le\sigma y+\tfrac12 z+\tfrac12\varepsilon^2.
\tag{RE.4}
\]
最后一步为 2ε√z≤z+ε²；前一步用零均值 Fourier 对偶配对 |⟨e,R⟩₂|≤‖R‖Ḣ⁻¹‖∇e‖₂。反对称梯度的二次型为零，但对称梯度项一般不为零；上述相消仅在这个能量内积成立，不能用于删除状态或来源向量。原解同样的能量恒等式给 ‖u(r)‖₂≤M。

定义时间权重及非负预算
\[
A(t)=2\int_0^t\sigma(r)\,dr,\qquad
J(t)=d_0^2+\int_0^t e^{-A(r)}\varepsilon(r)^2\,dr,\qquad
E(t)=e^{A(t)/2}\sqrt{J(t)}.
\tag{RE.5}
\]
将 RE.4 乘 2，再用积分因子，对每个 0≤t≤Θ 完整得到
\[
e^{-A(t)}y(t)+\int_0^t e^{-A(r)}z(r)\,dr\le J(t),\qquad
\boxed{\ \|u(t)-v(t)\|_2\le E(t)\ }.
\tag{RE.6}
\]
故还可保留 ∫₀ᵗz≤e^{A(t)}J(t) 的较粗耗散预算。这里时间权重是 e^{A(t)−A(r)}，不是将后时刻的应变上界当成全历史常数；没有额外体积因子。若 d₀=0 且 ε=0 几乎处处，则 J=E=0，由 RE.6 得同区间 e≡0。证明始终针对 y，不除以 ‖e‖₂，因此零误差时刻也适用。它不构造该区间之外的 u。

## 3. 同一重建的有限环带历史

仅取旧 H_j={k:2^{j+2}≤|k|<2^{j+3}}，j=0,1,2，全部正负模各一次；N_j=#H_j 保留为符号。令 h_j=P_{H_j}u、h_j^v=P_{H_j}v，Cauchy 与投影收缩给
\[
\|h_j-h_j^v\|_2\le E,\quad \|h_j-h_j^v\|_{A0}\le\sqrt{N_j}E=:E_j,\quad
\|h_j\|_2\le M,\quad \|h_j^v\|_2\le M+E.
\tag{RE.7}
\]
这直接使用 L² 误差，不冒称旧 OE.1 的 H³ 前提或其频率权重已经支付。完整无散输入满足 f_ℓ·m=f_ℓ·k，故卷积 Cauchy 给 |B(f,g)_k|≤|k|‖f‖₂‖g‖₂。定义
\[
K_j(\tau)=\sum_{k\in H_j}|k|e^{-|k|^2\tau},\qquad
I_{ij}(b,c)=\int_b^c K_j(c-r)E(r)[2M+E(r)]\,dr.
\tag{RE.8}
\]
准确恒等式 B(h_i,h_i)−B(h_i^v,h_i^v)=B(h_i−h_i^v,h_i)+B(h_i^v,h_i−h_i^v)，结合 RE.7 得热累计上界 I_ij；E² 已保留，两个有序项不合并为二倍同一向量。所有输入带及输出带均有限，不需要求和交换的额外假设。

任意 0≤s<a<t≤Θ、s≤r≤t，按同一连续历史定义
\[
g_s(r)=\int_s^r e^{(r-q)\Delta}P_{H_1}B(h_0,h_0)(q)dq,\quad
g_s^v(r)=\int_s^r e^{(r-q)\Delta}P_{H_1}B(h_0^v,h_0^v)(q)dq,
\]
\[
S(t;a)=\int_a^t e^{(t-q)\Delta}P_{H_2}B(h_1,h_1)(q)dq,\quad
S^v(t;a)=\int_a^t e^{(t-q)\Delta}P_{H_2}B(h_1^v,h_1^v)(q)dq.
\tag{RE.9}
\]
第二源使用实际 P_{H₁}v，而不是 g_s^v；原解侧亦使用实际 h₁。积分三角不等式给 ‖g_s−g_s^v‖A0≤I₀₁(s,r)、‖S−S^v‖A0≤I₁₂(a,t)。不以第一门成立为该误差界的前提。

写 Q₁=g_s、Q₂=S，q₁^v=g_s^v、q₂^v=S^v，以及 η_j=h_j−Q_j、η_j^v=h_j^v−q_j^v（j=1,2，各用自己的时刻和起点）。则
\[
\|\eta_1-\eta_1^v\|_{A0}\le E_1(r)+I_{01}(s,r),\qquad
\|\eta_2-\eta_2^v\|_{A0}\le E_2(t)+I_{12}(a,t).
\tag{RE.10}
\]
为明确没有清空目标初端或其它来源，任意 0≤b≤c≤Θ 及目标 H_j 的完整误差身份仍是
\[
P_{H_j}e(c)=e^{(c-b)\Delta}P_{H_j}e(b)
+\int_b^c e^{(c-r)\Delta}P_{H_j}\{B(e,u)+B(v,e)-R\}(r)dr.
\tag{RE.11}
\]
进一步，令 z_i=u−h_i，j=i+1；真实目标减其 h_i 自作用历史，恰等于 e^{(c−b)Δ}h_j(b) 加上三项 B(h_i,z_i)+B(z_i,h_i)+B(z_i,z_i) 的完整投影热积分。v 侧相应身份另有 +∫heat P_{H_j}R。故正起点已有 h₂(a)、原种子、回流、非相邻及带外作用均保留；RE.6 从初始差 d₀ 控制目标差，并未暗设 P_{H_j}e(b)=0。

## 4. 门函数、求值与适用边界

令 F_j=‖η_j‖A0−‖Q_j‖A0/4，F_j^v 同样定义，则反三角不等式给
\[
|F_1(r)-F_1^v(r)|\le E_1(r)+\tfrac54 I_{01}(s,r),\qquad
|F_2(t)-F_2^v(t)|\le E_2(t)+\tfrac54 I_{12}(a,t).
\tag{RE.12}
\]
若报告向量与精确 q_j^v、η_j^v 的 A0 误差另经认证为 ξ_Q、ξ_η，报告门函数自身的范数/标量求值误差为 ξ_F，则 RE.12 右侧须再加 ξ_η+ξ_Q/4+ξ_F。ξ_η 包括目标/来源读取及相减圆整，不能因共用来源而自动抵消；精确时标误差与历史求积差也须计入相应预算，不能只对齐节点名称。

**新 v 的精确 g_s^v、S^v 不自动等于旧 Lawson 增广状态所存 G/W。** 即使 v 插值经过旧检查点，也必须另付两套连续历史与保存状态之间的差。本文没有定义该插值、时间重建或求积证书，不能直接将 RE.12 贴到旧四路的正 F 上作为原 NS 门失败证据。

对精确重建门，F_j^v 加总误差上界小于 0 是严格通过的充分条件，F_j^v 减总误差上界大于 0 是失败的充分条件；有求值误差时换成认证的报告区间。认证第一门通过须覆盖全 r∈[a,t]；一个已认证失败点已足以否定该全窗门；第二门的通过/失败只在指定终点判定；有限采样不支付连续窗。无法分离时保持未决。严格门自动迫使 Q_j≠0；非严格门可能仅为 Q_j=η_j=0。另有 ‖q_j^v‖A0>I_ij 可给真实来源正下界，使用报告时须再扣全部来源求值误差；零分母比值从不定义。若来源非零且门成立，则目标范数至少为 3‖Q_j‖A0/4。

旧特例 s=0、a=T/2、t=T 只能在同一原解已被其它证据证明存在至 T 且全部 RE.3 输入覆盖全窗时使用；T=8/C 不是这里推出的寿命。RE.6 给 L∞_tL²_x 与积分耗散，不给 H³ 上界、强解延续或无限尺度。有限带用途不声称逐对相位/形状返回、一般再生排除或真实门已经成立。旧 H³ 延续接口还需其高阶范数、完整高阶残差和控制上解；本稿未支付，也不伪造不延续反例。科学 worker 0，当前没有新的已认证轨迹或候选。

## 实际来源及停稿

本轮实际全文读本合同 1–13 行、NEXT_ERROR_HISTORY 全文、DTI 独立稿 1–71 行、OE 分段覆盖 1–320 行；只复用 OE 的归一化、完整系数及观测预算和 DTI 的同解能量/完整残差边界，不承接未付的 H³ 误差。NEXT_ERROR_HISTORY 所列其它原稿/外引本轮未读，不把其摘要当重新认证。

| 本轮实际文件（均相对 research/reverse/） | SHA-256 |
|---|---|
| `relative-energy-error-preflight/CONTRACT.md` | `54de0027574ec8b323deee8bdc6cc51894f5e929ac81a0ab79225cab4f7ba539` |
| `dissipation-tail-preflight/NEXT_ERROR_HISTORY.md` | `e1d998459eed74cb48801acf6b035e287f30c2c199c0cbee9f78a066a86aa43d` |
| `dissipation-tail-preflight/INDEPENDENT.md` | `495c1f8fef2798165dceb8f971aaa57705e1c15644917784e835a777b5edd3fe` |
| `annular-source-observation/OBSERVATION_ERROR.md` | `5823a2e03e4e176eb2ab444f58fce1797ebef6aafc5f84ada594b359e44c1b05` |

本稿仅文本写读、手工证明和字节哈希；无程序/数组/FFT/参数求值、Git 或外发。全文自读核源后停止修改，随后另交非作者审查；最终本稿 SHA 由任务消息给出。
