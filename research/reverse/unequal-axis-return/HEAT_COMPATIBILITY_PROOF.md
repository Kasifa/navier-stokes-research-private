# 两个带热接收时间严格分离

2026-09-08，PRIVATE_CORE。依先锁定的 HEAT_COMPATIBILITY_CONTRACT.md 推导，独立核对前为主稿。本证明处理指定完整热权重的 w₂₂ 树，不处理完整 NS 原解。

**命题。** 对剩余正长度 q₁<q₂<q₃、q₂²<q₁q₃，两个已知各自唯一的时间严格满足
\[
t_{13}<t_{12}^{(2)}.
\]
因此 g₁=g₃=2g₂ 在任何正时间都不成立。结合已经接纳的热排序与相位门，三对互异正整数轴向长度、全部非零复二维横向极化、一次平移和相容正交符号变换下，指定 w₂₂ 树均不能在全部加倍接收模上成为统一幅度原模板。

此全时间表述只分类定义良好的树积分，不延长真实 NS 存在时间，不支付完整原解的混合树与无限维余项。

## 1. 消去共同基频

写
\[
X=q_1,\quad A=q_2-q_1,\quad B=q_3-q_2,\quad C=A+B.
\]
剩余条件 (X+A)²<X(X+C) 等价于
\[
B>A>0,\qquad X>\frac{A^2}{B-A}.                             \tag{HC.1}
\]
频率差比为
\[
\alpha=\frac{A}{2X+A},\quad
\beta=\frac{B}{2X+2A+B},\quad
\gamma=\frac{C}{2X+C}.
\]
令
\[
K_1=H_{12}H_{13},\quad K_2=H_{21}H_{23},\quad K_3=H_{31}H_{32},
\qquad P=K_1/K_3,\quad Q=K_1/K_2.                           \tag{HC.2}
\]
所有量取同一正时间。共同平移 q_i→q_i+X₀ 只给每个H乘 exp(−4X₀t)，故P、Q只依赖A、B、t。这是符号消元，不是改变实际原解的初值。

在唯一时间t=t₁₃，g₁=g₃给 αP=β。因此
\[
1<P=\beta/\alpha<B/A.                                      \tag{HC.3}
\]
最后的严格上界可直接从α、β分式得到，因为2X+A<2X+2A+B。解出X并代回可得
\[
X=\frac{A[P(2A+B)-B]}{2(B-AP)},\quad
2X+A=\frac{APC}{B-AP},\quad
2X+2A+B=\frac{BC}{B-AP},\quad
2X+C=\frac{A^2P+B^2}{B-AP}.
\]
因此在该同一个时间
\[
\frac{g_1}{g_2}=\frac{\gamma}{\beta}Q
=\frac{C^2Q}{A^2P+B^2}.                                    \tag{HC.4}
\]
要使另一个门同时满足g₁=2g₂，必须Q=2(A²P+B²)/C²。以下证明严格小于。

## 2. 三行对数热积分的曲率界

固定t>0及三个q_j。引入辅助实变量x，记
\[
H(x,y;t)=t^3e^{-4xt}f(2(x-y)t),\qquad
f(u)=\int_0^1\theta^2e^{u\theta}\,d\theta.
\]
它在x=q_i、y=q_j时恰是原H_ij。定义
\[
\Phi(x)=\sum_{j=1}^3\log H(x,q_j;t)-\log H(x,x;t).
\]
在三个轴值上，Φ(q_i)=logK_i。由于f(0)=1/3，
\[
\Phi(x)=6\log t-8xt+\sum_{j=1}^3\log f(2(x-q_j)t)-\log f(0).
\]
在任意有限实u上，以θ²e^(uθ)/f(u)为概率密度，(logf)''等于θ的方差。密度在(0,1)正，故
\[
0<(\log f)''<1/4.
\]
例如Eθ²<Eθ给Varθ<Eθ(1−Eθ)≤1/4，严格性不依赖两端点密度为正。于是
\[
0<\Phi''(x)<3t^2.                                          \tag{HC.5}
\]
微分只涉及紧区间正积分；辅助x并非新的物理频率选取。

置
\[
\lambda=A/C,\qquad \omega=B/C=1-\lambda,\qquad 0<\lambda<1/2.
\]
三个位置X、X+A、X+C的弦差为
\[
E_{\rm heat}
=\omega\Phi(X)+\lambda\Phi(X+C)-\Phi(X+A)
=\log Q-\lambda\log P.
\]
凸性与二阶上界给
\[
0\le E_{\rm heat}\le\frac32ABt^2.                           \tag{HC.6}
\]
具体地，Φ(x)−(3t²/2)x²为凹函数，应用中间点的凹性，二次弦差恰为AB，即得上界。没有把对数热核错当成凹函数。

已接纳的热排序证明给(logP)' >2C及P(0+)=1。设ℓ=logP，则
\[
t<\frac{\ell}{2C}.
\]
代入HC.6得到
\[
E_{\rm heat}<\frac38\lambda\omega\,\ell^2.                   \tag{HC.7}
\]
这里完全保留热核的不同权重，没有小时间近似或未估余项。

## 3. 返回等式要求的严格正间隙

令
\[
L=\log(\omega/\lambda)>0.
\]
HC.3给0<ℓ<L。定义标量函数
\[
h(\ell)=\log[2(\lambda^2e^\ell+\omega^2)]-\lambda\ell.
\]
其导数为
\[
h'(\ell)=\frac{\lambda^2e^\ell}{\lambda^2e^\ell+\omega^2}-\lambda<0
\quad(0\le\ell<L).
\]
故
\[
h(\ell)\ge h(L)
=\log2+\lambda\log\lambda+\omega\log\omega=:\mathcal D(L).
                                                                    \tag{HC.8}
\]
需要一份明确下界，不能只引用该量非负。

以s≥0为积分变量，写λ_s=1/(1+e^s)、ω_s=1−λ_s，令
\[
\mathcal D(s)=\log2+\lambda_s\log\lambda_s+\omega_s\log\omega_s.
\]
直接微分给D'(s)=sλ_sω_s，且D(0)=0。λ_sω_s在s>0严格递减，所以
\[
\mathcal D(L)=\int_0^L s\lambda_s\omega_s\,ds
>\frac12\lambda\omega L^2.                                  \tag{HC.9}
\]
这是有限实积分恒等式及单调性，不需要外部概率不等式或数值熵估计。

## 4. 矛盾与时间次序

在t=t₁₃，将HC.4、HC.7–9合并：
\[
\begin{aligned}
\log\frac{2g_2}{g_1}
&=\log[2(\lambda^2P+\omega^2)]-\log Q\\
&=h(\ell)-E_{\rm heat}\\
&>\frac12\lambda\omega L^2-\frac38\lambda\omega\ell^2\\
&>\frac18\lambda\omega L^2>0 .
\end{aligned}                                               \tag{HC.10}
\]
因此g₁(t₁₃)<2g₂(t₁₃)，两个门不能同时成立。由于g₁/g₂已经证明严格递增且在剩余长度下唯一达到2，必有t₁₃<t₁₂^(2)。

所有常数均来自方差的统一1/4上界和已经接受的严格热时间界；没有逐参数调整常数。λ趋向0或1/2时下界可退化，本命题并未声称对所有长度存在一个统一正数间隙。每个题定B>A给出的HC.10则严格为正，足以排除等式。

## 5. 树分类与原解的边界

本证明连同热排序门封闭了全部互异正轴长度的树模板方程：q₂²≥q₁q₃由旧排序排除；q₂²<q₁q₃由HC.10排除。主推导甚至适用于正实平方频率的辅助代数域，故覆盖原固定环面的正整数长度子集；没有把非整数辅助频率当作实际候选。

全部完整复极化与八个相容正交符号分支已在前门保留并归结为必要等式。本轮否定该必要等式，不再需要为已失败的分支寻找极化系数。因此结论为 **NO-CANDIDATE FOR THE SPECIFIED EXACT HEAT-WEIGHTED PURE-2+2 DOUBLED-TEMPLATE GATE**。

这不是完整NS的再生成不可能定理。w₂₂只有四叶根分裂2+2，真实解仍包含1+3/3+1、原种子、目标外作用、后继回流与其它时间树。v₁不是已认证的实际前代投影，树与原解之差的无限维余项没有支付。没有排除其它模板、近似返回或更宽支撑，没有接受单个固定初值的有限两步奇性机制，也没有统一无限尺度、有限总时间或NS奇性/正则性结论。
