# 两个带热接收时间的独立相容性推导

2026-09-08，PRIVATE_CORE。独立手推状态：**严格得到 \(t_{13}<t_{12}^{(2)}\)，两个必要时间不能相同；尚待非作者全文审查。**

本轮完整读取 `HEAT_COMPATIBILITY_CONTRACT.md`，复用本人已接受的 `HEAT_ORDER_INDEPENDENT.md` 中精确热积、相位相关性与比例单调性。没有读取本轮兼容性主稿，也没有读取他人的兼容性推导。以下消元及误差比较自行推导；不以主稿结论为前提。无科学程序、数组、指数数值求值、实际频率/时间/极化选择、Git 或外部文献调用。

## HC.1 问题及剩余必要条件

记 \(q_i=n_i^2\)，仍为同一合同中的三对轴向种子和完整有序 Fourier–Leray 单树 \(w_{22}\)。沿用
\[
H_{ij}(t)=\int_0^t s^2e^{-4q_i(t-s)-2(q_i+q_j)s}\,ds,
\]
\[
g_1=\alpha\gamma H_{12}H_{13},\quad
g_2=\alpha\beta H_{21}H_{23},\quad
g_3=\beta\gamma H_{31}H_{32},
\tag{HC.1}
\]
其中
\[
\alpha=\frac{q_2-q_1}{q_2+q_1},\quad
\beta=\frac{q_3-q_2}{q_3+q_2},\quad
\gamma=\frac{q_3-q_1}{q_3+q_1}.
\]
已接受的相位与共同幅度论证要求：任意模板返回只能使用 \(D=I\)，三行相关性模长为 \((1,1/2,1)\)，三个相关性实部乘积为正，且
\[
g_1=g_3=2g_2.
\tag{HC.2}
\]
剩余长度满足
\[
q_1<q_2<q_3,\qquad q_2^2<q_1q_3,
\quad\text{即 }\alpha<\beta.
\tag{HC.3}
\]
在此范围，\(g_1/g_3\) 与 \(g_1/g_2\) 严格随正时间增长，各自有唯一的
\[
g_1(t_{13})=g_3(t_{13}),\qquad
g_1(t_{12}^{(2)})=2g_2(t_{12}^{(2)}).
\]
本稿只须比较这两个时间，不必重新构造复极化。

为证明覆盖整数平方的统一不等式，下文允许 \(q_i\) 为任意满足 HC.3 的正实数。这是证明域的扩大；没有据此选择连续频率候选，也没有把非整数频率视为环面允许模态。

## HC.2 消去共同频率平移

令
\[
A=q_2-q_1>0,\qquad B=q_3-q_2>0,
\qquad r=B/A,\qquad \xi=q_1/A,\qquad \tau=At.
\]
HC.3 等价于 \(q_1B>A(q_1+A)\)，所以
\[
r>1,\qquad \xi>\frac1{r-1}.
\tag{HC.4}
\]
分别定义纯热行积及其比值
\[
W_1=H_{12}H_{13},\quad W_2=H_{21}H_{23},\quad W_3=H_{31}H_{32},
\qquad \mathcal D=W_1/W_3,\quad \mathcal E=W_1/W_2.
\]
三个 \(q_i\) 同时增加一个常数时，每个 \(H_{ij}\) 乘同一 \(e^{-4ct}\)，因此这些比值不变。更明确地，置
\[
f(u)=\int_0^1\theta^2e^{u\theta}\,d\theta>0,
\qquad H_{ij}(t)=t^3e^{-4q_it}f(2(q_i-q_j)t),
\]
则
\[
\mathcal D_r(\tau)
=e^{8(1+r)\tau}
\frac{f(-2\tau)f(-2(1+r)\tau)}
{f(2(1+r)\tau)f(2r\tau)},
\tag{HC.5}
\]
\[
\mathcal E_r(\tau)
=e^{8\tau}
\frac{f(-2\tau)f(-2(1+r)\tau)}
{f(2\tau)f(-2r\tau)}.
\tag{HC.6}
\]
这些是同一个精确热积分的恒等变换，没有替换黏性或引入渐近余项。

以下取 \(t=t_{13}\)，暂省略时间参数。由 \(g_1=g_3\) 得
\[
\mathcal D=\frac\beta\alpha
=\frac{r(2\xi+1)}{2\xi+2+r},
\qquad 1<\mathcal D<r.
\tag{HC.7}
\]
下界使用 \(\alpha<\beta\)，上界来自分母严格大于 \(2\xi+1\)。消元给
\[
\xi=\frac{\mathcal D(r+2)-r}{2(r-\mathcal D)},
\qquad
\frac\gamma\beta=\frac{(r+1)^2}{r^2+\mathcal D}.
\tag{HC.8}
\]
例如第二式可逐项验证：
\(2\xi+2+r=r(r+1)/(r-\mathcal D)\)，
\(2\xi+1+r=(r^2+\mathcal D)/(r-\mathcal D)\)。于是
\[
\frac{g_1(t_{13})}{g_2(t_{13})}
=\frac{(r+1)^2\mathcal E}{r^2+\mathcal D}.
\tag{HC.9}
\]
要证明它严格小于2，精确所需的不等式是
\[
\mathcal E<\frac{2(r^2+\mathcal D)}{(r+1)^2},
\qquad 1<\mathcal D<r.
\tag{HC.10}
\]
后续给出此不等式的严格证明，不把消元本身当作相容性结论。

## HC.3 三行热积的对数插值误差

固定此刻的三个 \(q_j\) 与 \(t>0\)，对辅助实变量 \(x\) 定义
\[
L(x)=-8xt+\sum_{j=1}^3\log f(2(x-q_j)t)
-\log f(0)+6\log t.
\tag{HC.11}
\]
恰有 \(L(q_i)=\log W_i\)：求和中 \(j=i\) 的 \(f(0)\) 被扣除，剩下的就是该行两个真实热权重。引入第三项只用于统一插值表达，没有向原树添加相互作用。

有限区间的正密度
\[
\frac{\theta^2e^{u\theta}}{f(u)}\,d\theta\quad(0<\theta<1)
\]
使 \((\log f)''(u)\) 等于 \(\theta\) 的方差。密度在整个开区间为正，故方差严格为正；又因 \(\theta^2<\theta\)，
\[
0<(\log f)''(u)
<\mu(u)(1-\mu(u))\le\frac14,
\qquad \mu=(\log f)'.
\]
有限区间内微分合法，得到对全部有限 \(x\)
\[
\boxed{0<L''(x)<3t^2.}
\tag{HC.12}
\]
令
\[
\omega=\frac1{r+1},\qquad \pi=\frac r{r+1},
\qquad q_2=\pi q_1+\omega q_3.
\]
严格凸性与 HC.12 的二阶上界给插值误差
\[
S=\pi L(q_1)+\omega L(q_3)-L(q_2),
\qquad 0<S<\frac32t^2AB=\frac32r\tau^2.
\tag{HC.13}
\]
上界可直接对 \(L(x)-(3t^2/2)x^2\) 应用严格凹性，其二次项差恰为 \(AB\)。故不依赖未估计的 Taylor 余项。相减得精确分解
\[
\log\mathcal E=\omega\log\mathcal D+S.
\tag{HC.14}
\]
这里插值误差为正，不能误用凸性把它删去而宣称 \(\mathcal E\le\mathcal D^\omega\)。

还须把 HC.13 的时间尺度误差和同一个 \(\mathcal D\) 联系。完整正核直接给
\[
\frac{H_{12}}{H_{32}}>e^{2(q_3-q_1)t},\qquad
\frac{H_{13}}{H_{31}}>1.
\]
第一式的两核比为 \(e^{(q_3-q_1)(4t-2s)}\)，第二式为 \(e^{4(q_3-q_1)(t-s)}\)，在 \(0<s<t\) 中均满足所写的严格下界。于是
\[
\log\mathcal D>2(A+B)t=2(r+1)\tau.
\]
代回 HC.13，得
\[
\boxed{0<S<\frac38\pi\omega(\log\mathcal D)^2.}
\tag{HC.15}
\]
这是已支付的明确上界，完整保留热权重，而不是仅利用其正性迁移瞬时矛盾。

## HC.4 所需幅度差额严格大于插值误差

对固定 \(r>1\) 及 \(1<d\le r\)，记
\[
G_r(d)=\log\frac{2(r^2+d)}{(r+1)^2}-\omega\log d.
\]
精确微分为
\[
G_r'(d)=\frac{\pi(d-r)}{d(r^2+d)}.
\tag{HC.16}
\]
所以在 \(1<d<r\) 上严格递减，且
\[
G_r(d)>G_r(r)
=\log2+\pi\log r-\log(r+1).
\tag{HC.17}
\]
对端值给一个自包含的正下界。置 \(h=\log r>0\)，定义辅助实函数
\[
p(v)=\frac{e^v}{1+e^v},\quad
w(v)=\frac1{1+e^v},\quad
K(h)=\log2+h p(h)-\log(1+e^h).
\]
有 \(K(0)=0\)、\(K'(v)=v p(v)w(v)\)。在 \(v>0\) 上，
\((p(v)w(v))'=p(v)w(v)(w(v)-p(v))<0\)。因此
\[
G_r(r)=K(h)=\int_0^h v p(v)w(v)\,dv
>\frac12p(h)w(h)h^2
=\frac12\pi\omega(\log r)^2.
\tag{HC.18}
\]
所有积分均在有限区间；没有对指数或对数进行数值求值。

在 \(t_{13}\) 处由 HC.7 有 \(0<\log\mathcal D<\log r\)。HC.15 与 HC.17–18 于是给
\[
S<\frac38\pi\omega(\log r)^2
<\frac12\pi\omega(\log r)^2
<G_r(r)<G_r(\mathcal D).
\tag{HC.19}
\]
结合 HC.14，这正是
\[
\log\mathcal E
<\omega\log\mathcal D+G_r(\mathcal D)
=\log\frac{2(r^2+\mathcal D)}{(r+1)^2},
\]
从而 HC.10 得证。证明的严格差额还可记录为
\[
\log\frac{2}{g_1(t_{13})/g_2(t_{13})}
=G_r(\mathcal D)-S
>\frac18\frac r{(r+1)^2}(\log r)^2>0.
\tag{HC.20}
\]
此差额只用于说明所有严格号已有依据，不据此选择频率或新增参数优化。

## HC.5 两个时间严格分离

在剩余范围 HC.3，\(\gamma<\alpha+\beta<2\beta\)，故已接受的单调性和端点极限保证 \(t_{12}^{(2)}\) 存在且唯一。由 HC.9–10，
\[
\frac{g_1(t_{13})}{g_2(t_{13})}<2.
\]
\(g_1/g_2\) 严格随时间增长，因此
\[
\boxed{t_{13}<t_{12}^{(2)}.}
\tag{HC.21}
\]
这对所有满足 HC.3 的正实 \(q_i\) 成立，因而也覆盖固定环面允许的全部互异正整数长度的剩余子集。两个唯一时间无法相同。

与已接受的相位门合并：非恒等 signed-axis 分支已由相关符号排除；\(n_2^2\ge n_1n_3\) 已由热排序排除；最后的 \(D=I\)、\(n_2^2<n_1n_3\) 分支现在由 HC.21 排除。因此对本合同固定的纯 \(w_{22}\) 树、同一个原模板、一次平移、共同正幅度及全部八个 D，**全部正时间的精确返回均不相容**。

## HC.6 已付内容、独立性与不能迁移的边界

本轮新增的是精确消元 HC.7–10、热行积对数插值误差 HC.11–15，以及控制该误差的严格幅度差额 HC.16–20；结论不是重复旧排序，也没有以两个时间区间相交或数值未命中作判断。所有恒等式的解析余项为零；唯一插值误差 S 保留且已给出严格界。

本稿没有推导或使用真实 NS 原解的完整四叶响应。\(w_{22}\) 只是已固定分账中的单个树；1+3、3+1、种子混合、接收集外反馈、\(v_1\) 与真实前代的偏差及无限维余项仍未支付。这里的精确返回障碍不能扩大成任意近似返回、其他模板或完整 NS 奇性的障碍；也不提供有限两步原解机制、统一迭代、单初值无限尺度或有限总时间结论。

本稿在未读本轮主稿的情况下完成，待根代理及非作者实际全文审查后才能决定接纳。没有修改旧冻结文件或重启任何关闭的计算。

## HC.7 来源字节

| 来源（相对此目录） | 使用范围 | SHA256 |
|---|---|---|
| HEAT_COMPATIBILITY_CONTRACT.md | 本轮全文实读，固定问题与边界 | 868c41244ecc0512106fbbf1e3c769b7e02d1cacb00ae7f3cb031481b66573a9 |
| HEAT_ORDER_INDEPENDENT.md | 复用本人已接受的精确热积分、相位门及单调性；本轮核其实际字节 | 80b3b7dc3565bc8fbc8328e501c4f1a17b2d2929c82bb1863c39690793ddafc9 |

本轮没有新增外部定理依赖或原文阅读声明，不作新颖性声明。哈希仅绑定所用来源，不能替代数学审查。
