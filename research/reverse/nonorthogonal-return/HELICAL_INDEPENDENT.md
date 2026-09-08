# 单螺旋三对共享种子：独立方向障碍

2026-09-08，PRIVATE_CORE。依先锁定的 HELICAL_CONTRACT 与 JOINT_CONTRACT 独立手推。本文尚待非作者全文审查，不以作者结论代替最终接纳。

**命题。** 对合同内任意三个线性独立、长度两两不同的整数波向量，至少一对非正交，任意三个独立螺旋符号及非零复幅度，指定完整纯 \(w_{22}\) 树在全部六个加倍接收模上都不能成为
\(\rho Oa(2O^T(x-x_0))\)。这里保留所有 Gram 相容的 O、同一正时间、共同正幅度及平移。证明仅使用接收方向的必要条件和全部精确热权重的正性；没有先把幅度、时间或相位当作独立可调供给。

这只否定单螺旋极化子类的指定精确树返回，不否定非圆偏振种子、其它模板或完整 NS 再生成。

## HI.1 实际来源与推导范围

本轮完整读取以下四个文件，路径相对此目录：

| 来源 | SHA256 |
|---|---|
| HELICAL_CONTRACT.md | b64a3142fb6e0d261ece899e5b5f4c767d0ed89e1ae0083637b0f4acac3f2e05 |
| JOINT_CONTRACT.md | cc3cd571b87cde40488345d8d8faa6ac774892701f30869ee479c3d82088e23c |
| SPATIAL_PROOF.md | 50510f2b1b2bee2ed3739bd9a5a1276f16056e244f5b71192b9a39b8066190a5 |
| SOURCE_AND_HEAT_PREFLIGHT.md | cd0206ef0164387d41e246485d1f4a3a0815fef42ed45163816d21ac4e6fdbe0 |

未读取根代理的新 JOINT／HELICAL 证明或另一代理的共同稿。复用已接纳的完整单对空间映射，并自行代入螺旋约束、重建接收配对与变换条件；没有重做或重命名单对原公式。全部新推导为手工符号运算；没有科学程序、数组、指数数值、具体参数选择、Git、外部定理或新颖性声明。

以下点积按复双线性延拓，只有明确写出的共轭及 Hermitian 范数取共轭。记

\[
P_i=|p_i|^2,\quad \xi_i=\chi_i\sqrt{P_i},\quad
M_i=U_i\cdot\overline U_i>0,\qquad
i p_i\times U_i=\xi_i U_i.
\tag{HI.1}
\]

长度不同保证 \(\xi_i-\xi_j\ne0\) 及 \(\xi_i+\xi_j\ne0\)，不论两个螺旋符号是否相同。圆偏振有 \(U_i\cdot U_i=0\)，但这绝不意味着 \(U_i=0\) 或 \(M_i=0\)。

## HI.2 接收配对穷尽与全部允许变换

以线性独立的 \(p_1,p_2,p_3\) 作频率的代数基底。横向性使同轴原种子配对逐项为零，故第一层支撑包含于全部
\(\{\sigma p_i+\tau p_j:i<j,\ \sigma,\tau=\pm1\}\)。

两个这样的第一层频率之和若为 \(2p_i\)，两者的第 i 基底系数都必须为一；各自剩下的另一轴必须相同且符号相反。因此全部配对恰为

\[
(p_i+p_j,p_i-p_j),\quad(p_i-p_j,p_i+p_j),\qquad j\ne i.
\]

没有其它接收配对，也没有把其中任何有序项再乘二。于是完整接收系数为

\[
F_i(t):=(w_{22})_{2p_i}(t)
=\sum_{j\ne i}J_{ij}(t)C_{ij},\qquad t>0,
\tag{HI.2}
\]

其中 \(C_{ij}\) 是已接纳的共享单对映射。完整树在接收集外的系数未从演化中删除。精确权重为

\[
J_{ij}(t)=\int_0^t
e^{-4P_i(t-s)-2(P_i+P_j)s}
\left(\frac{\sinh(c_{ij}s)}{c_{ij}}\right)^2ds>0,\qquad
c_{ij}=p_i\cdot p_j.
\tag{HI.3}
\]

若 \(c_{ij}=0\)，括号取其精确连续值 s。证明不改变各边不同的热权重，也不以小时间近似替代它们。

长度两两不同使任何题定 O 必满足 \(Op_i=\varepsilon_i p_i\)。保持 Gram 内积给

\[
c_{ij}=\varepsilon_i\varepsilon_j c_{ij};
\]

因此非正交边的两个端点必须有相同符号。反过来，对一组满足该条件的符号，以这三个基向量定义的线性映射保持 Gram 矩阵，故确实正交。其行列式为
\(\delta=\varepsilon_1\varepsilon_2\varepsilon_3\)。
这涵盖 \(O=\pm I\) 及非正交图断开时的其它相容符号，不把每行反射独立化。

正接收模的目标系数严格是

\[
\rho e^{-2ip_i\cdot x_0}O U_i^{(\varepsilon_i)},\qquad
U_i^{(+)}=U_i,\quad U_i^{(-)}=\overline U_i.
\tag{HI.4}
\]

由正交叉积恒等式
\(a\times Ob=\delta O((O^Ta)\times b)\)，及
\(i p_i\times U_i^{(\varepsilon_i)}
=\varepsilon_i\xi_iU_i^{(\varepsilon_i)}\)，得到

\[
i p_i\times O U_i^{(\varepsilon_i)}
=\delta\xi_i O U_i^{(\varepsilon_i)}.
\tag{HI.5}
\]

故 \(\delta=+1\) 的目标与 \(U_i\) 同一螺旋直线，\(\delta=-1\) 的目标与 \(\overline U_i\) 同一直线。特别 \(O=-I\) 的目标是带共同模板规则的 \(-\overline U_i\)，不是 \(U_i\)。

两条螺旋直线都是 \(p_i^\perp\) 内的一维复空间。由其双线性零向量结构，返回必分别满足

\[
\delta=+1:\quad U_i\cdot F_i=0;\qquad
\delta=-1:\quad \overline U_i\cdot F_i=0.
\tag{HI.6}
\]

这只是方向必要条件；没有用它替换共同幅度或平移的充分性。所有目标系数都非零，故 \(F_i=0\) 也不能算返回。负接收模始终为真正复共轭。

## HI.3 螺旋代入共享单对映射

对有序边 \(i\leftarrow j\)，暂写 \(p=p_i,q=p_j,P=P_i,Q=P_j,c=c_{ij}\)，并令

\[
\Delta=PQ-c^2>0,\quad
L_\pm=P+Q\pm2c,\quad R=L_+L_->0,
\]
\[
e_p=q-\frac cPp,\quad e_q=p-\frac cQq,\quad n=p\times q.
\]

因为 \(p\times e_p=n,\ p\times n=-Pe_p\)，以及
\(q\times e_q=-n,\ q\times n=Qe_q\)，全部螺旋极化恰写为

\[
U_i=a\left(e_p+\frac{i}{\xi_i}n\right),\qquad
U_j=d\left(e_q-\frac{i}{\xi_j}n\right),\qquad a,d\ne0.
\tag{HI.7}
\]

这里 a、d 是同一原种子的边分量，不能跨边独立选择。记
\(z_{ij}=U_i\cdot p_j\)。横向分解给

\[
a=\frac{P}{\Delta}z_{ij},\quad
|a|^2=\frac{PM_i}{2\Delta},\quad
|d|^2=\frac{QM_j}{2\Delta},\quad z_{ij}\ne0.
\tag{HI.8}
\]

最后非零性也可由圆偏振的实二维表示直接看到：非零螺旋向量与非零实横向向量的双线性点积不为零。

将 \(b=ia/\xi_i,\ e=-id/\xi_j\) 代入已接纳的 NS.5–6，法向括号化为

\[
a^2Q(L_-d\overline e+L_+\overline d e)
+4cPab|d|^2
=4ic\,a^2|d|^2(\xi_i-\xi_j).
\]

所以当 \(c\ne0\) 时，

\[
C_{ij}=C_e\left(e_p+\frac{2i}{\xi_i+\xi_j}n\right),\qquad
C_e=\frac{4ic\Delta^3(P-Q)^2}{P^2Q^2R}a^2|d|^2.
\tag{HI.9}
\]

投影、双有序项及共享种子的 b 项均保留。若 \(c=0\)，应直接代入完整 NS.5–6：平面项为零，法向项含
\(d\overline e+\overline d e=0\)，其余项也带 c，故

\[
c_{ij}=0\quad\Longrightarrow\quad C_{ij}=0.
\tag{HI.10}
\]

这里没有错误地把仅在 \(c\ne0\) 下成立的 NS.7 零判据套到正交边。

利用 \(|e_p|^2=\Delta/P,\ |n|^2=\Delta\)，在 HI.9 上分别点乘 \(U_i\)、\(\overline U_i\)，再用 HI.8，得到对所有边都成立的两个精确投影：

\[
\boxed{
U_i\cdot C_{ij}
=-\frac{2ic_{ij}(P_i-P_j)^3M_j}
{P_jR_{ij}(\xi_i+\xi_j)^2}\,z_{ij}^{\,3}.}
\tag{HI.11}
\]

\[
\boxed{
\overline U_i\cdot C_{ij}
=\frac{ic_{ij}\Delta_{ij}(P_i-P_j)^2M_iM_j}
{P_iP_jR_{ij}}\,
\frac{3\xi_i+\xi_j}{\xi_i+\xi_j}\,z_{ij}.}
\tag{HI.12}
\]

例如前式的方向因子是
\[
1-\frac{2\xi_i}{\xi_i+\xi_j}
=\frac{\xi_j-\xi_i}{\xi_i+\xi_j}
=-\frac{P_i-P_j}{(\xi_i+\xi_j)^2},
\]
后式则为 \(1+2\xi_i/(\xi_i+\xi_j)\)。这核明了立方符号及特殊因子 \(3\xi_i+\xi_j\)。式中是 \(z_{ij}^3\) 和 \(z_{ij}\)，不能改成模长或另取共轭。

## HI.4 反定向目标：保留特殊长度比后仍矛盾

固定 i，令 j、k 为另外两轴。三个波向量的线性独立性在此表现为：
\[
p_j-\frac{c_{ij}}{P_i}p_i,\qquad
p_k-\frac{c_{ik}}{P_i}p_i
\]
在实平面 \(p_i^\perp\) 线性独立。非零圆偏振点积
\(v\mapsto U_i\cdot v\) 是该实平面到 \(\mathbb C\) 的可逆实线性映射，因此 \(z_{ij},z_{ik}\) 在 \(\mathbb C\) 中实线性独立。

HI.12 中除 i 和 \(z_{ij}\) 外的系数均为实数，包括精确正热权重。因此反定向必要条件
\(\overline U_i\cdot F_i=0\) 强迫两个实系数逐一为零。对每条非正交边，所有几何、长度及模长因子都非零，故必有

\[
3\xi_i+\xi_j=0.
\tag{HI.13}
\]

这是一个允许出现的单向特殊分支，未事先删除。可是同一条边反向接收也须满足 \(3\xi_j+\xi_i=0\)；合并即得 \(\xi_i=9\xi_i\)，与 \(\xi_i\ne0\) 矛盾。

合同至少有一条非正交边，所以所有 \(\det O=-1\) 的共同返回均失败。这包含 \(O=-I\)，也包含非正交图断开时其它反定向 O；不需要假定所有螺旋符号相同。

## HI.5 保定向目标：缺边和三倍相位条件

现在取 \(\det O=+1\)。由 HI.10，正交边没有树输出。若非正交图不完整，三个顶点中至少一个度数不超过一。度零时 \(F_i=0\)；度一时，HI.11 的唯一非正交项严格非零，因为 \(P_i\ne P_j,\ z_{ij}\ne0\)。二者分别违反非零目标或 \(U_i\cdot F_i=0\)。

因此只剩三个 \(c_{ij}\) 全非零。写

\[
U_i\cdot F_i=i\sum_{j\ne i}w_{ij}z_{ij}^3,\qquad
w_{ij}=
-\frac{2J_{ij}c_{ij}(P_i-P_j)^3M_j}
{P_jR_{ij}(\xi_i+\xi_j)^2}\in\mathbb R\setminus\{0\}.
\tag{HI.14}
\]

每行只有两项；若它们相消，两个非零复数必须共线且相反。特别
\(z_{ij}^3/z_{ik}^3=-w_{ik}/w_{ij}\) 是非零实数。

取 \(p_i^\perp\) 的实正交单位基 \(e_1,e_2\)，其中
\(e_2=(p_i/|p_i|)\times e_1\)。由单螺旋条件，
\(U_i=A_i(e_1+i\chi_i e_2)\)。
如果 j、k 的实横向投影的夹角余弦为 \(t_i\)，那么
\(z_{ij}/z_{ik}\) 的辐角就是该有向夹角乘 \(\chi_i\)，模长为正。
投影线性独立排除了夹角零或 \(\pi\)。因此三倍辐角为 \(\pi\) 的整数倍，恰强迫

\[
t_i\in\{-1/2,1/2\}.
\tag{HI.15}
\]

且由 \(\cos(3\theta)=4\cos^3\theta-3\cos\theta\)，

\[
\operatorname{sgn}\!\left(\frac{z_{ij}^3}{z_{ik}^3}\right)
=-\operatorname{sgn}(t_i).
\]

结合相消等式，有必要符号条件

\[
\operatorname{sgn}(t_i)=\operatorname{sgn}(w_{ij}w_{ik}).
\tag{HI.16}
\]

这一符号关系不依赖 \(\chi_i\) 的正负，也没有给每条边新设独立相位。

## HI.6 Gram 正定性与最低频行的冲突

令 \(x_{ij}=c_{ij}/\sqrt{P_iP_j}\)，G 为三个单位波向量的 Gram 矩阵。G 严格正定，且

\[
t_i=\frac{x_{jk}-x_{ij}x_{ik}}
{\sqrt{(1-x_{ij}^2)(1-x_{ik}^2)}},
\qquad \{i,j,k\}=\{1,2,3\}.
\tag{HI.17}
\]

把 \(G^{-1}\) 用正对角矩阵归一化为对角线全一的矩阵 K。由三阶余子式公式，K 的三个非对角元依次为
\(K_{12}=-t_3,\ K_{13}=-t_2,\ K_{23}=-t_1\)。
故在 HI.15 下，

\[
0<\det K
=1-(t_1^2+t_2^2+t_3^2)-2t_1t_2t_3
=\frac14-2t_1t_2t_3.
\]

若三个 t 的乘积为 \(1/8\)，该行列式为零，违反线性独立性；所以

\[
t_1t_2t_3=-\frac18.
\tag{HI.18}
\]

再对 \(K^{-1}\) 作对角归一化会恢复 G。其同一余子式公式给

\[
x_{jk}=\frac{t_i+t_jt_k}
{\sqrt{(1-t_j^2)(1-t_k^2)}}
=\frac23t_i.
\tag{HI.19}
\]

最后一步用 \(t_jt_k=-t_i/2\) 和分母 \(3/4\)。因此

\[
x_{12}x_{13}x_{23}=-\frac1{27}<0,\qquad
\operatorname{sgn}x_{jk}=\operatorname{sgn}t_i.
\tag{HI.20}
\]

这些值是必要角条件与正定性强迫的代数结果，不是选定一组三维频率或作参数实验。

现在仅重排标签使 \(P_1<P_2<P_3\)。HI.14 的所有未带符号因子都严格正，因而在最低频行

\[
\operatorname{sgn}(w_{12}w_{13})
=\operatorname{sgn}(c_{12}c_{13})
=\operatorname{sgn}(x_{12}x_{13}).
\]

HI.16 要求 \(\operatorname{sgn}t_1=\operatorname{sgn}(x_{12}x_{13})\)；
HI.19 又给 \(\operatorname{sgn}t_1=\operatorname{sgn}x_{23}\)。
二者迫使 \(x_{12}x_{13}x_{23}>0\)，与 HI.20 矛盾。

故保定向共同返回也不成立。推导没有遗漏圆偏振的零双线性范数，没有预设各螺旋符号相同，也没有用不同接收幅度遮蔽这个方向矛盾。

## HI.7 结论与边界

反定向分支由同一非正交边两端的特殊长度比冲突排除；保定向分支先排除缺边，再由共同三倍相位、Gram 正定性与最低频行符号排除。所有 Gram 相容 O 都由其行列式落入这两个分支。正交边、单通道、零接收及 \(3\xi_i+\xi_j=0\) 的单向特殊分支均已单列处理。

因此本文给出的结论是 **NO-CANDIDATE FOR THE SPECIFIED SINGLE-HELICITY PURE-2+2 DOUBLED-TEMPLATE GATE**，待独立审查。没有试算任何实际波向量、时间、复幅度或新初值。

该障碍只使用已定义纯树的完整接收公式，并未将 \(v_1\) 认证为同一真实解中的第一代供给，也未支付树项到真实原解的误差。真实 NS 的 1+3/3+1、种子直接混合、回流、目标外反馈及无限维余项仍未控制。没有否定非圆偏振极化、其它模板、近似返回或一般有限两步机制，更没有统一无限尺度、有限总时间或 NS 奇性／正则性结论。
