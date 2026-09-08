# 真实发送相干代入后的两个剩余实部

2026-09-08，PRIVATE_CORE。独立有界推导，待非作者审查及根比较。

**有界目标与直接前提：** 固定同一 C0≠0、最低种子线性、两个高种子面积非零的合法三频几何；只在下文明确重列的最低完整方向、两个指定高投影、实际面积平方及同一正最低幅度都已恢复的域内，从已接纳 FR.10 推导两个剩余实部的准确条件。另一发送的实相干必须来自同一实际 Xj/Mj，不能作为自由实量。此处不假定任何剩余虚部已经为零，也不预设共同可解或全域矛盾。

**所得结果：** 真实发送相干可用前置投影等式消去为同一 Bj 的倒数。两个剩余实部分别准确等价于本文两个至多三次多项式零式；给出全部系数和完整非零乘数。沿同一非零方向三次，各自还可无损约减为显式至多二次式。可能为零的 αij、Gi 和多项式首项均保留，并得到实部为零所必需的严格 BG 区间。没有证明任何合法几何的共同根存在或不存在。

本人曾形成 TEI、HI、PP、FH、几何独立稿及相关审查，紧前已审过新的剩余虚部主稿；该阅读历史如实披露，不称全课题盲审。本项未读根的 remaining-real-compatibility 新稿或其它本项新推导，未收到根对此项的具体结构结果。新的剩余虚部稿及其结论不作为本稿输入，下文直接从 FR.10 和同数据恢复等式手推。任务先按父任务明确的有界消息启动；本文件开头及第 1 节记录实际使用的目标与前提，不倒写为此前已全文读取某份本项纸面合同。

仅手工符号、文本和哈希元数据；无科学程序、数组、数值求值、实际频率/初值/幅度/时间选择、扫描、Git、重置、外发或发布。

## 1. 同一恢复域及来源

固定原独立整数三频 p0、p1、p2，Pi=|pi|²，P0<P1<P2，全部非正交、最低双 β 零、所需 χ 非零。令
\[
E_{ij}=\frac{p_j-(p_i\cdot p_j)p_i/P_i}
{\sqrt{\Delta_{ij}/P_i}},\qquad
N_{ij}=\widehat p_i\times E_{ij},\qquad
\Delta_{ij}=P_iP_j-(p_i\cdot p_j)^2>0.
\]
最低基的 C=E01·E02≠0、S=N01·E02≠0；高基的 Ci=Ei0·Eij、Si=Ni0·Eij≠0，其中 {i,j}={1,2}。所有这些几何量在判断 r 前固定。

最低实代表及高种子统一保持
\[
R=E_{01}+\frac{r-C}{S}N_{01},\quad r\ne0,
\qquad U_0=z_0R,\quad |z_0|^2=h>0,
\]
\[
U_i=a_i\{E_{i0}+(s_i+iy_i)N_{i0}\},
\quad a_i\ne0,\quad y_i\in\mathbb R\setminus\{0\}.
\tag{RRI.1}
\]
负模是这同一组三种子的共轭。没有为不同接收行另选种子。

以下都是本稿明确直接输入；即使前阶段整包尚在综合接纳，也只使用这些实际等式：
\[
F_1=b_{10}+b_{11}r,\quad F_2=b_{20}r+b_{21},
\quad B_1=F_1,\quad B_2=F_2/r,
\]
\[
G=\frac{\chi_{12}\chi_{20}\chi_{01}}
{\chi_{10}\chi_{21}\chi_{02}}\ne0,\quad
\omega=\frac{L_{02}\chi_{02}}{L_{01}\chi_{01}}\ne0,
\quad L_{ik}=2(\Delta_{ik}/P_i)^{3/2},
\]
\[
rF_1F_2\ne0,\qquad
w=\frac{F_1}{GrF_2},\qquad
w/\omega=|a_2|^2/|a_1|^2>0,
\]
\[
P(r)=rF_1(A_2Cr-M)+GF_2(Lr-A_1C)=0,
\qquad A_1,A_2,L,M>0.
\tag{RRI.2}
\]
F 的系数均为同一几何的实际系数。这里的方向多项式 P 与平方长度 Pi 不混用；G 也不同于下文的实际发送相干系数 Gi。

为把仿射系数也明确绑定到原几何，令
\[
\mu_i=\kappa_{i0}/\chi_{i0}>2,\qquad
\zeta_i=\sqrt{P_i/P_0}\frac{\alpha_{i0}}{\chi_{i0}}\frac{S_i}{S}.
\]
则实际有
\[
b_{10}=(1-\mu_1)C_1+\zeta_1C,\quad b_{11}=-\zeta_1,
\]
\[
b_{20}=(1-\mu_2)C_2-\zeta_2C,\quad b_{21}=\zeta_2.
\]
这些式子由 R·N01=(r−C)/S、(R·N02)/(R·E02)=(Cr−1)/(Sr) 代入 FR.3 直接得到，不把四个 b 当成可独立调节的通道参数。

最低唯一实部和实际接收实部为
\[
\gamma_i^0=\sqrt{P_0/P_i}\,\alpha_{0i}/\chi_{0i}\ne0,\qquad
v_i=S_i/(S\gamma_i^0),
\]
\[
s_1=\frac{2r-C+wr^2}{S\gamma_1^0},\qquad
s_2=\frac{C-2/r-1/(wr^2)}{S\gamma_2^0},\qquad
X_i=C_i+S_i s_i.
\]
写出 ASI 的同一实际二次分子：
\[
Q_1=[C_1+v_1(2r-C)]GF_2+v_1rF_1,
\]
\[
Q_2=(C_2+v_2C)rF_1-v_2(2F_1+GF_2),
\qquad
X_1=\frac{Q_1}{GF_2},\quad X_2=\frac{Q_2}{rF_1}.
\tag{RRI.3}
\]
两式可以直接由上一行 s_i 通分核出，未将另一边实相干独立化。

前置实际平方、面积和共同幅度均已通过：
\[
\mu_i=\kappa_{i0}/\chi_{i0}>2,\qquad
M_i=-\frac{2X_iB_i}{\mu_i}>X_i^2>0,\qquad
D_i=\frac{M_i-X_i^2}{S_i^2}>0,
\]
\[
k=-\frac{\sqrt{P_1/P_2}}{wr^3}
=-\sqrt{P_1/P_2}\frac{GF_2}{r^2F_1}\ne0,
\qquad D_2=k^2D_1,\quad y_2=ky_1,\quad y_i^2=D_i,
\]
\[
K_i=\frac{L_{ij}\chi_{ij}|a_j|^2}
{L_{i0}\chi_{i0}(R\cdot E_{0i})^2},\qquad
h=-\frac{2K_1X_1M_2}{\mu_1}
=-\frac{2K_2X_2M_1}{\mu_2}>0.
\tag{RRI.4}
\]
因此对同一个 ti=Xi+iSi yi，实际投影权重
\[
b_i=\frac{K_iM_j}{h}=-\frac{\mu_i}{2X_i}\ne0,
\qquad |t_i|^2=M_i,\qquad B_i=b_iM_i
\tag{RRI.5}
\]
使两个指定高投影 bi ti²+μi ti+Bi 为零。RRI.4 已保证 Xi、Bi、Qi、Mi、Ki 均非零；不是等到后续清分母后才忽略其零支。

本次实际来源如下，路径相对于 research/reverse/：

| 来源及本轮阅读范围 | SHA-256 |
|---|---|
| full-high-row-reduction/PROOF.md，第 1–120 行，实际重读 FR.1–10 及紧接虚式开头；该文此前已全文阅读 | 3d02da817e164bbf8f75bdddfea74a4e0d2b14c12d890952aeeb727866cc3c6b |
| area-square-compatibility/INDEPENDENT.md，本轮先局部重读后再次全文读取；使用所明列恢复公式、实际分子和非零方向三次 | 489fd488a5dbc8dcdc1336904a16d8dcbe3817077ec74137ead1706f545d4acc |

内文转引不自动计为本次实读。这里未重做全部原始 Leray 展开，也未使用正在形成的剩余虚部判据。

## 2. 实际发送实相干的无损代入

按 FR 的同一单位基换基，另一高发送的实际实比值是
\[
\operatorname{Re}\omega_{ji}
=\frac{C_j-X_j/M_j}{S_j}.
\]
RRI.4 的等式给出关键恒等式
\[
\boxed{\frac{X_j}{M_j}=-\frac{\mu_j}{2B_j},\qquad
\operatorname{Re}\omega_{ji}
=\frac{C_j+\mu_j/(2B_j)}{S_j}.}
\tag{RRI.6}
\]
这里约去 Xj 之前已由严格平方门支付 Xj≠0，Bj、Sj 也非零。该相干仍是同一个 Uj 的真实换基量，不能从 RRI.6 把 Bj 改成另一个自由实参数。

为避免最低 γ_i^0 与高交互系数混同，定义固定实数
\[
\mathfrak d_i=
\sqrt{P_i/P_j}\frac{\alpha_{ij}}{\chi_{ij}}\frac{S_i}{S_j},
\qquad
\mathfrak a_i=(1-\rho_i)C_i+\mathfrak d_iC_j,
\qquad
\rho_i=\kappa_{ij}/\chi_{ij},\quad
\ell_i=2+\mu_i\rho_i.
\tag{RRI.7}
\]
ρ2>2 来自严格最长接收；ρ1 不预设正号或大于 2。这里的花体 a 不指种子系数 ai。αij、花体 d、花体 a、ℓ_i 均允许为零，不作为除数。

FR.8 的实际相干系数因此准确成为
\[
\boxed{G_i=\mathfrak a_i+\frac{\mathfrak d_i\mu_j}{2B_j}.}
\tag{RRI.8}
\]
Gi 可以在某个允许方向上为零，后面不能先除 Gi。该式消去的是实相干的自由外观，没有删掉实际相干贡献。

## 3. 两个完整实部的直接降阶

从 FR.10 的完整实残差出发，
\[
\mathcal R_i=
\frac{2X_i^2-M_i}{M_i^2}
+\frac{b_i\rho_iX_i}{M_i}+b_iG_i.
\]
用 RRI.4–5，首先有
\[
\frac{2X_i^2-M_i}{M_i^2}
=\frac{\mu_i^2}{2B_i^2}+\frac{\mu_i}{2X_iB_i},
\qquad \frac{X_i}{M_i}=-\frac{\mu_i}{2B_i}.
\]
除以已非零 bi，逐项得到
\[
\boxed{\frac{\mathcal R_i}{b_i}
=G_i-\frac{\mu_iX_i}{B_i^2}-\frac{\ell_i}{2B_i}.}
\tag{RRI.9}
\]
第一分式的贡献为 −μiXi/Bi²−1/Bi，第二项另给 −μiρi/(2Bi)，所以 ℓ_i 的常数 2 及所有号均有出处。

将 RRI.8 代入，再乘非零 2Bi²Bj，定义实际中间表达式
\[
\mathcal E_i=
2\mathfrak a_iB_i^2B_j
+\mathfrak d_i\mu_jB_i^2
-2\mu_iX_iB_j-\ell_iB_iB_j.
\]
其完整恒等式为
\[
\boxed{\mathcal E_i
=\frac{2B_i^2B_j}{b_i}\mathcal R_i.}
\tag{RRI.10}
\]
这里 E 不是面积正性因子，也不是新自由残差名；右侧给出准确原实部及非零乘数。

把 B1=F1、B2=F2/r 和实际 X1、X2 全部代入，对第一行乘 Gr、第二行乘 r²，分别得到显式多项式
\[
\boxed{\begin{aligned}
\mathcal L_1(r)={}&
2G\mathfrak a_1F_1^2F_2
+G\mathfrak d_1\mu_2rF_1^2
-2\mu_1Q_1-G\ell_1F_1F_2,\\
\mathcal L_2(r)={}&
2\mathfrak a_2F_1F_2^2
+\mathfrak d_2\mu_1F_2^2
-2\mu_2rQ_2-\ell_2rF_1F_2.
\end{aligned}}
\tag{RRI.11}
\]
每式次数至多三：F 仿射，Q 至多二次。实际发送相干代入后的相消使第一行 Xi 项直接成为 Q1，第二行成为 rQ2；不能把它们先看作独立高阶变量。

不仅零集一致，准确有
\[
\mathcal L_1=Gr\,\mathcal E_1
=-\frac{4F_1^2Q_1}{\mu_1}\mathcal R_1,
\qquad
\mathcal L_2=r^2\mathcal E_2
=-\frac{4F_2^2Q_2}{\mu_2r}\mathcal R_2.
\tag{RRI.12}
\]
所有乘数非零，故在第 1 节原恢复域内，
\[
\boxed{\mathcal R_1=\mathcal R_2=0
\iff \mathcal L_1(r)=\mathcal L_2(r)=0.}
\tag{RRI.13}
\]
反向可直接用
\[
\mathcal R_1=-\frac{\mu_1\mathcal L_1}{4F_1^2Q_1},
\qquad
\mathcal R_2=-\frac{\mu_2r\mathcal L_2}{4F_2^2Q_2}
\]
恢复。带号乘数只用于等式，不当作严格不等式的正因子。r=0、F1F2G=0 或 Qi=0 的形式多项式根不能因此增入原域。

## 4. 两个三次多项式的全部系数

本节仅以 u=b10、v=b11、s=b20、t=b21 简写固定仿射系数，即 F1=u+vr、F2=sr+t；它们不是新选定的几何或种子参数。写 Qi=q_i2 r²+q_i1 r+q_i0，其实际系数可直接由 RRI.3 确定：
\[
q_{12}=v_1(2Gs+v),\quad
q_{11}=G[(C_1-v_1C)s+2v_1t]+v_1u,\quad
q_{10}=G(C_1-v_1C)t,
\]
\[
q_{22}=(C_2+v_2C)v,\quad
q_{21}=(C_2+v_2C)u-v_2(2v+Gs),\quad
q_{20}=-v_2(2u+Gt).
\tag{RRI.14}
\]
这里 v_i 是 RRI.3 的固定基系数，不等同于无下标 v=b11。

令 \(\mathcal L_i=\lambda_{i3}r^3+\lambda_{i2}r^2+\lambda_{i1}r+\lambda_{i0}\)。直接展开 RRI.11，第一行全部系数为
\[
\lambda_{13}=Gv^2(2\mathfrak a_1s+\mathfrak d_1\mu_2),
\]
\[
\lambda_{12}
=2G\mathfrak a_1(v^2t+2uvs)
+2G\mathfrak d_1\mu_2uv
-2\mu_1q_{12}-G\ell_1vs,
\]
\[
\lambda_{11}
=2G\mathfrak a_1(2uvt+u^2s)
+G\mathfrak d_1\mu_2u^2
-2\mu_1q_{11}-G\ell_1(us+vt),
\]
\[
\lambda_{10}
=2G\mathfrak a_1u^2t-2\mu_1q_{10}-G\ell_1ut.
\tag{RRI.15}
\]
第二行则为
\[
\lambda_{23}
=2\mathfrak a_2vs^2-2\mu_2q_{22}-\ell_2vs,
\]
\[
\lambda_{22}
=2\mathfrak a_2(us^2+2vst)
+\mathfrak d_2\mu_1s^2
-2\mu_2q_{21}-\ell_2(us+vt),
\]
\[
\lambda_{21}
=2\mathfrak a_2(2ust+vt^2)
+2\mathfrak d_2\mu_1st
-2\mu_2q_{20}-\ell_2ut,
\]
\[
\lambda_{20}=t^2(2\mathfrak a_2u+\mathfrak d_2\mu_1).
\tag{RRI.16}
\]
这逐项列出两个实际多项式，而非只指定“存在某个消元分子”。所有系数可以按其实际几何发生消失；本文未除 λ_i3 或宣称它恒非零。

## 5. 同一方向三次上的无损二次门

方向多项式的明确系数为
\[
P(r)=p_3r^3+p_2r^2+p_1r+p_0,
\]
\[
p_3=A_2Cb_{11},\quad
p_2=A_2Cb_{10}-Mb_{11}+GLb_{20},
\]
\[
p_1=-Mb_{10}+GLb_{21}-GA_1Cb_{20},
\qquad p_0=-GA_1Cb_{21}.
\]
当前 C≠0 域的非零首项有实际几何理由：
\[
b_{11}=-\sqrt{P_1/P_0}\frac{\alpha_{10}}{\chi_{10}}\frac{S_1}{S},
\qquad
\alpha_{i0}=
\frac{2(4x^4+8x^3+19x^2+30x+20)}
{3(x+2)(4x^2+2x+3)}>0,\quad x=P_i/P_0>1.
\tag{RRI.17}
\]
该直接公式在已读 ASI 中明列，且此前本人已从 NC 复算；此处只用其每项严格正及 A2Cχ10S1S≠0 得 p3≠0，不借前阶段整包未来状态。C=0 的较弱域不在当前结论内。

定义两个显式缩放余式
\[
\boxed{\begin{aligned}
\widehat{\mathcal L}_i(r)={}&
(p_3\lambda_{i2}-p_2\lambda_{i3})r^2\\
&+(p_3\lambda_{i1}-p_1\lambda_{i3})r\\
&+p_3\lambda_{i0}-p_0\lambda_{i3}.
\end{aligned}}
\tag{RRI.18}
\]
不是仅给“取余式”的名字：其每个系数均在 RRI.14–17 中明确给出。精确多项式恒等式为
\[
\widehat{\mathcal L}_i=p_3\mathcal L_i-\lambda_{i3}P.
\]
由于 p3≠0，
\[
\boxed{P=\mathcal L_1=\mathcal L_2=0
\iff P=\widehat{\mathcal L}_1=\widehat{\mathcal L}_2=0}
\tag{RRI.19}
\]
在原恢复域内双向成立。这里甚至不需为余式系数新增 p3 分母，亦未除 λ_i3；λ_i3=0 时依然直接适用。

若某一余式为非零常数，则该固定几何无共同方向根；非零一次、二次余式分别至多给一个、两个不同实共同根。一个余式恒零时它不再新增对应等式，另一个与 P 及原域仍须检查；两个均恒零时，两实部在允许的 P 根上不再加条件，但尚未支付的其它要求仍保留。P 非零三次，至多三个不同实方向根；这不是有限个实际初值的声明。重根、余式降次或恒零均未删除，其实际几何可实现性未解决。

## 6. 不除 Gi 的严格必要界和零分支

RRI.9 给每一实部为零的等价形式
\[
B_iG_i=\frac{\mu_iX_i}{B_i}+1+\frac{\mu_i\rho_i}{2}.
\]
而前置严格面积门给
\[
-2/\mu_i<X_i/B_i<0.
\]
因此得到必要严格区间
\[
\boxed{\frac{\mu_i\rho_i}{2}-1
<B_iG_i<
\frac{\mu_i\rho_i}{2}+1.}
\tag{RRI.20}
\]
此式没有把 Bi 或 Gi 当正因子。它只是在同一 r 上的必要界，不能替代 RRI.11 的等式。

Gi=0 的分支精确按原式处理：
\[
\mathcal R_i=0,\ G_i=0
\iff
\frac{X_i}{B_i}=-\frac1{\mu_i}-\frac{\rho_i}{2},\ G_i=0
\]
并继续要求原恢复域。与严格面积相容必须有
\[
-2/\mu_i<\rho_i<2/\mu_i.
\tag{RRI.21}
\]
这是必要可行号域及仍须成立的准确等式，不证明它可由实际几何实现。最长侧 μ2>2、ρ2>2，使 RRI.20 的下端严格正，所以 G2=0 不可能通过该实部；若通过，B2G2>0。中间 G1=0 不能照搬最长排除，必须保留 RRI.21 和同一 r 的等式。

αij=0 时，花体 d_i=0，实际 Gi=(1−ρ_i)Ci，RRI.9–19 原样成立；没有除 αij。花体 a_i=0、ℓ_i=0、Ci=0 或某多项式系数为零也只是相应项消失，不产生另选发送实相干的自由度。ρ1 的正负不预设。若 G_i 因两实际项相消而为零，仍只能用上述原式，不能删除该方向。

两种共同 y 符号恢复保持 Xi、Mi、真实 Re ωji 和两个 L 多项式不变，因此两个共同符号对本实部门的通过状态一致。这不授权独立改变相对号 k；实际面积与最低 C 方向仍要求同一个 y2=ky1。

## 7. 条件恢复与尚未支付的完整目标

在第 1 节直接恢复域内，两个至多三次式零、或同一 P 上两个缩放二次余式零，精确等价于两个 FR.10 实残差零。必要性和反向恢复由 RRI.12 直接给出，没有从清分母的形式根恢复被禁用分支。

与 ASI 的接口是条件性的：先在同一个 r 上支付最低实方向、合法发送模方号、两个正平方及实际带号关系和同一正 h，按这些条件恢复同一种子；再检验本文两个多项式。本文不证明前置域非空，也不从面积多项式根自动推定 h 正。

尚缺的两个虚残差仍是已接纳 FR.11 的直接等式，本文既未求它们为零，也不使用正在形成的新剩余虚部推导来补证。只有日后在同一组恢复数据中另付两虚部，才可结合 FR 完整二分量接口判断完整高行；不能将本文两个实式单独称为完整 M0=0。其它两个 C 原方向、三行共同模板幅度仍未检查。

这些低次多项式与必要号界不证明合法整数几何或全部种子共同根存在，也不证明所有几何无解。没有实际频率、初值、面积、幅度或时间选择；没有新 NS 时间核、同解供给或无限维跨代误差预算。精确零首项筛选不排除任意正来源容限或所有有限时间机制。有限两步、再生成、统一迭代、同一固定初值无限尺度、有限总时间及奇性仍未支付，旧失败证据未修复。

本稿完成后全文自读并复核实际来源字节，再报告最终 SHA 后停改。EXACT CONDITIONAL REAL-PART CUBICS；ACTUAL SENDER COHERENCE RETAINED；EXPLICIT SCALED QUADRATIC REMAINDERS；REALIZATION OPEN；NO-CANDIDATE；NOT CLAY。
