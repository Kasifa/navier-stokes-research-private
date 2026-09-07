# 非正交共享前代：独立热因子与第二门适用性预检

2026-09-08，PRIVATE_CORE。状态：**精确有限树公式；旧等长第二门的前提不满足；未接受候选。** 本稿为独立推导，待非作者实读审查。

本轮只完整读取本目录 `PREFLIGHT_CONTRACT.md`，没有读取本轮主预检。下文从完整有序 Fourier–Leray 式自行计算；涉及旧等长门的部分直接重证其所需初等恒等式，不声称本轮重读任何旧论文或旧引理全文。未运行科学程序、数组、指数数值求值、参数搜索或 Git；未选定波向量、极化、时间或实际初值。

## NP.1 同一对原种子与共轭约束

令 \(p,q\in\mathbb Z^3\) 非平行，\(c=p\cdot q\ne0\)，并记
\[
P=|p|^2,\quad Q=|q|^2,\quad S=P+Q,\quad
k_+=p+q,\quad k_-=p-q,\quad
\lambda_\pm=|k_\pm|^2=S\pm2c.
\]
非平行性给 \(P,Q>0\)、\(c^2<PQ\)，故 \(k_\pm\ne0\)、\(\lambda_\pm>0\)，且 \(k_+,k_-\) 也非平行。取同一对复横向种子
\[
p\cdot U=0,\qquad q\cdot V=0,
\]
负模严格为 \(\overline U,\overline V\)。本节只处理这对种子的贡献；若未来加入其他种子，任何额外配对仍须另计，不能默认不存在。

采用
\[
B(f,g)_k=-iP_k\sum_{r+s=k}(f_r\cdot s)g_s,
\qquad P_k=I-\frac{k\otimes k}{|k|^2}.
\]
点积在复向量上按双线性延拓，不在有序作用中额外取复共轭。全部两种有序输入分别给
\[
N_+=-iP_{k_+}\bigl[(U\cdot q)V+(V\cdot p)U\bigr],
\tag{NP.1}
\]
\[
N_-=-iP_{k_-}\bigl[-(U\cdot q)\overline V+(\overline V\cdot p)U\bigr].
\tag{NP.2}
\]
所以 \(N_+\perp k_+\)、\(N_-\perp k_-\)。\(N_-\) 一般不是 \(\overline{N_+}\)：它仅翻转了 q 种子，不能连 p 种子一起共轭。真正负输出满足 \(N_{-k_\pm}=\overline{N_\pm}\)。同轴种子配对，包括相反频率，因横向点积而逐项为零。

NP.1–2 使两个前代严格共享同一个 \(U,V\)。以下没有把 \(N_+,N_-\) 作为可独立调节的输入，也不假设它们非零。

## NP.2 第一层树的精确热因子

固定 \(\nu=1\)，记 \(v_0(t)=e^{t\Delta}a\)，
\[
v_1(t)=\int_0^t e^{(t-s)\Delta}B(v_0(s),v_0(s))\,ds.
\]
两种符号的输入乘积都带热率 \(S=P+Q\)，但输出热率分别为 \(\lambda_\pm\)。因此
\[
(v_1)_{k_\pm}(t)=F_\pm(t)N_\pm,
\qquad
F_\pm(t)=\int_0^t e^{-\lambda_\pm(t-s)-Ss}\,ds.
\tag{NP.3}
\]
由 \(\lambda_\pm-S=\pm2c\ne0\)，精确积分给
\[
\boxed{
F_\pm(t)=e^{-\lambda_\pm t}
\frac{e^{\pm2ct}-1}{\pm2c}
=e^{-St}\frac{1-e^{\mp2ct}}{\pm2c}
=e^{-(S\pm c)t}\frac{\sinh(ct)}{c}.}
\tag{NP.4}
\]
对每个 \(t>0\)，NP.3 的正积分直接说明 \(F_\pm(t)>0\)，无须从某一分母或指数差的符号猜测。\(F_\pm(0)=0\)。所有负模仍是对应正模的共轭，因为热因子为实数。

两个热因子不同。特别地，
\[
\frac{F_+(t)}{F_-(t)}=e^{-2ct},
\qquad
\boxed{F_+(s)F_-(s)=e^{-2Ss}\frac{\sinh^2(cs)}{c^2}.}
\tag{NP.5}
\]
后一式使用的是同一个时间 s 和同一对共享种子，不能把两因子分别评在独立时间。

## NP.3 共享前代自作用至 \(2p\) 的完整权重

对仅含这两对原种子的第一层支撑，通向 \(2p\) 的配对恰为 \((k_+,k_-)\) 及其反序。定义完整空间系数
\[
\boxed{\mathcal K_p=-iP_{2p}\bigl[
(N_+\cdot k_-)N_-+(N_-\cdot k_+)N_+
\bigr].}
\tag{NP.6}
\]
两个有序项已各写一次，不能只保留一项，亦不能在此基础上额外乘2。压力通过完整 \(P_{2p}\) 保留；\(N_\pm\) 自身已分别包含各自第一层投影。

对指定单树
\[
w_{22}(t)=\int_0^t e^{(t-s)\Delta}B(v_1(s),v_1(s))\,ds,
\]
由 \(|2p|^2=4P\) 和 NP.5 得
\[
(w_{22})_{2p}(t)=\mathcal H_p(t)\mathcal K_p,
\tag{NP.7}
\]
\[
\boxed{
\mathcal H_p(t)=\int_0^t e^{-4P(t-s)-2Ss}
\frac{\sinh^2(cs)}{c^2}\,ds
=e^{-4Pt}\int_0^t e^{2(P-Q)s}
\frac{\sinh^2(cs)}{c^2}\,ds.}
\tag{NP.8}
\]
这是精确权重，\(\mathcal H_p(t)>0\) 对每个 \(t>0\) 成立。若 \(N_+\)、\(N_-\) 或其完整双有序作用退化为零，NP.7 仍成立且相应输出为零；正权重不证明空间系数非零。

若需不带积分的复核表达，可定义整延拓函数
\[
\Phi(z,t)=\int_0^t e^{zs}\,ds
=\begin{cases}(e^{zt}-1)/z,&z\ne0,\\t,&z=0.\end{cases}
\]
则对 \(c\ne0\)
\[
\mathcal H_p(t)=\frac{e^{-4Pt}}{4c^2}
\bigl[\Phi(2(P-Q+c),t)+\Phi(2(P-Q-c),t)
-2\Phi(2(P-Q),t)\bigr].
\tag{NP.9}
\]
即使 \(P-Q\) 或 \(P-Q\pm c\) 为零，\(\Phi\) 的定义也没有奇点。NP.9 有有符号相消，正性应由 NP.8 判断；本稿没有用数值计算验证该差。

## NP.4 连续正交接口

把 c 暂作实参数，在固定有限时间区间上，
\[
\frac{\sinh(cs)}c\longrightarrow s\quad(c\to0)
\]
一致成立；例如 \(\sinh(cs)/c=\int_0^s\cosh(cu)\,du\) 直接给出一致收敛和局部一致有界。故可在上述有限积分内取极限：
\[
F_\pm(t)\longrightarrow t e^{-St},
\tag{NP.10}
\]
\[
\boxed{\mathcal H_p(t)\longrightarrow
e^{-4Pt}\int_0^t s^2e^{2(P-Q)s}\,ds.}
\tag{NP.11}
\]
这恰是正交共享前代的 \(s^2\) 热权重。这里只验证标量公式的连续接口，不建立固定整数格点中连续改变 c 的频率路径，也不据此改变实际初值。标量权重对 c 为偶函数；这不意味着 NP.1–2 的空间系数可以独立于波向量几何保持不变。

## NP.5 旧等长第二门的准确前提

直接恒等式为
\[
\boxed{|p+q|^2-|p-q|^2=4p\cdot q=4c.}
\tag{NP.12}
\]
因此旧门所要求的两个**第二层输入频率** \(k_+,k_-\) 等长，恰当且仅当 \(c=0\)。它不是 \(|p|=|q|\) 的条件；即使 \(P=Q\)，只要 \(c\ne0\)，这两个第二层输入仍不等长。

为把门的结论及前提写清，取一般非平行实频率 \(\ell,m\)，令 \(k=\ell+m\ne0\)，及横向复向量 \(X\cdot\ell=Y\cdot m=0\)。置
\[
T=(X\cdot m)Y+(Y\cdot\ell)X,
\qquad Z=-iP_kT.
\]
完整有序和满足
\[
T\cdot(\ell-m)=0,\qquad
T\cdot k=2(X\cdot m)(Y\cdot\ell).
\]
所以
\[
\boxed{Z\cdot(\ell-m)=
\frac{2i(X\cdot m)(Y\cdot\ell)}{|k|^2}
(|\ell|^2-|m|^2).}
\tag{NP.13}
\]
若 \(|\ell|=|m|\)，则 \(Z\) 同时垂直 k 和 \(\ell-m\)，故落在 \(\operatorname{span}_{\mathbb C}(\ell\times m)\)；这个空间像约束允许 \(Z=0\)，不证明每个法向值都可由共享原种子达到。

代入 \(\ell=k_+,m=k_-,X=N_+,Y=N_-\)，其等长前提因 \(c\ne0\) 而不成立。具体地，NP.13 只给
\[
\mathcal K_p\cdot q
=\frac{ic}{P}(N_+\cdot k_-)(N_-\cdot k_+).
\tag{NP.14}
\]
这个条件恒等式用于显示前提在哪里失效；本项不评价右端对共享 \(U,V\) 是否非零，不分类全部空间像。失去等长前提并不自动获得独立极化自由度；某些种子可仍使右端或全部 \(\mathcal K_p\) 为零。

## NP.6 已付范围与来源

本项支付 NP.1–11 的完整共享种子热公式，以及 NP.12–14 的旧等长门适用边界。全部解析余项为零。尚未核完其他接收通道、复极化相关性和实值反馈，不形成候选合同的成功证据。

\(v_1\) 是定义中的一阶树，不能称为真实 NS 原解的纯第一代供给；\(w_{22}\) 只是单个 2+2 树。1+3、3+1、其他种子作用、目标外回流和无限维余项仍须在完整原解中另付。平面频率子问题也不能替代未来三波向量线性独立的三维问题；本稿不引入坐标变换后的各向异性方程，不给 NS 奇性、有限两步原解机制或统一迭代结论。

| 本轮完整实读来源 | SHA256 |
|---|---|
| PREFLIGHT_CONTRACT.md | cf60ed5f76911da486656f8cf6543bd0822980f2990129c52c3b733300e03684 |

未读本轮主预检，未新增外部定理依赖，不作新颖性声明。此哈希绑定来源字节，不替代非作者审查。
