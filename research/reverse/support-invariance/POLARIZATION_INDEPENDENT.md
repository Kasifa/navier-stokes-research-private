# 同一轴投影极化：独立有界推导

2026-09-08。PRIVATE_CORE。INDEPENDENT DERIVATION / NON-AUTHOR REVIEW PENDING / NO-CANDIDATE / NOT CLAY。

## 1. 合同、接触历史与直接输入

先全文读 POLARIZATION_CONTRACT.md，SHA-256：
de3df9e8df78d42f619996c411425b6ce6c66bedaf1a8285bbfc4e29076d7483。
合同已披露根在锁定前手工预检过“三重积乘两个方向余弦平方之差”及全秩寻对思路。本文在这一已披露目标下独立逐式推导，不称对结构完全盲推；没有读取 POLARIZATION_PROOF.md，也没有接收另一作者的新公式。

本人此前写过 Miller 原文范围预检，知道其模型同时限制频谱、极化并改变非线性后的投影；该来源经历不作为本项完整 NS 不变性的证明。本文不使用 Miller 的实际壳数据或模式计算。

唯一旧数学输入为 reconnection-preflight/SOURCE_ATTRIBUTION_LEMMA.md（SAL），本轮实际读第1–114行（§§1–2）及第173–225行（§4）；SHA-256：
d22bcca237977647b54ebbe13288c63a24a7c610a52a7c2265f4e3cfe366607a。
使用其完整 Fourier–Leray 算子、Wiener局部构造、同窗光滑性及唯一性。定位 SAL 时，一次检索也返回纯支撑 PROOF/MAIN_REVIEW 的少量 SAL 调用片段；没有展开这些文件，且不以这些片段或纯支撑阶段的未来接纳为本项输入。

固定 \(T^3=(\mathbb R/2\pi\mathbb Z)^3\)、\(\nu>0\)、非零实向量 \(\sigma\)，及满足
\(\operatorname{span}_{\mathbb R}L=\mathbb R^3\) 的加法子群 \(L\subset\mathbb Z^3\)。对非零频率，
\[
 P_k=I-\frac{k\otimes k}{|k|^2},\qquad
 U_k=P_k\sigma,\qquad E_k=\mathbb C U_k.
 \tag{PI.1}
\]
若 \(U_k=0\)，这里的 \(E_k\) 就是零空间。允许的场实值、光滑、无散、零均值，且系数支撑在 L、逐模位于这些 E；标量仅受实值共轭约束。

**结论。** 对每个上述固定 \(\sigma,L,\nu\)，存在本文符号构造的有限 Fourier 初值，其同一完整 NS 解对所有充分小的正时间均离开该极化空间。这个结论针对整个自由标量空间，不排除其中的特殊不变子类或特殊轨道。

## 2. 两个有序输入的完整线外测试

先取非零、不共线的 \(p,q\)，令 \(k=p+q\)，并在
\(n=k\times\sigma\ne0\) 的分支工作。记
\[
 P=|p|^2,\quad Q=|q|^2,\quad C=p\cdot q,\quad
 a=\sigma\cdot p,\quad b=\sigma\cdot q,\quad
 D=\sigma\cdot(p\times q).
 \tag{PI.2}
\]
P、Q在本节为正实数，不与带频率下标的 Leray 投影混同。所有实向量的点积按双线性方式延拓到复向量。

设在 p、q 的输入系数分别为 \(c_pU_p,c_qU_q\)。完整两个有序来源给 k 的非线性系数
\[
 -i c_pc_q P_k W,\qquad
 W=(U_p\cdot q)U_q+(U_q\cdot p)U_p.
 \tag{PI.3}
\]
这是 SAL 的 \(B(f,g)=-P_L[(f\cdot\nabla)g]\) 在所定 \(e^{ik\cdot x}\) 规范下的系数；没有将有序项减半或只留一个方向。

由 \(n\perp k,\sigma\)，有 \(n\cdot P_kW=n\cdot W\)，且
\[
 n\cdot p=D,\quad n\cdot q=-D,\quad
 U_p\cdot q=b-\frac{aC}{P},\quad
 U_q\cdot p=a-\frac{bC}{Q}.
 \tag{PI.4}
\]
于是直接展开，两项混合乘积恰好抵消：
\[
 \begin{aligned}
 n\cdot W
 &=D\left[\frac bQ\left(b-\frac{aC}{P}\right)
          -\frac aP\left(a-\frac{bC}{Q}\right)\right]\\
 &=D\left(\frac{b^2}{Q}-\frac{a^2}{P}\right).
 \end{aligned}
 \tag{PI.5}
\]
因此线外测试量为
\[
 d=-i c_pc_q\,D
       \left(\frac{(\sigma\cdot q)^2}{|q|^2}
                    -\frac{(\sigma\cdot p)^2}{|p|^2}\right).
 \tag{PI.6}
\]
此处测试方向是 \(k\times\sigma\)；若反转该方向，符号也相应反转。因 \(n\cdot U_k=0\)，非零 d 认证完整 Leray 输出在 \(E_k\) 之外。括号等于 \(|\sigma|^2\) 乘两方向余弦平方之差，但式(PI.6)不引入归一化极化或隐藏的长度因子。

这一步不假定 p、q 等长、异长、正交或非正交。若某一输入平行 \(\sigma\)，其实际 \(U\) 为零，不能补入其它极化。若 \(k\parallel\sigma\)，则 \(E_k=0\)、n也为零，本测试不作非零认证。三重积或括号为零的分支，同样不被误读为整个空间保持；下面仅证明总能避开这些零分支。

## 3. 任意全秩 L 都有非退化对

首先在 L 中找到
\[
 a=\sigma\cdot p\ne0,\qquad p\not\parallel\sigma .
 \tag{PI.7}
\]
因为 L 的实张成是全空间，存在 \(r\in L\) 使 \(\sigma\cdot r\ne0\)。若 r 已不平行 \(\sigma\)，取 p=r 即可。否则，由全秩取 \(v\in L\setminus\operatorname{span}\sigma\)。对于符号整数 j，\(r+jv\) 在 \(j\ne0\) 时不平行 \(\sigma\)，而 \(\sigma\cdot(r+jv)=0\) 至多排除一个 j。整数集不被这有限集合耗尽，故存在满足(PI.7)的 p。这里没有挑选或枚举一个具体整数样本。

由于 \(\sigma\times p\ne0\)，全秩又给 \(q_0\in L\)，使
\[
 D_0=\sigma\cdot(p\times q_0)\ne0.
 \tag{PI.8}
\]
否则整个 L 均落在该非零线性泛函的核平面，矛盾。
考虑所有符号整数 h 对应的 \(q_h=q_0+hp\in L\)。它们均有相同的非零三重积 D₀，因而 q_h非零、不与 p 共线、也不平行 \(\sigma\)；\(p+q_h\) 亦不平行 \(\sigma\)。

写 \(b_0=\sigma\cdot q_0,\ C_0=p\cdot q_0,\ Q_0=|q_0|^2\)。方向平方差的分子为
\[
 \begin{aligned}
 F(h)&=P(\sigma\cdot q_h)^2-a^2|q_h|^2\\
 &=P b_0^2-a^2Q_0+2h(Pab_0-a^2C_0).
 \end{aligned}
 \tag{PI.9}
\]
二次项严格抵消，故它至多一次。若 F恒零，因 \(a\ne0\)，一次系数先给
\(b_0=aC_0/P\)，常数项继而给
\[
 C_0^2=P Q_0.
 \tag{PI.10}
\]
实 Euclidean Cauchy–Schwarz 的等号迫使 p、q₀共线，与(PI.8)矛盾。
因此 F不是零多项式。它或者是非零常数，或者仅有一个实零点；两种分支下都存在整数 h 使 \(F(h)\ne0\)，不需要数值选择或扫描。

固定这样的符号 q=q_h 后，
\[
 D\ne0,\qquad
 \frac{b^2}{Q}-\frac{a^2}{P}
   =\frac{F(h)}{P|q_h|^2}\ne0.
 \tag{PI.11}
\]
这也保证 \(U_p,U_q,U_k\ne0\) 和 \(k\ne0\)，将(PI.6)的输入、输出及测试方向全部落在非退化分支。证明只用了全秩和加法子群性质，不假定 L 等于整个整数格。

## 4. 从符号系数到同一真实解的严格 o(t)

对上节的 p、q，任取两个非零复标量 \(c_p,c_q\)，保留全部共轭，定义符号有限初值
\[
 A(x)=c_pU_p e^{ip\cdot x}
       +\overline{c_p}U_p e^{-ip\cdot x}
       +c_qU_q e^{iq\cdot x}
       +\overline{c_q}U_q e^{-iq\cdot x}.
 \tag{PI.12}
\]
此式不选实际频率或标量数值。由于 \(U_{-p}=U_p\)、\(U_{-q}=U_q\) 均为实向量，A符合实值共轭条件；无散、零均值、光滑，并位于合同空间。

p、q不共线，所以 k=p+q不属于这四个初始支撑点。在完整初始卷积中，加和为 k 的来源恰为有序的 (p,q) 和 (q,p)；共轭对及自作用不会另给 k。于是 \(\widehat A(k)=0\)，且对完整 NS，
\[
 \left.\frac{d}{dt}\widehat u(k,t)\right|_{t=0}
 =-\nu|k|^2\widehat A(k)+\widehat{B(A,A)}(k)
 =-i c_pc_qP_kW.
 \tag{PI.13}
\]
黏性项为零只因这个目标模初始为零；压力始终通过完整 Leray 保留。没有在正时间删除任何其它频率或反馈。

SAL §4从这个光滑 A 给一个正的数据依赖窗口中的完整无限维 NS 解，并在同一窗口给空间各阶连续性和由方程得到的时间正则。因此该固定 Fourier 系数在初始时刻可微，其固定线外测试满足
\[
 n\cdot\widehat u(k,t)=t\,d+o(t),\qquad d\ne0,
 \quad t\downarrow0.
 \tag{PI.14}
\]
o(t)属于这一完整真实解。它包含所有随后生成的模式及全部高阶相互作用，不是有限 Galerkin 或受限投影模型的误差。

由 o(t)的定义，存在同一数据决定的 \(T_A>0\)，使
\[
 |n\cdot\widehat u(k,t)|\ge\frac{|d|}{2}\,t>0,
 \qquad 0<t<T_A.
 \tag{PI.15}
\]
因而这整段正时间均有 \(\widehat u(k,t)\notin E_k\)。只承诺存在性小窗，没有求数值时刻、统一时窗或把充分局部窗口当成最大存在时刻。

## 5. 结论的有限范围

所有固定非零实 \(\sigma\) 和全秩整数子群 L 都满足上述非闭合结论。输出频率仍在 L；失败来自极化线外分量，并非支撑不加法。

这一见证可保有垂直于 p、q平面的平移不变性，不能据其称作新的三维奇性初值。本文不分类低秩 L、受限标量相干、额外离散对称、任意极化丛、孤立特殊解或近似不变空间，尤其不将此自由标量、全子群论证推广为 Miller 特定壳/极化/对称组合的真实泄漏证明。

没有科学程序、数组、实际整数例子、数值求值、扫描、Git、外发或发布。全文自读与来源字节复核后停止改动，等待非作者审查；结论仍为 NO-CANDIDATE / NOT CLAY。
