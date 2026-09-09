# 第一来源门终点：指定预算方法的必要目标

2026-09-09，PRIVATE_CORE。**作者稿，待非作者审查；CONDITIONAL-ENDPOINT-CERTIFICATE-SCREEN / NO-NEW-PAID-INPUT。** 本人是 BF/RE 作者、AP 非作者审查者；本题依先锁合同单独形成，不称盲审或新颖性发现。只沿用同一 a_*、准确 T 和单一路 trajectory160_512 的条件重建对象，不重推 BF/AP，不读本题其它形成稿，不属于第 29 包。

## 1. 精确对象与完整严格失败判据

令 v 是同一个在 [0,T] 合格的有限谱 C¹ 实值无散零均值重建；AP 给的是一种有条件定义，不表示保存数组已认证为这种对象。凡下文涉及真实 u，均另以同一 a_* 的原 NS 已光滑存在至 T、RE.1–3 的完整输入已付为前提。采用归一化 Haar L²、Hermitian Fourier 长度及 A0 范数，H₀=[4,8)、H₁=[8,16) 按频率长度取全部正负整数模，N₁=#H₁>0、M=‖a_*‖₂。
\[
h_i^v=P_{H_i}v,\qquad
g^v(T)=\int_0^T e^{(T-r)\Delta}P_{H_1}B(h_0^v,h_0^v)(r)\,dr,\qquad
F^v(T)=\|h_1^v(T)-g^v(T)\|_{A0}-\tfrac14\|g^v(T)\|_{A0}.
\tag{FG.1}
\]
这是同一连续重建的精确第一历史；不能据此认定它等于旧保存 G。目标的初端差、完整残差及此前所有真实来源，仍由 RE 的原状态/历史接口保留。

对 RE.5 的特定预算 E，完整历史项和门预算为
\[
K_1(\tau)=\sum_{k\in H_1}|k|e^{-|k|^2\tau},\qquad
I=\int_0^T K_1(T-r)E(r)[2M+E(r)]\,dr,\qquad
\Delta=\sqrt{N_1}E(T)+\tfrac54 I.
\tag{FG.2}
\]
I 非负，其误差平方、两个完整有序来源及物理热权重没有删减。真实第一门函数 F(T) 满足 |F(T)−F^v(T)|≤Δ。因此本题所审议的**精确 RE.12 充分判据**为
\[
F^v(T)-\Delta>0.
\tag{FG.3}
\]
它若被认证便给 F(T)>0；反之，F(T)>0 并不保证 FG.3 成立。FG.3 左端等于零不认证严格失败。第一原全窗门要求所有 r∈[T/2,T] 的 F(r)≤0，故一个已认证的终点失败足以否定它；终点通过不代表全窗通过，也不处理第二门。

若只有报告值 \(\check F\)，必须另付 \(|\check F-F^v(T)|\le\xi\)，其中可取
\[
\xi=\xi_\eta+\tfrac14\xi_Q+\xi_F\ge0
\tag{FG.4}
\]
作为 RE.12 的报告附加预算：ξ_Q 控制来源向量，ξ_η 控制目标减来源的向量，ξ_F 控制范数及最终标量求值。历史求积、系数读取、向量相减及准确时标差均须计入相应项。此时实际使用的判据是 \(\check F-\xi-\Delta>0\)，不能用未认证的旧浮点 F 直接代替 \(\check F-\xi\)。

## 2. 端点预算下界能给什么

假定仅已认证 0≤c≤E(T)，例如在 BF 全部资格满足后得到的末段下界。由 FG.3 必有
\[
F^v(T)>\sqrt{N_1}c+\tfrac54 I,\qquad
c<\frac{F^v(T)-5I/4}{\sqrt{N_1}}.
\tag{FG.5}
\]
对报告判据，相应必要条件为
\[
\check F>\sqrt{N_1}c+\tfrac54 I+\xi,\qquad
c<\frac{\check F-\xi-5I/4}{\sqrt{N_1}}.
\tag{FG.6}
\]
这些只是充分认证方法能够通过的必要条件。即使右侧为正且 c 小于它，实际 E(T) 仍可能远大于 c；I 和 ξ 也仍须完整支付。没有把必要条件反过来当真实失败的充分条件。

尤其，c≤E(T) 不能推出 c≤E(r) 对所有早期 r 成立，因而不能据此把 I 换成 ∫₀ᵀK₁(T−r)c(2M+c)dr。RE.5 的 E 虽非减，但其端点下界不会向过去传播。这里允许为更弱的必要筛查只用 I≥0；这种舍弃不会缩减最终 FG.3/报告判据的认证预算。若要从 BF 的其它结构另证历史下界，须另外证明，本稿没有默用它。

## 3. 从连续 H₀ 能量得到 Fᵛ 的可核上界

定义同一个 v 的精确非负量
\[
H=\|h_1^v(T)\|_{A0},\qquad
\mathcal V_0(r)=\|h_0^v(r)\|_2^2,\qquad
\mathcal B=\int_0^T K_1(T-r)\mathcal V_0(r)\,dr.
\tag{FG.7}
\]
对每个 k，完整 Leray 系数先用无散移导数到输出 k，再作卷积 Cauchy，给 |B(h₀ᵛ,h₀ᵛ)_k|≤|k|𝒱₀。保留热权重并求有限全带和，所以 ‖gᵛ(T)‖A0≤𝓑。再用三角不等式，
\[
F^v(T)\le H+\tfrac34\|g^v(T)\|_{A0}
\le H+\tfrac34\mathcal B=:\mathcal U.
\tag{FG.8}
\]
其中 3/4 来自先估 ‖h₁ᵛ−gᵛ‖≤H+‖gᵛ‖、再减 ‖gᵛ‖/4。𝒱₀ 是完整连续重建的平方 L² 范数，不是原 NS 的能量；不能未经证明以 M²、保存节点值或旧 G 的量替代。FG.8 不需要有利相消，但可能很粗。

若未来另行认证 \(\bar H\ge H\)、\(\bar{\mathcal B}\ge\mathcal B\)，令
\[
\bar{\mathcal U}=\bar H+\tfrac34\bar{\mathcal B},\qquad
\zeta_{\rm cap}=\frac{\bar{\mathcal U}}{\sqrt{N_1}}.
\tag{FG.9}
\]
这给一个从同一重建对象预先规定公式的**必要预算上限**，不是从旧浮点 F 临时挑选的容限。FG.3、FG.5 与 FG.8 联合严格要求
\[
\sqrt{N_1}c+\tfrac54 I<\bar{\mathcal U},\qquad c\le E(T)<\zeta_{\rm cap}.
\tag{FG.10}
\]
故若 c≥ζ_cap，或者另有独立认证的 0≤I₋≤I 且 √N₁c+5I₋/4≥Ū，则这个 RE.12 方法不能在该终点认证严格失败。反向严格小于仅意味着此必要筛查没有挡住它，不证明判据通过。等号同样只挡住严格认证；c=0 不自带正障碍，Ū=0 时则 Fᵛ≤0，非负预算下 FG.3 不可能成立。

报告情形也有 \(\check F-\xi\le F^v(T)\le\bar{\mathcal U}\)，所以 FG.10 同样必要；这里不是再从 Ū 扣一次 ξ。ξ 仍完整存在于实际 FG.6 及报告认证式中，较粗的上限只用了报告下端不大于精确 Fᵛ 的关系。

## 4. 本题实际能完成的判别范围

已有符号接口给出了可检查的停止条件 c≥ζ_cap，或其含 I₋ 的加强形式；当前没有 c、\(\bar H\)、\(\bar{\mathcal B}\)、合格报告 ξ 及连续历史的实际证书，故不能判断该条件是否发生，也不预设粗上界有数值判别力。只给 ζ_cap 的公式不算已获准的残差求值目标或成本预算；是否值得另立求值合同仍需这些输入与成本的独立价值审议。

方法不能通过 FG.3，不表示真实 F(T)≤0，也不表示 F(T)>0；更不否定其它后验方法、其它时刻的失败见证或真实 NS 解。若另一已认证时刻的同类判据严格失败，仍可否定该全窗门。端点 c 是特定上包围 E 的下界，不是 ‖u−v‖₂ 下界；原解存在至 T、强延续、逐频相位/形状及跨尺度机制均不由本稿支付。

## 实读范围与停止记录

本轮全文读 FIRST_GATE_TARGET_CONTRACT、AP 根稿 1–41 行；定向读 BF 稿 78–94 行（BF.10–11），RE 稿 7–53、55–112 行（完整输入、E、历史、报告误差及全窗量词）。既往作者/审查身份已披露，未重推或修改这些停稿，也未读取本题其它形成稿。

| 实际文件（相对 research/reverse/） | SHA-256 |
|---|---|
| residual-budget-floor-preflight/FIRST_GATE_TARGET_CONTRACT.md | b55d2d9b7b70afd0699feef821f04472082e9c43cf67fceaaf8ff64fb90471f3 |
| residual-budget-floor-preflight/PROOF.md | 1ab573bbc9bdc16445964cc65245182357b14327dea8df0a8f070e72bbde81d1 |
| residual-budget-floor-preflight/ROOT_APPLICATION_PREFLIGHT.md | e361e0fa8c2db879906b60ca7901f295c38fe643d5d3ffd49b37678c17a0dddb |
| relative-energy-error-preflight/PROOF.md | d1484629cbc592f2cdd14c7d86a370bc7fc915172f2d7a553285675a564c811f |

科学 worker 0、数组打开 0、选参 0；仅手工符号及文本/哈希，无重建或残差求值、FFT、Git 或外发。只写本稿，全文自读核源后停定，再交非作者审查；最终 SHA 由任务消息给出。
