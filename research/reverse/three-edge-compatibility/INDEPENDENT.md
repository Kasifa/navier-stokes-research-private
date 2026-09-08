# 三条活跃边的共享极化：独立标量约化与混合极化必要门

2026-09-08，PRIVATE_CORE。状态：**闭合了完整共享种子的标量恒等式、线性/非线性极化混合分支的精确几何必要条件，以及该分支完整 \(W_0\) 的条件性非零；三边相消实现性仍 OPEN，待非作者审查。**

全文读取本目录合同，使用本人已接受的完整 NC.7–9；未读本项新主稿或其他代理的新推导。全部为手工符号，工具仅用于文本和 SHA-256，没有实际参数、频率、极化或时间选择，没有科学程序、数组、数值求值、扫描、Git、额度重置或外发。本轮仅写本独占文件。

以下不是重述负实射线或幅度环。本稿给出共享种子换基后的完整标量式，并证明：按长度平方排序后，若全部混合首项为零，所有线性极化节点必位于所有非线性极化节点之前；任何跨组边都须满足一个精确的 \(\beta=0\) 几何式。更进一步，只要两类节点同时存在，每个线性接收的完整自供给行都非零。后一句证明在同一接收行取完整向量和，没有以单边非零代替总和。

## TE.1 完整对象与非退化域

固定合同的同一份三对初值，三频 \(p_i\) 为线性独立整数向量，成对非正交，\(P_i=|p_i|^2\) 两两不同；三条边全部活跃：
\[
(U_i\cdot p_j)(U_j\cdot p_i)\ne0\qquad(i\ne j).
\tag{TE.1}
\]
每个 \(U_i\ne0\) 且 \(U_i\cdot p_i=0\)，负模为共轭。点积在卷积中为复双线性，模长和投影距离才使用 Hermitian 范数。固定单位黏性、无外力和三维 \(2\pi\) 环面。

沿用完整双有序 Fourier–Leray 作用
\[
\mathfrak B(X,Y;r,s)
=-iP_{r+s}[(X\cdot s)Y+(Y\cdot r)X],
\qquad P_k=I-\frac{k\otimes k}{|k|^2}.
\]
固定有向边 \(p\leftarrow q\)，令 \(U=U_i,V=U_j,V_+=V,V_-=\bar V\)，并保留
\[
N_\sigma=\mathfrak B(U,V_\sigma;p,\sigma q),\qquad
T_\sigma=\mathfrak B(U,N_\sigma;p,p+\sigma q),
\]
\[
G_\sigma=\mathfrak B(V_{-\sigma},T_\sigma;-\sigma q,2p+\sigma q),
\quad Z=G_++G_-,
\quad C=\mathfrak B(N_+,N_-;p+q,p-q).
\tag{TE.2}
\]
因此正接收总向量是
\[
6M_{0,i}=\sum_{j\ne i}Z_{ij},\qquad
3W_{0,i}=\sum_{j\ne i}C_{ij}.
\tag{TE.3}
\]
每行先相加，负接收取完整共轭。以下没有删除任何根、反序项、相干项或投影。

在单边上记
\[
P=|p|^2,\quad Q=|q|^2,\quad c=p\cdot q\ne0,\quad
d=P-Q\ne0,\quad \Delta=PQ-c^2>0,\quad S=P+Q,
\]
\[
\lambda_\pm=S\pm2c,\quad E_\pm=4P+Q\pm4c,\quad
\Lambda=\lambda_+\lambda_->0,\quad \Omega=E_+E_->0,
\]
\[
h_\pm=\frac{Q\pm2c}{\lambda_\pm E_\pm},\quad
\alpha=2-d(h_++h_-),\quad
\beta=-d(h_+-h_-),\quad
\kappa=\frac{4cdP}{Q\Lambda},
\]
\[
H=4P^2-PQ+Q^2-4c^2,\qquad
\chi=\frac{4cd(2P+Q)H}{Q\Lambda\Omega}.
\tag{TE.4}
\]
所有这些是当前固定几何的实标量；\(\chi\) 允许为零，未在下文除以它。

## TE.2 有向正交横向基中的完整相干式

对每个有向接收 \(i\leftarrow j\)，定义两个端点各自正定向的实正交单位基：
\[
E_{ij}=\frac{p_j-(c_{ij}/P_i)p_i}{\ell_{ij}},
\quad \ell_{ij}=\sqrt{\frac{\Delta_{ij}}{P_i}},
\qquad N_{ij}=\frac{p_i}{\sqrt{P_i}}\times E_{ij}.
\tag{TE.5}
\]
因而
\[
N_{ij}=\frac{p_i\times p_j}{\sqrt{\Delta_{ij}}},
\qquad N_{ji}=-N_{ij}.
\]
写同一个种子的边坐标为
\[
U_i=a_{ij}(E_{ij}+\omega_{ij}N_{ij}),\qquad
a_{ij}=U_i\cdot E_{ij}\ne0.
\tag{TE.6}
\]
TE.1 保证所有 \(a_{ij}\) 非零；不同邻边的 \(\omega_{ij}\) 不是独立变量。

与 NC 的非单位基
\[
e=p_j-\frac cPp_i,\quad f=p_i-\frac cQp_j,\quad n=p_i\times p_j,
\quad U_i=ue+vn,\quad U_j=xf+yn
\]
逐项比较，得到
\[
u=\frac{a_{ij}}{\ell_{ij}},\qquad
\frac vu=\frac{\omega_{ij}}{\sqrt P},\qquad
x=\frac{a_{ji}}{\ell_{ji}},\qquad
\frac yx=-\frac{\omega_{ji}}{\sqrt Q}.
\tag{TE.7}
\]
发送端最后一个负号来自 \(N_{ji}=-n/\sqrt\Delta\)，它决定相干虚部的号，不能略掉。

记
\[
L_{ij}=2\left(\frac{\Delta_{ij}}{P_i}\right)^{3/2}>0,
\qquad r_{ij}=\sqrt{\frac{P_i}{P_j}}>0,
\]
\[
q_{ij}=\kappa_{ij}\omega_{ij}
-r_{ij}\alpha_{ij}\Re\omega_{ji}
+ir_{ij}\beta_{ij}\Im\omega_{ji}.
\tag{TE.8}
\]
将 TE.7 代入完整 NC.7–8，恰得
\[
\boxed{
Z_{ij}=iL_{ij}a_{ij}^2|a_{ji}|^2
\left[\chi_{ij}E_{ij}+q_{ij}N_{ij}\right].}
\tag{TE.9}
\]
例如 NC 法向相干项是 \(\alpha\Re(x\bar y)+i\beta\Im(x\bar y)\)；
由 \(y/x=-\omega_{ji}/\sqrt Q\)，其归一化实部为负而虚部为正，正是 TE.8。整体因子是 \(a_{ij}^2|a_{ji}|^2\)，没有接收相位平均。

完整 \(C\) 也可用同一单位基精确保留。设
\[
\chi^C_{ij}=\frac{2c_{ij}d_{ij}^2}{P_j\Lambda_{ij}},\qquad
\alpha^C_{ij}=\frac{2d_{ij}(P_i+P_j)}{\Lambda_{ij}},\qquad
\beta^C_{ij}=-\frac{4c_{ij}d_{ij}}{\Lambda_{ij}},
\]
\[
q^C_{ij}=\kappa_{ij}\omega_{ij}
-r_{ij}\alpha^C_{ij}\Re\omega_{ji}
+ir_{ij}\beta^C_{ij}\Im\omega_{ji}.
\]
则 NC.9 给
\[
\boxed{
C_{ij}=iL_{ij}a_{ij}^2|a_{ji}|^2
\left[\chi^C_{ij}E_{ij}+q^C_{ij}N_{ij}\right].}
\tag{TE.10}
\]
这里 \(Z,C\) 的 \(\kappa\) 相同，其余三个实系数不同；总 \(Z\) 的一个标量条件不能直接替换成总 \(C\) 的条件。

## TE.3 两个完整标量及其无丢失性

在 \(p_i^\perp\) 的复化中，定义复双线性横向行列式
\[
[X,Y]_i=\frac{p_i}{\sqrt{P_i}}\cdot(X\times Y),
\qquad J_iX=\frac{p_i}{\sqrt{P_i}}\times X.
\tag{TE.11}
\]
该式不含共轭。令 \(R_i=\sum_{j\ne i}Z_{ij}\)，定义
\[
\mathcal D_i=[U_i,R_i]_i,\qquad
\mathcal H_i=\overline U_i\cdot R_i.
\tag{TE.12}
\]
\(\mathcal H_i\) 则是 Hermitian 对偶标量。直接用
\([U_i,J_i\overline U_i]_i=\|U_i\|^2\) 以及
\(\overline U_i\cdot J_i\overline U_i=0\)，得到精确重构
\[
\boxed{
R_i=\frac{\mathcal H_i}{\|U_i\|^2}U_i
+\frac{\mathcal D_i}{\|U_i\|^2}J_i\overline U_i.}
\tag{TE.13}
\]
这不除以可能为零的复双线性 \(U_i\cdot U_i\)，所以圆极化等各分支都保留。两个右侧方向 Hermitian 正交且等长，还给
\[
\boxed{
\|R_i\|^2=\frac{|\mathcal H_i|^2+|\mathcal D_i|^2}{\|U_i\|^2},
\qquad
M_{0,i}=0\iff\mathcal D_i=\mathcal H_i=0.}
\tag{TE.14}
\]
单独 \(\mathcal D_i=0\) 仅说明 \(R_i\in\mathbb C U_i\)，不能说明 \(R_i=0\)。

TE.9 的两个局部贡献明确为
\[
\boxed{
[U_i,Z_{ij}]_i
=iL_{ij}a_{ij}^3|a_{ji}|^2
\left[(\kappa_{ij}-\chi_{ij})\omega_{ij}
-r_{ij}\alpha_{ij}\Re\omega_{ji}
+ir_{ij}\beta_{ij}\Im\omega_{ji}\right],}
\tag{TE.15}
\]
\[
\boxed{
\overline U_i\cdot Z_{ij}
=iL_{ij}a_{ij}^2\overline a_{ij}|a_{ji}|^2
\left[\chi_{ij}+\overline\omega_{ij}q_{ij}\right].}
\tag{TE.16}
\]
每个行标量必须对两个邻点完整求和。特别是 TE.15 的接收幅度为三次 \(a_{ij}^3\)，一般既非实也非正。

## TE.4 共享换基、相位和实虚部方程

固定顶点 \(i\) 的一个邻点为参考，写参考坐标 \(A_i,\omega_i\)。另一邻点给出的单位基由唯一实平面旋转联系：
\[
E'=CE+SN,\qquad N'=-SE+CN,\qquad C^2+S^2=1.
\]
因三频独立，两个邻方向不平行，故这里 \(S\ne0\)。同一个 \(U_i\) 的坐标必须满足
\[
\boxed{
a'=A_i(C+S\omega_i),\qquad
\omega'=\frac{-S+C\omega_i}{C+S\omega_i}.}
\tag{TE.17}
\]
分母非零由另一条边的活跃性支付。尤其
\[
\boxed{
\Im\omega'=\frac{\Im\omega_i}{|C+S\omega_i|^2}.}
\tag{TE.18}
\]
这给定了相邻边的极化比和投影幅度，不能只换比值却保留原幅度。

记每条边的 \(a_{ij}=A_i s_{ij}\)，其中参考边 \(s_{ij}=1\)，另一边 \(s_{ij}=C_i+S_i\omega_i\)。所有 \(\omega_{ij}\) 用 TE.17 表示，所有发送因子也必须用 \(a_{ji}=A_j s_{ji}\) 表示。于是 TE.15 的行方程等价于
\[
\boxed{
\frac{\mathcal D_i}{iA_i^3}
=\sum_{j\ne i}
L_{ij}|A_j|^2|s_{ji}|^2s_{ij}^3
(g_{ij}+ih_{ij})=0,}
\tag{TE.19}
\]
其中全为实数的两个括号系数是
\[
g_{ij}=(\kappa_{ij}-\chi_{ij})\Re\omega_{ij}
-r_{ij}\alpha_{ij}\Re\omega_{ji},
\]
\[
h_{ij}=(\kappa_{ij}-\chi_{ij})\Im\omega_{ij}
+r_{ij}\beta_{ij}\Im\omega_{ji}.
\tag{TE.20}
\]
若 \(s_{ij}=b_{ij}+it_{ij}\)，令
\[
X_{ij}=b_{ij}^3-3b_{ij}t_{ij}^2,\qquad
Y_{ij}=3b_{ij}^2t_{ij}-t_{ij}^3,\qquad
\lambda_{ij}=L_{ij}|A_j|^2|s_{ji}|^2>0.
\]
则精确实虚部条件为
\[
\boxed{
\sum_{j\ne i}\lambda_{ij}(X_{ij}g_{ij}-Y_{ij}h_{ij})=0,
\qquad
\sum_{j\ne i}\lambda_{ij}(X_{ij}h_{ij}+Y_{ij}g_{ij})=0.}
\tag{TE.21}
\]
第二个 Hermitian 标量则由 TE.16 同样求和：
\[
\boxed{
\frac{\mathcal H_i}{iA_i^2\overline A_i}
=\sum_{j\ne i}L_{ij}|A_j|^2|s_{ji}|^2
s_{ij}^2\overline s_{ij}
(\chi_{ij}+\overline\omega_{ij}q_{ij})=0.}
\tag{TE.22}
\]
TE.19、22 在三顶点同时实施时，只有同一组三个种子对应的三个参考比值和三个参考模长；没有六个独立发送协方差。

缩放也可直接核查。若 \(U_i\mapsto z_iU_i\)、\(z_i\ne0\)，则
\[
a_{ij}\mapsto z_i a_{ij},\quad\omega_{ij}\mapsto\omega_{ij},
\quad Z_{ij},C_{ij}\mapsto z_i^2|z_j|^2(Z_{ij},C_{ij}),
\]
\[
[U_i,Z_{ij}]_i\mapsto z_i^3|z_j|^2[U_i,Z_{ij}]_i,\qquad
\overline U_i\cdot Z_{ij}\mapsto
z_i^2\overline z_i|z_j|^2(\overline U_i\cdot Z_{ij}).
\tag{TE.23}
\]
因此除去参考非零因子合法，但不能除去邻边之间的 \(s_{ij}^3\) 相位。上述换基是正定向实横向换基；如果对全部空间作反射，横向行列式与有向面积均随行列式符号变号，零条件不变。

TE.21 也明确暴露一个不能由该标量单独关闭的项：非线性极化的接收端一般使 \(Y_{ij}\ne0\)，于是虚部方程包含 \(Y_{ij}g_{ij}\)，而 \(g_{ij}\) 保留发送比值的实部。它不是仅含发送有向面积的正权重和。未证明这些实相干项在三行联合下消失或有同号；删除它们就相当于改变同一接收种子。故目前不能从行列式虚部直接推出“三种子必全线性”，更不能由三个行列式为零推出全部向量为零。

## TE.5 基不变的极化面积与线性接收刚性

定义每个原种子的实有向极化面积
\[
\mathfrak h_i=
i\frac{p_i}{\sqrt{P_i}}\cdot(U_i\times\overline U_i)
=2|a_{ij}|^2\Im\omega_{ij}\in\mathbb R.
\tag{TE.24}
\]
TE.18 保证它与邻边无关，且缩放时
\(\mathfrak h_i\mapsto|z_i|^2\mathfrak h_i\)。实部、虚部均在二维实横向平面内，故
\[
\boxed{
\mathfrak h_i=0
\iff U_i\text{ 是非零复标量乘非零实横向向量}.}
\tag{TE.25}
\]
这就是线性极化；本稿称 \(\mathfrak h_i\ne0\) 为非线性极化，不附加螺旋纯度假设。还可写
\(|\mathfrak h_i|\le\|U_i\|^2\)，因为 \(2|\Im\omega|\le1+|\omega|^2\)。

现在只假定接收 \(i\) 线性极化，写 \(U_i=z_iR_i^{\rm real}\)，其中 \(R_i^{\rm real}\) 是非零实横向向量。为避免与 TE.12 总和混淆，以下用 \(u_{ij}^{\rm real}\) 表示这个实代表在 NC 基 \(e_{ij}\) 上的坐标。所有 \(u_{ij}^{\rm real}\ne0\)。

发送端在同一 NC 基中的
\[
I_{ji}=\Im(x_{ji}\overline y_{ji})
=\frac{\sqrt{P_j}}{2\Delta_{ij}}\,\mathfrak h_j.
\tag{TE.26}
\]
接收实代表的 \(u,v\) 都实，故 NC.7–8 在去掉共同接收因子 \(z_i^2\) 后，实部只有完整相干虚部项：
\[
\boxed{
\Re\left(z_i^{-2}\sum_{j\ne i}Z_{ij}\right)
=-\sum_{j\ne i}
\frac{\Delta_{ij}^2(u_{ij}^{\rm real})^2}
{P_i^2\sqrt{P_j}}\,
\beta_{ij}\mathfrak h_j\,n_{ij}.}
\tag{TE.27}
\]
这里 \(n_{ij}=p_i\times p_j\) 为非单位法向。两个 \(n_{ij}\) 在实 \(p_i^\perp\) 中线性独立：若其线性组合为零，叉积之前的邻频组合必平行于 \(p_i\)，与三频独立性矛盾。

TE.27 的其它系数严格正。因此这是完整行的必要条件：
\[
\boxed{
M_{0,i}=0,\ \mathfrak h_i=0
\quad\Longrightarrow\quad
\beta_{ij}\mathfrak h_j=0
\quad\text{对两个邻点各自成立}.}
\tag{TE.28}
\]
此处用的是整个行向量的实部与两个独立方向，而不是只用一个行列式。它没有把两个相干项取绝对值，也没有为不同邻边重新定相；去除的是同一个 \(z_i^2\)。

## TE.6 \(\beta=0\) 的精确几何域

从 TE.4 通分可手核
\[
h_+-h_-=
\frac{4c[4P^2-PQ-2Q^2+8c^2]}{\Lambda\Omega}.
\]
因此
\[
\boxed{
\beta=-\frac{4cd}{\Lambda\Omega}\,\mathcal K(P,Q,c),
\qquad
\mathcal K(P,Q,c)=4P^2-PQ-2Q^2+8c^2.}
\tag{TE.29}
\]
通分依据为
\(\lambda_\pm E_\pm=(P+Q)(4P+Q)+8c^2\pm6(2P+Q)c\)；
取差后分子恰为上式，未运行符号程序。

若 \(P\ge Q\)，令 \(d=P-Q\ge0\)，则
\[
\mathcal K=Q^2+7Qd+4d^2+8c^2>0.
\]
当前长度不同，所以当接收更长时必有 \(\beta\ne0\)。在全非正交、不同长度、非平行域内，
\[
\boxed{\beta=0\iff
8c^2=-4P^2+PQ+2Q^2.}
\tag{TE.30}
\]
这一等式与 \(c^2>0,\Delta>0\) 相容的准确长度域为
\[
\boxed{
\frac Q4<P<\frac{1+\sqrt{33}}8\,Q<Q.}
\tag{TE.31}
\]
证明：在 TE.30 上，
\[
\Delta=\frac{(4P-Q)(P+2Q)}8,
\]
故 \(\Delta>0\iff P>Q/4\)；同时 \(c^2>0\) 等价于
\(4(P/Q)^2-(P/Q)-2<0\)，其正根是 \((1+\sqrt{33})/8<1\)。
反过来，该开区间和 TE.30 保证当前所需的正性、不同长度和非正交。它只描述两频实几何的符号域，不保证合同的同一整数三频可以同时实现各条等式。

特别地，TE.30 上还有
\[
H=\frac{3P(4P-Q)}2>0.
\tag{TE.32}
\]
所以在当前活跃域 \(\chi\ne0\)，完整 \(Z\) 的平面分量仍非零。\(\beta=0\) 不是不活跃边、不是完整 \(Z=0\)，也不是此前要求 \(H=0\) 的单向混合零门。

## TE.7 三节点共同极化的闭合分类门

仅作标签排序，写 \(P_1<P_2<P_3\)。令
\[
\mathcal L=\{i:\mathfrak h_i=0\},\qquad
\mathcal E=\{i:\mathfrak h_i\ne0\}.
\]
假设完整三行 \(M_0=0\)。对每个 \(i\in\mathcal L,j\in\mathcal E\)，TE.28 强制 \(\beta_{ij}=0\)，TE.31 又强制 \(P_i<P_j\)。因此
\[
\boxed{\text{每个线性极化节点都比每个非线性极化节点短。}}
\tag{TE.33}
\]
所以可能的节点类型只剩下：

| 线性极化节点集合 | 必须额外满足的跨组几何 |
|---|---|
| 空集 | 本引理无额外结论；三个种子都非线性极化 |
| \(\{1\}\) | \(\mathcal K(P_1,P_2,c_{12})=\mathcal K(P_1,P_3,c_{13})=0\) |
| \(\{1,2\}\) | \(\mathcal K(P_1,P_3,c_{13})=\mathcal K(P_2,P_3,c_{23})=0\) |
| \(\{1,2,3\}\) | 三者都线性极化；仍须核全部实向量相消 |

每个零 \(\mathcal K\) 都保留 TE.30–31 的完整开域。此表只是必要模式，不声称其中任何一行有同一组三对解。

几个直接后果是：最长种子若线性极化，则三者全线性；只有一个线性种子时它必最短；只有一个非线性种子时它必最长。还可用一条频率条件排除所有混合极化模式：
\[
\boxed{
\mathcal K(P_1,P_3,c_{13})\ne0,\ M_0=0
\quad\Longrightarrow\quad
\text{三者全线性或三者全非线性}.}
\tag{TE.34}
\]
如果最短—最长的这条 \(\mathcal K\) 为零，也仍须上表另一条跨组等式及所有剩余向量方程，不能把它视为足够条件。

## TE.8 混合极化分支的完整 \(W_0\) 非零

与 TE.27 相同地，接收 \(i\) 线性极化时，从完整 NC.9 取去共同因子后的实部，得到
\[
\boxed{
\Re\left(z_i^{-2}\sum_{j\ne i}C_{ij}\right)
=\sum_{j\ne i}
\frac{4c_{ij}d_{ij}\Delta_{ij}^2(u_{ij}^{\rm real})^2}
{P_i^2\sqrt{P_j}\Lambda_{ij}}\,
\mathfrak h_j\,n_{ij}.}
\tag{TE.35}
\]
核号可直接看 NC 法向项中的
\(4i\,Q(-2icI)=8cQ I\)，然后使用 TE.26。
当前每条边的 \(c_{ij},d_{ij},u_{ij}^{\rm real}\) 均非零；两个法向仍独立。因此
\[
\boxed{
\mathfrak h_i=0
\quad\Longrightarrow\quad
\sum_{j\ne i}C_{ij}=0
\ \text{只可能在两个邻点均线性极化时发生}.}
\tag{TE.36}
\]
等价地，只要该线性接收有任一非线性邻点，它的完整 \(C\) 行必非零。TE.36 不是反向充分性：两个邻点都线性时，总 \(C\) 仍可非零。

三边图中，只要 \(\mathcal L,\mathcal E\) 都非空，每个线性顶点都接到至少一个非线性顶点，故
\[
\boxed{
\mathcal L\ne\varnothing,\ \mathcal E\ne\varnothing
\quad\Longrightarrow\quad W_{0,i}\ne0\ (i\in\mathcal L),
\quad W_0\ne0.}
\tag{TE.37}
\]
此结论本身甚至不需要 \(M_0=0\)；如果混合极化分支后来确实实现了 \(M_0=0\)，则 \(W_0\ne0\) 已由完整线性接收行保证。它不依赖中心或某条边的非零替代总和，也不依赖不同接收之间的范数估计。实际存在性仍完全未由此支付。

## TE.9 剩余系统与边界

已闭合的新结果是 TE.13–23 的无丢失共享标量式、TE.28–34 的混合极化几何必要门，以及 TE.35–37 的完整行非零。三行仍须同时满足 TE.19、22；只满足三个行列式、节点排序或零 \(\beta\) 等式都不够。

全线性分支、全非线性分支，以及上表保留下来的两个混合分支，均没有在本轮证明存在或无解。对于全非线性分支，TE.21 中实相干量与接收三次相位的混合项仍是准确的未闭合项；对于全线性分支，去相位后的完整实向量相消仍未支付。混合分支虽然条件下 \(W_0\ne0\) 已闭合，跨组几何与剩余三个完整行是否能由同一整数三频、同一三个种子同时实现仍 OPEN。

本稿全部结论只收窄完整短时系数 \(M_0,W_0\)。没有将 \(M_0=0\) 当作任意正时间混合项为零，没有声称模板返回或两步再生成；本轮不新增真实原解短窗结论。若以后需要从这些系数接到原解，仍须调用已接受 SOURCE_BRIDGE 的同一数据全 Fourier 余项并支付相应严格间隙。统一迭代、同一固定初值无限尺度、跨代无限维误差与有限总时间均未支付。NO-CANDIDATE ACCEPTED；NOT CLAY。

## 实际来源与最终字节

| 来源 | 实读范围及用途 | SHA-256 |
|---|---|---|
| three-edge-compatibility/CONTRACT.md | 本轮全文 | 51909466ff2baf93b83d419775b0fbd2f1ceff4dec59c785358401d80ff01143 |
| net-mixed-cancellation/INDEPENDENT.md | 本人此前完整推导、自核并已接受的最终稿；本轮实际重读第 1–150 行，使用 NC.1–10 的完整作用、\(Z,C\) 和缩放 | 25111397d32eef2751a91b1ad1ab6a446794742874b97bf6b0b73b3964d11a58 |

没有把来源内部引用的其它文件记为本轮实读，没有新增外部定理或文献新颖性声明。以上源哈希已实际核对。本文自身哈希在最终写入、全文自核后单独提供；最终审查须绑定该实际字节。
