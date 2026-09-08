# 同一方向的五余式联合判据与符号恢复

2026-09-08，PRIVATE_CORE。独立有界手工推导，待非作者审查与根比较。

**先锁合同。** 本次已先全文读取本目录 CONTRACT.md。固定同一 C0≠0、最低线性、两高面积非零的合法三频几何，只使用下列三份停改文本明列的直接等式，把最低方向、面积、两个剩余虚部和两个剩余实部放在同一个实方向 r 上。最高结论是该固定域内完整 M0=0 且最低 C 非零原方向的条件恢复；不假定前阶段整包将在未来接纳，不研究其它两行 C 原方向或共同模板。

**所得结果。** 五条至多二次余式的同根条件等价于一个实际五行三列系数矩阵对 (1,r,r²) 的零式，再与同一个非零方向三次及严格号域相交。本文给出全部系数秩退化的判据，并用一个三维实线性算子的最大不变核把共同代数根精确识别为该核上限制算子的实特征值。核非零或低秩本身不保证有合法实根。所有实际几何的秩、共同根及号域能否同时达到均未判定。

本人是剩余实部独立稿及此前部分最低、投影、完整高行和几何独立稿作者，并曾非作者审查面积主稿与剩余虚部主稿；这不是全课题盲推导。本次按明确许可全文读取 ASI、RI 主稿和本人 RRI，未读取本目录 PROOF.md 或本项另一推导，也未收到另一推导的具体结构。没有重新展开原始 Leray 树；使用三份来源明列的同数据恢复等式和完整行接口。

全部矩阵和秩只作为纸面有限符号数学。无科学程序、矩阵数组执行、数值求值、实际频率或种子选取、扫描、Git、重置、外发或发布。

## 1. 实际来源与同一固定数据

路径相对于 research/reverse/。本次实际全文读取并实测以下四份来源；其内部转引不自动计为本次实读。

| 来源 | SHA-256 |
|---|---|
| joint-direction-compatibility/CONTRACT.md，先全文读取 | 5b8dc82300556766260a13c1f9124d7a02989ec14e242cf5aad8b49fc5d16ad3 |
| area-square-compatibility/INDEPENDENT.md，全文，简称 ASI | 489fd488a5dbc8dcdc1336904a16d8dcbe3817077ec74137ead1706f545d4acc |
| remaining-imaginary-compatibility/PROOF.md，全文，简称 RI | 638ef8812fad8bf3337ecf1c6bd73a4fb73e34843eaa94a2b6a1cb8daff3fdef |
| remaining-real-compatibility/INDEPENDENT.md，全文，本人已停改稿，简称 RRI | df69ea23d67efa7b970010327833480435867cad305b665e077930e7ae71725f |

固定同一独立整数三频，平方长度 P0<P1<P2，全部非正交、最低双 β 零及实际所需 χ 非零。沿用三份来源同一单位有向基；C=C0≠0、S=S0≠0，两个高基的 Si≠0。所需 γ_i^0≠0、G≠0、ω≠0、g2≠0，μ_i>2、ρ2>2 均是该固定域的实际几何条件。ρ1、g2、G、ω 不擅自正化。所有几何系数在判断 r 前固定。

最低实代表及高种子规范是
\[
R=E_{01}+\frac{r-C}{S}N_{01},\qquad
U_0=z_0R,\quad |z_0|^2=h>0,
\]
\[
U_i=a_i\{E_{i0}+(s_i+iy_i)N_{i0}\},\qquad
a_i\ne0,\quad y_i\in\mathbb R\setminus\{0\}.
\tag{JDI.1}
\]
该规范固定 R·E01=1、R·E02=r；两个投影均须非零。负模为同一组三种子的共轭。本文不扩展到最低投影为零的其它坐标分支。

重列实际仿射量和最低唯一实部：
\[
F_1=b_{10}+b_{11}r,\quad F_2=b_{20}r+b_{21},\quad
B_1=F_1,\quad B_2=F_2/r,
\]
\[
w=\frac{F_1}{GrF_2},\quad
s_1=\frac{2r-C+wr^2}{S\gamma_1^0},\qquad
s_2=\frac{C-2/r-1/(wr^2)}{S\gamma_2^0}.
\tag{JDI.2}
\]
这里 μ_i=κ_i0/χ_i0，且
\[
\zeta_i=\sqrt{P_i/P_0}\frac{\alpha_{i0}}{\chi_{i0}}\frac{S_i}{S},
\]
\[
b_{10}=(1-\mu_1)C_1+\zeta_1C,\quad b_{11}=-\zeta_1,
\quad b_{20}=(1-\mu_2)C_2-\zeta_2C,\quad b_{21}=\zeta_2.
\]
同一来源给
\[
G=\frac{\chi_{12}\chi_{20}\chi_{01}}
{\chi_{10}\chi_{21}\chi_{02}},\quad
\omega=\frac{L_{02}\chi_{02}}{L_{01}\chi_{01}},\quad
L_{ik}=2(\Delta_{ik}/P_i)^{3/2},
\]
\[
g_2=(\Delta_{12}/\Delta_{20})^{3/2}\chi_{21}/\chi_{20},
\quad \frac w\omega=\frac{|a_2|^2}{|a_1|^2}.
\]
这些系数不是可独立调节的形式通道参数。

最低方向等式为同一三次
\[
P(r)=rF_1(A_2Cr-M)+GF_2(Lr-A_1C)
=p_3r^3+p_2r^2+p_1r+p_0,\quad A_1,A_2,L,M>0,
\]
\[
\begin{split}
p_3&=A_2Cb_{11},\\
p_2&=A_2Cb_{10}-Mb_{11}+GLb_{20},\\
p_1&=-Mb_{10}+GLb_{21}-GA_1Cb_{20},\\
p_0&=-GA_1Cb_{21}.
\end{split}
\tag{JDI.3}
\]
非零首项不是新增假定的未来结论。ASI 明列
\[
\alpha_{i0}=
\frac{2(4x^4+8x^3+19x^2+30x+20)}
{3(x+2)(4x^2+2x+3)}>0,\qquad x=P_i/P_0>1.
\]
分子分母每项正，故 b11、b21 非零，在当前 C≠0 域有 p3p0≠0。因而 P 恰为三次，r=0 不是其根。C=0 不属于本文余式除法的定义域。

## 2. 五个实际分子与原严格域

令 v_i=Si/(Sγ_i^0)，沿用 ASI 的分子规范：
\[
Q_1=[C_1+v_1(2r-C)]GF_2+v_1rF_1,\qquad
Q_2=(C_2+v_2C)rF_1-v_2(2F_1+GF_2),
\]
\[
X_1=Q_1/(GF_2),\quad X_2=Q_2/(rF_1),\quad Z=F_1F_2.
\tag{JDI.4}
\]
此处 Z 仅为仿射乘积，不是 Fourier 来源向量。两个 Q_i 次数至多二。

实际面积因子和多项式为
\[
E_1=-Q_1(\mu_1Q_1+2GZ),\qquad
E_2=-Q_2(\mu_2Q_2+2Z),
\]
\[
\mathcal A=P_2\mu_1S_1^2r^2E_2-P_1\mu_2S_2^2E_1.
\tag{JDI.5}
\]
其次数至多六。本文采用的全部待检严格域记为
\[
\boxed{\mathscr D(r):\quad
rF_1F_2\ne0,\qquad
\frac{F_1}{GrF_2\omega}>0,\qquad
E_1(r)>0,\qquad
g_2Q_2(r)\,rF_1(r)<0.}
\tag{JDI.6}
\]
固定几何的非零域另按第 1 节保留。JDI.6 尚未断言面积等式成立；须与同一 r 的 \(\mathcal A=0\) 合用。此时 E2>0、两个实际平方正、Q1Q2≠0 和共同 h>0 才得到完整支付。

令 a=P1/P2>0；这里 a 不指种子复系数。RI 的两虚部分子准确是
\[
J_1=\mu_1Q_2(\rho_1GZ+2Q_1)
-a(2-\rho_1)G\mu_2Q_1F_1^2,
\]
\[
J_2=\mu_2Q_1(\rho_2Z+2Q_2)
-a^{-1}(2-\rho_2)\mu_1Q_2F_2^2.
\tag{JDI.7}
\]
它们各至多四次，保留 ρ1=2 支，没有用配对乘积代替两式。

再令
\[
\mathfrak d_i=\sqrt{P_i/P_j}
\frac{\alpha_{ij}}{\chi_{ij}}\frac{S_i}{S_j},\quad
\mathfrak a_i=(1-\rho_i)C_i+\mathfrak d_i C_j,\quad
\ell_i=2+\mu_i\rho_i,\quad \{i,j\}=\{1,2\}.
\]
RRI 的两实部分子为
\[
\begin{split}
\mathcal L_1={}&2G\mathfrak a_1F_1^2F_2
+G\mathfrak d_1\mu_2rF_1^2
-2\mu_1Q_1-G\ell_1F_1F_2,\\
\mathcal L_2={}&2\mathfrak a_2F_1F_2^2
+\mathfrak d_2\mu_1F_2^2
-2\mu_2rQ_2-\ell_2rF_1F_2.
\end{split}
\tag{JDI.8}
\]
每式至多三次。αij、花体 d_i、花体 a_i、ℓ_i 或其系数可能为零，均未用作除数。实际发送实相干仍为
\[
G_i=\mathfrak a_i+\frac{\mathfrak d_i\mu_j}{2B_j};
\]
它必须来自同一个发送的 \(X_j/M_j=-\mu_j/(2B_j)\)，并非矩阵中可另行选择的实量。允许 G1=0；G2=0 的原式障碍仍自动由完整条件保留。

## 3. 明确定义全部五条二次余式

令 σ=p2/p3、τ=p1/p3、υ=p0/p3。为避免任何展开过程藏入自由系数，定义仅有四步的纸面余式递推：
\[
V_0(r)=1,\quad V_1(r)=r,\quad V_2(r)=r^2,
\]
\[
V_n=-(\sigma V_{n-1}+\tau V_{n-2}+\upsilon V_{n-3}),
\qquad n=3,4,5,6.
\tag{JDI.9}
\]
由 r³+σr²+τr+υ≡0 模 P，归纳得到 r^n≡V_n 模 P。各 V_n 至多二次；首步及下一步分别为
\[
V_3=-\sigma r^2-\tau r-\upsilon,\qquad
V_4=(\sigma^2-\tau)r^2+(\sigma\tau-\upsilon)r+\sigma\upsilon.
\]
若 \(H=\sum_{n=0}^6 h_nr^n\)，定义
\[
\operatorname{rem}_P H=\sum_{n=0}^6h_nV_n.
\]
这里 h_n 是已明列实际多项式的系数，缺失次数的系数取零；这是一条纸面系数定义，不是执行程序。

五个实际余式定义为
\[
f_0=\operatorname{rem}_P\mathcal A,\qquad
f_1=\operatorname{rem}_P J_1,\quad
f_2=\operatorname{rem}_P J_2,
\]
\[
f_3=p_3\mathcal L_1-\lambda_{13}P,\qquad
f_4=p_3\mathcal L_2-\lambda_{23}P,
\quad \lambda_{i3}=[r^3]\mathcal L_i.
\tag{JDI.10}
\]
ASI.15–19 给出 f0 的全部展开系数；RI.12 正是 f1、f2；RRI.14–18 正是 f3、f4。JDI.3–5、7–10 也独立给出确定它们全部系数的有限显式表达式。后两行整体缩放 p3≠0，不要求 λ_i3 非零。

由上述多项式恒等式，对每个实 r 准确有
\[
\boxed{
P=\mathcal A=J_1=J_2=\mathcal L_1=\mathcal L_2=0
\iff
P=f_0=f_1=f_2=f_3=f_4=0.}
\tag{JDI.11}
\]
此处未除任何未知方向函数，新增除数只有已经支付的 p3 幂。每个 f 可以降次或恒零；JDI.11 在这些退化情况下也成立。

## 4. 五行矩阵与全部直接秩支

按常数、一次、二次顺序写
\[
f_\ell(r)=a_{\ell0}+a_{\ell1}r+a_{\ell2}r^2,\quad
\mathsf A=(a_{\ell j})_{\substack{0\le\ell\le4\\0\le j\le2}},
\quad v(r)=\begin{pmatrix}1\\r\\r^2\end{pmatrix}.
\]
全部 a_{\ell j} 都由第 3 节同一固定几何给定。五个条件联立恰为
\[
\boxed{\mathsf A v(r)=0.}
\tag{JDI.12}
\]
禁止为各行分别选根。下列分类涵盖 rank A 的全部退化，但每支仍保留同一 r 的 P=0 和 \(\mathscr D\)。

| 实际 rank A | 精确代数候选条件 |
|---|---|
| 3 | 无非零核向量，故无任何方向候选。 |
| 2 | 取实核直线的任一非零代表 z=(z0,z1,z2)。必须 z0≠0、z0z2=z1²；此时唯一可能方向 r=z1/z0，再检验 P(r)=0。 |
| 1 | 取任一非零行多项式 q。所有五行都是 q 的实倍数，共同候选恰为 q(r)=P(r)=0 的实根。 |
| 0 | 五余式全部恒零，代数候选恰为非零三次 P 的实根。 |

rank 2 的 P 条件也可不除 z0 写为
\[
p_3z_1^3+p_2z_1^2z_0+p_1z_1z_0^2+p_0z_0^3=0.
\tag{JDI.13}
\]
若 z0=0，则它不能与 v(r) 成比例，无论齐次锥关系是否形式成立，均不增入有限 r。rank 1 中 q 若为非零常数则无根；若为一次则至多一个候选；若为二次则按其真实判别式处理无实根、重实根或两个实根，且仍须与 P 同根。q 的最高项从未作为默认非零量。

这张表没有证明某一实际几何达到任何指定秩，尤其不能把条件“rank A=3 则无解”写成全几何无解。另一方面，rank A<3 也不充分：核中的任意向量未必是 v(r)，更未必通过 P 与严格域。下一节把这些共同代数条件统一变为一个有限实线性算子判据。

## 5. 三维不变核恰给共同代数根

定义纸面实线性算子
\[
\mathsf T=
\begin{pmatrix}
0&1&0\\
0&0&1\\
-\upsilon&-\tau&-\sigma
\end{pmatrix}.
\tag{JDI.14}
\]
粗体算子 \(\mathsf T\) 与实际发送比 \(T=kM_1/M_2\) 完全不同，后者不引入任何新自由度。直接逐行可见
\[
\mathsf T v(r)=r v(r)\quad\iff\quad P(r)=0.
\tag{JDI.15}
\]
反之，若实非零向量 z 满足 \(\mathsf Tz=r z\)，前两行给 z1=rz0、z2=rz1。z0=0 将强迫 z=0，故 z0≠0 且 z=z0v(r)；最后一行给 P(r)=0。这里使用的是实特征向量，广义特征向量本身不提供额外方向。

定义
\[
\mathsf O=
\begin{pmatrix}
\mathsf A\\
\mathsf A\mathsf T\\
\mathsf A\mathsf T^2
\end{pmatrix},\qquad
\mathcal N=\ker_{\mathbb R}\mathsf O.
\tag{JDI.16}
\]
这是至多十五行、三列的纸面实矩阵。由 JDI.14 的移位和末行关系可直接核得
\[
\mathsf T^3+\sigma\mathsf T^2+\tau\mathsf T+\upsilon I=0.
\tag{JDI.17}
\]
具体地，令 \(e^\top=(1,0,0)\)，则 \(e^\top\mathsf T=(0,1,0)\)、\(e^\top\mathsf T^2=(0,0,1)\)，而末行正给
\(e^\top(\mathsf T^3+\sigma\mathsf T^2+\tau\mathsf T+\upsilon I)=0\)。
该多项式与 \(\mathsf T\) 交换，再左乘上述三行即得整矩阵为零。

若 z∈N，则 A z=A T z=A T² z=0；由 JDI.17 又有 A T³z=0，所以 Tz∈N。故 N 是 T 不变的。任何包含在 ker A 中的 T 不变实子空间都满足这三个零式，因而包含于 N；这证明 N 恰为 ker A 中最大的不变子空间，不是只给必要的较小子空间。

现在有精确对应
\[
\boxed{
\{r\in\mathbb R:P(r)=0,\ \mathsf A v(r)=0\}
=\operatorname{spec}_{\mathbb R}
(\mathsf T|_{\mathcal N}).}
\tag{JDI.18}
\]
当 N={0} 时右边按空集理解。证明如下：

* 若左边成立，则 T^jv(r)=r^jv(r)，故 O v(r)=0；v(r) 是 N 内对应实特征向量。
* 若 r 为右边的实特征值，在 N 内取相应非零实特征向量 z。由 JDI.15 的反向论证，z=z0v(r)、P(r)=0；由 N⊂ker A 得 A v(r)=0。

实算子出现实特征值时，其实核有非零实向量，故此处不需要额外复化假设。重根、不可对角化以及所有零余式都已包含在证明中。没有用“某个特征向量存在”替代实根条件，也没有把无穷远点加到 JDI.18。

置 m=dim N=3−rank O。选任一实基表示限制算子 \(T_N\)，其真实实特征值集合与基选择无关，且有以下全部情况：

| m | 精确代数候选 |
|---|---|
| 0 | 空集。 |
| 1 | 限制算子的唯一实标量特征值；仍须严格域检查。 |
| 2 | 用实际 \(d=(\operatorname{tr}T_N)^2-4\det T_N\)：d<0 无实候选；d=0 一个不同实候选；d>0 两个不同实候选。重根时不要求可对角化。 |
| 3 | N=R³，此时 A=0，限制算子的特征多项式为 P/p3；取 P 的全部不同实根。 |

因每个候选均为 P 的根，任何分支至多三个不同实方向。这个步骤只需固定的有限实线性代数和次数至多三的实特征值代数判断；本文没有执行任何矩阵、求根或秩计算。m=2 的非零核仍可能只有一对非实特征值，m=1 或 m=3 的实根也可能全部被严格域排除。故不能把 rank O<3 宣称为最终可行条件。各秩支在实际几何是否能达到仍 OPEN。

## 6. 同一个 r 的严格恢复与完整条件 iff

令
\[
\mathscr C=
\{r\in\operatorname{spec}_{\mathbb R}
(\mathsf T|_{\mathcal N}):\mathscr D(r)\}.
\tag{JDI.19}
\]
JDI.18 与 JDI.11 保证每个 r∈C 同时满足方向、面积、两虚及两实全部六个原多项式等式。接下来只在此同一个 r 恢复同一种子，不能换根。

首先由面积式和 E1>0 得 E2>0，并有
\[
D_1=\frac{E_1}{\mu_1S_1^2G^2F_2^2}>0,\qquad
D_2=\frac{E_2}{\mu_2S_2^2r^2F_1^2}>0,
\]
\[
k=-\sqrt{P_1/P_2}\frac{GF_2}{r^2F_1}\ne0,\qquad D_2=k^2D_1.
\tag{JDI.20}
\]
精确乘数为正：
\[
P_2\mu_1\mu_2S_1^2S_2^2r^4F_1^2(D_2-k^2D_1)=\mathcal A.
\]
按一个共同符号恢复
\[
y_1=\varepsilon\sqrt{D_1},\quad y_2=k y_1,\quad
\varepsilon\in\{-1,1\}.
\tag{JDI.21}
\]
两个平方根不能独立取号。两种共同符号都保留同一实部、模方、发送比和五条余式的通过状态。

保留任一符号性的整体尺度 \(\mathcal B=|a_1|^2>0\)，由原号域恢复
\[
|a_2|^2=\mathcal B\,w/\omega>0,\qquad
h=\frac{4\mathcal B\,g_2Q_1Q_2}
{\mu_1\mu_2G r^3F_2}.
\tag{JDI.22}
\]
该式指定恢复关系，不是在本文选择实际幅度。面积正性给
\[
M_i=X_i^2+S_i^2D_i=-2X_iB_i/\mu_i>X_i^2>0,
\]
从而 XiBi<0、Q1Q2≠0。于是 h 的号是 −sgn(g2X2)，故 JDI.6 的最后一个不等式恰支付 h>0，不是用面积正性替代它。可以保留任意相位的 a1、a2、z0，使其模方为这些同一恢复值。

ASI 的实际权重关系
\[
K_1=g_1|a_2|^2,\quad K_2=g_2\mathcal B/r^2,\quad
K_1/K_2=Gwr^2
\]
与 JDI.2 给 K1B2=K2B1，故同一个 h 使
\[
b_i=K_iM_j/h=-\mu_i/(2X_i),\qquad
b_iM_i=B_i.
\]
对实际 \(t_i=X_i+iS_i y_i\)，两个指定高投影
\(b_it_i^2+\mu_it_i+B_i\) 的虚部和实部因此同时为零。没有给两条行分别分配最低幅度。

最低唯一实部已经按 JDI.2 恢复；P=0 和同一有符号 y2=ky1 恢复最低 C 原方向。ASI 的已明列完整最低接口及其独立法向非零结论同时保证最低 C≠0。本文不以方向多项式单独替代这一非零接口。

还需核两高剩余分量。实际比固定为
\[
T=kM_1/M_2
=-\sqrt{P_1/P_2}\frac{\mu_2Q_1F_1}{\mu_1Q_2F_2}.
\]
用 RI.7 与 RRI.12 的完整非零乘数恒等式，
\[
J_1=\mu_1GQ_2Z M_1\mathcal I_1,\qquad
J_2=\mu_2Q_1Z M_2\mathcal I_2,
\]
\[
\mathcal L_1=-\frac{4F_1^2Q_1}{\mu_1}\mathcal R_1,\qquad
\mathcal L_2=-\frac{4F_2^2Q_2}{\mu_2r}\mathcal R_2,
\tag{JDI.23}
\]
得到同一种子的两虚残差和两实残差全部为零。所有乘数在前述恢复后非零，不从清分母的形式根反向增入禁用支。三份来源共同使用的完整行接口是：最低完整 Z 条件及两个高指定投影通过后，其余两个完整高分量恰由这四个实残差检验。因此现在支付的是三个完整 Z 行，亦即完整 M0=0；不是只检查两条投影或一个配对乘积。

反向，若当前固定规范及原严格域内确有同一种子满足完整 M0=0、最低 C 非零原方向和所列前置接口，则 ASI 给同一实际 r、w、面积式及 JDI.6，RI 和 RRI 给 J1=J2=L1=L2=0。由 JDI.11、18，该 r 必属于 JDI.19。由此获得所要求的条件充要接口：
\[
\boxed{\text{当前固定分支可恢复完整 M0=0 且最低 C 非零原方向}
\iff \mathscr C\ne\varnothing.}
\tag{JDI.24}
\]
这是来源明列接口上的联合恢复定理，没有假定 ASI、RI、RRI 的未来整包接纳，亦不重新证明所有原始 Fourier 展开。

## 7. 号门、退化和未决范围

任一通过 JDI.24 的方向还自动满足 RI 的必要号门
\[
GF_1F_2<0,\quad
0<Q_1<-2GF_1F_2/\mu_1,\quad
0<GQ_2<-2GF_1F_2/\mu_2.
\]
理由是最长实际虚式给 T>0，故 k>0；再用面积正性。它们可作为同一 r 的附加必要筛选，不能代替两条 J 等式、面积关系或 h>0。真实相干的实部门还给
\[
\mu_i\rho_i/2-1<B_iG_i<\mu_i\rho_i/2+1.
\]
这也不是新增充分条件，且不能借其删掉中间 G1=0 的原式分支。本文从未除 2−ρ1、αij、Gi、余式首系数或某个未经判非零的行列式。

五行可有任意数量零行、线性相关、降次或全部为零，分别由 JDI.12–18 保留。即使五余式全零，非零三次 P 仍须成立，并仍须全部严格域；不意味着所有方向可行。形式 r=0、F1F2=0、E1≤0、错误发送模方号和 h≤0 均不被清分母或特征值步骤接纳。项目规范外的最低零投影和无穷方向、C=0 或其它 χ 零域没有被本文排除，而是未覆盖。

本文没有证明实际几何必给某个矩阵秩，也没有证明任一秩支可由整数三频实现。不能从五条二次方程多于一个方向变量推断矛盾；所有系数具有同一几何依赖，且符号定理已保留它们可能相关的情形。也不能把某一余式单独有根与另一余式另有根拼成共同种子。

完成的是同一固定 C0≠0 分支的联合代数与符号接口。其它两个 C 原方向、三行共同模板幅度、实际整数几何及全种子存在或全域排除仍未支付。至多三个方向不等于至多三个初值；尺度与相位仍未实际选取。没有 NS 两步、有限时间再生成、统一余项、单初值无限尺度、有限总时间、奇性或全局正则性结论。精确 M0 首项为零的筛选不排除任意正来源容限；旧失败证据未获追认。

本稿已完成全文自读；最终停改前再次复核四份实际来源字节，随后报告 SHA。EXACT CONDITIONAL JOINT SAME-DIRECTION CRITERION；ALL RANK DEGENERACIES RETAINED；REALIZATION OPEN；NO-CANDIDATE；NOT CLAY。
