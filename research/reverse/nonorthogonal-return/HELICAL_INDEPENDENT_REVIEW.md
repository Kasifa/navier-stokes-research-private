# 单螺旋独立证明的非作者审查

2026-09-08，PRIVATE_CORE。结论：**限定 PASS；HI.1–20 及所述子类障碍无待修数学阻断。**

本轮全文读取 HELICAL_CONTRACT、HELICAL_INDEPENDENT，并直接手推其新步骤。此前已完成共同模板的独立对称化简和共同方向门审查，因此不是对背景的盲审；我不是被审独立证明的作者。本轮未读根 HELICAL_PROOF、Pauli HELICAL_REVIEW 或其它新螺旋证明。没有用根也报告障碍作为证据，没有科学程序、数组、指数数值、参数选择、Git 或新外部定理审计。

## HIR.1. 接收与目标螺旋性的连接

被审稿 HI.2 的配对穷尽与已核共同合同一致：独立频率坐标中，第一层每项恰涉及两轴；加到 \(2p_i\) 的两项只能是 \(p_i+p_j,p_i-p_j\) 及其交换。全部接收仍是 \(F_i=\sum_{j\ne i}J_{ij}C_{ij}\)。第一、第二层的所有有序项和各边不同的热权重都保留，目标外系数未被删去。

非零 Gram 边约束 \(\varepsilon_i\varepsilon_j=1\) 与长度排除置换给出全部题定 \(O\)，其行列式是 \(\delta=\prod_i\varepsilon_i\)。正目标系数确为
\[
\rho e^{-2ip_i\cdot x_0}O U_i^{(\varepsilon_i)}.
\]
共轭种子满足 \(ip_i\times\bar U_i=-\xi_i\bar U_i\)，且 \(O^Tp_i=\varepsilon_i p_i\)。由正交叉积恒等式，
\[
ip_i\times O U_i^{(\varepsilon_i)}
=\delta\varepsilon_i O(ip_i\times U_i^{(\varepsilon_i)})
=\delta\xi_i O U_i^{(\varepsilon_i)}.
\tag{HIR.1}
\]
两个 \(\varepsilon_i\) 因子正好抵消。故目标相对原种子的螺旋性由 \(\det O\) 决定，不由每行符号单独决定；这也涵盖非正交图断开的其它相容变换。

对非零单螺旋 \(U_i\)，\(U_i\cdot U_i=0\) 而 \(M_i=U_i\cdot\bar U_i>0\)。\(U_i,\bar U_i\) 是复横向平面的两条独立直线；若 \(Z=\alpha U_i+\beta\bar U_i\)，则
\[
U_i\cdot Z=\beta M_i,\qquad \bar U_i\cdot Z=\alpha M_i.
\]
所以 HI.6 的两个方向必要条件准确，完全不除以零的双线性范数。零接收也满足这些方向条件，但违反非零模板；独立稿已单独保留这一限制。

## HIR.2. 单对代入、归一化和两个投影

沿用被审稿 \(P,Q,c,\Delta,L_\pm,R,e_p,e_q,n\)。由于 \(\Delta>0\)，有
\[
|e_p|^2=\Delta/P,\quad |e_q|^2=\Delta/Q,\quad |n|^2=\Delta,
\quad e_p\cdot n=e_q\cdot n=0.
\]
由 \(p\times e_p=n,p\times n=-Pe_p\) 解螺旋方程，得到 \(b=ia/\xi_i\)；由 \(q\times e_q=-n,q\times n=Qe_q\) 得 \(e=-id/\xi_j\)。两式符号相反，正是 HI.7。非零单螺旋强迫 \(a,d\ne0\)。其 Hermitian 范数为
\[
M_i=\frac{2\Delta}{P}|a|^2,\qquad
M_j=\frac{2\Delta}{Q}|d|^2,
\]
而 \(z_{ij}=a\Delta/P\ne0\)。这核对 HI.8 的全部归一化因子二，不把 \(U_i\cdot U_i=0\) 误作零极化。

在完整单对 NS.6 的括号中，
\[
d\bar e=i|d|^2/\xi_j,\quad \bar d e=-i|d|^2/\xi_j,
\]
故前两项合为 \(-4ic\xi_j a^2|d|^2\)，共享 \(b\) 项是 \(+4ic\xi_i a^2|d|^2\)。总和正是
\(4ic(\xi_i-\xi_j)a^2|d|^2\)。由于长度不同，\(\xi_i\pm\xi_j\ne0\)，且 \(P-Q=(\xi_i-\xi_j)(\xi_i+\xi_j)\)。因此在 \(c\ne0\) 时法向与平面系数之比为
\[
\frac{C_n}{C_e}=\frac{2i}{\xi_i+\xi_j},
\quad
C_e=\frac{4ic\Delta^3(P-Q)^2}{P^2Q^2R}a^2|d|^2.
\]
这支付 HI.9，未删除任何投影或共享项。

为独立核查 HI.11–12 的系数，先不约去边分量，直接点乘得到
\[
U_i\cdot C_{ij}
=aC_e\frac{\Delta}{P}
\left(1-\frac{2\xi_i}{\xi_i+\xi_j}\right),
\]
\[
\bar U_i\cdot C_{ij}
=\bar aC_e\frac{\Delta}{P}
\left(1+\frac{2\xi_i}{\xi_i+\xi_j}\right).
\]
前一个括号等于 \(-(P-Q)/(\xi_i+\xi_j)^2\)，后一个等于 \((3\xi_i+\xi_j)/(\xi_i+\xi_j)\)。代入 \(a=Pz_{ij}/\Delta\) 及上述两个范数恒等式，恰得到
\[
U_i\cdot C_{ij}
=-\frac{2ic(P-Q)^3M_j}{QR(\xi_i+\xi_j)^2}z_{ij}^3,
\]
\[
\bar U_i\cdot C_{ij}
=\frac{ic\Delta(P-Q)^2M_iM_j}{PQR}
\frac{3\xi_i+\xi_j}{\xi_i+\xi_j}z_{ij}.
\tag{HIR.2}
\]
立方项的负号、全部 \(P,Q,\Delta\) 因子、线性项的特殊因子均与被审稿一致。这里分别是 \(z^3\) 和 \(z\)，没有模长或共轭替代。

对 \(c=0\)，必须回到完整单对式：\(C_e=0\)，法向两项中的 \(d\bar e+\bar d e=0\)，其它项带 \(c\)，故 \(C_{ij}=0\)。于是 HIR.2 在正交边也成立；此处并未扩用仅针对 \(c\ne0\) 的单对零判据。

## HIR.3. 反定向分支和特殊长度比

固定 \(i\) 时，其余两波向量在 \(p_i^\perp\) 的实投影线性独立，否则原三个波向量也线性相关。用定向实正交横向基写
\(U_i=A_i(e_1+i\chi_i e_2)\)，\(A_i\ne0\)。映射
\[
v_1e_1+v_2e_2\longmapsto U_i\cdot v=A_i(v_1+i\chi_i v_2)
\]
是从实二维平面到 \(\mathbb C\) 的可逆实线性映射。故 \(z_{ij},z_{ik}\) 实线性独立，即使两者作为复标量当然复线性相关，也不能据此混淆实系数相消。

HIR.2 第二式乘正实 \(J_{ij}\) 后，除公共 \(i\) 与 \(z_{ij}\) 外所有系数均实。反定向必要条件因此强迫两系数各自为零。非正交边的其余因子都非零，只可能
\[
3\xi_i+\xi_j=0.
\]
这保留了单向允许的特殊长度比与相反螺旋符号。共同返回还要求同一条边的反向条件 \(3\xi_j+\xi_i=0\)，两式推出 \(8\xi_i=0\)，矛盾。至少一条非正交边足以完成此分支，不需同号螺旋或完整非正交图。

## HIR.4. 保定向分支的三倍相位

图不完整时，三顶点中至少有一行度数至多一。度零由正交边零输出得 \(F_i=0\)，违反非零模板；度一的唯一非正交项在 HIR.2 第一式中非零，违反保定向方向条件。所有零和正交分支在转入完整图之前已处理。

完整图下，HI.14 的 \(w_{ij}\) 是非零实数。单行相消要求
\[
z_{ij}^3/z_{ik}^3=-w_{ik}/w_{ij}\in\mathbb R\setminus\{0\}.
\]
两实横向投影独立，故其有向夹角不是 \(0\) 或 \(\pi\)。圆偏振点积使上述两个 \(z\) 的相位差等于该有向角乘 \(\chi_i\)，可能因角度次序改一个整体负号，均不改变下面的余弦及三倍角符号结论。立方比为非零实数强迫
\[
t_i=\cos\theta_i\in\{-1/2,1/2\},\qquad
\operatorname{sgn}(z_{ij}^3/z_{ik}^3)=-\operatorname{sgn}t_i.
\]
与右端的负号比较，得到
\(\operatorname{sgn}t_i=\operatorname{sgn}(w_{ij}w_{ik})\)。因此 HI.15–16 的符号准确，且不依赖 \(\chi_i=\pm1\)；不存在额外可逐边调整的相位。

## HIR.5. 逆 Gram 及最低频符号

归一 Gram 矩阵 \(G\) 严格正定，所有 \(|x_{ij}|<1\)。投影夹角公式 HI.17 直接由投影内积与两投影范数得到。对逆矩阵作正对角归一化，余子式给
\[
K_{12}=-t_3,\quad K_{13}=-t_2,\quad K_{23}=-t_1.
\]
所以在三个 \(|t_i|=1/2\) 时，
\[
0<\det K=1-\sum_i t_i^2-2t_1t_2t_3
=1/4-2t_1t_2t_3.
\]
乘积只能是 \(\pm1/8\)；正值会使行列式为零，故必须是 \(-1/8\)。再次对 \(K^{-1}\) 正对角归一化确实恢复 \(G\)：若 \(K=D G^{-1}D\)，则 \(K^{-1}=D^{-1}GD^{-1}\)，且 \(G\) 的对角线已为一。

第二次余子式因而给
\[
x_{jk}=\frac{t_i+t_jt_k}
{\sqrt{(1-t_j^2)(1-t_k^2)}}.
\]
使用 \(t_jt_k=-t_i/2\) 及分母 \(3/4\)，得到 \(x_{jk}=2t_i/3\)，从而
\[
x_{12}x_{13}x_{23}=-1/27,
\qquad \operatorname{sgn}x_{jk}=\operatorname{sgn}t_i.
\]
这只是相消的必要角条件强迫的代数值，不是选取一组频率或参数。

仅重排标签使 \(P_1<P_2<P_3\) 后，\(w_{12},w_{13}\) 各自的分母、范数、热权重均正；两项 \((P_1-P_j)^3\) 均负。因此
\[
\operatorname{sgn}(w_{12}w_{13})
=\operatorname{sgn}(c_{12}c_{13})
=\operatorname{sgn}(x_{12}x_{13}).
\]
最低频行的相位必要条件与逆 Gram 关系共同要求此符号等于 \(\operatorname{sgn}x_{23}\)，即三个 \(x\) 的乘积严格为正，与 \(-1/27\) 矛盾。该论证未使用高频近似、小时间展开或三行幅度相等的假定。

## HIR.6. 最终范围与实际绑定

两种行列式分支覆盖全部 Gram 相容 \(O\)。长度两两不同支付 \(P_i-P_j\) 及 \(\xi_i\pm\xi_j\) 非零；单螺旋非零性支付 \(M_i>0,z_{ij}\ne0\)；所有 \(J_{ij}\) 在正时间严格正。正交边、零接收、单通道及反定向特殊长度比均已单列，不存在依靠未处理零分母跳过分支的步骤。

接受结论严格限于：合同内单螺旋三对种子的完整纯 \(w_{22}\) 接收，无法成为指定加倍原模板；所有正时间、非零复幅度、独立螺旋符号及题定 \(O\) 均覆盖。它不排除非圆偏振极化、其它模板、近似返回或真实 NS 的一般有限再生成。没有支付 \(1+3/3+1\)、种子直接混合、目标外反馈、无限维误差、同一固定初值的无限尺度或有限总时间。**NO-CANDIDATE 仅用于这一指定纯树门，不是 NS 奇性或正则性结论。**

前两份本轮全文实读；其余依赖此前已全文实读，本轮核实际 SHA 未变。本次没有读取或绑定未读的其它螺旋稿。

| 工作树相对路径 | SHA256 |
| --- | --- |
| `research/reverse/nonorthogonal-return/HELICAL_CONTRACT.md` | `b64a3142fb6e0d261ece899e5b5f4c767d0ed89e1ae0083637b0f4acac3f2e05` |
| `research/reverse/nonorthogonal-return/HELICAL_INDEPENDENT.md` | `7125955d59a14a5c55b7c4616ea1f242b52db0c17bc7e1be30b992c0b6a304a5` |
| `research/reverse/nonorthogonal-return/JOINT_CONTRACT.md` | `cc3cd571b87cde40488345d8d8faa6ac774892701f30869ee479c3d82088e23c` |
| `research/reverse/nonorthogonal-return/SPATIAL_PROOF.md` | `50510f2b1b2bee2ed3739bd9a5a1276f16056e244f5b71192b9a39b8066190a5` |
| `research/reverse/nonorthogonal-return/SOURCE_AND_HEAT_PREFLIGHT.md` | `cd0206ef0164387d41e246485d1f4a3a0815fef42ed45163816d21ac4e6fdbe0` |
| `research/reverse/nonorthogonal-return/JOINT_SYMMETRY_REDUCTION.md` | `bd5db3d7963e38afd5b08a5c59ea35826a439f2a4b425bbfe59c2812581421b2` |
