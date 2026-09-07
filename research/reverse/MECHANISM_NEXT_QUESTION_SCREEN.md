# 两类机制的下一问题筛选

2026-09-08，PRIVATE_CORE。非正式发布包。本轮只读已有科学文本、定向核对原文、手工推导及绑定文件；没有运行科学程序、解码数组、扫描参数、选择新初值或执行 Git。

**裁决：没有通过筛选的奇性机制。只保留一个值得完成的有界结构障碍问题：任意平移、转轴、正幅度及等向尺度调制，能否救回既有纯方位外环的精确局部轨道？** 这个问题由根代理在本轮提出；我独立核对其历史差别与可判性。它不是正面候选，不启动数值生产，也不延续全局证书常数的细化。

## 1. 已有结果不能重复申报什么

| 已读来源 | 已支付的实际内容 | 此次不能当作新问题的改写 |
|---|---|---|
| return-interface/ROOT_INTERFACE_NOTES；R0.10 §7、R0.11 §3、§6 | FA 第一代四中心的主极化共用法向；其中心纯前代自作用为零。一般等长中心门的一维像已经是 R0.11 引理1。有限包宽及真实目标带余项仍保留。 | 再求一次中心输出、更高阶非零，或只把小横向分量叫作第二种输入。R0.11 的反向一维闭合障碍另有差频消失前提，不能无条件套到 FA。 |
| driver-dominance/OUTCOME；route-screen/HISTORY_SCREEN | 同一完整六模初值原解中，新生项的净驱动占优与逐通道绝对占优失败已区分；当前目标几何与旧 R0.9–10 相同，最直接整组复制已失败。 | 换单模比值、提高 Taylor 阶、把已有中心增厚为预置稠密初值族，均未补齐同轨道实际返回状态。 |
| swirl-regeneration/OUTCOME | 一个固定旋流初值的第一代真实产生；指定模板的最早二阶自反馈为零；固定中心最初的拉伸标量为负。 | 当前球形旋流合同已结束；另取中心、稍晚时刻或更高 Taylor 阶，不能自动成为结构替换问题。固定点负号也不是所有轨迹、位置或全涡量变化率的符号。 |
| heat-preload-boundary/DERIVATION，H.4、H.7c、H.11–15 | 同一无限谱热初值的固定高尾比例不增；空接收带的相对误差门是平方量；完整 NS 通量可与黏性竞争，未加权尾紧性不控制高导数。 | 换成无限热预置不绕过 H.4；正尾通量不证明前代纯供给；全时小相对误差尚须实际支付，也不排除带趋零能量的浓缩。 |
| next-concentration/OUTCOME；exterior-pressure/OUTCOME | 指定收缩路径失败；能量和中心压力同时合规仍可 NON-NS；固定外环在小 C3 邻域的一次连续持留有上界。 | 扫描静态外环、补一个中心压力矩阵或只调能量幅度，已经没有新的机制解释。旧持留结论没有限制再进入次数。 |

FA.13–14 实际控制完整原解的短时状态及目标带余项，不能贬低为只算第一 Picard。问题在于没有返回模板、接收时间和按真实来源分账的下一次输入；不是完全没有状态信息。其常数对 N 一致，不等于对包宽趋零一致。FA.16 则明确使用随 N 变化的初值族。

来源分解引理也已给出 \(u=h+g+\mathcal G+\mathcal H+\mathcal R\) 的九个有序通道和条件余项；其中 g 含切点以前的全部历史，不是纯第一代。将未知 M 写成假设、重命名 g 或把 \(\mathcal R\) 小称作 \(\mathcal G\) 占优，均不产生新的可检验模板。第一类机制在本次指定来源中仍是 **NO-CANDIDATE**；没有另提一项数值或高阶任务。

## 2. 唯一保留问题与历史差别

`JOINT_TEST_PROOF.md` §6 已在既定尺度和幅度路径上，以外环的非零方位残差旋度证明 NON-NS。该文确实允许其指定的时间幅度与外壳位置变化，不能声称这些从未处理。`RESCALED_EXIT_PROOF.md` 则使用固定坐标球、固定形状及给定重标尺度，证明真实解不能长时间停留于其小 C3 邻域。其独立审查明确保留平移、旋转调制后的形状为未覆盖范围。

本问题新增的范围是**任意 C1 中心和转轴，连同任意正幅度、等向尺度函数**的精确局部形状保持；没有调制速度小性的假设。需要完整角环的原因不是技术装饰：单点上，轴倾转和平移产生的项可以非零，旧单点符号不能直接照搬。

定向检查上述外压、旋流、固定浓缩和路线筛选文件中的平移、旋转、转轴、调制条目，未发现这个完整范围已被证明。该结论仅是本地历史去重，不是文献新颖性判断。其核心方位对流公式仍是旧恒等式；可增加的是调制项的准确消除范围，不能称为新奇性机制。

## 3. 建议锁定的有界合同

只使用旧外环
\[
W(y)=w(r,z)e_\theta,
\quad w(r,z)=2r h'\big((1/20)^2-r^2-(z-3/2)^2\big),
\]
其中轴仍为 \(e_2\)，右手圆柱基及 h 均取 `JOINT_TEST_PROOF.md` §6 的原定义，不改变截止、尺寸或初值。

沿用旧 \(y_*=(1/40,61/40,0)\)、\(B_*=B_{1/400}(y_*)\)。令 \(\mathcal O\) 是 \(B_*\) 绕 \(e_2\) 的所有旋转的并。它包含整个见证圆周及其开邻域，闭包仍在同一个外环支撑球内部，并远离轴线；这是旧球的对称轨道，不是另选数值参数。

设 u 是固定黏性1、无外力、固定三维环面上一条已给定初值的光滑真实 NS 解。只问在某个正长度开时间段 J 上，能否存在
\[
c\in C^1(J,\mathbb R^3),\quad
\mathsf Q\in C^1(J,SO(3)),\quad A,\ell\in C^1(J,(0,\infty)),
\]
使实际**总速度**在整个移动时空管上精确满足
\[
u\big(t,\pi(c(t)+\ell(t)\mathsf Q(t)y)\big)
=A(t)\mathsf Q(t)W(y),\qquad y\in\mathcal O.
\tag{MQ.1}
\]
这里 \(\pi\) 是到固定环面的覆盖映射；每个时刻须有包含完整移动圆周的注入局部坐标图，且等式在开时空邻域成立。不能只给一条曲线上的取值而借用邻域空间导数。c 可理解为该局部时间段的连续提升；\(\mathsf Q\) 只是局部坐标表达，不是假定环面具有任意旋转对称。

所有其它频率和外场都属于同一真实 u、p。只有它们在此局部合成的总速度满足 MQ.1 时才能使用合同，不能先删去背景速度再套它。完整周期压力保留；其旋度在局部精确为零。

待证明的有限结论是：对于旧非零见证，这种精确保持不存在。它不要求构造一个新初值，也不要求先知道某条真实轨道曾接近 W。若证成，任何一个固定初值的真实轨道都不能在一个正长度区间满足这个局部假设；不能由此证明该轨道全局正则。

## 4. 独立手推的可判性检查

下列计算用于决定问题是否值得继续，不将本筛选页冒充完成的独立证明包。令 \(K=\mathsf Q^T\mathsf Q'\)、\(b=\mathsf Q^Tc'/\ell\)、\(\lambda=\ell'/\ell\)。在固定物理 x 处微分，必须完整保留
\[
\mathsf Q^T u_t
=A'W+A\{KW-(Ky)\cdot\nabla W\}
-A(b\cdot\nabla W)-A\lambda(y\cdot\nabla W).
\tag{MQ.2}
\]
旋度的物理缩放还贡献 \(1/\ell\)，不能遗漏。

写 \(\Omega=\operatorname{curl}W=\Omega_r e_r+\Omega_z e_z\)，并令 \(K y=\beta\times y\)。旋转生成元取旋度后是 \(\beta\times\Omega-(\beta\times y)\cdot\nabla\Omega\)，其方位分量恰为
\[
\beta_r\left(\frac{z\Omega_r}{r}-\Omega_z\right).
\]
平移生成元的方位分量为 \(-b_\theta\Omega_r/r\)。在固定 r、z 的完整角平均中，\(\beta_r\) 与 \(b_\theta\) 均平均为零。轴向旋转并未留下一项常量误差；它因 W 的轴旋转协变精确消失。这个检查不限制 \(\beta\) 或 b 的大小。

幅度项的旋度、尺度项的 \(\Omega+y\cdot\nabla\Omega\)，以及 \(\Delta\Omega\) 都是轴对称经向向量。因此，若记完整动量残差
\(R=u_t-\Delta u+(u\cdot\nabla)u+\nabla p\)，目标恒等式为
\[
\frac1{2\pi}\int_0^{2\pi}
e_\theta(\theta)\cdot\mathsf Q^T
\operatorname{curl}_xR\big(t,\pi(c+\ell\mathsf Qy_\theta)\big)\,d\theta
=\frac{A^2}{\ell^2}q(r,z),
\tag{MQ.3}
\]
\[
y_\theta=(r\cos\theta,z,-r\sin\theta),
\qquad q(r,z)=-\partial_z(w^2/r).
\]
旧见证圆周 \(r=z-3/2=1/40\) 上，已经解析证明
\[
q(r,z)=\frac1{100}h'(1/800)h''(1/800)>0.
\]
故 MQ.3 一旦按上述时空管合同完整证明，就与真实 NS 的 R=0 矛盾。黏性未被近似为零；它在所选平均量中的分量为零。压力也不是被指定或补偿，而是由精确旋度恒等式消去。

这些等式给出可直接审查的有限工作量：时间变坐标、curl 与 proper rotation、两个一阶角谐波的平均、旧圆周支撑和局部周期图。无需新 Fourier 卷积、PDE 轨道、Taylor 阶或数值阈值。若正式推导发现任一零平均项不成立，就停止并记录该合同未通过，不通过缩小速度、改变角环或引入新参数挽救。

## 5. 它会改变什么，不能支付什么

若该合同成立，将关闭“旧外环只需漂移、转轴或改变幅度/尺度就能成为精确真实轨道”的修补解释。下一次真正使用外场的构造必须改变局部速度形状，并为新增经向或非轴对称作用提供真实动力学；不能仅调节运动参数。本筛选不要求立刻为这些更广的结构另设任务。

严格不外推到小 C3 距离的调制轨道：误差乘任意快的调制速率可能不能由固定误差常数控制。也不外推到只覆盖一段方位角的局部邻域、另加背景输运/应变的场、一般非定常外压结构、离开后的再进入次数或累计持留时间。有限角平均障碍不提供这些结论。

最终状态仍是 **NO-CANDIDATE FOR A SINGULARITY MECHANISM**。保留的是一次非定常形状解释的结构检验，不是可迭代供给候选。频带再生成、单个固定初值的无限尺度、完整无限维迭代误差、有限总时间及奇性仍未支付。不同已固定初值的结果不得拼接；\(\forall N\exists u_{0,N}\) 仍不推出 \(\exists u_0\forall N\)。

## 6. 实读范围与实际输入字节

四份指定文本全文读取。补充读取旧路线筛选、来源分解、固定浓缩及外压阶段结论；外压持留证明全文，JOINT_TEST §1–6，FA.13–17，R0.10 §7 与 R0.11 §3、§6 的原始命题和证明局部。RESCALED_EXIT_REVIEW 只定向读取其未覆盖调制的结论段。未重扫全部研究库、重开 Tsai 或其它外部论文，未主张外部文献新颖性。下列哈希定位实际字节，不替代那些来源的原证书或本问题后续独立审查。

| 文件（相对反向工作树） | SHA256 |
|---|---|
| research/reverse/return-interface/ROOT_INTERFACE_NOTES.md | 03deb65a173e254832e298dfe31c3fc8e8c82fe38d996e9bab33dfaaece7bab7 |
| research/reverse/driver-dominance/OUTCOME.md | 7469778e1a2269225ca192baa77a1af25ded9d8b3c94346454af48d90eef5040 |
| research/reverse/swirl-regeneration/OUTCOME.md | 0ad7cbccb6c758ebbb9165e785ae3746d203736e6766a3d2abf263904c95b2ab |
| research/reverse/heat-preload-boundary/DERIVATION.md | 333d5708b253a3f86d52324dd7e28e97b941afcf9c7c71c9b041616df0bc6a1a |
| research/reverse/route-screen/HISTORY_SCREEN.md | 9fb62c4d1fa569e8fefb12dbbc58d3cb9d0423879d6afa80af68f9de863a9bfb |
| research/reverse/reconnection-preflight/SOURCE_ATTRIBUTION_LEMMA.md | d22bcca237977647b54ebbe13288c63a24a7c610a52a7c2265f4e3cfe366607a |
| research/reverse/next-concentration/OUTCOME.md | d0c3123589f13b19692c6b2116a23f7e08e4f584f2d85404e03753b0feeec372 |
| research/reverse/exterior-pressure/OUTCOME.md | 17024e2a79907d19f6d25c2d3261f58b899f9f269626f30cb841e22ccd301d7e |
| research/reverse/exterior-pressure/RESCALED_EXIT_PROOF.md | e96f1bce6d2076d560191211e208bd43f33e0db2d5c21de8abc6dfd31b361e78 |
| research/reverse/exterior-pressure/RESCALED_EXIT_REVIEW.md | d9b29618ec836e0d3ea3a63fde0888db59add6b289dc7900c84a0e748601a0d6 |
| research/reverse/exterior-pressure/JOINT_TEST_PROOF.md | 9d0100f62ec6ef25ef2552348120d2b7b1e802aba49167bf4115edad02a3cd91 |
| public/notes/r0-10.html | d7566fd57a4b8198a866ff3d317ef15bcd1b6671054c964f8875b00635145a0a |
| public/notes/r0-11.html | ad8ebe34c67939cd371f621cc7fbf5f54cf501c4d2506e587aa1494f4ef52095 |
| research/clay_b_frequency_activation_20260907.md | 42bbc2ba3abae7aa1eeb25ee0b29f896d7d8ddcafccb0da518dded4851dd897a |
