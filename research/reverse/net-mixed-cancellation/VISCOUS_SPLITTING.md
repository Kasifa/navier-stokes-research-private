# 空间混合首项相消后的精确热核分裂

2026-09-08，PRIVATE_CORE。状态：独立有界推导，待根全文核验。

**锁定问题与结论：固定一条活跃、非正交、不同长度的非平行频率边，假设其完整空间混合和 \(Z=G_++G_-=0\) 且 \(C\ne0\)。则有限热混合项在每个 \(t>0\) 都非零；其首个非零时间项是 \(-\tfrac c2G_+t^4\)，并有显式五次误差。对满足相同叶行条件的两边星形，同一真实 NS 解在合法短窗中的叶接收其余来源也有这个非零四次项，但它相对自供给仍为 \(O(t)\)。这不是再生成排除。**

全部为手工符号推导。未运行 Git、科学程序、数组、数值求值、扫描或额度重置，没有外发，也没有选择实际新频率、初值或时间。本轮只写本文件。没有读取 `ROOT_REVIEW.md`、`STAR_CENTER_ANALYSIS.md` 或本项 `INDEPENDENT.md`；不依赖它们的口头结果，也不以先前尚待根核验的星形推导作本项前提。

## 1. 实际来源与固定数据

路径相对于 `research/reverse/`。以下文本已在本连续工作中实际全文读取并完成相应非作者核验，本轮检查字节未变。

| 来源及本次使用范围 | SHA-256 |
|---|---|
| net-mixed-cancellation/CONTRACT.md，当前总首项与来源范围 | 8ec55579d3288a15e47f2b1af17a2d981ac174fb649dc496fb6d5ac0d9b2e7e8 |
| mixed-polarization/MIXED_ROOT_INDEPENDENT.md，MI.19–20 完整空间系数、MI.25–27 精确热作用量、完整加倍接收根 | cad93f863ad371723d4510f20588a0f7abcee3e4f8e2984010f88ebcb2fc2dbf |
| mixed-polarization/SOURCE_BRIDGE_INDEPENDENT.md，同一原解及 SB.33、39、41–49 的真实尾部常数 | 1d3d33fbb8fcc17ac1266f2ee88c88eebe328867f385277a0a684cfa2247630a |

保持单位黏性、无外力及固定三维 \(2\pi\) 环面。令该边为 \(p\leftarrow q\)，同一份种子为 \(U\perp p\)、\(V\perp q\)，负模严格取共轭。记
\[
P=|p|^2>0,\quad Q=|q|^2>0,\quad c=p\cdot q\ne0,
\quad d=P-Q\ne0,\quad\Delta=PQ-c^2>0,
\]
\[
S=P+Q,\quad\lambda_\sigma=S+2\sigma c>0,
\quad E_\sigma=4P+Q+4\sigma c>0.
\tag{VS.1}
\]
\(G_\sigma\) 是该同一对种子的完整三层有序 Leray 混合根，即已接受 MI.16–20 的 \(D_\sigma\)。假设
\[
(U\cdot q)(V\cdot p)\ne0,
\qquad G_++G_-=0,\qquad C\ne0.
\tag{VS.2}
\]
以下不把两个 \(G_\sigma\) 当作可独立指定的前代。

## 2. 空间相消没有使单个混合根为零

沿用实横向分解
\[
e=q-\frac cPp,\quad f=p-\frac cQq,\quad n=p\times q,
\qquad U=u e+v n,\quad V=x f+y n.
\]
活跃性给 \(ux\ne0\)。完整 MI.19 给
\[
(G_\sigma)_e=
\frac{4i\Delta^3d(P+\sigma c)(2c+\sigma Q)}
{P^2Q^2\lambda_\sigma E_\sigma}u^2|x|^2.
\tag{VS.3}
\]
若 \(c>0\)，\((P+c)(2c+Q)>0\)，所以 \((G_+)_e\ne0\)。若 \(c<0\)，\(P-c>0\)、\(2c-Q<0\)，所以 \((G_-)_e\ne0\)。结合 \(G_-=-G_+\)，两种情况都给
\[
\boxed{G_+\ne0,\qquad G_-=-G_+\ne0.}
\tag{VS.4}
\]
该论证不需删除法向分量，不需种子线性极化，也不使用未审查的新零门。\(C\ne0\) 与当前完整非退化单对公式一致；它将在真实自供给比较中使用。

## 3. 精确热作用量在全部正时间严格分开

定义时间单纯形
\[
\mathscr T_t=\{(s,\tau,r):0\le r\le\tau\le s\le t\}.
\]
已接受 MI.25–27 直接给
\[
K_\sigma(t)=\int_{\mathscr T_t}e^{-\mathcal A_\sigma}
\,dr\,d\tau\,ds,
\]
\[
\mathcal A_\sigma=
4P(t-s)+(E_\sigma+Q)(s-\tau)
+(\lambda_\sigma+S)(\tau-r)+2Sr.
\tag{VS.5}
\]
全部四个衰减率严格为正。两个作用量的精确差是
\[
\boxed{\mathcal A_+-\mathcal A_-
=8c(s-\tau)+4c(\tau-r)
=4cL,\qquad L=2s-\tau-r.}
\tag{VS.6}
\]
\(L\ge0\)，且在正时间单纯形内部严格为正。因此
\[
c>0\Longrightarrow K_+(t)<K_-(t),
\qquad
c<0\Longrightarrow K_+(t)>K_-(t)
\quad(t>0).
\tag{VS.7}
\]
这比较的是两个完整热核，不是把它们都近似为 \(t^3/6\)。

令 \(\kappa(t)=K_+(t)-K_-(t)\)，并置
\[
\mathcal A_\theta=(1-\theta)\mathcal A_-+\theta\mathcal A_+,
\qquad0\le\theta\le1.
\]
指数函数的精确积分差式给
\[
\boxed{
\kappa(t)=-4c\int_{\mathscr T_t}L
\left(\int_0^1e^{-\mathcal A_\theta}\,d\theta\right)
dr\,d\tau\,ds.}
\tag{VS.8}
\]
故其符号始终为 \(-\operatorname{sgn}c\)。由 VS.4，有限热混合项满足
\[
\boxed{
\mathcal M_{\rm pair}(t)
=K_+G_++K_-G_-=\kappa(t)G_+\ne0
\quad\text{对每个 }t>0.}
\tag{VS.9}
\]
VS.9 只对该精确有限树成立；真实 NS 解的可用窗口另由第 5 节限制。

## 4. 首个非零时间系数和显式下一阶界

定义明确几何常数
\[
\mu_\sigma=
\max\{4P,E_\sigma+Q,\lambda_\sigma+S,2S\},
\qquad\mu=\max\{\mu_+,\mu_-\}>0.
\tag{VS.10}
\]
四段时间长度和为 \(t\)，所以
\(0\le\mathcal A_\theta\le\mu t\)。同时，逐次手工积分给
\[
\int_0^t\int_0^s\int_0^\tau(2s-\tau-r)
\,dr\,d\tau\,ds
=\int_0^t\frac{s^3}{2}\,ds=\frac{t^4}{8}.
\tag{VS.11}
\]
VS.8 因而给对所有 \(t>0\) 的严格量化界
\[
\boxed{
\frac{|c|t^4}{2}e^{-\mu t}
\le|\kappa(t)|\le\frac{|c|t^4}{2}.}
\tag{VS.12}
\]
再用 \(0\le1-e^{-a}\le a\)，得到无需未估 Taylor 项的误差
\[
\boxed{
\left|\kappa(t)+\frac c2t^4\right|
\le\frac{|c|\mu}{2}t^5.}
\tag{VS.13}
\]
因此设
\[
F=-\frac c2G_+\ne0,
\]
则
\[
\boxed{
\|\mathcal M_{\rm pair}(t)-t^4F\|
\le\mu\|F\|t^5,
\qquad t>0.}
\tag{VS.14}
\]
这确定了首个非零项为四次，系数的符号是 \(-cG_+/2\)。相应的全正时间非零下界为
\(\|\mathcal M_{\rm pair}(t)\|\ge\|F\|t^4e^{-\mu t}\)。

三次空间和相消不意味着三次核之后只剩形式上的未知余项；VS.13–14 明确控制了下一阶。它也不意味着真实解在所有正时间有同样的非零结论。

## 5. 两边星形叶行的同一原解接口

现在回到同一份固定三对数据，中心为 \(p_0\)，叶为 \(p_1,p_2\)。本节明确限制在三个频率线性独立、所有成对点积非零、平方长度两两不同的星形域。假设双向活跃边恰为两条中心边，而且叶行的空间混合和为零。若原假设是全部 \(M_0=0\)，则特别包含这两个叶行条件。于是每条叶接收、中心发送的边均具有 VS.1 的非平行、非正交及不同长度条件；活跃性由图假设给出，\(Z_i=0\) 和 \(C_i\ne0\) 由下面的完整接收零门与非退化公式得到。本文不把仅有“两边活跃及叶行零”的一般星形推广到正交或等长边。

非活跃叶边意味着其接收坐标 \(u\) 或发送坐标 \(x\) 为零。完整 MI.19–20 在任一分支都使每个 \(G_\sigma\) 为零，完整 \(C\) 也为零，两个方向均成立。因此在每个叶接收 \(2p_i\) 上，有限混合接收只剩中心边：
\[
(M_4(t))_{2p_i}=\mathcal M_{{\rm pair},i}(t),
\qquad Z_i=G_{i,+}+G_{i,-}=0,
\qquad i=1,2.
\tag{VS.15}
\]
各中心边都活跃、非正交且长度不同，故 \(C_i\ne0\)，并可逐边使用 VS.4–14。没有求解或使用中心接收行的相消式。

对这同一份初值定义
\[
A=\|a\|_{\mathcal A_0}>0,
\qquad K=\max_i|p_i|>0,
\qquad T_{\rm sb}=\frac1{8AK}.
\]
已接受 SOURCE_BRIDGE 给唯一同数据的光滑 NS 解 \(u\)，真实 \(g=P_{\mathcal L}u\)，及
\[
\mathcal S(t)=\int_0^t e^{(t-s)\Delta}P_DB(g,g)(s)\,ds.
\]
使用其 SB.48 的明确粗常数
\[
C_D=\frac43A(4AK)^5,\qquad
C_S=A(4AK)^5,\qquad C_{\rm tail}=C_D+C_S,
\tag{VS.16}
\]
全频带真实预算是
\[
\|P_Du-\mathcal S-M_4\|_{\mathcal A_0}
\le C_{\rm tail}t^5,
\qquad0\le t\le T_{\rm sb}.
\tag{VS.17}
\]
所以令真实叶行其余来源
\[
R_i(t)=(P_Du(t)-\mathcal S(t))_{2p_i},
\qquad F_i=-\frac{c_i}{2}G_{i,+}\ne0,
\]
有
\[
\boxed{
\|R_i(t)-t^4F_i\|
\le L_i t^5,
\qquad L_i=\mu_i\|F_i\|+C_{\rm tail}>0.}
\tag{VS.18}
\]
取解析窗口
\[
T_i=\min\left\{T_{\rm sb},\frac{\|F_i\|}{2L_i}\right\}>0,
\]
即得
\[
\boxed{
\frac12\|F_i\|t^4\le\|R_i(t)\|
\le\frac32\|F_i\|t^4,
\qquad0<t\le T_i.}
\tag{VS.19}
\]
两叶同时使用 \(\min\{T_1,T_2\}\) 即可；这是同一数据的符号窗口，并未指定实际时间。负接收为这些系数的完整共轭，具有同样的非零性与范数界。

## 6. 相对自供给仍小一阶，不是再生成排除

叶行另一条边的完整 \(C\) 为零，所以令
\[
W_i=\frac13C_i\ne0,
\qquad S_i(t)=\mathcal S(t)_{2p_i}.
\]
已接受 \(J_i\) 的正积分误差和真实 \(\mathcal S-W\) 界给
\[
\boxed{
\|S_i(t)-t^3W_i\|
\le\mu_{22,i}\|W_i\|t^4+C_St^5,
\quad\mu_{22,i}=\max\{4P_i,2(P_i+Q_i)+2|c_i|\}.}
\tag{VS.20}
\]
这里 \(P_i=|p_i|^2\)、\(Q_i=|p_0|^2\)，仍是叶接收、中心发送的同一对几何。

进一步限制在明确正窗
\[
\widehat T_i=
\min\left\{T_i,\frac1{4\mu_{22,i}},
\sqrt{\frac{\|W_i\|}{4C_S}}\right\}>0,
\tag{VS.21}
\]
则 \(\|S_i\|\) 在 \([\|W_i\|t^3/2,3\|W_i\|t^3/2]\) 内。与 VS.19 相除得到
\[
\boxed{
\frac{\|F_i\|}{3\|W_i\|}t
\le\frac{\|R_i(t)\|}{\|S_i(t)\|}
\le\frac{3\|F_i\|}{\|W_i\|}t,
\qquad0<t\le\widehat T_i.}
\tag{VS.22}
\]
更精确地，VS.18、20 给
\[
\boxed{
\lim_{t\downarrow0}
\frac{\|R_i(t)\|}{t\|S_i(t)\|}
=\frac{\|F_i\|}{\|W_i\|}
=\frac{3|c_i|}{2}\frac{\|G_{i,+}\|}{\|C_i\|}>0.}
\tag{VS.23}
\]
因此，在该条件分支内，精确热核使叶行有限混合项及真实其余来源具有非零四次项；但自供给仍从非零三次项开始，其余来源/自供给比值趋零。不能把这个 \(O(t)\) 比例称为相对来源障碍或再生成排除。

本稿没有证明两边星形的全部空间相消假设存在实例，也没有检验中心行、总模板、形态、正交能量或可迭代结构。有限树的全正时间非零与原解在 \(\widehat T_i\) 内的非零已分别限定。不存在对全部正时间、全部极化或跨代的统一原解结论，没有同一初值无限尺度、有限总时间、奇性或全局正则性结论。FINITE HEAT SPLITTING AND CONDITIONAL LOCAL SOURCE ASYMPTOTICS；NO-CANDIDATE ACCEPTED；NOT CLAY。
