# 最低行之后：两个高投影的共享面积与正幅度精确消元

2026-09-08，PRIVATE_CORE。独立有界推导，待非作者审查和根比较。

**结果：固定合同几何、共同实最低代表和两个发送投影后，最低 Z 确定发送实部。若最低 C 的实三次式已经成立，则两个高投影各自唯一锁定一个非零面积平方和一个所需最低幅度。存在同一组两非零面积及同一个正最低幅度，当且仅当本文的两个平方为正、它们满足最低有符号面积比的平方关系、两行所需幅度相等且为正。给出全部解的恢复式，并保留零实部、零 χ、非正平方及幅度不相容分支。充要性严格限于最低行和这两个高投影。**

本稿先全文读已锁定 PROJECTED_PAIR_CONTRACT.md，只使用本人已形成的 TEI、HI 文本；未读任何根新推导、其它高行稿或新审查。HI 作为已完成但尚待分开审查的输入使用，若输入修正须同步复核。全部手工符号，没有程序、数组、数值求值、实际频率/种子/幅度/时间选择、扫描、Git、重置、外发或发布。

## 1. 实际来源与固定数据

路径相对于 research/reverse/。

| 实际来源及阅读范围 | SHA-256 |
|---|---|
| two-elliptic-compatibility/PROJECTED_PAIR_CONTRACT.md，本轮先全文读取 | 1974afe029ad619aa1bccc43e1ecef1ed2ca454a47c20f43ed78952159d3b3a0 |
| two-elliptic-compatibility/INDEPENDENT.md，本连续任务已全文自核；本轮实际重读第 107–252 行，即 TEI.9–19 及 TEI.20 的引入 | 9a39799e39b9ec40e4ae61e86f3b0dda0dabc0885dcbea17febd91b868524da9 |
| two-elliptic-compatibility/HIGHER_ROW_INDEPENDENT.md，本连续任务前一轮全文自核；本轮实际重读第 250–320 行，即原三边对应及 HI.14–20 | ab7df7bbf6d698c2ee6bb223c06fe478cc34ecc37db1806bc8a774a9c037d9e0 |

这些文件内部列出的其它来源没有自动算作本轮实读。本补充不借用最低可解性存在族中的其它成员。

固定合同中的合法独立整数三频 p0、p1、p2，P_i=|p_i|² 且 P0<P1<P2。记
\[
c_{ij}=p_i\cdot p_j\ne0,\qquad
\Delta_{ij}=P_iP_j-c_{ij}^2>0,\qquad
\ell_{ij}=\sqrt{\Delta_{ij}/P_i}.
\]
原两条最低 β 零几何成立。固定一个 R∈R³∖{0}，R⊥p0、R·p1 和 R·p2 均非零。实际最低种子为
\[
U_0=z_0R,\qquad h=|z_0|^2>0,
\tag{PP.1}
\]
其中 h 尚待求。R 的代表及尺度已经固定，不随某一高行改变。

合同给定的两个非零发送平面投影复系数记为 x1、x2，沿用 TEI 的未单位化基：
\[
f_{0i}=p_0-\frac{c_{0i}}{P_i}p_i,\qquad
n_{0i}=p_0\times p_i,\qquad
U_i=x_i\bigl(f_{0i}+(\xi_i+i\theta_i)n_{0i}\bigr).
\tag{PP.2}
\]
x_i 的模方和相位都保持给定值；如果给定的是单位基系数或 U_i·p0，按固定几何作非零实尺度转换即可，后者满足 U_i·p0=x_iΔ_i0/P_i。ξ_i 已由最低 Z 唯一确定；只有 θ1、θ2∈R∖{0} 与共同 h 待求。

## 2. 最低行输入和必须保留的有符号面积比

为明确固定关系，令最低单位基 E_0i 为 pi 在 p0⊥ 的单位投影，N_0i=(p0×pi)/(√P0ℓ_0i)，并记
\[
C_0=E_{01}\cdot E_{02},\quad S_0=N_{01}\cdot E_{02}\ne0,\quad
T=\frac{R\cdot E_{02}}{R\cdot E_{01}}\in\mathbb R\setminus\{0\}.
\]
χ_ij、α_ij、L_ij 沿用 HI/TEI 的完整几何系数。最低实际发送平面权重比为
\[
\varrho=
\frac{L_{02}|x_2|^2\chi_{02}/\ell_{02}}
{L_{01}|x_1|^2\chi_{01}/\ell_{01}}\in\mathbb R\setminus\{0\}.
\]
它固定，且符号为 sgn(c01c02)。TEI.13–14 给
\[
\eta_{01}=\frac{C_0-2T-\varrho T^2}{S_0},\qquad
\eta_{02}=\frac{-C_0+2/T+1/(\varrho T^2)}{S_0},
\]
\[
\xi_i=
\frac{2c_{0i}(P_0-P_i)}
{\sqrt{P_0}\,P_i(5P_0+4P_i)}\,\eta_{0i}.
\tag{PP.3}
\]
两 ξ_i 是给定数据的确定实数，可以为零，不再随高行修改。

以下直接假设最低 C 的 TEI.16 实三次式在这个同一 T 上成立。它不含 θ_i 或 h，但完整最低 C 方向还准确要求
\[
P_1\theta_1+\varrho P_2T^3\theta_2=0.
\]
因此固定非零有符号数
\[
\boxed{\zeta=-\frac{\varrho P_2T^3}{P_1},\qquad
\theta_1=\zeta\theta_2,\quad\theta_2\ne0.}
\tag{PP.4}
\]
这不是两个独立面积大小。面积本身为
\[
\mathfrak h_i=
\frac1{2i}p_i\cdot(\overline U_i\times U_i)
=-\Delta_{0i}|x_i|^2\theta_i\ne0.
\tag{PP.5}
\]
固定 x_i 后，PP.4 同时规定了面积的符号比和绝对值比。

## 3. 同一高种子的接收比值：法向反号必须保留

对高接收 i，令另一高指标 j 满足 {i,j}={1,2}。定义 HI 的实单位基
\[
E_{i0}=\frac{p_0-c_{i0}p_i/P_i}{\ell_{i0}},\quad
N_{i0}=\frac{p_i\times p_0}{\sqrt{P_i}\ell_{i0}},\quad
E_{ij}=\frac{p_j-c_{ij}p_i/P_i}{\ell_{ij}},
\]
\[
C_i=E_{i0}\cdot E_{ij},\qquad
S_i=N_{i0}\cdot E_{ij}\ne0.
\]
因为 n_0i=−(pi×p0)，PP.2 精确写成
\[
U_i=x_i\ell_{i0}
\left[E_{i0}-\sqrt{P_i}(\xi_i+i\theta_i)N_{i0}\right].
\]
故同一高种子的实际接收比值为
\[
\boxed{
t_i=\frac{U_i\cdot E_{ij}}{U_i\cdot E_{i0}}
=a_i+i d_i\theta_i,\quad
a_i=C_i-\sqrt{P_i}S_i\xi_i,\quad
d_i=-\sqrt{P_i}S_i\ne0.}
\tag{PP.6}
\]
a_i、d_i 已经固定。a_i 可以为零，须在后面单独处理；θ_i 非零保证 t_i 非实，有限且非零。

这也与 HI.16 的同一向量表达式一致：
\[
t_i=\sqrt{\frac{\Delta_{i0}}{\Delta_{ij}}}
\frac{U_i\cdot p_j}{U_i\cdot p_0}.
\tag{PP.7}
\]
同一个 U_i 在另一行作为发送时，交叉点积 U_i·pj 就由这个 t_i 及固定 U_i·p0 决定。

令 Y_i=Im t_i=d_iθ_i。由 PP.4，
\[
\boxed{Y_1=mY_2,\qquad m=\frac{d_1\zeta}{d_2}\ne0.}
\tag{PP.8}
\]
有向三重积 J=(p0×p1)·p2≠0 给
\[
S_1=-\frac{J\sqrt{P_1}}{\sqrt{\Delta_{10}\Delta_{12}}},
\qquad
S_2=\frac{J\sqrt{P_2}}{\sqrt{\Delta_{20}\Delta_{12}}}.
\]
所以
\[
\frac{d_1}{d_2}
=-\frac{P_1}{P_2}\sqrt{\frac{\Delta_{20}}{\Delta_{10}}},
\qquad
\boxed{m=\varrho T^3\sqrt{\frac{\Delta_{20}}{\Delta_{10}}}.}
\tag{PP.9}
\]
两个高接收的法向取向相反，这个符号已经计入。使用平方关系以后仍须恢复 PP.8 的有符号式。

## 4. 实际共享权重与两个复投影

每个高接收面对较短线性发送 p0。HI.6 给固定比值
\[
b_i=\frac{\kappa_{i0}}{\chi_{i0}}>2,\qquad\chi_{i0}\ne0.
\]
同一实最低代表决定线性发送比值
\[
\rho_i=
\frac{R\cdot(p_i\times p_0)}
{P_0(R\cdot p_i)}\in\mathbb R,\qquad
\tau_i=(1-b_i)C_i+
S_i\frac{\sqrt{P_i}\alpha_{i0}\rho_i}{\chi_{i0}}\in\mathbb R.
\tag{PP.10}
\]
这些值与 z0 的相位、h 及 θ1、θ2 无关。两行的 ρ_i 来自同一个 R，不独立选取。

HI.15 的真实权重为
\[
\lambda_i=
\frac{P_j\sqrt{\Delta_{ij}}\chi_{ij}}
{P_0\sqrt{\Delta_{i0}}\chi_{i0}}\,
\frac{|U_j\cdot p_i|^2}{h(R\cdot p_i)^2}.
\]
由 PP.7 以及 U_j·p0=x_jΔ_j0/P_j，化成
\[
\boxed{\lambda_i=\frac{K_i}{h}|t_j|^2,}
\]
\[
\boxed{
K_i=
\frac{|x_j|^2\,\Delta_{j0}\Delta_{ij}^{3/2}\chi_{ij}}
{P_0P_j\sqrt{\Delta_{i0}}\chi_{i0}(R\cdot p_i)^2}
\in\mathbb R.}
\tag{PP.11}
\]
K_i 已由固定数据决定，含真实投影模方；它没有 θ 或 h，可能为零或任一符号。h 是唯一共同最低幅度，不能把两行分母分别调节。

两个高行沿另一高频的完整复点积为零，分别精确等价于 HI.8：
\[
\boxed{\lambda_i t_i^2+b_it_i+\tau_i=0,\qquad i=1,2.}
\tag{PP.12}
\]
这是沿 E_ij 的两个完整投影；另一发送的法向相干因其法向与 E_ij 正交而不出现在该式。其它分量仍保留完整相干，尚未被求解。

## 5. 每行锁定面积平方和所需幅度

先处理不能除掉的分支。若 a_i=0，则 t_i=iY_i、Y_i≠0，PP.12 的虚部为 b_iY_i≠0，所以该投影不能为零。若 K_i=0，则 λ_i=0，PP.12 同样只允许实 t_i，仍不通过。

以下假设 a_iK_i≠0。PP.12 的虚部除以非零 Y_i 给
\[
2\lambda_i a_i+b_i=0.
\]
故每行实际权重必须取固定值
\[
\boxed{\lambda_i=\Lambda_i:=-\frac{b_i}{2a_i}\ne0.}
\tag{PP.13}
\]
把它代回实部，得到
\[
a_i^2+Y_i^2=\frac{\tau_i}{\Lambda_i}.
\]
定义完全由固定数据确定的实数
\[
\boxed{
M_i=-\frac{2a_i\tau_i}{b_i}-a_i^2,\qquad
N_i=a_i^2+M_i=\frac{\tau_i}{\Lambda_i}.}
\tag{PP.14}
\]
通过投影必须且仅能取 Y_i²=M_i。由于 Y_i≠0，要求 M_i>0；此时 N_i>0，τ_i 也非零。与 HI 的判别式对应为
\[
b_i^2-4\Lambda_i\tau_i=-4\Lambda_i^2M_i<0.
\tag{PP.15}
\]
因此 M_i=0 是面积为零的禁用边界，M_i<0 没有实面积大小；没有靠重实根或纯虚 t_i 绕过合同。

由 PP.11、13，行 i 对同一最低幅度的要求为
\[
\boxed{
h=H_i:=\frac{K_iN_j}{\Lambda_i}
=-\frac{2a_iK_i}{b_i}(a_j^2+M_j).}
\tag{PP.16}
\]
当 M1、M2>0 时，
\[
H_i>0\iff a_iK_i<0.
\tag{PP.17}
\]
这精确记录实际权重符号：Λ_i 与 K_i 必须同号，接收比值实部与 K_i 必须异号。两行即使各自给出正 H_i，也必须给同一个值。

## 6. 这组最低行加两个投影的条件充要判据

在第 1–2 节固定输入及最低 C 实三次式已经成立的前提下，存在 θ1、θ2≠0 和 h>0，使最低完整 Z 为零、最低完整 C 为非零原方向输出、且两个高投影 PP.12 均为零，当且仅当：

\[
\boxed{
a_1K_1a_2K_2\ne0,\qquad
M_1>0,\quad M_2>0,}
\]
\[
\boxed{
M_1=m^2M_2,\qquad
H_1=H_2>0.}
\tag{PP.18}
\]
这些是固定数据的显式等式、不等式。没有剩余可各自调节的两个面积大小或两个最低幅度。

必要性已由 PP.8、13–17 给出。充分性可以逐项恢复，且给出全部允许未知量：
\[
\boxed{
\theta_2=\varepsilon\,\frac{\sqrt{M_2}}{d_2},\qquad
\theta_1=\zeta\theta_2,\qquad
h=H_1=H_2,\qquad \varepsilon\in\{-1,1\}.}
\tag{PP.19}
\]
由于 M2>0、d2≠0、ζ≠0，两 θ 非零，且 PP.4 的有符号面积比准确成立。由 PP.8、18 得 Y2²=M2、Y1²=M1。PP.11、16 又给每行 λ_i=Λ_i；最后 PP.13–14 同时令该投影的实部和虚部为零。这没有在某一行替换发送向量。

z0 可具有任意相位且满足 |z0|²=h；两个 ε 是共同虚部符号的两种选择，不能在两行分别另选。反过来，任何合法解的 Y2²=M2 和有符号 PP.8 都迫使它属于 PP.19，h 也唯一。未知量的这一恢复是符号存在证明，没有选择实际频率、极化或数值幅度。

PP.3、4 保证最低完整 Z 零行及最低 C 复方向。最低 C 的非零性沿用 TEI.12、18 后的独立法向论证：去掉共同 z0² 后，其保留面积部分是两个独立最低法向上的非零系数和，因 θ1、θ2 均非零而不能为零。恢复 z0² 不改此非零性与原方向。因此这里的最低 C 是非零输出，未把零向量计作方向通过。

实际面积大小也已锁定：
\[
|\mathfrak h_i|^2
=\Delta_{0i}^2|x_i|^4\,\frac{M_i}{d_i^2}>0.
\tag{PP.20}
\]
面积符号按 PP.5、19 恢复；单凭 PP.18 的平方关系而忽略 ζ 的符号，并不能得到同一最低 C 方向。

两行幅度相等还可无损写成
\[
\boxed{K_1\tau_2=K_2\tau_1,}
\tag{PP.21}
\]
因为 N_j=τ_j/Λ_j，故 H_i=K_iτ_j/(Λ_iΛ_j)。但 PP.21 只替代 H1=H2，仍须另外保留正性和全部面积条件；它单独不充分。

## 7. 零、符号与共享分支

判据中的边界准确如下：

- 任一 χ_ij=0，即 K_i=0：另一平面项消失，剩余线性投影不能消去面积非零接收。在原 P0<P1<P2 中 χ_21、χ_10、χ_20 非零，只有 χ_12 仍可能为零；它等价于 H_12=0，按 HI.21 是明确条件障碍。这里 H_12=4P1²−P1P2+P2²−4c12² 是几何系数，区别于本文所需幅度 H_i。
- 任一 a_i=Re t_i=0：虚部 b_iY_i 非零，所有面积大小和正 h 均失败。
- a_iK_i≠0 但任一 M_i≤0：负值无实平方，零值使面积为零，均被排除；特别 τ_i=0 时 M_i=−a_i²<0。
- 两 M_i>0 但 M1≠m²M2：各自投影所需大小不符合最低有符号面积比，不能用两个不同种子补齐。
- 面积平方相容但任一 H_i≤0：不允许的最低幅度；当两 M 正时此条件等价于对应 a_iK_i 符号不合。
- 两 H_i 均正而不相等：每行各自所需的最低幅度不同，同一个 U0=z0R 不能满足两者。

如果 PP.18 全部通过，正或负 K_i 都由 PP.17 正确保留，PP.19 恢复有符号面积；没有把权重固定为正。ξ_i、ρ_i、C_i 或最低实部消元中的 η_0i 为零都不被约去，直接进入 a_i、τ_i 即可。S0、S_i、d_i、T、ζ、m、x_i 及两个 R·pi 的零值由当前合同排除；若去掉这些活跃或独立假设，须另立退化合同，不能使用这里的除法。

对 PP.19 的两种共同符号，高种子的实、虚部仍独立。因此其对另一非平行实频率的交叉点积非零；最低两个投影非零已经由固定 R 保证。也可直接由 PP.7 的有限非实 t_i 验证这些高交叉点积。每个 U_i 在发送和接收中的全部坐标均来自 PP.2 的同一个向量。

## 8. 准确范围

PP.18 是本合同固定输入下，最低行加两个指定高投影的条件充要消元；它不预先保证这些固定数据条件会通过。也没有证明它们必然冲突、必然可行，或存在实现它们的合法整数几何。若判据失败，只排除当前固定几何、R、x1、x2 的这一组投影要求，不自动排除所有其它固定数据。

每个高行还有 HI.13 的独立完整分量尚未求解，其中的另一发送相干不能删除。其它两个 C 方向及三行共同模板幅度也未支付。这里不能把最低方向已通过和两个高投影为零合并成完整三行、实际有限两步机制或再生成。

全程使用同一组三种子。没有把最低存在族的不同成员拼接，没有新增真实 NS 时间、余项或跨代控制，没有实际参数、候选接纳或旧失败证据修复。单初值无限尺度、有限总时间及奇性仍在范围外。

EXACT CONDITIONAL ELIMINATION FOR LOWEST ROW AND TWO HIGH PROJECTIONS；FULL HIGHER ROWS OPEN；NO-CANDIDATE；NOT CLAY。
