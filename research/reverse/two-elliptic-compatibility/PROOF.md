# 最短线性接收的完整消元与原方向条件

2026-09-08，PRIVATE_CORE。状态：**完成最低完整 \(Z\) 行的唯一实部消元，并得到最低完整 \(C\) 行沿原种子复方向的精确充要条件；本轮未证明三频实例或其余接收行可解，待独立推导和非作者审查。**

全文读取本目录合同，直接以两条 \(\beta=0\) 几何式作为假设，从已接受 NC.7–9 手工推导。本稿不重开已关闭的“两种子线性”类型。没有实际频率、极化、幅度或时间选择，没有科学程序、数组、数值求值、扫描、Git、额度重置或外发；本轮只写本独占文件。

本次结果不是单边或逐边取模判断。最低行的两个发送实比值由同一个实接收方向与实际发送投影模方唯一决定；发送面积仍非零且未进入该 \(Z\) 实部消元。最低 \(C\) 的原方向条件则另有一个面积比约束和一个实方向方程，二者缺一不可。

## TL.1 同一数据与完整来源

记最短频率 \(p=p_0\)，两个发送频率为 \(q_j=p_j\)，其中
\[
P=|p|^2<Q_1=|q_1|^2<Q_2=|q_2|^2,\quad
c_j=p\cdot q_j\ne0,\quad d_j=P-Q_j<0,\quad
\Delta_j=PQ_j-c_j^2>0.
\]
三频为线性独立整数向量，全部频率对非正交且三条边活跃；负模保持同一原种子的共轭。固定单位黏性、无外力、三维 \(2\pi\) 环面。

合同直接假设
\[
\boxed{
8c_j^2=-4P^2+PQ_j+2Q_j^2,\qquad
\frac{Q_j}4<P<\frac{1+\sqrt{33}}8Q_j<Q_j.}
\tag{TL.1}
\]
这些假设不保证实际整数三频可以同时实现。

完整双有序 Fourier–Leray 作用为
\[
\mathfrak B(X,Y;r,s)
=-iP_{r+s}[(X\cdot s)Y+(Y\cdot r)X],
\qquad P_k=I-\frac{k\otimes k}{|k|^2}.
\]
对每个最低接收边，\(V_+=U_j,V_-=\bar U_j\)，仍定义
\[
N_\sigma=\mathfrak B(U_0,V_\sigma;p,\sigma q_j),\quad
T_\sigma=\mathfrak B(U_0,N_\sigma;p,p+\sigma q_j),
\]
\[
G_\sigma=\mathfrak B(V_{-\sigma},T_\sigma;-\sigma q_j,2p+\sigma q_j),
\quad Z_{0j}=G_++G_-,
\]
\[
C_{0j}=\mathfrak B(N_+,N_-;p+q_j,p-q_j).
\tag{TL.2}
\]
所以 \(6M_{0,0}=Z_{01}+Z_{02}\)、\(3W_{0,0}=C_{01}+C_{02}\)。下文的每个行条件都在这个完整向量和上实施。

## TL.2 \(\beta=0\) 上的全部所需实系数

暂省 \(j\)，沿用 NC 的
\[
\lambda_\pm=P+Q\pm2c,\quad E_\pm^{\rm freq}=4P+Q\pm4c,\quad
\Lambda=\lambda_+\lambda_-,\quad\Omega=E_+^{\rm freq}E_-^{\rm freq},
\]
\[
h_\pm=\frac{Q\pm2c}{\lambda_\pm E_\pm^{\rm freq}},\quad
\alpha=2-d(h_++h_-),\quad\beta=-d(h_+-h_-),
\]
\[
\kappa=\frac{4cdP}{Q\Lambda},\quad
H=4P^2-PQ+Q^2-4c^2,\quad
\chi=\frac{4cd(2P+Q)H}{Q\Lambda\Omega}.
\]
TL.1 直接给
\[
\Lambda=\frac32P(2P+Q),\qquad
\Omega=3(4P-Q)(2P+Q),\qquad
H=\frac32P(4P-Q)>0,
\]
\[
\Delta=\frac{(4P-Q)(P+2Q)}8,\qquad
h_+=h_-=\frac1{3(2P+Q)}.
\tag{TL.3}
\]
最后一个式子可直接核：TL.1 上
\(\lambda_\pm E_\pm^{\rm freq}=3(2P+Q)(Q\pm2c)\)。
且 \(c^2<Q^2/4\) 由 \(P>Q/4\) 保证，所以两个被约去的 \(Q\pm2c\) 均非零。

因此
\[
\boxed{
\beta=0,\quad
\alpha=\frac{2(5P+4Q)}{3(2P+Q)}>0,\quad
\chi=\frac{4cd}{3Q(2P+Q)}\ne0,\quad
\kappa=2\chi.}
\tag{TL.4}
\]
\(\chi,\kappa\) 的符号为 \(cd\)，这里 \(d<0\)；没有假定两条通道同号。

为了同时保留 \(C\)，定义其单位基系数
\[
\chi^C=\frac{2cd^2}{Q\Lambda},\quad
\alpha^C=\frac{2d(P+Q)}{\Lambda},\quad
\beta^C=-\frac{4cd}{\Lambda}.
\]
在 TL.1 上恰为
\[
\boxed{
\chi^C=\frac{4cd^2}{3PQ(2P+Q)}
=\frac dP\chi,\quad
\alpha^C=\frac{4d(P+Q)}{3P(2P+Q)},\quad
\beta^C=-\frac{8cd}{3P(2P+Q)}
=-\frac{2Q}P\chi.}
\tag{TL.5}
\]
它们均非零。尤其 \(\beta=0\) 并没有使 \(C\) 的相干虚部系数 \(\beta^C\) 为零。

## TL.3 一个共同实接收方向与两个完整发送比值

写最低种子为
\[
U_0=z_0R,\qquad z_0\ne0,\quad R\in p^\perp\cap\mathbb R^3,\quad R\ne0.
\tag{TL.6}
\]
每条边使用正定向单位基
\[
E_j=\frac{q_j-(c_j/P)p}{\ell_j},\quad
\ell_j=\sqrt{\Delta_j/P},\qquad
N_j=\frac p{\sqrt P}\times E_j
=\frac{p\times q_j}{\sqrt{\Delta_j}},
\]
\[
F_j=\frac{p-(c_j/Q_j)q_j}{\sqrt{\Delta_j/Q_j}},
\qquad \widetilde N_j=\frac{q_j}{\sqrt{Q_j}}\times F_j=-N_j.
\tag{TL.7}
\]
发送种子保持完整复比值：
\[
U_j=\mathcal A_j(F_j+\eta_j\widetilde N_j),\quad
\eta_j=\xi_j+i\tau_j,\quad
\mathcal A_j\ne0,\quad \xi_j,\tau_j\in\mathbb R,\quad\tau_j\ne0.
\tag{TL.8}
\]
其有向极化面积为
\[
\mathfrak h_j=
i\frac{q_j}{\sqrt{Q_j}}\cdot(U_j\times\bar U_j)
=2|\mathcal A_j|^2\tau_j\ne0.
\tag{TL.9}
\]
这记录了发送协方差的实、虚相干，而非仅两个强度。TL.8 的一个复向量也同时决定该发送种子在另一个邻边的坐标；本稿不再为其另设独立种子。

记最低实代表的实际边投影
\[
x_j=R\cdot E_j\ne0,\qquad y_j=R\cdot N_j.
\]
这里 \(x_j\) 是本稿的实接收投影，不是 NC 的发送坐标。若 NC 发送坐标记为 \(x_j^{\rm NC},y_j^{\rm NC}\)，则
\[
x_j^{\rm NC}=\mathcal A_j\sqrt{Q_j/\Delta_j},\qquad
\frac{y_j^{\rm NC}}{x_j^{\rm NC}}=-\frac{\eta_j}{\sqrt{Q_j}}.
\tag{TL.10}
\]
发送端法向的负号被明确保留。

定义实系数
\[
L_j=2(\Delta_j/P)^{3/2}>0,\qquad
\theta_j=L_j|\mathcal A_j|^2\chi_j\ne0,
\]
\[
\gamma_j=\frac{\sqrt{P/Q_j}\,\alpha_j}{\chi_j}
=\frac{\sqrt{PQ_j}(5P+4Q_j)}{2c_jd_j}\ne0,\qquad
t_j=\gamma_j\xi_j.
\tag{TL.11}
\]
从完整 NC.7–8 直接代入 TL.4、7–10 后，最低行的每条贡献恰为
\[
\boxed{
\frac{Z_{0j}}{iz_0^2}
=\theta_j
\left[x_j^2E_j+(2x_jy_j-t_jx_j^2)N_j\right].}
\tag{TL.12}
\]
这里 \(\tau_j\ne0\) 仍属于同一发送种子，只因当前 \(\beta=0\) 没出现在这一个 \(Z\) 式子里；没有把发送线性化。

## TL.4 最低完整 \(Z\) 行的唯一实部解

设
\[
\mathsf C=E_1\cdot E_2,\qquad
\mathsf S=N_1\cdot E_2,\qquad
\mathsf C^2+\mathsf S^2=1,\quad\mathsf S\ne0.
\]
三频独立保证 \(\mathsf S\ne0\)，允许 \(\mathsf C=0\)。令
\[
a=R\cdot E_1,\qquad b=R\cdot E_2,\qquad
\rho=b/a\in\mathbb R\setminus\{0\},\qquad
w=\theta_2/\theta_1\in\mathbb R\setminus\{0\}.
\tag{TL.13}
\]
活跃性给 \(a,b\ne0\)，且
\[
y_1=(b-\mathsf Ca)/\mathsf S,\qquad
y_2=(\mathsf Cb-a)/\mathsf S.
\tag{TL.14}
\]
其中
\[
\operatorname{sgn}w=\operatorname{sgn}(c_1c_2)
\tag{TL.15}
\]
由两个 \(d_j<0\) 及其它正因子得到；不能把 \(w\) 默认为正。

TL.12 的总和为零，对 \(E_2,E_1\) 分别点乘，精确得到
\[
0=\theta_1(2ab-\mathsf Ca^2-\mathsf S t_1a^2)+\theta_2b^2,
\]
\[
0=\theta_1a^2+\theta_2(2ab-\mathsf Cb^2+\mathsf S t_2b^2).
\tag{TL.16}
\]
两个实泛函独立，故这两式等价于完整最低向量和为零。解为
\[
\boxed{
t_1=\frac{2\rho-\mathsf C+w\rho^2}{\mathsf S},\qquad
t_2=\frac{\mathsf C-2/\rho-1/(w\rho^2)}{\mathsf S}.}
\tag{TL.17}
\]
因此两个发送比值实部的完整唯一解是
\[
\boxed{\xi_j=t_j/\gamma_j,\qquad
\Re\!\left(\frac{y_j^{\rm NC}}{x_j^{\rm NC}}\right)
=-\frac{t_j}{\sqrt{Q_j}\gamma_j}.}
\tag{TL.18}
\]
没有未处理的线性系统降秩：未知实部在 TL.12 中分别乘两个独立 \(N_j\)，其系数
\(-\theta_j\gamma_jx_j^2\) 均非零。TL.17 的分母也全部非零；分子为零只给允许的 \(\xi_j=0\)，不要求 \(\tau_j=0\)。

所以对于一份给定的合同几何、共同实 \(R\) 和实际非零发送投影 \(\mathcal A_j\)，最低 \(Z\) 行为零恰要求 TL.17–18；两个 \(\tau_j\) 仍保留为非零实量。这是最低行的条件充分性，不证明给定的原种子必满足这些式子，更不证明两个较高行同时为零。

## TL.5 最低完整 \(C\) 行的两个独立方向条件

记
\[
\lambda_j=d_j/P<0,\quad
s_j=(P+Q_j)/P>0,\quad
\nu_j=\frac{2d_j}{5P+4Q_j}<0,\quad
m_j=s_j\nu_j.
\tag{TL.19}
\]
把完整 NC.9 和 TL.5 代入同一单位基，有
\[
\boxed{
\frac{C_{0j}}{iz_0^2}
=\theta_j\left[
\lambda_jx_j^2E_j+
\left(2x_jy_j-m_jt_jx_j^2
-2i\sqrt{Q_j/P}\,\tau_jx_j^2\right)N_j\right].}
\tag{TL.20}
\]
这里 \(m_j=\alpha_j^C/\alpha_j\)，且
\(\sqrt{P/Q_j}\,\beta_j^C/\chi_j=-2\sqrt{Q_j/P}\)；
后者直接核定了发送面积项的系数与号。

因此定义两个实向量
\[
V_{\rm re}=2\sum_{j=1}^2
\theta_j\sqrt{Q_j/P}\,\tau_jx_j^2N_j,
\]
\[
V_{\rm im}=\sum_{j=1}^2\theta_j
\left[\lambda_jx_j^2E_j+(2x_jy_j-m_jt_jx_j^2)N_j\right],
\]
便有
\[
z_0^{-2}(C_{01}+C_{02})=V_{\rm re}+iV_{\rm im}.
\tag{TL.21}
\]
两个 \(N_j\) 实线性独立，各个面积系数均非零，故 \(V_{\rm re}\ne0\)。最低完整 \(C\) 行因此始终非零，不能被同一行另一边消掉。

定义双线性横向行列式
\([X,Y]=(p/\sqrt P)\cdot(X\times Y)\)。
由于 \(R\) 是非零实向量，
\[
\boxed{
C_{01}+C_{02}\in\mathbb C U_0
\iff [R,V_{\rm re}]=[R,V_{\rm im}]=0.}
\tag{TL.22}
\]
这恰是实部与虚部都沿同一 \(R\)，不能只检查其中一个。

面积部分给
\[
[R,V_{\rm re}]
=2\sum_j\theta_j\sqrt{Q_j/P}\,\tau_jx_j^3,
\]
所以其完整充要条件为
\[
\boxed{
\frac{\tau_2}{\tau_1}
=-\frac{\sqrt{Q_1/Q_2}}{w\rho^3}.}
\tag{TL.23}
\]
右侧非零，故该式保持两个面积都非零。等价的基不变面积式是
\[
\boxed{
\frac{\mathfrak h_2}{\mathfrak h_1}
=-\frac{L_1\chi_1\sqrt{Q_1}}
{L_2\chi_2\sqrt{Q_2}\,\rho^3}.}
\tag{TL.24}
\]
这是实际发送面积的约束，不是强度平均。

另一方面，利用 \([R,E_j]=-y_j\)、\([R,N_j]=x_j\)，有
\[
\boxed{
[R,V_{\rm im}]
=\sum_j\theta_js_jx_j^2(y_j-\nu_jt_jx_j).}
\tag{TL.25}
\]
其中 \(2-\lambda_j=s_j\)、\(m_j=s_j\nu_j\)。TL.25 仍保留最低 \(Z\) 行解出的发送实相干，不能从 TL.23 自动推出。

## TL.6 代入后的实方向式及完整零系数分支

定义只由两条长度比决定的实系数
\[
\mathsf A_j=s_j(1-\nu_j)
=\frac{3(P+Q_j)(P+2Q_j)}{P(5P+4Q_j)}>0,
\]
\[
\mathsf B_j=s_j\nu_j
=\frac{2(P^2-Q_j^2)}{P(5P+4Q_j)}<0,
\]
\[
D_*=\mathsf B_2-\mathsf B_1,\qquad
\mathsf L=\mathsf A_1+D_*,\qquad
\mathsf M=\mathsf A_2-D_*.
\tag{TL.26}
\]
在当前 \(Q_1<Q_2<4P\) 下，
\[
\boxed{D_*<0,\quad \mathsf L>0,\quad\mathsf M>0,\quad
0<\frac{\mathsf L\mathsf M}{\mathsf A_1\mathsf A_2}<1.}
\tag{TL.27}
\]
这些正性可全手核。令 \(r_j=Q_j/P\)，则 \(1<r_1<r_2<4\)，
\[
\mathsf B_2-\mathsf B_1
=-\frac{2(r_2-r_1)[5(r_1+r_2)+4+4r_1r_2]}
{(5+4r_1)(5+4r_2)}<0.
\]
又有
\[
\mathsf A(r)-2=\frac{(r-1)(6r+7)}{5+4r}>0,\quad
\mathsf B(r)+2=\frac{2[6+r(4-r)]}{5+4r}>0.
\]
因此 \(\mathsf L=\mathsf A_1+\mathsf B_2-\mathsf B_1>0\)，
\(\mathsf M>0\)。由 \(\mathsf A_j+\mathsf B_j=1+r_j\)，
\(\mathsf A_2-\mathsf A_1=(r_2-r_1)-D_*>0\)，从而
\[
\mathsf L\mathsf M
=\mathsf A_1\mathsf A_2+
D_*(\mathsf A_2-\mathsf A_1)-D_*^2
<\mathsf A_1\mathsf A_2.
\]

将 TL.14、17 代入 TL.25 并保持同一个 \(a,b\)，得到
\[
\boxed{
[R,V_{\rm im}]=\frac{\theta_1a^3}{\mathsf S}\,\Psi(\rho,w),}
\]
\[
\boxed{
\Psi(\rho,w)
=w\mathsf A_2\mathsf C\rho^3
-w\mathsf M\rho^2+\mathsf L\rho-\mathsf A_1\mathsf C.}
\tag{TL.28}
\]
供逐项核查，代入前的无合并括号为
\[
\begin{aligned}
\Psi={}&s_1[(1-2\nu_1)\rho-(1-\nu_1)\mathsf C-\nu_1w\rho^2]\\
&+ws_2\rho^2[(1-\nu_2)\mathsf C\rho+(2\nu_2-1)+\nu_2/(w\rho)].
\end{aligned}
\tag{TL.29}
\]
合并后依次给 \(w\mathsf A_2\mathsf C\)、\(-w\mathsf M\)、\(\mathsf L\)、\(-\mathsf A_1\mathsf C\) 四个系数。

对于实际给定的 \(\rho,w\)，最低实方向条件就是 \(\Psi(\rho,w)=0\)。
若按 \(w\) 消元，设
\[
\mathcal N(\rho)=\mathsf A_1\mathsf C-\mathsf L\rho,\qquad
\mathcal D(\rho)=\rho^2(\mathsf A_2\mathsf C\rho-\mathsf M).
\tag{TL.30}
\]
所有分支如下，仍须保留 \(w\ne0\) 和 TL.15 的实际符号：

- 若 \(\mathcal D\ne0\)，则恰需 \(w=\mathcal N/\mathcal D\)。若同时 \(\mathcal N=0\)，它给 \(w=0\)，与当前非零发送投影矛盾，故该子分支无解。
- 若 \(\mathcal D=0,\mathcal N\ne0\)，则实方向条件无解。
- 若 \(\mathcal D=\mathcal N=0\)，则这个实方向条件对任何实际非零 \(w\) 都成立，但其它条件不消失。该分支恰要求
\[
\boxed{
\mathsf C\ne0,\qquad
\rho=\frac{\mathsf M}{\mathsf A_2\mathsf C},\qquad
\mathsf C^2=\frac{\mathsf L\mathsf M}{\mathsf A_1\mathsf A_2}.}
\tag{TL.31}
\]

TL.27 表明 TL.31 的右侧位于 \((0,1)\)，因此不能仅凭投影独立性 \(|\mathsf C|<1\) 把这个零系数分支删除；是否与合同的全部原频率几何同时实现仍未证明。

若 \(\mathsf C=0\)，TL.28 的三次项和常数项同时消失，但 \(\rho\ne0\)，剩余式精确给
\[
\boxed{\rho=\frac{\mathsf L}{w\mathsf M}.}
\tag{TL.32}
\]
这里 \(\mathcal D=-\mathsf M\rho^2\ne0\)，无额外降秩。若再满足 TL.23，则 \(\tau_2/\tau_1<0\)，即两个发送面积异号。这是投影方向正交的子情形，原三对频率仍按合同非正交。

也可使用吸收实际接收投影平方后的权重比
\[
\mathfrak r=w\rho^2=
\frac{\theta_2(R\cdot E_2)^2}{\theta_1(R\cdot E_1)^2}.
\]
TL.28 完全等价于更短的式子
\[
\boxed{
(\mathfrak r\mathsf A_2\mathsf C+\mathsf L)\rho
=\mathfrak r\mathsf M+\mathsf A_1\mathsf C.}
\tag{TL.33}
\]
它对 \(\mathfrak r,\rho\) 分别为一次；但 \(\mathfrak r=w\rho^2\) 必须同时保留，改变共同接收方向时不能将其当作原发送幅度比不变。TL.30–31 已处理相同关系的零分母分支，没有因这种规范转换增加自由变量。

## TL.7 最低行的准确充要接口与范围

在合同几何、共同实 \(R\)、非零实际 \(\mathcal A_1,\mathcal A_2\) 及两非零发送面积的固定坐标描述下，以下是最低行的精确条件：
\[
\boxed{
Z_{01}+Z_{02}=0
\iff \xi_j=t_j/\gamma_j\text{，其中 }t_j\text{ 由 TL.17 给出}.}
\tag{TL.34}
\]
在此基础上，
\[
\boxed{
C_{01}+C_{02}\in\mathbb C U_0
\iff
\Psi(\rho,w)=0
\ \text{且}\ 
\tau_2/\tau_1=-\sqrt{Q_1/Q_2}/(w\rho^3).}
\tag{TL.35}
\]
这是最低行的条件充分性也是必要性。若两式满足，TL.21 的非零 \(V_{\rm re}\) 保证完整 \(C\) 行非零，因此得到的是一个非零原方向输出；不是零向量也被算作模板成功。发送面积关系右侧非零，所以此接口不会把任一发送种子变为线性极化。

这些式子给出实际可核的最低行条件，未实例化任何频率或原种子。一个非零面积发送种子在其二维实横向平面内的实部、虚部独立，所以它与任一非平行实频率的投影点积不能为零；然而最低实接收的两条活跃性仍须保持 \(a,b\ne0\)。式中同一发送种子在其它邻边的坐标已经由该向量决定，不能以后另行自由选择。

本稿未证明 \(\Psi=0\)、面积比、合同整数几何及两个较高接收的完整 \(M_0\) 行能同时实现，也未证明其无解。若最低行接口成立，另外两行、其它原方向条件和再生成仍完全未付。已知或本稿直接证明的 \(W_{0,0}\ne0\) 不代替方向式 TL.35，更不等于全模板合格。

边界均已保留：\(\xi_j=0\)、实接收法向分量为零、\(\mathsf C=0\)、任意允许 \(w\) 符号、消元分母为零及发送面积异号。真正作为分母的 \(\chi_j,\gamma_j,\theta_j,a,b,\mathsf S,w\) 非零均由当前域支付；\(\tau_j\) 的两个非零值没有被平均或删除。

全部结论只属于完整有限空间首项。本轮不新增真实原解时间、模板返回或跨代误差结论；若以后连接真实原解，必须另行明确调用同一数据 SOURCE_BRIDGE 预算。没有实际候选、统一迭代、同一初值无限尺度、有限总时间、奇性或全局正则性结论。EXACT LOWEST-ROW CONDITIONS ONLY；NO-CANDIDATE ACCEPTED；NOT CLAY。

## 实际来源与字节

| 来源 | 本轮实际阅读与用途 | SHA-256 |
|---|---|---|
| two-elliptic-compatibility/CONTRACT.md | 全文；两条几何作为直接假设，最低行范围 | ee05b39370f178cac5aebcf3c3046478c848c74b0078ee26edafb3282029ad52 |
| net-mixed-cancellation/INDEPENDENT.md | 本人此前完整推导、自核的已接受最终稿；本轮重读第 44–119 行，使用 NC.4–10 的完整相干 \(Z,C\)、坐标及缩放 | 25111397d32eef2751a91b1ad1ab6a446794742874b97bf6b0b73b3964d11a58 |

TL.3–35 为本轮手工核算；TL.33 作为吸收投影平方的等价规范由 TL.28 直接代数核对，不替换原始 \(w\) 定义。未新增外部定理或文献新颖性声明，没有冒记其它来源为实读。源哈希已实际核对；本文自身最终哈希在全文自核停改后提供。
