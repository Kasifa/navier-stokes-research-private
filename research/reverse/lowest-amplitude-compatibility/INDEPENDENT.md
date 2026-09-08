# 最低方向与共同所需幅度：独立消元及非恒等退化证明

2026-09-08，PRIVATE_CORE。独立有界推导完成，待非作者审查及根比较。

**结果：同一固定几何中，最低实方向式与共同最低所需正幅度的代数门可消去实际有符号高发送模方比 w。C0≠0 时得到首尾系数非零的三次多项式；C0=0 时，去掉失活 r=0 后得到不恒等为零的至多一次式。每个允许方向根唯一恢复 w，但仍须检查本文明列的非零、实际符号和所需 h 正性。这个局部 iff 不替代 PP 的面积平方门，也不证明任何合法整数实例或完整高行可行。**

本稿先全文读取当前合同，随后全文重读已接纳 TL 主稿及 PP 独立稿。未读本目录 PROOF.md 或本项其它新推导。本人是旧 TL 主稿作者，并已审过旧 PP 和后续若干稿件；本次独立性仅针对当前新消元，不能称为全课题盲审。全部手工符号，无科学程序、数组、数值求值、实际选参、扫描、Git、重置或外发。

## 1. 实际来源与固定规范

路径相对于 research/reverse/。

| 来源及本轮实际阅读范围 | SHA-256 |
|---|---|
| lowest-amplitude-compatibility/CONTRACT.md，先全文读取 | 50c69862e48753368b012e7df43e9af4ba3c4ceec0375b0e7c3d8fc06bb74b6a |
| two-elliptic-compatibility/PROOF.md，全文重读，使用 TL.1–35 的完整最低接口和几何系数 | 8961c72504eb7d60f35ee53050c99a2a25203ad539f85a9135ca16706dcc1cba |
| two-elliptic-compatibility/PROJECTED_PAIR_INDEPENDENT.md，全文重读，使用 PP.6、10–21 的实际投影及所需幅度 | 44c1f7fd6b616bd3bc1313c8b08607331f641f805329070ea4f93db5e72d8eef |

上述字节本轮已实测。源内部转引不自动列为实读，本稿不使用尚在审查的新几何相容结果。

固定一份合同几何，记 \(P_i=|p_i|^2\)、\(c_{ij}=p_i\cdot p_j\)、\(\Delta_{ij}=P_iP_j-c_{ij}^2>0\)。有 \(P_0<P_1<P_2\)，三频独立、全部非正交，且最低两条 beta 零。令
\[
E_{ik}=\frac{p_k-c_{ik}p_i/P_i}{\sqrt{\Delta_{ik}/P_i}},
\qquad N_{ik}=\widehat p_i\times E_{ik}.
\]
记 \(C=C_0=E_{01}\cdot E_{02}\)、\(S=S_0=N_{01}\cdot E_{02}\ne0\)。采用唯一实代表规范
\[
R=E_{01}+\frac{r-C}{S}N_{01},\qquad
R\cdot E_{01}=1,\quad R\cdot E_{02}=r\ne0,\qquad U_0=z_0R.
\tag{LAI.1}
\]
对任一原活跃实代表，只需将其非零第一投影吸收到 z0；这不改变同一物理种子。以下 \(h=|z_0|^2\) 总是相对于此规范的模方。

写高种子单位坐标
\[
U_i=a_i\{E_{i0}+(s_i+iy_i)N_{i0}\},\qquad a_i\ne0,\quad y_i\ne0.
\tag{LAI.2}
\]
令 \(L_{ik}=2(\Delta_{ik}/P_i)^{3/2}>0\)，并定义固定几何比与实际权重
\[
\omega=\frac{L_{02}\chi_{02}}{L_{01}\chi_{01}}\ne0,\qquad
w=\omega\frac{|a_2|^2}{|a_1|^2}.
\tag{LAI.3}
\]
故实际允许域是 \(w/\omega>0\)，等价于 \(\operatorname{sgn}w=\operatorname{sgn}(c_{01}c_{02})\)，不能只写 w≠0 后忘记这个号。

## 2. 最低实方向式与真实高接收实部

沿 TL.26–28 固定正几何系数
\[
A_1,A_2,L,M>0.
\]
这里 A_i 是 TL 的 \(\mathsf A_i\)，与种子单位复系数 a_i 区别；L、M 是 TL 的 \(\mathsf L,\mathsf M\)，不是 \(L_{ik}\)。最低实方向条件为
\[
\Psi(r,w)=wr^2(A_2Cr-M)+Lr-A_1C=0.
\tag{LAI.4}
\]
最低 Z 唯一实部必须同步恢复。令
\[
\gamma_i=\sqrt{P_0/P_i}\,\alpha_{0i}/\chi_{0i}\ne0.
\]
由 TL.17–18，实际高种子的单位实部为
\[
s_1=\frac{2r-C+wr^2}{S\gamma_1},\qquad
s_2=\frac{C-2/r-1/(wr^2)}{S\gamma_2}.
\tag{LAI.5}
\]
对高接收 \(i\)、另一高指标 \(j\)，记
\[
C_i=E_{i0}\cdot E_{ij},\qquad S_i=N_{i0}\cdot E_{ij}\ne0,\qquad
X_i=C_i+S_i s_i.
\tag{LAI.6}
\]
X_i 是实际接收比 \(t_i=(U_i\cdot E_{ij})/(U_i\cdot E_{i0})\) 的实部，不能在幅度消元后另行选取。

## 3. 两高常数的仿射与倒数形式

为避免 PP 同名字母混淆，本文记
\[
\mu_i=\kappa_{i0}/\chi_{i0}>2.
\]
PP.10 的高投影实常数 \(\tau_i\) 在本文记作 B_i。由
\[
\frac{R\cdot(p_i\times p_0)}{P_0(R\cdot p_i)}
=-\frac1{\sqrt{P_0}}\frac{R\cdot N_{0i}}{R\cdot E_{0i}},
\]
完整常数准确为
\[
B_i=(1-\mu_i)C_i-
\sqrt{P_i/P_0}\frac{\alpha_{i0}}{\chi_{i0}}S_i
\frac{R\cdot N_{0i}}{R\cdot E_{0i}}.
\tag{LAI.7}
\]
同一个 R 给
\[
\frac{R\cdot N_{01}}{R\cdot E_{01}}=\frac{r-C}{S},
\qquad
\frac{R\cdot N_{02}}{R\cdot E_{02}}=\frac{C-1/r}{S}.
\]
因此定义固定实几何系数
\[
d_i=\sqrt{P_i/P_0}\frac{\alpha_{i0}}{\chi_{i0}}\frac{S_i}{S},
\]
\[
b_{10}=(1-\mu_1)C_1+d_1C,\quad b_{11}=-d_1,\qquad
b_{20}=(1-\mu_2)C_2-d_2C,\quad b_{21}=d_2,
\tag{LAI.8}
\]
就有
\[
\boxed{B_1=b_{10}+b_{11}r,\qquad
B_2=b_{20}+b_{21}/r.}
\tag{LAI.9}
\]
这些系数与 w、发送模方和 z0 无关。后文将直接证明 \(\alpha_{i0}>0\)，故两个斜率 \(b_{11},b_{21}\) 非零；截距 b10、b20 在一般 C 域不预设非零。

## 4. PP 的 K 必须使用同一发送模方

先处理 \(\chi_{12}=0\)：PP.11–12 此时给 K1=0，而非实接收的投影虚部不可能为零。因此原目标中此几何分支失败，不能在这里定义 1/χ12。以下只在 \(\chi_{12}\ne0\) 域推导；其它所需 χ 非零已由最低 beta 零和严格较长接收支付。

定义固定非零几何量
\[
g_1=\left(\frac{\Delta_{12}}{\Delta_{10}}\right)^{3/2}
\frac{\chi_{12}}{\chi_{10}},\qquad
g_2=\left(\frac{\Delta_{12}}{\Delta_{20}}\right)^{3/2}
\frac{\chi_{21}}{\chi_{20}}.
\tag{LAI.10}
\]
PP 的未单位发送坐标 x_j 与本文单位系数满足
\[
|x_j|^2=|a_j|^2P_j/\Delta_{j0},\qquad
(R\cdot p_i)^2=(\Delta_{i0}/P_0)(R\cdot E_{0i})^2.
\]
将它们逐项代入 PP.11，得到真实
\[
\boxed{K_1=g_1|a_2|^2,\qquad K_2=g_2|a_1|^2/r^2.}
\tag{LAI.11}
\]
没有删掉实接收投影平方。于是
\[
\boxed{\frac{K_1}{K_2}=Gwr^2,\qquad
G=\frac{g_1}{g_2\omega}
=\frac{\chi_{12}\chi_{20}\chi_{01}}
{\chi_{10}\chi_{21}\chi_{02}}\ne0.}
\tag{LAI.12}
\]
全部 Δ 比在这一步准确抵消；G 的号不预设为正。

## 5. 所需共同 h 与局部消元域

若两个高投影最终通过，PP.13–16 强制
\[
X_i\ne0,\qquad
\lambda_i=\Lambda_i:=-\frac{\mu_i}{2X_i}\ne0,\qquad
|t_i|^2=B_i/\Lambda_i.
\]
因此 B_i=0 已不可能：它要求 |t_i|²=0，而 t_i 非实非零。也可由 PP 所需面积平方 \(B_i/\Lambda_i-X_i^2=-X_i^2\) 直接见到失败。不能把两个 B 同时为零当作“共同幅度任意”的有效分支。

为准确限定本轮较弱筛选，记两个代数所需值
\[
\widehat H_1=\frac{K_1B_2}{\Lambda_1\Lambda_2},\qquad
\widehat H_2=\frac{K_2B_1}{\Lambda_1\Lambda_2}.
\tag{LAI.13}
\]
它们在 PP 其余门通过后就是实际所需最低 h；在本轮外层代数筛选中，不预先把 \(B_i/\Lambda_i\) 当作已实现的实际模方。共同正值要求
\[
K_1B_2=K_2B_1,\qquad
h=\widehat H_1=\widehat H_2>0.
\tag{LAI.14}
\]
这是本稿保留的幅度子条件。它本身不证明 \(B_i/\Lambda_i-X_i^2>0\)，更不证明两面积平方相容。

以下恢复域明确要求 r、w、X_i、B_i 全部非零，w/ω>0。置
\[
F_1(r)=b_{10}+b_{11}r=B_1,\qquad
F_2(r)=b_{20}r+b_{21}=rB_2.
\tag{LAI.15}
\]
LAI.12、14 精确给
\[
\boxed{w=W(r):=\frac{F_1(r)}{G\,rF_2(r)}.}
\tag{LAI.16}
\]
这个 w 是真实发送模方比所需值；不是另一个按接收方向重新定义的权重。

把 LAI.16 代入最低实式并乘非零 \(GF_2\)，得到
\[
\boxed{\mathscr P(r)=
rF_1(r)(A_2Cr-M)+G F_2(r)(Lr-A_1C)=0.}
\tag{LAI.17}
\]
完整系数为
\[
\mathscr P(r)=A_2Cb_{11}r^3
+(A_2Cb_{10}-Mb_{11}+GLb_{20})r^2
+(-Mb_{10}+GLb_{21}-GA_1Cb_{20})r
-GA_1Cb_{21}.
\tag{LAI.18}
\]
此处从未除以最低实方向式自身的系数 \(r^2(A_2Cr-M)\)。所以 TL.31 中该系数和 \(A_1C-Lr\) 同时为零的分支没有被删除；它仍须通过同一个 W(r)、非零条件与 h 正性。

## 6. 精确反向恢复与符号

固定几何、\(\chi_{12}\ne0\) 后，下面两组条件等价：

- r、w 处于上述恢复域，最低实方向式 Ψ=0，且 LAI.14 的两个代数所需幅度相等并为正；
- r 是 LAI.17 的实根，且依次满足
\[
rF_1(r)F_2(r)\ne0,\quad W(r)/\omega>0,\quad
X_1(r,W)X_2(r,W)\ne0,\quad
g_2X_1(r,W)X_2(r,W)F_1(r)>0.
\tag{LAI.19}
\]
第一组的必要性由前述消元得到。反向取 w=W(r)，LAI.12 自动恢复共同幅度等式；因 GF2≠0，LAI.17 除回后恢复 Ψ=0。X_i 用 LAI.5–6 的唯一实部计算，绝不另选。

为核最后的正性并恢复尺度，设实际 \(|a_1|^2=\mathcal A>0\)，则
\[
|a_2|^2=\mathcal A\,W(r)/\omega>0,
\]
\[
\boxed{h=
\frac{4\mathcal A\,g_2X_1X_2F_1(r)}
{r^2\mu_1\mu_2}>0.}
\tag{LAI.20}
\]
这正是 LAI.13 的第二式。任意预先保留的发送相位可随同其模方表示；没有各边独立的发送向量。若在符号恢复中选取同一个模平方 \(\mathcal A>0\)，所有 K 与 h 同步缩放，不能分别修改两行。

可进一步以任意非零符号 y1 和
\[
\frac{y_2}{y_1}=-\frac{\sqrt{P_1/P_2}}{W(r)r^3}
\tag{LAI.21}
\]
恢复最低完整 C 的面积方向条件。右侧非零，最低两个面积都保持非零；TL.21 的独立法向保证最低 C 非零。这只恢复最低完整接口，不是恢复两个高投影的实际面积大小。

尤其，LAI.19–20 的 iff 精确限于最低实式与共同所需正幅度子门。未证明 PP 的两个实际平方
\[
B_i/\Lambda_i-X_i^2>0
\]
及其有符号相容关系；即使所需 h 为正，平方门仍可能失败。若后来这些 PP 条件通过，才可把此处所需 h 与同一实际两高投影完整绑定。

## 7. 逆向最低 beta 零上的严格正系数

为关闭多项式恒等退化，先直接重算高接收的 α。暂令接收平方长度 P、最低发送 Q，故 Q<P<4Q；最低反向 beta 零给
\[
8c^2=2P^2+PQ-4Q^2.
\]
沿 TL 所列通用 NC 几何式，写
\[
\Lambda=(P+Q)^2-4c^2,\quad
\Omega=(4P+Q)^2-16c^2.
\]
直接通分有
\[
h_++h_-=
\frac{2[Q(P+Q)(4P+Q)-4(6P+Q)c^2]}{\Lambda\Omega}.
\]
代入反向 beta 几何，
\[
\Lambda=\tfrac32Q(P+2Q),\qquad
\Omega=3(4P^2+2PQ+3Q^2).
\]
令 \(x=P/Q\in(1,4)\)、\(F(x)=4x^4+8x^3+19x^2+30x+20\)，得到
\[
\boxed{\alpha(P,Q,c)=
\frac{2F(x)}{3(x+2)(4x^2+2x+3)}>0.}
\tag{LAI.22}
\]
分母和 F 的每项均正。这里是手工展开 \(\alpha=2-(P-Q)(h_++h_-)\)，不是参数求值。因此 LAI.8 中 d_i 及 \(b_{11},b_{21}\) 确实非零。

还需一个更细的边系数：
\[
v_i=\frac{c_{0i}(\kappa_{i0}-\chi_{i0})}
{P_i\alpha_{i0}}.
\]
由 \(\mu_i>2\)、\(c_{0i}\chi_{i0}>0\) 和 α_i0>0，先有 v_i>0；其中 χ 的号直接由 \(H=(P-Q)(4P-Q)+4\Delta>0\) 及通用 χ 式核得。用同一反向 beta 等式及通用 χ、κ，再手工通分给
\[
v_i=
\frac{(2x^2+x-4)(x-1)(4x^3+4x^2+3x-2)}
{4xF(x)},\qquad x=P_i/P_0.
\]
其与 1 的差有正系数因式
\[
\boxed{1-v_i=
\frac{(4-x)(8x^5+20x^4+30x^3+33x^2+15x+2)}
{4xF(x)}>0.}
\tag{LAI.23}
\]
可复核的分子展开为
\[
4xF(x)-(2x^2+x-4)(x-1)(4x^3+4x^2+3x-2)
\]
\[
=(4-x)(8x^5+20x^4+30x^3+33x^2+15x+2).
\]
故严格有 \(0<v_i<1\)。没有在 x=4 的 Δ=0 退化边界取实例，也没有把该边界的极限等号算入本域。

## 8. C0≠0 与 C0=0：均无恒等零多项式

若采用较强联合目标允许的 C≠0，LAI.18 的首项系数 \(A_2Cb_{11}\ne0\)，常数项 \(-GA_1Cb_{21}\ne0\)。因此 \(\mathscr P\) 确为三次且不以 r=0 为根。固定几何至多三个实方向根；每根仍要过 LAI.19。这不是有限个初值或候选已经存在的断言。

较弱当前问题必须另保留 C=0。此时 LAI.17 化为
\[
\mathscr P(r)
=r\{(-Mb_{11}+GLb_{20})r+(-Mb_{10}+GLb_{21})\}.
\tag{LAI.24}
\]
r=0 已失活。下面证明花括号不能恒等为零。

C=0 给 \(c_{12}=c_{01}c_{02}/P_0\)。由实际单位投影和同一有向三频，
\[
C_1=\frac{c_{02}\sqrt{\Delta_{10}}}{P_0\sqrt{\Delta_{12}}},
\qquad
C_2=\frac{c_{01}\sqrt{\Delta_{20}}}{P_0\sqrt{\Delta_{12}}},
\]
\[
\frac{S_1}{S}=-\sqrt{\frac{P_1}{P_0}}
\sqrt{\frac{\Delta_{20}}{\Delta_{12}}},\qquad
\frac{S_2}{S}=\sqrt{\frac{P_2}{P_0}}
\sqrt{\frac{\Delta_{10}}{\Delta_{12}}}.
\]
因而四个 b 系数均非零，并直接得到
\[
\boxed{\frac{b_{10}b_{20}}{b_{11}b_{21}}
=\prod_{i=1}^2
\frac{c_{0i}(\kappa_{i0}-\chi_{i0})}{P_i\alpha_{i0}}
=v_1v_2\in(0,1).}
\tag{LAI.25}
\]
若 LAI.24 的两个系数同时为零，则
\[
Mb_{11}=GLb_{20},\qquad Mb_{10}=GLb_{21},
\]
相消推出 \(b_{10}b_{20}=b_{11}b_{21}\)，与 LAI.25 矛盾。这不需要预设 G 为正。

所以 C=0 时，r≠0 上仅剩不恒零的至多一次门：一次系数非零时至多一根，仍须非零并过恢复域；一次系数为零时常数必非零，故无根。若常数为零而一次系数非零，唯一形式根是失活 r=0，亦不通过。该结论没有删除较弱问题的正交投影子域。

最低实式在 C=0 时还直接给 \(w=L/(Mr)\)，故必要 \(wr>0\)。LAI.16–19 仍保留它和实际 w 允许号；不能因更强高行目标另有 C≠0 门而在此偷换较弱问题的量词。

## 9. 零支与最终范围

本稿全部除法由以下条件支付：P_i、Δ_ij 和相应单位基长度正；S、S_i、r 非零；最低 χ、γ 和 ω 非零；严格较长 χ_i0、χ_21 非零；χ_12=0 已先排除；进入恢复域后 G、F1、F2、w、X_i、Λ_i、B_i 非零。没有除一般截距 b10、b20、C、最低消元的原系数 D，或任何未知号残差。LAI.25 的四 b 非零只在 C=0 子域另证后使用。

若 F1=0 或 F2=0，对应 B1 或 B2 为零，不能用共同幅度等式的退化零和作为有效恢复；若 W/ω≤0，不能实现真实非零高发送模方；若 X_i=0，非实投影虚部不通过；若 LAI.20 不正，则所需共同最低模方无效。其余平方门还可能另外失败，本稿没有把这些失败吞入多项式。

已闭合的是：真实 B 的仿射/倒数形式、真实 K 比例、至多三次消元门、明列符号与正性域上的局部反向恢复，以及两个 C0 域的非恒等退化证明。固定几何下 r 的有限候选根不证明该几何可由合法整数三频实现，也不证明存在过完所有门的同一组三种子。

两个高投影的实际面积平方及相容、完整高行残差、其它两个 C 方向、共同模板幅度、真实 NS 时间、同数据无限维与跨代余项均未支付。没有实际频率、初值、幅度或时间选择；没有有限两步机制、单初值无限尺度、有限总时间、奇性或全局正则性结论。旧失败证据没有修复或追认。

EXACT LOCAL AMPLITUDE ELIMINATION；NO IDENTICALLY ZERO DIRECTION POLYNOMIAL IN THE STATED DOMAIN；REALIZATION OPEN；NO-CANDIDATE；NOT CLAY。
