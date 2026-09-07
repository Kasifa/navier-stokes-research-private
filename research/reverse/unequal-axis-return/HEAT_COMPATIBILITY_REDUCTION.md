# 两个带热接收时间的无量纲消元

2026-09-08，PRIVATE_CORE。只读指定 HEAT_COMPATIBILITY_CONTRACT.md 与 HEAT_ORDER_ROOT_REVIEW.md，并复用我此前 HEAT_TRANSFER_PREFLIGHT.md 的精确 H。未读根的兼容性主稿或 Pauli 本轮新稿。以下为独立手工代数与正积分比较；没有科学程序、数组、指数数值求值、参数选择或 Git。

**本轮结果：两个必要等式 \(g_1=g_3=2g_2\) 可以消去共同基频，化为一个明确的二变量标量零点条件及严格域条件。** 这里不判定该标量式是否有零点；正实辅助频率中的等价不意味着存在整数频率、可用极化或真实 NS 候选。

## 1. 对象和无量纲变量

沿用已接受的排序 \(0<q_1<q_2<q_3\)，\(q_i=n_i^2\)，以及
\[
\alpha=\frac{q_2-q_1}{q_2+q_1},\quad
\beta=\frac{q_3-q_2}{q_3+q_2},\quad
\gamma=\frac{q_3-q_1}{q_3+q_1}.
\]
只保留合同中的 \(q_2^2<q_1q_3\)。记
\[
\Delta=q_2-q_1>0,\quad
r=\frac{q_3-q_2}{\Delta},\quad
m=\frac{q_1}{\Delta},\quad x=2\Delta t.
\tag{CR.1}
\]
于是 \((q_1,q_2,q_3)=\Delta(m,m+1,m+1+r)\)。条件
\((m+1)^2<m(m+1+r)\) 精确等价于
\[
\boxed{r>1,\qquad m>\frac1{r-1},\qquad x>0.}
\tag{CR.2}
\]
这里只改变符号坐标，不给 \(\Delta,r,m,x\) 任何数值。
频率比变为
\[
\alpha=\frac1{2m+1},\quad
\beta=\frac r{2m+2+r},\quad
\gamma=\frac{1+r}{2m+1+r}.
\tag{CR.3}
\]

## 2. 热权重中共同基频精确消去

令
\[
f(u)=\int_0^1\theta^2e^{u\theta}\,d\theta>0
\quad(u\in\mathbb R).
\]
精确式 \(H_{ij}=t^3e^{-4q_it}f(2(q_i-q_j)t)\) 来自原热积分的 \(s=t\theta\) 换元。使用三行公共幅度权重
\[
g_1=\alpha\gamma H_{12}H_{13},\quad
g_2=\alpha\beta H_{21}H_{23},\quad
g_3=\beta\gamma H_{31}H_{32}.
\tag{CR.4}
\]
若对 g 使用共同正因子不同的规范，以下比值不变。

三行的共同正因子为 \(t^6e^{-4mx}\)。定义
\(\widetilde g_i=g_i/(t^6e^{-4mx})\)，则精确地
\[
\begin{aligned}
\widetilde g_1&=\alpha\gamma f(-x)f(-(1+r)x),\\
\widetilde g_2&=\alpha\beta e^{-4x}f(x)f(-rx),\\
\widetilde g_3&=\beta\gamma e^{-4(1+r)x}f((1+r)x)f(rx).
\end{aligned}
\tag{CR.5}
\]
只除去同一个精确因子，没有作渐近替换。
定义两个完全不含 m 的正函数
\[
X(r,x)=e^{4x}
\frac{f(-x)f(-(1+r)x)}{f(x)f(-rx)},
\]
\[
Z(r,x)=e^{4(1+r)x}
\frac{f(-x)f(-(1+r)x)}{f((1+r)x)f(rx)}.
\tag{CR.6}
\]
于是
\[
\frac{g_1}{g_2}=\frac\gamma\beta X,
\qquad \frac{g_1}{g_3}=\frac\alpha\beta Z.
\tag{CR.7}
\]
所有分母严格正，没有借用相位相消或数值近似。

## 3. 消去 m 后的唯一标量相容式

\(g_1=g_3\) 当且仅当
\[
Z=\frac\beta\alpha
=\frac{r(2m+1)}{2m+2+r}.
\tag{CR.8}
\]
对固定 \(r>1\)，右侧作为 m 的函数，在 CR.2 的范围严格增加，值域恰为 \((1,r)\)。求解得到
\[
\boxed{m=\frac{(r+2)Z-r}{2(r-Z)}.}
\tag{CR.9}
\]
反向检查并非省略的正性假设：若 \(1<Z<r\)，则
\[
m-\frac1{r-1}
=\frac{r(r+1)(Z-1)}{2(r-Z)(r-1)}>0.
\tag{CR.10}
\]
所以 CR.9 在恰当域中恢复的就是有限且允许的正实共同基频。

代回第二个必要等式需要的比值，精确得到
\[
\frac{2\beta}{\gamma}
=\frac{2r(2m+1+r)}{(r+1)(2m+2+r)}
=\frac{2(r^2+Z)}{(r+1)^2}.
\tag{CR.11}
\]
因此两条幅度等式在正实辅助域中的相容性等价于
\[
\boxed{
r>1,\quad x>0,\quad 1<Z(r,x)<r,\quad
\mathcal F(r,x):=(r+1)^2X(r,x)-2Z(r,x)-2r^2=0.
}
\tag{CR.12}
\]
这是所求的一个明确可检验标量条件。若不希望出现 f 的比值，可乘以严格正的
\(f(x)f(-rx)f((1+r)x)f(rx)\)。同一个零点条件是
\[
\begin{aligned}
0={}&(r+1)^2e^{4x}f(-x)f(-(1+r)x)f((1+r)x)f(rx)\\
&-2e^{4(1+r)x}f(-x)f(-(1+r)x)f(x)f(-rx)\\
&-2r^2f(x)f(-rx)f((1+r)x)f(rx).
\end{aligned}
\tag{CR.13}
\]
CR.13 不改变 CR.12 的严格域条件；不能只解这个等式而接纳域外点。

## 4. 反代的充分性只属于两条正实标量等式

若某个未指定的 \((r,x)\) 满足 CR.12，按 CR.9 定义 m，再对任意符号 \(\Delta>0\) 置
\[
(q_1,q_2,q_3)=\Delta(m,m+1,m+1+r),\qquad
t=x/(2\Delta).
\]
CR.10 保证剩余长度不等式；CR.8 给 \(g_1/g_3=1\)，CR.11–12 给 \(g_1/g_2=2\)。反之，合同的任一正实两等式解经 CR.1 必给 CR.12。这说明消元没有丢失正实域中的解，也没有因除法添入该域中的伪解。

这段反代是符号等价证明，未提供或选择一组参数。若要求原固定环面的允许频率，还须有同一个 \(\Delta>0\) 使三个 \(q_i\) 都是正整数的平方。仅有正实解、甚至某些频差比有理，都不自动支付这一要求。

此外 CR.12 只等价于两条 g 等式，不等价于原来的复极化返回方程。共同相位、相关性 \((1,1/2,1)\)、\(R_1R_2R_3>0\) 及完整极化充分可解性不能由反代暗中补齐。

## 5. 一个严格的有限无量纲时间域

由相同 s 的原 H 积分核比较，令 \(c=q_3-q_1>0\)，有
\[
e^{2ct}<\frac{H_{12}}{H_{32}}<e^{4ct},\qquad
1<\frac{H_{13}}{H_{31}}<e^{4ct}.
\]
第一比值的逐 s 指数差是 \(c(4t-2s)\)，第二个是 \(4c(t-s)\)；s 在内部具有正权，所以界严格，无需两种权重相同。
两式相乘恰给
\[
e^{(1+r)x}<Z(r,x)<e^{4(1+r)x}.
\tag{CR.14}
\]
故 CR.12 的可用域必满足
\[
\boxed{0<x<\frac{\log r}{1+r}.}
\tag{CR.15}
\]
该有限上界没有选取任何时间值，也不替代 \(Z<r\) 本身。由已经接受的 g 比值严格单调，Z 对固定 r 严格递增；因其与 m 无关，\(Z=r\) 的边界若另作定义也是唯一的，但本轮没有求这个时间。

连续延拓到 x=0 时，\(X=Z=1\)，所以
\(\mathcal F(r,0)=-(r-1)^2<0\)。这是端点符号，不能推出整个 CR.12 域内无零点。\(Z=1\) 对应旧长度域的边界，\(Z=r\) 对应 CR.9 的无穷基频极限，二者均不能作为有限正时间允许解接纳。

## 6. 结果和未付条件

本轮新增的是共同基频的精确消元、可逆域条件和一个标量零点式。尚缺的是对 \(\mathcal F\) 在 CR.12 域内的零点或严格符号作解析判断；本稿不以正积分的正性推断其含负项组合的符号，也不重复唯一时间排序作为新结论。

即使该标量门将来通过，整数频率、完整极化可解性以及固定同一初值的真实 NS 机制仍未支付。这里始终只是 \(w_{22}\) 树；1+3/3+1、种子混合、目标外反馈、真实前代偏差与无限维余项没有消失。没有候选、全时间分类、统一再生成、单初值无限尺度、有限总时间或奇性结论。

## 7. 实际来源与独立性

指定的两个新输入全文实读。H 和三行 g 的公式复用我先前已写、已读的 HEAT_TRANSFER_PREFLIGHT；本轮 CR.1–15 均手推。未读根的兼容性主稿或 Pauli 新稿，未执行科学程序、指数数值或数组。来源哈希仅用于固定所用文本。

| 文件（相对此目录） | SHA256 |
|---|---|
| HEAT_COMPATIBILITY_CONTRACT.md | 868c41244ecc0512106fbbf1e3c769b7e02d1cacb00ae7f3cb031481b66573a9 |
| HEAT_ORDER_ROOT_REVIEW.md | 2f1ea3d1c36d9aec4ca34a4b3c1ade5a7334ce9d082956786e0604242f846467 |
| HEAT_TRANSFER_PREFLIGHT.md | efe1b7313abaee0d1cd986da6ffdba38ff818eb8707b0cdda003f66eee18f369 |
