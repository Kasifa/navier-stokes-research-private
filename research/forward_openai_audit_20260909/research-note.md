# OpenAI 新论文：条件对照与一个零外力候选的检查

2026-09-09。私有内部记录。输入提交：`fad1a0b403f1feb08ee5cc5c47dbe7ab385affd4`。

本轮核对的论文陈述和 Lean 定义对应 Clay 允许的含力 C/D，不直接否定无外力 A/B。主证明入口的显式本地导入链没有引用参考题目的占位证明；这不是完整证明验收。Lean 重建、实际公理依赖输出、Comparator 和独立内核检查均未运行。

随后只检查了一个现有正向入口：能否利用零外力消去外力功，从随机压力冲量的已知恒等式中取得新的终端控制。结果为 **NO-CANDIDATE（限本次 SPI/TG 接口）**：适当地补入真实外力冲量后，补偿误差的涨落—耗散关系仍成立；令 f=0 没有自动补上压力冲量的二次尾部控制。没有新的无条件临界估计，也没有关于正则性或奇性的结论。

## 1. 固定材料与实读范围

- [OpenAI 公告](https://openai.com/index/navier-stokes-solution/)：本轮实际在线读取，2026-09-08 发布。公告中的解题、形式化成功等属于作者声明，不记为本轮复验。
- [论文原件](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf)：固定本地166页版本，SHA-256 `0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f`。实际全文读取第1–3、117、125–126页；第1、125页另做图像核对。读完了定理1.1和推论10.6及后者证明，但没有读完166页构造及其依赖证明。
- [Clay 原问题](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf)：固定6页版本，SHA-256 `c1b5f27b1a64705cfaf1afceea513db5deedca8a18ca56ab32e7f86445a06d0c`。本轮实读第1、2、6页，第2及勘误第6页另做图像核对。
- [Lean 固定版本](https://github.com/openai/NavierStokesAndEuler/tree/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538)：提交 `8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538`，Git 根树 `8163a2fac282a90cc60b5afbc1f0dc7b2e5c6755`。本轮网络 API 核对提交与根树，重新计算本地快照目录对象及所检文件 blob；不是只接受下载目录名。
- [独立题目上游](https://github.com/google-deepmind/formal-conjectures/blob/8bf45ed70d48b2b2a501de9c00b26bfa38c573ee/FormalConjectures/Millenium/NavierStokes.lean)：本轮在线全文读固定版本，逐字段对照实际本地定义。命名空间、导入及辅助记号经过适配；没有运行内核级定义等价检查。

两个 PDF 原件继续位于管理记录的 `.workflow/strategy-openai-ns-20260909/sources/`，没有改动。外部 Lean 快照与本项目研究树分离，没有导入、编译或执行其代码。具体本地指针、13个锚点文件哈希及扫描结果见 [机器记录](static-source-audit.json)；[只读复核程序](audit_snapshot.mjs)不调用 Lean、Lake 或外部项目脚本。

外部成果状态为“作者声明／陈述已核对／完整验证待完成”。此状态不同于本项目局部核算的 OPEN / NOT CLAY；不能因 C/D 允许外力，就把作者的 C/D 主张改称为非 Clay 问题。

## 2. Clay—论文—Lean 的实际对照

| 条件 | Clay 原文 | 论文实际陈述 | 本轮实读的 Lean 定义或入口 |
|---|---|---|---|
| 初值与外力量词 | A/B：每个允许初值、f恒零；C/D：存在允许初值和允许外力，使全局解不存在 | 定理1.1及推论10.6选零初值并构造光滑外力 | `ComparatorSolution.lean` 两个定理均为存在 u₀、f；不是对 f=0 的断言；两个适配器实际选 u₀=0 |
| 维数、黏性 | n=3；正黏性 | 每个 ν>0；标准 Laplacian | 主定理参数 `nu : ℝ`、`hnu : nu > 0`，空间 `EuclideanSpace ℝ (Fin 3)`，PDE 中是 `nu • Δ` |
| 初值合法性 | 光滑、无散；全空间还需所有空间导数快速衰减 | 零初速度；满足上述条件 | `InitialVelocityCondition` 加 `Decay` 或 `Periodic`；没有将全空间要求替换成仅L2 |
| 外力跨终点合法性 | 全半时间轴上光滑；全空间满足(5)，周期满足(9) | 定理1.1的外力在空间和时间紧支撑；周期外力在时间紧支撑 | `ForceCondition` 为闭半空间上的 `ContDiffOn`；两个派生定义对每阶时空导数、每个衰减指数给统一界 |
| PDE、初值与光滑解 | (1)–(3)、(6)/(11) | 真实含力 NS，t<1 上光滑 | `NavierStokesExistenceAndSmoothness` 保留输运、黏性、压力、物理力、无散、初值，以及速度和压力的光滑条件 |
| 全空间能量 | (7)：全时间统一有限动能 | 构造在 t<1 上统一L2有界，并排除同力同初值的全局光滑有限能量解 | `...Rn` 另含各时刻 `MemLp` 与一个统一能量上界；不能只利用 Lean 积分对不可积函数的默认值 |
| 周期与压力 | 单位空间周期；第6页勘误补充压力周期 | 推论10.6把紧支撑构造缩入单位胞，再作不相交平移；速度、压力均周期 | `...Periodic` 同时要求速度和压力的 `IsOnePeriodic`；不允许把任意常力吸入非周期压力 |
| 失去光滑性的结论 | C/D：同一允许数据、外力没有所要求的全局解 | 定理1.1、推论10.6有速度L∞的 `limsup` 无界，并通过比较排除全局解 | 顶层定理直接陈述全局解不存在；顶层签名本身不重述全部构造细节，也不能把 `limsup` 改成全极限 |

Lean 中用 `derivWithin`、`iteratedFDerivWithin` 表达闭半时间轴导数。对应字段已读，所有 Mathlib 底层语义及其形式化等价没有在本轮完全展开或重检。定理、适配器和定义的源码吻合，不等于证明项已经被本机内核接受。

推论10.6的周期化证明已读到第126页结束：固定黏性下先作抛物缩放和时间平移，紧支撑平移之间有间隙，因此非线性交叉项不会出现；再用同力、同数据的周期光滑唯一性比较。这个局部论证仍依赖前面构造已成立，本轮不认证其前提。

本项目采用2π周期胞，而上述原题和 Lean 用单位胞。一次固定抛物重标度保留正黏性和 f=0 属性；周期单位不是消去外力的方法。主目标仍是固定胞、固定正黏性、同一无外力演化，正向保留任意允许初值的量词。

## 3. 参考定义、主入口和公理检查边界

实际入口为 `NavierStokes.lean → ComparatorSolution`。后者分别调用 `ComparatorR3Theorem` 和 `ComparatorTheorem` 的适配结果；前者取得紧支撑全空间候选，后者取得周期候选。两者实际证明都不是直接调用挑战文件中的同名定理。

本轮独立静态扫描和主任务的程序重跑得到相同范围：以 `NavierStokes.ComparatorSolution` 为根，共580个本地 NS 模块，379522行，20226808字节；转发入口 `NavierStokes.lean` 另作锚点核对，不计入580个模块。所有已扫描本地文件的 blob 与字节数匹配固定树，显式导入无缺失，不包含 `ComparatorChallenges`。边界上有209个不同 Mathlib 导入；没有递归审查 Mathlib、Lean 内核或全部第三方包。

参考挑战第277、284行的两个 `sorry` 是待验证题目的占位。`ComparatorDefinitions.lean` 不包含这两个定理；与参考文件的共同定义／辅助引理区段一致。这说明不能仅凭参考文件里有 `sorry` 就宣布主证明使用了它们。反过来，也不能凭当前扫描没发现它们，就宣布所有证明依赖已无附加公理。

[机器记录](static-source-audit.json)保存实际扫描规则的结果。程序去掉嵌套块注释、行注释和字符串，再解析显式导入，检查其中列出的占位、公理、原生判定及执行标记；当前无命中。它不是 Lean 解析器、展开器或内核。静态导入关系不等于展开后证明项的公理依赖闭包，所选关键词扫描也不是安全认证。

`ComparatorChallenges/NavierStokes.json` 指定两个真实主定理，允许 `propext`、`Quot.sound`、`Classical.choice`，并启用 nanoda。`formalization.yaml` 自报零占位、相同公理列表及 `self-assessed`；主入口末尾的两条 `#print axioms` 是源码命令，不是本轮执行输出。

## 4. 形式化重检方案：已列条件，尚未启动

锁定文件给出 Lean `v4.34.0-rc2`、Mathlib `85e3a25e006c35636f0e53b0e9296caca2685bc0`、Comparator `19e111e2141cf333c7daff0f64c5f24acc91dd2e`、lean4export `cacf989bd75f608700820f6afc595f32e7a99a4d`，共11个依赖包。`landrun` 和 `nanoda_bin` 的版本未由该项目固定。锁文件的项目名仍为 `fluidEquations`，且 `fixedToolchain:false`；这些是未来构建前需解释的配置项，不凭此推断数学错误，也不静默重写锁文件。

本机只读盘点为18个逻辑CPU、36GiB内存、约1.2TiB可用磁盘；这不是已批准的构建预算或耗时预测。PATH和通常的 `.elan` 位置未发现工具链，外部快照没有依赖缓存。没有安装、拉取缓存、构建、导出证明项或启动DGX。

后续重检分开保存以下状态，必须先满足执行授权和隔离条件：

1. 固定外部代码及全部工具版本、平台、二进制校验和；独立审查可信参考和其传递依赖，解释锁文件差异。缺一个版本就保留缺口，不用可变分支补成已固定。
2. 在没有私有研究、凭据或敏感目录挂载的可丢弃 Linux 环境中准备验证。普通编译测试和可信参考验证使用隔离的环境；不得先在可信参考环境中无隔离运行候选代码，再将其称为未受影响的参考。
3. NS 指定入口的普通编译、真实公理输出、Comparator语义比较、独立内核重检分别记录退出码、日志、输入哈希和资源峰值。不默认构建 Euler，也不把下载缓存或编译成功等同于后两项成功。
4. [固定 Comparator 文档](https://github.com/leanprover/comparator/blob/19e111e2141cf333c7daff0f64c5f24acc91dd2e/README.md)要求可信参考环境、真实沙箱和内核等前提，另列Linux本地通信限制。开发用 `fake-landrun` 不纳入安全验证方案；在Mac上跳过这些前提不叫同等级独立验证。
5. 先以保守并发测量一个受限阶段，再据内存和恢复能力决定完整运行；如使用DGX，沿用至少保留10% CPU的既定上限。每阶段分别保存已完成模块、工具链、缓存来源和日志；版本变化后不沿用旧成功状态。当前没有耗时或内存实测，不承诺完成期限。

上述是可恢复执行的前置清单，不是完整重检已经获准或已经完成。本轮授权不启动长构建，也不新增定时任务。

## 5. 唯一动力学检查：外力是否改变原压力冲量缺口

本节只对照旧 [SPI](../clay_b_stochastic_pressure_impulse_20260908.md)、[TG](../clay_b_strong_gradient_terminal_trace_20260908.md)，不分析外部构造的具体外力功能、后段零投影或内生供给；后者由反向任务负责。

在固定周期胞上取 \(0<a<T<\infty\)、ν>0，u是每个闭前终端区间上光滑的不可压含力NS解，\(\operatorname{div}u=0\)，物理外力f在含端点T的闭时空柱上光滑。令 \(G=\nabla u\)、\(\Gamma=\partial_t+u\cdot\nabla-\nu\Delta\)，采用周期压力和完整Leray投影。记体积平均为角括号，\(e(t)=\langle|u|^2\rangle\)、\(\mathcal D(s,t)=\int_s^t\langle|G|^2\rangle dr\)、\(\mathcal W(s,t)=\int_s^t\langle u\cdot f\rangle dr\)。
\[
 \Gamma u=-\nabla p+f,\qquad
 e(t)+2\nu\mathcal D(s,t)=e(s)+2\mathcal W(s,t).
 \tag{OF.1}
\]
能量计算给 \(\sqrt{e(t)}\le\sqrt{e(a)}+\int_a^t\|f(r)\|_{2,\mathrm{av}}dr\)，因此有限总耗散仍成立。零外力时消失的是显式外力功，得到的能量单调性已经在 SPI 中使用。

沿旧稿同一个前向概率空间取均匀初始标签η和独立Brownian运动，\(dX_t=u(X_t,t)dt+\sqrt{2\nu}\,dW_t\)、\(X_a=\eta\)。无散性保持均匀单时分布。定义
\[
 J_t=\int_a^t f(X_r,r)dr,\quad I_t=\int_a^t\nabla p(X_r,r)dr,
 \quad Y_t^f=u(\eta,a)+J_t-I_t,\quad U_t=u(X_t,t),\quad Z_t^f=Y_t^f-U_t.
 \tag{OF.2}
\]
对标记密度用Itô并比较线性方程，得 \(E[Y_t^f\mid X_t]=U_t\)。不加入J却沿用旧条件均值会是错误的。继续用该条件期望及周期压力正交性，得
\[
 E|Y_t^f|^2=e(a)+2\mathcal W(a,t),\qquad
 E|Z_t^f|^2=2\nu\mathcal D(a,t).
 \tag{OF.3}
\]
外力功在总二阶矩中存在，在两项相减后的方差关系中抵消。前向Itô的实际符号为
\[
 dU_t=(2\nu\Delta u-\nabla p+f)(X_t,t)dt+\sqrt{2\nu}G(X_t,t)dW_t,
 \quad dZ_t^f=-2\nu\Delta u(X_t,t)dt-\sqrt{2\nu}G(X_t,t)dW_t.
 \tag{OF.4}
\]
以确定时刻s重启同一计算，得到 \(E|Z_t^f-Z_s^f|^2=2\nu\mathcal D(s,t)\)。所以Z的强L2终端迹和旧稿的有符号黏性冲量控制，不是无外力特有信息；Z也没有因此成为前向鞅。

压力不能继续误写成无外力的全部压力。分解
\[
 p=p_N+p_f,\qquad -\Delta p_N=\operatorname{tr}(G^2),\qquad
 \nabla p_f=(I-P)f,\qquad
 \Gamma G=-G^2-\nabla^2p_N+\nabla(Pf).
 \tag{OF.5}
\]
旧 [GD §2](../clay_b_gradient_rank_one_defect_20260908.md) 的Hardy压力接口控制 \(\|\nabla^2p_N\|_1\le C\|G\|_2^2\)。光滑f的 \(\nabla(Pf)\) 在闭有限柱可积，可用高阶Sobolev投影及嵌入估计；没有声称P在一般L∞上有界。于是TG的同漂移可积源引理仍给梯度强L1迹。速度均值不再恒定，而是 \(\overline u(t)-\overline u(s)=\int_s^t\overline f(r)dr\)，其收敛补上原Poincaré步骤。

所需非临界速度时间界也没有获得新指数。令 \(y=\|G\|_2^2,z=\|\Delta u\|_2^2\)，原 [LP §3](../clay_b_leray_paid_budget_20260907.md) 的梯度能量测试多出 \(C\nu^{-1}\|f\|_2^2\)。除以 \((1+y)^2\) 并积分给 \(\int_a^T z/(1+y)^2<\infty\)。零均值部分的插值及时间Hölder给
\[
 \int_a^T\|u-\overline u\|_\infty dt
 \le C\left(\int_a^T\frac z{(1+y)^2}dt\right)^{1/4}
 \left(T-a+\int_a^T y\,dt\right)^{3/4}<\infty.
 \tag{OF.6}
\]
均值另有有限时间积分，故同一随机轨道有终端极限。压力的L3/2界保留原 \(C\|G\|_2^2\) 和额外 \(\|(I-P)f\|_{3/2}\)；均值输运 \(\overline u\cdot\nabla u\) 无散，不贡献压力梯度。由此，旧压力冲量的强L3/2收敛及统一L2界仍可按同样步骤得到。

新增外力冲量满足
\[
 \|J_t-J_s\|_{L^\infty(\mathbb P)}\le\int_s^t\|f(r)\|_\infty dr.
 \tag{OF.7}
\]
它强L∞收敛。OF.2中的 \(u(\eta,a)+J_t-Z_t^f\) 已强L2收敛；结合刚说明的TG/LP终端接口和均匀标签论证，仍有
\[
 u(t)\to u_*\text{ 强L2}\quad\Longleftrightarrow\quad
 I_t\to I_*\text{ 强L2}\quad\Longleftrightarrow\quad
 \{|I_t|^2\}\text{ 在终端邻域一致可积}.
 \tag{OF.8}
\]
这里只复核既有论证在光滑力下多出的项，未重新认证GD的全部外部Hardy依赖。外力功可积使能量有左极限，不强迫左极限等于终端弱极限的能量。即使取得强L2迹，本身也不是光滑延拓。

## 6. 本轮结论和下次入口

就所检验的SPI/TG链而言，外力功、外力冲量和可积梯度源的消失没有形成新的无外力临界控制。首轮选择结果为准确的NO-CANDIDATE，不扩大为所有无外力方法不可能，也不把含力构造当作本项目无外力目标的反例。

下一次正向候选须先写出区别于OF.1–8、真正利用同一无外力演化的具体估计；若它仍适用于上述全部光滑含力解类，就不能仅凭名称声称抓住了f=0特有信息。压力有符号相关性及临界集中仍是未解决项；此处没有已经选定或被证明可用的替代不等式。TT的初始层反检、SPI径向尾矩更名和IB同轨道移植不重新展开。

这份记录完成有界条件审计和一个候选差异检查，不是新论文或独立研究冻结。TG仍是最后独立冻结；无重复交接、网站、翻译、调度、远端配置或大计算。形式化重检待上述前置条件及相应授权；本轮不以等待它为理由轮询或监督其他任务。
