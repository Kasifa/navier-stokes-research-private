# 调制纯方位外环的非作者解析审查

2026-09-08，PRIVATE_CORE。结论：**PASS — 仅限 MS.1 精确局部轨道合同下的 MS.2 / MP.10。** 未发现阻断问题或必须修改的排版项。

我不是 CONTRACT.md、PROOF.md 或 INDEPENDENT_DERIVATION.md 的作者，但参与了前期问题建议、历史筛选和角分量先算，因此本审查**不是盲审**。本轮全文实读三份实际文件，先独立核主证明，再全文对照另一作者的独立推导。该作者声明未读根 PROOF；其实际文本从合同及旧来源重推了完整点公式。这里不把我自己的先前筛选或同一推导的重读计作额外独立证书，不声称真人同行评审或形式化证明。

## 1. 固定物理坐标与全部尺度

从 \(y=Q^T(x-c)/\ell\)、\(Q'=QK\)、\(K^T=-K\) 在固定物理 x 求导，得到
\[
y_t=-Q^Tc'/\ell-Ky-(\ell'/\ell)y.
\]
这与 MP.3、ID.2 相同。先求旋度 \(\omega=(A/\ell)Q\Omega\)，再固定 x 微分，必须保留
\[
\left(A'/\ell-A\ell'/\ell^2\right)\Omega
+(A/\ell)\{K\Omega-[(b+Ky+\lambda y)\cdot\nabla]\Omega\}.
\]
MP.4 与 ID.3 完全等价。它们求的是 \(Q^T\partial_t\omega\)，不是移动点上的全导数，也不是先取 \(Q^T\omega\) 再忽略基运动。只出现一阶调制导数；C¹ 正幅度、尺度及 C¹ proper rotation 足够。

空间变换的尺度亦逐项正确：黏性旋度为 \(A\ell^{-3}Q\Delta\Omega\)，对流本身为 \(A^2\ell^{-1}Q[(W\cdot\nabla)W]\)，再取旋度得到 \(A^2\ell^{-2}\)。不存在遗漏外层旋度的逆尺度。

## 2. 方位基微分、转轴和完整角周

原右手基满足 \(e_r\times e_\theta=e_z\)、\(\partial_\theta e_r=e_\theta\)。由旧 W 直接核得
\[
\Omega=F e_r+G e_z,\quad
F=-w_z=4r(z-3/2)h''(s),\quad
G=(rw)_r/r=4h'(s)-4r^2h''(s).
\]
因此恒定空间向量 b 的输运只有基的角导数贡献方位分量：
\(e_\theta\cdot(b\cdot\nabla)\Omega=b_\theta F/r\)。

令 \(Ky=\kappa\times y\)。两项分别是
\[
e_\theta\cdot K\Omega=\kappa_zF-\kappa_rG,
\qquad e_\theta\cdot Ky=\kappa_zr-\kappa_rz.
\]
于是其差为 \(\kappa_r(zF/r-G)\)。此处必须是体坐标全 z，不是 \(z-3/2\)：转轴生成元以所定义的坐标原点为中心，形状球心的运动已经包含在 Ky 中。主稿使用全 z，独立稿也专门核明这一点。

平移项与转轴项不逐点为零；沿同一 r、z 的整圆，F、G 为常数，而 \(b_\theta\)、\(\kappa_r\) 的均值为零。轴向自转的 \(\kappa_zF\) 在求平均以前就相消。这个证明覆盖任意有限的调制速率，不依赖小性。幅度及尺度项涉及 \(\Omega\)、\((r\partial_r+z\partial_z)\Omega\)，本身没有方位分量。

因此 MP.7 成立。ID.10 给出的更完整点公式，恰是相同的对流源加上上述两项第一角谐波；它独立支持主稿的角平均，未引入新的假设或删除单点运动项。

## 3. 周期管、完整压力和黏性

合同要求在包含完整移动圆周的**开时空管**内，真实总速度精确等于调制 W。这允许先在邻域求空间与固定 x 的时间导数，再代入圆周；仅有圆周取值或单个时间快照不足。原圆周与轴分离且在旧支撑球内：\(r=1/40\)、\(z-3/2=1/40\)，故 \(s=1/800>0\)、球心距离 \(\sqrt2/40<1/20\)。所有角点使用同一光滑形状。

局部周期提升及相容的邻域等式足以作上述求导；不要求把 Q 延拓成整个环面的对称或使 \(Q\mathbb Z^3=\mathbb Z^3\)。如果某组参数没有合同所要求的相容时空管，其表示本身不满足前提，本结论并不替它建立全域周期拼接。

完整周期压力只通过 \(\operatorname{curl}\nabla p=0\) 精确消去。管外速度及其压力没有被删除，也不要求压力轴对称。向量 Laplacian 的径向项含正确的 \(-F/r^2\)，轴向项为标量柱坐标 Laplacian；它仍经向，所以原黏性1的方位配对逐点为零。这是完整黏性项的分量恒等式，不是 Euler 近似。

## 4. 正源、结论与未覆盖范围

旧纯方位对流给
\[
(W\cdot\nabla)W=-w^2e_r/r,
\quad q=-\partial_z(w^2/r)=16r(z-3/2)h'(s)h''(s).
\]
旧圆周上 \(16r(z-3/2)=1/100\)，且 \(h'(1/800)>0\)、\(h''(1/800)>0\)。所以三稿的同一平均式严格为
\[
\frac{1}{2\pi}\int_0^{2\pi}(Qe_\theta)\cdot\operatorname{curl}_x\mathcal R\,d\theta
=\frac{A^2}{\ell^2}q_*>0.
\]
左侧绝对值至多是圆周上残差旋度的 Euclidean 范数上确界，主稿附带的下界没有漏常数。真实 NS 令残差恒为零；任取非空开区间内的时刻即矛盾。不需要给时间段最小长度或 A 的统一正下界。

接受的新增范围是旧纯方位形状的任意 C¹ 有限维调制精确轨道。旧证明允许固定重标形状的小 C³ 误差而限制连续持留；新证明允许任意调制但要求零误差，二者不是包含关系下的全面加强。

本结论不排除单个时刻经过该形状；这样的快照没有给定时间导数。它也不覆盖近似调制轨道、另加平移速度或应变等背景、经向/非轴对称速度、局部角弧、再进入次数或全时稳定性。任意调制速度与非零误差的乘积未有统一预算，不能据此自动给近似持留定理。没有证明任何给定初值到达此族、全局正则、奇性或可迭代压力再生。

## 5. 实际审查和字节绑定

所有等式及旧小整数、符号在本文手工核对。工具只用于文本读取、SHA 和写本文；未运行科学程序、读取数组、扫描参数、选新初值、制作图档或执行 Git。对旧证明只复用本项需要的 W、q_* 和适用范围，不重审旧包全部计算证据。

| 实际输入（相对 research/reverse/） | SHA256 |
|---|---|
| modulated-swirl-screen/CONTRACT.md | 147e3a624a620f71792f9610fa779c09ed5d877c791fda922d0ca445ab41cf02 |
| modulated-swirl-screen/PROOF.md | 25d5bff7b2a96a9562af373cde2929a674acf1ee1cdaea3311785158e326142a |
| modulated-swirl-screen/INDEPENDENT_DERIVATION.md | 868bdf7eaed4bf6170759e6e9434b43f62c83e7a3c393c7c6e3613b84da23706 |
| exterior-pressure/JOINT_TEST_PROOF.md | 9d0100f62ec6ef25ef2552348120d2b7b1e802aba49167bf4115edad02a3cd91 |
| exterior-pressure/RESCALED_EXIT_PROOF.md | e96f1bce6d2076d560191211e208bd43f33e0db2d5c21de8abc6dfd31b361e78 |
| exterior-pressure/RESCALED_EXIT_REVIEW.md | d9b29618ec836e0d3ea3a63fde0888db59add6b289dc7900c84a0e748601a0d6 |
| MECHANISM_NEXT_QUESTION_SCREEN.md | dcf80554cab4004eb69c0ea12452d5a500185c02b7907581fafc7ad75f85f17e |

前三份全文实读。后三份旧外压来源及自有筛选在紧邻任务已按相应范围读过，本轮复用同一字节；自有筛选只记录前期参与和历史差别，不计作独立证明来源。
