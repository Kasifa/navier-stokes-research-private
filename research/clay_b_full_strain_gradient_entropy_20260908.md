# 完整应变梯度、形状耗散与时间指数的缺口

2026-09-08，北京时间。SG，PRIVATE_CORE。本地解析推导及经典结果的范围核对；一般三维 Navier–Stokes 正则性仍为 OPEN / NOT CLAY。不宣称新颖性或真人同行评审。

这一步补充了 SC 中没有估计的完整应变梯度，但有对数权重损失。另一个凸函数直接控制完整归一化应变的空间变化，不限于正负谱子空间。两者共同给出归一化形状和孤立特征线的加权抛物算子估计。实际插值没有得到 SC.11 所需的时间指数；以下把正面估计和这一限制一起证明。

## 1. 对象、初值与经典输入

同一个无散、无外力光滑 NS 解，固定未归一化的 \(\mathbb T^3_{2\pi}\)、\(\nu>0\)，先在闭光滑区间 \([0,T]\) 计算。沿用 SE、SC 的
\[
 A_{ij}=\partial_j u_i,\quad S=\operatorname{sym}A,\quad
 \Omega=\operatorname{skew}A,\quad H=\nabla^2p,\quad
 N=S^2+\Omega^2+H,\quad L=\partial_t+u\cdot\nabla-\nu\Delta,
 \qquad LS=-N.
 \tag{SG.1}
\]
矩阵范数为 Frobenius 范数；\(q=|S|\)，\(q_{\rm op}=|S|_{\rm op}\)。所有未注明区域的空间积分在整胞上。设
\[
 E_0=\tfrac12\|u(0)\|_2^2,\quad
 \mathcal N_0=\int\operatorname{tr}|S(0)|,\quad
 G=|A|^2+\sqrt3|H|,\quad G_F=|A|^2+|H|,
\]
\[
 \mathcal B=\mathcal N_0+(1+\sqrt3C_H)E_0/\nu,\qquad
 \mathcal B_F=\int q(0)+(1+C_H)E_0/\nu.
 \tag{SG.2}
\]
SE.2–4 的经典周期散度—旋度 Hardy 估计给 \(\|H(t)\|_1\le C_H\|A(t)\|_2^2\)。结合能量等式，\(\int_0^T G\le\mathcal B-\mathcal N_0\)。本稿依赖这一已核对的接口，不对一般 L1 函数声称 Riesz 变换 L1 有界，也不将初始梯度项 \(\mathcal N_0\) 擅自换成 \(E_0\)。

下文对数中的固定幅度单位选为 1；可以引入任何固定正参考幅度并相应改常数。这些对数权重不是缩放不变估计。所有有限候选终点的结论只涉及 \(T\uparrow T_*\) 前的累计量，不假定终点存在强迹或光滑延拓。

## 2. 有界斜率的凸谱函数控制完整梯度

取偶的 \(C^2\) 凸函数 h，\(h(0)=0\)、\(|h'|\le1\)。SE.7–9 的同一链式法则给
\[
 \mathcal E_h(T)+\nu\int_0^T\!\!\int d_h
 =\mathcal E_h(0)-\int_0^T\!\!\int h'(S):N\le\mathcal B,
\quad
 \mathcal E_h(t)=\int\operatorname{tr}h(S),\quad
 d_h=\sum_kD^2\operatorname{tr}h(S)[\partial_kS,\partial_kS]\ge0.
 \tag{SG.3}
\]
这里 \(h\ge0\)、\(h(s)\le|s|\)。在 S 的特征基中，Hessian 的对角系数是 \(h''(\lambda_i)\)，非对角系数是 \(2[h'(\lambda_i)-h'(\lambda_j)]/(\lambda_i-\lambda_j)\)；重根按连续极限解释。

具体选
\[
 w(r)=\frac1{(e+r)\log^2(e+r)},\quad r\ge0,\qquad
 h(s)=\int_0^{|s|}(|s|-r)w(r)\,dr.
 \tag{SG.4}
\]
于是 \(h''(s)=w(|s|)\)，
\(h'(s)=\operatorname{sign}(s)[1-1/\log(e+|s|)]\)，在 0 取 0。
函数 h 为全域 \(C^2\) 偶凸函数，且 \(|h'|\le1\)。w 单调递减；差商是两特征值之间 \(h''\) 的平均。因此对任意实对称矩阵 V，
\[
 D^2\operatorname{tr}h(S)[V,V]\ge w(q_{\rm op})|V|^2\ge w(q)|V|^2.
\]
代入 SG.3 得
\[
 \boxed{D_w(T):=\nu\int_0^T\!\!\int
       \frac{|\nabla S|^2}{(e+|S|)\log^2(e+|S|)}
       \le\mathcal B.}
 \tag{SG.5}
\]
这包括对角幅度导数、同号谱块变化和跨符号谱变化，在零谱与重根处不退化为未定义表达式。与 SE.11 不同，SG.5 是完整梯度的加权估计；它没有给出去掉对数的 \(\int|\nabla S|^2/q\)。

## 3. 完整归一化形状的空间耗散

谱绝对值 \(\operatorname{tr}|S|\) 在同号谱块上是线性的，但矩阵 Frobenius 范数不是。取
\[
 \Phi_\epsilon(S)=\sqrt{|S|^2+\epsilon^2}-\epsilon,\qquad
 B_\epsilon=S/\sqrt{|S|^2+\epsilon^2}.
\]
直接微分得非负 Hessian 密度
\[
 d_\epsilon=\sum_k\left[
 \frac{|\partial_kS|^2}{\sqrt{q^2+\epsilon^2}}-
 \frac{(S:\partial_kS)^2}{(q^2+\epsilon^2)^{3/2}}\right]\ge0.
 \tag{SG.6}
\]
\(|B_\epsilon|\le1\)，故 \(|B_\epsilon:N|\le G_F\)。在 \(q>0\) 上令 \(B=S/q\)；在零集只为定义源项取 \(B_0=0\)，其余处 \(B_0=B\)。同 SE 的分布极限论证给唯一非负测度
\[
 \mu_F=\frac{-B_0:N-Lq}{\nu}
 =\mathbf1_{\{q>0\}}q|\nabla B|^2\,dxdt+\zeta_F,\qquad
 \zeta_F\ge0,\quad\operatorname{supp}\zeta_F\subset\{q=0\}.
 \tag{SG.7}
\]
具体地，\(\Phi_\epsilon\to q\) 一致，源项受 \(G_F\) 控制；固定光滑区间内
\(\int d_\epsilon=-\int B_\epsilon:\Delta S\le\|\Delta S\|_1\)，
排除时间端点聚集。在 \(q>0\) 的紧子集上 Hessian 一致趋于 SG.7 的密度。正性给余测度及其支撑；本稿不删除零集项，也不必判定其进一步分解。

因此
\[
 \boxed{\int q(T)+D_B(T)+\nu\zeta_F(\mathbb T^3\times(0,T))
 \le\mathcal B_F,\qquad
 D_B(T)=\nu\int_0^T\!\!\int_{q>0}q|\nabla B|^2.}
 \tag{SG.8}
\]
它控制整个归一化矩阵的空间形状变化，包括同号特征值的相对比例，而不控制径向幅度导数。恒等式
\(|\nabla S|^2=|\nabla q|^2+q^2|\nabla B|^2\) 只在 \(q>0\) 使用。

## 4. 能估计抛物算子，不能把它改称时间变差

在 \(q>0\) 上，直接使用 SG.1 和乘积法则：
\[
 Lq=-B:N-\nu q|\nabla B|^2,
\qquad
 \boxed{LB=-\frac{N-(B:N)B}{q}
       +\nu|\nabla B|^2B+2\nu\nabla\log q\cdot\nabla B.}
 \tag{SG.9}
\]
两个黏性项都是正号；\(B:LB=\nu|\nabla B|^2\) 与 \(|B|=1\) 相符。定义
\[
 b(q)=\sqrt{q\,w(q)}
 =\frac{\sqrt{q/(e+q)}}{\log(e+q)},\qquad 0\le b\le1.
\]
投影 \(N-(B:N)B\) 的范数不超过 \(|N|\le G_F\)，混合项由
\(b^2/q=w\) 和 \(|\nabla q|\le|\nabla S|\) 配对。Cauchy–Schwarz 遂给
\[
 \boxed{\int_0^T\!\!\int_{q>0}q\,b(q)|LB|
 \le\int_0^T\!\!\int G_F+D_B(T)+2\sqrt{D_B(T)D_w(T)}.}
 \tag{SG.10}
\]
这是同一实际 NS 解上的无条件加权估计，常数由固定初值和黏性控制；不声称其为文献中未知的结果。它没有单独估计 \(\Delta B\)，因而不等于 \(\partial_tB\) 或 \((\partial_t+u\cdot\nabla)B\) 的 BV 时间控制。不能跨 \(q=0\) 将 SG.9 当作全域 B 方程。高幅度权重约为 \(q/\log q\)，低幅度权重约为 \(q^{3/2}/\sqrt e\)。

## 5. SC 的孤立特征线：两个符号区域一并保留

SC.4 的行列式证明没有用锥的凸性。如果 \(T(x)\in K_{e,\delta}\cup(-K_{e,\delta})\)，其固定平面压缩的行列式仍至少为 \(\delta(1-\delta)a^2\)，余子式范数的界也不变。因此 SC.4 对双侧锥成立，a 为非负幅度。这里仍是同一个空间固定轴 e，不允许任意随 x 改轴。

在开集 \(\det S\ne0\) 上令 \(\sigma=\operatorname{sign}\lambda_2\)。若 \(\sigma=1\)，f 是负孤立特征线、\(a=-\lambda_1\)；若 \(\sigma=-1\)，f 是正孤立特征线、\(a=\lambda_3\)。统一写为 \(Sf=-\sigma af\)。\(\sigma\) 在各开区域局部常值，\(a\le q\le\sqrt2a\)。令 \(P=f\otimes f,\ \Pi=I-P\)，
\[
 J_\sigma=\Pi[(\sigma S+aI)|_{f^\perp}]^{-1}\Pi.
\]
SE.11 与 SC 的同一推导给
\[
 d_\pm=4\sum_k\partial_kf\cdot(\sigma S+aI)\partial_kf,\qquad
 2a|\nabla P|^2\le d_\pm\le4a|\nabla P|^2,
\]
\[
 La=\sigma\left[a^2-\tfrac14|\omega\times f|^2+f\cdot Hf\right]
       -\tfrac\nu2d_\pm,
\]
\[
 Lf=\nu|\nabla f|^2f+
 J_\sigma\Pi\left[\sigma\left(Hf+\tfrac14(\omega\cdot f)\omega\right)
 +2\nu\sum_k(\sigma\partial_kS+(\partial_ka)I)\partial_kf\right].
 \tag{SG.11}
\]
证明对 \((\sigma S+aI)f=0\) 施加 L，保留乘积的 \(-2\nu\) 交叉项，再分别取 f 分量和垂直分量。用 \(\Omega^2=(\omega\otimes\omega-|\omega|^2I)/4\) 得所写符号。P 的方程仍为 SC.15，不依赖局部 f 的换号。仅在上述开集断言，不跨零谱求 \(\sigma\) 的导数。

特别地，SC.16 的绝对值界在两区域上均成立。由于 \(w(a)\le Cw(q)\) 当 \(a\le q\le\sqrt2a\)，SG.5、SE.13 及
\[
 b(a)|\nabla S||\nabla P|
 =\sqrt{w(a)|\nabla S|^2}\sqrt{a|\nabla P|^2}
\]
给
\[
 \boxed{\int_0^T\!\!\int_{\det S\ne0}a\,b(a)|LP|
 \le C\left[\int_0^T\!\!\int(|H|+|\omega|^2)
       +D_P+\sqrt{D_wD_P}\right]<\infty,\quad
 D_P=\nu\int_0^T\!\!\int_{\det S\ne0}a|\nabla P|^2\le\mathcal B/2.}
 \tag{SG.12}
\]
常数与光滑终点高阶范数无关。相比 SC.16，这是混合项带对数损失的实际控制，不是未加权混合项已可积，更不是孤立线的时间 BV。

双侧锥也允许在 SC.6 中以 \(|\lambda_2|\ge\delta a\) 和孤立线角度定义好集，连同 \(S=0\)。SC.7–10 保持成立，因为原旋转和余项分解只需将 T 放在双侧锥中，不对好集指示函数求导。相应补集仍含所有非零零中间谱、近零中间谱和角度失效点；它的 L4 时间条件仍需另证。不能因处理了两种谱符号就把补集删除。

## 6. 幅度层边界的正测度没有被抹去

完整梯度权重也可拆成真实谱幅度层。对 \(M>0\) 定义
\[
 h_M(s)=(|s|-M)_+,\quad F_M(S)=\operatorname{tr}h_M(S),\quad
 q_M(s)=
 \begin{cases}\operatorname{sign}s,&|s|>M,\\
 \tfrac12\operatorname{sign}s,&|s|=M,\\0,&|s|<M.\end{cases}
\]
用固定偶的非负光滑近似恒等核卷积 \(h_M\)，减去在 0 的值。这样得到非负凸光滑函数，斜率不超过 1，导数极限正是 q_M。令 \(Q_M=q_M(S)\)，链式极限给
\[
 \mu_M=\frac{-Q_M:N-LF_M(S)}{\nu}\ge0,\quad
 \int F_M(S(T))+\nu\mu_M(\mathbb T^3\times(0,T))
 =\int F_M(S(0))-\int_0^T\!\!\int Q_M:N.
 \tag{SG.13}
\]
在没有特征值等于 \(\pm M\) 的开集上，其普通密度为
\[
 d_M=2\sum_{k,i<j}
 \frac{q_M(\lambda_i)-q_M(\lambda_j)}{\lambda_i-\lambda_j}
 |(\partial_kS)_{ij}|^2.
 \tag{SG.14}
\]
该开集的对角系数为零，重根差商为零。除此之外还要保留非负余测度 \(\zeta_M\)，支撑在谱层边界 \(\{\operatorname{spec}S\cap\{-M,M\}\ne\varnothing\}\)；不直接称其为纯奇异测度。固定光滑区间上的逐时耗散界 \(\int d_{M,\epsilon}\le\sqrt3\|\Delta S\|_1\) 同样排除时间端点原子。M>0 时零谱不是 h_M 的新折点，但仍可能参与 SG.14 的跨层密度。

\(Q_M=0\) 于 \(q_{\rm op}<M\)。故
\[
 \boxed{\int F_M(S(T))+\nu\mu_M
 \le\int F_M(S(0))+\int_0^T\!\!\int_{\{q_{\rm op}\ge M\}}G.}
 \tag{SG.15}
\]
右侧在 \(M\to\infty\) 时趋零，也可先取有限候选终点前的累计上界；这只有可积尾部结论，没有关于 M 的所需速率。

Tonelli 与分布链式等式进一步给
\[
 h(s)=\int_0^\infty w(M)h_M(s)\,dM,\qquad
 d_h\,dxdt=\int_0^\infty w(M)\mu_M\,dM.
 \tag{SG.16}
\]
第二式是非负测度的弱积分恒等式，可先对紧支集测试函数积分核验；源项因 \(\int_0^\infty w=1\) 绝对可积。幅度层边界本来就是完整熵耗散的一部分，不是分层后可丢弃的误差。

## 7. 二阶导数的弱 L4/3 控制及其文献位置

这一体系也重得一个经典强度的界，不将它计算为新的临界增益。选固定光滑偶函数 \(\rho\)，\(0\le\rho\le1\)，在 \([-1,1]\) 为 1，在 \([-2,2]\) 外为 0。令 \(k''=\rho,\ k(0)=k'(0)=0\)，\(k_M(s)=Mk(s/M)\)。则 \(|k_M'|\le2\)、\(0\le k_M\le2|s|\)，且当 \(q_{\rm op}\le M\) 时矩阵 Hessian 至少为 \(1/M\) 倍恒等二次型。SG.3 的斜率 2 版本给
\[
 \int_{\{q_{\rm op}\le M\}}|\nabla S|^2\le D M,\qquad D=2\mathcal B/\nu.
\]
设 \(K=\int_0^T\int q^2\le E_0/\nu\)。时空集合的测度满足
\[
 |\{|\nabla S|>\Lambda\}|
 \le K/M^2+DM/\Lambda^2.
\]
若 K、D 正，取 \(M=(K/D)^{1/3}\Lambda^{2/3}\) 得
\[
 |\{|\nabla S|>\Lambda\}|\le2K^{1/3}D^{2/3}\Lambda^{-4/3}.
 \tag{SG.17}
\]
零值情形直接退化为平凡界。由逐点相容性
\[
 \partial_j\partial_k u_i
 =\partial_jS_{ik}+\partial_kS_{ij}-\partial_iS_{jk},
 \qquad|\nabla^2u|\le3|\nabla S|,
\]
故二阶速度导数也有同类弱 L4/3 界。这里没有调用弱 L1 Riesz 有界性。

[Vasseur–Yang 原稿](https://arxiv.org/html/2009.14291v1) 导言记述 Constantin 的周期二阶导数结果及 Lions 的弱 L4/3 改进；其 Corollary 1.2 对全空间有限能量适当弱解给更细的局部 \(L^{4/3,\ell}\)、\(\ell>4/3\) 控制。本轮实际核对导言、Theorem 1.1、Corollary 1.2 和 Theorem 1.3 的条件，未重审全文证明或本轮重读 Constantin、Lions 原著。SG.17 只是在当前光滑周期框架中的直接推导，既不宣称超越那些结果，也不擅自推广到任意适当弱解。

## 8. 实际插值的结果与仍然缺少的时间指数

令
\[
 \Psi(q)=\int_0^q\sqrt{w(s)}\,ds.
\]
由 \(|\nabla q|\le|\nabla S|\)、SG.5 和 \(\Psi(q)^2\le Cq\)，在任意固定有限候选区间前有
\[
 \Psi(q)\in L^\infty_tL^2_x\cap L^2_tH^1_x.
\]
三维 Sobolev 和插值给
\[
 \Psi(q)^2\in L^{1/\theta}_tL^{3/(3-2\theta)}_x,\qquad0\le\theta\le1.
 \tag{SG.18}
\]
高幅度时 \(\Psi(q)^2\) 与 \(q/\log^2(e+q)\) 两侧可比；有界幅度部分在有限时空胞上直接控制。因此 SG.18 也适用于 \(Z=q/\log^2(e+q)\)。例如 \(\theta=3/4\) 只给 \(Z\in L^{4/3}_tL^2_x\)，而非 \(q\in L^4_tL^2_x\)。

即使暂时把对数损失乐观地忽略，SG.18 的端点 \(L^\infty_tL^1_x\)、\(L^1_tL^3_x\) 以及基本能量的 \(L^2_tL^2_x\)，其 \((1/p,1/r)\) 分别为 \((0,1)\)、\((1,1/3)\)、\((1/2,1/2)\)。线性量 \(2/p+3/r\) 分别为 3、3、5/2，插值不能达到应变临界线 2。特别是 SC.11 需要的 \(L^4_tL^2_x\) 不在这个插值范围内。恢复对数损失只会削弱结论。

这只是对所列范数及其直接插值的精确限制，不是所有 NS 方法的不可行性定理；也没有用一个非 NS 脉冲族冒充实际解反例。SG.10、12 仍可用于后续局部分析，但它们目前没有给出临界补集范数或跨层边界的时间小性。

## 9. 这一方法的一个边界与下一项计算

只靠有界斜率的凸函数，不能在所有大幅度上令 \(h''(s)\ge c/s\)：积分会给 \(h'(R)-h'(1)\ge c\log R\)，与斜率有界矛盾。即使只要求迹零矩阵上的完整径向控制，沿 \(S=\operatorname{diag}(R,-R,0)\) 也有同一障碍。它仅限制这一凸测试构造，不排除带符号消项、压力补偿或其他动力学方法。

本小节的确切增量是 SG.5、8、10、12 的完整梯度／形状估计，SC 双侧锥的扩展，以及保留层边界的 SG.13–16。没有新的无条件临界估计，不能以这些低阶累计量推断任意初值正则性。

下一项转向一个实际未受控的项，而不再更换有界权重：对光滑的 \(q\log(e+q)\) 型径向熵，写出完整源项 \(-D\Phi(S):N\) 和耗散，检查带对数的惯性／压力配对是否有来自原 NS 相容性的可用消项。必须先写精确等式再评估能否闭合；压力的 L1 控制本身不足以支持无界测试系数。即使只消去梯度权重的对数损失，第 8 节的直接插值仍达不到临界线，故这项计算只作为局部几何机制的有限检查，不自动开启另一轮权重改良。若未能得到可用于临界问题的额外控制，保留未证项，不把换熵函数列为新的正则性结果。

没有仿真、DGX 作业、数值证书、科学附图或新的公开回顾。推导和审读为 AI 辅助研究；实际文件审查范围另记。完整证明默认私有，后续一次交接不等于归档已经执行。
