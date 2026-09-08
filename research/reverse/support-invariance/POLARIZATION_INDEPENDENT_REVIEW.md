# 同轴极化独立稿：非作者逐式审查

2026-09-08。PRIVATE_CORE。**PASS，限于所锁合同和下述最终字节；没有待修意见。NO-CANDIDATE / NOT CLAY。**

被审稿为 POLARIZATION_INDEPENDENT.md，SHA-256：
\(\texttt{21758a8ad18606f8cea2158a7a1cda3ab62976da530d1a395ab7fd8e618ce57e}\)。
本次先全文读 POLARIZATION_CONTRACT.md，再首次全文读被审停改稿，直接复读其唯一旧数学输入 SAL 的指定段。没有读取根 POLARIZATION_PROOF.md 或其 REVIEW，也不使用它们的结论补全本稿。

我不是被审极化稿作者；我是本目录纯支撑 INDEPENDENT.md 及旧 SOURCE_BRIDGE_INDEPENDENT.md 的作者，也参与过此前多阶段审查。本次属于有明确历史关联的非作者审查，不是第三路独立形成的极化证明，不称全课题盲审。合同和被审稿已经披露根在合同前手工观察过相关结构；被审稿另披露作者此前的 Miller 预检和定位 SAL 时接触过少量纯支撑调用片段。本次不把两个作者的证明或这些历史经历称为课题互盲。

## PIR.1 逐项结论

| 检验对象 | 结论 |
|---|---|
| PI.1–6：完整两个有序项、Leray、线外测试及符号 | PASS |
| PI.7–11：任意固定非零实轴和任意全秩整数子群中的非退化对 | PASS |
| 零极化空间、零三重积及方向平方差退化分支 | PASS，保留原有限量词 |
| PI.12–15：同一有限初值、真实解初始导数、严格小量及存在性短窗 | PASS |
| 自由逐模标量空间与特定壳、附加对称、特殊轨道的区别 | PASS |
| 实际阅读、旧来源适用性及无计算边界 | PASS |

## PIR.2 两个有序来源与线外方向

沿用被审稿全部记号，特别
\[
 n=(p+q)\times\sigma,\quad
 D=\sigma\cdot(p\times q),\quad
 P=|p|^2,\ Q=|q|^2,\ C=p\cdot q,\quad
 a=\sigma\cdot p,\ b=\sigma\cdot q.
\]
直接核定
\[
 n\cdot p=D,\qquad n\cdot q=-D,
\]
所以
\[
 n\cdot U_p=-\frac{aD}{P},\qquad
 n\cdot U_q=\frac{bD}{Q}.
\]
该符号依赖被审稿明确采用 \(n=k\times\sigma\)；没有把它换成 \(\sigma\times k\)。

SAL 的 Fourier 规范为 \(e^{ik\cdot x}\)，其负号约定是
\(B(f,g)=-\mathbb P[(f\cdot\nabla)g]\)。在 \(p,q\) 的输入系数为 \(c_pU_p,c_qU_q\) 时，两个有序项之和确为
\[
 -i c_pc_q P_k\bigl[
    (b-aC/P)U_q+(a-bC/Q)U_p
 \bigr].
 \tag{PIR.1}
\]
没有额外系数二或二分之一，也没有把两个有序项当成相等。

因 \(n\perp k\)，有 \(n\cdot P_kW=n\cdot W\)。逐项测试 PIR.1 得
\[
 \begin{aligned}
 n\cdot W
 &=D\left(\frac{b^2}{Q}-\frac{abC}{PQ}
                 -\frac{a^2}{P}+\frac{abC}{PQ}\right)\\
 &=D\left(\frac{b^2}{Q}-\frac{a^2}{P}\right).
 \end{aligned}
 \tag{PIR.2}
\]
因此 PI.5–6 的号、分母及混合项抵消均准确。\(n\) 未归一化，稿内也没有漏记一个应有的 \(|n|\) 因子。由于 \(n\perp\sigma,k\)，它消灭整个复线 \(E_k=\mathbb C P_k\sigma\)。当 PI.6 的复标量非零时，完整 Leray 输出确实不在 \(E_k\)，不是仅未投影对流项的检测。

该论证使用每模投影 \(P_k\sigma\) 的实际长度。把它换为单位极化会改变标量系数；被审稿没有进行这种未披露的换元。任意非零复 \(c_p,c_q\) 的乘积都非零，不需要固定实幅度、相位或随机化。

## PIR.3 任意全秩格中的存在性和退化处理

PI.7 的第一步成立。全秩保证存在 \(r\in L\) 满足 \(\sigma\cdot r\ne0\)。若这个 \(r\) 平行 \(\sigma\)，再取 \(v\in L\setminus\operatorname{span}\sigma\)，则 \(r+jv\) 对所有非零整数 \(j\) 都不平行 \(\sigma\)。其轴向点积是常数项非零的至多一次式，至多再排除一个整数。因此可得
\[
 p\in L,\qquad a\ne0,\qquad \sigma\times p\ne0.
\]
这一步不要求 \(\sigma\) 有理，也不要求其方向本身含非零整数向量。

线性泛函
\(q\mapsto(\sigma\times p)\cdot q=\sigma\cdot(p\times q)\)
非零。若它在 \(L\) 上恒为零，便在 \(L\) 的全实张成上为零，矛盾。这准确给出 PI.8 的 \(q_0\)。

对 \(q_h=q_0+hp\)，三重积恒为 \(D_0\ne0\)。所以各 \(q_h\) 非零、不与 \(p\) 共线，也不平行 \(\sigma\)。若 \(p+q_h\parallel\sigma\)，则
\(\sigma\cdot[p\times q_h]=0\)，又矛盾。因此输出 \(k=p+q_h\) 非零且 \(k\times\sigma\ne0\)。所有输入极化、输出极化和测试方向均非零。

手工展开需避免的方向平方差分子：
\[
 \begin{aligned}
 P(b_0+ha)^2-a^2(Q_0+2hC_0+h^2P)
 &=P b_0^2-a^2Q_0\\
 &\quad+2h(Pab_0-a^2C_0).
 \end{aligned}
 \tag{PIR.3}
\]
这与 PI.9 一致。若该多项式恒为零，因 \(a\ne0\)，一次系数给
\(b_0=aC_0/P\)。常数项变为
\[
 \frac{a^2}{P}(C_0^2-PQ_0)=0.
 \tag{PIR.4}
\]
\(P>0\)，故实 Cauchy–Schwarz 取等，迫使 \(q_0\parallel p\)，与 \(D_0\ne0\) 冲突。这里无除以可能为零的 \(b_0\)、\(C_0\) 或一次系数；因此它们为零的分支也已覆盖。剩下的多项式可能是非零常数，或是恰有一个实根的一次式。两种情况都能避开有限个整数，不需要实际整数值、枚举或扫描。

最终分母 \(P|q_h|^2\) 严格正，PI.11 的方向平方差非零。全证明只用 \(L\) 的加法子群性质和全实秩，没有把 \(L\) 偷换为 \(\mathbb Z^3\) 或饱和子格。

对未使用的退化支，被审稿处理准确：

- \(p\parallel\sigma\) 或 \(q\parallel\sigma\) 时，实际允许极化为零，不能补一个新方向；
- \(k\parallel\sigma\) 时，输出允许空间为零且 \(n=0\)，当前线外测试失效；稿内没有据此认定输出也为零；
- \(D=0\) 或方向平方差为零时，只说明这个标量检测没有给出非零证据，没有推出整个空间不变。

作者是在每个固定 \(\sigma,L\) 内证明存在另一对避开这些退化支，并未将每一对频率都宣称为见证。

## PIR.4 共轭初值、真实 NS 与严格余项

PI.12 中 \(U_{-p}=U_p\)、\(U_{-q}=U_q\) 都为实向量，负模系数恰是正模的共轭。所有其它模取零，包括任何 \(E_\ell=\{0\}\) 的退化模，均符合合同。初值无散、零均值、光滑且非零，没有另行修改每模允许方向。

因 \(p,q\) 不共线，从 \(\{\pm p,\pm q\}\) 中加出 \(p+q\) 的有序对恰为 \((p,q),(q,p)\)。目标频率也不属于初始四点。因此 PI.13 精确保留完整初始卷积；其他共轭对或自作用不会与此系数碰撞。固定黏性项在该频率的初始值为零，原因是 \(\widehat A(k)=0\)，并非删去正黏性。压力由完整 \(P_k\) 保留。

本次直接核读 SAL §§1–2、§4：其固定对象包含一般固定 \(\nu>0\) 和光滑实值无散初值；式(7)–(8)保留所有卷积和热传播。§4 的 Wiener 收缩在整个 Fourier 空间进行，高阶权重估计把同窗空间正则性传至极限，方程再给初始端点的时间正则，唯一性由收缩及重叠短段获得。这里的有限 Fourier 初值 \(A\) 具有有限非零的所需 Wiener 范数，满足该入口，不需要旧三对数据、未知全窗范数或未来纯支撑接纳。

于是 \(f(t):=n\cdot\widehat u(k,t)\) 属于初始端点右侧的 \(C^1\) 类，\(f(0)=0\)，且由 PI.13 和 PIR.2 得
\[
 f'(0+)=d=-i c_pc_qD(b^2/Q-a^2/P)\ne0.
\]
为核清被审稿 PI.14 的小量，现有时间正则性直接给
\[
 f(t)-td=\int_0^t[f'(s)-f'(0+)]\,ds,\qquad
 \frac{|f(t)-td|}{t}
 \le\sup_{0\le s\le t}|f'(s)-f'(0+)|
 \longrightarrow0.
 \tag{PIR.5}
\]
这是展开被审稿已调用的同解时间正则性，不借用另一份极化证明补缺口。它保证 PI.15 的数据依赖存在性短窗，可以缩在已付局部存在窗内。因 \(n\) 为固定线性测试，非零复值 \(f(t)\) 确认 \(\widehat u(k,t)\notin E_k\)。

该余项属于同一个完整 NS 解，包含随后所有模式、压力和反馈，没有有限系统替代。没有显式数值时间、统一于 \(\sigma,L\) 或幅度的窗口，也没有由本稿推出最大时间或长期行为。

## PIR.5 结论量词与范围

通过的是：对每个事先固定的非零实 \(\sigma\)、全秩整数加法子群 \(L\) 和 \(\nu>0\)，存在稿中符号有限初值，使同一 NS 解在某个整个正短窗内离开该全子群自由标量极化空间。输出 \(k\) 仍在 \(L\)，失效来自极化线外方向。

这不等于每个初值或每一对允许频率都泄漏，也不等于任何更窄壳集合、标量相干关系或附加对称子空间不变性失败。尤其不能把该见证放入 Miller 的指定壳和附加约束而不再核资格。保有低维平移不变性的有限见证也不构成新三维奇性初值。低秩分类、其它极化丛、孤立特殊解、近似闭合、第二代供给和奇性均未被接纳。

## PIR.6 实际来源及字节绑定

以下路径相对于 /Users/kasifa/Documents/Math/navier-stokes-reverse/。本次所有数学检查均为手工符号核验，仅用文本与哈希工具，没有科学程序、数组求值、实际选参、Git、外部消息或发布。

| 来源 | 本次实际阅读范围 | SHA-256 |
|---|---|---|
| research/reverse/support-invariance/POLARIZATION_CONTRACT.md | 全文；先锁合同及预检披露 | de3df9e8df78d42f619996c411425b6ce6c66bedaf1a8285bbfc4e29076d7483 |
| research/reverse/support-invariance/POLARIZATION_INDEPENDENT.md | 全文，PI.1–15 逐式；作者声明停改后的当前字节 | 21758a8ad18606f8cea2158a7a1cda3ab62976da530d1a395ab7fd8e618ce57e |
| research/reverse/reconnection-preflight/SOURCE_ATTRIBUTION_LEMMA.md | 第1–114行（§§1–2）及第173–225行（§4） | d22bcca237977647b54ebbe13288c63a24a7c610a52a7c2265f4e3cfe366607a |

本次没有新读外部原文；Miller 只作为合同和被审稿已披露的适用性边界，不作为额外定理输入。自身此前的纯支撑稿和 SBI 稿只在身份历史中披露，没有用其结论替代本极化稿的逐式证明。

结论为 **PASS：被审独立稿在当前合同内自行闭合，无需修订。** 本审查不代替根的最终比较、字节冻结或其它合同的接纳。
