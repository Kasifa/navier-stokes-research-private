# 最低接收独立稿的非作者逐式审查

2026-09-08，PRIVATE_CORE。结论：**PASS，TEI.1–24 在所列合同内成立，无待修数学意见。** 接纳范围是最低完整 Z 行的唯一实部消元、最低完整 C 行非零及原方向的准确双条件；不接纳实例存在、较高两行相消或真实 NS 再生成。

## 1. 身份、实际阅读与字节绑定

审查者是本目录 PROOF.md 的作者。该主稿在本审查开始前已完成并停改，SHA-256 为 8961c72504eb7d60f35ee53050c99a2a25203ad539f85a9135ca16706dcc1cba。本次首次完整阅读被审 INDEPENDENT.md，故属于被审稿的非作者审查，**不是全课题盲审**。本文逐式核对被审稿自身表达式及已接受来源，不用自己的主稿填补被审稿证明；没有修改自己的主稿。

路径相对于 research/reverse/。

| 本次实际读取对象及范围 | SHA-256 |
|---|---|
| two-elliptic-compatibility/CONTRACT.md，全文 | ee05b39370f178cac5aebcf3c3046478c848c74b0078ee26edafb3282029ad52 |
| two-elliptic-compatibility/INDEPENDENT.md，全文；TEI.1–24 逐式手核，最终全文重读 | 9a39799e39b9ec40e4ae61e86f3b0dda0dabc0885dcbea17febd91b868524da9 |
| net-mixed-cancellation/INDEPENDENT.md，第 44–119 行，完整 NC.4–10 的几何定义、相干 Z、完整 C 和缩放 | 25111397d32eef2751a91b1ad1ab6a446794742874b97bf6b0b73b3964d11a58 |

来源内部引用的其它文件不自动计为本次实读。审查全部采用手工符号推导；没有科学程序、数组、数值求值、实际参数选择、扫描、Git、外发或发布。

## 2. 同一数据、完整系数和换基

**TEI.1–4：通过。** 去掉共同接收因子 z0² 由 NC.10 严格允许，既保持 Z 零行，也保持属于原 U0 复直线的条件。两条边用同一个实 U，发送比值始终是同一 V_j 的 ξ_j+iθ_j。由
\[
q_j\cdot(f_j\times n_j)=-\Delta_j,\qquad
\overline V_j\times V_j
=2i|x_j|^2\theta_j(f_j\times n_j)
\]
得到稿内有向面积的确切负号。θ_j 非零与该面积非零等价；u_jx_j 非零来自活跃边，不是为消元额外删去合同内分支。

**TEI.5–8：通过。** 将合同的 8c² 等式分别代入 Λ、Ω、H，得到所列三个因式分解。P>Q/4 保证 Ω、H 正；同时 Q²−4c²=P(4P−Q)/2>0，所以在两个 h_σ 中约去 Q+2σc 合法。随即得到
\[
\alpha=\frac{2(5P+4Q)}{3(2P+Q)},\qquad
\chi=\frac{4cd}{3Q(2P+Q)},\qquad
\kappa=2\chi .
\]
α 严格正、χ 非零且与 c 异号。NC.7–8 中抽出 L u²|x|² 后，平面项为 χ、接收法向项为 2χv/u，核得 TEI.7。NC.9 中 I=−|x|²θ，因此完整 C 的法向虚项是 **正** 2icQθ；TEI.8 保留了该项和接收反馈，没有以 β=0 删除 C 中相干。

**TEI.9–12：通过。** e、n 的模分别为 ℓ、√Pℓ，因此
\[
u_j=A_j/\ell_j,\qquad v_j=B_j/(\sqrt P\,\ell_j).
\]
由两个基的有向旋转，逐项得到 B1、B2 的共享坐标式。三频实独立保证投影 E1、E2 独立，故 \(\mathsf S\ne0\)。换基后的完整 C 平面比例为 d/P，实发送比例为 ρ，反馈仍为 2AB，虚发送比例为 ν，均与 TEI.12 相符。k_j 真实保留发送模方；sign r=sign(c1c2)，没有把有符号权重改成两个自由正数。

## 3. 最低 Z 的唯一消元及面积保持

**TEI.13–14：通过，且为合同内充要式。** 与 E2、E1 点积分别消去第二边、第一边的法向发送项，得到稿内两个实方程；它们对 η1、η2 的系数分别是 \(\mathsf S\) 和 \(-r\mathsf S t^2\)，均非零。解式及恢复 ξ 的因子
\[
\frac{\chi_j}{\sqrt P\,\alpha_j}
=\frac{2c_jd_j}{\sqrt P\,Q_j(5P+4Q_j)}
\]
完全一致。因此这里不仅是必要的射线条件，而是对两个发送实部的唯一完整解。

这些方程未除以 \(\mathsf C,\eta_j,\xi_j\)，其为零不丢解。t=0 或无穷分别意味着某个 U·q_j 为零，确实落在合同排除的失活边上。发送 x_j 和 θ_j 固定时，解 ξ_j 不改变投影模方或有向面积。

关于高种子间活跃性的说明也成立：非零极化面积使实、虚部在该发送横向实平面内独立；若同一复种子再与另一非平行实频率正交，两者会同落在两横向平面的实一维交线中，矛盾。这只验证失活没有由该实部消元引入，不等于验证两个较高完整 Z 行为零。

## 4. 完整 C 的方向和非零性

**TEI.15–18：通过。** 直接从 TEI.12 计算
\[
\omega_p(U,C_j)
=i\sqrt P\,k_j
\left[(2-\sigma_j)A_j^2B_j
+\rho_j\eta_jA_j^3+i\nu_jA_j^3\right].
\]
代入 TEI.9、13 后，实系数分子为
\[
(2-\sigma_1)(t-\mathsf C)
+\rho_1(\mathsf C-2t-rt^2)
+rt^2\left[(2-\sigma_2)(\mathsf Ct-1)
+\rho_2(-\mathsf Ct+2+1/(rt))\right].
\]
其常数、一次、二次、三次项分别为
\[
-\Gamma_1\mathsf C,\quad
(\Gamma_1+\delta)t,\quad
r(\delta-\Gamma_2)t^2,\quad
r\Gamma_2\mathsf Ct^3,
\]
恰是 TEI.16。虚系数为 ν1+rt³ν2，核得 TEI.17 的全部因子与符号。横向复二维交替形式非退化，且 U 非零，故行列式为零与完整 C 属于复直线 \(\mathbb C U\) 等价。两个括号内量均为实，必须同时为零。这证明 TEI.18 的双向性；单独三次式不能替代完整方向条件。

**TEI.19–20：通过。** 不仅符号一致，固有面积式的公共常数也可直接追踪：
\[
\begin{aligned}
\sum_j k_jQ_jA_j^3\theta_j
&=\sum_j2\Delta_j\chi_j|x_j|^2\theta_j(U\cdot q_j)^3\\
&=-2\sum_j\chi_j\mathfrak h_j(U\cdot q_j)^3\\
&=-\frac83\sum_j
\frac{c_jd_j}{Q_j(2P+Q_j)}
\mathfrak h_j(U\cdot q_j)^3 .
\end{aligned}
\]
这里使用 \(\ell_j^4=\Delta_j^2/P^2\)。左端为 \(k_1a^3(Q_1\theta_1+rQ_2t^3\theta_2)\)，因而 TEI.19 与方向虚条件确切等价。各项非零后才取符号，得到
sign(\(\mathfrak h_1\mathfrak h_2\))=−sign(rt)。稿内明确保留准确幅度等式，未把此符号条件升级为充分性。

**完整 C 非零：通过。** 除去共同接收相位后，(C1+C2)/i 的虚部是两个独立实向量 N1、N2 的线性组合。两个系数 \(k_j\nu_jA_j^2\) 各非零，所以该虚部严格非零，完整行也严格非零。恢复 z0² 不改变结论。这是完整向量总和证明，未用单边非零替代行非零；亦不自动证明原方向合格。

## 5. 三次式全部列出的退化与符号边界

**TEI.21–22：通过。** 由 1<ζ1<ζ2<4 手工通分核得 δ 的式子及 δ<0。Γ>0，而
\[
\rho(\zeta)+2
=\frac{2[6+\zeta(4-\zeta)]}{5+4\zeta}>0
\]
给出 \(\mathcal A=1+\zeta_1+\rho_2-2\rho_1>0\)；
\(\mathcal B=\Gamma_2-\delta>0\)。把 TEI.16 按 r 收集，精确得到 N+rD。故 D 非零、仅 D 零及 D=N=0 三分支穷尽了这一消元分母；r 必须为非零且符合同一模方给定的符号。N=0、D≠0 要求 r=0，正确排除。

**TEI.23：通过。** 当 t≠0 时，D=0 给 \(\Gamma_2\mathsf Ct=\mathcal B\)，因此 \(\mathsf C\ne0\)。再联立 N=0，恰得稿内 t 与 \(\mathsf C^2\) 两式，反向代入亦成立。另由
\[
\mathcal A\mathcal B-\Gamma_1\Gamma_2
=\delta(\Gamma_2-\Gamma_1)-\delta^2<0
\]
及 \(\mathcal A\mathcal B>0\)，该平方比严格落在 (0,1)。这只说明所列退化几何条件与投影角的基本范围并不直接冲突；被审稿没有宣称整数三频实现它。此分支只取消当前实方向式对 r 的限制，不取消面积式、唯一 ξ 解或较高行条件。

**TEI.24 与其余边界：通过。** 投影正交 \(\mathsf C=0\) 时 D=−\(\mathcal B t^2\ne0\)，F=t(\(\mathcal A-r\mathcal Bt\))，在允许域唯一给 t=\(\mathcal A/(r\mathcal B)\)。于是 rt>0，完整方向要求两面积异号。t=0 被正确标作失活根。若 \(\mathsf C\ne0\)，三次系数 \(r\Gamma_2\mathsf C\ne0\)；若 \(\mathsf C=0\)，降次式也不恒零，故不存在遗漏的恒零多项式分支。

合同外的 c_j=0、d_j=0、Δ_j=0、\(\mathsf S=0\)、x_j=0、A_j=0 或 θ_j=0 不被此证明覆盖；稿内依赖这些非零量的除法都明确处于合同允许域。实部或投影余弦为零的合同内分支则已处理，二者没有混淆。

## 6. 接纳边界

被审稿完成了合同所需的实质消元与完整方向检验：最低 Z 零行等价于唯一发送实部公式；在此零行上，最低 C 始终非零，且其沿原 U0 复方向等价于准确三次式和有符号面积平衡同时成立。所列符号障碍及 D=N=0、投影正交、降次、失活边界均已手核。

本审查未发现需要修改被审稿或本人主稿的内容。较高两接收的完整 M0 行、同一整数几何的实际实现、最低方向联合条件的实现性、其它接收方向、模板幅度及再生成仍为 OPEN。没有新的原解时间估计、跨代误差、实际参数或奇性结论；未来使用 SOURCE_BRIDGE 仍须显式核其同一数据和预算。

**PASS AT THE BOUND CONTRACT；HIGHER ROWS AND REALIZATION OPEN；NO-CANDIDATE；NOT CLAY。**
