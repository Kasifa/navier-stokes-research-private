# SwirlRegeneration 包的最终独立审查

2026-09-07。PRIVATE_CORE。最终结论：**PASS FOR THE STATED TWO GATES；NO-CANDIDATE FOR THESE GATES / NOT CLAY。** 当前结论与最终证明、独立审查和来源范围一致，没有未关闭的阻断问题。本报告认证下列实际文件版本的有限数学范围；正式研究冻结及其源码提交仍须由 freeze.json 另行记录，不因本文件自动成立。

审查者 `driver_contract_review`（VALIDATION 中的 Rawls）不是第一代几何、局部余项或中心应变/正时间证明的作者。此前已独立重推并全文核验两项数学检验，分别写入 REMAINDER_REVIEW 与 CENTER_STRETCH_REVIEW。现在完成最终稿实际差异、裁决和来源/证据范围的核对；这一步不被重复计作另一份独立数学证明。

## 1. 最终证明与已审草稿的实际差异

已分别执行完整逐行 diff，并检查全部差异：

- LOCAL_REMAINDER_PROOF 相对 LOCAL_REMAINDER_DRAFT 仅有开头状态说明及末尾当前状态段的变更。局部存在区间、压缩常数、高阶 Volterra 与插值论证、u_tt 估计、第一代和反馈余项均没有改动。
- CENTER_STRETCH_PROOF 相对 CENTER_STRETCH_PROOF_DRAFT 仅改开头/末尾状态说明，并将第 4 节 LOCAL_REMAINDER_DRAFT 引用改到 LOCAL_REMAINDER_PROOF。已先核实这个最终依赖与旧稿数学相同，故没有引用到未经核验的新论证。周期像和、M_G 常数、中心投影符号、固定 δ、黏性结构及 Π 的正时间余项均没有改动。

两次 diff 的非零退出码仅表示上述已列文本差异，不是执行失败。没有用草稿 PASS 未经比较就认证最终稿，也没有回写草稿和其审查的历史状态。

## 2. 第一个门：真实第一代与最早模板回馈

本审查者在 REMAINDER_REVIEW 中已经独立确认：a 只固定一次；完整 Wiener 压缩在 T0=min{1/100,1/(256||a||A4²)} 上产生同一真实光滑 NS 解；所有高阶 Picard 界和强收敛在这个共同时间窗保持。余项来自完整无限维方程，而非 Galerkin 截断。

最终稿保留 n=P_MB(a,a)=B(a,a)≠0、m(t)=tn+r(t) 及 ||r||A0≤R0t²。因此第一代确实产生，不能把模板门的零值误写成没有新流场。

由 curl n=γa 及完整 Leray 自伴性，Q=〈a,B(n,n)〉=0。逐点为零的是移去积分投影后的三重积；a(x)·B(n,n)(x) 未被证明逐点为零，B(n,n) 和整个 P_T 输出也未被证明为零。真实反馈的完整误差界是

\[
|\langle a,B(m,m)\rangle|
\le Z[2C_0\|n\|_2t^3+C_0^2t^4].
\]

故它不能在所有充分小的正时间满足同一个正 ct² 下界。OUTCOME 只据此拒绝预定二阶领先模板回馈解释，没有排除别的方向、种子混合通道、更高阶或较晚时间的回馈。其表述与原合同匹配。

## 3. 第二个门：固定空间点的初始负拉伸项

CENTER_STRETCH_REVIEW 已独立确认完整四阶周期像和的绝对交换、全部 81 个张量分量的范数常数、M_G<11781/6250<2、径向 Fourier 中心 Leray 投影及固定 δ=1/100 下的严格负号。没有通过事后缩小初值尺度取得符号。

黏性对初始中心对称梯度的贡献为零，是实际径向旋流的精确恒等式。其余黏性和全部非线性仍保留在同一真实解的 A6 构造及 Π'' 余项中。A6 构造的时间段包含于既有解区间，光滑唯一性保证两次估计作用于同一个原解；欧氏/Frobenius 常数没有漏项。

最终稿及 OUTCOME 所声明的是

\[
\Pi(0)=0,\qquad
\Pi(t)\le-\frac{L_*}{2}t<0,
\qquad0<t\le T_{\rm comp},
\]

其中 x_c 是固定空间观测点。它不是随流追踪的材料轨迹；Π 也不是含输运和黏性的完整涡量模长变化率。OUTCOME 已明确这两项区别。其负号不推出别处没有正拉伸、此后不能翻转、全域涡量单调、普遍不拉伸或正则性。

T0、T6、Tcomp 通过固定初值的有限 Wiener 范数及已证常数严格定义，没有未经认证的数值时间长度。M_G 的显式粗数值上界是完整无穷级数的解析估计，与有限截断或数值 PDE 误差不同。

## 4. 来源与历史审计的实际范围

已全文读取 SOURCE_HISTORY_REVIEW，并核对其与本包的对象、来源和结论关系。它是另一作者的有界来源/历史审计，不代替数学全文审查。本报告没有重新声称读完它列出的 21 份来源全文或 282 份检索语料。

本次实际按字节重算其 21 项直接输入的 SHA-256 与长度，全部匹配；另按已说明的排序及 JSON 编码重算两组检索语料清单，20 份 R0.1–20 页面与 262 份顶层 R0.73 Markdown 的数量、总字节及 manifest 哈希均匹配。读取字节作哈希并不构成全文审读，也不是新科学计算证书。

另对本轮新强调的 first-cycle/PROOF §5 式(16) 作定向原文件复读：旧循环初值已经满足 B(N,a_cyc)=0。按相同 B 符号及周期分部积分，确有 〈a_cyc,B(N,N)〉=−〈N,B(N,a_cyc)〉=0。来源审计正确指出模板标量零值现象的既有先例，同时没有把旧向量场恒等式错误迁移成当前球形旋流的 B(n,a)=0。

固定 W、局部 q* 见证、周期 Green 定义和四阶 Newton 核已有冻结来源；本包不把这些重新称为发现。中心公式的定向历史检索未命中只是一项有界检索结果，不能证明领域新颖性。旧 RESCALED_EXIT_PROOF 已是来自真实 NS 方程的条件定理，来源审计没有将此前工作全部贬成静态或 NON-NS。

本包新增证明没有借用一个未读外部 NS 定理作为黑箱，也没有新增外部原文阅读记录。历史台账中的已读 Tsai 等文献不被算成本轮重新读取。来源审计的限定符合最终裁决。

## 5. 证据类别及 checker 的边界

已全文读取 VALIDATION 和 check_bindings.py。作者分工与既有审查记录一致：Pauli 写第一代几何，根代理写完整局部余项；Pascal 独立算中心应变，根代理另写正时间控制；本审查者未参与这些证明的撰写，而独立核对实际推导。版本差异核对不增加数学证明次数。

本包没有新的科学数值实验、参数扫描、频率截断、近似轨迹或图档。球面矩、壳计数及常数界均以解析方式计算；本报告不声称执行了新的整数证书或区间求解器。无图的图档/渲染项目为 NOT_APPLICABLE，不代表数学或来源审查省略。

check_bindings.py 的作用限于：读取已列输入、校验工作树内路径、逐条哈希及可选字节数，校验来源 JSON 的固定 schema，并重建两组检索语料的字节清单。它还读取各审查文件的实际哈希。这个程序不验证命题、常数推导或方程，不认证新数值时间窗；其 PASS 不能代替前三节的数学复核。本报告采用它能识别的统一 path/sha 表，并保留来源审计自己的 21 项 JSON 输入。

本次也独立核对 REMAINDER_REVIEW 的 4 项及 CENTER_STRETCH_REVIEW 的 9 项实际输入绑定，均未变化。最终完整 checker 的实际运行输出及运行日志由本包验证流程另行保存；日志只记录各次真实执行，不回填首次时间。

## 6. 最终裁决与直接绑定

OUTCOME 的 NO-CANDIDATE 明确限于所声明的两个门。第一代非零只是门槛输入；模板领先反馈失败与中心初始负拉伸共同完成本次有界筛选，不被包装成三个奇性障碍或三个研究阶段。

没有接受可迭代再生成机制，没有将 ∀N∃u0_N 换成 ∃u0∀N，也没有得到单个固定初值的无限尺度、无限维跨代误差、有限总时间或奇性。已经支付的无限维余项仅属于一个明确有限局部时间段。结论没有越界，也没有以自动增加 Taylor 阶或更换截止/尺度绕过筛选。

合同内未解决项：无。以下 17 个直接输入绑定覆盖根代理指定的全部 12 份当前文件、两份实际 diff 用草稿，以及三份实际复用/定向复读的旧证明。审查表不自绑定，也不绑定未来 freeze.json 或尚待生成的运行日志。被审文件改变后，本报告不能自动认证新版本。

本报告没有修改被审稿、旧冻结内容、git 或发布状态。全部科学核心继续处于 PRIVATE_CORE；本数学 PASS 不是公开许可。AI 独立复核不等于人类同行评审、形式化证明或 Clay 问题解决。

| path | sha256 |
| --- | --- |
| research/reverse/swirl-regeneration/CONTRACT.md | `c887d8cc20495f0cf2e80585e66f92663f82c605f923194d49df5dda44bc9e12` |
| research/reverse/swirl-regeneration/CENTER_STRETCH_CONTRACT.md | `4502487b1379740ea169e1e5d5f5faffd5e7c1d8ecd225dfd19516be7c574280` |
| research/reverse/swirl-regeneration/INDEPENDENT_DERIVATION.md | `1ee6495178a4d6def57e733765ae0b778a3c90abf3456c352776c77e6db39581` |
| research/reverse/swirl-regeneration/LOCAL_REMAINDER_PROOF.md | `f4b12d5a745ab5da6df578e4c6cc66184ea29edbb501f029a9ea983cf601ee9a` |
| research/reverse/swirl-regeneration/CENTER_STRETCH_PROOF.md | `4874268bd9fb9e21d609b10b776ba8cb66c0181973edeb161327f99a252bcb22` |
| research/reverse/swirl-regeneration/CENTER_STRAIN_DERIVATION.md | `65dcbe9cbafffc13289cb774426f6e18bf7edab230bb03324a7ea894f01c3bcc` |
| research/reverse/swirl-regeneration/REMAINDER_REVIEW.md | `0c73fb914be4e3d17886dfe4d3a0d6240f7c7a7f42066c4d6d39dfbc63684a77` |
| research/reverse/swirl-regeneration/CENTER_STRETCH_REVIEW.md | `d5ff3bf32b3a541431a344a101d6d6c7a392f9a5b5b8e069aafeb446b19f89dd` |
| research/reverse/swirl-regeneration/SOURCE_HISTORY_REVIEW.md | `d26440b8a929279e294ab4a6b7f1f6b4e0fd5a5380bf45cc28d3694f8e5faa63` |
| research/reverse/swirl-regeneration/OUTCOME.md | `0ad7cbccb6c758ebbb9165e785ae3746d203736e6766a3d2abf263904c95b2ab` |
| research/reverse/swirl-regeneration/VALIDATION.md | `18c08b81a6635bb4206559a4d1416c4741ed3430e323141e16f5b86ec0fa3899` |
| research/reverse/swirl-regeneration/check_bindings.py | `4527ad14512527f32d7eb256309edd4058fb583464a7da20132f606166b5b8b7` |
| research/reverse/swirl-regeneration/LOCAL_REMAINDER_DRAFT.md | `c0346e98e776e7a5526727fde1572f1fc543d66b8fd3c31450ca791ea7297f8c` |
| research/reverse/swirl-regeneration/CENTER_STRETCH_PROOF_DRAFT.md | `1eaf197ab6c8b443792cefadfbaac3d96bad3771a281fded32ca2d15d5c92283` |
| research/reverse/exterior-pressure/PROOF.md | `50df7a60076567acac9cbad6588132c3e0f49e77f84f17ee68e740a8a32478b9` |
| research/reverse/next-concentration/PROOF.md | `fafadaecc7972111cd6d55e5cfa5ede746f306353f8b953266dc37d37a39a7f1` |
| research/reverse/first-cycle/PROOF.md | `a87672a035f1c80a0225ce8956fca53ffc2eb07fdd4e83092505b4ac657f6120` |
