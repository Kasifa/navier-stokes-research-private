# Clay B：时钟路线去重与随机表示预检

2026-09-07。内部研究记录，非新研究小节，非发布冻结。
状态：候选机制预检；G、R.216--R.217、三维全局正则性均 OPEN；NOT CLAY。

## 1. 本轮决定

我停止自动做一般的相邻尺度时钟相减。旧记录已经处理了固定物理尺度内的
壳层相减、停止时刻重组和真正跨物理尺度的热核局部预算。
把这些恒等式换一种记号，不会减少尚未证明的输入。

我改为检查随机拉格朗日表示是否带来不同的可用估计。
原著适用范围已经核查；下文记录一个同一光滑解上的双噪声预检。
它区分了相对坐标退化、物理对角扩散和未支付的应变成本。
目前没有得到更弱的充分输入，因此不把这些预检包装为新的正则性结果，
也不创建新 release。上一小节的单次交接状态保持不变。

全局目标仍按指定中心合同 G：对任意光滑周期散度零初值和有限候选首次
奇点时间，对每个指定空间点找到原合同中的移动能量小尺度。
不能假定每个奇点都有正能量原子，也不能用几乎处处的中心替换每个中心。

## 2. 旧路线的精确对应

以下是本轮阅读全文后的对应记录，不是对历史仓库作整体重新认证。
公式编号必须连同文件名理解；两个不同文件中的 S.14 不是同一公式。

| 对象 | 已有来源与实际结论 | 本轮决定 |
| --- | --- | --- |
| 固定物理 R 的完整壳层时钟 K=E+D=Q+F | arbitrary-clock 文件 R.202--207 给总变差和三分法；R.216 要求除有限例外外，K 可由可求和误差与端点动能控制；R.217 另要求时间持久性系数的加权和有界 | 空间相减本身不产生时间宽度 |
| 实际有厚度的梯度环带 | actual-collar 文件 S.43、46、50：相邻环带不共享一条可直接抵消的面；根、外边界、间隙、失配四项须完整保留 | 不把点态面抵消移植到厚环带 |
| 边界失配的正时钟 | boundary-mismatch 文件 S.67--74：得到薄边界时钟；空间系数有所改善，但 S.80--81 的提取与持久性仍是条件 | 不把一个通道的改善记作完整时钟已支付 |
| 加权 Abel 与单侧球时钟 | weighted-Abel 的 S.3、9--10、17--19 及 one-sided-ball 的 S.89--111：端点和权重总变差仍支付完整质量；终端残差是全体的一次和 | 抽象 N 与 sqrt(N) 例子不是 NS 反例 |
| 四通道重组 | cross-channel 文件 S.115--120 精确重建未知的停止时钟上穿量；三通道 S.137--139 消去部分停止/合并项，却仍留终端一次和 | 已知重组不是新的时空估计 |
| 不同物理 R 与 theta R | cross-scale-path 的 B.6--11：两个实际中心不同；能量尾趋零不给其归一化趋零速度 | 不能把两条路径当成一条 |
| 热核嵌套的真实物理尺度差 | signed-scale-local-budget 的 S.8--15：能量、通量、输运、时间和耗散全项的和，返回原单尺度方程测试失配；非负的耗散不使带符号测试失配变正 | 不可保留有利端点而丢弃压力或测试失配 |

特别要区分：R.216--217 的 k 是固定 R 内的壳层指标；
G-P/G-C 的 n 才是 R_n=theta^n R_0 的物理尺度指标。
前者的条件定理也还需要后续桥梁才能得到 G。
跨物理尺度比较保留 X_R、X_r、时间窗、归一化、完整压力和缺陷补全耗散。
压力规范常数的消去，不等于压力通量已经支付。

## 3. 原著核查怎样影响选择

[Constantin--Iyer，作者版 v4，Theorem 2.2 与第 4 节](https://arxiv.org/html/math/0511067v4)
给出光滑区间内的 Weber 随机表示。逆流形变仍在公式中；
保体积不等于形变有界。这里不移植奇点终端或任意弱解版本。

[Drivas--Eyink，作者版 v3，式 (53)--(54)](https://arxiv.org/html/1606.00729v3#S5.E53)
的 NS 方差包含压力冲量；其方差的一半在体积平均后等于累计黏性耗散。
它不是原合同中移动球的局部预算。标量的无源最大值原理不能越过压力项。

[Mahithitarmmatorn，arXiv:2608.16915v1，第 3--4 节](https://arxiv.org/html/2608.16915v1)
已写出同噪声均值—协方差闭合方程及共同坐标扩散。
闭合不等于能量级先验界；应变与梯度源仍在。
该文是预印本，不采用其后段外部正则性定理作为本轮证明输入。

这三项是文献适用性结论，不是新颖性证明。
日期、实际阅读范围、未读部分和检索停止理由见配套文献记录。

## 4. 双噪声：固定同一个光滑 NS 解

以下是本轮的直接 Itô 预检，不声称新颖性。
取固定 nu>0、无外力、周期光滑解 u，于每个紧区间 [0,T]，
T<T_* 上讨论。为简化常数取单位体积环面；初值 u_0 光滑、散度零。
记 G_ij=partial_j u_i，S=(G+G^T)/2。
这里的 G 矩阵与“合同 G”不是同一对象。

两组 Brownian W^1,W^2 各自是三维标准 Brownian，且
d[W^1_k,W^2_l]=rho delta_kl dt，0<=rho<=1。
可取 W^1=B，W^2=rho B+sqrt(1-rho^2) B'，B、B' 独立。
每一组噪声对所有空间标签相同。两组随机流都使用同一个确定的 u，
不是各自反馈的粒子近似系统，也不是修改 NS 的黏性。

令 dX^m=u(t,X^m)dt+sqrt(2nu)dW^m，A^m=(X^m)^{-1}，
J^m_ai=partial_i A^m_a，V^m_a=u_{0,a}(A^m)。
a 是材料分量，i,j,k 是空间指标。每组边缘分布与单噪声相同：
M=E J^m，N=E V^m。设

\[
 H_{\rho,i}(t,x,y)=\mathbb E\sum_aJ^1_{ai}(t,x)V^2_a(t,y),
 \qquad C_\rho=H_\rho-M(x)^TN(y).
 \tag{CG.1}
\]

空间微分、期望和 Itô 乘积在固定光滑紧区间上合法：
流和逆流的空间导数有由该区间 u 的导数范数控制的路径一致界。
这些界不是仅由初始能量控制、也没有被延伸到 T_*。

由逆流的 Itô 方程，重复指标求和，

\[
\begin{split}
 dJ^1_{ai}
 &=\{-u_j(x)\partial_{x_j}J^1_{ai}
       +\nu\Delta_xJ^1_{ai}-(\partial_{x_i}u_j(x))J^1_{aj}\}\,dt
       -\sqrt{2\nu}\,\partial_{x_k}J^1_{ai}\,dW^1_k,\\
 dV^2_a
 &=\{-u_j(y)\partial_{y_j}V^2_a+\nu\Delta_yV^2_a\}\,dt
       -\sqrt{2\nu}\,\partial_{y_k}V^2_a\,dW^2_k .
\end{split}
\tag{CG.2}
\]

两噪声负号的乘积给出正交叉变差
2nu rho sum_k partial_xk J^T partial_yk V。
定义不含零阶矩阵项的算子

\[
 L_\rho=\partial_t+u(x)\cdot\nabla_x+u(y)\cdot\nabla_y
       -\nu(\Delta_x+\Delta_y+2\rho\nabla_x\cdot\nabla_y).
 \tag{CG.3}
\]

于是

\[
\begin{split}
 (L_\rho+G(x)^T)H_\rho&=0,& H_\rho(0,x,y)&=u_0(y),\\
 (L_\rho+G(x)^T)C_\rho
 &=2\nu\rho\sum_k(\partial_kM(x))^T(\partial_kN(y)),
 & C_\rho(0)&=0 .
\end{split}
\tag{CG.4}
\]

证明：逐分量应用 (CG.2) 的乘积公式并取期望。
边缘方程是 D_u M+MG=0、D_u N=0，其中 D_u=partial_t+u.grad-nu Delta。
M(x)^TN(y) 在 L_0+G(x)^T 下为零；
L_rho 相比 L_0 多出的负混合导数恰给右侧的相反数，作差即得 (CG.4)。

rho=0 时独立性给 H_0=M^TN、C_0=0。
rho=1 时两噪声可取完全相同，H_1(t,x,x) 才是原始 Weber 均值，
且 u=P[H_1(t,x,x)]，P 为周期 Leray 投影。
rho<1 的 H_rho 不是原始输出；改变相关性仅定义辅助耦合。

## 5. 相对扩散与物理对角不能混同

在局部线性变量 c=(x+y)/2、r=x-y 下，

\[
 \Delta_x+\Delta_y+2\rho\nabla_x\cdot\nabla_y
 =\frac{1+\rho}{2}\Delta_c+2(1-\rho)\Delta_r.
 \tag{CG.5}
\]

这里只用 c,r 表示微分恒等式，不把它们误当成两个独立标准周期坐标。
rho=1 仅使相对扩散消失。令 h_rho(x)=H_rho(x,x)，链式法则给

\[
 (D_u+G^T)h_\rho
 =-2\nu(1-\rho)
   \left[\sum_k\partial_{x_k}\partial_{y_k}H_\rho\right]_{y=x}.
 \tag{CG.6}
\]

因此 rho=1 的对角方程有完整的 nu Delta。
rho=0 时 (CG.6) 正好是
(D_u+G^T)(M^TN)=-2nu sum_k(partial_kM)^T partial_kN，
独立核对了负号。对 c_rho(x)=C_rho(x,x) 则有

\[
 (D_u+G^T)c_\rho
 =2\nu\rho\sum_k(\partial_kM)^T(\partial_kN)
 -2\nu(1-\rho)
  \left[\sum_k\partial_{x_k}\partial_{y_k}C_\rho\right]_{y=x}.
 \tag{CG.7}
\]

同噪声端点的源与文献协方差方程一致。
对每个固定光滑 [0,T]，rho→1 可以借流的稳定性恢复原耦合；
这里既未证明也未假定与 T→T_* 一致的临界估计。
小系数 (1-rho) 不允许未经控制直接丢弃混合导数。

## 6. 一个不随相关参数发散的条件能量估计

直接取 (CG.4) 第一式的六维空间 L2 内积，输运因散度零消去，得

\[
 \frac12\frac d{dt}\|H_\rho\|_2^2+\nu Q_\rho
 =-\int_{\mathbb T^3\times\mathbb T^3}H_\rho^TS(x)H_\rho,
 \quad
 Q_\rho=\|\nabla_xH_\rho\|_2^2+\|\nabla_yH_\rho\|_2^2
      +2\rho\langle\nabla_xH_\rho,\nabla_yH_\rho\rangle .
 \tag{CG.8}
\]

不能把右侧视为非正，也不需要先用会退化的全六维强制性常数。
改用合法的周期自同构 z=y、r=x-y，逆变换为 x=z+r、y=z，
Jacobian=1，且 partial_z=partial_x+partial_y。
写 a=grad_x H、b=grad_y H，则

\[
 Q_\rho=\frac{1+\rho}{2}\|a+b\|_2^2
        +\frac{1-\rho}{2}\|a-b\|_2^2
 \ge\frac12\|\nabla_zH_\rho\|_2^2 .
 \tag{CG.9}
\]

固定 r，S(z+r) 的 L2_z 范数等于 g(t)=||S(t)||_2。
先在三维 z 上用周期 Gagliardo--Nirenberg，再对 r 用 Hölder：

\[
\begin{split}
 \left|\int H_\rho^TS(x)H_\rho\right|
 &\le Cg\,\|H_\rho\|_2^{1/2}\|\nabla_zH_\rho\|_2^{3/2}
       +Cg\,\|H_\rho\|_2^2\\
 &\le\frac{\nu}{4}\|\nabla_zH_\rho\|_2^2
       +C(\nu^{-3}g^4+g)\|H_\rho\|_2^2 .
\end{split}
\tag{CG.10}
\]

其中逐 r 的乘积是
||H(.,r)||_2^(1/2)||grad_z H(.,r)||_2^(3/2)；
r 上 Hölder 指数 4 与 4/3 给出第一行。Young 指数 4/3 与 4
给出第二行。因而

\[
 \frac d{dt}\|H_\rho\|_2^2
   +\frac{\nu}{2}\|\nabla_zH_\rho\|_2^2
 \le C(\nu^{-3}\|S(t)\|_2^4+\|S(t)\|_2)\|H_\rho\|_2^2 .
 \tag{CG.11}
\]

常数不随 rho→1 发散，初值范数为 ||u_0||_2。
在有界时间内，低阶 g 项可由基本能量和时间 Cauchy--Schwarz 支付；
g^4 的积分尚未支付。S 属于 L4_t L2_x 是临界应变输入，
不是基本能量给出的 L2_t L2_x。
把先前粗估计中的 (1-rho)^(-3) 当作必然障碍是不正确的。

(CG.11) 的六维范数自身也不控制 r=0 的迹。
例如 f_epsilon(r)=epsilon^(-3/2)f(r/epsilon)，f 为支撑在小球且
f(0)≠0 的光滑函数；H_epsilon(z,r)=v(z)f_epsilon(r)。
其 H 和 grad_z H 的 L2 范数保持有界，对角值却随 epsilon→0 增大。
这只是函数空间的迹控制反例，不是由同一 NS 解实现的 H_rho 族。
若直接对 rho=1 的三维对角方程做能量估计，也会得到上述未支付的
四次应变成本；不能把六维迹问题说成所有对角方法的不可能性。

## 7. 当前价值与下一项检查

本轮排除了两种错误简化：旧时钟恒等式重命名，以及把相对扩散退化
直接当成物理对角不正则。也给出了统一 rho 的条件估计 (CG.11)。
这些是预检与错误修正，没有降低合同 G 或 R.216--217 的任何输入。

下一项仅保留一个有界问题：在原始同噪声 rho=1 上，
把完整 Leray 投影与 M^TN、C_1 的输运—应变配对一起展开。
先核对梯度部分的精确消去，确定剩下的真实项；
再问能否用已支付的能量和 NS 演化把其中某一项控制在足以接入 G
的尺度上。不得把 ||S||_L4L2、形变最大值或等价的临界速度范数
换名后当成更弱假设；不得丢弃周期压力或非局部投影交换项。

这只是待筛选的问题，不是已认可的新机制。
进入下一层推导前须先查已有 Eulerian--Lagrangian 磁化变量/投影恒等式，
确认不是文献中 NS 的等价改写。如果展开只返回原方程或原来同等强度的
临界输入，记录精确对应并停止该支线，不自动制作更多相邻变体。

本轮没有数值实验、DGX 任务、科学附图或新读者 PDF。
没有创建发布冻结，也没有重复发送上一 release。
固定发布任务继续独立承担网站工作；本研究任务不查询或报告其状态。
