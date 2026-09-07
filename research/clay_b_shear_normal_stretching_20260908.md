# 剪切流的法向偏离与涡伸长：抵消在哪里失效

2026-09-08，北京时间。SN，PRIVATE_CORE。范围内解析推导及真实 NS 解族的反检；一般三维正则性仍 OPEN / NOT CLAY。不宣称新颖性或真人同行评审。

一维热剪切的法向梯度满足一个封闭的线性压力系统；整胞涡伸长的一阶项也确实抵消。但这不是“接近秩一”本身带来的普遍抵消。把背景改为仍然秩一的二维横向热剪切，一阶涡伸长即可为正，而且保持到共同的固定正时间窗。

这给出一个明确限制：不能把 GD 的线性偏离伸长界，未经额外条件地提升为整胞的偏离平方界。下面先保留一维情形的正确抵消，再给出失效的精确背景条件与相容反例。

## 1. 完整线性化，不先删压力

固定未归一化的 \(\mathbb T^3_{2\pi}\)、\(\nu>0\)。沿用 GD/LK 的
\(A=\nabla u\)、\(Q=|A|_F\)、\(d=\operatorname{dist}_F(A,\{\operatorname{rank}\le1\})\)、
\(k=|\operatorname{adj}A|/Q\)，零点按 LK 定义。先取光滑精确背景
\[
 \bar u=U(t,y)e_1,\quad U_t=\nu U_{yy},\quad
 a=U_y,\quad \bar A=aE_{12},\quad \bar p=0,\quad
 \bar L=\partial_t+U\partial_x-\nu\Delta.
 \tag{SN.1}
\]
令 w 为任意三维、周期、无散的线性化扰动，压力均值零，\(V_{ij}=\partial_jw_i\)。直接求导原 NS 得
\[
 \bar Lw=-aw_2e_1-\nabla\pi,\qquad
 \Delta\pi=-2aV_{21},
\]
\[
 \boxed{\bar LV=-V\bar A-\bar AV-a_yw_2E_{12}-H,\qquad H=\nabla^2\pi.}
 \tag{SN.2}
\]
压力源均值为零，因为 a 与 x 无关且 \(V_{21}=\partial_xw_2\)。\(a_yw_2E_{12}\) 是真实背景曲率项，不因接下来某些分量没有它而从完整方程消失。

## 2. 四个法向分量及零背景限制

定义
\[
 n=(V_{33},V_{23},V_{31},V_{21}),\qquad
 \mathcal N(V)=
 \begin{pmatrix}0&-V_{33}&V_{23}\\0&0&0\\0&V_{31}&-V_{21}\end{pmatrix}.
 \tag{SN.3}
\]
在 \(a\ne0\)、\(\epsilon|V|\le|a|/2\) 处，伴随矩阵二次多项式及分母展开给
\[
 \frac{\operatorname{adj}(\bar A+\epsilon V)}{|\bar A+\epsilon V|}
 =\epsilon\,\operatorname{sgn}(a)\mathcal N(V)
   +O\!\left(\frac{\epsilon^2|V|^2}{|a|}\right),\qquad
 k(\bar A+\epsilon V)=\epsilon|n|
   +O\!\left(\frac{\epsilon^2|V|^2}{|a|}\right)
 \quad(\epsilon>0).
 \tag{SN.4}
\]
这里使用完整恒等式
\(D\operatorname{adj}_{\bar A}[V]=\bar AV+V\bar A-(\operatorname{tr}V)\bar A-\operatorname{tr}(\bar AV)I\)。
因 \(\operatorname{tr}V=0\)，才得到 SN.3。n 对应固定非零秩一矩阵的四个法向梯度方向。

这不是跨 \(a=0\) 的统一可微化。若 \(a=0\)，商在正向射线上等于
\(\epsilon\operatorname{adj}V/|V|\)（V=0 时为零），依赖 V 的方式不是线性的。下文直接求 n 的导数，不求 \(\operatorname{sgn}(a)\) 的导数，也不把 n 在全域等同于 k 或 d。

## 3. 压力系统闭合，背景系数仍在

令 \(R_{ij}=\partial_i\partial_j\Delta^{-1}\)，逆算子作用于均值零周期源。取 SN.2 的四个分量，得到
\[
 \boxed{\bar Ln
 =2(R_{33},R_{23},R_{31},R_{21})(a n_4).}
 \tag{SN.5}
\]
这是对实际梯度得到的全域方程，包括 \(a=0\)；它不要求选取法向框架在零点连续。其相容约束至少包括
\(\partial_zn_4=\partial_xn_2\)、\(\partial_xn_1=\partial_zn_3\)，并且 n 来自同一个无散 w，不能任取四个标量后都解释成速度梯度。

被投影掉的切向分量仍满足
\[
 \bar LV_{12}=aV_{33}-a_yw_2-H_{12}.
\]
因此 n 的封闭并不等于完整扰动梯度的无背景增长。

对非零频率 \(\xi\)，SN.5 中四个乘子的平方和是
\[
 \frac{\xi_3^4+\xi_2^2\xi_3^2+\xi_3^2\xi_1^2+\xi_2^2\xi_1^2}{|\xi|^4}\le1.
\]
用 Plancherel 和输运积分消去，
\[
 \frac12\frac d{dt}\|n\|_2^2+\nu\|\nabla n\|_2^2
 =2\langle n,(R_{33},R_{23},R_{31},R_{21})(an_4)\rangle
 \le2\|a\|_\infty\|n\|_2^2.
 \tag{SN.6}
\]
所以 \(\|n(t)\|_2\le\exp(2\int_0^t\|a(s)\|_\infty ds)\|n(0)\|_2\)。这只是显式保留背景系数的线性估计，右端压力配对不是已经证明为零或非正。没有从一般 NS 能量界得到这个背景系数，也没有由此控制非线性余项或 GD.11。

## 4. 真正的整胞涡伸长与 k 增长不同

对任意光滑无散周期 v，令 \(V=\nabla v\)、\(E=\operatorname{sym}V\)、\(\zeta=\operatorname{curl}v\)。这里只在固定时刻展开
\(u_\epsilon=\bar u+\epsilon v\)，不假定 v 是不变的演化模式。记
\[
 \mathscr S(u)=\int_{\mathbb T^3}\omega(u)\cdot S(u)\omega(u).
\]
一维背景有 \(\bar\omega=-ae_3\)、\(\bar S\bar\omega=0\)，故精确点态展开为
\[
 \omega(u_\epsilon)\cdot S(u_\epsilon)\omega(u_\epsilon)
 =\epsilon a^2V_{33}
 +\epsilon^2a\{\zeta_1\zeta_2-2(E\zeta)_3\}
 +\epsilon^3\zeta\cdot E\zeta.
 \tag{SN.7}
\]
\(\int a^2V_{33}=\int a^2\partial_zv_3=0\)，因为 a 与 z 无关。由此得到整胞的一阶消去；不能把点态 \(a^2V_{33}\) 直接置零。

写 \(\mathscr S(u_\epsilon)=\epsilon^2\mathcal C_2+\epsilon^3\mathcal C_3\)。周期分部积分给
\[
 \int aV_{31}V_{23}=\int aV_{33}V_{21},\qquad
 \int aV_{13}V_{32}=\int aV_{12}V_{33}+\int a_yv_1V_{33}.
\]
把 \(\zeta=(V_{32}-V_{23},V_{13}-V_{31},V_{21}-V_{12})\) 代入 SN.7，得到
\[
 \boxed{\mathcal C_2=
 \int a\{V_{33}(V_{21}+V_{12})-V_{31}V_{32}-V_{13}V_{23}\}
 -\int a_yv_1V_{33},\qquad
 \mathcal C_3=\int\zeta\cdot E\zeta.}
 \tag{SN.8}
\]
每个 \((x,y)\) 上 \(V_{33}\) 的 z 均值为零。对末项的 v_1 减去该方向均值并用周期 Poincaré，再用 Cauchy–Schwarz，得
\[
 |\mathcal C_2|
 \le(\sqrt2\|a\|_\infty+\|a_y\|_\infty)\|n(V)\|_2\|V\|_2.
 \tag{SN.9}
\]
这是法向量与完整扰动的混合二次界，不是法向量平方闭合。三次项仍为真实扰动伸长，没有从 SN.6 推出其无条件控制。

二次项也不恒为零。例如取 \(M>0\)、\(\bar u=-M\sin y\,e_1\)，
\[
 v=(\sin x\cos y\cos z,\;(\sin x-\cos x\sin y)\cos z,\;0).
\]
直接求导验证无散和均值零。SN.8 只剩
\(-\int aV_{13}V_{23}=M\pi^3\)。平移 \(z\mapsto z+\pi\) 使 V 变号，所以三次项积分为零；完整初始 \(\mathscr S=M\pi^3\epsilon^2>0\)。

反之，LK 的平面二维解族具有 \(u_3=0\)、\(\partial_zu=0\)，其涡伸长点态恒为零。LK 的 k 压力生产不是涡伸长生产，不能互换两个对象的反例。

## 5. 秩一背景本身不保证一阶消去

改取同样是原无外力 NS 精确解的背景
\[
 \bar u=U(t,y,z)e_1,\qquad U_t=\nu\Delta_\perp U,\qquad
 \bar p=0,\qquad
 \bar A=e_1\otimes(0,U_y,U_z),\quad
 \bar\omega=(0,U_z,-U_y).
 \tag{SN.10}
\]
其梯度处处秩至多一，\(\bar u\cdot\nabla\bar u=0\)。对任意三维无散 v，由 \(\bar S\bar\omega=0\)，伸长的一阶泛函为
\[
 \mathcal L_U(v)
 =\int\bar\omega\cdot(\operatorname{sym}\nabla v)\bar\omega
 =-\int v\cdot(\bar\omega\cdot\nabla)\bar\omega
 =\int v_\perp\cdot F_U,\qquad
 F_U=(\Delta_\perp U)\nabla_\perp U.
 \tag{SN.11}
\]
最后使用
\[
 (\bar\omega\cdot\nabla)\bar\omega
 =\nabla_\perp\frac{|\nabla_\perp U|^2}{2}
 -(\Delta_\perp U)\nabla_\perp U
\]
和无散测试。若 v 依赖 x，可先取其 x 平均；横向平均速度仍无散。因此下述条件针对所有三维无散变分，而不只针对二维测试。

F_U 的每个分量均值为零：
\(\int\Delta U\,\partial_iU=-\frac12\int\partial_i|\nabla U|^2=0\)。
周期 Helmholtz 分解于是给精确判据
\[
 \boxed{\mathcal L_U(v)=0\ \hbox{对所有周期无散 v}
 \iff P_\perp F_U=0
 \iff \mathcal J_U:=(\Delta U)_yU_z-(\Delta U)_zU_y=0.}
 \tag{SN.12}
\]
这里 \(P_\perp\) 是二维周期 Leray 投影。均值零条件排除了常向量障碍。若 \(\mathcal J_U\ne0\)，取
\(v_\perp=(\partial_z\mathcal J_U,-\partial_y\mathcal J_U)\) 即有
\(\mathcal L_U(v)=\int\mathcal J_U^2>0\)。

这只是 SN.10 这类背景的一阶变分判据，不是所有秩一梯度的分类，也不是全局正则性判据。一维 U 或单个 Laplace 特征空间中的 U 满足此条件；一般横向热剖面未必满足。

## 6. 一阶真实伸长对二阶偏离的相容反例

固定
\[
 U_0=\sin y+\sin(2z),\qquad
 \phi=\cos y\cos(2z),\qquad
 v_0=(0,\phi_z,-\phi_y)
 =(0,-2\cos y\sin(2z),\sin y\cos(2z)).
 \tag{SN.13}
\]
它们给光滑、周期、均值零、无散初值 \(u_{\epsilon,0}=U_0e_1+\epsilon v_0\)，所有固定阶 Sobolev 范数在 \(0<\epsilon\le1\) 上统一有界。由
\(\Delta U_0=-\sin y-4\sin(2z)\)，
\[
 \mathcal J_{U_0}=6\cos y\cos(2z),\qquad
 \mathcal L_{U_0}(v_0)=\int\phi\mathcal J_{U_0}=12\pi^3.
\]
此外 \(\zeta_0=(5\cos y\cos(2z),0,0)\)，\(E_0=\operatorname{sym}\nabla v_0\) 的第一行列均为零，而 \(\bar S_{11}=0\)。所以二、三次伸长项点态都为零，得到精确整胞式
\[
 \boxed{\mathscr S(u_{\epsilon,0})=12\pi^3\epsilon.}
 \tag{SN.14}
\]
另一方面，比较矩阵 \(\bar A_0\) 本身秩至多一，
\[
 d(A_{\epsilon,0})\le\epsilon|\nabla v_0|,\qquad
 Q_{\epsilon,0}\le|\bar A_0|+\epsilon|\nabla v_0|,\qquad
 \int Q_{\epsilon,0}d(A_{\epsilon,0})^2\le C\epsilon^2.
 \tag{SN.15}
\]
因此不存在对该共同有界初值族成立的有限 C，使
\(\mathscr S(u_{\epsilon,0})\le C\int Q_{\epsilon,0}d^2\)。
允许 C 依赖固定背景、黏性与共同光滑范数上界，仍不改变这个阶数矛盾。它也否定更强的绝对值版本；不是只对任意矩阵作阶数检查。

## 7. 固定正时间窗，不只初始切片

背景精确热演化为
\(\bar U(t)=e^{-\nu t}\sin y+e^{-4\nu t}\sin(2z)\)。
标准局部强解理论给初值族的共同区间 \([0,T_1]\) 与统一 \(H^m\) 界，固定 \(m\ge5\)。沿用 LK.16–17 的差商能量证明，对此光滑背景有
\[
 u_\epsilon=\bar u+\epsilon w+O_{C_tH^{m-1}}(\epsilon^2),
 \quad
 \sup_{[0,T_1]}\|(u_\epsilon-\bar u)/\epsilon\|_{H^m}\le C.
 \tag{SN.16}
\]
该论证只要求背景有相应高阶界：差商以 u_epsilon 输运，保留 \(w_\epsilon\cdot\nabla\bar u\)；线性化误差的外源为 \(-\epsilon w_\epsilon\cdot\nabla w_\epsilon\)，不要求背景只依赖 y。常数与共同时间不依赖 epsilon。

唯一性保留 x 独立性。线性压力满足
\(\Delta\pi=-2(U_y\partial_xw_2+U_z\partial_xw_3)=0\)，故归一后为零。横向线性速度直接满足热方程，
\[
 w_\perp(t)=e^{-5\nu t}(v_{0,2},v_{0,3}),\qquad
 (\partial_t-\nu\Delta_\perp)w_1=-w_\perp\cdot\nabla_\perp\bar U,\quad w_1(0)=0.
\]
受迫的 w_1 不进入 SN.11 的一阶伸长，不能因此称完整线性速度只按热半群演化。计算
\(\mathcal J_{\bar U(t)}=6e^{-5\nu t}\cos y\cos(2z)\)，得到
\[
 \boxed{\mathscr S(u_\epsilon(t))
 =12\pi^3\epsilon e^{-10\nu t}+O(\epsilon^2)
 \quad\hbox{一致于 }[0,T_1].}
 \tag{SN.17}
\]
伸长是梯度的三次多项式，SN.16 和 Sobolev 嵌入足以给一致余项；这里不用 k 的零集极限。

故任意固定 \(0\le t_a<t_b\le T_1\) 都有
\[
 \int_{t_a}^{t_b}\mathscr S(u_\epsilon(t))\,dt
 =\epsilon\frac{12\pi^3}{10\nu}
   (e^{-10\nu t_a}-e^{-10\nu t_b})+O(\epsilon^2),\qquad
 \int_{t_a}^{t_b}\!\!\int Q_\epsilon d(A_\epsilon)^2=O(\epsilon^2).
 \tag{SN.18}
\]
末式由同时刻的秩一背景、统一差商梯度和 Q 上界给出。可取 \(t_a>0\)，时间窗不随 epsilon 缩短。因而上述纯二次吸收在真实原 NS 的共同正时间区间同样失败。

这里改变初值并研究共同局部寿命；没有假定一条固定解趋近奇异终点，没有奇点构造，也没有否定含初值项、线性背景耦合、方向变化或其他补偿项的估计。该特殊 x 独立解族不是一般三维问题的代表性证明。

## 8. 方向重写只恢复一个尚未控制的幅度项

为避免把 SN.11 的方向导数重新命名后当作新控制，直接与旧 VB 预算比较。对同一光滑周期速度，令 \(q=|\omega|\)、\(\xi=\omega/q\) 于 q>0，c 为任意空间常向量。周期分部积分和 \(\nabla\cdot\omega=0\) 给
\[
 \mathscr S(u)=-\int(u-c)\cdot(\omega\cdot\nabla)\omega,\qquad
 (\omega\cdot\nabla)\omega
 =q^2\{(\xi\cdot\nabla)\xi-(\nabla\cdot\xi)\xi\}\quad(q>0).
\]
第二式使用 \(\xi\cdot\nabla q=-q\nabla\cdot\xi\)。在 q=0 处，左边的乘积为零，右边只按该零值延拓；不在零点给方向选值或求导。由 \(|\nabla\cdot\xi|\le\sqrt3|\nabla\xi|\) 和 Cauchy–Schwarz，
\[
 \boxed{|\mathscr S(u)|
 \le(1+\sqrt3)
 \left(\int_{q>0}q|\nabla\xi|^2\right)^{1/2}
 \left(\int|u-c|^2q^3\right)^{1/2}.}
 \tag{SN.19}
\]
时间积分可再次用 Cauchy–Schwarz。旧 VB.8 已控制第一因子的时空平方积分，并保留初始涡量与非负零集测度；它没有给第二因子趋近候选终点的统一时空平方积分界。这里是一次导数的积分恒等式，不改写或删除 VB 的二阶链式测度。

局部也不能直接照搬全胞式。对光滑截止 \(\chi\)，分部积分还产生
\(-\int((u-c)\cdot\omega)(\omega\cdot\nabla\chi)\)，必须与带 \(\chi\) 的体积分一起保留。

SN.19 因而只明确了未得到的速度—幅度成本，不是新的临界估计。下轮不重复这条直接 Cauchy–Schwarz 重组，也不能凭“方向预算有限”宣布伸长可积。

## 9. 路线边界与来源

一维剪切的正确结论是 SN.5 的法向系统、SN.7–9 的一阶消去和带背景系数的混合二次项。SN.12–18 则阻止把它直接推广为“所有近秩一梯度都有二次整胞伸长”。压力不是唯一障碍：第二个解族的线性压力为零，一阶伸长仍为正。

下一步转向一个正面但尚未证明的局部接口：在候选点的抛物柱内，临界缩放的秩一偏离小量，连同写明的局部能量与压力条件，是否足以推出内柱正则性。先核对已有原文与量词，再推导局部涡量估计，保留输运边界、压强尾和零集成本。这个问题不得假定背景是一维剪切；小量正则性引理与“任意 NS 演化产生该小量尺度”是两个不同的缺口，前者即使完成也不等于 Clay。固定先检查 \(d\) 的尺度不变 \(L^{5/2}\) 时空小量，不作权重扫描；若它只是已有结果或不能由所列假设推出，如实记录并调整。不重复一次齐次熵、压力平方吸收、直接方向 Cauchy 重组或已否定的整胞二次提升。

去重定向读了旧 research/r072z_report-source.md 的第0–2节：Orr–Sommerfeld/Squire 三角系统与压力交换子已在旧稿出现，本节不重新认领。外部定向核对 [Li–Wei–Zhang 原稿 v1，导言 (1.1)–(1.6) 及线性三角式](https://arxiv.org/html/1801.05645v1)：该文处理受迫稳态 Kolmogorov 背景与特定周期，不将其增强耗散或稳定阈值结论移植到本文。未审查其定理证明、全部依赖或新颖性。局部强解输入和差分步骤按 LK 的已核对接口继承。

主任务及两位参与推导的 AI 审读者复算，实际文件版本另记；不是完全非作者或真人同行评审。没有 PDE 仿真、数值证书、DGX、科学附图或读者 HTML/PDF，不触发大里程碑回顾。新完整内容私有，按分工一次移交 PRIVATE_ARCHIVE；不请求网站、本地读者、公开概要、计数或附件。GD.11 的临界范数与一般 NS／Clay 结论仍未得到。
