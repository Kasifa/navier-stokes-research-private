# 第一球谐矩的完整演化与滤波应变

2026-09-08，北京时间。PRIVATE_CORE。TP，接续TD的解析小节。范围内的恒等式、估计及光滑例已在文内证明；任意初值正则性、新颖性及新的临界先验界均未建立。PROVED IN STATED SCOPE / STANDARD IDENTITIES / OPEN / NOT CLAY。

## 1. 要核查的量

沿用TD第1节的原NS、固定 \(2\pi\) 周期胞、\(\nu>0\)、闭光滑时间区间及局部提升。记 \(a=\omega(x),b=\omega(x+r)\)，\(r=\rho n\)，\(n\in\mathbb S^2\)，
\[
 W=a\times b,\quad \Theta=W\cdot r,\quad
 m(x,\rho)=\langle n\Theta(x,\rho n)\rangle_{\mathbb S^2},
 \qquad \Pi_1\Theta=3n\cdot m.
 \tag{TP.1}
\]
球面平均除以 \(4\pi\)。固定 \(0<R<R_0<\min(1,\pi/4)\)，采用TD非负径向截断 \(\chi(\rho/R)\)，对 \(0<s<1\) 置
\[
 w(\rho)=\chi(\rho/R)\rho^{-3-2s},\quad
 \mathcal A_1=12\pi\int_{\mathbb T^3}\int_0^{2R}w|m|^2\,d\rho\,dx,\quad
 \mathcal D_1=12\pi\int w|\nabla_xm|^2 .
 \tag{TP.2}
\]
它们是TD的 \(\mathcal A^{(1)}_{s,R}\) 及其共同平移耗散，\(12\pi\) 来自 \(\int_{\mathbb S^2}|3n\cdot m|^2dS=12\pi|m|^2\)。不是改变周期胞归一化。本文所有空间积分仍不除以胞体积。

## 2. 完整矩方程、空间零模及加权能量

使用TD.2的 \(R_A,V_{\rm trap}\)，令
\[
 b_r=(u(x+\rho n)-u(x))\cdot n,\quad
 v_T=u(x+\rho n)-u(x)-b_r n,\quad
 C=\sum_j\partial_j a\times\partial_j b.
\]
这里 \(b_r\) 是径向相对速度，不是涡量 \(b\)。在固定 \(x,\rho\) 上定义
\[
 F=\langle n b_r\Theta\rangle,\quad
 T=\langle v_T\Theta\rangle,\quad
 G=\langle n\{\rho n\cdot R_A+W\cdot V_{\rm trap}\}\rangle,\quad
 C_1=\langle n\,\rho n\cdot C\rangle .
 \tag{TP.3}
\]
因 \(\operatorname{div}_r\delta u=0\)，
\(\rho^{-2}\partial_\rho(\rho^2b_r)+\rho^{-1}\operatorname{div}_{\mathbb S^2}v_T=0\)。
把TD.6中的相对输运写成散度，再使用
\[
 \langle n\,\operatorname{div}_{\mathbb S^2}(v_T\Theta)\rangle=-T,
 \qquad \nabla_{\mathbb S^2}n_i=e_i-n_i n,
\]
得到
\[
 \boxed{(\partial_t+u(x)\cdot\nabla_x-\nu\Delta_x)m
       +\rho^{-2}\partial_\rho(\rho^2F)-\rho^{-1}T
       =G-2\nu C_1.}
 \tag{TP.4}
\]
径向通量与切向矩都保留下来；只将整个输运算子同 \(\Pi_1\) 交换会漏掉它们。

有一个未投影量不具备的零模恒等式：
\[
 \int_{\mathbb T^3}m(x,\rho)\,dx=0,\qquad \mathcal D_1\ge\mathcal A_1.
 \tag{TP.5}
\]
证明是 \(\Theta(x,r)=\Theta(x+r,-r)\)，故空间平均关于 \(r\) 为偶函数，乘 \(n\) 后球面平均为零；再用固定 \(2\pi\) 胞的Poincaré不等式。这里确实核实了所需零均值。

定义完整投影黏性组合
\[
 \mathcal H_1=\mathcal D_1+24\pi\int w\,m\cdot C_1.
 \tag{TP.6}
\]
将TP.4乘 \(12\pi wm\)，在周期 \(x\) 和径向分部积分，得
\[
 \boxed{\begin{aligned}
 \tfrac12\mathcal A_1'+\nu\mathcal H_1
 =12\pi\int\big\{&
 w m\cdot G+wF\cdot\partial_\rho m\\
 &+(w'-2w/\rho)m\cdot F+(w/\rho)m\cdot T\big\}\,dx\,d\rho .
 \end{aligned}}
 \tag{TP.7}
\]
其中
\(w'-2w/\rho=R^{-1}\chi'(\rho/R)\rho^{-3-2s}-(5+2s)\chi(\rho/R)\rho^{-4-2s}\)，
没有除以可能为零的 \(\chi\)，也没有省略外截断导数。固定 \(R\) 是假设。

光滑Taylor展开结合球面奇偶性给
\[
 m=O(\rho^3),\quad \partial_\rho m=O(\rho^2),\quad
 F,T=O(\rho^4),\quad G,C_1=O(\rho^3).
\]
梯形余项对 \(G\) 的贡献单独为 \(O(\rho^5)\)。例如 \(F\) 的形式首项为 \(\rho^3\) 乘奇函数，其球平均为零。内端边界 \(wm\cdot F=O(\rho^{4-2s})\) 消失，体积分近零至多为 \(O(\rho^{3-2s})\)，故 \(0<s<1\) 时上述操作合法。各常数取于闭光滑时间区间，未延伸为候选奇点前的一致控制。TP.4–7没有封闭层级；\(F,T,G,C_1\) 仍含完整角向信息和原解导数，也没有产生径向耗散。

## 3. 球面矩究竟选择了什么应变

对周期函数定义局部平均
\[
 M_\rho f(x)=\langle f(x+\rho n)\rangle_{\mathbb S^2},\quad
 B_\rho f(x)=\frac{3}{4\pi\rho^3}\int_{|r|<\rho}f(x+r)\,dr,\quad
 J_\rho=B_\rho-M_\rho .
 \tag{TP.8}
\]
对非零Fourier模 \(k\)，令 \(z=\rho|k|\)、\(e=k/|k|\)。从
\(\langle e^{iz e\cdot n}\rangle=\sin z/z=j_0(z)\) 对向量 \(ze\) 两次求导，得到
\[
 \langle n_i n_j e^{i\rho k\cdot n}\rangle
       =\frac{j_1(z)}z\delta_{ij}-j_2(z)e_i e_j.
 \tag{TP.9}
\]
零模取 \(\delta_{ij}/3\)。这里
\[
 j_1(z)=\frac{\sin z}{z^2}-\frac{\cos z}{z},\qquad
 j_2(z)=\left(\frac3{z^3}-\frac1z\right)\sin z-\frac3{z^2}\cos z
       =\frac{3j_1(z)}z-j_0(z).
\]
这些标准公式与[NIST DLMF 10.49.3](https://dlmf.nist.gov/10.49#E3)、[10.51.1](https://dlmf.nist.gov/10.51#E1)一致。因此 \(M_\rho,B_\rho,J_\rho\) 的乘子分别为 \(j_0(z),3j_1(z)/z,j_2(z)\)，并有 \(J_\rho1=0\)。

令 \(A_\rho=J_\rho A,\ S_\rho=J_\rho S\)。TP.9与 \(\widehat\omega(k)=ik\times\widehat u(k)\) 给出完整向量身份
\[
 \boxed{m=\frac\rho3\omega\times B_\rho\omega-\rho A_\rho^\top\omega
       =-\rho S_\rho\omega+
                  \frac\rho6\omega\times(3M_\rho\omega-B_\rho\omega).}
 \tag{TP.10}
\]
说明第二项的指标：\(e\cdot(\omega(x)\times\widehat\omega(k))
=i|k|\omega(x)\cdot\widehat u(k)\)，因此TP.9的纵向项正是
\(-\rho(A_\rho^\top\omega)_i\)。局部因子 \(\omega(x)\) 留在乘子外，不把它错误地当作平移不变输入。第二个等号用
\(\Omega v=\frac12\omega\times v\)，其中 \(A=S+\Omega\)。

与 \(\omega\) 收缩后叉积项为零。若
\(q_\rho=\omega\cdot S_\rho\omega\)，TD.20于是等价于
\[
 \omega\cdot m=-\rho q_\rho,\qquad
 \mathcal V_{\rm near}
       =3\int_0^{2R}\frac{\chi(\rho/R)}{\rho}
                         \int_{\mathbb T^3}q_\rho\,dx\,d\rho .
 \tag{TP.11}
\]
这与已有R0.70B §8.1式(8.7)的 \(j_2\) 环带符号直接相接，不是新的滤波应变来源。R0.70B在那里用的是全空间Fourier表示；本文的等式由周期Fourier模重新证明，没有把其全空间其他定理搬成周期定理。

进一步，由球体平均的定义直接微分可得
\(J_\rho=-(\rho/3)\partial_\rho B_\rho\)。因此
\[
 \mathcal V_{\rm near}
 =\mathcal V+\int_0^{2R}\frac{\chi'(\rho/R)}R
                  \int\omega\cdot B_\rho S\,\omega\,dx\,d\rho .
 \tag{TP.12}
\]
内端 \(B_\rho S\to S\)，外端 \(\chi=0\)，两个端点都已计入。剩余项对应TD的完整周期余核，而不是可以抛弃的外部误差：\(-\chi'/R\) 的质量为1且支集在 \([R,2R]\)，
\(\|B_\rho S\|_\infty\le C\rho^{-3/2}\|S\|_2\le C\rho^{-3/2}Y^{1/2}\)，
再得 \(|\mathcal V_{\rm rem}|\le CR^{-3/2}Y^{3/2}\)。这也从平均算子给出TD余核界的第二个证明。

## 4. 配对量的原NS动力学及一项实际估计

记 \(L=\partial_t+u\cdot\nabla-\nu\Delta\)，并定义
\[
 N=S^2+\Omega^2+\nabla^2p,\qquad
 C_\rho=[u\cdot\nabla,J_\rho]S .
\]
原NS的梯度方程给 \(LA=-A^2-\nabla^2p\)，所以 \(LS=-N\)。固定 \(\rho\) 后 \(J_\rho\) 与普通导数可交换，故
\[
 LS_\rho=-J_\rho N+C_\rho .
 \tag{TP.13}
\]
压力项并未因先前的涡量表述而消失。用 \(L\omega=S\omega\) 对三因子乘积求导，得到
\[
 \boxed{\begin{aligned}
 Lq_\rho={}&2(S\omega)\cdot S_\rho\omega
       -\omega\cdot J_\rho N\,\omega+\omega\cdot C_\rho\omega\\
 &-2\nu\sum_j\{\partial_j\omega\cdot S_\rho\partial_j\omega
              +2\partial_j\omega\cdot(\partial_jS_\rho)\omega\}.
 \end{aligned}}
 \tag{TP.14}
\]
周期积分后左端成为 \(\partial_t\int q_\rho\)。这些梯度交叉项、压力与交换子均没有已证的有利符号。R0.70L §3已有一般滤波应变的完整演化；本节是在明确的零质量滤波器及原速度输运下直接推导，并非发现滤波应变必须含压力。

零质量的准确限制是：\(J_\rho\) 不是正归一化平均，不能继承其Jensen或协方差正性。若 \(J_\rho f=\int f(x+r)d\kappa_\rho(r)\)，则
\[
 J_\rho(u\otimes u)
 =u\otimes J_\rho u+J_\rho u\otimes u
       +\int\delta_ru\otimes\delta_ru\,d\kappa_\rho .
 \tag{TP.15}
\]
不能偷用质量1的增量表达式。不过，定义完整残差后，纯代数滤波NS方程仍成立；零质量不意味着所有这类方程失效。

先实际估计压力项，检验是否已经超出普通控制。\(B_\rho,M_\rho\) 各是 \(L^p\) 压缩，故 \(\|J_\rho\|_{p\to p}\le2\)。利用
\(-\Delta p=\operatorname{tr}(A^2)\)、周期Calderón–Zygmund、Sobolev和插值，
\[
 \|J_\rho\nabla^2p\|_{3/2}\le C\|A\|_3^2
       \le C\|A\|_2\|A\|_6\le C\sqrt{YZ},
 \qquad
 \left|\int\omega\cdot J_\rho\nabla^2p\,\omega\right|
       \le C Y^{1/2}Z^{3/2}.
 \tag{TP.16}
\]
常数对允许的 \(\rho\) 一致。这里 \(Y=\|\omega\|_2^2,Z=\|\nabla\omega\|_2^2\)，并用了 \(\|\omega\|_6^2\le CZ\)。基本Leray耗散控制的是 \(\int Y\,dt\)，不控制TP.16右端的时间积分。这个不足不是该项在真实NS中必然发散的证明。

交换子也有直接但未闭合的上界：
\[
 C_\rho(x)=\int[u(x)-u(x+r)]\cdot\nabla S(x+r)\,d\kappa_\rho(r),
 \qquad
 \|C_\rho\|_p\le2\rho\|\nabla u\|_\infty\|\nabla S\|_p
 \quad(1\le p\le\infty).
 \tag{TP.17}
\]
其证明只用 \(\operatorname{supp}\kappa_\rho\subset\overline B_\rho\)、总变差2及Minkowski。半径因子仍伴随未控制的高阶范数，没有带来新的临界时间控制。

## 5. 第一球谐量也不具有普遍的黏性单调性

TD.15的两模剪切是一个必要的对照。在复涡量记号
\(\omega_1+i\omega_2=\alpha e^{iz}+\beta e^{-2iz}\) 下，令
\[
 f(\zeta)=\frac12\int_{-1}^1\mu^2\cos(\zeta\mu)\,d\mu
       =\frac{j_1(\zeta)}{\zeta}-j_2(\zeta)
       =\frac13-\frac{\zeta^2}{10}+O(\zeta^4).
\]
球面对称性使 \(m_1=m_2=0\)，而
\[
 m_3=\rho\alpha\beta[f(\rho)-f(2\rho)]\sin3z,\qquad
 \mathcal A_1(t)=e^{-10\nu t}\mathcal A_1(0).
 \tag{TP.18}
\]
所以TD.15的未投影增长在这个投影中确实被去掉了；这不蕴含一般单调性。

现在取另一个、且仅取这一个检验该一般性声明的光滑NS例：
\[
 u(t,z)=\left(-\sum_{k=1}^3\frac{c_k(t)}k\cos kz,\
             -\sum_{k=1}^3\frac{c_k(t)}k\sin kz,\ 0\right),\quad p=0,
\]
\[
 c_1=e^{-\nu t},\qquad c_2=5e^{-4\nu t},\qquad
 c_3=-\tfrac12e^{-9\nu t}.
 \tag{TP.19}
\]
它无散、均值为零，且 \(u_3=0,\ u=u(z)\)，所以 \(u\cdot\nabla u=0\)、
\(\partial_tu=\nu\Delta u\)：这是无外力原NS的全局光滑解。记
\(v(z)=\omega_1+i\omega_2=\sum c_ke^{ikz}\)。由球面平均，
\[
 m_3=\rho\operatorname{Im}\{\overline v\,f(\rho|D_z|)v\}
   =-\frac{\rho^3}{10}\{q_1(t)\sin z+q_2(t)\sin2z\}+O(\rho^5),
\]
\[
 q_1=15e^{-5\nu t}-\tfrac{25}2e^{-13\nu t},
 \qquad q_2=-4e^{-10\nu t}.
 \tag{TP.20}
\]
余项及其时间导数在 \(t=0\) 的邻域对 \(\rho\) 一致，原因是有限个解析三角函数。于是
\[
 q_1(0)=\tfrac52,\quad q_1'(0)=\tfrac{175}2\nu,\quad
 q_2(0)=-4,\quad q_2'(0)=40\nu,
\]
\[
 \boxed{\left.\partial_t\langle m_3^2\rangle_z\right|_{t=0}
       =\frac{\rho^6}{100}\{q_1q_1'+q_2q_2'\}_{t=0}
                  +O(\nu\rho^8)
       =\frac{47}{80}\nu\rho^6+O(\nu\rho^8)>0}
 \tag{TP.21}
\]
当 \(\rho\) 充分小时成立；\(\langle\cdot\rangle_z\) 除以 \(2\pi\)。
这里正号来自同一个输出频率内不同输入对的不同热衰减率，而非外力或数值舍入。

令 \(I_{s,\chi}=\int_0^2\chi(\eta)\eta^{3-2s}d\eta>0\)。对任意固定
\(0<s<1\) 及所述截断，
\[
 \mathcal A_1'(0)
 =12\pi(2\pi)^3\nu
       \left\{\tfrac{47}{80}I_{s,\chi}R^{4-2s}
                         +O(R^{6-2s})\right\}>0
 \tag{TP.22}
\]
当 \(R\) 充分小且仍在局部坐标范围内。Taylor正主项严格支配余项，故无需数值选定半径。

该剪切中 \(\delta u\cdot\nabla_r\Theta=0,\ R_A=0,\ W\cdot V_{\rm trap}=0\)，所以TP.4的输运通量组合为零，并有
\(\mathcal A_1'=-2\nu\mathcal H_1\)。因此TP.22严格否定 \(\mathcal H_1\ge0\) 的普遍声明，即使TP.5的零模已经消失。它仍是全局光滑、总伸长恒零的例子，不能被写成NS爆破或全部几何方法的反例。

## 6. 本节完成了什么，下一步不再重复什么

TD–TP完成了这个两点对象的点态恒等式、加权演化、实际伸长配对、投影方程、滤波等价和两个有限单调性检验。TP.16–17则明确算出了普通压力与交换子上界，并没有建立基本能量之外的先验控制。

这两个相邻计算回合没有闭合新的正则性步骤。策略上停止“整体平方量单调”“第一球谐平方量单调”这两个已被否定的分支；不再默认追加角向投影、换权重或再做剪切扫描来扩充版本。第一球谐的有效配对已经回到既有 \(j_2\) 滤波应变，下一项若继续这一路线，必须针对TP.14的真实联合源提出不同的动力学机制，不能把已有滤波身份重新命名为进展。否则先做有限路线重评，选择另一项明确的原NS结构计算。

这不是禁止探索未证的困难估计。所要求的是写明一个非循环的目标及实际第一步，区分探索、范围内证明和完整Clay结论。当前没有这样的新联合源控制，也没有由上述反例证明它不可能。一般光滑初值的正则性与奇异性排除继续保持OPEN。

本节不宣称文献新颖性。实际使用TD完整稿、R0.70B §8.1–8.3的相关表示及R0.70L §3；外部仅核DLMF所列球Bessel公式和递推，普通周期椭圆/Sobolev接口为明确的标准理论。推导、构造与分项复核由AI任务完成，实际文件审读范围记于audit，不是人类同行评审。没有PDE仿真、数值证书或科学附图。冻结与一次性交接状态以研究release和dispatch记录为准，不以本文证明完成推断网站发布。
