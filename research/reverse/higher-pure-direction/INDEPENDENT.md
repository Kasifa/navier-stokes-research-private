# 两个高纯供给总行的复方向条件

2026-09-08，PRIVATE_CORE。独立有界手工推导，待非作者审查及根比较。

**先锁合同。** 已先全文读取本目录 CONTRACT.md。本文从已接纳 NC.9 的完整自供给系数出发，在同一接收平面相加最低发送和另一高发送的实际贡献，给出两个高总 C 行沿各自原复种子方向的条件。FR 及本人 JDI 的停改等式只作明列条件输入；不借前阶段未来整包接纳证明本项。

**结果。** 对每个高接收，总行方向精确等价于一个明确复行列式为零。在共同面积已恢复时，它又等价于下文两个实条件；两高行必须在同一份数据上同时通过。总行非零由另一个明确复系数检验。没有除复双线性自点积，也没有用单条 C 非零替代总行非零。另得到一个有限范围的必要结论：最低发送对某一高椭圆种子的单条 C 必不沿该种子方向，故若高总行沿原方向，另一发送必须实际抵消这一非零方向行列式。此结论不排除两条真实贡献相消。

本人是 JDI 及此前若干投影、完整高行、剩余实部独立稿作者，亦有相关非作者审查历史。本项未读本目录 PROOF.md 或另一作者的新推导，未收到对方本项公式，不称全课题盲推导。全部为一般手工符号，仅工具读取或写入文本、核对哈希；无科学程序、矩阵数组执行、实际频率、初值、幅度、时间或方向选择、求值、枚举、扫描、Git、重置或外发。

## 1. 实际来源和固定域

路径相对于 research/reverse/。以下为本次实际阅读范围及实测字节；旧源内部转引不自动计为本轮实读。

| 来源与实际阅读范围 | SHA-256 |
|---|---|
| higher-pure-direction/CONTRACT.md，先全文读取 | cdda8089bdfedd67d090634ca91fc25e83c33cd0072bd60235c98e5f11d55187 |
| net-mixed-cancellation/INDEPENDENT.md，第 1–140 行，完整 NC.1–12，尤其 NC.9 的全部有序项及协方差规范 | 25111397d32eef2751a91b1ad1ab6a446794742874b97bf6b0b73b3964d11a58 |
| full-high-row-reduction/PROOF.md，本轮全文重读，简称 FR | 3d02da817e164bbf8f75bdddfea74a4e0d2b14c12d890952aeeb727866cc3c6b |
| joint-direction-compatibility/INDEPENDENT.md，本人前轮已全文自读；本轮重读第 24–161、306–390 行，直接几何、种子和共享恢复公式，简称 JDI | 4ed20002939dbafce9f20955dbcf3a0efde1da8aa2ad1f040ce474b9c5861c26 |

保留合同固定的独立整数三频 p0,p1,p2，Pi=|pi|²，P0<P1<P2，全部非正交、最低两条 β 零，及先前所需非零域。记
\[
c_{ik}=p_i\cdot p_k,\quad
\Delta_{ik}=P_iP_k-c_{ik}^2>0,\quad
\Sigma_{ik}=P_i+P_k,\quad d_{ik}=P_i-P_k,
\]
\[
\Lambda_{ik}=\Sigma_{ik}^2-4c_{ik}^2>0,\quad
E_{ik}=\frac{p_k-c_{ik}p_i/P_i}{\sqrt{\Delta_{ik}/P_i}},
\quad N_{ik}=\widehat p_i\times E_{ik}.
\tag{HDI.1}
\]
这里 Σ 不同于下文换基正弦 Si。固定基及同一种子保持
\[
U_0=z_0R,\quad R\ \text{实},\quad |z_0|^2=h>0,
\]
\[
U_i=a_i(E_{i0}+z_iN_{i0}),\quad
z_i=s_i+iy_i,\quad a_i\ne0,\quad y_i\ne0,\quad i=1,2.
\tag{HDI.2}
\]
R·E01、R·E02 非零，负模严格共轭。记
\[
C_i=E_{i0}\cdot E_{ij},\quad S_i=N_{i0}\cdot E_{ij}\ne0,
\quad \{i,j\}=\{1,2\},
\]
\[
t_i=C_i+S_iz_i=X_i+iS_iy_i,\quad
n_i=-S_i+C_iz_i=\frac{C_it_i-1}{S_i},\quad M_i=|t_i|^2>0.
\tag{HDI.3}
\]
字母 n_i 是无量纲复坐标，不是 NC 的向量 p×q。高种子非零面积保证 t_i≠0；这里不要求 Ci 非零。

本文首先不要求完整 M0 已为零：第 2–4 节是该同种子域内直接从 NC.9 得到的纯供给方向恒等式。第 5 节再在 JDI 的明列恢复等式已满足时减少未知量，仍不证明该前置域存在实际实例。

## 2. 从完整 NC.9 到单位基，核对发送法向号

先固定一个接收 p、发送 q，令 P=|p|²、Q=|q|²、c=p·q、Δ=PQ−c²、d=P−Q、Σ=P+Q、Λ=Σ²−4c²。把同一实际种子写成
\[
U=A E+B N,\quad V=D F+H N',
\quad E=E_{pq},\ N=N_{pq},\ F=E_{qp},\ N'=N_{qp},
\quad \omega=H/D.
\]
当前应用中 D≠0：高发送非零面积给每个非零实平面方向的复投影非零。事实上，若该方向的两个实坐标为 α、β，则投影除以 a_i 后为 α+βs_i+iβy_i；其为零将先由 yi≠0 得 β=0，再得 α=0。最低发送的这两个投影已列为非零条件。

NC.9 使用未归一化 e=q−cp/P、f=p−cq/Q、n=p×q，因而
\[
E=\sqrt{P/\Delta}\,e,\quad F=\sqrt{Q/\Delta}\,f,\quad
N=n/\sqrt\Delta,\quad N'=-n/\sqrt\Delta.
\]
所以 NC 的标量坐标准确为
\[
u=A\sqrt{P/\Delta},\quad v=B/\sqrt\Delta,\quad
x=D\sqrt{Q/\Delta},\quad y=-H/\sqrt\Delta,
\]
\[
|x|^2=\frac Q\Delta|D|^2,\quad
\Re(x\bar y)=-\frac{\sqrt Q}{\Delta}|D|^2\Re\omega,\quad
\Im(x\bar y)=\frac{\sqrt Q}{\Delta}|D|^2\Im\omega.
\tag{HDI.4}
\]
发送法向的负号不能删除。将 HDI.4 逐项代入完整 NC.9，得到
\[
\boxed{
C(U,V)=i\theta |D|^2
\left[
cd\,A^2E+
\left\{2cP\,AB-\sqrt{PQ}\,A^2
(\Sigma\Re\omega+2ic\Im\omega)\right\}N
\right],}
\]
\[
\boxed{\theta=\frac{4\Delta^{3/2}d}{P^{3/2}Q\Lambda}.}
\tag{HDI.5}
\]
例如 E 项是 \(4i\Delta^{3/2}cd^2A^2|D|^2/(P^{3/2}Q\Lambda)\)；法向反馈项为 \(8i\Delta^{3/2}cd\,AB|D|^2/(\sqrt P Q\Lambda)\)。这同时核对 θ 的长度因子、两次 d 的位置，以及接收 A²、AB 的复二次依赖。

HDI.5 没有重选某一个有序根：它直接继承 NC.9 中两个第一层完整双有序场的作用以及发送的两个共轭协方差。接收反馈项和发送实、虚相干均保留。

对原频率对定义实际系数，其中 θ、ξ、ψ、λ 为实，Ω 一般为复：
\[
\theta_{ik}=\frac{4\Delta_{ik}^{3/2}d_{ik}}
{P_i^{3/2}P_k\Lambda_{ik}},\quad
\xi_{ik}=c_{ik}d_{ik},\quad
\psi_{ik}=2c_{ik}P_i,
\]
\[
\lambda_{ik}=\theta_{ik}|U_k\cdot E_{ki}|^2,\quad
\Omega_{ik}=\sqrt{P_iP_k}
\{\Sigma_{ik}\Re\omega_{ki}+2ic_{ik}\Im\omega_{ki}\},
\quad
\omega_{ki}=\frac{U_k\cdot N_{ki}}{U_k\cdot E_{ki}}.
\tag{HDI.6}
\]
λ 是带号的完整纯供给权重，不是 FR 的混合投影权重 b。当前排序给 λ10、λ20、λ21>0，λ12<0；不把它们统统改成正数。

## 3. 同一接收平面的总行及精确行列式

最低发送比是实际实数
\[
v_{0i}=\frac{R\cdot N_{0i}}{R\cdot E_{0i}},\qquad
\Omega_{i0}=\sqrt{P_iP_0}\Sigma_{i0}v_{0i}.
\]
另一高发送不能独立设相干；FR 的同一换基给
\[
\omega_{ji}=\frac{C_jt_j-1}{S_jt_j},\quad
\Re\omega_{ji}=\frac{C_j-X_j/M_j}{S_j},\quad
\Im\omega_{ji}=\frac{y_j}{M_j},
\]
\[
|U_j\cdot E_{ji}|^2=|a_j|^2M_j.
\tag{HDI.7}
\]
这些量来自同一个 Uj。接收 i 在另一边的坐标同样必须为 a_i(t_i,n_i)。

记未乘时间首项常数的完整总行
\(\mathcal C_i=C_{i0}+C_{ij}\)。NC.3 的纯供给首项为 \(W_{0,i}=\mathcal C_i/3\)。在同一基 Ei0,Ni0 内准确有
\[
\frac{\mathcal C_i}{ia_i^2}
=\mathfrak q_iE_{i0}+\mathfrak n_iN_{i0},
\tag{HDI.8}
\]
\[
\boxed{\mathfrak q_i=
\lambda_{i0}\xi_{i0}
+\lambda_{ij}
\{(C_i\xi_{ij}+S_i\Omega_{ij})t_i^2
-S_i\psi_{ij}t_in_i\},}
\]
\[
\mathfrak n_i=
\lambda_{i0}(\psi_{i0}z_i-\Omega_{i0})
+\lambda_{ij}
\{S_i\xi_{ij}t_i^2+
C_i(\psi_{ij}t_in_i-\Omega_{ij}t_i^2)\}.
\tag{HDI.9}
\]
这里使用 Eij=CiEi0+SiNi0、Nij=−SiEi0+CiNi0，先相加两条向量，再判断方向。

以 [Ei0,Ni0]=1 定义复双线性有向行列式。由于 Ui 的第一坐标为 a_i≠0，
\[
[\ U_i,\mathcal C_i\ ]=ia_i^3\mathcal F_i,\qquad
\mathcal F_i=\mathfrak n_i-z_i\mathfrak q_i.
\]
直接在每条边自己的同向基中求该行列式，利用 ψik−ξik=cikΣik，得
\[
\boxed{\begin{split}
\mathcal F_i={}&
\lambda_{i0}\Sigma_{i0}
\{c_{i0}z_i-\sqrt{P_iP_0}v_{0i}\}\\
&+\lambda_{ij}t_i^2
\{c_{ij}\Sigma_{ij}n_i-\Omega_{ij}t_i\}.
\end{split}}
\tag{HDI.10}
\]
其与 HDI.9 相减相同，不约去任何可能为零的相干括号。因此
\[
\boxed{\mathcal C_i\in\mathbb C U_i
\iff \mathcal F_i=0,\qquad i=1,2.}
\tag{HDI.11}
\]
此处包含零总行。两行条件必须对同一组种子同时成立。

若需要总行非零，则准确另加
\[
\boxed{\mathfrak q_i\ne0.}
\tag{HDI.12}
\]
因为在 HDI.11 下，
\[
\mathcal C_i=ia_i\mathfrak q_iU_i,\qquad
W_{0,i}=\frac{ia_i\mathfrak q_i}{3}U_i.
\tag{HDI.13}
\]
这里从非零坐标 a_i 取比例，不除 \(U_i\cdot U_i=a_i^2(1+z_i^2)\)。即使该复双线性自点积为零，HDI.8–13 仍原样有效。q_i 的零与非零保留，不能从 C_i0 的非零性跳到总行非零。

## 4. 一个实际但有限的单对方向障碍

最低发送单条贡献的归一化方向行列式是
\[
\frac{[U_i,C_{i0}]}{ia_i^3}
=\lambda_{i0}\Sigma_{i0}
\{c_{i0}s_i-\sqrt{P_iP_0}v_{0i}+ic_{i0}y_i\}.
\tag{HDI.14}
\]
其虚部 λi0Σi0ci0yi 非零：最低发送投影非零，Pi>P0、ci0≠0、yi≠0，且 Σi0>0。故该单条 C_i0 在当前域必不沿高种子 Ui 的复方向。

于是若某个高总行通过 HDI.11，则另一高发送的行列式必须非零并精确等于 HDI.14 的负值。特别地，不能先要求两条单边各自沿 Ui 再把它们相加；该办法在当前域已经失败。这只是两条真实方向缺陷必须相消的必要结构，不证明相消无法实现，也不证明总行非零。

## 5. 在共同面积恢复域中的四个实条件

现在明确加入 FR/JDI 的直接条件输入：最低完整接口、同一真实两个指定高投影、严格面积、共同比值和共同 h 已恢复。使用同一 r 的实际量
\[
M_i=-2X_iB_i/\mu_i>X_i^2>0,\quad
D_i=y_i^2=(M_i-X_i^2)/S_i^2>0,\quad
y_2=ky_1,\quad k\ne0.
\tag{HDI.15}
\]
不预设五条联合余式已在某个实际几何找到共同根。若还要求完整 M0=0，必须把其原等式作为同一数据的另一个条件保留。

对每个 i，令 \(k_1=k,\ k_2=1/k\)，所以 yj/yi=k_i。定义全部实际实系数
\[
\mathsf H_i=
\frac{c_{ij}\Sigma_{ij}C_i}{S_i}
-\sqrt{P_iP_j}\Sigma_{ij}
\frac{C_j-X_j/M_j}{S_j},
\]
\[
\mathsf L_i=\frac{c_{ij}\Sigma_{ij}}{S_i},\qquad
\mathsf V_i=\frac{2c_{ij}\sqrt{P_iP_j}\,k_i}{M_j}.
\tag{HDI.16}
\]
H、L、V 不是可调相干数据。若使用已付 XiBi 非零的投影等式，H 中的实际 \((C_j-X_j/M_j)/S_j\) 也准确等于 \((C_j+\mu_j/(2B_j))/S_j\)。本文不除 H、L 或 V，任一实际相消仍按原式保留。

由 n_i=(Cit_i−1)/Si 和 HDI.7，HDI.10 恰成为
\[
\mathcal F_i=
\lambda_{i0}\Sigma_{i0}
\{c_{i0}(s_i+iy_i)-\sqrt{P_iP_0}v_{0i}\}
+\lambda_{ij}\{(\mathsf H_i-i\mathsf V_i y_i)t_i^3
-\mathsf L_i t_i^2\}.
\tag{HDI.17}
\]
这只是三次 t 与实际 y 的有限表达式，没有大规模清除 r 分母。

把 \(t_i=X_i+iS_iy_i\)、\(D_i=y_i^2\) 代入，逐项分离实虚部：
\[
\boxed{\mathcal F_i=\mathcal D_i^{\rm R}
+iy_i\mathcal D_i^{\rm I},}
\tag{HDI.18}
\]
\[
\boxed{\begin{split}
\mathcal D_i^{\rm R}={}&
\lambda_{i0}\Sigma_{i0}
(c_{i0}s_i-\sqrt{P_iP_0}v_{0i})\\
&+\lambda_{ij}\{
\mathsf H_iX_i(X_i^2-3S_i^2D_i)
+\mathsf V_iS_iD_i(3X_i^2-S_i^2D_i)\\
&\hspace{38mm}-\mathsf L_i(X_i^2-S_i^2D_i)\},
\end{split}}
\]
\[
\boxed{\begin{split}
\mathcal D_i^{\rm I}={}&
\lambda_{i0}\Sigma_{i0}c_{i0}\\
&+\lambda_{ij}\{
\mathsf H_iS_i(3X_i^2-S_i^2D_i)
-\mathsf V_iX_i(X_i^2-3S_i^2D_i)
-2\mathsf L_iX_iS_i\}.
\end{split}}
\tag{HDI.19}
\]
核对用的两式为
\[
t_i^2=(X_i^2-S_i^2D_i)+2iX_iS_iy_i,
\]
\[
t_i^3=X_i(X_i^2-3S_i^2D_i)
+iS_iy_i(3X_i^2-S_i^2D_i).
\]
在 \(-i\mathsf V_i y_i t_i^3\) 中，实部因此是正的 \(\mathsf V_iS_iD_i(3X_i^2-S_i^2D_i)\)，虚部除 yi 后是负的 \(\mathsf V_iX_i(X_i^2-3S_i^2D_i)\)。没有把相干虚部删掉。

由于 yi≠0，得到完整条件
\[
\boxed{
\mathcal C_1\in\mathbb C U_1,\quad
\mathcal C_2\in\mathbb C U_2
\iff
\mathcal D_1^{\rm R}=\mathcal D_1^{\rm I}
=\mathcal D_2^{\rm R}=\mathcal D_2^{\rm I}=0.}
\tag{HDI.20}
\]
若还要求两个高总行都非零，另加同一数据的 \(\mathfrak q_1\mathfrak q_2\ne0\)，不能用 HDI.20 替代。

## 6. 与同一 r、幅度和相位的准确接口

在 JDI 的规范 R·E01=1、R·E02=r≠0 中，记 r1=1、r2=r，实际有
\[
v_{01}=(r-C)/S,\qquad v_{02}=(Cr-1)/(Sr).
\]
直接采用 JDI 明列的同一恢复式
\[
w=F_1/(GrF_2),\quad |a_1|^2=\mathcal B>0,\quad
|a_2|^2=\mathcal B w/\omega>0,
\]
\[
k=-\sqrt{P_1/P_2}\frac{GF_2}{r^2F_1},\qquad
h=\frac{4\mathcal B g_2Q_1Q_2}{\mu_1\mu_2G r^3F_2}>0,
\]
\[
X_1=Q_1/(GF_2),\quad X_2=Q_2/(rF_1),\quad
M_i=-2X_iB_i/\mu_i,\quad D_i=(M_i-X_i^2)/S_i^2>0.
\tag{HDI.21}
\]
si 仍为 JDI 的最低唯一实部，或等价地 si=(Xi−Ci)/Si。所有 rF1F2、G、ω、Si 及必要 χ、γ 非零条件、严格发送模方号、面积等式和共同正 h 均保留。

于是 HDI 的两条权重必须为
\[
\boxed{\lambda_{i0}=\theta_{i0}h r_i^2,\qquad
\lambda_{ij}=\theta_{ij}|a_j|^2M_j.}
\tag{HDI.22}
\]
不能在第二个高行另选最低幅度、发送相干或发送强度。代 HDI.21–22 入 HDI.16、19 即给同一 r 上的四个明确实条件；它们的各项只用已付分母，没有必要在本合同内展开无收益的高次 r 多项式。

共同翻转 y1,y2 时，k_i、Xi、Mi、Di、λ、H、L、V 全部不变，故 HDI.20 的通过状态不变。HDI.9 的 q_i 相应变成其复共轭，零与非零状态也不变。这准确消去一个共同正负选择；不允许独立翻转两条面积或为两个方向条件各用不同 r。

种子各自整体相位只给 HDI.10 的完整行列式乘非零 \(ia_i^3\)，发送端只通过真实 Hermitian 协方差进入。因此相位不能修复失败的方向条件。共同尺度 \(\mathcal B\) 只把 λ、两个 D 残差及 q_i 同乘正尺度，其零状态也不能据此修复。另一方面，实际比例 \(ia_i\mathfrak q_i/3\) 仍含接收相位；三行要符合某个共同模板幅度，还必须另核真实的跨行比例，本文未支付。

## 7. 零支及结论边界

本推导没有除 1+zi²、Ci、si、αij、βij、Gi、H_i 或任何可能为零的相干括号；其零分支保留。单位基换算只除正长度、Δ、Λ 和已付非零发送投影；换基、四实化与 JDI 接口还只除 Si、Sj、ti、Mj、yi、k 和先前明确原域。合同域外的平行、等长、正交、零发送投影或零面积分支不能因本稿得到原域外排除；这些边界若要研究，仍须回到未约除的 NC.9。

总行零是 HDI.11 的一个真实分支，必须以 HDI.12 检验。两个高方向零式可能发生系数消失或相关；本文不以变量个数或形式次数推断不可能，也没有证明任一实际固定几何和方向通过四式。最低完整 C 非零可在前置条件中给定，但高总行的非零不是其后果。

本项新增的是完整 NC.9 的单位基换算、同接收总和的两个复行列式、共同恢复下的四个实条件、总行非零系数及最低发送单对的方向障碍。这些式子给出保留所有真实相干和共享幅度的条件接口，没有实际整数频率或全种子实现，没有一般几何全域排除。若与 JDI 接入，必须先在同一 r 满足其所有等式和严格域，再同时检查本文方向及非零式。

三个行非零、共同模板幅度、真实空间实例、原解时间窗、NS 两步、有限时间再生成、统一余项、单初值无限尺度和有限总时间仍非本项结论。没有新候选，也没有追认旧失败证据；精确空间首项条件不排除任意正来源容限。

本稿已完成逐式手核；最终停改前再次全文自读并复核实际来源字节，随后报告 SHA。EXACT CONDITIONAL HIGHER PURE-DIRECTION TEST；ACTUAL COHERENCE RETAINED；REALIZATION OPEN；NO-CANDIDATE；NOT CLAY。
