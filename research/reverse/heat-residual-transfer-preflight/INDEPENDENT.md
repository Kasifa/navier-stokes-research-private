# 完整热交换差的全周期传递界：独立手推

2026-09-09，PRIVATE_CORE。Gauss（`coherence_independent_resumed`）只核本合同第1–2项。本人是前项热接口/完整加权误差独立稿作者；合同已披露 root 的先行桥积分思路，本稿据合同自行核算，不称互盲，未读本题 root 证明。未改变同一 U、λ_p、ρ 或原数据。科学程序、数组、FFT、扫描、Git、外发均0。

**结论。** 所求全周期估计成立，常数可取下面明确的有限 Gaussian 积分常数。现有速度裕量 ε=h/4 经此估计产生两个不衰减的上界幂次，故结论是 `CONDITIONAL_INTERFACE / INPUT_NOT_QUALIFIED`：此证书不足以证明缩放后的实际有符号交换差趋零，亦不足以证明它不趋零。

## RTI.1 规范与完整投影热核

在单位环面 `T³=R³/Z³`，使用体积1的 Haar 测度、频率 `ξ_k=2πk`，向量取 Euclidean/Hermitian 范数、张量取 Frobenius 范数。普通有序张量 `(B⊗E)_ij=B_iE_j` 不含共轭；绝对值仍满足 `|B⊗E|_F=|B||E|`。定义 `(div T)_i=Σ_j∂_jT_ij`。`P_k=I−ξ_k⊗ξ_k/|ξ_k|²`（k≠0）、`P₀=I`，没有删除 B、E 的均值或假定它们无散。

记 `g_a(x)=(4πa)^(−3/2)exp(−|x|²/(4a))`，完整周期热核 `K_a(x)=Σ_{n∈Z³}g_a(x+n)`。对一阶和三阶导数张量，周期化、三角不等式和 Gaussian 缩放给
\[
 \|D^mK_a\|_{L^1(\mathbb T^3;F)}
 \le\int_{\mathbb R^3}|D^mg_a(x)|_F\,dx
 =c_m a^{-m/2},\qquad m=1,3,
 \quad c_m:=\int_{\mathbb R^3}|D^mg_1(x)|_F\,dx<\infty.
 \tag{RTI.1}
\]
这里是一阶向量或三阶全导数张量的 Frobenius 范数，不是单个分量的常数。有限性可直接由
\[
 \partial_i g_1=-\frac{x_i}{2}g_1,\qquad
 \partial_i\partial_j\partial_\ell g_1
 =\left(\frac{\delta_{ij}x_\ell+\delta_{i\ell}x_j+\delta_{j\ell}x_i}{4}
 -\frac{x_ix_jx_\ell}{8}\right)g_1
 \tag{RTI.2}
\]
及多项式乘 Gaussian 的绝对可积性验证。没有对 c₁、c₃ 作数值求值。

令 `L_a T=P div S_a T`，a>0。逐个非零模，`Δ⁻¹` 的符号为 `−|ξ_k|⁻²`，所以正确的全算子身份是
\[
 (L_aT)_i=\sum_j\partial_j S_aT_{ij}
 +\int_a^\infty\sum_{j,\ell}
 \partial_i\partial_j\partial_\ell S_bT_{j\ell}\,db.
 \tag{RTI.3}
\]
第二项的 Fourier 符号是 `−iξ_iξ_jξ_ℓ e^(−a|ξ|²)/|ξ|²`，与第一项合成 P 的正确负号。零模两项均因导数为0，与 P₀=I 相容；没有在 Δ⁻¹ 的零模作除法。RTI.1 给三阶项在 `[a,∞)` 的绝对算子积分可积，故 RTI.3 也是合法的 L∞ Bochner 积分，而非仅形式逐模式。张量收缩的 Cauchy–Schwarz、RTI.1 和 `∫_a^∞b^(−3/2)db=2a^(−1/2)` 给
\[
 \boxed{\ \|L_aT\|_\infty\le C_L a^{-1/2}\|T\|_{\infty;F},
 \qquad C_L=c_1+2c_3.\ }
 \tag{RTI.4}
\]
这个常数适用于全部 a>0；使用 Euclidean 周期化上界即可，包括大 b 尾，不需要有限频率近似。RTI.4 控制的是带热与导数的完整算子，没有断言裸 P 在 L∞ 上有界。

## RTI.2 热后乘积的精确桥身份

对任意两个光滑周期向量场 F、G（不要求无散或零均值），按周期延拓定义完整张量
\[
 H_\rho(F,G)(x)=\int_{\mathbb R^3}g_{\rho/2}(z)
 F(x+z)\otimes G(x-z)\,dz,
 \qquad \|H_\rho(F,G)\|_{\infty;F}\le\|F\|_\infty\|G\|_\infty.
 \tag{RTI.5}
\]
Gaussian 质量为1使此积分绝对收敛。对所有 x，
\[
 (S_\rho F)(x)\otimes(S_\rho G)(x)
 = S_{\rho/2}H_\rho(F,G)(x).
 \tag{RTI.6}
\]
直接证明：右边是 `∫∫g_a(y)g_a(z)F(x−y+z)⊗G(x−y−z)dy dz`，a=ρ/2。作 `u=y−z, v=y+z`，Jacobian 为 `2⁻³`，且 `|y|²+|z|²=(|u|²+|v|²)/2`；于是 `2⁻³g_a((u+v)/2)g_a((v−u)/2)=g_ρ(u)g_ρ(v)`，恰得左边。此证明使用周期延拓的完整积分，全部周期像均在；Fubini 由有界场和正可积核支付。

也可逐有序频率 `(p,q)` 核对：桥给因子 `exp[−(ρ/2)|ξ_p−ξ_q|²]`，外层热再乘 `exp[−(ρ/2)|ξ_p+ξ_q|²]`，乘积恰为 `exp[−ρ(|ξ_p|²+|ξ_q|²)]`。这个检查包括 p=0、q=0、p+q=0 和全部正负频率，未通过相位平均丢项。RTI.6 保留 F⊗G 的顺序，不用对称化或不可用的散度消项。

定义双线性交换差 `Q_ρ(F,G)=S_ρ(F⊗G)−S_ρF⊗S_ρG`。由 RTI.4–6，
\[
 \begin{aligned}
 \|\mathbb P\operatorname{div}Q_\rho(F,G)\|_\infty
 &\le C_L\{\rho^{-1/2}\|F\otimes G\|_{\infty;F}
 +(\rho/2)^{-1/2}\|H_\rho(F,G)\|_{\infty;F}\}\\
 &\le C_*\rho^{-1/2}\|F\|_\infty\|G\|_\infty,
 \qquad C_*=(1+\sqrt2)(c_1+2c_3).
 \end{aligned}\tag{RTI.7}
\]
ρ>0 是必需的；本稿没有在 ρ=0 代入该上界。

## RTI.3 全部有序混合项与误差自作用

合同的 `C_ρ(Z)=Q_ρ(Z,Z)` 严格满足
\[
 C_\rho(B+E)-C_\rho(B)=Q_\rho(B,E)+Q_\rho(E,B)+Q_\rho(E,E).
 \tag{RTI.8}
\]
其中包括 `S_ρ(B⊗E+E⊗B+E⊗E)`，以及带负号的全部热后项 `S_ρB⊗S_ρE+S_ρE⊗S_ρB+S_ρE⊗S_ρE`。逐项用 RTI.7 得所求明确常数界
\[
 \boxed{\ \|\mathbb P\operatorname{div}[C_\rho(B+E)-C_\rho(B)]\|_\infty
 \le C_*\rho^{-1/2}\bigl(2\|B\|_\infty\|E\|_\infty+\|E\|_\infty^2\bigr).\ }
 \tag{RTI.9}
\]
因子2正是两个有序交叉，并非遗漏一项后补的对称假设。证明对任意光滑 B、E 成立，包括均值非零、非无散和复横向分解之前的场。E=0 时实际差与界均为0；B=0 时保留完整 EE 项；常值等退化情形可有实际抵消，RTI.9 不提供非零下界。

## RTI.4 原固定误差裕量的实际尺度

现在只代入合同已给的同一周期场分解 `U=B+E` 与晚时界，固定 `λ_p>0`、`τ=λ_p²ρ`、`A=1/2+h`：
\[
 \|B\|_\infty\le C_B\tau^{-A},\qquad
 \|E\|_\infty\le C_E\tau^{-A+\epsilon},\qquad \epsilon=h/4.
 \tag{RTI.10}
\]
常数已允许吸收原固定周期缩放，不能再改变 λ_p、热时间或误差指数。由 `ρ⁻¹/²=λ_pτ⁻¹/²`，RTI.9 给
\[
 \begin{aligned}
 &\tau^{A+1}\|\mathbb P\operatorname{div}[C_\rho(U)-C_\rho(B)]\|_\infty\\
 &\quad\le C_*\lambda_p\left(2C_BC_E\tau^{\epsilon-h}
 +C_E^2\tau^{2\epsilon-h}\right)
 =C_*\lambda_p\left(2C_BC_E\tau^{-3h/4}+C_E^2\tau^{-h/2}\right).
 \end{aligned}\tag{RTI.11}
\]
因此这条绝对范数证书并不推出目标趋0。它也不推出目标发散、不趋0、原完整残差非零或机制不可能：右边是上界，实际有符号张量及 Pdiv 仍可能消去。若已有较锐的 `τ^(−A+h/2)(1+|logτ|)^M` 速度界，完全相同的代入给交叉项 `τ^(−h/2)(1+|logτ|)^M` 与自作用项 `(1+|logτ|)^(2M)`，仍不从此界获得趋0；没有借此提高实际误差阶。纯幂条件 ε>h 是 RTI.11 足够小阶的一种充分条件，不是所有可能证明、所有场或所有消去的必要条件。

本稿只支付传递接口。现有速度比较未支付缩放后**完整有符号**交换差的消去或更强控制，因而也不支付它与实际 `S_ρPF`、`−ΔV_h` 的合成；完整残差仍为旧接口的 `G_h=S_ρPF−ΔV_h−Pdiv C_ρ(U)`。B/E 单独不无散的事实没有改变这项限制。后续实际输入边界由 root 的合同第3项另列，本稿不选择新输入、不把热张量正性当成向量/能量符号，也不推到原 a* 的动力学或强稳定。

## 实际阅读与字节

- 本目录 `CONTRACT.md` 全文，SHA-256 `17e94e397c9832de1c3e9fe5c49038403cffef564da01dd92e88365dd98c427f`；RTI.10 作为该合同明列的既有输入使用。没有读取本目录 root 新稿。
- 本人前稿 `../heat-vorticity-tail-preflight/WEIGHTED_ERROR_INDEPENDENT.md`，此前全文自读，本轮只复读第85–106行（WE.5/10及周期缩放入口）并核 SHA `fb7a2f8284f2f1a838306e3a68f9a2ae7cb6cf76a9a63b574d05832eb8f38018`；未重开原文构造或改善已停误差幂次。
- 本人旧 `../heat-vorticity-tail-preflight/INDEPENDENT_INTERFACE.md`，本轮只复读第54–99行的 HTI.5–10 残差/交换差范围，SHA `bf3a8c2a2fe330cdf930877222f349f52b85ceab6f0c410aabecff5bf43fbcff`。该稿的 E=V−U 与本稿 E=U−B 记号不同，不相互替换。
- RTI.1–11 的核、桥恒等式和幂次在本稿自含手核；本轮没有新增外部原文阅读或数值常数求值。以上是条件性分析接口，不声称经典热核方法新颖，不认证实际残差下界或 NS 无力尾段。
