# 完整两高行的四实条件与共同虚部符号的无损消去

2026-09-08，PRIVATE_CORE。独立有界推导完成，待非作者审查及根比较。

**结果：在明确列出的最低条件和共享投影条件下，两个高行尚缺的完整分量等价于本文四条显式实等式。另一发送的比值和模方由同一个种子准确换基获得。共同虚部正负选择可以无损消去：四式若成立，两种共同符号都通过；若任一失败，两种都失败。结合前置条件，这给出本固定数据类型内“完整总 M0=0 且最低 C 为非零原方向输出”的条件充要接口，不保证该接口有解。**

本稿先全文读锁定合同，未读本目录 PROOF.md 或任何本项其它新推导。本人已形成前阶段 TEI、HI、PP，并在之后非作者审读过前阶段面积独立稿；这一阅读历史不称作盲态。这里不以面积稿或未完成综合接纳的阶段作为新定理输入：以下实际使用的前置条件明确列为直接等式，并从 NC 和同一向量换基重新手核所需步骤。若前置源变更须同步复核。

全部手工符号，没有科学程序、数组、数值求值、实际几何/种子/幅度/时间选择、扫描、Git、重置、外发或发布。

## 1. 实际来源与前置量词

路径相对于 research/reverse/。

| 来源及实际阅读范围 | SHA-256 |
|---|---|
| full-high-row-reduction/CONTRACT.md，本轮先全文读取 | 8f1dd745dc12409f3e49b7b56073b3fb38fca4a26d23774f0df4ea12292ecc6e |
| two-elliptic-compatibility/PROJECTED_PAIR_INDEPENDENT.md，本轮实际重读第 1–282 行，PP.1–21；此前已全文自核 | 44c1f7fd6b616bd3bc1313c8b08607331f641f805329070ea4f93db5e72d8eef |
| two-elliptic-compatibility/HIGHER_ROW_INDEPENDENT.md，本轮重读第 185–248 行的零系数、投影分类及完整余分量；此前已全文自核 | ab7df7bbf6d698c2ee6bb223c06fe478cc34ecc37db1806bc8a774a9c037d9e0 |
| net-mixed-cancellation/INDEPENDENT.md，本轮实际重读第 1–119 行，NC.1–10；此前已全文非作者核验 | 25111397d32eef2751a91b1ad1ab6a446794742874b97bf6b0b73b3964d11a58 |
| three-edge-compatibility/MAX_RECEIVER_RATIO.md，本连续任务前一轮全文重读，本轮复核字节 | ff52531d6e1b5563c99504aba8e6b6e4e5afce77b76e7e286e74d397c3d610c5 |
| two-elliptic-compatibility/INDEPENDENT.md，本连续任务前一轮实际重读第 120–338 行的最低接口，本轮复核字节 | 9a39799e39b9ec40e4ae61e86f3b0dda0dabc0885dcbea17febd91b868524da9 |

源文件内部转引的其它文件不自动列为实读。这里不声称整个前阶段已完成审查，也不把源稿形成时的状态文字当最终接纳记录。

固定同一合法独立整数三频 p0、p1、p2，P_i=|p_i|² 且 P0<P1<P2，全部非正交，并具有原两条最低 β 零几何。固定非零实 R⊥p0，R·p1、R·p2 非零；固定两个非零发送投影复系数 x1、x2。种子必须统一恢复为
\[
U_0=z_0R,\qquad
U_i=x_i\bigl(f_{0i}+(\xi_i+i\theta_i)n_{0i}\bigr),\quad i=1,2,
\]
\[
f_{0i}=p_0-\frac{p_0\cdot p_i}{P_i}p_i,\qquad
n_{0i}=p_0\times p_i,\qquad h=|z_0|^2>0.
\tag{FH.1}
\]
负模为这同一组三种子的共轭。ξ_i 是最低 Z 唯一公式 PP.3/TEI.13–14 的固定实数；最低 C 实三次式在同一最低方向 T 上成立，作为直接前提。无需在此重证最低引理。

使用 PP 的最低量 T、权重比 varrho，必须保留同一个有符号面积条件
\[
\theta_1=\zeta\theta_2,\qquad
\zeta=-\frac{\varrho P_2T^3}{P_1}\ne0.
\tag{FH.2}
\]
这不是可独立指定的两个高发送面积。

## 2. 显式列出的投影输入及重新手核

对 {i,j}={1,2}，令 c_ij=pi·pj、Δ_ij=P_iP_j−c_ij²>0、ℓ_ij=√(Δ_ij/P_i)，定义正定向单位基
\[
E_{ij}=\frac{p_j-c_{ij}p_i/P_i}{\ell_{ij}},\qquad
N_{ij}=\frac{p_i\times p_j}{\sqrt{P_i}\ell_{ij}}.
\]
每组 E_ij×N_ij=pi/√Pi；再记
\[
C_i=E_{i0}\cdot E_{ij},\qquad S_i=N_{i0}\cdot E_{ij}\ne0.
\]
共有 E_ij=C_iE_i0+S_iN_i0、N_ij=−S_iE_i0+C_iN_i0。同一 U_i 的接收比值为
\[
t_i=\frac{U_i\cdot E_{ij}}{U_i\cdot E_{i0}}
=a_i+i d_i\theta_i,\qquad
a_i=C_i-\sqrt{P_i}S_i\xi_i,\quad d_i=-\sqrt{P_i}S_i\ne0.
\tag{FH.3}
\]
这里的反号来自 n_0i=−√Piℓ_i0 N_i0，不更改任何基的正定向。

完整几何系数全部按 NC 定义。为使下文可直接核算，记
\[
\Lambda_{ij}=(P_i+P_j)^2-4c_{ij}^2>0,\quad
\Omega_{ij}=(4P_i+P_j)^2-16c_{ij}^2>0,
\]
\[
H_{ij}=4P_i^2-P_iP_j+P_j^2-4c_{ij}^2,\quad
h^\pm_{ij}=\frac{P_j\pm2c_{ij}}
{(P_i+P_j\pm2c_{ij})(4P_i+P_j\pm4c_{ij})},
\]
\[
\alpha_{ij}=2-(P_i-P_j)(h^+_{ij}+h^-_{ij}),\qquad
\beta_{ij}=-(P_i-P_j)(h^+_{ij}-h^-_{ij}),
\]
\[
\kappa_{ij}=\frac{4c_{ij}(P_i-P_j)P_i}{P_j\Lambda_{ij}},\quad
\chi_{ij}=
\frac{4c_{ij}(P_i-P_j)(2P_i+P_j)H_{ij}}
{P_j\Lambda_{ij}\Omega_{ij}}.
\tag{FH.4}
\]
高行的较短线性发送给
\[
b_i=\kappa_{i0}/\chi_{i0}>2,\quad
\rho_i=\frac{R\cdot(p_i\times p_0)}{P_0(R\cdot p_i)},\quad
\eta_i=\frac{\sqrt{P_i}\alpha_{i0}\rho_i}{\chi_{i0}},
\quad \tau_i=(1-b_i)C_i+S_i\eta_i.
\]
两个真实发送投影模方决定固定实系数
\[
K_i=
\frac{|x_j|^2\Delta_{j0}\Delta_{ij}^{3/2}\chi_{ij}}
{P_0P_j\sqrt{\Delta_{i0}}\chi_{i0}(R\cdot p_i)^2}.
\tag{FH.5}
\]
精确投影权重为 λ_i=(K_i/h)|t_j|²。该式可由
U_j·p0=x_jΔ_j0/P_j 及
t_j=√(Δ_j0/Δ_ij)(U_j·pi)/(U_j·p0)
直接重算；没有调节独立通道幅度。

以下列出的条件作为本稿明确的投影输入：
\[
a_iK_i\ne0,\qquad
L_i:=-\frac{b_i}{2a_i}\ne0,\qquad
M_i:=-\frac{2a_i\tau_i}{b_i}-a_i^2>0,\quad
N_i:=a_i^2+M_i>0,
\]
\[
m:=\frac{d_1\zeta}{d_2}
=\varrho T^3\sqrt{\frac{\Delta_{20}}{\Delta_{10}}}\ne0,\qquad
M_1=m^2M_2,
\]
\[
\boxed{\frac{K_1N_2}{L_1}=\frac{K_2N_1}{L_2}=h>0.}
\tag{FH.6}
\]
这里 L_i 是已锁投影权重，等于 PP.13 的单下标 Λ_i；它不是 NC 的双下标几何 Λ_ij，也不是双线性映射。以上分母已明确分开。

重新核其作用：完整 NC 在 E_ij 上的点积归一化为
λ_it_i²+b_it_i+τ_i。若 t_i=a_i+iY_i 且 Y_i≠0，其虚部给 λ_i=L_i，其实部给 Y_i²=M_i；所以若任一 a_i 或 K_i 为零，或 M_i≤0，面积非零投影已不能通过。FH.2 再给 Y1=mY2，共同正 h 给 FH.6 最后一式。反过来，这些等式直接恢复同一数据中的两个指定投影为零。

所有剩余候选未知量因此统一表示为
\[
y_2=\sqrt{M_2}>0,\qquad y_1=my_2\ne0,\qquad
t_i=a_i+i\varepsilon y_i,\qquad
\theta_i=\varepsilon y_i/d_i,\quad \varepsilon\in\{-1,1\}.
\tag{FH.7}
\]
有 y_i²=M_i、|t_i|²=N_i，实际 λ_i=L_i。两个 ε 必须同取；z0 只剩任意相位及已定正模方 h。这里没有预先接纳前阶段整包，只将已写出的条件逐项重核为本稿直接输入。

## 3. 另一发送必须来自同一邻边换基

现在核接收 i 面对发送 U_j 时的真实 f_ij、n_ij 坐标。这两个发送基位于 pj⊥，满足
\[
f_{ij}=p_i-\frac{c_{ij}}{P_j}p_j=\ell_{ji}E_{ji},\qquad
n_{ij}=p_i\times p_j=-\sqrt{P_j}\ell_{ji}N_{ji}.
\]
由同一 U_j 的接收坐标变换，
\[
\frac{U_j\cdot N_{ji}}{U_j\cdot E_{j0}}
=\frac{C_jt_j-1}{S_j},\qquad
U_j\cdot E_{j0}=x_j\ell_{j0}.
\]
若写 U_j=X_ij(f_ij+w_ij n_ij)，则精确有
\[
\boxed{
X_{ij}=x_j\sqrt{\frac{\Delta_{j0}}{\Delta_{ij}}}\,t_j,\qquad
w_{ij}=\frac{t_j^{-1}-C_j}{\sqrt{P_j}S_j}.}
\tag{FH.8}
\]
没有在另一边重选发送复系数。写 w_ij=ξ_ij^s+iθ_ij^s，则
\[
\boxed{
\xi_{ij}^{s}=\frac{a_j/N_j-C_j}{\sqrt{P_j}S_j},\qquad
\theta_{ij}^{s}=-\frac{\varepsilon y_j}{\sqrt{P_j}S_jN_j}
=\frac{\theta_j}{N_j},}
\]
\[
\boxed{|X_{ij}|^2=|x_j|^2\frac{\Delta_{j0}}{\Delta_{ij}}N_j.}
\tag{FH.9}
\]
所有 N_j、t_j、S_j 非零。直接核面积规范：
\[
-\Delta_{ij}|X_{ij}|^2\theta_{ij}^{s}
=-\Delta_{j0}|x_j|^2\theta_j.
\tag{FH.10}
\]
所以相干虚部和投影模方的换基同步保持同一种子的有向面积，而非自由协方差。

FH.9 也直接给出 FH.5 中真实权重的另一核算。它与 ε 无关，但虚相干保留 ε；不能从模方不变推断发送极化不变。

## 4. 完整第二点积和实际系数

由 FH.6，χ_ij≠0。令另一边的有限实比值
\[
B_i=\kappa_{ij}/\chi_{ij}.
\]
只对 i=2 有 B2>2；i=1 不预设其符号或大于 2。对 χ_ij≠0 的一般边，NC 分母直接通分给
\[
\boxed{\beta_{ij}/\chi_{ij}=2-B_i.}
\tag{FH.11}
\]
具体地，若 P=Pi、Q=Pj、c=cij，令 K=4P²−PQ−2Q²+8c²，则
h+−h−=4cK/(ΛΩ)，β=−4c(P−Q)K/(ΛΩ)，而
PΩ−2(2P+Q)H=QK。代入 χ、κ 即得 FH.11，不要求 P>Q；这里只在已付 χ≠0 后使用它。

完整发送相干系数为
\[
\gamma_{ij}=\frac{\sqrt{P_i}}{\chi_{ij}}
\bigl(\alpha_{ij}\xi_{ij}^{s}-i\beta_{ij}\theta_{ij}^{s}\bigr).
\tag{FH.12}
\]
其中负 i 号来自 NC 的 Im(X bar Y)=−|X|²θ。FH.9 使其成为固定实部加 iε 乘固定实系数，不能删去后者。

令 A_i=U_i·E_i0=x_iℓ_i0≠0，
\[
k_{i0}=
\frac{2\Delta_{i0}^3}{P_i^2P_0}\,
\frac{|X_{i0}|^2\chi_{i0}}{\ell_{i0}}\ne0,\qquad
X_{i0}=\frac{P_0}{\Delta_{i0}}(U_0\cdot p_i).
\]
NC 全和除以非零 ik_i0 A_i² 后，沿 E_ij 的第一点积已是 FH.6 所支付的投影；沿 E_i0 的第二点积精确为
\[
\boxed{
\frac{(Z_{i0}+Z_{ij})\cdot E_{i0}}{ik_{i0}A_i^2}
=1+L_i\left[B_it_i+
\bigl((1-B_i)C_i-S_i\gamma_{ij}\bigr)t_i^2\right].}
\tag{FH.13}
\]
这是对完整 NC 向量的实际点积：E_ij·E_i0=C_i、N_ij·E_i0=−S_i，且
(U_i·N_ij)/A_i=(C_it_i−1)/S_i。
因此第二式的 B_i、γ_ij 项均有确定出处。

E_i0、E_ij 在复横向平面独立。第一投影已经为零后，完整高行零当且仅当 FH.13 为零。除以非零 L_it_i² 后，其精确形式为
\[
S_i\gamma_{ij}=(1-B_i)C_i+\frac{B_i}{t_i}+\frac1{L_it_i^2}.
\tag{FH.14}
\]
以下只对这一已写出的完整等式作实虚分离。

## 5. 四个显式实条件与 ε 的无损消去

定义不含面积正负选择的几何正系数和有符号比
\[
D_i=\frac{P_i}{P_j}\sqrt{\frac{\Delta_{j0}}{\Delta_{i0}}}>0,
\qquad q_1=1/m,\quad q_2=m.
\tag{FH.15}
\]
由同一有向三频，
\[
\frac{S_i}{S_j}\sqrt{\frac{P_i}{P_j}}=-D_i,\qquad
q_i=y_j/y_i.
\]
第一恒等式可直接由
S1=−J√P1/√(Δ10Δ12)、S2=J√P2/√(Δ20Δ12)
核得，其中 J=(p0×p1)·p2≠0。

用 1/t_i=(a_i−iεy_i)/N_i 与
1/t_i²=(a_i²−M_i−2iεa_iy_i)/N_i²，得到以下完全显式实数：
\[
\boxed{
\mathcal R_i=
(B_i-1)C_i-\frac{B_ia_i}{N_i}
-\frac{a_i^2-M_i}{L_iN_i^2}
-D_i\frac{\alpha_{ij}}{\chi_{ij}}
\left(\frac{a_j}{N_j}-C_j\right),}
\tag{FH.16}
\]
\[
\boxed{
\mathcal I_i=
\frac{B_i}{N_i}+\frac{2a_i}{L_iN_i^2}
+D_i(B_i-2)\frac{q_i}{N_j}.}
\tag{FH.17}
\]
所有量都来自固定几何、R、x_i、最低确定的 ξ_i 及 FH.6 锁定的平方。没有隐藏的发送相干参数。

为核每个号，FH.12 的实部乘 S_i 后为
−D_i(α_ij/χ_ij)(a_j/N_j−C_j)。
其虚部除以 εy_i 后为
D_i(B_i−2)q_i/N_j。
而 FH.14 右边的虚部为
−εy_i[B_i/N_i+2a_i/(L_iN_i²)]。
这同时给出 FH.16–17，不只给出四个残差的名字。

更精确地，完整第二点积有因式恒等式
\[
\boxed{
\frac{(Z_{i0}+Z_{ij})\cdot E_{i0}}{ik_{i0}A_i^2}
=-L_it_i^2\bigl(\mathcal R_i+i\varepsilon y_i\mathcal I_i\bigr).}
\tag{FH.18}
\]
L_i、t_i、y_i 均非零，且 R_i、I_i 都是实数。因此
\[
\boxed{Z_{i0}+Z_{ij}=0
\iff \mathcal R_i=0,\quad\mathcal I_i=0}
\tag{FH.19}
\]
在已过第一投影的条件下成立。这里没有平方化复等式；仅除以已证非零的 εy_i。于是共同 ε 的消去不增解、不漏解：任一 ε 能通过则四个实数均为零，另一个 ε 也通过；若任一实数不为零，则两种 ε 都不能通过。发送整体相位 x_i 固定，不需要把种子替成另一组独立相位。

## 6. 总 M0 与最低非零 C 的条件充要接口

沿用 NC.3 的准确总向量规范：
\[
M_{0,i}=\frac16\sum_{j\ne i}Z_{ij},\qquad
W_{0,i}=\frac13\sum_{j\ne i}C_{ij}.
\]
负接收为共轭，三正接收是不同频率的分量，故 M0=0 当且仅当三条完整接收总行分别为零。

固定本合同的几何、R 和 x1、x2，并以最低 Z 唯一实部、最低 C 实三次式作为明确前提。在此域内，存在同一组面积非零 U1、U2 及正 h，使
\[
M_0=0,\qquad C_{01}+C_{02}\in\mathbb C U_0\setminus\{0\},
\]
当且仅当 FH.6 的共享投影条件成立，且
\[
\boxed{\mathcal R_1=\mathcal I_1=\mathcal R_2=\mathcal I_2=0.}
\tag{FH.20}
\]
必要性：最低面积方向锁 FH.2，两个高指定投影先锁 FH.6–7，完整另一点积再锁 FH.19。充分性：以 FH.7 恢复任一共同 ε，取同一个 h 及任意 z0 相位；最低 Z 和最低 C 方向由前置实部、实三次式及有符号 FH.2 满足，两个高行由两独立点积均零而完整为零。

最低 C 非零不能靠方向条件空算：按已接纳 TEI 完整 C 表达式，去掉共同 z0² 后，它的面积部分是两个独立最低法向上的非零系数和。FH.7 保证两 θ 非零及最低接收投影非零，所以该和不为零。恢复 z0² 后仍非零，进而 W_0 的最低分量也非零。

这只是可检验的条件充要接口，不证明存在一组固定数据使 FH.20 全部成立，也不证明必然无解。其它两个 C 方向、三行共同模板幅度均未计入此充要性。

## 7. 零支、必要符号和精确边界

前置零支先于任何新除法处理：a_i=0、K_i=0（等价于 χ_ij=0）、M_i≤0、面积平方不相容或所需最低幅度不相等/不正，都不能通过两个指定投影，因而不能达到本合同的完整 M0=0。特别中间边 H12=0 使 χ12=0；最长边 χ21 非零。不存在在这些零支上继续使用 B_i、1/χ_ij 的许可。

进入 FH.6 后，本稿所用新分母为 P_i、Δ_ij、ℓ_ij 的正幂，χ_i0、χ_ij、S_i、N_i、L_i、t_i、m、y_i 及非零点积规范。它们由严格排序、非平行非正交、三频独立、实际投影门和非零面积逐项保证。没有除以 α_ij、β_ij、C_i、ξ_i 或 R_i/I_i；这些量为零均按同一公式检查。

β_ij=0 的分支没有遗漏。FH.11 使此时 B_i=2，而由 L_i=−b_i/(2a_i)，
\[
\mathcal I_i=
\frac2{N_i}-\frac{4a_i^2}{b_iN_i^2}
=\frac{2[N_i-2a_i^2/b_i]}{N_i^2}>0
\]
因为 b_i>2、N_i=a_i²+M_i>a_i²。所以它是明确的剩余分量障碍，不能由删去虚相干后宣称通过。α_ij=0 则只删去 FH.16 中相应实项，不产生额外自由比值。

最长行 i=2 还有必要符号可从新公式直接核得，无需援引前阶段面积结论。B2>2、b2>2 给
\[
\frac{B_2}{N_2}+\frac{2a_2}{L_2N_2^2}
=\frac{B_2N_2-4a_2^2/b_2}{N_2^2}>0.
\]
D2>0、B2−2>0，故 I2=0 强制 q2=m<0。结合 FH.2、6，
\[
\boxed{m<0\iff\varrho T<0,\qquad
\mathfrak h(U_1;p_1)\mathfrak h(U_2;p_2)>0.}
\tag{FH.21}
\]
面积同号不充分，必须继续保留四个等式及全部前置幅度条件。

最低实三次式仍须在这个相同 T 上成立。其已接纳形式
\[
\varrho\Gamma_2C_0T^3-\varrho\mathcal B_0T^2
+\mathcal A_0T-\Gamma_1C_0=0
\]
有 Γ1、Γ2、𝒜0、𝓑0>0；𝒜0、𝓑0 仅指最低三次的正系数。令 varrho=ε0r0、T=−ε0s（r0、s>0），得
\[
-\varepsilon_0 C_0=
\frac{r_0\mathcal B_0s^2+\mathcal A_0s}{r_0\Gamma_2s^3+\Gamma_1}>0.
\]
所以还须 varrho C0<0；C0=0 的最低降次支不满足联合要求。这只是必要号加仍须满足的准确剩余方程，不以某一最低存在支代表全部根，不除掉原最低 D=N=0 或重根分支。

其它几何比值 B1 的正负不预设，中间行不从最长正性直接外推。它必须接受 FH.16–17 的原式检查。

## 8. 最终产出范围

本稿给出真实邻边发送换基 FH.8–10、完整第二点积 FH.13、四个实际实条件 FH.16–17、无损符号消去恒等式 FH.18，以及 FH.20 的准确条件充要接口。前置投影等式已在本稿直接重核，不宣称前阶段整包预先接纳。

没有实际整数几何或种子实例；固定数据的等式是否共同有解仍 OPEN。没有把有限首项条件称为实际有限两步机制、共同模板再生成或单初值无限代。其它 C 方向、共同模板幅度、真实 NS 时间、同数据 SOURCE_BRIDGE 预算和无限维跨代误差均未支付。旧失败证据没有修复或追认。

EXACT CONDITIONAL FULL-HIGH-ROW REDUCTION；SHARED IMAGINARY SIGN ELIMINATED WITHOUT EXTRA ROOTS；REALIZATION OPEN；NO-CANDIDATE；NOT CLAY。
