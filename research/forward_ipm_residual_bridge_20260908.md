# 从 IPM 终端收敛到 NS 残差：同一速度轨道不能直接移植

2026-09-08。PRIVATE_CORE，内部接口核算和策略衔接，不是独立成果冻结。
基准提交：`5ecb99019944d3c93fa229cef69ccc71240cc937`。
分类：外部主定理按原稿引用（LITERATURE）；下述解析推论在所列假设下成立
（LOCAL PROOF / CONDITIONAL ON THE CITED TRAJECTORY）。一般 NS、Clay 仍 OPEN / NOT CLAY。

本次得到一个具体限制。IPM 原稿的密度在每个固定 0<η<1 的 Hölder 指数下收敛，
使其 Darcy 速度在终端前一致有界；速度梯度却发散。将这一条速度轨道原样放入
固定正黏性的 NS，所需的投影残差不属于任何 Lq_t L∞_x，2<q≤∞。
因此不能用终端仍光滑的 NS 外力实现这种直接移植，更不能令它成为无外力 NS。
这是经典热核梯度估计的限定应用，不主张新的正则性准则或原创性。

## 1. 暂停点与本次完成范围

用户先要求完成未收尾小节并建立旧路线到优化路线的中间路径，随后暂停，
现在明确恢复。本次接回这个有界任务，不启动无限参数扫描或另一项构造。

| 对象 | 核对后的状态 | 本次处理 |
|---|---|---|
| SPI 第 7–10 节，式 SPI.12–20 | 已在基准提交完成并审读。尾矩极限等于能量缺陷，缺陷消失未证。 | 读回全文，保留原文；不把 OPEN 当成小节尚未收尾。 |
| TG 独立冻结 | 科学源 `0d916d57db8d69e67cd253a1f3e5ce07bd8ae1a7`；冻结 `93965a9c3cf8ccb3e61aad637a2f736c8d0fd5fd`。 | 保持最后独立冻结身份，不重复移交。 |
| 双点候选去重 | 暂停前只启动检查，随后中断；未形成可接纳的命题、证明或计算。 | 不作为已开展的数学小节补数，也不在本轮复活。 |
| 外部 IPM 与正向路线的接口 | 暂停时核验回执已到，但主任务尚未整理、审读成稿和提交。 | 本文给出原稿前提、残差恒等式、完整证明和策略调整。 |

## 2. 只使用原稿的准确轨道前提

来源为 Alpöge、Buckmaster、Coiculescu 的
*Extending the Córdoba-Martínez-Zoroa IPM Blow-Up to Uniformly Space-Time Smooth Forcing*，
本地固定 PDF 第 3 页 Theorem 2.1 及式 (1)–(4)。不假定已经重证整篇构造。
令 T²=(R/2πZ)²，Fourier 系数用胞体积平均。Darcy 算子记为 T：
\[
 \widehat{T\rho}(k)=2\pi\left(\frac{k_1k_2}{|k|^2},
                    -\frac{k_1^2}{|k|^2}\right)\widehat\rho(k),\quad k\ne0,
 \qquad \widehat{T\rho}(0)=0.
 \tag{IB.1}
\]
它输出无散向量。原稿给出一组固定光滑初值和闭时空光滑的标量力
F∈C∞([0,1]×T²)，使同一条轨道满足
\[
 \partial_t\rho+v\cdot\nabla\rho=F,\qquad v=T\rho,
 \qquad \rho\in C^\infty([0,b]\times\mathbb T^2)\quad(b<1).
 \tag{IB.2}
\]
其初值和每时的力均奇、零均值。存在一个相同的 ρ*，使
\[
 \rho(t)\to\rho_*\text{ 于每个 }C^\eta(\mathbb T^2),\ 0\le\eta<1,
 \qquad \lim_{t\uparrow1}\|D_xv(t)\|_\infty=\infty.
 \tag{IB.3}
\]
原稿还给密度梯度发散；本文使用的是直接声明的速度梯度发散，
并非从密度梯度发散单独推断。下述论证实际上只需速度梯度的 limsup 发散。

### 固定一个正指数，就有速度的一致有界性

取 η=1/2，不需要令 η 趋近 1。这里不用不成立的 T:L∞→L∞。
用固定平滑周期 Littlewood–Paley 分解 Δ_j。对 j≥0，壳乘子
TΔ_j 的核可写为一个固定光滑紧支撑符号的逆 Fourier 变换的缩放及周期化，
故其 L1 范数一致有界。为应用到 Δ_j f，在稍大的频壳插入恒为一的截止即可。
频壳核零积分与 Hölder 差商给
\[
 \|\Delta_j f\|_\infty\le C_\eta 2^{-j\eta}\|f\|_{C^\eta},
 \qquad \|T\Delta_j f\|_\infty\le C\|\Delta_j f\|_\infty.
\]
有限低频部分同样有界，零模由 IB.1 单独置零。对壳求和得到
\[
 \|Tf\|_\infty\le C_\eta\|f\|_{C^\eta},\quad 0<\eta<1.
 \tag{IB.4}
\]
只需要这个映射结论，不额外依赖完整的 Hölder 空间乘子定理。
IB.3 在终端附近提供 C1/2 共同界，紧前缀光滑性覆盖剩下的时间。
因此 v(t) 在 L∞ 收敛到 Tρ*，且 sup_(t<1)||v(t)||∞<∞。

## 3. 固定正黏性所要求的准确残差

作平凡三维嵌入 U(x₁,x₂,x₃,t)=(v₁,v₂,0)，∂₃U=0。
无散性、L∞ 范数和梯度上确界保持；这不是新增一个三维动力学构造。
对每个固定 ν>0，定义完整三维 Leray 投影 P₃ 下的残差
\[
 R_\nu=\partial_tU-\nu\Delta_3U
              +P_3\operatorname{div}(U\otimes U).
 \tag{IB.5}
\]
它是无散的，并在每个闭前终端区间光滑。P₃ 在 k₃=0、第三分量为零的
子空间上限制为二维 P₂；P₂T=T。由 IB.2 逐项计算，其前两分量为
\[
 r_\nu=TF+
 P_2\big[(v\cdot\nabla)T\rho-T((v\cdot\nabla)\rho)\big]
       -\nu\Delta_2v,\qquad R_\nu=(r_\nu,0).
 \tag{IB.6}
\]
该恒等式保留交换子、黏性项和全部投影。若以 Rν 本身作为 NS 力，
压力须重新选择 ∇π=−(I−P₃)div(U⊗U)，不能沿用 Darcy 压力。
若改用任意非无散的物理力 f，则必要关系是 P₃f=Rν。

## 4. 有界速度和可控投影力不能支持梯度爆破

**引理。** 固定 ν>0 和 0<a<T*<∞。设 U 是 T³ 上无散向量场，
在每个 [a,b]、b<T* 上光滑，满足 IB.5 的投影 NS 方程，并且
\[
 M:=\sup_{a\le t<T_*}\|U(t)\|_\infty<\infty,
 \qquad F_q:=\|R_\nu\|_{L^q((a,T_*);L^\infty)}<\infty,
 \quad 2<q\le\infty.
 \tag{IB.7}
\]
则 sup_(a≤t<T*)||∇U(t)||∞<∞。只断言这一梯度界，不在粗力假设下
自动断言全部高阶导数有界或经典光滑延拓。

### 完整周期核及黏性因子

下面补齐 [BI 第 2 节](clay_b_fixed_history_mild_preflight_20260906.md)
所用核的直接证明。全空间热核 Γ_s 的缩放给 ||D^mΓ_s||₁≤C_m s^(−m/2)。
完整 Oseen 导数核为
\[
 K_{iab}(x,s)=\delta_{ia}\partial_b\Gamma_s(x)
       +\int_s^\infty\partial_i\partial_a\partial_b\Gamma_\sigma(x)\,d\sigma.
 \tag{IB.8}
\]
第二项在 L1 中绝对可积；它的 Fourier 乘子正是
iξ_b(δ_ia−ξ_iξ_a/|ξ|²)e^(−s|ξ|²)，在零频取零。特别地
\[
 \|K(s)\|_1\le C s^{-1/2}
       +C\int_s^\infty\sigma^{-3/2}d\sigma\le C_1s^{-1/2},
 \qquad \int K(s)=0.
 \tag{IB.9}
\]
Gaussian 导数的逐点界还给 |K(x,s)|≤C(|x|²+s)^(−2)，
因此全部 2π 周期副本绝对收敛。胞积分展开表明周期核 K_per
恰表示 e^(sΔ)P₃div，而非删去远场或压力的局部核。
周期化不增加上述 L1 上界；梯度热核同理。因此
\[
 \|K_{\rm per}(\nu\tau)\|_1\le C_1(\nu\tau)^{-1/2},
 \qquad \|\nabla\Gamma_{\rm per}(\nu\tau)\|_1
                   \le C_0(\nu\tau)^{-1/2}.
 \tag{IB.10}
\]
这里只给上界，未给固定周期下全时间的双边同阶关系。
IB.8 用的是热时间 s；若改为物理时间积分，
∫_(ντ)^∞Γ_σdσ=ν∫_τ^∞Γ_(νr)dr，不能漏掉前面的 ν。

### 梯度化 mild 式与非循环的时间估计

令 H=T*−a，g(t)=||∇U(t)||∞。周期卷积 * 采用未归一化胞积分，
周期热核的质量为 1。完整 mild 式为
\[
 U(t)=e^{\nu(t-a)\Delta}U(a)
 -\int_a^tK_{\rm per}(\nu(t-s))*(U\otimes U)(s)\,ds
 +\int_a^te^{\nu(t-s)\Delta}R_\nu(s)\,ds.
 \tag{IB.11}
\]
新增非线性导数移到 U⊗U 上，||∇(U⊗U)||∞≤2Mg；
初端用热半群对 ∇U(a) 的收缩，力项直接用梯度热核，得到
\[
 g(t)\le g(a)+B\int_a^t(t-s)^{-1/2}g(s)\,ds
 +\frac{C_0}{\sqrt\nu}\int_a^t(t-s)^{-1/2}\|R_\nu(s)\|_\infty\,ds,
 \qquad B=2C_1M/\sqrt\nu.
 \tag{IB.12}
\]
这里 Rν 已投影，不使用 P₃ 在 L∞ 上有界。允许有零模：
平均残差等于平均速度的时间导数；梯度核将该模消去。

令 q′=q/(q−1)，对 q=∞ 取 q′=1。因为 q′<2，时间 Hölder 给
\[
 \int_a^t(t-s)^{-1/2}\|R_\nu(s)\|_\infty ds
 \le c_q H^{1/2-1/q}F_q,
 \quad c_q=(1-q'/2)^{-1/q'},
 \quad A=g(a)+C_0\nu^{-1/2}c_qH^{1/2-1/q}F_q.
 \tag{IB.13}
\]
在 q=∞ 时 c_q=2。于是 g≤A+B k*g，其中 k(t)=t^(−1/2)。
每个紧前缀上再迭代一次，用 k*k=π 得
\[
 g(t)\le A(1+2B\sqrt H)+\pi B^2\int_a^tg(s)\,ds,
 \quad
 \sup_{a\le t<T_*}g(t)\le A(1+2B\sqrt H)e^{\pi B^2H}.
 \tag{IB.14}
\]
最后是普通 Gronwall。证明只在各个光滑前缀上先用有限量，所得常数
不依赖前缀顶端；没有预设所要证明的终端梯度界。引理得证。

q=2 的直接 Hölder 卷积存在端点障碍，本证明不包括它；不声称该端点
结论必然失败，也不声称 q>2 最优。ν 固定为正，常数可随 ν→0 发散。

## 5. 对 IPM 同轨道移植的结论与限度

将 IB.3–4 代入引理，对每个固定 ν>0、每个 0<a<1 得
\[
 \boxed{\quad R_\nu\notin L^q((a,1);L^\infty(\mathbb T^3))
                    \quad\text{对每个 }2<q\le\infty.\quad}
 \tag{IB.15}
\]
否则 IB.14 与 IB.3 的速度梯度发散矛盾。这是对原稿所述轨道的条件推论。

由闭时空光滑的 F，TF 也闭时空光滑：对 F 的每个时间导数，
取足够高阶的空间 Fourier 衰减估计，即可控制 TF 的各个混合导数。
因此 IB.6 中“交换子减黏性项”这个联合差同样没有 IB.15 排除的积分控制。
不能据此分别断言交换子、黏性项各自发散，更没有排除它们部分抵消。

若某个 NS 物理力 f 在 [a,1]×T³ 光滑，则 P₃f 也在该紧时空上光滑有界。
必要关系 P₃f=Rν 与 IB.15 冲突。这个结论仅排除同一 U 配上这类力的 NS，
不把任意 f∈Lq_t L∞_x 自动代换为同类 P₃f，也不把所有带力 NS 排除出 Clay。
当前正向目标仍是无外力周期 NS；本文不切换到强迫问题。

## 6. 旧路线与优化路线之间实际成立的连接

| 连接 | 当前依据 | 不能跨越的缺项 |
|---|---|---|
| 原 NS → TG 定性强 W1,1 终端迹 | 已有本地冻结；本轮仅按固定来源引用。 | 没有自动的临界尺度速率、速度平方一致可积性或光滑延拓。 |
| SPI 尾矩 → 原速度终端能量缺陷 | 原 SPI.20，已完成的等式识别。 | 缺陷等于零仍未证；重复换表示不增加控制。 |
| IPM 的 Cη 密度迹 → 有界 Darcy 速度 → NS 同轨道残差障碍 | 本文 IB.4、IB.14–15；以原稿所述轨道为前提。 | 外部例子不是 TG、PF 或 NS 延拓准则的反例。 |
| 原 NS 的新动态控制 → PF 的指定中心共同好尺度 → 正则性 | 后一箭头为 PF-A；前一箭头仍 OPEN。 | 同一尺度同时满足 A+E≤M 和 K<ε_PF(M)，不能拆开选尺度。 |

这修正了比较报告中容易读得过宽的一点：IPM 的“较低正则性收敛”
只能提醒检查拓扑和方程，不能直接当作 TG 的 NS 反例。密度的正 Hölder 控制
对 Darcy 速度其实很强；真正阻断直接移植的是固定黏性动量方程的残差要求。

我采纳外部报告关于“同一历史、逐层条件恢复、误差求和”的检查方式，
但不将反向构造的任务搬到正向，也不因无黏结果存在就重开已结束的同预算测试。
下一次选题按以下顺序执行：

1. 先写候选在原无外力 NS 上新增的具体估计，标明同一初值、正龄、中心和时间区间。
2. 对照 [旧选题入口](forward_route_selection_20260908.md) 读取对应已做段落。
   如果只是 SPI 尾矩、定性迹、纪录帽或已算压力分项的相邻改写，到这里停止。
3. 如果借鉴外部构造，先写完整投影残差及其所需函数空间；本文已结束
   “保留该 IPM 速度轨道、用闭端光滑力吸收正黏性”的候选，不再扫描其参数。
4. 选择预期能改善共同好尺度、同源导数非退化、能量集中排除或延拓控制的
   明确候选作有界推导，是否真正改善以核验为准，不要求探索前已有证明。
   若仅得到条件出口或已有缺陷的等价式，如实保存内部核算。

下一条无条件临界估计尚未选定。本文完成的是一个必要的方程接口检查，
没有假定外部机制已转为 NS 动态增益，也没有为了给“下一步”命名而虚构可行性。
本次在指定的旧小节收尾和策略衔接边界结束；不据此启动自动连续研究。

## 7. 来源与可复核边界

- IPM 固定来源：`/Users/kasifa/Documents/Math/reports/2026-09-08-fluid-blowup-comparison/sources/ipm.pdf`，
  57 页，SHA-256 `b3ebdbb8d9a93dcca5f3b3f8796e63f7f28b48e0b0e258b909110a4b69c72a12`；
  原始地址为 <https://cims.nyu.edu/~tristanb/ipm.pdf>。
  主任务本轮提取并视觉核对第 3 页完整定理和公式；未重证全稿、未运行 Lean。
  本轮网络重新打开原始地址被工具拒绝，故只绑定已有固定副本，不声称核验最新版。
- 比较报告：`/Users/kasifa/Documents/Math/reports/2026-09-08-fluid-blowup-comparison/README.md`，
  SHA-256 `695cb01818fe9754c1cd029aab5ac059cb0b4f789b36ffcad1ed8d8891aa46e4`。
  主任务全文读报告及正向八项核验；反向状态仅为报告快照，没有重新读取其运行状态。
- [BI](clay_b_fixed_history_mild_preflight_20260906.md)：定向读取第 2–3 节，
  SHA-256 `6889ac3d6297c651b37a0292867b9706fd028bd03f65564857054b75ec5c2fb4`。
  本文自行写出所需完整核，不额外调用 BI 的古老解紧性结论。
- 本轮全文读 [SPI](clay_b_stochastic_pressure_impulse_20260908.md)、
  [PF](clay_b_pressure_free_shape_criterion_20260908.md)、[TG](clay_b_strong_gradient_terminal_trace_20260908.md)
  和 [选题入口](forward_route_selection_20260908.md)，
  没有重审所有历史冻结的上游依赖。历史结论身份不因本次版本核对而变成新的认证。
- 独立核算和实际成稿审读范围见 [配套审读](forward_ipm_residual_bridge_review_20260908.md)。
  均为 AI 辅助推导和审读，不是正式验证、充分查新或真人同行评审。

本次没有仿真、DGX 作业、数值证书或科学附图，也未制作读者 PDF、网页、翻译或公开摘要。
保存的是内部策略与经典估计的应用，不增加独立研究小节、release 或成果计数；
不发送新的发布交接，不查询发布状态。既有 TG 冻结与交接记录保持不变。
