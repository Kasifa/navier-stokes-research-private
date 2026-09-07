# 同一段后验导数输入的范围审计与一个必要门建议

2026-09-08。PRIVATE_CORE。状态：**现有整段导数证据不足以支付固定指数包络；尚无针对新 μ 的已接受导数障碍。本轮只提出一个未执行的必要门。**

本项固定既有参照、原六模初值、ν=1、T=5/2、G 的完整4912个双符号模式，以及 I=[1280/2048,1281/2048]。不选择 ε、节点、时间窗、模板或新精度，不生成轨道或证书包。本人只读取下表数学文本和小型旧记录，没有解码科学二进制、重建系数、求新范数或执行科学核。另实际对同一旧节点的两个已存有理数作了阈值交叉乘比较，范围详见第3节。

本审计不是对本人此前参与的 HYBRID/C¹ 接口再作一份非作者证明，也不是第三次导数计算。本文核对已接受结果的适用范围，并手推一个后续可失败退出的必要条件。

## 1. P.1 与一侧应变版本必须分别记账

PARAMETRIC_COST_LEMMA.md 的 P.1 要求整个 [0,T] 上

\[
\|D^jv(t)\|_{\infty,F}\le M_j(t)\le\mu_je^{-t},\qquad
(\mu_1,\mu_2,\mu_3)=(19/5,19/5,6),
\]

另有完整 r₀、r₂ 包络、同一参照的结构/时间正则性以及终点条件。这里的范数是归一化体积下、全部有序空间指标的 Frobenius 范数。

STRAIN_CONTROL_REFINEMENT.md 的 S.1–S.2 则合法地将两处 M₁ 换成

\[
\sigma_v(t)=\sup_x[-\lambda_{\min}((Dv+Dv^T)/2)]\ge0,
\]

但 **M₂、M₃及残差没有随之替换**。要复用同一参数化控制代数，须明确采用应变版本，并另付 σᵥ(t)≤(19/5)e⁻ᵗ；不能把一个 σ 上界填入 P.1 原本的完整梯度栏。

这不是符号上的细节：σᵥ≤‖Dv‖∞,F，逆向一般不成立。指定 μ 的应变版本仍有完全相同的二阶必要要求 ‖D²v‖∞,F≤(19/5)e⁻ᵗ。

## 2. 已认证的整段导数界支付到哪里

ONE_SEGMENT_DERIVATIVE_OUTCOME.md 与其最终审查接受了同一 I 上、同一原参照的三个上界。它们来自固定 χ=Re v_(+e₁),2、b=v−χa 的三次 Bernstein 包围；包含全部正负谱，没有删除模板差。

| 已有证据 | 已支付的输入 | 尚未支付的固定要求 |
| --- | --- | --- |
| σᵥ≤343/100 | S.2 在 I 上的有限一侧系数上界 | σᵥ≤(19/5)e⁻ᵗ；也没有由此给出 P.1 的完整 M₁ |
| ‖D²v‖∞,F≤3833/500 | I 上完整二阶有限上界 | M₂≤(19/5)e⁻ᵗ |
| ‖D³v‖∞,F≤6507/500 | I 上完整三阶有限上界 | M₃≤6e⁻ᵗ |
| 共享节点值/斜率的原有理 Hermite 定义 | 同一 v 的 C¹、实值、无散、零均值和初值锚 | 不自动产生任何全窗数值包络 |
| 旧终点独立门 A₋₁(v(5/2))<1/2 | 参照终点一项 | 控制函数终点、全窗误差与真实解延拓仍须其余条件 |

上述三个显示常数是向外放宽的合法上界。对 I 上的 t，t≥5/8 且 eᵗ>1+t≥13/8，所以

\[
(19/5)e^{-t}<152/65,
\qquad 6e^{-t}<48/13.
\]

343/100 与 3833/500 均大于152/65，6507/500 大于48/13。因此这些显示上界不能通过大小关系认证所需固定指数包络。**这并不说明真实 σᵥ、M₂或M₃超过靶标**；一个过宽上界不是下界，也不证明其它验证方法必败。

初时刻确有 σₐ=2、‖Dʲa‖∞,F=2√3（j=1,2,3）；均与上述初时刻靶标相容。这只是一点事实，不能沿整个参照自动传播。已有段界也只覆盖 I，不能填充其余5119段或推算全窗认证成本。

## 3. 同一 n1280 的历史点值去重

先核旧 NODE_TRIAL_OUTCOME.md、NODE_GATE_LEMMA.md、NODE_GATE_INDEPENDENT_RUN_CONTRACT.md、NODE_GATE_INDEPENDENT_RESULT.md 和 node-independent-comparison.json。旧独立算术只覆盖 n=640 的27个有序三阶点向量及 n=5120 的终点范数；其两节点58944个投影系数实虚标量对照，**不包含 n=1280 的点张量独立复算**。

根的 node-gates-root-run.json 的 n=1280、t₀=5/8、x*=(π/2,π/2,π/2) 条目实际保存了二阶与三阶点值平方及 P₃₂(5/4)。本次只提取该条目，不扫描其它节点，不重求点值或导数张量。记旧点值平方为 qⱼ^pt，以区别下文完整空间 L² 平方 Q₂。

已有有理数的两次整数交叉乘给出：

| 固定节点的旧记录 | 对现有 μ 的有理必要门 | 本次读档判断 |
| --- | --- | --- |
| q₂^pt=0 | q₂^pt P₃₂(5/4)>361/25 | 不触发，差的符号为负 |
| 已存 q₃^pt | q₃^pt P₃₂(5/4)>36 | 不触发，差的符号为负 |

具体运算仅为：若所存 q=qₙ/q_d、P=pₙ/p_d、门限 a/b，比较 b qₙpₙ−a q_dp_d 的整数符号，分别取 (a,b)=(361,25)、(36,1)。实际输出两个 sign 均为 −1；使用 bundled Python 3.12.14 的标准库 json/int。没有重新求和 P₃₂、张量或任何 Fourier 系数。

根旧记录的三阶旧门是 q₃^ptP₃₂>16，它拒绝 μ₃=4，不能因此拒绝 μ₃=6。这里即使暂按该根记录的值判断，新 μ 的两个固定点门也没有触发；再考虑 n1280 缺少独立点值对照，更不能把它包装成新的已认证障碍。不触发同样不是 Mⱼ 的空间上界，也不是新指数包络通过。

用于去重及下文候选的指数多项式严格沿用 NODE_GATE_LEMMA.md：

\[
P_{32}(x)=\sum_{m=0}^{32}\frac{x^m}{m!}\le e^x\quad(x\ge0).
\]

同一旧节点记录中的已存值是

\[
P_{32}(5/4)=\frac{p_n}{p_d},\quad
p_n=216855050694226616015293034897070208000737154738853,
\]
\[
p_d=62130012247255622811856771761794767595935176327168.
\]

这些整数直接来自已绑定旧记录，不是本次新生成的指数证书。另实际读取已完成完整节点独立结果 full-nodal-independent-trial-01/result.json 的 exponential 小字段，其 x=[5,4]、terms_through_degree=32、lower 两整数与此完全一致；该旧完整节点指数接口已有 FULL_NODAL_RESIDUAL_OUTCOME.md 所记完整比较与终审来源。这里仅复用同一指数有理数的既有证据，不扩大旧独立点张量覆盖范围，也不重算旧残差。

其数学定义仍由上述正项多项式给定。未来执行入口须同时绑定引理、既有指数结果与其实际已接受来源，不可只复制一个脱离来源的小数。此门平方了导数靶标，指数参数是 **2t₀=5/4**，不是 t₀=5/8，也不是残差平方下界合同曾用的4t₀=5/2。

## 4. 唯一建议：原 n1280 的完整空间二阶必要门

因为第3节没有现成可用的新 μ 障碍，建议最多一次下述整数读档门。它测试固定 M₂ 包络的一条必要条件；不以单点上界生产为目标，也不选择新的观测点。

### 4.1 自包含数学式与最小工作量

在同一 t₀=5/8，以原精确参照系数 cₖ定义

\[
Q_2:=\|D^2v(t_0)\|_2^2
=\sum_{k\in G}|k|^4|c_k|^2.
\tag{NI.1}
\]

归一化体积给 Q₂≤‖D²v(t₀)‖∞,F²。全部有序二阶指标满足 Σᵢ,ⱼ kᵢ²kⱼ²=|k|⁴，故 NI.1 没有遗漏混合导数重数。

SD.1 和 SE.1 的逐模原分子表示为

\[
c_k=\frac{n_k^{c,0}}{2Qs_k},\quad s_k=|k|^2,
\qquad b_{k,0}=2048n_k^{c,0},\quad Q=2^{52}.
\]

所以空间权重与分母**完全消去**：

\[
N:=\sum_{k\in G}\sum_{a=1}^3
[(\Re n_k^{c,0,a})^2+(\Im n_k^{c,0,a})^2],
\qquad Q_2=\frac{N}{4Q^2}=\frac{N}{2^{106}}.
\tag{NI.2}
\]

若复用已认证的四层幂系数分子 b 档案，则只读取其第0层，并有

\[
B_0:=\sum_{k\in G}\sum_{a=1}^3
[(\Re b_{k,0}^{a})^2+(\Im b_{k,0}^{a})^2],
\qquad Q_2=\frac{B_0}{4Q^2\,2048^2}=\frac{B_0}{2^{128}}.
\tag{NI.3}
\]

两式是同一有理数的可选既有表示，执行时锁定其中一份完整档案即可，不为此生成第二套系数。恰有4912×6=29472个原整数标量平方进入全和；完整正负谱已计入，不能再乘2。零均值模按原定义为零，不进行除零；不能以模式很小或看似为零来删项。

这不需要逐模 Fraction、空间卷积、FFT、打包乘法、整数根号或新的中心量化。特别地不能用 QP=2⁹⁶ 的辅助中心替代原 c 而不支付其差；NI.2–3直接使用原有理场，故不引入 Eⱼ、Mδ 或残差误差。

### 4.2 唯一门及严格失败范围

固定检验

\[
Q_2P_{32}(5/4)>361/25.
\tag{NI.4}
\]

若用 n 档案，NI.4 等价于25Npₙ>361·2¹⁰⁶p_d；若用 b₀，则等价于25B₀pₙ>361·2¹²⁸p_d。只需最终整数交叉乘，不调用近似 exp，不选择新根号精度。

严格触发时，

\[
\|D^2v(t_0)\|_{\infty,F}^2\ge Q_2
>(361/25)e^{-5/4},
\]

从而 **这份固定参照的 M₂≤(19/5)e⁻ᵗ 包络被拒绝**。它同时拒绝 P.1 原完整梯度版本和 S.2 应变版本中这一个共同的固定 M₂输入；没有对 σ 的新下界或对完整 M₁ 的判断。

即使 S.2 只要求几乎处处包络，也不能把严格违规简单忽略为一个端点：原有限 Fourier C¹ 参照使 Q₂(t)连续，严格 NI.4 在 t₀ 给出与实际指数门的正余量，因此同一 I 的一个右邻域上仍违规。这里无需计算该邻域长度，也不产生新时间段。

若 NI.4 不触发，包括等号，则只记 **UNDECIDED_FOR_LINF**。Q₂只是下界，P₃₂也只用于一方向比较；不触发不认证实际 M₂上界，不证明这一包络可行，也不据此自动改点、加密或延长窗口。

### 4.3 输入验收、成本边界和停止

未来小核须复用**已经完成两核原系数算术连接与相应非作者验收**的 n 或 b 档案，实际硬绑定所选文件、格式/顺序、运行记录、源审查及原 manifest/modes/同一 Q52 块的来源链。这里的验收限于下述资源缺口补充所允许的算术范围，不是原生产核完整成本验收。n 的值/斜率及两端布局必须准确取 n1280 的原值；b 必须准确取 θ=0 的幂系数层。不能把已舍入中心、残差 W、S 或 Bernstein 系数当成这里的原分子。

主 SE 规定 n 档案2×2×4912×6×10字节、b 档案4×4912×6×12字节；独立路线若把同一 b 写为16字节 AH，应以明确的 AH=b 数学连接和实际全量系数对照验收，不能要求不同编码哈希相同。本文读取的是数学/验收合同，**没有在此宣称本次整段两核已完成全量比较**。下一入口使用届时已接受的实际来源连接，不把“合同要求比较”当成已完成比较。

**资源范围更新：** ONE_SEGMENT_HIDDEN_HELPER_RESOURCE_AUDIT.md 已确认两单段生产核调用 platform() 时存在未纳入自管 wait4 账目的 uname/file 隐式子进程路径，完整后代资源证据缺失；根已撤回原“全部资源收齐”的验收含义。原算术字节和已有实际观测保留，两核不重跑。ONE_SEGMENT_COMPARISON_RESOURCE_GAP_ADDENDUM.md 及其非作者审查仅允许后续一次既有档案完整算术对照；未来 n/b 来源连接可以引用该限定对照的实际结果，但不能把它称为生产成本补证。

即使未来对照及本必要门均完成，派生记录仍须携带 producer_resource_complete=false、resource_complete=false、certificate_ready=false、release_ready=false，并绑定上述三份补充/审计实际字节。对照的允许正状态只限 ARITHMETIC_AGREEMENT_WITH_PRODUCER_RESOURCE_EVIDENCE_GAP。本小核自身的资源观察须另行真实保存；它的成功不能消除旧生产成本缺口，也不能将本项提升为完整新研究证书或正式冻结就绪状态。

为避免把一个必要门扩成生产任务，可沿用已有单段导数核的60秒、256 MiB、16 MiB上限作为这个单进程小核的保守候选上限；这不是本次计时或成本保证。固定工作只含所选既有整数档案字节认证、29472项平方全和、上述一个门及小型证据写后回读；不写新的 Fourier 数组。默认静态入口不得求 Q₂；实际源码需审查后由根安排唯一执行。来源/格式/整除或资源检查失败即保留 FAILED/STOP，不自动更换输入、参数、精度或重跑。

实际结果至少保存原文件 SHA/顺序、取层规则、29472计数、N或B₀、固定正分母、旧 pₙ/p_d 来源、两个完整交叉乘整数及严格比较、实际环境与资源。不能预填触发或 PASS。本审计没有实施该源码，没有算出 N、B₀或Q₂。

## 5. 与同段残差认证的独立性和恢复边界

导数包络与完整残差是后验定理的不同输入。新残差段认证即使给出有效 r̄₀、r̄₂，也不推出 M₂或 σ 包络；反过来 NI.4 若触发，也不使已认证的残差上界失效。两者可以共用同一原参照的字节来源，但不能互相代替数学结论。此门不需要重算本次已完成的六个张量、旧节点卷积或残差。

同时，现有两单段生产的完整资源验收已按第4.3节撤回。隐藏 helper 的逐进程资源/完整日志缺口不能用后续较小运行、余量估计或经验补齐；本发现既不证明实际超限，也不自行证明某个算术值错误。未来允许的原系数对照或必要门只积累带此来源限制的算术信息，四项完整性/就绪标志继续为 false。恢复时不得把旧 run 的成功字样、限定算术一致或本门触发解释为旧生产成本已支付，不自动重跑旧核，也不据此生成完整新研究证书。

历史上的 ε=2×10⁻⁷统一二阶残差门已经由 FULL_NODAL_RESIDUAL_OUTCOME.md 的实际节点下界拒绝。参数化引理及旧导数文末“残差尚未计算”等文字属于当时状态，不能作为本次重跑指令。本文不重新选择 ε；NI.4 的目标是独立检验仍在使用的固定 μ₂，不挽回已拒旧 ε，也不预先否定其它经过另行证明的控制族。

当前准确结论仍是：有同一段的有限导数上界，但固定全窗指数导数输入未付；没有从这些粗上界得到新 μ 障碍。一个固定参照包络的否定或未认证，都不是原 NS 的奇性、全球正则性或一般后验方法不可能性。本文不新建正式包、不扩展节点、不触发任何科学执行。

## 6. 本轮实际来源绑定

以下路径统一相对于本反向工作树；SHA只绑定实际所读字节，不代替科学独立复算。数学文本读取用于对应第1–5节；小JSON只用于第3节限定的读档、两次有理比较及旧完整节点指数/比较来源核对。DI合同本轮定向复读的是原幂系数整数化与输出布局；此前本人为其作者，不冒称其非作者再审。没有把历史审查的来源范围扩称为本轮重新读取全部原始证据。
| 实际输入路径 | SHA-256 |
| --- | --- |
| `research/reverse/fixed-seed-global-screen/PARAMETRIC_COST_LEMMA.md` | `bcbb265b0b9639d2fcae54dddee5415cce0cec62f1874d008dc389d2ae7ea2cf` |
| `research/reverse/fixed-seed-global-screen/ONE_SEGMENT_DERIVATIVE_CONTRACT.md` | `a53006b424c2166ad943166abca8e284138e64d31a6d07131041f9da9afa229a` |
| `research/reverse/fixed-seed-global-screen/ONE_SEGMENT_DERIVATIVE_OUTCOME.md` | `ac2e7737600b1584da1ed47197335e84dedae4dc61659eae667847391acaa81f` |
| `research/reverse/fixed-seed-global-screen/ONE_SEGMENT_DERIVATIVE_FINAL_REVIEW.md` | `7300c2ec68e3eed0da855ab2c9303af6321fca301c666bd8c86f187e6100d111` |
| `research/reverse/fixed-seed-global-screen/STRAIN_CONTROL_REFINEMENT.md` | `d6ab251e47d5818078f045d3f0ab7aae778e8e624c468633c360a9ed08930e01` |
| `research/reverse/fixed-seed-global-screen/STRAIN_CONTROL_INDEPENDENT_REVIEW.md` | `628ced02a9107039119dcb1744a718db7e2a4b692444c9867b3c62886e39c42e` |
| `research/reverse/fixed-seed-global-screen/NODE_TRIAL_OUTCOME.md` | `5a95b85195250051cacfcbdbdee95609785cad0a1d5dc5be31045b08bba062dc` |
| `research/reverse/fixed-seed-global-screen/NODE_GATE_LEMMA.md` | `177fe82983bb8d6d3e172615c716176338bdc7e31cd546e0416b502b80dd76fb` |
| `research/reverse/fixed-seed-global-screen/NODE_GATE_INDEPENDENT_RUN_CONTRACT.md` | `56dc24b236fe6eeec1209a121534f9ba01137cb401089b2370055abd30100936` |
| `research/reverse/fixed-seed-global-screen/NODE_GATE_INDEPENDENT_RESULT.md` | `a74584ee7de5f14d8425f56ac4ac2ad0394c634b5e5950f071ad0ba326be92d0` |
| `research/reverse/fixed-seed-global-screen/node-independent-comparison.json` | `78d37a683c4476955dc02dc174aaa2b05f8945bd67f1adaa805d6d4301a56043` |
| `research/reverse/fixed-seed-global-screen/node-gates-root-run.json` | `681d8c1194a8f08869050a803ba08127703b021c4c0330368e7c0cd69f69fae2` |
| `research/reverse/fixed-seed-global-screen/ONE_SEGMENT_RESIDUAL_DENOMINATOR_LEMMA.md` | `de6b150813559e6d0856b3df8db77491c9a3da4cad1f07a3d94282cd29642104` |
| `research/reverse/fixed-seed-global-screen/ONE_SEGMENT_RESIDUAL_EXECUTION_CONTRACT.md` | `7687786631b17cb9f8e21b3f9723f3eeb8d6e16cf3415a246544cb5c4df9d8eb` |
| `research/reverse/fixed-seed-global-screen/ONE_SEGMENT_RESIDUAL_INDEPENDENT_EXECUTION_PREFLIGHT.md` | `fd77dcc9ac5f1ed822d3d14cd1eb8ca33eb242d5f2322f862b170bbbdf6ce8ea` |
| `research/reverse/fixed-seed-global-screen/ONE_SEGMENT_RESIDUAL_COMPARISON_CONTRACT.md` | `e6a39b644953609429d5d2560dad500026f2db31dca6f40bd52dfe47bccc86db` |
| `research/reverse/fixed-seed-global-screen/FULL_NODAL_RESIDUAL_OUTCOME.md` | `223c963e10ae14c93a231901dfe1554b8c61b63324537ebc250ddb7ae15d32ee` |
| `research/reverse/fixed-seed-global-screen/full-nodal-independent-trial-01/result.json` | `e637e7fcde5f2fa8ac7cf55d635ada579f6fae189ebf903b6a7a018c351e393b` |
| `research/reverse/fixed-seed-global-screen/full-nodal-agreement.json` | `f2ccad0d3a963e1a0bdbf0e9695e2979271807201ef3427964b2a11052511ed8` |
| `research/reverse/fixed-seed-global-screen/ONE_SEGMENT_HIDDEN_HELPER_RESOURCE_AUDIT.md` | `c971a90e0c7d230bd25df1dd80b2e27c74b9af089ad6194099e217e981a77c87` |
| `research/reverse/fixed-seed-global-screen/ONE_SEGMENT_COMPARISON_RESOURCE_GAP_ADDENDUM.md` | `212df48b07648511024524ab746d41ec3e419914cb111862ae3569663ccf9355` |
| `research/reverse/fixed-seed-global-screen/ONE_SEGMENT_COMPARISON_RESOURCE_GAP_INDEPENDENT_REVIEW.md` | `36141219e713ed8a72cb1c6cef9609d00e86aed36f7fd7d80e242d0331562e06` |
