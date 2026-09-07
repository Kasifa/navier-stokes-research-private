# 不等长三轴纯前代加倍返回：独立推导

2026-09-08，PRIVATE_CORE。**裁决：NO-CANDIDATE FOR THIS EXACT PURE-2+2 DOUBLED-TEMPLATE GATE。**

本作者只从实际合同出发独立手推，未读本目录根代理的 PROOF.md。没有选择频率、极化、ρ、平移或新初值，没有运行科学程序、数组或旧核。本结论覆盖合同中的全部复二维横向极化和八个 signed-axis D；它只否定指定有限代数返回门。

## 1. 记号与配对穷尽

写
\[
z_{ij}:=U_i\cdot e_j,\qquad z_{ii}=0.
\]
若 \(\{i,j,k\}=\{1,2,3\}\)，定义行内实交叉量
\[
R_i:=\operatorname{Re}(\overline{z_{ij}}z_{ik}).
\tag{IA.1}
\]
交换 j、k 不改变 \(R_i\)。它不是两独立横向通道的自由参数，而是同一 \(U_i\) 的相关量。

完整双线性系数为
\[
\widehat{B(f,g)}_\xi=-iP_\xi\sum_{r+s=\xi}
(\widehat f_r\cdot s)\widehat g_s.
\]
同轴种子配对因横向性逐项为零，包括零频和 \(\pm2p_i\)；
故第一代 N 的支撑包含于合同的 L，不假定其中所有系数非零。

若 L 中两输入之和为 \(2p_i\)，它们的第 i 轴坐标必须分别为 \(+n_i,+n_i\)。
每个输入另有且只有一个非零轴坐标；这两个额外坐标必须落在同一 j≠i 上并反号。
因此全部输入恰为
\[
(p_i+p_j,p_i-p_j),\qquad(p_i-p_j,p_i+p_j),
\quad j\ne i.
\tag{IA.2}
\]
没有其它 L+L 配对能到达 \(2p_i\)。这由独立轴坐标逐项推出，不依赖把不等频率当成非共振近似。
下面保留 IA.2 的两个次序。

## 2. 第一代系数的完整 Leray 计算

固定互异 i、j，令 k 为剩余轴。临时记
\[
a=n_i,\ b=n_j,\quad
u=z_{ij},\ v=z_{ik},\ x=z_{ji},\ y=z_{jk},\qquad
\delta=\frac{b^2-a^2}{a^2+b^2}.
\]
这些字母只用于本节代数，不选取参数。
初始负模为严格复共轭。将两个有序初始项相加并做完整投影，得到
\[
\begin{aligned}
N_+&:=N_{p_i+p_j}=-iX_+,\\
X_+&=\delta ux(b e_i-a e_j)+(b u y+a x v)e_k,
\end{aligned}
\tag{IA.3}
\]
\[
\begin{aligned}
N_-&:=N_{p_i-p_j}=-iX_-,\\
X_-&=-\delta u\bar x(b e_i+a e_j)+(-b u\bar y+a\bar x v)e_k.
\end{aligned}
\tag{IA.4}
\]
例如正和频投影前是
\[
b u(xe_i+ye_k)+a x(ue_j+ve_k).
\]
它沿 \((a,b)\) 的内积为 \(2abux\)，因此必须减去
\((a e_i+b e_j)2abux/(a^2+b^2)\)，给出 IA.3 的 \(\delta\)。
差频的对应内积是 \(-2ab u\bar x\)，给出 IA.4。
这里没有把 Leray 替换为横向分量删取，亦没有将差频系数当作和频系数的共轭；
两者的 p_i 叶相同，只有 p_j 叶被共轭。

## 3. 第二代两有序项与全部接收系数

设 \(\xi_\pm=p_i\pm p_j\)。由 IA.3–4，
\[
N_+\cdot\xi_-=-2iab\delta ux,\qquad
N_-\cdot\xi_+=2iab\delta u\bar x.
\]
故该对 j 对 \(F_{2p_i}\) 的完整贡献为
\[
\begin{aligned}
F^{(ij)}_{2p_i}
&=-iP_{2p_i}
[(N_+\cdot\xi_-)N_-+(N_-\cdot\xi_+)N_+]\\
&=-2iab\delta u\,P_{2p_i}(\bar xX_+-xX_-).
\end{aligned}
\]
括号内的 e_j 分量恰为零；e_i 分量由 \(P_{2p_i}\) 消去；
剩余分量为
\[
(\bar xX_+-xX_-)\cdot e_k
=bu(\bar xy+x\bar y)
=2bu\,\operatorname{Re}(\bar xy).
\]
特别地，两个含 \(v|x|^2\) 的项完全相消。于是
\[
\boxed{\quad
F^{(ij)}_{2p_i}
=-4i\,n_i n_j^2
\frac{n_j^2-n_i^2}{n_i^2+n_j^2}\,
z_{ij}^{\,2}R_j\,e_k .
\quad}
\tag{IA.5}
\]
系数4已经包含两个有序次序及共轭交叉和，不再额外乘2。

定义非零实常数
\[
C_{ij}:=4n_i n_j^2\frac{n_j^2-n_i^2}{n_i^2+n_j^2},
\qquad i\ne j.
\]
频率长度互异保证 \(C_{ij}\ne0\)。由 IA.2 的穷尽，
\[
\boxed{\quad
F_{2p_i}
=-i C_{ik}z_{ik}^{\,2}R_k\,e_j
-i C_{ij}z_{ij}^{\,2}R_j\,e_k,
\qquad\{i,j,k\}=\{1,2,3\}.
\quad}
\tag{IA.6}
\]
写成六个明确分量即
\[
\begin{array}{ll}
F_{2p_1,2}=-iC_{13}z_{13}^2R_3,&
F_{2p_1,3}=-iC_{12}z_{12}^2R_2,\\
F_{2p_2,1}=-iC_{23}z_{23}^2R_3,&
F_{2p_2,3}=-iC_{21}z_{21}^2R_1,\\
F_{2p_3,1}=-iC_{32}z_{32}^2R_2,&
F_{2p_3,2}=-iC_{31}z_{31}^2R_1.
\end{array}
\tag{IA.7}
\]
轴向分量均为0。B将实场送为实场，所以
\(N_{-\xi}=\overline{N_\xi}\)、\(F_{-2p_i}=\overline{F_{2p_i}}\)。
IA.6–7连同这一共轭关系给出全部六个接收模，不只给正模的实极化特例。

## 4. 返回方程与所有零分支

允许任意 \(D=\operatorname{diag}(d_1,d_2,d_3)\)，每个 \(d_i=\pm1\)，
和合同的 \(\rho>0,|\eta_i|=1\)。
对复数 \(z\)，写 \(z^{(+)}=z,z^{(-)}=\bar z\)。
两横向返回方程是
\[
-iC_{ik}z_{ik}^2R_k
=\rho\eta_i d_j z_{ij}^{(d_i)},\qquad
-iC_{ij}z_{ij}^2R_j
=\rho\eta_i d_k z_{ik}^{(d_i)}.
\tag{IA.8}
\]

若 \(z_{ij}=0,z_{ik}\ne0\)，第二式左侧为0、右侧非零，矛盾。
若 \(z_{ik}=0,z_{ij}\ne0\)，第一式同理矛盾。
\(U_i\ne0\) 排除了两者同时为零。因此任何可能返回必须使全部六个 \(z_{ij}\ne0\)。

在此条件下，任意 \(R_j=0\) 都会使另一个接收模的某一横向通道为0，
而对应目标通道非零；故还必须有全部三个 \(R_i\ne0\)。
这处理了纯单通道种子、相对正交复相位及可能导致第一代退化的返回分支，
之后的除法不丢失允许解。

## 5. 行内相位只允许两种相关性模长

对每行固定一个 j、k次序，令
\[
r_i=\frac{z_{ik}}{z_{ij}}\ne0.
\]
IA.8 相除使同一行的 \(\rho\eta_i\) 消去，得到
\[
r_i^2r_i^{(d_i)}
=d_jd_k\,\frac{C_{ij}R_j}{C_{ik}R_k}
\in\mathbb R\setminus\{0\}.
\tag{IA.9}
\]
右侧实数的符号不被预先指定，负的频率差、交叉量和反射符号全部保留。

- 若 \(d_i=+1\)，则 \(r_i^3\) 为非零实数，故
  \(\arg r_i\in(\pi/3)\mathbb Z\)。
- 若 \(d_i=-1\)，则 \(r_i^2\bar r_i=|r_i|^2r_i\) 为非零实数，
  故 \(r_i\) 本身为实数。

因此正相关性模长
\[
\gamma_i:=\frac{|R_i|}{|z_{ij}||z_{ik}|}
=|\cos(\arg r_i)|
\]
只能取
\[
\gamma_i\in\{1,\tfrac12\};
\qquad d_i=-1\ \Longrightarrow\ \gamma_i=1.
\tag{IA.10}
\]
这并不是假设极化可取实，而是完整复返回方程强制的相位约束。
一次平移对同一行的两个分量给同一个 \(\eta_i\)，不能独立改变这两通道的比值。
本证明允许任意三个单位相位，包含合同中全部空间平移。

## 6. 共同ρ与不等长几何矛盾

对 IA.8 的两式取模并相乘，
\[
\rho^2|z_{ij}||z_{ik}|
=|C_{ij}C_{ik}|\,|z_{ij}|^2|z_{ik}|^2|R_jR_k|.
\]
全部量非零，因此
\[
\boxed{\quad
\rho^2
=\frac{|C_{ij}C_{ik}|}{\gamma_i}|R_1R_2R_3|.
\quad}
\tag{IA.11}
\]
同一个 \(\rho\) 强制三个正数
\[
P_i:=|C_{ij}C_{ik}|
\]
与 \(\gamma_i\) 成共同正比。行内交叉量的共同乘积在这里不能作为三份独立可调的幅度。

只为分析不等长频率，按标签记
\(n_\alpha<n_\beta<n_\gamma\)；
这是排序记号，不是在模板合同中新增一个轴置换。设
\[
X=n_\alpha^2<Y=n_\beta^2<Z=n_\gamma^2,
\]
\[
a=\frac{Y-X}{Y+X},\quad
b=\frac{Z-Y}{Z+Y},\quad
c=\frac{Z-X}{Z+X}.
\]
则 \(0<a,b<1\)，并由直接代数有
\[
c=\frac{a+b}{1+ab}>\max(a,b).
\tag{IA.12}
\]
例如 \(c-a=b(1-a^2)/(1+ab)>0\)，另一式同理。

提取共同正因子 \(\mathcal C=16n_1^2n_2^2n_3^2\)，准确得到
\[
P_\alpha=\mathcal C ac,\quad
P_\beta=\mathcal C ab,\quad
P_\gamma=\mathcal C bc.
\tag{IA.13}
\]
故 \(P_\beta\) 严格小于另外两者。
结合 IA.10–11，唯一可能的相关性模长是
\[
\gamma_\beta=\tfrac12,\qquad
\gamma_\alpha=\gamma_\gamma=1.
\]
于是必须
\[
P_\alpha=P_\gamma=2P_\beta,
\]
即 \(c=2b\) 且 \(c=2a\)。因此 \(a=b>0\) 且 \(c=2a\)。
但 IA.12 同时给
\[
c=\frac{2a}{1+a^2}<2a,
\]
矛盾。

证明对每个 D 仅使用它所允许的较弱条件
\(\gamma_i\in\{1,1/2\}\)；若某 \(d_i=-1\)，真实条件还更强。
因此上述统一矛盾已经排除全部八个 D，包括行共轭与反射，
无须通过遗漏某类符号矩阵来缩小合同。
各负模由实值共轭决定，所以正接收方程不可解便排除全部六模共同副本。

## 7. 接受与不接受的结论

IA.6 是完整有限恒等式，未省略 L+L 有序配对，代数余项为零。
IA.4 中的真实共轭、根投影、系数4、行内相关性和共同ρ都是障碍所必需的结构。
允许每模各自幅度、允许两通道独立相位或改变模板，会改变 IA.8–11，
不属于本合同。

本结论否定的是纯 \(2+2\) 树 \(B(B(a,a),B(a,a))\) 在固定加倍接收集合上的精确共同副本。
接收集外 F 未被置零，也没有形成 NS 不变子空间。
N、F 是给定初值的瞬时非线性算子，不是已经证明占优的正时间真实供给。
完整原方程仍保留黏性、原种子、\(1+3\)、\(3+1\) 及其它反馈；
此处没有把它们从方程删除，只是不把它们算入合同的纯 \(2+2\) 对象。

所以这不是所有不等长轴初值或所有两步机制失败。
它不排除有限正时间的黏性权重改变、混合供给参与、近似返回、
更宽支撑、不同模板或其它再生成合同。
没有统一迭代、一个固定初值的无限尺度、无限维跨代余项、有限总时间或 Clay 结论。

## 8. 实读来源与独立性

本次实际全文读取的唯一数学输入为
unequal-axis-return/CONTRACT.md，SHA256：

8bc4655cbb4ae5fecd672222d424f9b867aa79808113203367376f95315a8db4。

未读本目录 PROOF.md、HISTORY_SCOPE.md 或其它代理的推导。
合同标注的旧 R0.11 等长根门像结论在这里由 IA.3–5 自包含重算，
未将合同的历史提示冒称本轮重新实读旧原文或新颖性证据。
全部小整数、符号、复相位和比值恒等式均在本文手工展开；
工具仅用于合同读取、SHA及写本文件。没有科学程序、数值数组、选参或Git操作。
