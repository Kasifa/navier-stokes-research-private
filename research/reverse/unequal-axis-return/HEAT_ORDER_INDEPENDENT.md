# 带热纯 2+2 返回：独立积分排序与相关相位必要门

2026-09-08，PRIVATE_CORE。状态：**STRICT NECESSARY FREQUENCY / TIME / SIGN CONDITIONS；剩余相容性未决，未接受候选**。

本稿只完整读取本目录 `HEAT_TRANSFER_PREFLIGHT.md` 与 `HEAT_ORDER_CONTRACT.md`，没有读取 `HEAT_ORDER_PROOF.md`。沿用本人已完成的瞬时有序 Fourier–Leray 推导及其两通道相位分支；以下热积分的排序、符号相关性和时间条件独立手推。所读热适用性稿披露它使用了瞬时主稿，因此本稿不把这份间接来源说成没有主稿来源；本轮没有读取该瞬时主稿或其他人的热排序证明。无科学程序、数组、指数数值求值、参数选择、Git 或外部文献检索。

## HI.1 固定对象与准确系数

固定合同中的同一个符号初值，按长度重记
\[
q_1=n_1^2<q_2=n_2^2<q_3=n_3^2,
\qquad z_{ij}=(U_i)_j,
\qquad R_i=\Re(z_{ij}\overline{z_{ik}}),
\quad\{i,j,k\}=\{1,2,3\}.
\]
重记标签不是给返回模板增加轴置换。仍采用完整有序算子
\[
B(f,g)_k=-iP_k\sum_{r+s=k}(f_r\cdot s)g_s.
\]
由正交轴的热率相等，全部第一代对角系数精确为
\[
(v_1)_{\sigma p_i+\tau p_j}(s)
=s e^{-(q_i+q_j)s}N_{\sigma p_i+\tau p_j},
\qquad N=B(a,a).
\tag{HI.1}
\]
同轴配对逐项为零。到 \(2p_i\) 的全部第二层配对仍为
\((p_i+p_j,p_i-p_j)\) 及其反序，\(j\ne i\)。定义
\[
A_{ij}(t)=4n_i n_j^2\frac{q_j-q_i}{q_i+q_j}H_{ij}(t),
\qquad
H_{ij}(t)=\int_0^t s^2
e^{-4q_i(t-s)-2(q_i+q_j)s}\,ds.
\tag{HI.2}
\]
全部接收分量为
\[
((w_{22})_{2p_i})_j=-iA_{ik}(t)z_{ik}^{2}R_k,
\qquad
((w_{22})_{2p_i})_k=-iA_{ij}(t)z_{ij}^{2}R_j,
\qquad ((w_{22})_{2p_i})_i=0.
\tag{HI.3}
\]
这与所读热稿 HT.6 的 \(+4i(q_i-q_j)/(q_i+q_j)\) 记法相同。系数4已包含两个有序项及复共轭合并，不能再添一个2。负接收模为正接收模的完整共轭。\(H_{ij}>0\) 对每个 \(t>0\) 成立，但不同 \(i,j\) 不能抽出公共热权重。接收集外输出没有从树定义中删除。

令
\[
\alpha=\frac{q_2-q_1}{q_2+q_1},\quad
\beta=\frac{q_3-q_2}{q_3+q_2},\quad
\gamma=\frac{q_3-q_1}{q_3+q_1}
=\frac{\alpha+\beta}{1+\alpha\beta}.
\]
因此 \(0<\alpha,\beta<1\) 且 \(\gamma>\max(\alpha,\beta)\)。按合同
\[
g_1=\alpha\gamma H_{12}H_{13},\quad
g_2=\alpha\beta H_{21}H_{23},\quad
g_3=\beta\gamma H_{31}H_{32}.
\tag{HI.4}
\]

## HI.2 有限区间正积分的微分引理

置
\[
f(u)=\int_0^1\theta^2e^{u\theta}\,d\theta,
\qquad \mu(u)=\frac{f'(u)}{f(u)},
\qquad v(u)=\mu'(u).
\]
任意有限实 \(u\) 上，区间有界且被积函数光滑，故可在积分内任意有限次微分。归一化正密度 \(\theta^2e^{u\theta}/f(u)\) 给
\[
0<\mu(u)<1,\qquad
0<v(u)<\mu(u)(1-\mu(u)).
\tag{HI.5}
\]
后一个严格上界来自 \(\theta^2<\theta\) 在 \((0,1)\) 上，减去均值平方。定义 \(k(u)=u\mu(u)\)。分部积分 \((\theta^3e^{u\theta})'\) 给
\[
u\mu(u)=\frac{e^u}{f(u)}-3,
\qquad
k'(u)=\frac{e^u}{f(u)}(1-\mu(u))>0.
\tag{HI.6}
\]
若 \(u\le0\)，则 \(k'=\mu+uv\le\mu<1\)。若 \(u>0\)，另对 \((\theta^2e^{u\theta})'\) 积分得
\[
e^u=2\int_0^1\theta e^{u\theta}\,d\theta+uf(u)>(u+2)f(u).
\]
与 HI.6 合并为 \(u(1-\mu)<1\)，从而
\[
k'=\mu+uv<\mu+u\mu(1-\mu)<2\mu<2.
\]
因此统一得到
\[
\boxed{0<k'(u)<2\quad (u\in\mathbb R).}
\tag{HI.7}
\]
这里只需要上界2，不声称更尖锐的界。

把两个平方频率暂作正实变量，记
\[
H(a,b;t)=t^3e^{-4at}f(2(a-b)t),\qquad t>0.
\]
对 \(a\) 与物理时间 \(t\) 微分，有
\[
\partial_t\partial_a\log H(a,b;t)
=-4+2k'(2(a-b)t)<0.
\tag{HI.8}
\]
故对任意固定 \(b\) 及 \(a<c\)，\(H(a,b;t)/H(c,b;t)\) 严格随 \(t\) 增长：其对数导数等于
\(-\int_a^c\partial_t\partial_\xi\log H(\xi,b;t)\,d\xi>0\)。这是证明中的实变量积分，不是选择另一组物理初值。

对于交换输入输出的比例，令 \(\Delta=c-a>0\)，直接得
\[
\frac{d}{dt}\log\frac{H(a,c;t)}{H(c,a;t)}
=4\Delta-2\Delta[\mu(-2\Delta t)+\mu(2\Delta t)]>0.
\tag{HI.9}
\]
这一步不能由两个积分都为正推出；它使用了精确热率。

## HI.3 全部三行比例的严格排序

对任意 \(i<j\)，令 \(k\) 为剩余标签、\(\Delta_{ij}=q_j-q_i\)。将 \(g_i/g_j\) 写成固定正频率系数乘
\[
\frac{H_{ij}}{H_{ji}}\frac{H_{ik}}{H_{jk}}.
\tag{HI.10}
\]
HI.8–9 表明这两个因子各自严格随 \(t>0\) 增长。因此
\[
\boxed{g_1/g_2,\ g_2/g_3,\ g_1/g_3\text{ 均严格随 }t>0\text{ 增长}.}
\tag{HI.11}
\]
还可直接比较同一个积分变量 \(s\)。交换比例的两核之比为
\(e^{4\Delta_{ij}(t-s)}\)，同列比例的两核之比为
\(e^{\Delta_{ij}(4t-2s)}\)。对 \(s\in(0,t)\) 严格夹住它们并按分母正核积分，得到
\[
1<\frac{H_{ij}}{H_{ji}}<e^{4\Delta_{ij}t},\qquad
e^{2\Delta_{ij}t}<\frac{H_{ik}}{H_{jk}}<e^{4\Delta_{ij}t}.
\tag{HI.12}
\]
令
\(r_{12}^0=\gamma/\beta\)、\(r_{23}^0=\alpha/\gamma\)、\(r_{13}^0=\alpha/\beta\)，则
\[
\boxed{r_{ij}^0e^{2\Delta_{ij}t}
<\frac{g_i(t)}{g_j(t)}
<r_{ij}^0e^{8\Delta_{ij}t}.}
\tag{HI.13}
\]
换元 \(s=t\theta\) 及有界区间的连续性给 \(H_{ij}/t^3\to1/3\)，所以 \(g_i/g_j\to r_{ij}^0\) 当 \(t\downarrow0\)。HI.13 又给这些比例在 \(t\to\infty\) 时趋于无穷。所有极限仅涉及定义良好的有限树积分，不涉及原 NS 轨道延拓。

于是得到具体排序：

- 对所有 \(t>0\)，\(g_1>g_2\)。
- 存在唯一 \(t_{23}>0\) 使 \(g_2=g_3\)；此前 \(g_2<g_3\)，此后 \(g_2>g_3\)。
- 若 \(\alpha\ge\beta\)，则所有正时间 \(g_1>g_3\)。若 \(\alpha<\beta\)，存在唯一 \(t_{13}>0\) 使 \(g_1=g_3\)；此前 \(g_1<g_3\)，此后 \(g_1>g_3\)。在后一种情况下 \(t_{13}<t_{23}\)，因为 \(t_{13}\) 处 \(g_3=g_1>g_2\)。

此外，\(g_1=2g_2\) 在正时间有且仅有一个解 \(t_{12}^{(2)}\)，当且仅当 \(\gamma<2\beta\)；若 \(\gamma\ge2\beta\)，则它没有正时间解。这是比例等式的分类，尚不是模板返回的分类。

## HI.4 公共幅度与两通道相位，零分支先行

写 \(D=\operatorname{diag}(\varepsilon_1,\varepsilon_2,\varepsilon_3)\)，\(\varepsilon_i\in\{\pm1\}\)，以免与频率差符号混淆。假设合同的返回成立：
\[
((w_{22})_{2p_i})_j
=\rho\eta_i\varepsilon_j z_{ij}^{(\varepsilon_i)},
\qquad \rho>0,\quad |\eta_i|=1,
\tag{HI.14}
\]
其中上标负号取复共轭，每行的两个横向通道使用同一个 \(\eta_i\)。允许全部平移相位；\(x_{0,i}\mapsto e^{-2in_i x_{0,i}}\) 对每个圆周满射，所以本证明没有通过限制平移偷加障碍。

HI.3 中若一行某个横向输入为零而另一横向输入非零，则非零模板分量所需的输出为零，矛盾；两横向分量都零由 \(U_i\ne0\) 排除。因此全部六个 \(z_{ij}\ne0\)。随后任一 \(R_i=0\) 又会杀掉另一行一个必须非零的输出，所以三个 \(R_i\) 均非零。这些步骤使用 \(A_{ij}\ne0\)，后者由长度互异和 \(H_{ij}>0\) 保证。

对每行取另外两个标签 \(j<k\)，置
\[
r_i=z_{ik}/z_{ij},\qquad
C_i=\frac{|R_i|}{|z_{ij}z_{ik}|}=|\cos(\arg r_i)|>0.
\]
两通道相除精确得到
\[
r_i^2r_i^{(\varepsilon_i)}
=\varepsilon_j\varepsilon_k\frac{A_{ij}R_j}{A_{ik}R_k}
\in\mathbb R\setminus\{0\}.
\tag{HI.15}
\]
若 \(\varepsilon_i=+1\)，则 \(r_i^3\) 为非零实数，故 \(C_i\in\{1,1/2\}\)；若 \(\varepsilon_i=-1\)，则 \(|r_i|^2r_i\) 为非零实数，\(r_i\) 实且 \(C_i=1\)。因此
\[
C_i\in\{1,1/2\},\qquad C_i=1/2\Longrightarrow\varepsilon_i=+1.
\tag{HI.16}
\]
两横向模长方程相乘，并保留同一个 \(\rho\)，给
\[
\rho^2=16n_1^2n_2^2n_3^2
\Bigl(\prod_{\ell=1}^3|z_{\ell j_\ell}z_{\ell k_\ell}|\Bigr)
g_i C_jC_k.
\]
其中所有因子均正，故公共幅度要求
\[
\boxed{C_1:C_2:C_3=g_1:g_2:g_3.}
\tag{HI.17}
\]
特别地，严格的 \(g_1>g_2\) 强迫
\[
C_1=1,\quad C_2=1/2,\quad g_1=2g_2.
\tag{HI.18}
\]

## HI.5 三行实比值的符号相关性排除七个 signed-axis 分支

只使用绝对值会留下两个可能模式 \((1,1/2,1)\) 与 \((1,1/2,1/2)\)。它们还必须同时满足 HI.15 的实符号，不能独立挑选三行余弦。

记 \(s_i=\operatorname{sgn}R_i\)、\(S=s_1s_2s_3\)，并以 \(h_i=0\) 表示 \(C_i=1\)、\(h_i=1\) 表示 \(C_i=1/2\)。当 \(\varepsilon_i=+1\) 时，\(\cos(3\arg r_i)=\cos(\arg r_i)(4C_i^2-3)\)；当 \(\varepsilon_i=-1\) 时 \(r_i\) 已为实数且 \(h_i=0\)。两种情形统一为
\[
\operatorname{sgn}(r_i^2r_i^{(\varepsilon_i)})=(-1)^{h_i}s_i.
\]
按 \(q_1<q_2<q_3\)，每行 \(j<k\) 下
\[
\operatorname{sgn}(A_{ij}/A_{ik})=b_i,
\qquad (b_1,b_2,b_3)=(+1,-1,+1).
\]
HI.15 乘以 \(s_i\) 后给三条相关的符号方程
\[
(-1)^{h_i}=b_i\varepsilon_j\varepsilon_k S.
\tag{HI.19}
\]
三式相乘给 \(S=(-1)^{h_1+h_2+h_3+1}\)。已有 \(h_1=0,h_2=1\)。

若 \(h_3=1\)，则 \(S=-1\)，第一式要求 \(\varepsilon_2\varepsilon_3=-1\)；但两行的 \(C_2=C_3=1/2\) 又要求 \(\varepsilon_2=\varepsilon_3=+1\)。矛盾。因此 \((1,1/2,1/2)\) 对所有八个 D 均不可能。

若 \(h_3=0\)，则 \(S=+1\)，三式分别要求
\(\varepsilon_2\varepsilon_3=\varepsilon_1\varepsilon_3=\varepsilon_1\varepsilon_2=+1\)。三个符号相同，而 \(C_2=1/2\) 强迫 \(\varepsilon_2=+1\)。故
\[
\boxed{D=I,\quad (C_1,C_2,C_3)=(1,1/2,1),
\quad R_1R_2R_3>0,\quad g_1=g_3=2g_2.}
\tag{HI.20}
\]
这是从全部八种 D 出发的必要结论，包含了反射分支，未先假设 D 保向。

## HI.6 必要频率、唯一可能时间与未决等式

由 HI.3 的严格排序，\(g_1=g_3\) 有正时间解的必要且充分条件是 \(\alpha<\beta\)。这等价于
\[
\boxed{q_2^2<q_1q_3\quad\Longleftrightarrow\quad n_2^2<n_1n_3.}
\tag{HI.21}
\]
因此违反 HI.21 的长度三元组在全部正时间、全部允许极化、全部平移及全部 D 下都被本纯 2+2 返回合同排除。满足 HI.21 只使一个必要比例相交；没有提供返回解。

若 HI.21 成立，则 \(\gamma<\alpha+\beta<2\beta\)，故 \(t_{13}\) 和 \(t_{12}^{(2)}\) 都各自存在且唯一。任何返回只能发生在
\[
\boxed{t=t_{13}=t_{12}^{(2)},\qquad
g_1(t_{13})/g_2(t_{13})=2.}
\tag{HI.22}
\]
也就是说，对每个固定长度三元组，至多有一个可能返回时间。该时间是否同时满足另一条比例、以及剩余复极化方程是否可解，本稿均未判定。

不作任何指数数值求值，HI.13 还给严格时间夹界：
\[
\frac{\log(\beta/\alpha)}{8(q_3-q_1)}
<t_{13}<
\frac{\log(\beta/\alpha)}{2(q_3-q_1)},
\tag{HI.23}
\]
\[
\frac{\log(2\beta/\gamma)}{8(q_2-q_1)}
<t_{12}^{(2)}<
\frac{\log(2\beta/\gamma)}{2(q_2-q_1)}.
\tag{HI.24}
\]
返回时间必须同时属于这两个开区间，并满足 HI.22 的精确等式。这里没有选择实际长度、时间或极化，没有把这些开区间的交非空当作充分条件，也没有追加参数搜索。

## HI.7 精确余项与结论边界

HI.1–24 只使用固定有限树项的精确系数、正积分和实微积分，解析余项为零。热排序支付了瞬时障碍不能直接迁移后的一部分新必要条件；它没有把原来的纯频率矛盾原样套到正时间。

所得严格障碍是：七个非恒等 signed-axis 分支全部排除；恒等分支在 \(n_2^2\ge n_1n_3\) 时全部正时间排除。其余频率仅缩到唯一可能时间和未决等式 HI.22；没有接受任何候选，也没有宣称完成带热返回方程的全部分类。

\(v_1\) 不是同一原解中的纯第一代实际供给投影，\(w_{22}\) 也不是完整原解的第二代输出。1+3、3+1、原种子混合、接收集外回流、其他时间树和无限维误差都没有由本稿支付。精确保留本树的黏性权重，不等于获得真实 NS 正时间机制；本稿不排除其他模板、其他支撑或完整 NS 奇性，不给单初值无限尺度、统一迭代或有限总时间结论。

## HI.8 实际输入绑定

| 本轮完整实读文件（相对此目录） | SHA256 |
|---|---|
| HEAT_TRANSFER_PREFLIGHT.md | efe1b7313abaee0d1cd986da6ffdba38ff818eb8707b0cdda003f66eee18f369 |
| HEAT_ORDER_CONTRACT.md | a65d7ffb1350e7cb2a6ee20cc5be80eae41d4ac2544c163e9fc7765d1bacf9ad |

这些绑定记录来源字节，不替代推导或非作者审查。本轮尚未对照热排序主稿，本文件是独立推导，不能自称已通过非作者终审。
