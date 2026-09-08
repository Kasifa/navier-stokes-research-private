# 三对总混合相消门：独立零判据、活跃图与剩余域

2026-09-08，PRIVATE_CORE。状态：**得到闭合的双向单对障碍、总相消必要结构与形状固定后的精确幅度相容门；一般三对存在性仍 OPEN，待非作者全文审查。**

完整读取本目录 `CONTRACT.md`，沿用本人已全文推导、自核并核对当前字节的 `MIXED_ROOT_INDEPENDENT.md` 与 `SOURCE_BRIDGE_INDEPENDENT.md`。未读本项目主稿或其他代理本项输出。全部手工符号；未运行科学程序、计算数组、数值求值、扫描、Git、额度重置或外发。本项仅写本独占文件。

实际结果不以单边非零替代总和。一个关键闭合结论是：**同一对种子的两个接收方向若都没有混合首项，则两个方向的自供给首项也都为零。** 因而全三对的 \(M_0=0,W_0\ne0\) 若可实现，必有某个接收模发生两条非零混合向量的真实相消。下文进一步给出受限星形分支和一般闭环的准确剩余条件；没有声称这些条件已有同一组三对解。

## NC.1 完整根与总向量

固定合同的同一组三个线性独立整数频率 \(p_i\) 及非零复横向种子 \(U_i\)，负模严格共轭。本稿不预设长度互异。定义完整双有序作用
\[
\mathfrak B(X,Y;r,s)
=-iP_{r+s}[(X\cdot s)Y+(Y\cdot r)X],
\qquad P_k=I-\frac{k\otimes k}{|k|^2}.
\tag{NC.1}
\]
点积为复双线性点积，所有投影保留。固定接收 \(p=p_i\)、发送 \(q=p_j\)，令 \(U=U_i\)、\(V_+=V=U_j\)、\(V_-=\overline V\)，并写
\[
N_\sigma=\mathfrak B(U,V_\sigma;p,\sigma q),
\]
\[
T_\sigma=\mathfrak B(U,N_\sigma;p,p+\sigma q),
\]
\[
G_\sigma=\mathfrak B(V_{-\sigma},T_\sigma;-\sigma q,2p+\sigma q),
\qquad \sigma=\pm1,
\]
\[
C=\mathfrak B(N_+,N_-;p+q,p-q),
\qquad Z=G_++G_-.
\tag{NC.2}
\]
前稿记号 \(D_\sigma\) 即这里合同的 \(G_\sigma\)。上述每一层都包含双有序项；种子返回三叶场及其共线横向零根已在本人前稿穷尽，不因当前比较首项而删除。定义全部正接收总向量
\[
W_{0,i}=\frac13\sum_{j\ne i}C_{ij},
\qquad M_{0,i}=\frac16\sum_{j\ne i}Z_{ij},
\tag{NC.3}
\]
负接收为完整共轭。不同 \(j\) 的两项先在同一个 \(p_i^\perp\) 内相加；不同接收频率是完整 \(D\) 向量的不同分量。

## NC.2 保留相干性的单对完整和

记
\[
P=|p|^2>0,\quad Q=|q|^2>0,\quad c=p\cdot q,
\quad\Delta=PQ-c^2>0,\quad d=P-Q,\quad S=P+Q,
\]
\[
\lambda_\pm=S\pm2c>0,\qquad E_\pm=4P+Q\pm4c>0,
\quad\Lambda=\lambda_+\lambda_->0,\quad\Omega=E_+E_->0.
\tag{NC.4}
\]
使用同一个实横向分解
\[
e=q-\frac cPp,\quad f=p-\frac cQq,\quad n=p\times q,
\qquad U=u e+v n,\quad V=x f+y n.
\tag{NC.5}
\]
有 \(U\cdot q=\Delta u/P\)、\(V\cdot p=\Delta x/Q\)。令
\[
R=\Re(x\overline y),\qquad I=\Im(x\overline y),
\]
\[
h_+=\frac{Q+2c}{\lambda_+E_+},\qquad
h_-=\frac{Q-2c}{\lambda_-E_-},
\]
\[
\alpha=2-d(h_++h_-),\qquad
\beta=-d(h_+-h_-),\qquad
\kappa=\frac{4cdP}{Q\Lambda},
\]
\[
H=4P^2-PQ+Q^2-4c^2
=d(4P-Q)+4\Delta.
\tag{NC.6}
\]
这里 \(h_\pm\) 是实几何标量，不是螺旋向量。直接合并本人前稿的两个完整 \(G_\sigma\) 得
\[
\boxed{Z=Z_e e+Z_n n,}
\]
\[
\boxed{Z_e=
\frac{8ic\Delta^3d(2P+Q)H}{P^2Q^2\Lambda\Omega}
u^2|x|^2,}
\tag{NC.7}
\]
\[
\boxed{Z_n=
\frac{2i\Delta^3}{P^2Q}u^2(\alpha R+i\beta I)
+\frac{8ic\Delta^3d}{PQ^2\Lambda}uv|x|^2.}
\tag{NC.8}
\]
例如法向合并中的两个相干系数分别为
\[
(1-dh_+)x\overline y+(1-dh_-)\overline x y,
\]
其和正是 \(\alpha R+i\beta I\)。\(uv|x|^2\) 的系数利用
\[
\frac{Q+c}{\lambda_+}-\frac{Q-c}{\lambda_-}
=\frac{2cd}{\Lambda}
\]
得出，不能把两个 \(G_\sigma\) 的共轭或符号略去。

完整自供给空间系数仍是
\[
\boxed{C=\frac{4i\Delta^3d}{P^2Q^2\Lambda}u
\left[cdu|x|^2e+
\{Qu(SR-2icI)+2cP|x|^2v\}n\right].}
\tag{NC.9}
\]
NC.7–9 未除以 \(c,d,u,x\)，在下面所有退化分支都有意义。每个发送种子的 \(|x|^2,x\overline y,\overline x y\) 都来自同一个 Hermitian 秩一协方差；接收仍为复二次依赖 \(u^2,uv\)。特别地
\[
Z_{ij}(zU_i,wU_j)=z^2|w|^2 Z_{ij}(U_i,U_j),
\qquad C_{ij}(zU_i,wU_j)=z^2|w|^2 C_{ij}(U_i,U_j).
\tag{NC.10}
\]

## NC.3 单对零判据及全部退化分支

**不活跃输入。** 若 \(u=0\) 或 \(x=0\)，NC.7–9 给 \(Z=C=0\)。第一层场可能仍非零，这里只断言定义于 NC.2 的完整四叶接收系数为零。

**原频率等长。** 若 \(d=0\)，则
\[
C=0,\qquad
Z=\frac{4i\Delta^3}{P^2Q}u^2R\,n.
\tag{NC.11}
\]
因此 \(Z=0\iff u=0\) 或 \(R=0\)。等长并不让所有混合根恒为零，但自供给本对恒为零。

**正交频率。** 若 \(c=0\)，则
\[
\alpha=\frac{4[2P(P+Q)+Q^2]}{(P+Q)(4P+Q)}>0,
\qquad\beta=\kappa=0,
\]
\[
Z=\frac{8iP Q^2[2P(P+Q)+Q^2]}{(P+Q)(4P+Q)}u^2R\,n,
\qquad
C=\frac{4iP Q^2(P-Q)}{P+Q}u^2R\,n.
\tag{NC.12}
\]
因此正交分支 \(Z=0\iff u=0\) 或 \(R=0\)，并且 \(Z=0\Rightarrow C=0\)。这与等长分支相交时的 NC.11 一致。

**非正交、不同长度、双向耦合非零。** 现在限定
\[
c\ne0,\qquad d\ne0,\qquad ux\ne0.
\tag{NC.13}
\]
由于 \(e,n\) 在 \(p^\perp\) 内线性独立，NC.7 的平面分量首先迫使
\[
Z=0\ \Longrightarrow\ H=0.
\tag{NC.14}
\]
若 \(H=0\)，则
\[
4\Delta=(Q-P)(4P-Q)>0,
\quad P<Q<4P,
\]
\[
\Lambda=3P(Q-P),\qquad\Omega=3Q(4P-Q),
\]
\[
\alpha=\frac{2(3Q-2P)}{3Q},\qquad
\beta=\frac{4c}{3Q},\qquad
\kappa=-\frac{4c}{3Q}.
\tag{NC.15}
\]
这些等式由 NC.6 的两个分母直接通分、代入 \(4c^2=4P^2-PQ+Q^2\) 得到；全程未选择频率数值。

记 \(\zeta=y/x\)、\(\rho=v/u\)。此时 NC.8 等价于
\[
Z_n=\frac{2i\Delta^3}{P^2Q}u^2|x|^2
[\alpha\Re\zeta-i\beta\Im\zeta+\kappa\rho].
\]
因 \(\kappa\ne0\)，得到完整充要判据
\[
\boxed{
Z=0\iff
\begin{cases}
4P^2-PQ+Q^2-4c^2=0,\\
\displaystyle\frac vu=
\frac{3Q-2P}{2c}\Re\frac yx
-i\Im\frac yx.
\end{cases}}
\tag{NC.16}
\]
该充要式严格限于 NC.13；其余分支已在前面保留。它包含发送与接收的完整复极化比，不能由螺旋强度平均替换。

在 NC.16 分支，NC.9 的平面分量严格非零，所以 \(C\ne0\)。但这只是一个方向的符号相容条件；没有证明任何实际整数三对几何与同一组三个种子同时实现它。

几何还必须满足
\[
\frac{c^2}{PQ}
=\frac P Q+\frac Q{4P}-\frac14
=\frac34+\frac{(2P/Q-1)^2}{4P/Q}\ge\frac34,
\tag{NC.17}
\]
并严格小于一。因此该单向例外只能位于 \(P<Q<4P\) 的高相关几何子域。

综合全部分支，\(Z=0\) 而 \(C\ne0\) **恰只能**由 NC.13 与 NC.16 给出；这个判据并不将其三对实现性记为已解。

## NC.4 同一对的双向障碍与总和的必要结构

对同一对原种子 \((U_i,U_j)\)，双向活跃性由
\[
(U_i\cdot p_j)(U_j\cdot p_i)\ne0
\tag{NC.18}
\]
决定；交换接收方向并不改变这一条件。

有以下不需要长度互异或非正交预设的闭合结论：
\[
\boxed{Z_{ij}=Z_{ji}=0\quad\Longrightarrow\quad
C_{ij}=C_{ji}=0.}
\tag{NC.19}
\]
证明：若例如 \(C_{ij}\ne0\) 且 \(Z_{ij}=0\)，NC.3 强制其落在 NC.16 分支，特别是 \(P_i<P_j\)、非正交、双向活跃。反向接收具有 \(P=P_j>Q=P_i\)，而
\[
H(P,Q)=(P-Q)(4P-Q)+4\Delta>0.
\]
于是反向 NC.7 平面分量非零，\(Z_{ji}\ne0\)，矛盾。另一方向相同。证明始终使用同一对极化；没有为反向另造种子。

因此，若所有 \(M_{0,i}=0\) 而 \(W_0\ne0\)，必有至少一行满足
\[
\boxed{Z_{ij}=-Z_{ik}\ne0,
\qquad\{i,j,k\}=\{1,2,3\}.}
\tag{NC.20}
\]
否则每个零行都只有两条零 \(Z\)，故全部有序 \(Z_{ij}=0\)；NC.19 会使全部 \(C_{ij}=0\)，与 \(W_0\ne0\) 矛盾。**只安排单向零分支、而没有任何一行真正的非零向量相消，不能通过全三对门。**

同样，若 \(P_i\) 是最大长度平方（允许并列），且 \(M_{0,i}=0,W_{0,i}\ne0\)，该行必满足 NC.20。因为最大长度接收不可能进入要求 \(P_i<P_j\) 的 NC.16 例外；若该行两条 \(Z\) 都零，其两条 \(C\) 也必须都零。

另一个由完整向量方向直接得到的边界是：若某个 \(p_i\) 同时正交于另外两个原频率，则 NC.12 使两条 \(Z_{ij},Z_{ik}\) 分别沿 \(p_i\times p_j,p_i\times p_k\)。线性独立性保证这两条实方向在 \(p_i^\perp\) 内独立，所以
\[
\boxed{p_i\perp p_j,p_k\quad\Longrightarrow\quad
M_{0,i}=0\ \Rightarrow\ W_{0,i}=0.}
\tag{NC.21}
\]
特别地，全正交三对在任意完整复二维极化下不能满足本项的 \(M_0=0,W_0\ne0\)。这是当前来源首项的方向结论，不是重开正交模板返回分类。

## NC.5 同一组三对的活跃图

在三个标签上，以 NC.18 定义一条无向活跃边。该定义只检查同一原种子的两个实际点积，不设逐边新变量。不活跃边的两个方向都满足 \(C=Z=0\)。

无活跃边时 \(W_0=0\)。**恰一条活跃边也不能通过所求门，且不需任何额外几何假设。** 因其两个端点的零混合行分别迫使 \(Z_{ij}=Z_{ji}=0\)，NC.19 随即使该边的两个 \(C\) 都零。

为给两边情形一个明确收窄，以下这一段额外限定：三个长度两两不同，三对频率均非正交。若活跃图恰有两边，其形状为中心 \(i\) 与叶 \(j,k\) 的星形。每个叶行只有一条活跃混合向量，所以全部 \(M_0=0\) 必须且只可能满足：

1. 中心长度严格大于两个叶：\(P_j<P_i\)、\(P_k<P_i\)；并分别满足
\[
4P_j^2-P_jP_i+P_i^2-4c_{ji}^2=0,
\quad
4P_k^2-P_kP_i+P_i^2-4c_{ki}^2=0.
\tag{NC.22}
\]
因此分别有 \(P_i<4P_j\)、\(P_i<4P_k\)，两条边还须满足 NC.17 的相关角度限制。
2. 对两个叶作为接收、中心作为发送，NC.16 的完整复极化关系各自成立。两次出现的中心极化都是同一个 \(U_i\)，不能分别选择其坐标。
3. 非活跃叶间边仍须满足原始点积条件
\[
(U_j\cdot p_k)(U_k\cdot p_j)=0,
\tag{NC.23}
\]
且中心行须真正满足
\[
\boxed{Z_{ij}+Z_{ik}=0.}
\tag{NC.24}
\]

在既定星形活跃图与上述非正交、互异长度域内，这些条件合起来也充分使全部 \(M_0=0\)。若有同一组三对数据满足全部条件，两个叶的 \(C_{ji},C_{ki}\) 都由 NC.16 严格非零；叶行没有第二个活跃自供给项可抵消，因此那时确有 \(W_0\ne0\)。**本稿没有证明这样的同一组三对数据存在**：共同中心极化、叶间不活跃条件和中心向量相消的联合可解性仍 OPEN。这里不是把两个叶的单向条件当成三对候选。

由此，在上述全非正交、互异长度域内，若几何完全避开 NC.22 的单向例外，则任何可能满足 \(M_0=0,W_0\ne0\) 的活跃图必须是三边闭环。等长边或正交边的两边图不套用这一星形分类，仍由 NC.3 的真实零分支和下面的一般相容门处理。

## NC.6 共享形状固定后的精确正幅度门

以下恢复合同的全部非平行几何，不要求长度互异或三对都非正交。写同一个原种子为
\[
U_i=\sqrt{a_i}e^{i\theta_i}V_i,
\qquad a_i>0,\quad\|V_i\|=1,\quad V_i\perp p_i.
\tag{NC.25}
\]
这只是原数据的幅度、整体相位和形状表示；\(V_i\) 在它参与的全部边上必须相同。定义
\[
\mathcal Z_{ij}=Z_{ij}(V_i,V_j),\qquad
\mathcal C_{ij}=C_{ij}(V_i,V_j).
\tag{NC.26}
\]
NC.10 给
\[
M_{0,i}=\frac{e^{2i\theta_i}a_i}{6}
(a_j\mathcal Z_{ij}+a_k\mathcal Z_{ik}),
\]
\[
W_{0,i}=\frac{e^{2i\theta_i}a_i}{3}
(a_j\mathcal C_{ij}+a_k\mathcal C_{ik}).
\tag{NC.27}
\]
因此种子整体相位不能修复混合零行；全部发送相干性已经保留在同一个 \(V_jV_j^*\) 中。

对每一行，正幅度混合零条件精确分为：

- 两条 \(\mathcal Z\) 都零：该行不约束幅度。
- 恰一条 \(\mathcal Z\) 为零：该行不可能为零。
- 两条都非零：必须且只需存在 \(r_i>0\) 使
\[
\mathcal Z_{ik}=-r_i\mathcal Z_{ij},
\qquad \frac{a_j}{a_k}=r_i.
\tag{NC.28}
\]

NC.28 的向量部分可不用任何双线性自点积分母地检验：定义
\[
\Omega_i(X,Y)=p_i\cdot(X\times Y).
\]
\(\Omega_i\) 是复二维横向平面上的非退化交替形式。对两个非零横向向量，严格负实射线条件等价于
\[
\boxed{\Omega_i(\mathcal Z_{ij},\mathcal Z_{ik})=0,
\quad\Im(\mathcal Z_{ij}^*\mathcal Z_{ik})=0,
\quad\Re(\mathcal Z_{ij}^*\mathcal Z_{ik})<0.}
\tag{NC.29}
\]
第一条件使两向量复共线，后两条件使比例为负实数。此论证也适用于双线性自点积为零的非零复向量。通过时
\[
r_i=\frac{\|\mathcal Z_{ik}\|}{\|\mathcal Z_{ij}\|}>0.
\]

若三行都处于两条非零向量的分支，按循环 \((i,j,k)=(1,2,3),(2,3,1),(3,1,2)\)，全部正幅度相容当且仅当
\[
\boxed{r_1r_2r_3=1.}
\tag{NC.30}
\]
必要性来自三条幅度比相乘。充分性则直接由
\[
a_3=r_2a_1,\qquad a_2=r_1r_2a_1,\qquad a_1>0
\]
给出；没有选定实际幅度。若只有一行或两行约束，约束连接的是三个幅度变量之间的不同边，没有闭环，因此已通过的正比值相容；没有约束时幅度任意正。恰一个零向量的坏行始终排除。由此给出了固定共享形状时 \(M_0=0\) 对全部整体相位、正幅度的精确判定。

这个判定没有解决未知的共同形状或整数几何。若它通过，\(W_0\ne0\) 还要求 NC.27 的三个完整 \(\mathcal C\) 加权行不全为零。在三行都非零且 NC.30 成立的分支，该条件明确化为：以下三个向量至少一个非零，
\[
\boxed{
r_1\mathcal C_{12}+\mathcal C_{13},\qquad
r_2\mathcal C_{23}+\mathcal C_{21},\qquad
\mathcal C_{31}+r_1r_2\mathcal C_{32}.}
\tag{NC.31}
\]
此处使用的是 NC.30 强制的同一组三个幅度比。单条 \(\mathcal C\ne0\) 不足以替代 NC.31。

## NC.7 本轮闭合结果与明确剩余域

已闭合的解析结果为：完整相干单对和 NC.7–9；全部零分支及非正交单向例外 NC.16；同一种子的双向障碍 NC.19；真实总相消的必要结构 NC.20；最大长度接收与正交接收行的边界；一条活跃边的通用排除；受限两边星形的必要且条件充分关系；固定共享形状后的严格负实射线、正幅度循环和完整 \(W_0\) 检验 NC.29–31。

一般 \(M_0=0,W_0\ne0\) 的相容性仍 OPEN。具体未付的是：三边闭环中是否存在同一组三个完整复形状和合法整数几何，使各行 NC.29、共同 NC.30 及非零 NC.31 同时成立；或者受限星形条件中的共同极化、叶间不活跃和中心向量相消能否共同实现。含等长或正交边的其他退化组合仍由已给精确零分支与幅度门约束，没有被宣布通过或全部排除。

本人已接受的源桥接给同一真实解
\(\mathcal S/t^3\to W_0\)、\((P_Du-\mathcal S)/t^3\to M_0\)，并带明确有限树及无穷尾部界。因此在 \(W_0\ne0\) 时，当前门确实等价于真实非自供给/自供给范数比的短时极限为零。它仍只控制首项；\(M_0=0\) 不意味着所有正时间混合项恒为零，也不保证模板返回、形态纯度或独立的下一代 NS 解。

没有实际选择初值或时间，没有候选接受、正交代际能量、统一跨代控制、同一初值无限尺度、有限总时间、奇性或全局正则性结论。NOT CLAY。

## NC.8 实际来源绑定

路径相对于 `research/reverse/`。

| 文件与实际范围 | SHA256 |
|---|---|
| net-mixed-cancellation/CONTRACT.md，本项全文 | 8ec55579d3288a15e47f2b1af17a2d981ac174fb649dc496fb6d5ac0d9b2e7e8 |
| mixed-polarization/MIXED_ROOT_INDEPENDENT.md，本代理前项全文推导及自核，本项核对字节未变 | cad93f863ad371723d4510f20588a0f7abcee3e4f8e2984010f88ebcb2fc2dbf |
| mixed-polarization/SOURCE_BRIDGE_INDEPENDENT.md，本代理前项全文推导及自核，本项核对字节未变 | 1d3d33fbb8fcc17ac1266f2ee88c88eebe328867f385277a0a684cfa2247630a |

未新增外部文献依赖或新颖性声明。源码字节绑定不能代替本轮非作者数学审查。
