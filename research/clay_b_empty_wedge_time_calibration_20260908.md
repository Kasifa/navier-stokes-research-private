# 开楔反例的初端演化：压力与完整耗散的累计量

2026-09-08。EWT，PRIVATE_CORE。EWP 的内部时间范围校准，不另列研究小节或新 release。范围内推导；没有新的三维临界估计，一般 NS / Clay 仍 OPEN / NOT CLAY。

EWP 的初始压力配对虽随内核缩小而对数增长，但在这族初值的真实演化上，初端的压力绝对累计与完整梯度耗散都一致趋零。证明使用这族初值的统一速度上界和梯度空间平移模量；这些条件不能自动移到任意候选奇异终端。

本稿补全上一节的时间范围检查。它没有量化压力符号能保持多久，也不把静态下界乘以固定时间。已有 EWP 反例、GD 完整平衡和静态黏性成本均保持原样。

## 1. 同一解、共同短时窗和目标

取 EWP.4–13 的固定角函数与截断，初值记为 u_delta^0，梯度 G_delta^0。先在普通体积 T²_(2pi) 中演算，再沿 z 提升到 T³_(2pi)。每个 delta 使用从这个初值出发的原无外力 NS 解 u_delta(t)，固定 nu>0。

记 G=grad u、q=|G|_F、B0=G/q（零处取零），H 为同一速度的零均值规范压力 Hessian，并记
\[
Q_\delta(t)=\int |G_\delta(t)|,\quad
I_\delta(t)=\int B_0(G_\delta):(G_\delta^2+H_\delta),\quad
\ell_\delta(t)=1+\log_+\frac1{\delta+\sqrt{\nu t}}.
\tag{EWT.1}
\]
固定周期长度已给对数的空间参考单位；不声称该表达本身缩放不变。下文常数可依赖固定剖面、周期胞和 nu，但不依赖 delta 或 h。限制 delta 足够小，并选一个与 delta 无关的 T>0。

将证明，对 0<h≤T，
\[
\int_0^h\!\!\int |B_0:H_\delta|
\le\int_0^h\|H_\delta(t)\|_1dt
\le Ch\ell_\delta(h)
\le C_\nu h(1+|\log h|),
\tag{EWT.2}
\]
\[
\nu\mu_{G_\delta}(\mathbb T^2\times(0,h))
\le C_\nu\sqrt h(1+|\log h|).
\tag{EWT.3}
\]
mu_G 是 GD.4 中完整的非负正则化极限，包含 q=0 上的全部贡献。二维块沿演化保持，故 B0:G² 处处为零，EWT.2 同时控制 integral_0^h |I_delta|。

## 2. 初始剖面确实提供了哪些统一条件

EWP 的基旋流在主环与径向无关，内核基速度是固定剖面的缩放，外层固定；探针是delta倍的固定光滑场。由这些实际公式，对横截面到原点的距离 r，有
\[
\|u_\delta^0\|_\infty\le M,\quad
|G_\delta^0(x)|\le C\left(1+\frac1{r+\delta}\right),\quad
|\nabla G_\delta^0(x)|\le C\left(1+\frac1{(r+\delta)^2}\right),\quad
\|G_\delta^0\|_1\le K_1.
\tag{EWT.4}
\]
M≥1、K1和C固定。内层的一、二阶速度导数分别按 delta^-1、delta^-2 缩放；主环按 r^-1、r^-2 缩放；原点内部和外部光滑截止保留。因此这些界不是从有限能量推测而来。三维解释中的 r 是到 z 轴的横截面距离，不是到一个三维点的距离。

此外，EWP.22–23 的已完成计算包含 ||Delta G_delta^0||1≤C/delta。这里只使用这个已知界，不重复认领静态成本。EWT.4 给每个固定 1<p<2 的统一 W^{1,p} 速度界，但本族没有统一正 Hölder 模量：取使主环基速度不同的两个固定角，在r=sqrt(delta)上比较；位置间距趋零，速度差仍趋于非零常数。

## 3. 共同光滑寿命不能取自非统一 H1 范数

设 K_sigma 是固定周期胞的热核。对 0<sigma≤1，周期高斯求和及其导数给 ||grad^j K_sigma||1≤C_j sigma^(-j/2)。大 sigma 时，所有非零阶导数由 Fourier 级数指数衰减。因空间导数消去常模，Leray 核有分布恒等式
\[
e^{\sigma\Delta}\mathbb P_{ij}\partial_k
=\delta_{ij}\partial_k e^{\sigma\Delta}
 +\int_\sigma^\infty\partial_i\partial_j\partial_k e^{s\Delta}\,ds.
\tag{EWT.5}
\]
对积分用 ||grad³K_s||1≤Cs^-3/2（小s）和大s的指数衰减，得到
\[
\|e^{\sigma\Delta}\mathbb P\operatorname{div}F\|_j
\le C\sigma^{-1/2}\|F\|_j,\qquad j=1,2,\infty.
\tag{EWT.6}
\]
这里证明的是平滑后的核界，没有假定 P 本身在 L1 或 L∞ 有界。

对各自经典光滑解的 mild 式，令 U_delta(t)=sup_(s≤t)||u_delta(s)||∞，便有
\[
U_\delta(t)\le M+C\sqrt{t/\nu}\,U_\delta(t)^2.
\tag{EWT.7}
\]
选 T≤min{1,1/nu,c nu/M²}，c足够小。由连续性与首次达到2M的反证，U_delta(t)≤2M，在原最大光滑寿命与T的较小者之前成立。

此处使用经典周期速度 L∞ 延拓准则：最大光滑寿命有限则速度时空 L∞ 无界。实际核对的来源是 [Tao 254A Notes 1，Proposition 39 和 Corollary 40](https://terrytao.wordpress.com/2018/09/16/254a-notes-1-local-well-posedness-of-the-navier-stokes-equations/)，全部陈述及证明；不认证整篇讲义。该准则与 EWT.7 排除任意 delta 的寿命在T之前结束，故得到共同真实光滑窗。没有从 EWP 发散的 H1 范数取一个共同寿命，也没有调用三维大数据全局存在。

二维解的三维提升满足原三维方程；唯一性保持这一结构。以下的初端核估计并不需要额外调用二维涡量最大原理。

## 4. 热卷积的内核尺度由真实非线性估计保留

由 EWT.4 与二维高斯核，在固定横截面上
\[
|e^{\sigma\Delta}G_\delta^0(x)|
\le C\left(1+\frac1{r+\delta+\sqrt\sigma}\right),\qquad
\|e^{\nu t\Delta}G_\delta^0\|_2\le C\sqrt{\ell_\delta(t)}.
\tag{EWT.8}
\]
点态卷积界可直接分区核查。写 a=sqrt(sigma)。若 delta≤a，则先将源控制为1/r；r≤2a时高斯缩放给C/a，r>2a时分 |y|<r/2 与补集，分别用高斯尾 Cr/a² exp(-cr²/a²)≤C/r 和源界2/r。若 delta>a，分 |x-y|≤(r+delta)/2 与补集；前者分母至少(r+delta)/2，后者用 delta^-1 exp(-c(r+delta)²/a²)≤C/(r+delta)。周期像及远离内盘的固定部分一致有界。平方后按二维 r dr 积分即得第二界。

这只是热项；真实速度还包含非线性。对每个空间导数逐项交换 mild 式，得到精确表达
\[
\partial_k u(t)=e^{\nu t\Delta}\partial_k u^0
-\int_0^t e^{\nu(t-s)\Delta}\mathbb P\operatorname{div}
\big((\partial_k u)\otimes u+u\otimes(\partial_k u)\big)(s)\,ds.
\tag{EWT.9}
\]
于是 EWT.6–8 给 y_delta(t)=||G_delta(t)||2 满足
\[
y_\delta(t)\le C\sqrt{\ell_\delta(t)}
 +\frac{CM}{\sqrt\nu}\int_0^t(t-s)^{-1/2}y_\delta(s)\,ds.
\tag{EWT.10}
\]
对0<s≤t，有 delta+sqrt(nu s)≥sqrt(s/t)(delta+sqrt(nu t))，所以
\[
\ell_\delta(s)\le\ell_\delta(t)+\tfrac12\log(t/s),\qquad
\int_0^t(t-s)^{-1/2}\sqrt{\ell_\delta(s)}\,ds
\le C\sqrt t\sqrt{\ell_\delta(t)}.
\tag{EWT.11}
\]
最后一个常数有限，因为 integral_0^1 (1-z)^(-1/2)sqrt(log(1/z)) dz 有限，且 ell≥1。对固定delta，光滑性保证加权上确界有限；再缩小仅依赖M、nu的共同T，在 EWT.10 中吸收该上确界，得到真实解而非热轨道的
\[
\|G_\delta(t)\|_2^2\le C\ell_\delta(t),\qquad 0≤t≤T.
\tag{EWT.12}
\]

## 5. 完整压力与梯度初端差

使用已冻结 GD.3–5、SE.2–4 的固定周期 Hardy 压力接口 ||H_delta(t)||1≤C_H||G_delta(t)||2²。三维提升后该界除以共同2pi因子，同样给二维界；并非对任意L1源使用Riesz的L1有界性。

EWT.11 还给 integral_0^h ell_delta(t)dt≤h ell_delta(h)+h/2。因此 EWT.12 直接证明 EWT.2，无需压力符号抵消，也未丢失非局部压力。

完整耗散还需端点。EWT.9 的 L1 版与 EWT.6 同样吸收，给
\[
\sup_{\delta,t≤T}\|G_\delta(t)\|_1\le CK_1,\qquad
\|G_\delta(h)-e^{\nu h\Delta}G_\delta^0\|_1
\le CMK_1\sqrt{h/\nu}.
\tag{EWT.13}
\]
第一界也可由旧GD预算得到，不另称新成果。

EWT.4 的分层导数界给这族特有的平移模量：对小z，
\[
\|G_\delta^0(\cdot-z)-G_\delta^0\|_1
\le C|z|(1+\log_+|z|^{-1}).
\tag{EWT.14}
\]
若delta≥|z|，用 ||grad G_delta^0||1≤C(1+log_+(1/delta)) 和均值公式。若delta<|z|，距原点3|z|以内及其平移的梯度质量为O(|z|)；外区连线远离原点，用 |grad G|≤C(1+r^-2) 积分，得到 C|z|(1+log(1/|z|))。单有梯度点态上界而没有分层导数信息，不足以这样推断。

将 EWT.14 对周期高斯积分，使用有限的高斯一阶及对数矩，得到热初端模量。另一方面，热半群L1收缩与已知 ||Delta G_delta^0||1≤C/delta 给线性的时间界。合并为
\[
\|e^{\nu h\Delta}G_\delta^0-G_\delta^0\|_1
\le C\min\left\{\frac{\nu h}{\delta},
\sqrt{\nu h}\left(1+\log_+\frac1{\sqrt{\nu h}}\right)\right\}.
\tag{EWT.15}
\]

## 6. 两切片与全部零集耗散

对每个delta的闭光滑区间，GD正则化平衡给
\[
Q_\delta(h)+\nu\mu_{G_\delta}(\mathbb T^2\times(0,h))
=Q_\delta(0)-\int_0^h I_\delta(t)\,dt.
\tag{EWT.16}
\]
周期输运和空间Laplacian项在完整积分后为零；初末切片均保留。mu_G包含零集，不替换成只在q>0上的经典密度。由 |Q(h)-Q(0)|≤||G(h)-G(0)||1，EWT.2、13、15给
\[
\begin{split}
\nu\mu_{G_\delta}(\mathbb T^2\times(0,h))\le{}&
C\min\left\{\frac{\nu h}{\delta},
\sqrt{\nu h}\left(1+\log_+\frac1{\sqrt{\nu h}}\right)\right\}\\
&+CMK_1\sqrt{h/\nu}+Ch\ell_\delta(h).
\end{split}
\tag{EWT.17}
\]
这证明 EWT.3。不能仅从压力累计小就跳到这一步。三维提升时Q、I及mu均乘2pi，估计只改变共同常数。

在内核扩散时间 h_delta=delta²/nu≤T，上式具体给
\[
\int_0^{h_\delta}|I_\delta(t)|dt
\le C\nu^{-1}\delta^2(1+\log\delta^{-1}),\qquad
\nu\mu_{G_\delta}((0,h_\delta))\le C_\nu\delta.
\tag{EWT.18}
\]
在任意固定0<tau<T上，EWT.12则使压力Hessian的L1范数在[tau,T]内一致有界。故初始log(1/delta)大小不可能在固定正龄窗持续；这不是精确寿命或下界，也没有证明任意固定阈值的配对不再发生。

## 7. 不把方向初导数当成持久性证明

在零角区内部且2delta<r<R，初始G=delta A为空间常矩阵，A=diag(1,−1)，grad G=Delta G=0。原梯度方程的准确初导数为
\[
G_t(0)=-H_0-\delta^2I_2=-H_0^{\rm tf},\qquad
(B_0)_t(0)=-\frac{\Pi_{A/\sqrt2}^{\perp}H_0^{\rm tf}}{\delta\sqrt2}.
\tag{EWT.19}
\]
这里 H0^{tf}=H0+delta²I2，因为trace H0=−2delta²；Pi垂直投影在矩阵Frobenius内积下定义。不能漏掉原G²项。由此 (B0)_t:H0=−|Pi_perp H0^{tf}|²/(delta sqrt2)≤0；压力造成的方向变化并不自动使原配对衰减。求配对时间导数还含 B0:(H0)_t，且此逐点初导数没有随delta一致的余项，不能推断在某个指定的delta依赖时间尺度上的符号下界。EWT.2–18的证明不使用这种未证持续性。

定性的短区间则已有保证：EWP.20 给该正初值解的 I(0+) = I(u_delta^0)−J0，J0≥0，而 EWP.18 的 I(u_delta^0) 为负的对数阶。故每个充分小delta都有某个 s_delta∈(0,T]，使同一解在0<t<s_delta内满足 I_delta(t)≤−c log(1/delta)。两个L2范数的初端连续性同时保留其原上界；s_delta可随delta缩小。s_delta与前述内核时间h_delta是不同记号；这里没有给出s_delta的速率或统一下界，不能据此与delta²/nu比较。

## 8. 对策略的实际结论

GD已有有限累计预算，本稿只补出EWP族的初端一致趋零模量。相应量词来自统一速度上界、具体梯度平移模量、二维横截面热积分和同一解的非线性估计；没有从任意有限能量轨道推出这些输入。对一般三维流，mild核和完整梯度平衡仍可用，但二维惯性消失、横截面对数及涡量无伸长不能照搬。

统一W^{1,p}甚至速度Lipschitz上界本身也不给梯度耗散的统一初端模量。作为端点逻辑核对，原NS精确热剪切 u_n=n^-1 exp(-nu n²t)sin(ny)e1 的压力与惯性源为零；其Q_n(t)=16pi² exp(-nu n²t)。在t_n=(nu n²)^-1，完整 nu mu_G=16pi²(1-exp(-1))，不趋零。它只说明还需梯度空间连续性，不另计为新反例小节。

因此停止从EWP的初端对数族中推断一般终端障碍，也不继续做角宽、探针或热时间变体来增加版本。含原耗散的普遍带符号估计仍未解决；PF的指定中心好尺度仍缺动力学输入。下一步回到这个缺口，先选择一个能在同一候选终端重启、且不预设共同速度L∞或梯度平移模量的具体跨尺度命题；候选目前未选定、未证明，不用新的初端范数改写替代它。

本稿推导由主任务完成，good_scale_route_comparison独立核对热卷积、带权Volterra与黏性因素；variable_reference_check核查角区初导数，ma_freeze_review核查旧平衡、端点及适用范围。实际文件审读另记，模块回复不等于稿件通过。普通来源核对仅使用已列局部理论；没有Deep Research全面查新、仿真、DGX、数值证书、科学图、英文翻译或读者HTML/PDF。完整记录私有保存，EWP移交不重发。
