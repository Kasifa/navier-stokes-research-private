# 双对称周期压力包：最终范围与字节核验

2026-09-08，PRIVATE_CORE。**PASS：十一项接纳文本的 SHA-256 与字节数全部匹配；两稿、两份非作者审查及根比较的共同有限范围一致，无待修实质问题。** 本记录完成本次最终范围核验，不代替其后的冻结记录，也不声明已经归档或发布。

## 1. 身份与实际阅读次序

我是本项 MAIN_REVIEW 的作者，不是 PROOF 或 INDEPENDENT 的作者。此前审过 SAL/SBI 来源、局部弱退出及支撑/同轴极化主稿，并写过二阶平移预检。本项第一次主稿审查时没有读取独立稿；本次才首次全文读取最终 INDEPENDENT 和 INDEPENDENT_REVIEW，并作序贯合并核验。因此本记录不是未见主稿的盲审，不另计第三份独立证明，更不称人类同行评审或形式认证。

本次实际全文读取 ROOT_COMPARISON、OUTCOME、SOURCES、acceptance.json、INDEPENDENT、INDEPENDENT_REVIEW，并补全文读取前置 PREFLIGHT 和 ROOT_SOURCE_LOCATOR。CONTRACT、PROOF、本人 MAIN_REVIEW 及 PREFLIGHT_REVIEW 沿用此前已实际全文读取的停改字节，本次重新核对哈希；另复读 MAIN_REVIEW 的开头来源和既有逐式核验段。不是把作者的阅读声明直接计为我自己的原文阅读。

当前 MAIN_REVIEW 中“未读取 INDEPENDENT”、独立稿开头“待非作者审查”、主稿形成时的待审状态、预检的 OPEN 和 locator 的后续定位文字，均保留为各自形成时的历史记录。它们不被追写成当时已获最终接纳，也不与后来两份 PASS 审查矛盾。acceptance.json 的 FINAL_SCOPE_PENDING 是本记录写入前的接纳快照；我没有改写它或使自身循环绑定。

## 2. 十一项最终文本与接纳快照

以下路径相对于本科学工作树的 research/reverse/。哈希和字节数均为本次实际文本元数据核验，与 acceptance.json 的十一条记录逐项相同；没有只核摘要或前缀。

| 文本 | 字节数 | SHA-256 |
|---|---:|---|
| symmetry-pressure/CONTRACT.md | 4935 | be413616aa81f63f6bf7584c7dc41926fc721f8c845278df4164edc6f39d0124 |
| symmetry-pressure/PROOF.md | 12624 | 4ba474f1d6735bed9e9ccc60783ef002a7e13b9442a12d1e0db17364bc9aea14 |
| symmetry-pressure/INDEPENDENT.md | 17245 | c5c6d5cc0099d92270cb541173bcd0c8f04e083d2d1a840dc8b73ceec57996c1 |
| symmetry-pressure/MAIN_REVIEW.md | 9337 | 5bc7f56d1d45c9f81e21309c0505295681d827e367bfd77e7be6b4d3a323ed35 |
| symmetry-pressure/INDEPENDENT_REVIEW.md | 10992 | 02e0eaec16763d847b39cf8743d7f542424924513d6e16f726fc62911f5c55cf |
| symmetry-pressure/ROOT_COMPARISON.md | 5549 | 7ecb3e4fe6fc1b3f316fa9bd522e2ac85add49a7aa6831d69a3918525b899a53 |
| symmetry-pressure/OUTCOME.md | 2799 | 0ba73c06edd7dbe223fe9a4f7199196bc51bb313b66cad6d5056048a806f5086 |
| symmetry-pressure/SOURCES.md | 4133 | 35d5a20a4b7d1dd9e5e02691d964ef56684a94ecaab99a879c2051dddfc82ff9 |
| symmetry-pressure-preflight/PREFLIGHT.md | 11366 | abf66039c0c6d158d88c3b293c7bffbd93d9ebc043a327fe357dc9f84f867150 |
| symmetry-pressure-preflight/PREFLIGHT_REVIEW.md | 8758 | 6c71b9682f58fa1d0aa808548bad08aafdbf959b4136e8eb8919c5b4a7643b99 |
| symmetry-pressure-preflight/ROOT_SOURCE_LOCATOR.md | 1513 | bbd8c3d57ad138a123f5dcb32e5599ac013bf7442636e3a01ed31bd96edf350b |

实际全文读取的 acceptance.json 本身为 **3556 字节**，SHA-256 为
**eb9f39b2fcd9ee595e8f660249006af9d390f69dcfbbca3617bd3ca3dca94e3f**。
它是上述十一项的接纳快照，不是其自身的第十二条绑定；本记录也没有自列哈希。后续冻结必须由独立记录绑定本记录的最终字节。

数学旧源本次只重新核哈希，阅读沿用本人主审中准确列出的范围：

| 旧源 | 本人已实读、此次沿用的范围 | 本次复核 SHA-256 |
|---|---|---|
| exterior-pressure/PROOF.md | 第 1–118 行；数学复用限 §§1–2 完整周期 Green 与光滑修正，不采用旧静态参数 | 50df7a60076567acac9cbad6588132c3e0f49e77f84f17ee68e740a8a32478b9 |
| reconnection-preflight/SOURCE_ATTRIBUTION_LEMMA.md | §§2、4 全文，第 81–114、173–224 行；完整局部解、同窗正则及唯一性 | d22bcca237977647b54ebbe13288c63a24a7c610a52a7c2265f4e3cfe366607a |

其它历史源在预检或 SOURCES 中被列出，不因此成为本次全文实读。没有把旧数值实例复用为当前比较数据。

## 3. 两份完整构造的共同入口和不同符号

合法群是标准环面上的十二元正交整数群 \(\{P,-P\}\)。其作用保留完整 NS、散度、黏性、实值和压力零均值规范；局部唯一性传递两种对称。这里没有增加 Miller 文献中的其它平面镜像资格。

沿用已逐式核过的 SP.1–6，并直接比对 SPI.5–9：若
\(S=J-I\)，则
\[
A=\beta S,\qquad S^2=2I+S,\qquad
H=-2\beta^2I+hS,\qquad
\beta'=\nu\gamma-\beta^2-h.
\]
独立稿的 \(\gamma\) 对应主稿的 \(c\)。原点停滞只删除输运项；压力迹不决定 \(h\)，黏性三阶局部导数没有被删去，也没有调用需要 \(|u|>0\) 的旧除法公式。

两稿使用同一个正号 Lebesgue 压力卷积
\(p=\partial_{ij}G*(u_i u_j)\)。四阶核普通积分只在初始源远离原点时调用；正时间的完整压力由 Fourier 恢复及高阶正则支付。这里没有把初始支撑分离延伸为正时间支撑性质。

主稿的既审构造使用
\(\int W\otimes W=m(I-ee^T)\)，先在完整周期核下取得
\(D_e^4G(y)>0\)，再在十二个分离群像上叠加。每个群像的 \(e\) 方向观测相同，最终
\(h_b=6L_\varepsilon<0\)、\(d=-h_b>0\)。

本次首次实读独立稿后，另按其自身定义手核 SPI.10–22：径向 Hessian 积分的完全对称张量，其双迹为 \(15\kappa\)；与 \(\Delta\psi\) 的两个交叉矩各给 \(5\kappa ee^T\)。因此
\[
\int w\otimes w=\kappa(I+7ee^T),\qquad
\int|w|^2=10\kappa>0.
\]
两端奇性配对的局部块本身置换等变，分离支撑恰好删除二次交叉应力。其压力主核收缩为
\[
K(e):I=0,\qquad
K(e):(ee^T)=\frac{-12I+36ee^T}{4\pi},
\]
乘两端系数 \(2\) 和应力系数 \(7\kappa\)，得到
\(\mu_*=42\kappa/\pi>0\)。故独立稿的 \(h_b>0\)、\(d<0\) 与完整系数吻合；没有靠主稿的非零结论补其证明。

两份 \(b\) 的局部场、积分应力和符号不同。根比较准确保持这种区别：共同结果是各自 \(d\ne0\)，不能跨稿代入半径、误差常数或时间窗，不能拼成一条解的符号控制、重置初值或连续外源。

## 4. 三类余项与真实解入口分别支付

主稿的完整周期修正先被轴向 Newtonian 主部压过，再在固定非轴中心的完整核上使用
\(J_W\omega_y(\varepsilon)\to0\) 支付局部化。群作用后无相消的等式建立在已证明的初始分离和核协变上；不是把未经核验的对称化当作非零。

独立稿先固定径向 \(\psi\)，然后用
\[
\|H_\eta^E-H_*\|_F\le2\eta C_5J_1
\]
固定 \(\eta\)，取得混合分量至少 \(3\mu_*/4\)。此后保持这份场不变再作 \(\rho\) 缩放，完整周期修正满足
\[
H_{b_\rho}=\rho^{-2}H_\eta^E+\mathcal E_\rho,\qquad
\|\mathcal E_\rho\|_F\le20\kappa M_Q\rho^3.
\]
主项与误差比较确需 \(\rho^5\) 条件，给
\(h[b_\rho]\ge\mu_*/(2\rho^2)>0\)。五阶核所在紧球远离原点；周期修正是完整光滑 \(Q_G\)。误差常数即使为零也未被当作除数。几何支撑要求与小量条件同时可满足，不选实际数值。

这两套空间误差各自闭合，符号参数均先于时间固定。两稿随后直接调用同数据 SAL 完整 Fourier–Leray 局部收缩和同窗高阶正则，未作 Galerkin 截断。非零光滑 \(b\) 的 \(\mathcal A_1\) 范数有限且正，充分窗口
\(T=\nu/(256\|b\|_{\mathcal A_1}^2)\) 合法；零比较数据另用零解，不套零分母公式。所得 \(\beta\) 在初始端点右侧为 \(C^1\)。

两份初值的共同零邻域同时支付 \(\beta(0)\) 和黏性局部项相等，故差导数为 \(-h[b]\)。时间余项是各自真实导数差的积分，明确有
\[
|r(t)|\le t\sup_{0\le s\le t}
|\beta_b'(s)-\beta_a'(s)-d|=o(t).
\]
主稿的闭小窗端点和独立稿的开小窗端点均按各自声明保留；公共结论仅需一个依赖固定数据的非零正窗。没有借空间误差代替时间小量，没有未经证明的 \(O(t^2)\)、数值时刻或统一于所有数据的正窗口。

独立稿审查对 SPI.1–43 的这些核验与本次序贯手核一致。两份审查没有把另一份构造用来填补被审证明，根作者对读也没有另计证明通道。

## 5. 来源历史和最终接受边界

三个预检记录只允许开启后来这个窄合同，不计三份新科学证明；其中 PREFLIGHT 和 ROOT_SOURCE_LOCATOR 本次全文读取，PREFLIGHT_REVIEW 沿用此前实际全文读取的相同字节。PREFLIGHT 记录其作者的 §3.1 定向完整正文阅读；ROOT_SOURCE_LOCATOR 记录根当时只读陈述。二者属于不同人的实际范围，不能混记。

SOURCES 明确记录：根先定位 Miller 2404.01505v3 的陈述，**在主稿停改后**才补读 §3.1 完整提取文字，包括 Theorem 3.2 证明。PROOF 的成稿时阅读说明因此保持原状；后来补读不被倒填为成稿前认证。上述记录没有本轮 PDF 字节重取、视觉整篇检查或外引复证；我本次也没有新读该外文原文。历史 PDF 哈希只作历史身份，不作本次实取。该全空间瞬时积分及 Euler/受限投影结论没有进入本包的周期 NS 证明前提。

最终接受范围严格为：在固定任意正黏性、无外力、标准三维环面，存在满足全部坐标置换等变与中心奇性的光滑实值无散零均值比较初值，在原点一个共同邻域都为零，却有不同的完整周期混合压力 Hessian，并在各自同数据的真实 NS 解上给出 \(dt+o(t)\)、\(d\ne0\) 的应变差。因此，以该邻域的全部初始速度和固定黏性为唯一输入的普适初始导数闭合失败。

这不是每个局部资料纤维都能实现任意压力、任意符号或任意时间轨迹的定理。全域资料输入、特殊轨道和其它非局部闭合没有被排除。两稿没有支付同一解的真实两步供给、统一迭代、跨代无限维误差、单初值无限尺度、有限总时间或奇性；旧六项失败证据和证书缺口均不修复。原点矩阵形状、一般压力非局部性和局部存在方法均承认旧来源，不以本次核验宣称外部新颖性。

结论保持 **PROVED BOUNDED LOCAL-INPUT OBSTRUCTION / NO-CANDIDATE / NOT CLAY**。本项窄检验到此结束；没有读取 dynamic-sign-preflight 或其它后续科学稿，没有用后续问题补证。只写入本记录，执行文本阅读与哈希/字节元数据核验，未运行科学程序、数组或数值扫描，未选实际初值、参数或时刻，未使用 Git、对外消息或发布。本记录写后实际全文自读并复核上述来源字节，再停改交付。
