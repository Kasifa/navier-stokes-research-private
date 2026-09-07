# 固定二阶导数包络的单次整数必要门

2026-09-08。PRIVATE_CORE。这是执行前合同，尚未求 B₀，也不预设触发。执行和 Git 限本反向工作树。只授权下述同一节点读档门，失败保留 FAILED/STOP；禁止自动重跑、更换表示、改点或扩大范围。

## 数学目标与来源

采用 `ONE_SEGMENT_NEXT_INPUT_SCOPE_AUDIT.md` NI.1–4 及根非作者审查的证明。固定原六模初值、ν=1、无外力、三维2π周期环面、原有理 C¹ Hermite 参照 v；t₀=1280/2048=5/8，μ₂=19/5。仅检验这份参照的必要条件，不把 v 当作真实 NS 解。

唯一科学输入选 `one-segment-residual-trial-01/hermite-b.i96le.bin`，共1,414,656B，SHA `ba831967f4eeaa69bd7d16674c1f3a0cda913c14ac864d1dcfc6518e3ed1067c`。格式为4个时间幂层×4912个既定字典序双符号非零模式×3分量×实虚两项，每项12字节小端有符号整数。完整来源字节必须先验；只解码其首353,664B，即 θ⁰层29472标量。不解码其它层，不选子集或跳零，不读取第二套系数重算。

由已实际完成的两路线原系数全量比较，b₀为同一原节点系数的分子，cₖ=bₖ,₀/(2⁶⁴|k|²)，且 bₖ,₀=2048nₖ。读取时须检查逐值被2048整除，不能用这一整除替代来源连接。Q₂=‖D²v(t₀)‖₂²=B₀/2¹²⁸，其中 B₀是全部29472项平方和。每项只平方一次；可同时按3分量累加小计，供记录检验。

指数有理数沿用 `full-nodal-independent-trial-01/result.json`（SHA `e637e7fcde5f2fa8ac7cf55d635ada579f6fae189ebf903b6a7a018c351e393b`）中的 exponential：x=[5,4]、terms_through_degree=32、lower=[pn,pd]，

pn=216855050694226616015293034897070208000737154738853，
pd=62130012247255622811856771761794767595935176327168。

其 P₃₂ 定义和既有指数验收由 `NODE_GATE_LEMMA.md`、`FULL_NODAL_RESIDUAL_OUTCOME.md`、`full-nodal-agreement.json` 绑定；不重新求 exp 或选择精度。

唯一判定为 D=25B₀pn−361·2¹²⁸pd。D>0输出 FIXED_REFERENCE_M2_ENVELOPE_REFUTED；D≤0（包括等号）输出 UNDECIDED_FOR_LINF。两者均携带生产资源缺口。前者只否定同一参照在 t₀ 及其一个右邻域的指定 M₂ 包络，因此 P.1/S.2 的共同固定输入未付；不否定其它包络、控制族或真实 NS 解。后者不认证 L∞ 上界。

## 必要绑定及有限验证

执行源须固定上述文件实际 SHA，以及范围审计/根审查、本合同、原 manifest/modes/n1280所在Q52块、分母引理、主/独立生产源码和相应根验收、实际比较 comparison/run/final-receipt/根与独立执行验收。固定比较源提交为 `2e7ded4313eddbe7c2d7cbefc503d7bcb671b154`，comparison SHA `c0e454ac4fd980344c29704bdabb3e7dd8c00e00daac8942f3621d2c2428eba8`；比较器已唯一执行，禁止再运行。

同时固定 `ONE_SEGMENT_HIDDEN_HELPER_RESOURCE_AUDIT.md`、`ONE_SEGMENT_COMPARISON_RESOURCE_GAP_ADDENDUM.md` 及其独立审查。两个生产核完整成本证据不足；本次小核不补齐它们。所有成功、失败、收据及派生结论必须保留 producer_resource_complete=false、resource_complete=false、certificate_ready=false、release_ready=false；小核自身观测和上限可另记，不得混淆。

审查及静态入口只允许读字节、SHA、ASCII/AST与配置检查，不得解码科学整数或求 B₀。完整源码须经非作者审查、根全文读取、固定提交后才由根唯一 --run。执行时动态核验所传根审查的真实字节 SHA 和当前源码 SHA；不能使用自报 PASS 字段替代来源。固定源码/输入执行后再核字节不变。

负对照只需同一严格比较函数的正、零、负边界（故意把非严格条件用于零必须被拒绝），以及实际已绑定输入的 SHA 单字符变异拒绝；基线须通过。不得改原文件、重求整套范数或扩展科学工作。结果记录完整 B₀、3分量小计、29472计数、唯一固定正分母、pn/pd、两个交叉乘整数、D和严格判定。所有整数保持精确，不用浮点决定。

## 本次资源、输出和停止

标准库单进程，无 NumPy、FFT、卷积、根号、PDE步进、平台元数据 helper、subprocess/fork/线程/动态导入。元数据只读 sys、os.uname 的五个命名字段与 os.cpu_count，不使用 platform.platform/processor 或解包平台 uname。

从入口计时60秒，SELF峰值256MiB，全部本次输出16MiB，均为停止上限。逐批资源观察并覆盖写后阶段；单进程无需伪造后代资源。不能用旧硬件空闲数推断可分配保证。运行使用既有 bundled Python3.12.14，不安装或更改环境。

固定独占目录 `m2-necessary-gate-trial-01/`，固定外层 `m2-necessary-gate.stdout.log`、`m2-necessary-gate.stderr.log`。根通过 shell noclobber 重定向一次完整 stdout/stderr；无 tee 或管道。保存源码快照、配置、结果、运行记录和自洽最终收据，记录实际当前源码提交、进程、环境、时间、SELF峰值、完整输出字节和实际SHA。收据须包括自身、外层stdout/stderr，完成后回读核验；最终实际退出0和一致收据是接纳的必要条件。失败记录不得被后续成功覆盖，不自动重试。

无论必要门结果如何，本轮不新建正式冻结包、图档、公开内容或发布请求。继续研究从实际结果和限定适用范围出发。
