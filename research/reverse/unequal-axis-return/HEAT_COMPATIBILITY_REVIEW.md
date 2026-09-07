# 两个带热接收时间相容性：非作者全文审查

2026-09-08，PRIVATE_CORE。审查者为独立核验代理；本稿不是主证明作者的自评，也不代替本任务的最终冻结记录。

结论：**PASS — STRICT SEPARATION FOR THE SPECIFIED HEAT-TREE TEMPLATE GATE**。所读主稿 HC.1–10 的消元、严格不等式及范围表述均可接受，没有发现需要修订的数学阻断。对剩余正实平方频率 \(q_1<q_2<q_3,\ q_2^2<q_1q_3\)，确有 \(t_{13}<t_{12}^{(2)}\)。结合已接纳的热排序必要条件，指定完整热权重的单个 \(w_{22}\) 树不能满足共同幅度的精确加倍原模板返回。

这不排除完整 NS 的正时间再生成，不认证实际第一代供给，也不构成奇性或正则性结论。

## 1. 实际阅读与核验方式

先全文读本轮合同及主证明，再全文复读 HT 热积分接口和 HO 热排序主稿。全部数学核验是独立手算；工具仅用于读写文本与 SHA256。没有科学程序、数组、指数数值求值、参数选择、Git 或旧计算重跑。没有读取本轮 HEAT_COMPATIBILITY_INDEPENDENT.md 或另一代理正在写作的消元稿。

本稿是读过主证明后的非作者审查，不称盲推导。当前实际读取的字节如下，路径均相对此目录：

| 来源 | SHA256 |
|---|---|
| HEAT_COMPATIBILITY_CONTRACT.md | 868c41244ecc0512106fbbf1e3c769b7e02d1cacb00ae7f3cb031481b66573a9 |
| HEAT_COMPATIBILITY_PROOF.md | 5c156782846a836df4e2d57e355c9d7a0e802e09048849960ae65257f8329b61 |
| HEAT_TRANSFER_PREFLIGHT.md | efe1b7313abaee0d1cd986da6ffdba38ff818eb8707b0cdda003f66eee18f369 |
| HEAT_ORDER_PROOF.md | 2d4196425bf443fb113c34a4102a08fa089e5ac3956cebae4a86b5a159d4b32b |

本轮复核 HT.5 的精确核与 HT.11 的带权比例接口，复核 HO.1–7 在本证明中的使用；先前瞬时全部支撑和极化审查不重新包装成本轮的新推导。

## 2. 共同基频消元：HC.1–4

固定 \(X=q_1,\ A=q_2-q_1,\ B=q_3-q_2,\ C=A+B\)。展开给

\[
(X+A)^2-X(X+C)=A^2-X(B-A).
\]

在 \(X,A,B>0\) 下，其严格为负恰要求 \(B>A\) 且 \(X>A^2/(B-A)\)，所以 HC.1 没有遗失等号或符号分支。

从原热核

\[
H_{ij}(t)=\int_0^t s^2e^{-4q_i(t-s)-2(q_i+q_j)s}\,ds
\]

可逐项看到 \(q_i\mapsto q_i+X_0\) 时额外指数恰为 \(-4X_0t\)。每个行乘积 \(K_i\) 因而乘同一个 \(e^{-8X_0t}\)，比值 \(P=K_1/K_3,\ Q=K_1/K_2\) 不变。这是精确代数，不是假设物理解对共同频率平移不变。

在 \(g_1=g_3\) 的同一时刻，

\[
P=\frac\beta\alpha
=\frac{B(2X+A)}{A(2X+2A+B)}.
\]

剩余条件给 \(\beta>\alpha\)，而第二个分式的括号比严格小于一，故 \(1<P<B/A\)，所有后续分母 \(B-AP\) 为正。交叉相乘后

\[
2X(B-AP)=A[P(2A+B)-B].
\]

分别加上 \(A,\ 2A+B,\ C\) 并通分，分子依次是 \(APC,\ BC,\ A^2P+B^2\)。这核实了主稿列出的三个分母恒等式。特别

\[
\frac\gamma\beta
=\frac{C(2X+2A+B)}{B(2X+C)}
=\frac{C^2}{A^2P+B^2},
\qquad
\frac{g_1}{g_2}=\frac{C^2Q}{A^2P+B^2}.
\]

HC.4 只在该 \(g_1=g_3\) 时刻使用，没有把消去后的关系误作任意时间恒等式。

## 3. 辅助函数确为凸函数：HC.5–7

由 \(s=t\theta\) 得到

\[
H(x,y;t)=t^3e^{-4xt}f(2(x-y)t),\qquad
f(u)=\int_0^1\theta^2e^{u\theta}\,d\theta>0.
\]

固定三个 \(q_j\) 后，在 \(\Phi(x)=\sum_j\log H(x,q_j;t)-\log H(x,x;t)\) 中，\(x=q_i\) 时对角项被精确消去，留下另外两项。因此 \(\Phi(q_i)=\log K_i\)，没有多留一个对角热因子。

直接展开得到

\[
\Phi(x)=6\log t-8xt+\sum_j\log f(2(x-q_j)t)-\log f(0).
\]

对任意有限 \(u\)，所有所需微分都可在紧区间积分下进行；密度 \(\theta^2e^{u\theta}/f(u)\) 在 \((0,1)\) 严格正。令 \(m=E\theta\)，则 \(0<m<1\)，并且

\[
0<\operatorname{Var}(\theta)
=E\theta^2-m^2<m-m^2\le\frac14.
\]

左端严格性来自该分布不集中于一点，右端严格性来自 \(E[\theta(1-\theta)]>0\)。所以

\[
\Phi''(x)=4t^2\sum_{j=1}^3
\operatorname{Var}_{2(x-q_j)t}(\theta),\qquad
0<\Phi''(x)<3t^2.
\]

这里 \(\Phi\) 是严格凸函数。用于上界的凹函数是 \(\Phi(x)-(3t^2/2)x^2\)，二者没有混用。

令 \(\lambda=A/C,\ \omega=B/C\)。中间点满足 \(X+A=\omega X+\lambda(X+C)\)，二次函数的相应弦差为

\[
\omega X^2+\lambda(X+C)^2-(X+A)^2=AB.
\]

因此

\[
0\le E_{\rm heat}
=\omega\log K_1+\lambda\log K_3-\log K_2
=\log Q-\lambda\log P
\le\frac32ABt^2.
\]

这不是仅凭凸性得到上界，而是使用已核的曲率上界。

HO.5–6 的概率期望比较给

\[
(\log P)'=(\log(H_{12}/H_{32}))'
+(\log(H_{13}/H_{31}))'>2C.
\]

其严格性来自积分内点处的严格端值界，\(P(0+)=1\) 来自全部 \(H_{ij}/t^3\to1/3\)。积分即得 \(\ell=\log P>2Ct\)。代回弦差上界并用 \(AB/C^2=\lambda\omega\)，得到

\[
E_{\rm heat}<\frac38\lambda\omega\ell^2.
\]

没有交换无限极限，没有小时间截断，也没有被遗漏的热权重余项。

## 4. 熵函数下界及严格性：HC.8–9

由 \(B>A\) 知 \(0<\lambda<1/2<\omega<1\)。设 \(L=\log(\omega/\lambda)>0\)，HC.3 恰给 \(0<\ell<L\)。对固定 \(\lambda,\omega\)，

\[
h'(\ell)=
\frac{\lambda^2e^\ell}{\lambda^2e^\ell+\omega^2}-\lambda<0
\]

等价于 \(e^\ell<\omega/\lambda\)，所以主稿使用的递减区间准确。端点处 \(\lambda^2e^L+\omega^2=\omega\)，因而

\[
h(L)=\log2+\lambda\log\lambda+\omega\log\omega.
\]

主稿写 \(h(\ell)\ge h(L)\) 是足够的弱形式；在当前开区间实际上严格大于，不影响之后的论证。

再令 \(\lambda_s=(1+e^s)^{-1},\ \omega_s=1-\lambda_s\)。有

\[
\lambda_s'=-\lambda_s\omega_s,\qquad
\log(\lambda_s/\omega_s)=-s.
\]

因此

\[
\mathcal D'(s)
=\lambda_s'\log(\lambda_s/\omega_s)
=s\lambda_s\omega_s,\qquad \mathcal D(0)=0.
\]

并且

\[
(\lambda_s\omega_s)'=-\lambda_s\omega_s(\omega_s-\lambda_s)<0
\quad(s>0).
\]

由于 \((\lambda_L,\omega_L)=(\lambda,\omega)\)，对每个 \(0<s<L\) 都有 \(\lambda_s\omega_s>\lambda\omega\)。乘以正的 \(s\) 后积分，严格得到

\[
\mathcal D(L)=\int_0^L s\lambda_s\omega_s\,ds
>\frac12\lambda\omega L^2.
\]

这一方向是下界；没有把递减权重误用成积分上界，也没有用数值熵估计替代证明。

## 5. 正间隙及两个唯一时间

在 \(t=t_{13}\)，已核消元给

\[
\log\frac{2g_2}{g_1}
=\log[2(\lambda^2P+\omega^2)]-\log Q
=h(\ell)-E_{\rm heat}.
\]

结合上两节，

\[
\log\frac{2g_2}{g_1}
>\frac12\lambda\omega L^2-\frac38\lambda\omega\ell^2
>\frac18\lambda\omega L^2>0.
\]

最后一个比较使用的是 \(0<\ell<L\)，故正间隙及常数 \(1/8\) 都成立。这只是对每组题定频率的严格正数；随频率比退化时并不提供一个全族统一正下界。

合同已经给出 \(g_1/g_2\) 的严格递增及唯一达到二的接口。本轮另用同一 \(f\) 手核该接口，避免只靠文字转述：设 \(m(u)=(\log f)'(u)\)，则 \(0<m<1\) 且 \(m'>0\)。由精确热表达式，

\[
\begin{aligned}
(\log(H_{12}/H_{21}))'
&=4A-2A[m(-2At)+m(2At)]>0,\\
(\log(H_{13}/H_{23}))'
&=4A-2C m(-2Ct)+2B m(-2Bt)\\
&=4A-2A m(-2Ct)
+2B[m(-2Bt)-m(-2Ct)]>2A.
\end{aligned}
\]

所以 \((\log Q)'>2A\)。频率因子 \(\gamma/\beta\) 与时间无关；又由 \(\gamma=(\alpha+\beta)/(1+\alpha\beta)\) 及 \(0<\alpha<\beta<1\)，

\[
1<\lim_{t\downarrow0}\frac{g_1}{g_2}
=\frac\gamma\beta<2.
\]

于是 \(g_1/g_2\) 连续、严格递增并趋于无穷，唯一达到二。这是对已给定接口的手工复核，不是另选参数或新候选。类似地，HO.7 的 \((\log P)'>2C\) 与初值比 \(\alpha/\beta<1\) 保证 \(t_{13}\) 存在且唯一。

既然 \(g_1(t_{13})/g_2(t_{13})<2\)，严格单调性即给 \(t_{13}<t_{12}^{(2)}\)。没有仅从两个区间端点的位置猜测唯一时间的次序。

## 6. 结论的准确适用范围

HT.11 与 HO 的全部相位、反射必要条件是本轮的已接纳输入。当前证明否定它们共同要求的标量等式 \(g_1=g_3=2g_2\)，因此不需要再解剩余的极化充分性问题：必要条件已经失败。\(q_2^2\ge q_1q_3\) 由 HO 排除，严格另一侧由 HC.10 排除，边界没有遗漏。

正实 \(q_i\) 的辅助证明覆盖固定环面的正整数长度子集，但不把非整数频率当作允许物理初值。结论也不允许每行独立幅度或每个通道独立相位；始终是原合同的共同幅度、一次平移及相容正交符号变换。

可接受的全时间表述是：所定义的有限 Fourier 树积分在所有正时间都不能满足该精确接收门。它既不延长真实 NS 解的存在时间，也不说明实际解的全部第二代输出失败。完整原解还含其他时间树、1+3/3+1、原种子混合、目标外作用和后继回流；\(v_1\) 未被认证为实际前代投影，其与真实供给的差及无限维余项未控制。

因此本审查接受的是指定纯 2+2 热树模板门的 **NO-CANDIDATE** 结论。其它模板、近似返回、较宽支撑、真实有限两步机制、同一固定初值的无限尺度、统一误差和有限总时间均不由此否定或证明。本文没有新数值证书、科学计算或发布就绪声明。
