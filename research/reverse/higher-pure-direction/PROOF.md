# 两个较高总纯供给行的精确复方向式

2026-09-08，PRIVATE_CORE。根先按合同从完整 NC.9 手推单位基式及行列式，再利用明确 FR 等式化简；未读本项独立新稿，未收到对方具体新推导。两份新稿与审查均未完成，不先接纳本稿为候选证据。

本轮实际重读 net-mixed-cancellation/INDEPENDENT.md 第 1–120 行（完整 NC.1–10），SHA 25111397d32eef2751a91b1ad1ab6a446794742874b97bf6b0b73b3964d11a58；full-high-row-reduction/PROOF.md 第 1–115 行（FR.1–10 及紧接虚部开头），SHA 3d02da817e164bbf8f75bdddfea74a4e0d2b14c12d890952aeeb727866cc3c6b。另实际读 two-elliptic-compatibility/PROOF.md 第 230–315 行仅确认最低纯方向与非零界限，本项新系数不用它作输入。合同已全文读。不重推 NC 背后的所有原始树或新增黏性时间核；使用已明确的完整空间映射。

## 1. 每条有序边的完整单位基纯系数

接收 p、发送 q，记 P=|p|²、Q=|q|²、c=p·q、Δ=PQ−c²、d=P−Q、Σ=P+Q、Λ=(P+Q)²−4c²。当前合同中 P,Q>0、Δ>0、c,d≠0，Λ>0。用同一有向单位基
\[
E_{pq}=\sqrt{P/\Delta}(q-cp/P),\qquad N_{pq}=(p\times q)/\sqrt\Delta,
\]
\[
U=a(E_{pq}+zN_{pq}),\qquad
V=b(E_{qp}+\zeta N_{qp}),\quad \zeta=s+iy.
\tag{HC.1}
\]
这里 a,b 非零，z 为接收复比，s,y 是同一发送复比的实虚部。反向 N_qp=−N_pq，不能去掉这个号。NC 非单位坐标因此为
\[
u=a\sqrt{P/\Delta},\quad v=az/\sqrt\Delta,
\quad x=b\sqrt{Q/\Delta},\quad y_{\rm NC}=-b\zeta/\sqrt\Delta.
\]
故 R_NC=−|b|²√Q s/Δ、I_NC=|b|²√Q y/Δ。把这些实际相干代入完整 NC.9，得到
\[
\frac{C_{pq}}{iL_{pq}a^2|b|^2}
=K_{pq}E_{pq}
+(\kappa_{pq}z+A_{pq}^{C}s+iB_{pq}^{C}y)N_{pq},
\tag{HC.2}
\]
其中
\[
L_{pq}=2(\Delta/P)^{3/2},\qquad
K_{pq}=\frac{2cd^2}{Q\Lambda},\qquad
\kappa_{pq}=\frac{4cdP}{Q\Lambda},
\]
\[
A_{pq}^{C}=-\frac{2d\sqrt{PQ}(P+Q)}{Q\Lambda},\qquad
B_{pq}^{C}=-\frac{4cd\sqrt{PQ}}{Q\Lambda}.
\tag{HC.3}
\]
手推时平面 E 系数为 4i a²|b|² Δ^{3/2}cd²/(P^{3/2}QΛ)，正好是 HC.2 的 L K。法向里的完整三项分别是发送实相干、发送虚相干、接收反馈，均留在 HC.2；没有把它们取模或按单边平均。

定义无歧义的纯方向几何常数
\[
\ell_{pq}=\frac{P+Q}{2P}>0,\qquad
a_{pq}^{D}=-\sqrt{Q/P}\frac{P+Q}{2c},\qquad
b_{pq}^{D}=-\sqrt{Q/P}.
\tag{HC.4}
\]
它们与种子 a,b 或前稿 b_i 不同。因 κ非零，有 κ−K=κℓ、A^C=κ a^D、B^C=κ b^D。

在接收复平面上记 [X,Y]_p=(p/√P)·(X×Y)，是复双线性行列式。直接由 [E,N]=1 得
\[
\boxed{[U,C_{pq}]_p
=iL_{pq}a^3|b|^2\kappa_{pq}
(\ell_{pq}z+a_{pq}^{D}s+ib_{pq}^{D}y).}
\tag{HC.5}
\]
接收幂是 a³，不是 a²或|a|²a；发送仍是同一个 |b|²。相位因此没有在方向检验中丢掉。非零 U 与任意 C 的行列式为零当且仅当 C 属于复直线 C U；这在 U·U=0 时仍成立，没有把双线性自点积作分母。

## 2. 同一种子在两个发送边上的实际恢复

用 FR.1–7 的直接条件，固定高接收 i、另一个高发送 j。Ui=ai(E_i0+zi N_i0)，zi=si+i yi，yi≠0；令 ti=Ci+Si zi=Xi+iYi，Si≠0、Yi=Si yi≠0、Mi=|ti|²。最低 U0=z0R，xi=R·E0i≠0，v0i=(R·N0i)/xi 为实数，h=|z0|²>0。

同一个 Ui 在 ij 边的投影为 ai ti，接收比为
\[
z_{ij}=\frac{C_it_i-1}{S_it_i}.
\tag{HC.6}
\]
同一个 Uj 在 ji 边的发送投影为 aj tj，实虚比是
\[
s_{ji}=\frac{C_j-X_j/M_j}{S_j},\qquad y_{ji}=\frac{y_j}{M_j}.
\tag{HC.7}
\]
不是 Yj/Mj，也不是可另选的发送相干。定义实际正权重 η_i0=L_i0 h xi²、η_ij=L_ij|aj|²Mj。由 HC.5 在同一个 pi 接收平面相加，准确有
\[
\frac{[U_i,C_{i0}+C_{ij}]_i}{ia_i^3\eta_{i0}\kappa_{i0}}
=\ell_{i0}z_i+a_{i0}^{D}v_{0i}
+\frac{\eta_{ij}\kappa_{ij}}{\eta_{i0}\kappa_{i0}}t_i^3
(\ell_{ij}z_{ij}+a_{ij}^{D}s_{ji}+ib_{ij}^{D}y_{ji}).
\tag{HC.8}
\]
两条边的行列式使用相同的接收法向，换基为行列式一的实旋转，故两项可直接相加。该式已经是总行的原方向充要检测，不要求两条单边分别沿原方向。

## 3. 在实际指定高投影域中的有限化简

FR 的直接两高指定投影式给 b_i=−μ_i/(2Xi)、μ_i=κ_i0/χ_i0>2、Xi≠0、ρ_i=κ_ij/χ_ij。其实际定义又给
\[
\frac{\eta_{ij}\kappa_{ij}}{\eta_{i0}\kappa_{i0}}
=\frac{b_i\rho_i}{\mu_i}=-\frac{\rho_i}{2X_i}.
\tag{HC.9}
\]
这只是同数据代换，不重新选择两行幅度。现在 HC.8 乘非零 2XiSi，方向零式成为明确的一条复式
\[
\boxed{\mathcal K_i=
2X_i\{\ell_{i0}(t_i-C_i)+S_i a_{i0}^{D}v_{0i}\}
-\rho_i\{\ell_{ij}t_i^2(C_it_i-1)
+S_it_i^3(a_{ij}^{D}s_{ji}+ib_{ij}^{D}y_{ji})\}=0.}
\tag{HC.10}
\]
完整恒等式是 K_i=2XiSi[Ui,C_i0+C_ij]/(i ai³η_i0κ_i0)。所有乘数都非零，可带号，只用于等式。K_i=0 单独不保证总行非零。

为保留有限度数而不无收益地展开 r 的高次式，记实际实量
\[
\theta_i=\ell_{ij}C_i+S_i a_{ij}^{D}s_{ji},\qquad
\epsilon_i=S_i b_{ij}^{D}y_{ji}.
\]
因为 ti=Xi+iYi、Mi=Xi²+Yi²，恒有 ti²=2Xi ti−Mi、ti³=(4Xi²−Mi)ti−2XiMi。于是
\[
\mathcal K_i=\mathcal A_i t_i+\mathcal B_i,
\tag{HC.11}
\]
\[
\mathcal A_i=2X_i\ell_{i0}
-\rho_i\{(\theta_i+i\epsilon_i)(4X_i^2-M_i)-2X_i\ell_{ij}\},
\]
\[
\mathcal B_i=2X_i(S_i a_{i0}^{D}v_{0i}-\ell_{i0}C_i)
+\rho_i\{2X_iM_i(\theta_i+i\epsilon_i)-\ell_{ij}M_i\}.
\tag{HC.12}
\]
这不是一元自由系数求根：Xi、Mi、θi、εi 和 ti 始终是原同一种子的实际量。写 A_i=A_R+iA_I、B_i=B_R+iB_I 后，完整两个实条件为
\[
A_RX_i-A_IY_i+B_R=0,\qquad
A_RY_i+A_IX_i+B_I=0.
\tag{HC.13}
\]
无需除 A_i、B_i、θi 或其它可能为零的化简系数；全部零支保留。发送面积仍通过 εi 依赖真实 yj/Mj，没有被降低次数删掉。

## 4. 两高总方向与未支付条件

对 i=1、2 同时应用 HC.10 或 HC.13，得到两个较高总纯行沿各自原复种子方向的精确四实检验。两行必须使用同一组数据及前置恢复式。若再条件性满足已明确的全部 M0 零及最低 C 非零原方向输入，则这四式只补上其它两条 C 的方向；不据此宣布完整模板。

一旦方向成立，总行仍可能为零。若只需准确检测这一点，可以用恒正 Hermitian 分母定义 γ_i=(C_i0+C_ij)·conj(Ui)/|Ui|²，方向零式成立后，总行=γ_i Ui，非零当且仅当 γ_i≠0。这里不是自动断言 γ_i非零，更没有检查不同 i 的 |γ_i|是否一致或其与共同模板相位的关系。分母 |Ui|²严格正，不使用可能为零的 Ui·Ui。

没有证明任何合法整数几何和同一种子满足这些式子或其全域不可能性。当前已锁实际投影与非零χ域以外的分支未被排除。无科学程序、数组、实际选参、方向求值、扫描或新黏性时间核；没有实际候选、有限原解两步、统一迭代、单初值无限尺度、跨代无限维余项、有限总时间或奇性。旧失败不变。EXACT CONDITIONAL HIGHER PURE-DIRECTION EQUATIONS；NO-CANDIDATE；NOT CLAY。
