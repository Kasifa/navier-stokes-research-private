# 全秩子群上的同轴投影极化不闭合

2026-09-08。PRIVATE_CORE。根推导，未读本项独立稿；服从 POLARIZATION_CONTRACT.md。

**对每个固定非零实向量 \(\sigma\) 和每个全秩整数加法子群 \(L\)，允许所有标量系数的 \(\widehat u_k\in\mathbb C P_k\sigma\) 空间都不是完整 NS 的不变空间。** 下证一个符号两对频率见证，连接到同一个真实解；不选实际整数数据，不判断特定壳集合或附加对称约束。

## 1. 一对输入的完整线外分量

符号、Leray 和固定 \(2\pi\) 环面按 PROOF.md §1；\(\nu>0\) 始终固定。定义 \(U_j=P_j\sigma\)（\(j\ne0\)），\(E_j=\mathbb C U_j\)。\(j\parallel\sigma\) 时 \(E_j=\{0\}\)。设 \(p,q\in L\) 满足
\[
 \Theta:=\det(p,q,\sigma)\ne0,
 \qquad R(p):=\frac{(\sigma\cdot p)^2}{|p|^2}
 \ne R(q).                                                \tag{P1}
\]
于是 \(p,q,k=p+q\) 均非零，\(p,q\) 不共线，\(k\not\parallel\sigma\)，且
\(z=k\times\sigma\ne0\)。特别 \(z\perp k,\sigma,U_k\)。取
\[
 a(x)=2U_p\cos(p\cdot x)+2U_q\cos(q\cdot x).               \tag{P2}
\]
它是本合同允许空间中的实值无散光滑初值；\(U_{-j}=U_j\)，全部共轭频率保留。\(\Theta\ne0\) 排除了输入投影退化。

简记 \(P=|p|^2,Q=|q|^2,h=p\cdot q,\alpha=\sigma\cdot p,\beta=\sigma\cdot q\)。在 \(k\) 上只有 \((p,q),(q,p)\) 两个有序种子对贡献，按完整 NS 得
\[
 \widehat{B(a,a)}_k=-iP_k
 \left[\left(\beta-\frac{\alpha h}{P}\right)
        \left(\sigma-\frac\beta Qq\right)
       +\left(\alpha-\frac{\beta h}{Q}\right)
        \left(\sigma-\frac\alpha Pp\right)\right].         \tag{P3}
\]
因 \(p\cdot z=\Theta\)、\(q\cdot z=-\Theta\)，且 \(z\cdot P_kv=z\cdot v\)，两有序项给
\[
 \begin{aligned}
 z\cdot\widehat{B(a,a)}_k
 &=-i\Theta\left[
   \left(\beta-\frac{\alpha h}{P}\right)\frac\beta Q
  -\left(\alpha-\frac{\beta h}{Q}\right)\frac\alpha P\right]\\
 &=-i\Theta\left(\frac{\beta^2}{Q}-\frac{\alpha^2}{P}\right)
 =-i\Theta\,[R(q)-R(p)]\ne0.                              \tag{P4}
 \end{aligned}
\]
共同 \(\alpha\beta h/(PQ)\) 项是在两项相加后精确抵消，不是忽略回流。Leray 完整保留，测试向量只利用它的自伴性。这里只给 \(\Theta\ne0\) 分支的非闭合见证，不把 (P4) 在 \(\Theta=0\) 时的零值当作极化闭合判据；尤其不遗漏 \(E_k=\{0\}\) 的退化分支来宣称全分类。

## 2. 任意固定全秩子群都提供所需频率对

首先 \(L\) 中存在 \(p\notin\sigma^\perp\cup\mathbb R\sigma\)。否则，因 \(L\) 实张成三维，可选 \(v\in L\) 不在 \(\sigma^\perp\)，只能有 \(v\in\mathbb R\sigma\)；又可选 \(w\in L\) 不在 \(\mathbb R\sigma\)，只能有 \(w\in\sigma^\perp\)。但 \(v+w\in L\) 同时不在这两个空间，矛盾。因此可固定 \(p\) 使 \(\alpha=\sigma\cdot p\ne0\) 且 \(p\not\parallel\sigma\)。

由全秩，再固定 \(r\in L\setminus\operatorname{span}_{\mathbb R}\{p,\sigma\}\)。对任意非零整数 \(n\)，令 \(q_n=p+nr\in L\)。则
\[
 \det(p,q_n,\sigma)=n\det(p,r,\sigma)\ne0.                 \tag{P5}
\]
只须避免 \(R(q_n)=R(p)\)。设 \(b=\sigma\cdot r,D=p\cdot r,S=|r|^2\)，交叉相乘所得精确多项式为
\[
 F(n)=|p|^2(\alpha+nb)^2-\alpha^2|p+nr|^2
 =2n\alpha(Pb-\alpha D)+n^2(Pb^2-\alpha^2S).              \tag{P6}
\]
它不可能恒为零。若一次项为零，\(\alpha\ne0\) 给 \(b=\alpha D/P\)，于是二次项为
\[
 \alpha^2(D^2/P-S)<0,                                    \tag{P7}
\]
因为 \(p,r\) 不共线。非零多项式只有有限个实根，故存在一个非零整数 \(n\) 使 \(F(n)\ne0\)。固定这样一个 \(n\)，即得满足 (P1) 的 \(p,q=q_n\)。所有分母严格正；没有枚举或求具体整数，亦不要求 \(\sigma\) 为有理向量。这里的任意整数 \(n\) 是有限代数存在证明中的变量，不是换初值的无限尺度构造。

## 3. 原方程小时间桥接和严格余项

SAL（SOURCE_ATTRIBUTION_LEMMA.md）§2、§4 给 (P2) 的同一个完整无限维 NS 局部光滑解与唯一性。PROOF.md §5–6 已把该接口逐模写明；这里 \(\widehat a_k=0\)，因此
\[
 z\cdot\widehat u_k(t)=t d+\rho(t),\quad
 d=-i\Theta[R(q)-R(p)]\ne0,\quad
 |\rho(t)|/t\longrightarrow0.                            \tag{P8}
\]
理由是实际解的 \(A_1\) 连续性使每模右端连续，故
\(\rho(t)=\int_0^t[z\cdot\partial_s\widehat u_k(s)-d]ds\)。黏性初始贡献仅因这一模为零而消失；后续 \(-\nu|k|^2\widehat u_k\) 保留。\(L\) 是子群，整个实际解仍支撑于 \(L\)，但不能保持逐模极化线。

因为实际系数在 \(k^\perp\) 中，\(U_k,z\) 是其中互相正交的非零实向量，复线性张成该二维横向空间，故
\[
 \operatorname{dist}(\widehat u_k(t),E_k)
 =\frac{|z\cdot\widehat u_k(t)|}{|z|}
 \ge\frac{|\Theta|\,|R(q)-R(p)|}{2|z|}t>0                 \tag{P9}
\]
在某个依赖固定数据和 \(\nu\) 的 \(0<t<\delta\) 上成立。没有求数值 \(\delta\) 或给跨 \(\sigma,L\) 的统一常数。\(-k\) 上为共轭线外系数；所有其它输出、压力和全部原方程反馈均在真实解内。

## 4. 准确结论

对每个固定 \(\sigma\ne0\) 与全秩 \(L\)，(P2) 提供一个允许的固定初值，证明相应的整个极化空间不变性失败。它并不证明每个初值都离开该空间，也不排除其中的特殊热解、特殊非线性轨道或附加系数关联。见证本身只有两对共面输入，沿其法向平移不变；不作三维奇性构造。

这也不是对 Miller 指定壳集合、奇性、置换对称或镜像所共同定义的数据类的判决：这里的全秩加法子群和自由标量系数量词不同。若归一化 \(P_k\sigma\)，在非退化模上只是同一极化线；本论证不通过归一化掩盖退化模。低秩子群和一般极化丛未分类。

本合同筛选为 **NO-CANDIDATE**：在这个精确范围中，不能靠同轴投影的单线极化约束自动关闭完整 NS 的其它横向作用。没有对第二代真实供给、净来源优势、近似闭合、迭代、单初值无限尺度或奇性作出结论。所用两模有序 Fourier–Leray 原理和同解局部构造均已有；本轮只是这一具体全秩极化类别的独立符号检验，不声明外部新颖性。无科学程序、数组、数值证书、图件或新 PDF。
