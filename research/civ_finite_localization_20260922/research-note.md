# 固定角阈值的有限层局部能量估计

2026-09-22。PRIVATE_CORE / CONDITIONAL ESTIMATE / OPEN / NOT CLAY。实际审查状态另见同目录记录。

MP 得到的混合压力小量涉及外球耗散。本节在同一角阈值下使用有限个嵌套时空柱，检验这一外球项能否被原能量界控制。结果限于以下明确含源的不等式：在条件平均梯度界下，外球尾项及调和压力误差趋零，剩下完整的二次压力、跨模交换和输运。它不是无源衰减或一般正则性。

## 1. 固定解、阈值与有限层

沿用 MP 的固定母柱 \(\mathcal Q_0\)、同一实际无力周期解和固定轴。取足够小 \(R\)，使 \(B_{4R}\times(-4R^2,-R^2/2)\subset\mathcal Q_0\)。令
\[
\tau_R=-R^2/2,\qquad
\mathcal Q_r=B_r\times(-r^2,\tau_R),\quad R\le r\le2R.
\]
在整个外柱固定同一个 \(N\ge4\)，不逐层换阈值：
\(z=P_{\ge N}u=P_{\ge N}w,\ \ell=w-z\)。
设
\[
S=\operatorname*{ess\,sup}_{B_{2R}\times(-4R^2,\tau_R)}|\nabla v|,
\qquad
16R^2S\le\nu(N-1)^2.
\tag{FL.1}
\]
这是完整平均梯度条件，不是一般解已有的估计。

取
\[
M=\lfloor\sqrt N\rfloor,\qquad
d=\frac{R}{2M},\qquad
r_k=R+2kd,\quad k=0,\ldots,M.
\tag{FL.2}
\]
所以 \(r_M=2R\)。每一步记
\(r=r_k,\ a=r+d,\ s=r+2d=r_{k+1}\)。
径向空间截止满足 \(\chi_k=1\) 于 \(B_r\)，支于 \(B_a\)，
\[
|\nabla\chi_k|\le C/d,\qquad |\Delta\chi_k^2|\le C/d^2.
\]
取 \(0\le\vartheta_k\le1\)，在 \(t\le-a^2\) 为零、\(t\ge-r^2\) 为一，
\[
|\vartheta_k'|\le C/(a^2-r^2)\le C/(Rd).
\tag{FL.3}
\]
最终时刻以前无需让时间截止再次降为零；能量等式积分到每个实际时刻。其支撑均包含在外柱时间区间，始端项为零。

同一阈值的局部能量记为
\[
F_N(r)=\frac1R\left[
 \operatorname*{ess\,sup}_{-r^2<t<\tau_R}\int_{B_r}|z(t)|^2
 +\nu\int_{\mathcal Q_r}|\nabla z|^2\right].
\tag{FL.4}
\]
所有半径均用同一个 \(R\) 归一化。向量角谱隙与对称球上旋转投影的收缩给
\[
\int_{B_s}|z|^2\le\frac{s^2}{(N-1)^2}\int_{B_s}|\nabla z|^2,
\qquad
F_N(2R)\le R^{-1}(M_0^2+\nu D_0),
\tag{FL.5}
\]
其中 \(D_0=\int_{\mathcal Q_0}|\nabla u|^2<\infty\)。
梯度收缩使用旋转与梯度的张量协变交换及正交投影，不把圆柱分量的普通导数误当作 Cartesian 梯度。

## 2. 每一步的混合压力与截止费用

在母球 \(B_s\) 依 MP.2–6 作实际压力分解，取径向 \(\eta_s\) 在 \(B_s\) 为一、支于 \(B_{2s}\subset B_{4R}\)：
\[
Q_Np=Q_Nq_{ww,k}+q_{D,k}+Q_NH_{0,k}.
\tag{FL.6}
\]
未投影的 \(H_{0,k}\) 仍完整减去 \(q_{vv,k}\) 和全 \(q_{{\rm mix},k}\)，在整个 \(B_s\) 调和。特别是 \(q_{D,k}\) 为 MP.5 的球内零 Dirichlet 高模压力，真实压力没有被设为零边值。

从 SA.5–7 乘时间截止积分，FL.1 与加权向量角谱隙使平均应变项不超过
\(\frac14\nu\int\vartheta_k\chi_k^2|\nabla z|^2\)。
对混合压力利用 \(\nabla\chi_k^2=2\chi_k\nabla\chi_k\)：
\[
\begin{split}
\left|\int q_{D,k}z\cdot\nabla\chi_k^2\right|
&\le C\frac{s^2S}{N(N-1)d}\,
 \|z\|_{L^2(B_s)}
 \left(\int\chi_k^2|\nabla z|^2\right)^{1/2}\\
&\le\varepsilon\nu\int\chi_k^2|\nabla z|^2
 +C_\varepsilon\frac{s^6S^2}{\nu N^2(N-1)^4d^2}
  \int_{B_s}|\nabla z|^2.
\end{split}
\tag{FL.7}
\]
第一步分别使用 MP.7 的标量压力角增益和 \(\chi_k z\) 的向量角谱隙；第二步先 Young，再对外球 \(z\) 用 FL.5。
取固定小 \(\varepsilon\) 后，第一项吸收入同一截止耗散。第二项相对于外球 \(\nu\int D\) 的系数为
\[
C\frac{R^6S^2}{\nu^2N^2(N-1)^4d^2}
\le C\frac{M^2}{N^2},
\tag{FL.8}
\]
最后使用 FL.1，而不是额外假定外球临界耗散有界。

空间扩散截止误差和时间截止误差分别给
\[
\begin{split}
\nu\int |\Delta\chi_k^2||z|^2
 &\le C\frac{R^2}{d^2(N-1)^2}\,\nu\int_{B_s}|\nabla z|^2,\\
\int |\vartheta_k'|\chi_k^2|z|^2
 &\le C\frac{R}{\nu d(N-1)^2}\,\nu\int_{B_s}|\nabla z|^2.
\end{split}
\tag{FL.9}
\]
时间式对所需时间区间积分；空间式也乘 \(0\le\vartheta_k\le1\)。所有支撑都由 \(\mathcal Q_s\) 包含。相对时间系数含 \(1/\nu\)，不是 \(\nu\)。

## 3. 小间距下的真实调和余项

此处母球与截止支撑间距只有 \(d\)，不能用 HP 中固定比例的 \(R\le b/8\) 结论。直接重算球谐尾。

取 \(\rho=s-d/2\)。调和内点估计在距球面 \(d/2\) 的内球面上给
\[
\|H_{0,k}(\rho\,\cdot)\|_{L^2(S^2)}
 \le Cd^{-2}\|H_{0,k}\|_{L^{3/2}(B_s)}.
\]
若 \(x\in B_a\)，则 \(q=|x|/\rho\le(s-d)/(s-d/2)\)。利用
\[
\sum_{l\ge N}(2l+1)q^{2l}
 \le q^N\sum_{l\ge0}(2l+1)q^l
 \le Cq^N(1-q)^{-2}
\]
及球谐加法公式，得到
\[
\boxed{\|Q_NH_{0,k}\|_{L^\infty(B_a)}
 \le Cs\,d^{-3}e^{-cNd/s}\,
 \|H_{0,k}\|_{L^{3/2}(B_s)}.}
\tag{FL.10}
\]
没有调用尖锐角投影的一致 \(L^\infty\) 界。高角模只要求球谐次数至少 \(N\)，整个母球调和仍必需。

沿用 MP.10–11 的逐窗范数，窗口长度至多 \(4R^2\)：
\[
\|H_{0,k}\|_{L^{3/2}(B_s\times(-s^2,\tau_R))}
 \le P_*+C M_0 S R^{17/6}.
\]
用 \(|\nabla\chi_k^2|\le C/d\)、\(\|z\|_2\le M_0\) 和时间 Hölder，得每步共同上界
\[
\begin{split}
H_{R,N}&\ge
 R^{-1}\int_{-s^2}^{\tau_R}
 \vartheta_k\left|\int Q_NH_{0,k}z\cdot\nabla\chi_k^2\right|dt,\\
H_{R,N}&=
 C M^4 e^{-cN/M}
 \left[M_0P_*R^{-11/6}+M_0^2 R S\right]\\
&\le C N^2e^{-c\sqrt N}
 \left[M_0P_*R^{-11/6}+M_0^2 R S\right].
\end{split}
\tag{FL.11}
\]
固定 \(C,c>0\) 可调整，独立于层数与 \(R,N\)。这些只是调和余项的费用，不乘到其它压力或输运源上。

## 4. 含全部剩余源的有限递推

逐层保留实际非线性项
\[
\begin{split}
G_k=\frac1R\int_{-s^2}^{\tau_R}\vartheta_k(t)\Bigg[
&\left|\int\chi_k^2z\cdot(w\cdot\nabla)\ell\right|
 +\frac12\left|\int(u\cdot\nabla\chi_k^2)|z|^2\right|\\
&+\left|\int q_{ww,k}z\cdot\nabla\chi_k^2\right|
\Bigg]dt.
\end{split}
\tag{FL.12}
\]
内层均为空间积分。最后一项可移去 \(Q_N\)，因为 \(z\cdot\nabla\chi_k^2\) 是标量高模；不是把整个二次压力删除。实际 \(u=v+w\) 的输运、低高模配对、低低/高高压力全在这里。每个终点前紧窗光滑，故这些积分有限；本节不给它们共同的临界上界或小量。

SA 的能量等式、FL.7–11，在积分终点取上确界并估计耗散后给
\[
F_N(r_k)\le \alpha_N F_N(r_{k+1})+C G_k+C H_{R,N},
\quad
\alpha_N\le C\left(\frac{M^2}{(N-1)^2}
             +\frac{M}{\nu(N-1)^2}\right)
\le\frac{C_\nu}{N}.
\tag{FL.13}
\]
常数依赖固定截止形状与固定黏性，不依赖 \(k,R,N\)。要求 \(N\ge N_*(\nu)\)，使 \(\alpha_N\le1/2\)。给定这一个阈值后，只有 FL.2 的有限 \(M\) 层，没有将宽度继续缩到零。由有限次代入，
\[
\boxed{
F_N(R)\le
 \alpha_N^M\,\frac{M_0^2+\nu D_0}{R}
 +C\sum_{k=0}^{M-1}\alpha_N^kG_k
 +\frac{C}{1-\alpha_N}H_{R,N}.}
\tag{FL.14}
\]
逐层源与角阈值必须按定义保留。不能将 \(G_k\) 写成一个未经证明与层数无关的小量。

## 5. 条件尺度与剩余困难

若再有 MP.13 的完整平均结构界，在稍扩大的同一量级时间窗上仍有
\(S\le C_{\rm grad}R^{-2-2h}\)，\(0<h<1/2\)。
取固定 \(K>0\)，例如明确选择
\[
N_R=\max\!\left(N_*(\nu),4,\,
 1+\left\lceil K R^{-h}\right\rceil\right),
\qquad K^2\ge16C_{\rm grad}/\nu.
\tag{FL.15}
\]
则 FL.1 成立，FL.14 的第一、第三项随 \(R\to0\) 趋零。第一项的有限层幂 \((C_\nu/N_R)^{\lfloor\sqrt{N_R}\rfloor}\) 压过 \(R^{-1}\)；第三项的 \(e^{-c\sqrt{N_R}}\) 压过 FL.11 中全部多项式。这里只在每个窗口固定 \(N_R\)，并未建立不同窗口阈值变化的无代价能量演化。

因此在这些条件下，
\[
F_{N_R}(R)
 \le C\sum_{k=0}^{M_R-1}\alpha_{N_R}^kG_{k,R}+o(1).
\tag{FL.16}
\]
这是把平均混合压力的外球误差纳入原能量界的条件性局部化；不是把右侧非线性源控制住。其时间域止于 \(-R^2/2\)，不是整个 \((-R^2,0)\)，不能直接填入原 PF 的完整好尺度条件。

直接以固定 \(N\) 无限缩小间距时，FL.8–9 的常数会增大；本节靠有限层与随后增长的 \(N_R\) 处理尾项，未声称传统无限步迭代成立。固定一个大 \(N\) 而令 \(R\to0\)，也不能凭上述尾估计推出趋零。

本节只作解析检验，不运行科学数值，不引入新外力、不换初值或黏性。它沿用经典截止能量、角谱隙和球谐估计；没有新颖性、人类同行评审、形式证明或一般 B 结论。完整源的有符号控制、低模与 PF 的共同有限尺度常数仍开放。
