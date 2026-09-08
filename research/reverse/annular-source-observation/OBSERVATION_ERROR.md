# 环带两阶段来源的条件观测误差接口

2026-09-09，PRIVATE_CORE。**手推条件接口，待非作者审查。** 本文只在同一固定初值 a_* 的完整 NS 轨迹已有全窗 H³ 误差证书时，传递有限环带状态与两次历史积分的误差；当前没有这样的轨迹证书，不接纳任何实际来源门或数值候选，也不另计新独立正式结果包。

本人此前定位并阅读了旧 SOURCE_PREFLIGHT 的一般后验接口，随后先向根给出本推导摘要。根在形成前已披露 Cauchy 和三角预算的预见；这里不称全盲或与根互盲。本稿没有读取本项其它新推导、输入准备结果或求解器源码。下文先给一般时间接口，再固定为本合同的 s=0、a=T/2、t=T、T=8/C；C 的正有理值由单独输入准备锁定，本文不求值或优化它。

## 1. 前提与范数

仍在标准 2π 三维环面，ν=1，无外力，u 从第 24 包唯一 a_* 出发。设既有后验认证覆盖完整 [0,T]，其近似场 v 实值、零均值、无散，并具有 SOURCE_PREFLIGHT 所需的 C(H⁵)∩C¹(H³) 正则性。假设已经证明同一真实原解覆盖该窗且

\[
\|u(r)-v(r)\|_{\dot H^3,\mathrm{un}}
\le R(r),\qquad 0\le r\le T,
\tag{OE.1}
\]

其中 R 连续、非负。这里的“un”指旧原文以未归一化体积和正交归一 Fourier 基定义的齐次范数。OE.1 是前提，不由采样误差、分辨率差或有限 ODE 的存在推出；旧控制上解的比较及延续原理不在本文重证。

本文使用归一化 Fourier 系数 \(\widehat f(k)\)，向量长度为 Hermitian 长度。对零均值场，明确约定

\[
\|f\|_{\dot H^3,\mathrm{un}}^2
=(2\pi)^3\sum_{k\ne0}|k|^6|\widehat f(k)|^2.
\]

这是齐次 \(|k|^6\) 权重，不是非齐次 \((1+|k|^2)^3\) 权重。其余范数和换算为

\[
\|f\|_2^2=(2\pi)^{-3}\int|f|^2
=\sum_k|\widehat f(k)|^2,\qquad
\|f\|_{A0}=\sum_k|\widehat f(k)|,
\]
\[
\rho(r)=(2\pi)^{-3/2}R(r),\qquad
\sum_{k\ne0}|k|^6|\widehat{u-v}(k,r)|^2\le\rho(r)^2.
\tag{OE.2}
\]

B 内点积仍是复双线性；估计绝对值时才使用 Hermitian 长度。令 \(M=\|a_*\|_2\)。完整原解的能量不等式给 \(\|u(r)\|_2\le M\)。若以后只使用已认证上界 \(\overline M\ge M\)，下文可以统一以该上界替换 M；不需要更改物理初值。

唯一观测集是

\[
H_j=\{k\in\mathbb Z^3:L_j\le |k|<2L_j\},
\qquad L_j=2^{j+2},\quad j=0,1,2.
\]

它们分别是 [4,8)、[8,16)、[16,32) 三个环带，全部正负模均计入。置 \(h_j=P_{H_j}u,\ \widetilde h_j=P_{H_j}v\)。观测投影不限制完整 u 或 v 的支持。

## 2. Cauchy 权重与状态误差

只以符号保留有限集合大小和权重：

\[
N_j=\#H_j,\qquad
c_j=\left(\sum_{k\in H_j}|k|^{-6}\right)^{1/2}.
\]

对 \(\xi_j=h_j-\widetilde h_j\)，加权 Cauchy 直接给

\[
\|\xi_j(r)\|_{A0}
\le c_j\rho(r)=:E_j(r),\qquad
c_j\le \sqrt{N_j}\,L_j^{-3},
\tag{OE.3}
\]
\[
\|\xi_j(r)\|_2
\le L_j^{-3}\rho(r)=:d_j(r).
\tag{OE.4}
\]

因此

\[
\|h_j(r)\|_2\le M,\qquad
\|\widetilde h_j(r)\|_2\le M+d_j(r).
\tag{OE.5}
\]

没有枚举环带、计算 N_j 或用全带 A0 范数冒充单个正模范数。OE.3 的正负模只各计一次。

## 3. 完整有序热算子的绝对界

对无散 f,g，完整 Fourier–Leray 系数是

\[
\widehat{B(f,g)}(k)
=-iP_k\sum_{\ell+m=k}
(\widehat f(\ell)\cdot m)\widehat g(m).
\]

因为 \(\widehat f(\ell)\cdot\ell=0\)，可把 m 换为 k。Leray 的复 Euclidean 算子范数不超过 1；对卷积用 Cauchy，得到

\[
|\widehat{B(f,g)}(k)|
\le |k|\sum_\ell|\widehat f(\ell)|\,|\widehat g(k-\ell)|
\le |k|\|f\|_2\|g\|_2.
\tag{OE.6}
\]

这是对完整有序项的上界，没有删除负模、横向分量或相位。以下实际使用的输入均在有限环带内，卷积与投影没有收敛交换问题。

定义有限热权重

\[
K_j(\tau)=\sum_{k\in H_j}|k|e^{-|k|^2\tau},
\qquad \tau\ge0.
\]

则

\[
\|e^{\tau\Delta}P_{H_j}B(f,g)\|_{A0}
\le K_j(\tau)\|f\|_2\|g\|_2,\qquad
K_j(\tau)\le 2L_jN_j e^{-L_j^2\tau}.
\tag{OE.7}
\]

可保留精确有限核，也可使用右侧较粗核；本文不计算其中任何有限和。若 h=\(\widetilde h+\xi\)，准确身份为

\[
B(h,h)-B(\widetilde h,\widetilde h)
=B(\xi,h)+B(\widetilde h,\xi).
\]

第一项保留真实 h，故它已经包含展开后的误差平方项。结合 OE.4–7，

\[
\|e^{\tau\Delta}P_{H_j}
[B(h_i,h_i)-B(\widetilde h_i,\widetilde h_i)](r)\|_{A0}
\le K_j(\tau)d_i(r)[2M+d_i(r)].
\tag{OE.8}
\]

两个有序交叉没有合并为同一个向量；其中 \(d_i^2\) 不能略去。

## 4. 两次真实历史积分误差

先固定任意 \(0\le s<a<t\le T\)。定义

\[
g_s(r)=\int_s^r e^{(r-q)\Delta}P_{H_1}B(h_0,h_0)(q)\,dq,
\quad
\widetilde g_s(r)=\int_s^r e^{(r-q)\Delta}P_{H_1}
B(\widetilde h_0,\widetilde h_0)(q)\,dq,
\]
\[
S(t;a)=\int_a^t e^{(t-r)\Delta}P_{H_2}B(h_1,h_1)(r)\,dr,
\quad
\widetilde S(t;a)=\int_a^t e^{(t-r)\Delta}P_{H_2}
B(\widetilde h_1,\widetilde h_1)(r)\,dr.
\]

这些带波浪号的积分暂指从已给重建 v 定义的数学上精确积分，不是假定实际数值求积无误差。令

\[
I_{ij}(b,c)=\int_b^c K_j(c-r)d_i(r)[2M+d_i(r)]\,dr.
\tag{OE.9}
\]

由 OE.8 和积分三角不等式，

\[
\|g_s(r)-\widetilde g_s(r)\|_{A0}\le I_{01}(s,r),
\qquad s\le r\le t,
\]
\[
\|S(t;a)-\widetilde S(t;a)\|_{A0}\le I_{12}(a,t).
\tag{OE.10}
\]

第二源始终使用实际 \(h_1\) 及其近似 \(\widetilde h_1\)，不换成 \(g_s\) 或 \(\widetilde g_s\)。OE.10 本身不以第一来源门成立为前提；第一门是另外要观测的条件。

令

\[
e_1(r)=h_1(r)-g_s(r),\quad
\widetilde e_1(r)=\widetilde h_1(r)-\widetilde g_s(r),
\]
\[
e_2(t;a)=h_2(t)-S(t;a),\quad
\widetilde e_2(t;a)=\widetilde h_2(t)-\widetilde S(t;a).
\]

则有

\[
\|e_1-\widetilde e_1\|_{A0}\le E_1+I_{01}(s,r),
\qquad
\|e_2-\widetilde e_2\|_{A0}\le E_2+I_{12}(a,t).
\tag{OE.11}
\]

真实余项的完整方程身份没有改变。置 \(z_i=u-h_i\)，则

\[
\begin{aligned}
e_1(r)
&=e^{(r-s)\Delta}h_1(s)\\
&\quad+\int_s^r e^{(r-q)\Delta}P_{H_1}
[B(h_0,z_0)+B(z_0,h_0)+B(z_0,z_0)](q)\,dq,
\end{aligned}
\]
\[
\begin{aligned}
e_2(t;a)
&=e^{(t-a)\Delta}h_2(a)\\
&\quad+\int_a^t e^{(t-r)\Delta}P_{H_2}
[B(h_1,z_1)+B(z_1,h_1)+B(z_1,z_1)](r)\,dr.
\end{aligned}
\tag{OE.12}
\]

因此正起点已有场、初始种子、非相邻频率、回流和环带外所有作用都没有清空。周期压力已通过完整 Leray 保留，黏性通过原热半群保留。OE.1 若来自有限支持重建，旧一般接口还要求其残差同时包含支持内重建缺陷和支持外全部非线性漏出；OE.12 不能替一个漏项的轨迹证书补票。

## 5. 总带门的严格通过、否定与未决

先针对上述数学上精确的重建积分，定义真实门函数

\[
F_1(r)=\|e_1(r)\|_{A0}-\tfrac14\|g_s(r)\|_{A0},
\qquad
F_2(t)=\|e_2(t;a)\|_{A0}-\tfrac14\|S(t;a)\|_{A0}.
\]

波浪号门函数以相应波浪号向量定义。由范数的反三角不等式，

\[
|F_1(r)-\widetilde F_1(r)|
\le E_1(r)+\tfrac54 I_{01}(s,r)=:\Delta_1(r),
\]
\[
|F_2(t)-\widetilde F_2(t)|
\le E_2(t)+\tfrac54 I_{12}(a,t)=:\Delta_2(t).
\tag{OE.13}
\]

第一门要求所有 \(r\in[a,t]\) 同时成立。因而：

- 若证明 \(\max_{r\in[a,t]}[\widetilde F_1(r)+\Delta_1(r)]<0\)，第一门严格通过；只证该上界不超过 0，则认证原合同的非严格乘式门，但不称有严格裕量。
- 若某个经过认证的 \(r\in[a,t]\) 满足 \(\widetilde F_1(r)-\Delta_1(r)>0\)，第一全窗门被否定。
- 第二门分别由 \(\widetilde F_2(t)+\Delta_2(t)<0\) 严格通过，或由 \(\widetilde F_2(t)-\Delta_2(t)>0\) 否定；上界为 0 同样只给非严格门。
- 未落入可认证情形时，结论是“这些误差界无法判定”。这不是实际门失败，也不证明界已经足够精细。上述通过和否定判据均为充分判据，不声称必要性。

连续性使第一式中的最大值存在，但并不提供它的已计算上界。仅在若干采样时刻满足不等式，不能代替整个闭窗的证明。

## 6. 实际数值评估误差与非零责任

OE.1 控制 u 与指定重建 v 的差，不自动覆盖后来对 v 的系数读取、历史求积、向量相减和范数求值的误差。若实际向量报告分别为 \(\check g,\check e_1,\check S,\check e_2\)，并另外认证

\[
\|\check g-\widetilde g\|_{A0}\le\eta_g,\quad
\|\check e_1-\widetilde e_1\|_{A0}\le\eta_{e_1},
\]
\[
\|\check S-\widetilde S\|_{A0}\le\eta_S,\quad
\|\check e_2-\widetilde e_2\|_{A0}\le\eta_{e_2},
\]

则真实供给和余项的总向量误差可以取

\[
\sigma_g=I_{01}+\eta_g,\quad
\sigma_{e_1}=E_1+I_{01}+\eta_{e_1},
\]
\[
\sigma_S=I_{12}+\eta_S,\quad
\sigma_{e_2}=E_2+I_{12}+\eta_{e_2}.
\tag{OE.14}
\]

例如，若 \(\check e_1\) 由读取的 \(\check h_1\) 和 \(\check g\) 相减获得，\(\eta_{e_1}\) 须覆盖两者各自误差及该次相减的圆整误差；不能把共用 \(\check g\) 理解成误差自动抵消。OE.13 的门误差相应再增加 \(\eta_{e_i}+\eta_{\mathrm{source}}/4\)。报告范数本身的求值误差也另计。

等价地，对任一阶段的真实供给 Q 与余项 e，若最终非负报告数 \(n_Q,n_e\) 已有严格认证的标量误差
\[
|n_Q-\|Q\|_{A0}|\le\sigma_Q,\qquad
|n_e-\|e\|_{A0}|\le\sigma_e,
\]
这里的 \(\sigma\) 已包含轨迹、求积、读取及范数评估等全部相应误差，置

\[
L_Q=\max(0,n_Q-\sigma_Q),\quad U_Q=n_Q+\sigma_Q,\quad
L_e=\max(0,n_e-\sigma_e),\quad U_e=n_e+\sigma_e.
\tag{OE.15}
\]

则 \(U_e<L_Q/4\) 认证严格门，\(U_e\le L_Q/4\) 认证非严格门，\(L_e>U_Q/4\) 认证门失败。第一阶段必须在整个第二窗作此认证；第二阶段在固定终点作此认证。其它情形保留未决，不把区间重叠当作通过。

非零有效性应单独报告：\(L_Q>0\) 给实际供给正下界，若门同时成立，
\[
\|\text{实际目标}\|_{A0}
=\|Q+e\|_{A0}\ge\tfrac34\|Q\|_{A0}
\ge\tfrac34 L_Q>0.
\tag{OE.16}
\]
严格门判据本身强制供给非零；非严格门则可能只是 Q=e=0 的平凡情形。若证明 Q=0 而实际目标非零，门失败；不定义任何零分母比值。若现有界既不能分离零，也不能确认恒零，不能把非零资格记为已付。

## 7. 本合同特例与范围

本合同只能代入
\[
s=0,\qquad a=T/2,\qquad t=T,\qquad T=8/C>0.
\]
具体第一历史预算为 \(I_{01}(0,r)\)，必须依赖从 0 至 r 的完整轨迹误差；第一门覆盖每个 \(r\in[T/2,T]\)。第二预算为 \(I_{12}(T/2,T)\)，第二门及非零性在 T 支付。C 由单独输入准备锁定，本文不认证它的数值、T 的大小或任何时间比较；T 只是精确锁定的观测终点，不是已证明的原解存在时间。现有轨迹证书若未覆盖此 T，就不能据本接口认证本合同，也不能私自改用较短终点。

合同给定 \(h_1(0)=h_2(0)=0\)，所以 OE.12 的第一初始项在该特例确为零；这不删除其余来源，也不令 \(h_2(T/2)\) 自动为零。每个物理初值、重建初值误差和时间历程都仍属于同一 a_*，没有拼接不同解。

这里只有总带 A0 门；它不推出逐频率对门、每个模式非零、相位或形状返回、有利二次相干、跨代迭代或无限尺度。旧差型原绝对短窗障碍不被修复。本接口不求值合同所列三叶系数，不推断本环带实际门成立或失败，不启动数值执行。OPEN / NOT CLAY。

## 8. 实际来源与形成边界

| 来源 | 实际读取范围 | SHA-256 |
|---|---|---|
| annular-source-observation/CONTRACT.md | 本轮全文第 1–19 行；根补充齐次范数句后又全文读最终字节，核固定三个环带、T=8/C、两个时间门及数值边界 | 4ae019c3aac7d23a2392273a8cfb52ba08cf5131c35f8bc9e56918dae41c68d8 |
| fixed-seed-global-screen/SOURCE_PREFLIGHT.md | 本连续任务上一轮实际复读第 17–91、159–180 行；本轮复核当前字节。更早一次曾全文定位，本稿不冒称重读外部 PDF 或外引常数证明 | 9328d3b37fa35989149c02d9097f4c3279f5f366636c91eb1b6d79ef3c650192 |

本文没有重新使用旧特殊六模种子的具体控制参数。一般后验源中 K₃、G₃ 及经典延拓的证据边界仍按原记录；本文从已经给定的 OE.1 出发，OE.3–16 不需要重新取它们的数值。

全部推导为手工符号与有限和的规范估计；没有科学执行、导入、编译、FFT、环带枚举、未知系数/根/幅度/时间求值、Git、联网或外发。只写本文件，不改旧稿。全文自读和实际来源字节复核后停稿，随后另作非作者审查；本文件不自绑定自身哈希。
