# 完整两高行独立稿：非作者逐式审查

2026-09-08，PRIVATE_CORE。结论：**PASS，限于合同指定的条件充要代数接口。** 对所绑定的 INDEPENDENT.md，FH.1–21 的实际换基、四实条件、共同符号消去和条件恢复均通过手核；没有须作者修正的事项。是否存在使全部条件成立的合法整数几何和固定数据仍 OPEN。

被审最终稿 SHA-256：
42581306cb064f24514a4b6a690e2e91e098ce2d125c454d92562b1956ec1446。

本人不是本稿作者。本人曾撰写前阶段最低行主稿、最长面积独立稿，并对其它前阶段补充及最终范围作非作者审查；也曾撰写更早的 NC 独立稿。这是被审文本的非作者审查，不是全课题盲审或另一路全新推导。此次未读本目录 PROOF.md、其审查或其它本项新科学稿；不以本人以前的面积推导替代对本稿四实式的核验。全部核验为手工符号与文本、哈希元数据操作，没有程序求值、数组、数值选择、扫描、Git、重置或外发。

## 1. 实际读源与字节

以下路径相对于 research/reverse/。本轮先读取合同及被审稿全文，随后为逐式核验实际重读所列来源；文件内转引不自动视为实读。

| 来源及本轮实际阅读范围 | SHA-256 |
|---|---|
| full-high-row-reduction/CONTRACT.md，全文 | 8f1dd745dc12409f3e49b7b56073b3fb38fca4a26d23774f0df4ea12292ecc6e |
| full-high-row-reduction/INDEPENDENT.md，全文 | 42581306cb064f24514a4b6a690e2e91e098ce2d125c454d92562b1956ec1446 |
| two-elliptic-compatibility/PROJECTED_PAIR_INDEPENDENT.md，全文 | 44c1f7fd6b616bd3bc1313c8b08607331f641f805329070ea4f93db5e72d8eef |
| two-elliptic-compatibility/HIGHER_ROW_INDEPENDENT.md，第 185–320 行，HI.9–20 及相关上下文 | ab7df7bbf6d698c2ee6bb223c06fe478cc34ecc37db1806bc8a774a9c037d9e0 |
| two-elliptic-compatibility/INDEPENDENT.md，第 107–338 行，TEI.9–24 及范围说明 | 9a39799e39b9ec40e4ae61e86f3b0dda0dabc0885dcbea17febd91b868524da9 |
| net-mixed-cancellation/INDEPENDENT.md，第 1–119 行，NC.1–10 | 25111397d32eef2751a91b1ad1ab6a446794742874b97bf6b0b73b3964d11a58 |
| three-edge-compatibility/MAX_RECEIVER_RATIO.md，全文 | ff52531d6e1b5563c99504aba8e6b6e4e5afce77b76e7e286e74d397c3d610c5 |

本轮实测各 SHA 与被审稿所列来源一致。前阶段综合冻结的状态由其独立记录管理；本审查不改写当前合同及被审稿形成时的待审历史，也不凭历史状态标题否定已经逐式列明并复核的直接条件。

## 2. 同一数据与投影门：FH.1–7 通过

固定几何、实最低代表 R 和两个复系数 x_i 后，最低 TEI.13–14 确定的实部不能随高行改变。最低实三次式是同一 T 的前提，完整最低方向另要求
\[
P_1\theta_1+\varrho P_2T^3\theta_2=0.
\]
因此 FH.2 的有符号 ζ 不能由两个独立面积平方替代。

对单位基，实际有
\[
n_{0i}=-\sqrt{P_i}\ell_{i0}N_{i0},\qquad
U_i\cdot E_{i0}=x_i\ell_{i0},\qquad
t_i=C_i-\sqrt{P_i}S_i(\xi_i+i\theta_i).
\]
这核定 FH.3 的负号、有限非实比值及 d_i。三频有向积给出的 S_1、S_2 符号相反，故
\[
\frac{d_1}{d_2}
=-\frac{P_1}{P_2}\sqrt{\frac{\Delta_{20}}{\Delta_{10}}},
\quad
\frac{d_1\zeta}{d_2}
=\varrho T^3\sqrt{\frac{\Delta_{20}}{\Delta_{10}}}=m.
\]
没有将两高种子的面积独立化。

从 HI.14–16 的真实点积模方代入
\[
|U_j\cdot p_i|^2
=\frac{|x_j|^2\Delta_{j0}\Delta_{ij}}{P_j^2}|t_j|^2
\]
后，所得 λ_i 正是 FH.5 的 \((K_i/h)|t_j|^2\)，包括全部长度幂和 \((R\cdot p_i)^2\)。K_i 的符号不是任意通道幅度。

对第一投影 \(\lambda_i t_i^2+b_it_i+\tau_i=0\)，写 \(t_i=a_i+iY_i\)、\(Y_i\ne0\)。虚部强制 \(2\lambda_i a_i+b_i=0\)，实部随后给 \(Y_i^2=M_i\)。于是 FH.6 的 \(L_i=-b_i/(2a_i)\)、正平方、\(M_1=m^2M_2\)、共同正 h 均必要。其恢复 FH.7 同时支付两行真实 λ_i=L_i 和有符号最低关系，亦充分。a_i=0 或 K_i=0 在任何此类除法之前已由非零虚部排除。

## 3. 非单位发送换基与完整相干：FH.8–12 通过

这里发送在 \(p_j^\perp\) 中的基必须取
\[
f_{ij}=\ell_{ji}E_{ji},\qquad
n_{ij}=-\sqrt{P_j}\ell_{ji}N_{ji}.
\]
令 \(A_j=U_j\cdot E_{j0}=x_j\ell_{j0}\)。由实旋转而非自由重选坐标，
\[
U_j\cdot E_{ji}=A_jt_j,\qquad
U_j\cdot N_{ji}=A_j(C_jt_j-1)/S_j.
\]
据此解出 X_ij 与 w_ij，恰为
\[
X_{ij}=x_j\sqrt{\Delta_{j0}/\Delta_{ij}}\,t_j,\qquad
w_{ij}=\frac{t_j^{-1}-C_j}{\sqrt{P_j}S_j}.
\]
因此 FH.9 的实部、虚部及模方同时成立，尤其
\[
\theta_{ij}^{s}=\theta_j/N_j,\qquad
|X_{ij}|^2=|x_j|^2(\Delta_{j0}/\Delta_{ij})N_j.
\]
相乘后 N_j 消去，得到 FH.10 的同种子有向面积恒等式。只保持模方、另行指定相干是不允许的；本稿没有这样做。

FH.4 与 NC.6–8 的系数逐项相同。手工通分 \(h^+-h^-\) 的分子，得到
\[
4c\bigl(4P^2-PQ-2Q^2+8c^2\bigr).
\]
配合
\[
P\Omega-2(2P+Q)H
=Q(4P^2-PQ-2Q^2+8c^2)
\]
确有 \(\beta/\chi=2-\kappa/\chi\)。这一恒等式本身不要求 P>Q；但使用比值前必须先支付 χ≠0，稿中按 FH.6 做到了。只有最长的 B_2 可从 MAX 取 >2，没有给 B_1 添加不合法正性。

若发送 Y=X(ξ+iθ)，则 \(\operatorname{Im}(X\overline Y)=-|X|^2\theta\)。所以 FH.12 必须是 \(\alpha\xi-i\beta\theta\)，其负 i 号正确。

## 4. 第二点积及四实式：FH.13–19 通过

从 NC 的非单位表达式令 \(U=A E+B N\)，即 \(u=A/\ell\)、\(v=B/(\sqrt P\ell)\)，可直接得到完整单位表示
\[
Z=ik\left[A^2E+
\left(\frac{\kappa}{\chi}AB+
\frac{\sqrt P}{\chi}(\alpha\xi-i\beta\theta)A^2\right)N\right],
\quad
k=\frac{2\Delta^3}{P^2Q}\frac{|X|^2\chi}{\ell}.
\]
因此 FH.13 的 \(k_{i0}\) 是真实规范，未缺失 \(\ell_{i0}\) 或 \(\sqrt{P_i}\)；\(X_{i0}=P_0(U_0\cdot p_i)/\Delta_{i0}\) 也正确。

在线性发送基 E_i0、N_i0 中，其点积 E_i0 给常数 1；另一发送项满足
\[
\frac{U_i\cdot N_{ij}}{A_i}
=\frac{C_it_i-1}{S_i},\quad
E_{ij}\cdot E_{i0}=C_i,\quad N_{ij}\cdot E_{i0}=-S_i.
\]
于是它贡献
\[
L_i\left[C_it_i^2
-B_it_i(C_it_i-1)-S_i\gamma_{ij}t_i^2\right],
\]
整理即 FH.13。两点积方向独立是因为 S_i≠0；第一投影为零后，第二点积为零确实等价于完整高行向量零，不是检查了同一个分量两次。

将第二点积除以非零 \(L_it_i^2\) 得 FH.14。令其“左边减右边”为 F_i，则逐项有
\[
\operatorname{Re}F_i
=(B_i-1)C_i-\frac{B_ia_i}{N_i}
-\frac{a_i^2-M_i}{L_iN_i^2}
-D_i\frac{\alpha_{ij}}{\chi_{ij}}
\left(\frac{a_j}{N_j}-C_j\right),
\]
\[
\frac{\operatorname{Im}F_i}{\varepsilon y_i}
=\frac{B_i}{N_i}+\frac{2a_i}{L_iN_i^2}
+D_i(B_i-2)\frac{q_i}{N_j}.
\]
这里
\[
\frac{S_i}{S_j}\sqrt{\frac{P_i}{P_j}}=-D_i,\qquad
q_i=y_j/y_i
\]
由同一有向三频得出。这两式分别就是 FH.16、17；特别发送虚部贡献的号为正 \(D_i(B_i-2)q_i/N_j\)。

最后，原第二点积的归一化值严格等于 \(-L_it_i^2F_i\)，故 FH.18 的外部负号也正确。F_i 的两个实系数不含 ε；L_i、t_i、y_i 非零，所以零式双向等价于两个实系数分别为零。这里没有对复等式取模平方而丢失号，也没有各高行另选 ε。共同符号的两种恢复要么同时通过，要么同时失败；固定 x_i 的复相位完全保留。

## 5. 条件 iff、非零性和退化域：FH.20–21 通过

NC.3 的规范确为 \(M_{0,i}=\frac16\sum Z_{ij}\)、\(W_{0,i}=\frac13\sum C_{ij}\)。每一接收先求完整同频两项和，三个不同接收是不同 Fourier 分量，负模共轭。因此完整 M0=0 正是三条完整行分别为零。

在同一固定几何、R、x_i，最低唯一实部与同一实三次式为前提时：

- 必要性依次给最低有符号关系、FH.6 的共享正幅度与非零面积平方，以及 FH.16–17 四个实条件。
- 充分性由 FH.7 恢复同一 U1、U2 和同一个正 h。最低两条件按 TEI.13–18 成立；每一高行的两独立点积按本稿等式同时为零。
- 最低 C 非零另有实质证据：去掉共同最低相位平方后，TEI.12 的保留面积部分为 \(k_1\nu_1A_1^2N_1+k_2\nu_2A_2^2N_2\)。两实法向独立，两个系数各非零，故完整和不能为零。恢复非零相位平方仍不变；没有把零输出算作方向成立。

因此 FH.20 的 iff 确实覆盖完整总 M0 与最低非零 C 原方向，而不自动覆盖其它 C 行或共同模板幅度。

零分支的次序合法。K_i=0 与 χ_ij=0 等价；当前严格排序下仅中间 χ_12 可能由 H_12=0 消失，最长 χ_21 不消失。若 a_i=0、K_i=0、M_i≤0、平方不匹配或两所需 h 不同/不正，已经不能通过第一投影，不能借后续形式除法恢复。

在 FH.6 域内，所有 P、Δ、ℓ 正，χ_i0、χ_ij、S_i、L_i、N_i、t_i、m、y_i 以及点积规范均非零。未除以 α、β、C_i、ξ_i、实残差或虚残差；这些零值保留。T=0、投影为零、S_i=0 等是合同外域，不能沿用当前判据。

若 β_ij=0，B_i=2 后第二虚条件化为
\[
\mathcal I_i
=\frac{2(N_i-2a_i^2/b_i)}{N_i^2}>0,
\]
因为 b_i>2 且 N_i>a_i²。这是明确的剩余分量失败，不能删去发送虚相干后宣布通过。α_ij=0 则仅使相应实项消失。

最长行有 B_2>2、b_2>2，故
\[
\frac{B_2N_2-4a_2^2/b_2}{N_2^2}>0.
\]
其余虚项为 \(D_2(B_2-2)m/N_1\)，完整虚式为零强制 m<0。由 FH.2、6，这等价于 varrho T<0，并要求两高种子有向面积同号。这里是从被审稿的新实式直接验证，未拿本人面积稿替换。

最低三次在 T=−ε_0s、varrho=ε_0r_0 的负号支上，准确成为
\[
-\varepsilon_0 C_0
=\frac{r_0\mathcal B_0s^2+\mathcal A_0s}
{r_0\Gamma_2s^3+\Gamma_1}>0.
\]
因此 varrho C_0<0 必要，C_0=0 的联合分支失败。这个推导未除以最低消元的 D 或 N，未删除 D=N=0、重根或其它允许负号根；它也没有声称所有最低实根都失败。

## 6. 接纳范围

所绑定文本可接纳为：真实共享种子的非单位邻边换基、完整两高行四实条件、共同虚符号的无损消去，以及在明确最低前提下的完整 M0=0 / 最低 C 非零原方向条件 iff。

这不接纳任何实例，也不证明此显式系统必有解或必无解。整数几何存在、其它两 C 的方向、三行模板幅度相容、实际 NS 时间、同数据 SOURCE_BRIDGE 预算、无限维与跨代误差仍未支付。前阶段的条件最低存在不能替代本稿四式；本稿四式也不能替代真实有限两步机制或单初值无限代。没有公共发布或旧失败证据修复。

本审查完成后全文自读，并重新核对被审稿绑定；只有根实际比较及其冻结程序可形成本阶段综合接纳。本文件停止修改后另报实际 SHA-256。

PASS AT THE STATED CONDITIONAL SCOPE；REALIZATION OPEN；NO-CANDIDATE；NOT CLAY。
