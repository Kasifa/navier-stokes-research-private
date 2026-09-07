# 固定径向匹配线性应变剖面：独立推导草稿

PRIVATE_CORE。2026-09-07。状态：DERIVATION_DRAFT，待另一次独立审查；尚未冻结，也不标记 RESEARCH_COMPLETE。

原文去重与既有剖面排除结果的适用范围由根代理另记于 `LITERATURE_BOUNDARY.md`。本稿的能量和压力计算仅用于固定候选的残差及周期外场接口，不宣称新的自相似剖面排除定理或原创性。

本稿已逐项读取本目录 `CONTRACT.md`。只检查其中固定的剖面、固定周期外场和中心残差梯度合同；不增加候选、时间导数阶数或数值扫描。根代理随后指出一个更早的全局能量检验，本稿独立核实后将其置于压力推导之前：该固定路径已经不能满足能量恒等式，淘汰其精确解解释无需等待额外压力计算。中心压力计算仅提供对原先指定的局部残差合同的另一项有界检验。以下结论不使用任意局部浓缩或一般 Navier–Stokes 奇性的排除命题。

## 1. 切断场及单个初值

固定
\[
 S=\operatorname{diag}(1,2,-3),\quad T_*=1/100,
 \quad \tau=T_*-t,\quad\rho=\sqrt\tau,
 \quad 0\le t<T_*.
\]
采用合同给定的 \(h,\chi\)，并记
\[
 A_S(y)=-\tfrac13\chi(|y|)(y\times Sy),\qquad
 U_S=\nabla\times A_S.
\]
函数 \(h(s)=e^{-1/s}\mathbf1_{s>0}\) 在零点所有单侧导数趋零，故其延拓为 \(C^\infty\)。在 \(r\ge0\) 上，分母 \(h(2-r)+h(r-1)\) 始终为正。因此 \(\chi\) 光滑，\(r\le1\) 时为1，\(r\ge2\) 时为0。虽然 \(|y|\) 在原点不可微，\(\chi(|y|)\) 在整个内球恒为1，所以复合函数仍全域光滑。外边界处的平坦性保证场光滑地接到零。

向量恒等式给
\[
 \nabla\times(y\times Sy)
 =y\operatorname{tr}S-3Sy+(Sy\cdot\nabla)y-(y\cdot\nabla)(Sy)
 =-3Sy.
\]
故
\[
 U_S(y)=Sy\quad(|y|<1),\qquad U_S(y)=0\quad(|y|\ge2).
 \tag{1}
\]
由于 \(U_S\) 是光滑紧支撑向量势的旋度，它实值、无散，并逐分量满足
\(\int_{\mathbb R^3}U_S\,dy=0\)。最后一式由把每个旋度分量写成两个紧支撑函数的一阶导数后积分得到。

定义
\[
 u_\rho(x)=\rho^{-1}U_S(x/\rho)
\]
并在固定基本立方体 \((-\pi,\pi)^3\) 外周期延拓。其支撑半径不超过 \(2\rho\le1/5<\pi\)，所以不存在边界拼接问题。缩放保持实值和无散性；其周期积分为 \(\rho^2\int U_S=0\)。因此
\[
 u_0(x)=u_{\rm app}(0,x)=10U_S(10x)
\]
是一次固定的允许光滑初值。随后的 \(u_{\rm app}(t)=u_{\sqrt{T_*-t}}\) 仅是一条待检验的路径，尚未认定为这个初值产生的 NS 解。该初值与前一项六模初值不同，不能将两个检验说成同一条原解。

## 2. 更早的全局能量检验

本节用未归一化 Lebesgue 积分。记
\[
 J=\int_{\mathbb R^3}|U_S|^2dy>0,
 \qquad D_U=\int_{\mathbb R^3}|\nabla U_S|^2dy.
\]
这里用 \(D_U\) 区别后文的矩阵 \(D\)。\(J>0\) 来自内球中的 \(U_S=Sy\) 且 \(S\ne0\)。缩放精确给
\[
 \mathcal E(t)=\tfrac12\int_{\mathbb T^3}|u_{\rm app}|^2dx
 =\tfrac12\rho J,
 \quad \mathcal E'(t)=-\frac{J}{4\rho},
 \quad \int_{\mathbb T^3}|\nabla u_{\rm app}|^2dx=\frac{D_U}{\rho}.
 \tag{E1}
\]
固定黏性为1的无外力真解因此必须满足 \(D_U=J/4\)。

下面不引用 Poincaré 常数的外部结果。对支撑于 \([-2,2]\) 的任意光滑标量函数 \(f\)，由
\(f(x)=\int_{-2}^x f'(s)ds\) 和 Cauchy–Schwarz，
\[
 \int_{-2}^2|f(x)|^2dx
 \le\int_{-2}^2(x+2)\int_{-2}^x|f'(s)|^2ds\,dx
\]
\[
 =\int_{-2}^2\left(8-\frac{(s+2)^2}{2}\right)|f'(s)|^2ds
 \le8\int_{-2}^2|f'(s)|^2ds.
\]
由于 \(U_S\) 光滑并支撑在 \(B_2\subset[-2,2]^3\)，逐速度分量、逐坐标应用这个不等式并积分其余变量，得到对每个坐标 \(j\) 都有
\(J\le8\int|\partial_jU_S|^2\)。三个坐标相加后，
\[
 D_U\ge\frac{3J}{8}>\frac J4.
 \tag{E2}
\]
所以该路径已经不可能是精确无外力 NS 解。

更直接地，对合同中的完整残差 \(R\)，周期无散性给对流功和压力功的全域积分都为零。由 (E1)–(E2)，
\[
 \rho\int_{\mathbb T^3}R(t,x)\cdot u_{\rm app}(t,x)\,dx
 =D_U-\frac J4\ge\frac J8>0.
 \tag{E3}
\]
因此它也不满足左端趋零的归一化能量残差合同。这个结论只用了当前固定半径2的剖面、缩放和 \(\nu=1\)，不需要先完成后文的压力分类。

全局能量失败与中心条件 \(C(\tau)\to0\) 在逻辑上不同：前者本身不能说明残差在原点的哪一阶不消失。以下有限压力推导只负责额外核查原合同指定的中心条件，不能包装成否定精确路径的必需步骤。

## 3. 中心完整残差的符号

令 \(y=x/\rho\)。因为 \(d\rho/dt=-1/(2\rho)\)，
\[
 \partial_tu_{\rm app}
 =\frac1{2\rho^3}\big(U_S+(y\cdot\nabla)U_S\big),
\]
\[
 \Delta_xu_{\rm app}=\rho^{-3}\Delta_yU_S,
 \qquad
 (u_{\rm app}\cdot\nabla_x)u_{\rm app}
 =\rho^{-3}(U_S\cdot\nabla_y)U_S.
\]
在原点邻域，由 (1) 有 \(U_S=Sy\)。因此
\[
 \nabla_x\partial_tu_{\rm app}(0)=\rho^{-4}S,
 \qquad
 \nabla_x\Delta_xu_{\rm app}(0)=0,
\]
\[
 \nabla_x[(u_{\rm app}\cdot\nabla_x)u_{\rm app}](0)
 =\rho^{-4}S^2.
\]
这里速度梯度约定为 \((\nabla u)_{ij}=\partial_j u_i\)。黏性项的中心梯度为零是内球线性结构的严格结论；切断环带中的黏性没有从完整方程删掉。

对完整周期压力和合同中的 \(R,C\)，遂有精确恒等式
\[
 C(\tau)=S+S^2+\tau^2\nabla^2p_{\rm app}(0).
 \tag{2}
\]

## 4. 全空间压力与二次协变分类

暂令 \(S\) 遍历实对称无迹矩阵，保持同一个径向 \(\chi\)。令
\[
 \Phi(y)=\frac1{4\pi|y|},\qquad -\Delta\Phi=\delta_0,
\]
\[
 F_{ij,S}=U_{S,i}U_{S,j},\quad
 f_S=\partial_i\partial_j F_{ij,S},\quad
 p_S^{\mathbb R^3}=\Phi*f_S,
 \quad H_S=\nabla^2p_S^{\mathbb R^3}(0).
\]
此处及下文对重复的 \(i,j\) 求和。压力的符号是
\[
 -\Delta p_S^{\mathbb R^3}=\partial_i\partial_j(U_{S,i}U_{S,j}),
\]
与周期 NS 压力约定一致。等价写法为 \(p_S^{\mathbb R^3}=\partial_i\partial_j\Phi*F_{ij,S}\)，后者在核奇点处按分布理解。

上述 Hessian 不依赖对超奇异核作未经说明的绝对积分。可以把微分转移到紧支撑光滑源项上，写成
\[
 (H_S)_{ab}=\int_{\mathbb R^3}\Phi(-y)\,\partial_a\partial_b f_S(y)\,dy.
 \tag{3}
\]
\(\Phi\) 的局部奇性 \(|y|^{-1}\) 在三维可积，故 (3) 为有限普通积分。\(U_S\) 对 \(S\) 线性，因而 (3) 是 \(S\) 各分量的齐次二次多项式。

对任意 \(Q\in O(3)\)，叉积满足
\((Qv)\times(Qw)=\det(Q)Q(v\times w)\)。于是
\[
 A_{QSQ^T}(Qy)=\det(Q)Q A_S(y).
\]
旋度的坐标变换再给一个 \(\det(Q)\)，两因子相乘为1，故
\[
 U_{QSQ^T}(Qy)=Q U_S(y).
\]
利用 \(\Phi\) 的径向性及变量替换，压力与 Hessian 因而满足
\[
 p_{QSQ^T}^{\mathbb R^3}(Qy)=p_S^{\mathbb R^3}(y),
 \qquad H_{QSQ^T}=QH_SQ^T.
 \tag{4}
\]

下面直接分类 (4)，不调用张量表示定理。先取
\(S=\operatorname{diag}(\lambda_1,\lambda_2,\lambda_3)\)，其中 \(\lambda_1+\lambda_2+\lambda_3=0\)。任意对角变号正交矩阵都与 \(S\) 交换。由 (4)，\(H_S\) 的非对角元必须为零。

对固定的 \(i\)，其对角元 \(h_i\) 是 \(\lambda\) 的齐次二次多项式，并在交换另两个指标 \(j,k\) 时不变。故它可以写成
\[
 a\lambda_i^2+b\lambda_i(\lambda_j+\lambda_k)
 +c(\lambda_j^2+\lambda_k^2)+d\lambda_j\lambda_k.
\]
在无迹平面上，
\(\lambda_j+\lambda_k=-\lambda_i\) 及
\(2\lambda_j\lambda_k=\lambda_i^2-\lambda_j^2-\lambda_k^2\)。因此
\[
 h_i=\alpha\lambda_i^2+
 \beta(\lambda_1^2+\lambda_2^2+\lambda_3^2).
\]
置换协变性使同一对 \(\alpha,\beta\) 对三个 \(i\) 都适用。最后将任意实对称 \(S\) 正交对角化，并用 (4)，得到
\[
 H_S=\alpha_\chi S^2+
 \beta_\chi\operatorname{tr}(S^2)I.
 \tag{5}
\]
这两个有限系数已经包括整个切断环带产生的全空间压力；没有假设环带压力为零，也不需要算出其数值。

一个独立符号检查是：内球中
\(\partial_i\partial_j(U_iU_j)=\operatorname{tr}(S^2)\)，故
\(\operatorname{tr}H_S=\Delta p_S^{\mathbb R^3}(0)=-\operatorname{tr}(S^2)\)。代入 (5) 得
\[
 \alpha_\chi+3\beta_\chi=-1.
 \tag{6}
\]

## 5. 周期 Green 差的显式光滑构造

以下卷积使用 Lebesgue 测度，不使用归一化测度。记 \(V=(2\pi)^3\)，令周期 Green 分布 \(G\) 满足
\[
 -\Delta G=\delta_0-V^{-1},\qquad \int_{\mathbb T^3}G=0.
\]
为给出其与 \(\Phi\) 之差的可核查局部定义，采用热核
\[
 K_{\mathbb R}(s,z)=(4\pi s)^{-3/2}e^{-|z|^2/(4s)},
\]
\[
 K_{\mathbb T}(s,z)=\sum_{n\in\mathbb Z^3}K_{\mathbb R}(s,z+2\pi n)
 =V^{-1}\sum_{k\in\mathbb Z^3}e^{-|k|^2s}e^{ik\cdot z}.
\]
两个表示的等同性由计算周期化 Gaussian 的每个 Fourier 系数直接得到。积分
\(\int_0^\infty(K_{\mathbb T}-V^{-1})\,ds\) 的非零 Fourier 系数为 \(1/(V|k|^2)\)，所以它给出上述 \(G\)。同样，\(\int_0^\infty K_{\mathbb R}(s,z)\,ds=\Phi(z)\) 对 \(z\ne0\) 成立。

在 \(|z|\le1\) 上定义
\[
\begin{split}
 Q_G(z)={}&\int_0^1
 \left[\sum_{n\ne0}K_{\mathbb R}(s,z+2\pi n)-V^{-1}\right]ds\\
 &+\int_1^\infty
 \left[K_{\mathbb T}(s,z)-V^{-1}-K_{\mathbb R}(s,z)\right]ds.
\end{split}
 \tag{7}
\]
它在 \(z\ne0\) 时等于 \(G(z)-\Phi(z)\)，并给出原点处的光滑延拓。其有限性和逐阶光滑性可以直接从两段积分检查：

- 在短时段，对 \(n\ne0\)，有 \(|z+2\pi n|\ge(2\pi-1)|n|\)。Gaussian 的任意固定阶导数是 Gaussian 乘一个有限多项式，可用一个较慢衰减的 Gaussian 吸收该多项式；对 \(n\) 的和及对 \(0<s\le1\) 的积分于是对 \(|z|\le1\) 一致收敛。原点附近的全部奇性已由 \(n=0\) 的自由热核精确减去。
- 在长时段，周期部分的每阶导数由 \(V^{-1}\sum_{k\ne0}|k|^m e^{-|k|^2s}\) 控制，其 \(s\ge1\) 积分收敛。自由核的 \(m\) 阶导数在固定球上由 \(C_m s^{-(3+m)/2}\) 控制，同样可积。

这些一致可积界允许逐阶微分，故 (7) 在该球的一个开邻域内为 \(C^\infty\)。这里没有把未经界定的核正则性当作误差证书。

定义确定的有限常数
\[
 M_G=\sup_{|z|\le1}
 \left(\sum_{a,b,i,j=1}^3
 |\partial_a\partial_b\partial_i\partial_jQ_G(z)|^2\right)^{1/2},
 \qquad
 m_S=\int_{\mathbb R^3}|U_S(y)|^2\,dy,
\]
\[
 C_{\chi,G}=M_Gm_S<\infty.
 \tag{8}
\]
此处 \(S\) 已固定为合同中的矩阵，所以常数的记号省略了这个固定参数。式 (7)–(8) 是常数的严格定义和有限性证明；本稿没有声称已给出其数值上界。

## 6. 完整周期压力的严格余项

周期压力定义为
\[
 p_\rho=G*\partial_i\partial_j(u_{\rho,i}u_{\rho,j})
 =\partial_i\partial_jG*(u_{\rho,i}u_{\rho,j}).
\]
它均值为零，满足合同中的 Poisson 方程；非零 Fourier 系数由该方程唯一决定。全空间压力对同一紧支撑速度的缩放为
\[
 p_\rho^{\mathbb R^3}(x)=\rho^{-2}p_S^{\mathbb R^3}(x/\rho),
 \qquad \nabla^2p_\rho^{\mathbb R^3}(0)=\rho^{-4}H_S.
\]
由于 \(u_\rho\) 支撑于半径 \(1/5\) 内，在原点的一个固定邻域可直接使用 (7) 的光滑核差。两种压力 Hessian 的差精确为
\[
 (\nabla^2p_\rho(0)-\rho^{-4}H_S)_{ab}
 =\int \partial_a\partial_b\partial_i\partial_jQ_G(-z)
 u_{\rho,i}(z)u_{\rho,j}(z)\,dz.
 \tag{9}
\]
这是已经相消奇性的普通光滑核积分。用四阶张量的 Frobenius 范数，以及
\(\|v\otimes v\|_F=|v|^2\)，得到
\[
 \|\nabla^2p_\rho(0)-\rho^{-4}H_S\|_F
 \le M_G\int|u_\rho(z)|^2dz
 =M_G\rho m_S.
\]
乘上 \(\tau^2=\rho^4\) 后即为合同要求的显式余项形式
\[
 \left\|\tau^2\nabla^2p_{\rm app}(0)-H_S\right\|_F
 \le C_{\chi,G}\rho^5
 =C_{\chi,G}\tau^{5/2}.
 \tag{10}
\]
周期域并非旋转不变；(5) 仅用于全空间主项。固定周期域的所有影响由 (9)–(10) 保留，没有把周期压力直接替换成全空间压力。

## 7. 固定矩阵检测与暂定结论

对合同指定的矩阵
\[
 S=\operatorname{diag}(1,2,-3),\qquad
 D=\operatorname{diag}(5,-8,3),
\]
Frobenius 配对直接给
\[
 D:I=5-8+3=0,
 \qquad D:S^2=5-32+27=0,
 \qquad D:S=5-16-9=-20,
 \qquad \|D\|_F=\sqrt{98}.
\]
结合 (2)、(5)、(10)，令 \(E(\tau)=\tau^2\nabla^2p_{\rm app}(0)-H_S\)，则
\[
 C(\tau)=S+(1+\alpha_\chi)S^2
 +\beta_\chi\operatorname{tr}(S^2)I+E(\tau),
\]
\[
 |D:C(\tau)+20|\le\sqrt{98}\,C_{\chi,G}\tau^{5/2}.
 \tag{11}
\]
因此本推导给出
\[
 \lim_{\tau\downarrow0}D:C(\tau)=-20,
 \qquad
 \liminf_{\tau\downarrow0}\|C(\tau)\|_F
 \ge\frac{20}{\sqrt{98}}>0.
 \tag{12}
\]
若希望写成正时间区间，可在 \(C_{\chi,G}>0\) 时取
\[
 0<\tau\le\min\left\{T_*,
 \left(\frac{10}{\sqrt{98}C_{\chi,G}}\right)^{2/5}\right\},
\]
于是 \(D:C(\tau)\le-10\)。若 \(C_{\chi,G}=0\)，则 (11) 对全部合同时间都精确为 \(-20\)。无需把未计算的常数伪报为某个数值。

式 (12) 如经后续独立审查确认，便否定本固定路径的中心必要残差合同。精确 NS 路径的解释在更早的 (E1)–(E3) 已经失败；(12) 的附加内容是所定义中心尺度下的残差梯度也不能忽略。当前只是独立推导草稿，不据此提前生成正式冻结或交接。

## 8. 适用边界

本论证固定了径向 \(\chi\)、紧支撑匹配、三个不同特征值的指定线性应变内区、\(\rho=\sqrt{T_*-t}\)、\(\nu=1\)、固定环面，以及由整个候选速度唯一恢复的周期压力。

它不排除非径向切断、同阶附加背景速度及其压力、时间变化的剖面、其他内区结构、非自相似浓缩或一般 NS 奇性。一个同阶误差若能改变这里的压力 Hessian 或残差梯度，就不属于本合同允许忽略的小修正。也未证明从这个固定初值产生的真正 NS 解不能走向其他结构。

没有把局部缩放的能量范数与全域周期模板范数混用。没有删除切断环带、回流或周期压力外场；没有把通过或否定一个中心必要条件说成全域稳定性、固定初值可达性或奇性定理。
