# 星形空间相消下的原种子方向：独立检验

2026-09-08，PRIVATE_CORE。状态：独立推导，待非作者审查和根全文比较。

**结论：在合同所给的全非正交、长度互异、线性独立、两边星形及总 \(M_0=0\) 条件分支内，至少一条叶接收的完整 \(C_i\) 不在原种子复直线 \(\mathbb C U_i\) 上。纯 \(W(t)\) 对所有 \(t>0\) 都不能在全部加倍频率上返回这些方向；同一真实 NS 解的接收投影在下文明确短窗内有严格的相对距离下界。共同幅度、平移与合同允许的正交变换均包含在被否定的目标族中。**

这只是否定该条件分支的原种子方向模板，不判断其它形状、较晚时刻、一般三边图或奇性机制。本文没有证明星形全部相消条件存在实例，也没有求解中心相消。未读 `STAR_TEMPLATE_PROOF.md` 或 `STAR_CENTER_ANALYSIS.md`。全部手工符号，无实际新参数、科学程序、数组、数值求值、扫描、Git、额度重置、图档或外发；本轮只写入本文件。

## 1. 合同、已接受接口和实读来源

固定中心频率 \(p_0\) 与叶频率 \(p_1,p_2\)，三者线性独立，成对点积全非零，平方长度两两不同。同一份非零种子满足 \(U_i\perp p_i\)，负模为其共轭。双向活跃边恰为 \(\{0,1\}\)、\(\{0,2\}\)，并假设全部正负加倍接收的总混合首项 \(M_0=0\)。单位黏性、无外力和固定三维 \(2\pi\) 环面保持不变。

已接受星形必要性给三种子均线性极化，以及每个活跃叶接收零边的完整相干关系。以下从该关系与已接受的单对 \(C\) 继续推导，不使用未读的新主稿。

路径相对于 `research/reverse/`。

| 来源与实际阅读范围 | SHA-256 |
|---|---|
| net-mixed-cancellation/STAR_TEMPLATE_CONTRACT.md，本轮全文 | b7543164be08ff3b625e45745b7f9aab4b81d74f082f4f71cbb1f220f62e7ad0 |
| net-mixed-cancellation/STAR_POLARIZATION.md，本人前项独立推导并全文自核，本轮字节未变；使用 SP.9–18 | 84463afc66b0447db1c507eb805f4cf0df423634e809ec3367600d18ca8ba82c |
| nonorthogonal-return/SPATIAL_INDEPENDENT.md，本连续审查此前全文读取并核验，本轮字节未变；使用完整 SI.13–15、零门及 SI.21 | d8413facd655e775e7e3582b45947be92a3c0f60387b966625475088ff3703f8 |
| mixed-polarization/SOURCE_BRIDGE_INDEPENDENT.md，本连续审查此前最终全文读取并核验，本轮字节未变；使用同数据原解及 SB.45–49 | 1d3d33fbb8fcc17ac1266f2ee88c88eebe328867f385277a0a684cfa2247630a |

文中列举的其它历史文件不冒记为本次读取，没有外部新颖性声明。

## 2. 一个活跃零混合叶边的精确方向条件

固定叶接收 \(p\leftarrow q\)，其中 \(q=p_0\) 是中心。记
\[
P=|p|^2,\quad Q=|q|^2,\quad c=p\cdot q\ne0,
\quad d=P-Q\ne0,\quad S=P+Q,
\]
\[
\Delta=PQ-c^2>0,\qquad\Lambda=(P+Q)^2-4c^2>0,
\]
\[
e=q-\frac cPp,\quad f=p-\frac cQq,\quad n=p\times q,
\qquad U=u e+v n,\quad V=x f+y n.
\tag{STI.1}
\]
两边星形的另一叶边不活跃，所以该叶行总混合首项为零给单个中心边的 \(H=0\)。活跃性给 \(ux\ne0\)。已接受 SP.9、11 于是给
\[
P<Q<4P,
\qquad w:=\frac vu
=\frac{3Q-2P}{2c}\Re z-i\Im z,
\qquad z:=\frac yx.
\tag{STI.2}
\]
保留完整复相干量，先不把 \(z\) 的虚部设为零。

完整单对式写为 \(C=C_e e+C_n n\)，其中
\[
C_e=\frac{4ic\Delta^3d^2}{P^2Q^2\Lambda}u^2|x|^2\ne0,
\]
\[
\frac{C_n}{C_e}
=\frac{2P}{d}w
+\frac{Q}{cd}\left[S\Re z+2ic\Im z\right].
\tag{STI.3}
\]
这里 \(x\overline y=|x|^2\overline z\)，所以虚部的号正是 SI.21 的号；没有将复卷积点积改成 Hermitian 点积或作强度平均。

令 \(h=C_n/C_e\)。由 STI.2–3，直接相减得到
\[
\begin{aligned}
h-w
&=\frac Sd w+\frac{QS}{cd}\Re z
+\frac{2iQ}{d}\Im z\\
&=\boxed{\frac{S(5Q-2P)}{2cd}\Re z-i\Im z.}
\end{aligned}
\tag{STI.4}
\]
\(S(5Q-2P)/(2cd)\) 是非零实数，因为 \(Q>P>0\)、\(c d\ne0\)。而 \(e,n\) 在复化横向平面中线性独立，\(u,C_e\ne0\)，因此
\[
\boxed{
C\in\mathbb C U
\iff h=w
\iff z=0
\iff z=w=0.}
\tag{STI.5}
\]
最后一步使用 STI.2。此等价条件甚至在先不使用三种子线性极化时已经成立；完整相干关系没有被丢弃。

其几何意义是：一个叶边的 \(C\) 要回到原叶种子复方向，中心种子必须恰在 \(\mathbb C f\) 中，叶种子必须恰在 \(\mathbb C e\) 中。两者都位于该边的实频率平面之复化内。

## 3. 两条叶边不能同时满足该方向条件

对叶 \(i=1,2\)，令
\[
f_i=p_i-\frac{p_i\cdot p_0}{|p_0|^2}p_0
\in p_0^\perp.
\]
\(f_1,f_2\) 在复化 \(p_0^\perp\) 中线性独立。事实上，若 \(a f_1+b f_2=0\)，则
\[
a p_1+b p_2-
\frac{a(p_1\cdot p_0)+b(p_2\cdot p_0)}{|p_0|^2}p_0=0.
\]
三频独立使 \(a=b=0\)，也排除了复系数下的额外依赖。

若两条叶边都满足 \(C_i\in\mathbb C U_i\)，STI.5 将同时要求
\[
U_0\in\mathbb C f_1\cap\mathbb C f_2=\{0\},
\]
与 \(U_0\ne0\) 矛盾。因此
\[
\boxed{\text{至少一个叶节点满足 }C_i\notin\mathbb C U_i.}
\tag{STI.6}
\]
这里严格共享同一个中心向量，没有为两条叶边重新选择中心极化。中心行的相消方程未参与这个证明。

还可以明确写出叶行方向距离。令
\(\gamma_i=\operatorname{dist}_{\mathbb C U_i}(C_i)\)，距离使用 Hermitian 欧氏范数。由 \(|e|^2=\Delta/P\)、\(|n|^2=\Delta\)、\(e\perp n\)，直接投影给
\[
\boxed{
\gamma_i=|C_{e,i}|
\sqrt{\frac{\Delta_i}{1+P_i|w_i|^2}}
\left|
\frac{S_i(5Q_i-2P_i)}{2c_id_i}\Re z_i-i\Im z_i
\right|.}
\tag{STI.7}
\]
这是同一数据的明确非负解析量，且 \(\gamma_i=0\iff z_i=0\)。STI.6 证明两叶中的至少一个 \(\gamma_i\) 严格为正，没有指定哪份实际数据或给出未经计算的数值。

## 4. 共同幅度、平移与相容正交变换

令 \(O\) 为保持原频率集合 \(\{\pm p_0,\pm p_1,\pm p_2\}\) 的正交变换。平方长度互异迫使
\(Op_i=\varepsilon_i p_i\)，其中 \(\varepsilon_i=\pm1\)，不能置换不同长度的标签。保内积又给
\[
(\varepsilon_i\varepsilon_j-1)(p_i\cdot p_j)=0.
\]
因为所有成对点积非零，三个符号必须相同；三频为基，所以
\[
\boxed{O=I\quad\text{或}\quad O=-I.}
\tag{STI.8}
\]

已接受星形结论使 \(U_i=\alpha_iR_i\)，其中 \(R_i\) 为非零实横向向量。因此 \(\overline U_i\) 与 \(U_i\) 属于同一复直线。模板
\(\rho Oa(2O^T(x-x_0))\)
在 \(2p_i\) 的系数是原种子或其共轭经过 \(O\)，再乘共同幅度与平移相位；当 \(O=\pm I\) 时，它始终位于 \(\mathbb C U_i\)。

因此可以将全部允许目标进一步放宽为
\[
\mathcal T=\left\{b:\operatorname{supp}b\subseteq D,
\ b_{2p_i}=\lambda_iU_i,
\ b_{-2p_i}=\overline{b_{2p_i}},
\ \lambda_i\in\mathbb C\right\},
\tag{STI.9}
\]
其中每行任意复幅度，甚至允许零幅度。原合同允许的共同幅度、共同平移与相容 \(O\) 模板全包含于 \(\mathcal T\)。排除这个更大的集合即可排除原方向目标，但不排除别的方向或形状。

## 5. 纯 \(W\) 的精确全正时间方向失败

完整单对零门使不活跃叶边的 \(C\) 为零。故每个叶接收严格为
\[
(W(t))_{2p_i}=J_i(t)C_i,
\qquad J_i(t)>0\quad(t>0).
\tag{STI.10}
\]
至少一叶 \(\gamma_i>0\)，所以
\[
\boxed{
\operatorname{dist}_{\mathcal A_0}(W(t),\mathcal T)
\ge2\sum_{i=1}^2J_i(t)\gamma_i>0
\qquad(t>0).}
\tag{STI.11}
\]
系数二包括完整共轭负接收。对任何有缺陷的叶行，距离与其自身输出范数之比恰为 \(\gamma_i/\|C_i\|>0\)，与时间无关。

这是精确有限 \(W\) 的方向结论，不把纯 \(W\) 等同于实际 NS 轨道，也不宣称真实解全正时间失败。

## 6. 同一真实 NS 接收的明确相对距离窗口

对支持于 \(D\) 的实值共轭场定义逐模 Hermitian 正交投影 \(\mathscr Q\)：在正接收模取
\[
(\mathscr Q X)_{2p_i}
=\left(I-\frac{U_iU_i^*}{\|U_i\|^2}\right)X_{2p_i},
\]
负接收用共轭投影。\(\mathscr Q\) 在 \(\mathcal A_0\) 中范数至多一，并且独立逐模最小化给
\[
\operatorname{dist}_{\mathcal A_0}(X,\mathcal T)
=\|\mathscr QX\|_{\mathcal A_0}.
\tag{STI.12}
\]
负模的最优系数仍为正模最优系数的共轭，故没有擅自放开实值条件。

令 \(W_0\) 为 SOURCE_BRIDGE 中先逐接收求和的完整三次系数，定义同一数据的量
\[
w_0=\|W_0\|_{\mathcal A_0},
\qquad\delta_0=\|\mathscr QW_0\|_{\mathcal A_0}.
\tag{STI.13}
\]
叶行 \((W_0)_{2p_i}=C_i/3\)，由 STI.6–7，
\[
\delta_0\ge\frac23(\gamma_1+\gamma_2)>0,
\qquad w_0\ge\delta_0>0.
\tag{STI.14}
\]
因此这里的严格总向量缺陷已由本合同结构证明，未以逐边范数替代真实接收和。

设 \(A=\|a\|_{\mathcal A_0}>0\)、\(K=\max_i|p_i|>0\)、\(T_{\rm sb}=1/(8AK)\)。用已接受 SOURCE_BRIDGE 的明确常数
\[
B=B_W+B_M\ge0,
\qquad C_D=\frac43A(4AK)^5>0,
\tag{STI.15}
\]
其中 \(B_W,B_M\) 是该来源 SB.46 对同一数据定义的完整有限树误差常数。因本合同假设全部 \(M_0=0\)，该来源 SB.49 给实际唯一光滑 NS 解的全频带预算
\[
\boxed{
\|P_Du(t)-t^3W_0\|_{\mathcal A_0}
\le Bt^4+C_Dt^5,
\qquad0\le t\le T_{\rm sb}.}
\tag{STI.16}
\]
该界包括全部有序混合、回流与无限 Fourier 尾部，不是仅有纯 \(W\) 的有限树误差。

取明确数据依赖窗口
\[
\boxed{
T_{\rm dir}=
\min\left\{T_{\rm sb},\frac{\delta_0}{4B},
\sqrt{\frac{\delta_0}{4C_D}}\right\}>0,}
\tag{STI.17}
\]
其中 \(B=0\) 时相应分式取 \(+\infty\)。对 \(0<t\le T_{\rm dir}\)，余项不超过 \(\delta_0t^3/2\)。STI.12–16 因而给
\[
\operatorname{dist}_{\mathcal A_0}(P_Du(t),\mathcal T)
\ge\frac12\delta_0t^3,
\]
\[
\frac12w_0t^3\le\|P_Du(t)\|_{\mathcal A_0}
\le\frac32w_0t^3.
\]
相除得到严格相对距离下界
\[
\boxed{
\frac{\operatorname{dist}_{\mathcal A_0}(P_Du(t),\mathcal T)}
{\|P_Du(t)\|_{\mathcal A_0}}
\ge\frac{\delta_0}{3w_0}>0,
\qquad0<t\le T_{\rm dir}.}
\tag{STI.18}
\]
同一显式余项还给其极限为 \(\delta_0/w_0>0\)。原允许模板族是 \(\mathcal T\) 的子集，故同一下界也适用于它；没有要求选择或数值计算一个实际时间。

## 7. 完成范围与未付条件

本次完成了星形空间相消条件下的原种子方向检验：有限 \(W(t)\) 的方向失败对全部正时间成立，同一真实原解的接收失败只在 STI.17 的明确短窗中成立。两者范围不同。它是方向障碍，不是把其它来源相对自供给的 \(O(t)\) 比值改称为机制排除。

证明使用全非正交、长度互异及线性独立假设；正交边、等长频率、退化活跃图或三边闭环不在这个结论内。\(t=0\) 的接收为零，不使用相对距离比值。\(T_{\rm dir}\) 与 \(\delta_0/w_0\) 均依赖同一固定数据，没有跨数据统一常数。

本稿不证明星形全部 \(M_0=0\) 有实例，也不求解中心行。即使这些假设可实现，本结论仍只排除指定原种子复方向模板及其允许对称；不排除其它形状、其它接收集合、较晚真实时刻、近似但不同方向的模板、一般三边机制或奇性构造。没有可迭代再生成、统一跨代误差、同一初值无限尺度、有限总时间、奇性或全局正则性结论。CONDITIONAL ORIGINAL-DIRECTION OBSTRUCTION；NO-CANDIDATE ACCEPTED；NOT CLAY。
