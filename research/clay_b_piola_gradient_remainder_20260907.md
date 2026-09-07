# 应变梯度余项与 Piola 恒等式：还有什么没有被消去

2026-09-07（Asia/Shanghai）。内部来源接口检验 PGR；基准提交 454ace62fd12a720c411230649331c6364d864f0。不是科学发布冻结。

我接着 MSD 检查完整 NS 余项，而不是再测试热剪切上的标量费用。得到两项明确结论：高阶生产可以准确写成应变与梯度各向异性张量的配对，但没有获得其累计上界；一条确有符号的压力四次恒等式代回完整方程后恰好与惯性项抵消，不产生新增耗散。以下恒等式和原著接口不声称新颖性，更不等于正则性进展。

## 1. 完整方程的高阶配对

固定未归一化环面 \(\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3\)，\(V=(2\pi)^3\)，\(\nu>0\)。所有积分均在该环面。考察同一个实、光滑、无散、无外力 NS 解的任意光滑时间段。记
\(A_{ij}=\partial_j u_i\)、\(S=(A+A^\top)/2\)、\(\omega=\nabla\times u\)、\(H=\nabla^2p\)。

[Miller v2，第5节](https://arxiv.org/html/2407.02691v2) 将余项写为
\(R=P_{st}((u\cdot\nabla)S+S^2+\tfrac34\omega\otimes\omega)\)。
\(-\Delta S\) 属于应变空间，所以配对时可移除正交投影 \(P_{st}\)。
旧 R0.70X / MSD.1 已证明
\(\langle-\Delta S,\omega\otimes\omega\rangle=0\)。
完整应变方程中的 \(H\) 和标量倍数单位矩阵也与 \(-\Delta S\) 正交：前者两次分部积分用 \(\partial_i\partial_j S_{ij}=0\)，后者用 \(\operatorname{tr}S=0\)。因此
\[
 Y=\|\nabla S\|_2^2,\qquad Z=\|\Delta S\|_2^2,\qquad
 \frac12Y'+\nu Z
 =-\langle-\Delta S,R\rangle
 =-\langle-\Delta S,(u\cdot\nabla)S+S^2\rangle .
 \tag{PGR.1}
\]
这来自完整方程，不是删去输运后的模型能量。

令 \(T_k=\partial_kS\)，并设
\(I=\langle-\Delta S,(u\cdot\nabla)S\rangle\)、
\(J=\langle-\Delta S,S^2\rangle\)。
分部积分展开 \(I\) 后，输运 \(T_k\) 自身的项为
\(\int u_\ell\partial_\ell |T_k|^2/2=0\)。剩下的 Gram 矩阵对称，故速度梯度的反对称部分也消失。对 \(J\) 用乘积法则及迹的循环性：
\[
 \begin{aligned}
 I&=\sum_{k,\ell}\int \partial_ku_\ell\,(T_k:T_\ell)
   =\sum_{k,\ell}\int S_{k\ell}(T_k:T_\ell),\\
 J&=\sum_k\int T_k:(T_kS+ST_k)
   =2\sum_k\int\operatorname{tr}(S T_k^2).
 \end{aligned}
 \tag{PGR.2}
\]
这里 \(B:C=\operatorname{tr}(B^\top C)\)。

定义 \(\mathsf G_{k\ell}=T_k:T_\ell\)、\(\mathsf K=\sum_kT_k^2\)。
\(\mathsf G\) 是 Gram 矩阵；对任意 \(e\)，
\(e^\top\mathsf K e=\sum_k|T_ke|^2\)。故
\[
 \mathsf M=\mathsf G+2\mathsf K\succeq0,\qquad
 \operatorname{tr}\mathsf M=3|\nabla S|^2,\qquad
 \mathsf M^\circ=\mathsf M-|\nabla S|^2I_3,\qquad
 I+J=\int S:\mathsf M^\circ.
 \tag{PGR.3}
\]
最后一步只利用 \(\operatorname{tr}S=0\)。被消去的是各向同性部分，不是整个高阶生产。半正定的 \(\mathsf M\) 与迹零的 \(S\) 配对没有自动的有利符号。常规估计仍只有
\(-S:\mathsf M\le3\lambda_{\min}^-(S)|\nabla S|^2\le3|S||\nabla S|^2\)。
于是 \(Y'\le6\|S\|_\infty Y\) 是一个条件 Gronwall 接口；这里没有证明 \(\int\|S\|_\infty dt\) 有限。

## 2. 不能把相容性理解成整个配对为零

无需创造新的流族。使用既有 [HN.9–11 的场](clay_b_heat_normal_form_20260907.md)：正频率
\(p=(1,0,0),q=(0,2,0),r=(1,2,0)\)，系数分别为
\((0,1,0),(1,0,0),i(2,-1,0)\)，负频率取共轭。
它是一个相容的真实无散速度场，满足应变的全部微分约束。

记 \(\mathcal N(v)=P_{df}((v\cdot\nabla)v)\)。完整方程在这一初值处的高阶速度能量和应变能量一致，
\(Y=\tfrac12\|\Delta v\|_2^2\)，故
\(I+J=\tfrac12\langle\Delta v,\Delta\mathcal N(v)\rangle\)。
HN 的三个正频率实配对为 \(1,-4,3\)。保留负频率的因子2，得到
\[
 I+J
 =V\bigl(1^2\cdot1+4^2\cdot(-4)+5^2\cdot3\bigr)
 =12V\ne0.
 \tag{PGR.4}
\]
由于此场平面、无第三分量，\(S\) 和各 \(T_k\) 的平面块迹零且对称，\(T_k^2\) 的平面块是标量矩阵，所以 \(J=0\)、\(I=12V\)。有限全卷积另行复核了这些系数。

替换 \(v\) 为 \(-v\) 后，\(S\) 变号而 \(\mathsf M\) 不变，配对变为 \(-12V\)。这只否定该完整三次配对对所有相容场恒零或具有统一符号，不分类所有可能的高阶恒等式。每个这样的场可作局部光滑原 NS 的初值；没有假设有限 Fourier 支撑沿时间封闭，也没有仅凭非线性功的符号断言总导数为正或发生爆破。

## 3. 有符号的压力四次恒等式确实存在

本轮另查 [Carbone–Wilczek，JFM 948 (2022), R2，第5节](https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/article/only-two-betchov-homogeneity-constraints-exist-for-isotropic-turbulence/B7E010E18EEE8B1B0646E28DB86A4398)。以下直接在周期场上重证所需关系，不引入统计各向同性假设。

令 \(q=\operatorname{tr}(A^2)\)、\(C=A^2-\tfrac12qI_3\)。这个 \(C\) 一般不对称。指标方向不能随意互换：
\[
 \begin{aligned}
 \partial_i C_{ij}
 &=\partial_i(A_{ik}A_{kj})-\tfrac12\partial_jq\\
 &=A_{ik}\partial_jA_{ki}-\tfrac12\partial_jq=0,\\
 \int\operatorname{tr}(A^2\nabla w)
 &=\frac12\int q\,\operatorname{div}w
 \quad\text{对任意光滑周期向量场 }w .
 \end{aligned}
 \tag{PGR.5}
\]
这里用 \(\partial_iA_{ik}=\partial_k\operatorname{div}u=0\)、
\(\partial_iA_{kj}=\partial_jA_{ki}\)，以及
\(\operatorname{tr}(A^2\nabla w)=(A^2)_{ij}\partial_iw_j\)。
最后一行是对 \(\partial_i(C_{ij}w_j)\) 的积分；不是把一般矩阵的行散度与列散度混同。

NS 压力满足 \(\Delta p=-q\)。依次取 \(w=\nabla p\)、\(w=\Delta u\)、\(w=u\)，有
\[
 \int\operatorname{tr}(A^2H)=-\frac12\int q^2,\qquad
 \int\operatorname{tr}(A^2\Delta A)=0,\qquad
 \int\operatorname{tr}(A^3)=0 .
 \tag{PGR.6}
\]
第一项有确定符号。它不是此前点态压力 Hessian 符号反例能否定的对象；点态符号与这种完整全域配对必须区分。

但不能单独保留这项，声称获得四次耗散。对任意迹零 \(3\times3\) 矩阵，Cayley–Hamilton 为
\(A^3-\tfrac12qA-(\det A)I_3=0\)。乘以 \(A\) 取迹，得到
\[
 \operatorname{tr}(A^4)=\frac12q^2 .
 \tag{PGR.7}
\]
这个代数等式不要求 \(A\) 对称。

## 4. 代回同一条解，四次项恰好零和

完整的速度梯度方程是
\[
 (\partial_t+u\cdot\nabla)A
 =\nu\Delta A-A^2-H .
 \tag{PGR.8}
\]
对每时刻恒零的 Betchov 积分求导，输运项是全域散度。由 PGR.6–7，
\[
 \begin{aligned}
 0=\frac d{dt}\int\operatorname{tr}(A^3)
 &=3\nu\int\operatorname{tr}(A^2\Delta A)
   -3\int\operatorname{tr}(A^4)
   -3\int\operatorname{tr}(A^2H)\\
 &=0-\frac32\int q^2+\frac32\int q^2=0 .
 \end{aligned}
 \tag{PGR.9}
\]
因此有利的压力四次项被惯性四次项精确抵消。这个计算对同一个实际解、每个光滑时刻成立；它不是用静态反例猜测时间行为。但它的结果是零恒等式，没有给 \(\int q^2\,dx\,dt\) 新上界，也没有支付 PGR.3 中的有符号梯度配对。

Carbone–Wilczek 的完整性陈述只针对其单点速度梯度标量、统计齐次/各向同性框架。本轮不把它当作包含 \(\nabla A\)、非局部量或时间相关性的完整分类，也没有独立认证其整个张量表示分类证明。PGR.5–9 用的是直接指标证明，所以不依赖那项完整性陈述。

## 5. 本轮停止在哪里

Miller 第5节的比较判据仍需额外的 residual norm 或其与 \(\|\Delta S\|_2\) 的比值；第6节的谱偏离费用已在 MSD 检查过。这里的 \(\mathsf M^\circ\) 精确指出了余项，却没有获得新的动态小量。

我停止“这些运动学消去本身就能支付完整 NS 余项”的尝试。下一步不能仅把 \(-\int S:\mathsf M^\circ\) 命名为新耗减系数，也不能把 \(\int\|S\|_\infty\)、正性未知的压力项或高阶初值的未知终端范数放进右端，便称为闭合。需要一个尚未得到的、来自同一条原解时间演化的累计控制；本节没有接受这样的候选。

此决定不排除利用额外时空信息的其它应变、压力或几何方法。G、R216–R217、一般终端缺口与任意光滑初值三维正则性继续 OPEN / NOT CLAY。本文是内部来源接口关闭记录，不创建科学 release 或发布交接；没有仿真、DGX、科学附图、读者页面或累计 recap。有限复算与独立审查范围另见配套记录。
