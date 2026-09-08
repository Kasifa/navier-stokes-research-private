# 实际面积平方的单变量门与显式二次余式

2026-09-08，PRIVATE_CORE。独立有界推导完成，待非作者审查和根比较。

**结果：在同一 C0≠0 几何及明列恢复域中，面积平方相容可精确写成次数至多六的多项式等式，严格面积正性由一个次数至多四的显式因子表达式检查。方向三次门下，该面积多项式又等价于本文给出全部系数的至多二次余式。连同实际模方号、非零域及 h 正性，这给出最低完整接口加两个高指定投影的条件恢复；没有证明共同根在合法几何上存在或不存在。余式恒零的几何可能性保持 OPEN。**

本稿先全文读取当前合同，只用本人已停止的 LAI 明确公式及已接纳 PP 来源。未读本目录 PROOF.md 或其它本项新稿。本人是 LAI 独立稿作者，并已有前阶段数学与审查历史；本次独立性只针对当前新推导，不称全课题盲审。LAI 整包仍在审查的状态不作为未来定理输入，下文把实际所需等式及域明确重列。全部为手工符号，工具只读写文本及 SHA 元数据；无科学程序、数组、数值求值、实际选参、扫描、Git、重置或外发。

## 1. 实际来源及直接输入

路径相对于 research/reverse/。

| 来源及实际阅读范围 | SHA-256 |
|---|---|
| area-square-compatibility/CONTRACT.md，本轮先全文读取 | 8de0828beaa6b82c9984850b81008d3c0adabffac3bf7ba89172047ff3228c19 |
| lowest-amplitude-compatibility/INDEPENDENT.md，本人前轮全文自读停改；本轮重读第 31–279 行，实际恢复公式和 LAI.22 正性 | 9f4bf7ed5cd9b7dcea92576f9f0b262139451881f05956d329fc69203661962e |
| two-elliptic-compatibility/PROJECTED_PAIR_INDEPENDENT.md，本连续任务前轮全文重读；本轮重读第 177–282 行，PP.12–21 的平方、幅度及恢复 | 44c1f7fd6b616bd3bc1313c8b08607331f641f805329070ea4f93db5e72d8eef |

本轮已实测这三项字节，内部转引不自动计为实读。

固定合同的同一整数三频和单位基，记 \(P_i=|p_i|^2\)、\(C=C_0\ne0\)、\(S=S_0\ne0\)。保留 P0<P1<P2、三频独立、全部非正交、最低双 beta 零及实际所需 χ 非零域。最低实代表和高种子保持
\[
R=E_{01}+\frac{r-C}{S}N_{01},\quad r\ne0,\quad
U_0=z_0R,\quad
U_i=a_i\{E_{i0}+(s_i+iy_i)N_{i0}\}.
\tag{ASI.1}
\]
全部几何量固定，实际 y_i 将在恢复时确定，a_i 是单位平面复系数而非各边独立种子。

以下等式作为本稿直接输入。它们使用同一个 r：
\[
F_1=b_{10}+b_{11}r,\quad F_2=b_{20}r+b_{21},\quad
B_1=F_1,\quad B_2=F_2/r,
\]
\[
w=\frac{F_1}{G rF_2},\qquad
rF_1F_2\ne0,\quad G\ne0,\quad
\frac w\omega>0.
\tag{ASI.2}
\]
这里
\[
\omega=\frac{L_{02}\chi_{02}}{L_{01}\chi_{01}}\ne0,\quad
L_{ik}=2(\Delta_{ik}/P_i)^{3/2},
\quad
w=\omega\frac{|a_2|^2}{|a_1|^2},
\]
\[
g_2=\left(\frac{\Delta_{12}}{\Delta_{20}}\right)^{3/2}
\frac{\chi_{21}}{\chi_{20}}\ne0,\qquad
G=\frac{\chi_{12}\chi_{20}\chi_{01}}
{\chi_{10}\chi_{21}\chi_{02}}.
\tag{ASI.3}
\]
所以 w/ω>0 是真实发送模方号要求。
同一实际发送还满足以下明确输入：
\[
g_1=\left(\frac{\Delta_{12}}{\Delta_{10}}\right)^{3/2}
\frac{\chi_{12}}{\chi_{10}},\quad
K_1=g_1|a_2|^2,\quad K_2=g_2|a_1|^2/r^2,\quad
\frac{K_1}{K_2}=Gwr^2.
\]
最后一式由 \(G=g_1/(g_2\omega)\) 和实际 w 定义直接核得，不使用两个可独立选择的行权重。

最低方向门的直接等式为
\[
P(r)=rF_1(A_2Cr-M)+G F_2(Lr-A_1C)=0,\qquad
A_1,A_2,L,M>0.
\tag{ASI.4}
\]
最低唯一实部和高接收实部仍为
\[
s_1=\frac{2r-C+wr^2}{S\gamma_1},\qquad
s_2=\frac{C-2/r-1/(wr^2)}{S\gamma_2},\qquad
X_i=C_i+S_i s_i,
\tag{ASI.5}
\]
其中 \(\gamma_i=\sqrt{P_0/P_i}\alpha_{0i}/\chi_{0i}\ne0\)，\(S_i\ne0\)。

对每一高投影，\(\mu_i=\kappa_{i0}/\chi_{i0}>2\)。PP 在本单位坐标中的所需平方和实际最低面积比是
\[
D_i=\frac{-2X_iB_i/\mu_i-X_i^2}{S_i^2},
\qquad
k=-\frac{\sqrt{P_1/P_2}}{wr^3}.
\tag{ASI.6}
\]
需要 \(D_1,D_2>0\)、\(D_2=k^2D_1\) 及真实有符号式 \(y_2=k y_1\)，不能仅恢复两个独立平方根。

## 2. 同一个 w 下的两个二次分子

令固定非零数 \(v_i=S_i/(S\gamma_i)\)。代入 ASI.2，逐项清除 X_i 的分母：
\[
\boxed{X_1=\frac{Q_1(r)}{G F_2},\qquad
X_2=\frac{Q_2(r)}{rF_1},}
\tag{ASI.7}
\]
\[
\boxed{Q_1=[C_1+v_1(2r-C)]G F_2+v_1 rF_1,}
\]
\[
\boxed{Q_2=(C_2+v_2C)rF_1-v_2(2F_1+G F_2).}
\tag{ASI.8}
\]
没有为另一高行重选发送实部。两个 Q_i 都是次数至多二的显式多项式。

为给出可逐项核验的系数，写 \(Q_i=q_{i2}r^2+q_{i1}r+q_{i0}\)，则
\[
q_{12}=v_1(2G b_{20}+b_{11}),
\]
\[
q_{11}=G[(C_1-v_1C)b_{20}+2v_1b_{21}]+v_1b_{10},
\qquad q_{10}=G(C_1-v_1C)b_{21},
\]
\[
q_{22}=(C_2+v_2C)b_{11},
\]
\[
q_{21}=(C_2+v_2C)b_{10}-v_2(2b_{11}+G b_{20}),
\qquad q_{20}=-v_2(2b_{10}+G b_{21}).
\tag{ASI.9}
\]
这些系数可以为零，本文不约去任何 Q_i 的首项。

## 3. 四次正性因子与六次面积门

令 \(T(r)=F_1F_2\)，并定义完全显式的因子表达式
\[
E_1=-Q_1(\mu_1Q_1+2G T),\qquad
E_2=-Q_2(\mu_2Q_2+2T).
\tag{ASI.10}
\]
直接代入 ASI.6，得到
\[
\boxed{D_1=\frac{E_1}{\mu_1S_1^2G^2F_2^2},\qquad
D_2=\frac{E_2}{\mu_2S_2^2r^2F_1^2}.}
\tag{ASI.11}
\]
两分母严格正。因此 D_i>0 分别等价于 E_i>0；两表达式的次数至多四。这保留了 E_i 的零因子边界，而非仅命名一个新残差。

实际有符号 k 也被同一个 w 固定：
\[
\boxed{k=-\sqrt{P_1/P_2}\frac{G F_2}{r^2F_1}\ne0.}
\tag{ASI.12}
\]
故
\[
k^2D_1=
\frac{P_1E_1}{P_2\mu_1S_1^2r^4F_1^2}.
\]
G²F2² 在这里准确抵消，不能把它们再当作额外未知量。把 D2=k²D1 乘以严格正
\[
P_2\mu_1\mu_2S_1^2S_2^2r^4F_1^2
\]
得
\[
\boxed{\mathcal A(r)=
P_2\mu_1S_1^2r^2E_2-P_1\mu_2S_2^2E_1=0.}
\tag{ASI.13}
\]
因此面积平方门精确等价于
\[
\boxed{\mathcal A(r)=0,\qquad E_1(r)>0.}
\tag{ASI.14}
\]
这已推出 E2>0，因为 ASI.13 两个实权重以及 r² 均严格正。反向也不需要新增除法。\(\mathcal A\) 的次数至多六；没有证明其对每份几何都恰为六次或都不恒零。

## 4. 六次门的全部系数

写
\[
T=t_2r^2+t_1r+t_0,\quad
t_2=b_{11}b_{20},\quad
t_1=b_{10}b_{20}+b_{11}b_{21},\quad
t_0=b_{10}b_{21}.
\]
令 \(\eta_1=G,\eta_2=1\)，写 \(E_i=e_{i4}r^4+e_{i3}r^3+e_{i2}r^2+e_{i1}r+e_{i0}\)。手工展开 ASI.10 得
\[
e_{i4}=-q_{i2}(\mu_iq_{i2}+2\eta_i t_2),
\]
\[
e_{i3}=-2\mu_iq_{i2}q_{i1}
-2\eta_i(q_{i2}t_1+q_{i1}t_2),
\]
\[
e_{i2}=-\mu_i(q_{i1}^2+2q_{i2}q_{i0})
-2\eta_i(q_{i2}t_0+q_{i1}t_1+q_{i0}t_2),
\]
\[
e_{i1}=-2\mu_iq_{i1}q_{i0}
-2\eta_i(q_{i1}t_0+q_{i0}t_1),
\qquad
e_{i0}=-q_{i0}(\mu_iq_{i0}+2\eta_i t_0).
\tag{ASI.15}
\]
置固定正数 \(a=P_2\mu_1S_1^2\)、\(b=P_1\mu_2S_2^2\)，它们不是种子复系数 a_i。则
\[
\mathcal A(r)=j_6r^6+j_5r^5+j_4r^4+j_3r^3+j_2r^2+j_1r+j_0
\]
的全部系数是
\[
j_6=ae_{24},\quad j_5=ae_{23},\quad
j_4=ae_{22}-be_{14},\quad
j_3=ae_{21}-be_{13},
\]
\[
j_2=ae_{20}-be_{12},\qquad
j_1=-be_{11},\qquad j_0=-be_{10}.
\tag{ASI.16}
\]
ASI.9、15、16 一起给出仅由固定几何决定的每一个系数，无程序展开或隐藏自由参数。

## 5. 方向三次的非零首项与逐式余式

这里仅在当前 C≠0 域做除法。重列方向多项式系数：
\[
P(r)=p_3r^3+p_2r^2+p_1r+p_0,
\]
\[
p_3=A_2Cb_{11},\quad
p_2=A_2Cb_{10}-Mb_{11}+GLb_{20},
\]
\[
p_1=-Mb_{10}+GLb_{21}-GA_1Cb_{20},\qquad
p_0=-GA_1Cb_{21}.
\tag{ASI.17}
\]
非零首项不以未来整包接纳作前提：当前直接几何系数有
\[
b_{11}=-\sqrt{P_1/P_0}\,
\frac{\alpha_{10}}{\chi_{10}}\frac{S_1}{S},
\qquad
b_{21}=\sqrt{P_2/P_0}\,
\frac{\alpha_{20}}{\chi_{20}}\frac{S_2}{S}.
\]
所用已写出的反向最低 beta 几何恒等式为
\[
\alpha_{i0}
=\frac{2(4x^4+8x^3+19x^2+30x+20)}
{3(x+2)(4x^2+2x+3)}>0,\qquad x=P_i/P_0\in(1,4).
\]
这是 LAI.22 明确列出的系数输入；其分子分母逐项严格正。因此 b11、b21 均非零，进而 p3、p0 非零。本文只用这些明确等式及正性，不引用“LAI 整包已经接纳”。P 确为非零三次且 r=0 不是其根。

定义固定实数
\[
\sigma=p_2/p_3,\qquad \tau=p_1/p_3,\qquad
\upsilon=p_0/p_3.
\]
以下同余只指相差 P 的多项式倍数。由
\[
r^3\equiv-\sigma r^2-\tau r-\upsilon
\]
逐次乘 r 并回代，手工得到
\[
r^4\equiv(\sigma^2-\tau)r^2+(\sigma\tau-\upsilon)r+\sigma\upsilon,
\]
\[
r^5\equiv(-\sigma^3+2\sigma\tau-\upsilon)r^2
+(-\sigma^2\tau+\tau^2+\sigma\upsilon)r
-\sigma^2\upsilon+\tau\upsilon,
\]
\[
r^6\equiv(\sigma^4-3\sigma^2\tau+\tau^2+2\sigma\upsilon)r^2
+(\sigma^3\tau-2\sigma\tau^2-\sigma^2\upsilon+2\tau\upsilon)r
+\sigma^3\upsilon-2\sigma\tau\upsilon+\upsilon^2.
\tag{ASI.18}
\]
故显式余式 \(\mathcal R(r)=R_2r^2+R_1r+R_0\) 的实际系数为
\[
\begin{aligned}
R_2={}&j_2-\sigma j_3+(\sigma^2-\tau)j_4\\
&+(-\sigma^3+2\sigma\tau-\upsilon)j_5\\
&+(\sigma^4-3\sigma^2\tau+\tau^2+2\sigma\upsilon)j_6,
\end{aligned}
\]
\[
\begin{aligned}
R_1={}&j_1-\tau j_3+(\sigma\tau-\upsilon)j_4\\
&+(-\sigma^2\tau+\tau^2+\sigma\upsilon)j_5\\
&+(\sigma^3\tau-2\sigma\tau^2-\sigma^2\upsilon+2\tau\upsilon)j_6,
\end{aligned}
\]
\[
\begin{aligned}
R_0={}&j_0-\upsilon j_3+\sigma\upsilon j_4
+(-\sigma^2\upsilon+\tau\upsilon)j_5\\
&+(\sigma^3\upsilon-2\sigma\tau\upsilon+\upsilon^2)j_6.
\end{aligned}
\tag{ASI.19}
\]
所以在同一固定几何上，准确有
\[
\boxed{P(r)=\mathcal A(r)=0
\iff P(r)=\mathcal R(r)=0.}
\tag{ASI.20}
\]
这没有对未知 r 除以某个可能为零的函数；新分母仅是已付非零的 p3 幂。如需使余式系数不含这些新分母，可整体乘非零 \(p_3^4\)，零集不变。

没有声称余式必为二次或必非零。若 R2≠0，则同根方向至多两个；若 R2=0、R1≠0，则至多一个；若 R2=R1=0、R0≠0，则此几何无共同根；若三者均零，则面积等式在方向三次的全部根上自动成立，但仍须正性和恢复域。最后一种几何条件是否可能实现，本稿未解决。即使余式恒零，已付的非零 P 仍只给至多三个方向根；这不等于存在合法实例或有限个初值。

## 6. 正性、真实符号与完整 PP 恢复

保留实际符号
\[
k=-\sqrt{P_1/P_2}\frac{G F_2}{r^2F_1},
\qquad
\operatorname{sgn}k=-\operatorname{sgn}(GF_1F_2).
\tag{ASI.21}
\]
平方等式本身没有保留这个号。通过 ASI.14 后，可且必须按同一共同符号恢复
\[
y_1=\varepsilon\sqrt{\frac{E_1}{\mu_1S_1^2G^2F_2^2}},
\qquad y_2=k y_1,\qquad \varepsilon\in\{-1,1\}.
\tag{ASI.22}
\]
两个 y 非零且真实 D_i 都恢复，不能在第二行另选正负号。单位有向面积为 \(2|a_i|^2y_i\)，其比值是 \((|a_2|^2/|a_1|^2)k\)，一般不是 k；这里只能直接把 k 的号识别为面积比的号。

共同最低模方不能由正平方自动替代。保留 \(|a_1|^2=\mathcal B>0\) 为同一整体尺度，实际
\[
|a_2|^2=\mathcal B\,w/\omega>0,\qquad
K_2=g_2\mathcal B/r^2,
\]
\[
\boxed{h=
\frac{4\mathcal B\,g_2X_1X_2F_1}{r^2\mu_1\mu_2}
=\frac{4\mathcal B\,g_2Q_1Q_2}
{\mu_1\mu_2G r^3F_2}>0.}
\tag{ASI.23}
\]
在 E1>0、面积等式成立的域内，D_i>0 强制 \(X_iB_i<0\)，并给 X_i≠0。因此这里 h>0 还精确等价于
\[
g_2X_2<0
\iff g_2Q_2\,rF_1<0.
\tag{ASI.24}
\]
第二个等价只乘了正数 \((rF_1)^2\)。G、g2 皆可带号，本文没有将它们正化。

现在给出准确条件接口。在明列固定几何与 ASI.1–5 的直接最低恢复公式内，存在同一非零面积 y_i 及正 h，使最低完整条件与两个指定高投影均通过，当且仅当该 r 满足
\[
\boxed{
P(r)=0,\quad \mathcal A(r)=0,\quad E_1(r)>0,\quad
rF_1F_2\ne0,\quad w/\omega>0,\quad
g_2Q_2rF_1<0.}
\tag{ASI.25}
\]
其中 w 必须是 ASI.2 的实际值，\(\mathcal A=0\) 可按 ASI.20 替换为 \(\mathcal R=0\)；所有条件必须在同一 r 上判断。

必要性由 PP 的真实平方、最低面积关系及共同 h 直接给出。反向使用 ASI.22 恢复 y_i，并由 ASI.23 取同一所需正 h。此时
\[
|t_i|^2=X_i^2+S_i^2D_i=-2X_iB_i/\mu_i
=B_i/\Lambda_i>0,\qquad
\Lambda_i=-\mu_i/(2X_i).
\]
由 ASI.2 的实际 K 比例有 \(K_1B_2=K_2B_1\)，故
\[
\frac{K_i}{h}|t_j|^2=\Lambda_i.
\]
代回每个实际投影
\[
\lambda_i t_i^2+\mu_i t_i+B_i
\]
时，其虚部因 \(2\Lambda_iX_i+\mu_i=0\) 为零，实部因 \(\Lambda_i|t_i|^2=B_i\) 为零。这支付了 PP 的完整两个指定投影，而非只支付平方名字。

最低 Z 已由 s_i 唯一实部恢复；P=0 在非零 GF2 域等价于最低实三次式，y2=k y1 又是同一最低 C 的有符号面积条件。已接纳 PP 的独立法向论证保证该最低 C 非零。相位与尺度保持同一向量规范，负模仍是该组种子的共轭。上述充分性完全是条件恢复，未选出任何实际数据，也未证明 ASI.25 有解。

## 7. 零支与尚未解决范围

全部清分母步骤保留 \(rF_1F_2\ne0\)、G≠0、S、S_i、γ_i、χ 非零和正 P_i、μ_i。F1=0 或 F2=0 对应被 PP 排除的 B_i=0；不能因六次清分母式在那里有形式根而接纳它。r=0 失活，w=0 不对应两个非零实际发送模方。w/ω 的负号域也不能恢复实际 |a_i|²。

E1=0 是零面积边界，E1<0 无实非零平方，均排除。E1>0 与面积式已强制 Q1、Q2 非零；不需要先约去其可能零因子。两个 Q 或 E 的最高次系数可以为零，次数下降仍按同一式判断。ASI.19 的余式亦允许降次或恒零；未判其几何实现性。

本项只覆盖 C0≠0 域。p3 的除法理由已明确写出，不能把此余式公式用于较弱 C0=0 分支。单独的面积多项式可能恒零，不能以它宣称有限根；这里的有限方向根仅来自已明确非零的方向三次 P，且每根仍有全部严格不等式和同数据条件。

新闭合内容是：真实 X 的二次分子、面积四次因子与正性、次数至多六的精确清分母门、全部系数、模方向三次的实际二次余式，以及带号与正 h 的 PP 反向恢复。两高行尚余的完整复分量、其它两个 C 原方向、共同模板幅度均未支付。几何共同根存在、实际整数频率实现或全域排除仍 OPEN。

没有新 NS 时间、同数据无限维余项、跨代控制、有限两步机制、单初值无限尺度、有限总时间、奇性或全局正则性结论。没有实际参数、候选接纳或旧失败证据修复。

EXACT CONDITIONAL AREA-SQUARE POLYNOMIAL；EXPLICIT QUADRATIC REMAINDER；REALIZATION OPEN；NO-CANDIDATE；NOT CLAY。
