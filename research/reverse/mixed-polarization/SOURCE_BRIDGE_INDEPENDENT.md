# 固定三对初值的全叶数收敛与真实自供给：独立短窗桥接

2026-09-08，PRIVATE_CORE。状态：**独立稿，待非作者全文审查；没有接受再生成或奇性候选。**

本项从 `SOURCE_BRIDGE_CONTRACT.md` 自行推导。完整读取旧 `SOURCE_ATTRIBUTION_LEMMA.md`，定向读取 `first-cycle/PROOF.md` 第 80–140 行（覆盖第 3 节全文），沿用本代理已经全文自核的 `MIXED_ROOT_INDEPENDENT.md`。未读本轮 `SOURCE_BRIDGE_PROOF.md` 或其他本轮推导。旧文中的实际数值、初值选择及后续节结论未用于本稿。

本地旧文已经给出 Wiener 局部存在和条件来源估计；本稿不将这些原则称为新定理。这里具体支付合同中的全叶数级数收敛、同一三对数据的叶数奇偶尾部，以及 \(g=P_{\mathcal L}u\) 的真实自供给误差。全部手工符号，无科学程序、计算数组、数值求值、扫描、Git、外发或额度重置；本项仅写入本独占稿。

## SB.1 固定数据、全部响应与算子约定

固定同一份初值
\[
a(x)=\sum_{i=1}^3\left(U_i e^{ip_i\cdot x}
+\overline{U_i}e^{-ip_i\cdot x}\right),
\qquad p_i\in\mathbb Z^3,
\quad U_i\cdot p_i=0,
\quad U_i\ne0,
\tag{SB.1}
\]
其中 \(p_1,p_2,p_3\) 线性独立。保持单位黏性、无外力和三维 \(2\pi\) 环面。定义该固定数据的解析常数
\[
A=\sum_k|a_k|=2\sum_{i=1}^3|U_i|>0,
\qquad K=\max_i|p_i|>0.
\tag{SB.2}
\]
向量长度为 Hermitian 欧氏范数；卷积中的点积仍为复双线性点积。没有给 \(p_i,U_i,A,K\) 选取实际值。

用 \(\mathbb P_k=I-k\otimes k/|k|^2\) 表示非零频率的 Leray 投影，定义有序双线性作用
\[
B(f,g)_k=-i\mathbb P_k\sum_{r+s=k}(f_r\cdot s)g_s,
\qquad k\ne0.
\tag{SB.3}
\]
当第一输入无散时，零模卷积逐项为零，规定 \(B(f,g)_0=0\)。对频率集合 \(E\)，\(P_E\) 表示只保留该集合的 Fourier 投影。它与 Leray 投影不同；本稿用 \(\mathbb P\) 避免与旧来源中的 Leray 记号混淆。

置 \(E(t)=e^{t\Delta}\)，在全部频率上递归定义
\[
v_0(t)=E(t)a,
\]
\[
v_n(t)=\sum_{j=0}^{n-1}\int_0^t
E(t-s)B(v_j(s),v_{n-1-j}(s))\,ds,
\qquad n\ge1.
\tag{SB.4}
\]
\(v_n\) 有 \(n+1\) 个叶、\(n\) 个非线性门。每一项都使用 SB.1 的同一个固定 \(a\)，完整保留有序项、负模共轭、黏性及 Leray。以下证明是这组精确定义的积分的实际收敛，不以形式参数级数或 Galerkin 截断代替。

## SB.2 叶数支撑与逐阶上界

记
\[
\Sigma_m=\left\{\sum_{r=1}^m\varepsilon_r p_{i_r}:
\varepsilon_r=\pm1,\quad i_r\in\{1,2,3\}\right\}.
\]
由精确卷积和热半群不改变支撑，归纳得
\[
\operatorname{supp}v_n(t)\subseteq\Sigma_{n+1},
\qquad |k|\le(n+1)K\quad(k\in\operatorname{supp}v_n).
\tag{SB.5}
\]
每阶支撑有限，但阶数没有截断；不同表示的频率碰撞在卷积中真实相加。

定义 Wiener 范数
\[
\|f\|_{\mathcal A_m}=\sum_k(1+|k|)^m|f_k|,
\qquad \mathcal A=\mathcal A_0.
\tag{SB.6}
\]
由于 \(\|\mathbb P_k\|\le1\)，有完整卷积界
\[
\|B(f,g)\|_{\mathcal A}\le
\|f\|_{\mathcal A}\sum_s|s|\,|g_s|.
\tag{SB.7}
\]
在 SB.4 的 \((j,n-1-j)\) 项中，右输入支撑不超过 \((n-j)K\)。因此如果记 \(b_n(t)=\|v_n(t)\|_{\mathcal A}\)，热收缩给
\[
b_n(t)\le K\sum_{j=0}^{n-1}(n-j)
\int_0^t b_j(s)b_{n-1-j}(s)\,ds.
\tag{SB.8}
\]
这是已知有限叶数支撑支付的导数因子，不是未知真实轨道的高阶范数。

令 Catalan 标量数 \(c_0=1\)、
\[
c_n=\sum_{j=0}^{n-1}c_jc_{n-1-j}.
\]
标量生成式 \(C=1+zC^2\) 的常数项为一的分支，展开为
\[
c_n=\frac1{n+1}\binom{2n}{n}\le4^n.
\tag{SB.9}
\]
这个标量恒等式只用于显式上界；下文另行证明实际向量级数收敛。

从 \(b_0\le A\) 出发，SB.8 给出归纳界
\[
\boxed{b_n(t)\le c_n A^{n+1}(Kt)^n.}
\tag{SB.10}
\]
为核清叶数因子，若低阶满足该界，右侧至多
\[
\frac{A^{n+1}(Kt)^n}{n}
\sum_{j=0}^{n-1}(n-j)c_jc_{n-1-j}.
\]
用 \(j\leftrightarrow n-1-j\) 对称同一个标量和，得到
\[
\sum_{j=0}^{n-1}(n-j)c_jc_{n-1-j}
=\frac{n+1}{2}c_n.
\]
因此所需系数为 \((n+1)/(2n)\le1\)，包括 \(n=1\) 的等号，归纳闭合。这里的对称求和只发生在上界；精确的有序 \(B\) 没有被替换成对称算子或乘二。

特别地
\[
\boxed{\|v_n(t)\|_{\mathcal A}\le A\xi(t)^n,
\qquad \xi(t)=4AKt,}
\tag{SB.11}
\]
而第一层保留更紧的
\[
\|v_1(t)\|_{\mathcal A}\le A^2Kt=\frac A4\xi(t).
\tag{SB.12}
\]
单靠普通 \(\mathcal A\) 热核损一阶估计会给每门半次时间的预算；例如第五门的这种预算不能放在 \(t^3\) 首项之后。SB.5–10 则在每阶直接支付有限频率导数，得到整数次 \(t^n\)。估计中热半群按收缩处理，精确响应本身的黏性未被删除。

## SB.3 明确收敛窗和全 Fourier 尾部

取只依赖 SB.1 固定数据的充分窗口
\[
\boxed{T_{\rm sb}=\frac1{8AK}>0.}
\tag{SB.13}
\]
在 \(0\le t\le T_{\rm sb}\) 上，\(0\le\xi(t)\le1/2\)。于是
\[
\boxed{u(t):=\sum_{n=0}^\infty v_n(t)}
\tag{SB.14}
\]
在 \(C([0,T_{\rm sb}],\mathcal A)\) 绝对一致收敛，且
\[
\|u(t)\|_{\mathcal A}\le\frac A{1-\xi(t)}\le2A.
\tag{SB.15}
\]
全部 Fourier 模式的叶数尾部满足，对 \(N\ge0\)，
\[
\boxed{\left\|u(t)-\sum_{n=0}^Nv_n(t)\right\|_{\mathcal A}
\le\frac{A\xi(t)^{N+1}}{1-\xi(t)}.}
\tag{SB.16}
\]
这是完整频率范数，未固定任何 Galerkin 截断。

SB.5 还给每个非负整数 \(m\) 的同窗估计
\[
\|v_n(t)\|_{\mathcal A_m}
\le A[1+(n+1)K]^m\xi(t)^n.
\tag{SB.17}
\]
用 \((n+1)^m\le m!\binom{n+m}{m}\) 及其标量幂级数，得到
\[
\boxed{\|u(t)\|_{\mathcal A_m}
\le\frac{A(1+K)^m m!}{(1-\xi(t))^{m+1}}.}
\tag{SB.18}
\]
特别地，所有空间导数都在同一个 \(T_{\rm sb}\) 上受控，不为每一导数另缩窗口。

更明确的高阶叶数尾部为
\[
\boxed{\left\|u(t)-\sum_{n=0}^Nv_n(t)\right\|_{\mathcal A_m}
\le\frac{A[1+(N+2)K]^m m!\,\xi(t)^{N+1}}
{(1-\xi(t))^{m+1}}.}
\tag{SB.19}
\]
证明是令 \(n=N+1+r\)，用
\(1+(n+1)K\le[1+(N+2)K](r+1)\)，再对 \(r\) 求和。

若单独需要高频尾部，SB.5 同时给对任意符号截止 \(R\ge K\)
\[
\boxed{\|P_{\{|k|>R\}}u(t)\|_{\mathcal A}
\le\frac{A\xi(t)^{\lfloor R/K\rfloor}}{1-\xi(t)}.}
\tag{SB.20}
\]
因为能供给 \(|k|>R\) 的阶数必须满足 \(n\ge\lfloor R/K\rfloor\)。这只是全解的解析尾界，没有用有限截止定义或认证原解。

## SB.4 无穷求和、经典性、唯一性和周期压力

每个 \(v_n\) 是有限 Fourier 和，其时间系数为精确热积分，故在闭窗口上光滑（端点时间导数取单侧）。逐阶满足
\[
\partial_t v_n=\Delta v_n+
\sum_{j=0}^{n-1}B(v_j,v_{n-1-j})\quad(n\ge1),
\qquad \partial_t v_0=\Delta v_0.
\tag{SB.21}
\]
对每个 \(m\)，SB.17 和 \(\xi(T_{\rm sb})\le1/2\) 使
\[
\sum_n\|\Delta v_n\|_{C_t\mathcal A_m}
\le\sum_n (n+1)^2K^2
A[1+(n+1)K]^m\xi(T_{\rm sb})^n<\infty.
\tag{SB.22}
\]
另外完整有序卷积满足
\[
\|B(f,g)\|_{\mathcal A_m}
\le\|f\|_{\mathcal A_m}\|g\|_{\mathcal A_{m+1}},
\tag{SB.23}
\]
从而
\[
\sum_{j,l\ge0}\|B(v_j,v_l)\|_{C_t\mathcal A_m}
\le\left(\sum_j\|v_j\|_{C_t\mathcal A_m}\right)
\left(\sum_l\|v_l\|_{C_t\mathcal A_{m+1}}\right)<\infty.
\tag{SB.24}
\]
这些绝对一致界允许换序、积分及一次时间微分。对 SB.21 求和，得到同一个 SB.14 的实际方程
\[
\boxed{\partial_tu=\Delta u+B(u,u),\qquad u(0)=a,}
\tag{SB.25}
\]
以及完整 mild 恒等式。所有 \(\mathcal A_m\) 在同窗连续，方程右边在每阶范数连续，所以 \(u\) 在这些范数中 \(C^1\)。继续对方程求时间导数，每次只使用有限个更高空间阶及已知双线性乘积，归纳得到所有时间导数；不需要收缩空间窗口。故 \(u\) 在 \([0,T_{\rm sb}]\times\mathbb T^3\) 光滑。

每阶实值条件、无散和零均值都严格保持：热乘子为实偶函数；完整 Fourier–Leray 作用的负频率是正频率的共轭；所有非零输出经 \(\mathbb P_k\) 横向投影；零模的有序点积由第一输入无散逐项为零。绝对收敛将这些性质传给 \(u\)，覆盖全部正负模。

唯一性也可自包含核清。无散第一输入给 \(f_r\cdot s=f_r\cdot(r+s)\)，故
\[
\|E(\tau)B(f,g)\|_{\mathcal A}
\le\tau^{-1/2}\|f\|_{\mathcal A}\|g\|_{\mathcal A},
\qquad \tau>0.
\tag{SB.26}
\]
对两条同数据 \(C_t\mathcal A\) mild 解，在已经相等的起点之后长度为 \(h\) 的区间内，差满足
\[
\|u-\widetilde u\|_{C_t\mathcal A}
\le2\sqrt h\,(M_u+M_{\widetilde u})
\|u-\widetilde u\|_{C_t\mathcal A},
\]
其中 \(M_u,M_{\widetilde u}\) 是它们在整个有限窗口的有限连续范数。取 \(h\le[16(M_u+M_{\widetilde u})^2]^{-1}\)，系数至多 \(1/2\)；有限分段即得全窗唯一性。这里只为比较两条已经存在的连续解使用其有限范数；存在窗口和 SB.15 的认证完全来自 SB.2–3 的已知 \(A,K\)，没有循环使用未知原解上界。所有光滑解均属于这一唯一性类。

唯一零均值周期压力由全 Fourier 公式恢复：
\[
\boxed{\pi_k(t)=-\frac1{|k|^2}
\sum_{r+s=k}(k\cdot u_r(t))(k\cdot u_s(t)),\quad k\ne0,
\qquad\pi_0=0.}
\tag{SB.27}
\]
有 \(\|\pi\|_{\mathcal A_m}\le\|u\|_{\mathcal A_m}^2\)，空间与时间微分因上面的高阶界合法。因此
\[
\partial_tu-\Delta u+(u\cdot\nabla)u+\nabla\pi=0,
\qquad \nabla\cdot u=0,
\]
以及 \(-\Delta\pi=\partial_i\partial_j(u_i u_j)\) 精确成立。压力没有额外外场参数或任意局部补项。SB.14 因而确实是 SB.1 同一初值的唯一光滑 NS 原解，而非有限响应或条件假设中的未知轨道。

## SB.5 独立频率的叶数奇偶性

在线性独立频率生成的整数子格中，表示
\[
k=m_1p_1+m_2p_2+m_3p_3,\qquad m_i\in\mathbb Z,
\]
是唯一的。每个 \(n+1\) 叶频率的坐标满足
\[
m_1+m_2+m_3\equiv n+1\pmod2.
\tag{SB.28}
\]
负叶的 \(-1\) 与正叶的 \(+1\) 在模二意义相同，因此此式包括全部共轭分支。

定义合同中的
\[
D=\{\pm2p_i:i=1,2,3\},
\]
\[
\mathcal L=\{\sigma p_i+\tau p_j:i<j,\ \sigma,\tau=\pm1\}.
\tag{SB.29}
\]
这两集合的坐标总和均为偶数。因此
\[
\boxed{P_Dv_n=P_{\mathcal L}v_n=0\quad\text{当 }n\text{ 为偶数}.}
\tag{SB.30}
\]
第一层同轴配对因横向点积逐项为零，所以 \(v_1\) 的全部支撑包含于 \(\mathcal L\)。线性独立性使 \(D\cap\mathcal L=\varnothing\)，从而
\[
P_Dv_1=0,\qquad P_{\mathcal L}v_1=v_1.
\tag{SB.31}
\]
真实原解投影于是具有绝对收敛的精确展开
\[
\boxed{P_Du=P_Dv_3+\sum_{r=0}^\infty P_Dv_{5+2r},}
\]
\[
\boxed{g:=P_{\mathcal L}u=v_1+
\sum_{r=0}^\infty P_{\mathcal L}v_{3+2r}.}
\tag{SB.32}
\]
这里 \(g\) 是本合同的同一真实轨道频带投影，与旧来源引理中“在某时间切点取全部历史再热续演”的 \(g\) 定义不同；没有把旧来源标签直接移植过来。

置
\[
\delta(t)=1-\xi(t)^2>0.
\]
SB.11 与奇偶性给出本合同的前两份无限维预算：
\[
\boxed{\|P_Du(t)-P_Dv_3(t)\|_{\mathcal A}
\le\varepsilon_D(t):=\frac{A\xi(t)^5}{\delta(t)},}
\tag{SB.33}
\]
\[
\boxed{\|g(t)-v_1(t)\|_{\mathcal A}
\le\varepsilon_g(t):=\frac{A\xi(t)^3}{\delta(t)}.}
\tag{SB.34}
\]
这分别是带明确常数的五次和三次时间界；它们是完整无穷和尾部，不是有限树内部误差。

## SB.6 实际前代的真实自供给预算

按合同定义
\[
\mathcal S(t)=\int_0^t E(t-s)P_D B(g(s),g(s))\,ds,
\]
\[
W(t)=P_Dw_{22}(t)
=\int_0^t E(t-s)P_D B(v_1(s),v_1(s))\,ds.
\tag{SB.35}
\]
这里 \(g\) 是 SB.32 的实际轨道分量，未被假定等于自由指定的新种子。令 \(h=g-v_1\)，完整有序差为
\[
\boxed{\mathcal S-W=\int_0^t E(t-s)P_D
[B(v_1,h)+B(h,v_1)+B(h,h)](s)\,ds.}
\tag{SB.36}
\]
三个有序项全部保留；在恒等式中没有将前两项合并成 \(2B(v_1,h)\)。

对任何无散 \(f\in\mathcal A\) 和 \(z\in\mathcal A\)，把导数移到输出频率后，因 \(k\in D\) 满足 \(|k|\le2K\)，有
\[
\boxed{\|P_D B(f,z)\|_{\mathcal A}
\le2K\|f\|_{\mathcal A}\|z\|_{\mathcal A}.}
\tag{SB.37}
\]
该界不删除输入的任何频率。此处 \(g,h,v_1\) 都无散且支撑于 \(\mathcal L\)，也可直接用右输入频率不超过 \(2K\) 得到相同界。

对固定的符号终点 \(t\le T_{\rm sb}\)，令 \(b=4AK\)，则 \(\xi(s)=bs\)，且 \(1-\xi(s)^2\ge\delta(t)\) 对 \(s\le t\) 成立。用 SB.12、SB.34 得
\[
\begin{aligned}
\|\mathcal S(t)-W(t)\|_{\mathcal A}
&\le2K\int_0^t
\left[2\|v_1(s)\|_{\mathcal A}\|h(s)\|_{\mathcal A}
+\|h(s)\|_{\mathcal A}^2\right]ds\\
&\le2KA^2\int_0^t
\left[\frac{(bs)^4}{2\delta(t)}
+\frac{(bs)^6}{\delta(t)^2}\right]ds\\
&=\frac{KA^2b^4t^5}{5\delta(t)}
+\frac{2KA^2b^6t^7}{7\delta(t)^2}.
\end{aligned}
\tag{SB.38}
\]
因此第三份真实无限维预算为
\[
\boxed{\|\mathcal S(t)-P_Dw_{22}(t)\|_{\mathcal A}
\le\varepsilon_S(t):=
A\left[\frac{\xi(t)^5}{20\delta(t)}
+\frac{\xi(t)^7}{14\delta(t)^2}\right].}
\tag{SB.39}
\]
这里既控制 \(v_1\) 与真实偏差的双向作用，也控制偏差的自作用。没有使用未知原解范数或未经估计的 \(O\) 项。

SB.33、SB.34 和 SB.39 的误差场分别支撑在 \(D,\mathcal L,D\)，各模式长度不超过 \(2K\)。因此相同界乘以 \((1+2K)^m\) 就在每个 \(\mathcal A_m\) 成立，时间次数不变。

## SB.7 与完整四叶接收的真实归因接口

定义完整有限树的两个 \(D\) 频带向量
\[
W(t)=P_Dw_{22}(t),\qquad
M(t)=P_Dv_3(t)-W(t).
\tag{SB.40}
\]
\(M\) 包含本人上一独立稿已经穷尽的全部 \(1+3/3+1\) 根；每行先合计同一组三对种子的全部 \(j\) 通道及各自热核，再组成全部正负接收向量。没有将一条边独立自由化。

以 \(R_D=P_Du-P_Dv_3\)、\(R_S=\mathcal S-W\)，精确地
\[
\boxed{P_Du=W+M+R_D,\qquad
\mathcal S=W+R_S,\qquad
P_Du-\mathcal S=M+R_D-R_S.}
\tag{SB.41}
\]
故
\[
\boxed{\|P_Du(t)-\mathcal S(t)-M(t)\|_{\mathcal A}
\le\varepsilon_D(t)+\varepsilon_S(t).}
\tag{SB.42}
\]
这完成有限四叶系数与同一原解的来源误差接口。它不把 \(M\) 假定为小量；其真实三次首项可以与 \(W\) 同阶。

另外，若 \(r=u-g\) 为实际余下频率的场，则 \(P_DE(t)a=0\) 给出真实原解的完整有序来源恒等式
\[
P_Du(t)=\mathcal S(t)+\int_0^t E(t-s)P_D
[B(g,r)+B(r,g)+B(r,r)](s)\,ds.
\tag{SB.43}
\]
\(g\) 和 \(r\) 都来自同一 \(u\)；\(B(g,g)\) 不是独立无外力 NS 解，其他频率没有被删除。这些积分来源可以在同一接收模干涉，不能把它们当作正交的代际能量而删去交叉项。

对任何本窗内符号 \(t>0\)，以下下界始终成立。要据此断言对应真实量非零，须核对同一组三对总向量给出的右侧严格为正：
\[
\|\mathcal S(t)\|_{\mathcal A}
\ge\|W(t)\|_{\mathcal A}-\varepsilon_S(t),
\]
\[
\|P_Du(t)-\mathcal S(t)\|_{\mathcal A}
\ge\|M(t)\|_{\mathcal A}-\varepsilon_D(t)-\varepsilon_S(t),
\]
\[
\|P_Du(t)\|_{\mathcal A}
\ge\|W(t)+M(t)\|_{\mathcal A}-\varepsilon_D(t).
\tag{SB.44}
\]
相应上界同样由三角不等式给出。单边非零或前项单对的正比值，不能替代这里 \(W,M,W+M\) 在全部三对接收中的真实非零和相消间隙。

## SB.8 可核的三次总向量短窗条件

为把“足够小”也写成可复核条件，可沿用本人上一独立稿的有限树显式常数。本节只使用该稿 MI.10–41 的完整 Leray 代数与正积分界：其分母仅含非零的 \(P,Q,\lambda_\pm,E_\pm,\Lambda\)，未除以 \(d=P-Q\)。因此本合同若出现等长频率对，令 \(d=0\) 后同一投影等式仍直接成立；无需为本桥接定理增加长度互异假设。该稿的 \(P>Q\) 平面非零检验及单对比值不在本节使用。

按其中记号，设 \(C_{ij}\) 是完整 \(2+2\) 空间向量，\(D_{ij,\sigma}\) 是完整混合根向量，\(\mu_{22,ij},\mu_{ij,\sigma}\) 是相应正热作用量上界。定义支持在 \(D\) 的总向量 \(W_0,M_0\)，其正模为
\[
(W_0)_{2p_i}=\frac13\sum_{j\ne i}C_{ij},
\qquad
(M_0)_{2p_i}=\frac16\sum_{j\ne i}\sum_{\sigma=\pm1}D_{ij,\sigma},
\tag{SB.45}
\]
负模为完整共轭。每个分量中的求和发生在取范数之前。

显式有限树预算可取
\[
B_W=\frac23\sum_i\sum_{j\ne i}\mu_{22,ij}|C_{ij}|,
\]
\[
B_M=\frac13\sum_i\sum_{j\ne i}\sum_{\sigma=\pm1}
\mu_{ij,\sigma}|D_{ij,\sigma}|.
\tag{SB.46}
\]
这里系数中的二包括全部负接收。上一稿的正积分界直接给
\[
\|W(t)-t^3W_0\|_{\mathcal A}\le B_Wt^4,
\qquad
\|M(t)-t^3M_0\|_{\mathcal A}\le B_Mt^4.
\tag{SB.47}
\]

在本窗 \(\xi\le1/2\) 上，可将真实尾部粗化为仍显式的常数界
\[
\varepsilon_D(t)\le C_Dt^5,
\quad C_D=\frac43A(4AK)^5,
\]
\[
\varepsilon_S(t)\le C_St^5,
\quad C_S=A(4AK)^5.
\tag{SB.48}
\]
第二式例如由 \(\delta\ge3/4\) 和
\(1/(20\delta)+\xi^2/(14\delta^2)
\le1/15+2/63<1\) 直接得到。

于是
\[
\boxed{\|\mathcal S(t)-t^3W_0\|_{\mathcal A}
\le B_Wt^4+C_St^5,}
\]
\[
\boxed{\|P_Du(t)-\mathcal S(t)-t^3M_0\|_{\mathcal A}
\le B_Mt^4+(C_D+C_S)t^5,}
\]
\[
\boxed{\|P_Du(t)-t^3(W_0+M_0)\|_{\mathcal A}
\le(B_W+B_M)t^4+C_Dt^5.}
\tag{SB.49}
\]
这些是全三对接收向量的严格界，没有未估计的短时间余项。

例如，**若**同一固定数据的总向量满足 \(w=\|W_0\|_{\mathcal A}>0\)，则在明确窗口
\[
0<t\le\min\left\{T_{\rm sb},\frac{w}{4B_W},
\sqrt{\frac{w}{4C_S}}\right\},
\tag{SB.50}
\]
有 \(\|\mathcal S(t)\|_{\mathcal A}\ge wt^3/2>0\)。其中 \(B_W=0\) 时对应分式约定为 \(+\infty\)。同理，**若** \(m=\|M_0\|_{\mathcal A}>0\)，则在
\[
0<t\le\min\left\{T_{\rm sb},\frac{m}{4B_M},
\sqrt{\frac{m}{4(C_D+C_S)}}\right\}
\tag{SB.51}
\]
有 \(\|P_Du(t)-\mathcal S(t)\|_{\mathcal A}\ge mt^3/2>0\)，对 \(B_M=0\) 使用同一约定。

若 \(W_0\ne0\)，SB.49 还直接给
\[
\frac{\|P_Du(t)-\mathcal S(t)\|_{\mathcal A}}
{\|\mathcal S(t)\|_{\mathcal A}}
\longrightarrow
\frac{\|M_0\|_{\mathcal A}}{\|W_0\|_{\mathcal A}}
\quad(t\downarrow0).
\tag{SB.52}
\]
这里分子中的 \(M_0\) 是所有接收模的总向量。没有以先前单对比值断言它非零。若 \(W_0=0\)、\(M_0=0\) 或 \(W_0+M_0=0\)，相应判断必须保留真实相消并另核更高阶；本稿不分类这些数据。

## SB.9 范围与未付结论

本稿在 SB.13 的明确窗口内，为任意一份事先固定的合同三对数据证明全叶数响应的全 Fourier 绝对收敛、同一原解的光滑经典性与唯一性，以及 SB.33、SB.34、SB.39 三份真实无穷尾部预算。旧来源中的 Wiener 原则被明确承认；本稿没有新增文献适用性或新颖性声明。

有限树到真实轨道的这一短窗误差已在所述范围内支付，但“真实前代投影”只表示 \(g=P_{\mathcal L}u\) 的精确定义。它不认证物理涡管纯度、形态再生或自供给占优；后者仍需同一组三对的 \(W,M,W+M\) 或其三次总向量通过实际非零与相消间隙。没有选择实际数据或时间，没有候选通过，也没有把发送协方差逐边独立化。

\(T_{\rm sb}\) 随该固定数据的 \(A,K\) 而变。本稿不提供跨代统一窗口、跨尺度统一误差或可迭代结构；不证明同一初值无限尺度、有限总时间、奇性或全局正则性，不交换 \(\forall N\,\exists u_{0,N}\) 与 \(\exists u_0\,\forall N\)。NOT CLAY。

## SB.10 实际来源及字节绑定

路径相对于 `research/reverse/`。

| 来源及实际阅读范围 | SHA256 |
|---|---|
| mixed-polarization/SOURCE_BRIDGE_CONTRACT.md，全文 | 32e6c8152c8b42592d84b9c5809654b9a7528d96d4231bcfe9f2351ebc01ba37 |
| mixed-polarization/MIXED_ROOT_INDEPENDENT.md，本代理前项全文自核，本项核对字节未变 | cad93f863ad371723d4510f20588a0f7abcee3e4f8e2984010f88ebcb2fc2dbf |
| reconnection-preflight/SOURCE_ATTRIBUTION_LEMMA.md，全文 | d22bcca237977647b54ebbe13288c63a24a7c610a52a7c2265f4e3cfe366607a |
| first-cycle/PROOF.md，第 80–140 行；第 3 节在第 86 行开始、第 142 行进入下一节；此列为整文件 SHA | a87672a035f1c80a0225ce8956fca53ffc2eb07fdd4e83092505b4ac657f6120 |

这些来源内部列出的其他稿件或外部文献没有被冒记为本项实读。哈希仅绑定文本，不能替代本轮非作者数学审查。
