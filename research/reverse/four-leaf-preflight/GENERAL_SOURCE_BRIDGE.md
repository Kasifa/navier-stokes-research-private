# 一般有限初值的四叶来源桥接：独立条件引理

2026-09-08。PRIVATE_CORE。**独立推导稿，待非作者审查。条件接口 / NO-CANDIDATE / NOT CLAY。**

本稿按父任务直接给定的有界目标形成：一般固定有限实值无散三角多项式、固定正黏性、准确的第一生成带与目标支撑条件。未读本目录根的新合同、具体数据检验或其它新稿。旧 SB.1–4 的方法在下文重新核对；不假定三个基频独立，也不使用叶数奇偶性。

本稿只证明条件引理。它不替任何具体数据支付频率碰撞、完整有序相消、首系数非零或指定带的精确身份。没有科学程序、数组执行、数值求值、实际初值/频率/幅度/时间选择、枚举、扫描、Git、外发或状态修改；只写本文件。

## 1. 直接前提与准确目标

在固定 \(\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3\) 上，固定 \(\nu>0\)，无外力。令
\[
a(x)=\sum_{k\in F}a_ke^{ik\cdot x},\qquad
F=\operatorname{supp}\widehat a\ \text{有限},\qquad
a_{-k}=\overline{a_k},\quad k\cdot a_k=0.
\tag{GS.1}
\]
可保留原研究的零均值要求；下述估计也允许一个恒定均值，此时均值由原方程保持。使用复双线性卷积点积、Hermitian 向量范数，记
\[
A=\sum_k|a_k|,\qquad K=\max_{k\in F}|k|,\qquad
E_\nu(t)=e^{\nu t\Delta}.
\]
先处理 \(A>0,K>0\)。空初值为零解；仅有零频率的初值为常值解，全部非线性响应为零，不能满足后文 \(W_0\ne0\)，无需在 \(AK=0\) 上使用时间窗公式。

完整有序算子及全频递归定义为
\[
B(f,g)_k=-i\mathbb P_k\sum_{r+s=k}(f_r\cdot s)g_s,\quad k\ne0,
\qquad B(f,g)_0=0,
\]
\[
\mathbb P_k=I-\frac{k\otimes k}{|k|^2},\qquad
v_0=E_\nu(t)a,\qquad
v_n(t)=\sum_{j=0}^{n-1}\int_0^tE_\nu(t-s)
B(v_j(s),v_{n-1-j}(s))\,ds.
\tag{GS.2}
\]
\(v_n\) 有 \(n+1\) 叶、\(n\) 个非线性门。候选集合 \(F+F\) 可以含零；但对零输出，第一输入无散使每个有序点积 \(f_r\cdot(-r)\) 为零。因此 \(v_1\) 的真实零模为零，不能把候选频率集合与真实非零支撑混称。所有 \(n\ge1\) 的零模同样为零。

设 \(L,D\) 为固定频率集合，\(P_L,P_D\) 为系数投影。直接要求
\[
L\cap F=\varnothing,\qquad P_Lv_1(t)=v_1(t),\qquad
P_Dv_j(t)=0\quad(j=0,1,2)
\tag{GS.3}
\]
在下述整个窗口内成立。这里的支撑条件是对响应的完整时间身份，不是只检查 \(t=0\) 或无黏首系数。避开相应有限和集是充分方式，但本稿不要求用该较强方式。也不假定 \(L\subset F+F\)：后面的导数尾界允许 \(L\) 包含其它频率。若要求投影场本身实值，可取 \(L=-L,D=-D\)；范数估计对一般固定集合仍成立。

下文构造同一初值的完整光滑 NS 解 \(u\)，定义
\[
g=P_Lu,\qquad
S(t)=\int_0^tE_\nu(t-s)P_DB(g(s),g(s))\,ds,
\]
\[
W(t)=\int_0^tE_\nu(t-s)P_DB(v_1(s),v_1(s))\,ds,
\]
\[
M(t)=\int_0^tE_\nu(t-s)P_D
\bigl[B(v_0(s),v_2(s))+B(v_2(s),v_0(s))\bigr]\,ds.
\tag{GS.4}
\]
准确恒等式是 \(P_Dv_3=W+M\)。不能把未投影的全场 \(v_3\) 与仅在 \(D\) 上定义的两项混同。

## 2. 任意有限支持的全阶收敛与真实方程

令 \(\Sigma_m\) 是 \(F\) 中 \(m\) 个元素的全部有序和所形成的集合。完整递归给
\[
\operatorname{supp}v_n(t)\subset\Sigma_{n+1},
\qquad |k|\le(n+1)K\quad(k\in\Sigma_{n+1}).
\tag{GS.5}
\]
频率碰撞在卷积中真实相加。这个结论只用有限支持，不用任何基频独立性。

记 Wiener 范数与一阶齐次半范数
\[
\|f\|_{\mathcal A_m}=\sum_k(1+|k|)^m|f_k|,
\qquad \|f\|_{\mathcal A}=\|f\|_{\mathcal A_0},
\qquad |f|_{\dot{\mathcal A}_1}=\sum_k|k|\,|f_k|.
\]
Leray 的算子范数不超过一，故
\[
\|B(f,g)\|_{\mathcal A}\le
\|f\|_{\mathcal A}|g|_{\dot{\mathcal A}_1}.
\tag{GS.6}
\]
在第 \(n\) 门、分拆为 \(j,n-1-j\) 的项里，导数落第二输入，其最大频率为 \((n-j)K\)。因此
\[
\|v_n(t)\|_{\mathcal A}
\le K\sum_{j=0}^{n-1}(n-j)
\int_0^t\|v_j(s)\|_{\mathcal A}
\|v_{n-1-j}(s)\|_{\mathcal A}\,ds.
\tag{GS.7}
\]

令 \(c_0=1\)、\(c_n=\sum_{j=0}^{n-1}c_jc_{n-1-j}\)。这是平面有序二叉树的计数；递归编码为“左括号、左子树、右括号、右子树”，给长度 \(2n\) 的二进制串单射，故 \(c_n\le4^n\)。对称配对 \(j\leftrightarrow n-1-j\) 只用于上界中的标量和，给
\[
\sum_{j=0}^{n-1}(n-j)c_jc_{n-1-j}
=\frac{n+1}{2}c_n.
\]
时间积分除以 \(n\)，且 \((n+1)/(2n)\le1\)，从 GS.7 归纳得到
\[
\|v_n(t)\|_{\mathcal A}
\le c_n A^{n+1}(Kt)^n\le A q(t)^n,
\qquad q(t)=4AKt.
\tag{GS.8}
\]
另保留第一门的较紧界
\[
\|v_1(t)\|_{\mathcal A}\le A^2Kt=\frac A4q(t).
\tag{GS.9}
\]
正黏性热半群在这里按收缩估计，实际响应中的全部热因子仍保留。

置
\[
T_{\rm sb}=\frac1{8AK},\qquad 0\le t\le T_{\rm sb},
\qquad 0\le q(t)\le\frac12.
\tag{GS.10}
\]
于是完整级数 \(u=\sum_{n\ge0}v_n\) 在 \(C_t\mathcal A\) 绝对一致收敛，且
\[
\|u(t)\|_{\mathcal A}\le\frac A{1-q},\qquad
\left\|u(t)-\sum_{n=0}^Nv_n(t)\right\|_{\mathcal A}
\le\frac{Aq^{N+1}}{1-q}\quad(N\ge0).
\tag{GS.11}
\]
全部高阶范数在同一窗口满足
\[
\|v_n(t)\|_{\mathcal A_m}
\le A[1+(n+1)K]^m q^n,
\qquad
\|u(t)\|_{\mathcal A_m}
\le\frac{A(1+K)^m m!}{(1-q)^{m+1}},
\]
\[
\left\|u(t)-\sum_{n=0}^Nv_n(t)\right\|_{\mathcal A_m}
\le
\frac{A[1+(N+2)K]^m m!\,q^{N+1}}{(1-q)^{m+1}}.
\tag{GS.12}
\]
后两式用 \((r+1)^m\le m!\binom{r+m}{m}\) 及其幂级数；对尾部令 \(n=N+1+r\)。这与旧 SB 方法相同，所需输入仅为 GS.5。

为核清实际解资格，完整卷积还给
\[
\|B(f,g)\|_{\mathcal A_m}
\le\|f\|_{\mathcal A_m}\|g\|_{\mathcal A_{m+1}}.
\]
GS.12 使 \(\sum_n\nu\Delta v_n\) 及全部双重非线性和在每阶范数绝对一致收敛；可逐阶微分递归并换序，得到
\[
u\in C_t\mathcal A_m\cap C_t^1\mathcal A_m,\qquad
u_t=\nu\Delta u+B(u,u),\qquad u(0)=a
\tag{GS.13}
\]
对每个 \(m\) 成立，初始端点取右导数。继续对方程求导只使用有限个更高空间阶，给同窗光滑性。

无散第一输入允许导数移到输出，因而
\[
\|E_\nu(\tau)B(f,g)\|_{\mathcal A}
\le(\nu\tau)^{-1/2}\|f\|_{\mathcal A}\|g\|_{\mathcal A}.
\tag{GS.14}
\]
两条已存在的同数据连续 mild 解在足够短重叠区间上的差，由系数
\(2\sqrt{h/\nu}(M_u+M_{\widetilde u})<1\) 控制；有限分段给共同窗口唯一性。存在性来自 GS.8–13，不循环依赖这个未知解比较范数。

实值共轭与无散由完整算子保持，均值等于初始均值。零均值压力精确恢复为
\[
p_k=-\frac1{|k|^2}\sum_{r+s=k}(k\cdot u_r)(k\cdot u_s)
\quad(k\ne0),\qquad p_0=0.
\tag{GS.15}
\]
每阶绝对收敛支付压力光滑性，并恢复
\(u_t-\nu\Delta u+(u\cdot\nabla)u+\nabla p=0\)。
所以这里是同一固定数据的完整 NS 解，不是 Galerkin 系统或只满足 Poisson 关系的场族。

## 3. 真实第一带及来源误差的显式四阶预算

由 GS.3，
\[
e:=g-v_1=P_L\sum_{n\ge2}v_n.
\]
GS.5、GS.8 给
\[
\|e(t)\|_{\mathcal A}\le\frac{Aq^2}{1-q}\le2Aq^2,
\]
\[
|e(t)|_{\dot{\mathcal A}_1}
\le AK\sum_{n\ge2}(n+1)q^n
=AK\,\frac{q^2(3-2q)}{(1-q)^2}
\le8AKq^2.
\tag{GS.16}
\]
最后一个上界用
\((3-2q)/(1-q)^2=(1-q)^{-2}+2(1-q)^{-1}\le8\)。
这不假设 \(P_Lv_2=0\)：没有奇偶性时，误差从二阶开始。

GS.5、GS.9 另给
\[
|v_1(t)|_{\dot{\mathcal A}_1}\le2K\|v_1(t)\|_{\mathcal A}
\le\frac{AK}{2}q.
\]
完整有序差是
\[
B(g,g)-B(v_1,v_1)=B(e,v_1)+B(v_1,e)+B(e,e).
\tag{GS.17}
\]
由 GS.6、GS.9、GS.16，三个项合计至多
\[
A^2K\,[3q(s)^3+16q(s)^4].
\]
对真实热积分使用收缩及 \(q(s)=q(t)s/t\)，得到
\[
\|S(t)-W(t)\|_{\mathcal A}
\le A q^4\left(\frac3{16}+\frac45q\right)
\le\frac{47}{80}Aq^4
=C_S t^4,
\qquad C_S=\frac{752}{5}A^5K^4.
\tag{GS.18}
\]
这条源误差使用整个 \(g=P_Lu\)，包含所有后续反馈。没有把 \(L\) 外反馈从原方程删除；投影只定义本次来源观测。

GS.3 与 GS.11 给另一条不同的尾界
\[
P_Du=W+M+R_D,\qquad
\|R_D(t)\|_{\mathcal A}
\le\frac{Aq^4}{1-q}\le2Aq^4
=C_Dt^4,\qquad C_D=512A^5K^4.
\tag{GS.19}
\]
GS.18 是真实来源与有限四叶自作用之差，GS.19 是真实目标与全部四叶响应之差；二者不能相互替代。

## 4. 完整四叶树的热核与首项差

定义有限空间场
\[
a_1=B(a,a),\qquad
a_2=\frac12[B(a,a_1)+B(a_1,a)],
\]
\[
W_0=\frac13P_DB(a_1,a_1),\qquad
M_0=\frac13P_D[B(a,a_2)+B(a_2,a)].
\tag{GS.20}
\]
这些归一化使 \(t^3W_0,t^3M_0\) 正好是把有限树中全部热因子置为一后的响应。它们只是首系数，不以另一个 Euler 解替代当前 NS 解。

四叶三门共有五棵平面有序树：一棵 \(2+2\) 树形成 \(W\)，四棵 \(1+3\) 或 \(3+1\) 树形成 \(M\)。每一个有序门、每一个叶频率及每一份 Leray 都保留。对一棵树的固定叶频率和合法门时间，全部热因子可写为
\[
\exp(-\nu\mathcal H),\qquad
\mathcal H=\sum_{\text{树边 }\ell}|k_\ell|^2\,\Delta t_\ell.
\]
在任一中间时间，尚在传播的边将四个叶分成互不交的后代组。若其叶数为 \(m_\ell\)，则
\(|k_\ell|\le m_\ell K\)、\(\sum_\ell m_\ell=4\)，故
\[
0\le\mathcal H
\le\int_0^t K^2\sum_\ell m_\ell^2\,ds
\le16K^2t,\qquad
|e^{-\nu\mathcal H}-1|\le16\nu K^2t.
\tag{GS.21}
\]
这包括叶热演化、中间传播和根输出传播，不只是最后一段热核。零中间频率的门已为零，可以保留在绝对上界中。

现在估计去掉热因子后的逐树绝对和，不能先用相消后的 \(M_0\) 范数。每个门的导数因子至多为第二子树叶数乘 \(K\)，Leray 范数至多一，所有叶频率的绝对乘积和为 \(A^4\)。

平衡树的三个导数因子乘积是 \(2K^3\)，两个子门时间均在根门时间 \(s\) 以下，其时间体积为
\(\int_0^t s^2\,ds=t^3/3\)。因此该树绝对和至多
\((2/3)A^4K^3t^3\)。

四棵链形树的导数因子乘积依次为
\(6K^3,3K^3,2K^3,K^3\)：前两棵根的第二子树有三叶，后两棵根的第二子树仅一叶。每棵链的三个门时间有全序，体积为 \(t^3/6\)。四棵合计至多
\(2A^4K^3t^3\)。这里列的是符号树上界，不执行树或频率枚举。

将逐树绝对和乘 GS.21，得到对整个所述窗口有效的严格界
\[
\boxed{\|W(t)-t^3W_0\|_{\mathcal A}\le C_Wt^4,
\qquad C_W=\frac{32}{3}\nu A^4K^5,}
\]
\[
\boxed{\|M(t)-t^3M_0\|_{\mathcal A}\le C_Mt^4,
\qquad C_M=32\nu A^4K^5.}
\tag{GS.22}
\]
因此全部四叶响应还满足
\[
\|P_Dv_3(t)-t^3(W_0+M_0)\|_{\mathcal A}
\le\frac{128}{3}\nu A^4K^5t^4.
\tag{GS.23}
\]
首系数中的任何精确相消不影响这份绝对误差预算。反之，首系数相消本身不意味着正时间有限树恒零。

## 5. 条件相消后的明确相对来源窗口

现在另加必须由具体数据独立核验的条件
\[
M_0=0,\qquad w_*:=\|W_0\|_{\mathcal A}>0.
\tag{GS.24}
\]
则 GS.18–19、GS.22 给
\[
\|P_Du(t)-S(t)\|_{\mathcal A}\le C_Et^4,
\qquad
C_E=C_D+C_M+C_S
=\frac{3312}{5}A^5K^4+32\nu A^4K^5.
\tag{GS.25}
\]
这里 \(W(t)\) 在真实目标与真实来源的比较中精确相消，不重复加入 \(C_W\)。

分母需要另行支付：
\[
\|S(t)-t^3W_0\|_{\mathcal A}\le C_{\rm src}t^4,
\qquad C_{\rm src}=C_S+C_W,
\]
\[
\|P_Du(t)-t^3W_0\|_{\mathcal A}\le C_{\rm tar}t^4,
\qquad C_{\rm tar}=C_D+C_M+C_W.
\tag{GS.26}
\]
置 \(H_*=\max\{C_{\rm src},C_{\rm tar}\}>0\)。对任意事先指定的容限 \(\eta>0\)，定义未求值的解析时间窗
\[
\boxed{
T_\eta=\min\left\{
\frac1{8AK},\ \frac{w_*}{2H_*},\
\frac{\eta w_*}{4C_E}
\right\}>0.}
\tag{GS.27}
\]
全部分母严格为正；\(W_0\ne0\) 已排除零或常值初值退化。对每个 \(0<t\le T_\eta\)，反三角不等式给
\[
\|S(t)\|_{\mathcal A}\ge\frac{w_*}{2}t^3,\qquad
\|P_Du(t)\|_{\mathcal A}\ge\frac{w_*}{2}t^3.
\]
从而两种常用的相对来源误差均有严格上界
\[
\boxed{
\frac{\|P_Du(t)-S(t)\|_{\mathcal A}}{\|S(t)\|_{\mathcal A}}
\le\frac{\eta}{2}<\eta,\qquad
\frac{\|P_Du(t)-S(t)\|_{\mathcal A}}{\|P_Du(t)\|_{\mathcal A}}
\le\frac{\eta}{2}<\eta.}
\tag{GS.28}
\]
这是真实同一原解、全部 \(0<t\le T_\eta\) 的条件短窗结论。它不是只在某个离散时刻成立，也没有把解析范数或时间窗伪报为已求值数值证书。

## 6. 实际来源与未付范围

本稿独立使用的旧源路径相对于 /Users/kasifa/Documents/Math/navier-stokes-reverse/：

| 来源 | 本轮实际读取范围 | 实测 SHA-256 |
|---|---|---|
| research/reverse/mixed-polarization/SOURCE_BRIDGE_INDEPENDENT.md | 第1–248行，SB.1–4 全文及下一节标题；只复用有限支持、叶数上界、全阶收敛和经典性方法，不用后续奇偶性 | 1d3d33fbb8fcc17ac1266f2ee88c88eebe328867f385277a0a684cfa2247630a |
| research/reverse/reconnection-preflight/SOURCE_ATTRIBUTION_LEMMA.md | 第173–225行，§4 全文；复核完整 Wiener 构造与同数据/解析常数边界。本稿的存在窗另由 GS.8–13 直接给出 | d22bcca237977647b54ebbe13288c63a24a7c610a52a7c2265f4e3cfe366607a |

我有这些旧源的既往审查经历，本轮实际重读并重新核清一般化所需的条件。没有新读外部原文，不主张一般 Wiener 原理、有限树首项或本地接口的外部新颖性。

本引理只在 GS.3、GS.24 全部实际成立时工作。它没有核验根准备的具体四组数据，没有选择其中任何频率或幅度，也没有以无黏首项的支撑替代完整响应的支撑。若碰撞导致低阶目标非零、第一带不完整、\(M_0\ne0\) 或 \(W_0=0\)，本稿不提供该相对来源结论。

即使所有条件成立，GS.28 也只支付这份固定初值的第一短窗来源归因。它不证明把 \(g\) 重新当作原种子合法，不付下一代重置、共同复制形状、统一迭代、固定初值无限尺度、无限维跨代误差或有限总时间奇性。旧实际初值及旧失败证据不因此改判。本稿完成全文自读及源字节终核后停改，最终 SHA-256 由任务消息报告。
