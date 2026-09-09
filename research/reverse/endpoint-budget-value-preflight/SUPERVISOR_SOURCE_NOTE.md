# 唯一数值取值监督源码说明

本稿只交付标准库监督器，尚未执行、导入、编译、测试或创建运行目录；作者全文静态自读不代替非作者审查或执行准入。
本轮实际全文读取 `EXECUTION_CONTRACT_DRAFT.md`（27 行）、旧 `annular-source-observation/run_numerical.py`（358 行）及本次最终 `run_value.py`（363 行）。
复用旧监督器的单子进程、标准库哈希、计时和资源记录组织；不导入旧监督器或科学计算核心。新 worker 的接口来自根明确给定的 schema，未读取形成中的计算源码。

| 源文件 | SHA-256 |
|---|---|
| `EXECUTION_CONTRACT_DRAFT.md` | `b44b689db1066ced1632be7fd033ead81fa398b89f1194249190b0b00f0936f6` |
| `../annular-source-observation/run_numerical.py` | `0ed3c383fca00253af2970665078be9e390da36fb21c684d67a92b75aeacc987` |
| `run_value.py`（363 行，18872 B） | `7bd7d434aff19dd004503d400ab0146669d96dec950b3916001583e543b50d2c` |

运行接口（仅供后续审查后由根唯一执行，不是本稿运行授权）：
```text
/Users/kasifa/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 -B /Users/kasifa/Documents/Math/navier-stokes-reverse/research/reverse/endpoint-budget-value-preflight/run_value.py --run-id value-scout-160-512 --source-commit <根已外部核实的提交标识> --source-lock <本反向树内锁文件的绝对路径>
```
固定子命令仅调用同目录 `value_worker.py --run-id value-scout-160-512 --output-dir <固定唯一目录> --source-lock <同一绝对路径>`；五线程环境变量均强制为 1。
锁格式为 `schema:1, bindings:[{path,sha256,bytes}]`；path 是本反向树内规范相对路径，禁止重复、符号链接及数组/归档条目。父进程核全部源起终字节，锁自身不自绑定。
最低绑定为本监督器、worker、`budget_formulas.py`、最终 `EXECUTION_CONTRACT.md`、`input-bindings.json`，以及旧 `numerical_kernel.py`、`input-preparation.json`、`input-acceptance.json`、trajectory160_512 的 result/execution/checkpoints 清单。
原 NPZ 的起终读盘哈希由子进程在其 120 秒内完成；父进程不把旧 NPZ 放入源码哈希清单，不解码任何数组。源锁、worker 和最终执行合同的实际字节绑定留待形成后支付。
子结果必须有同一 PID/父 PID、run_id、锁 SHA、完整 `path→sha256` 起终 map、整数 `scientific_worker_invocations=1` 和状态 `COMPLETED_NUMERICAL_VALUE_ONLY`。
另须 `completion_verified=True`；实际计数严格为 17 个检查点、17 次 RHS160、1 次 RHS216、54 次批 FFT API、162 次标量 FFT。父仅核这些字段，实际循环计数真实性须由 worker 源码和后续结果审查支付。
固定 Python 3.12.14/NumPy 2.3.5 由 worker 检验并回报；父锁定解释器路径，不另启动版本探针。源码提交、实时可用内存至少 40%、磁盘至少 8 GiB、输入文件资格和无并行 worker 由根在外部准入。
已有运行目录即拒绝；独占 stdout/stderr 与 `execution.json.tmp`，Popen 尝试至多一次，成功取得子 PID 后才计一次科学调用；超时/异常杀死并回收同一子进程，保留失败材料且不重试。
120 秒界涵盖 Popen 开始至 reap；新鲜父进程的 Darwin CHILDREN 用户/系统 CPU、峰值 RSS 在回收后记录，6 GiB 是事后门，不是实时 RSS 硬限制。
SELF 的 CPU/RSS 与父墙时截止于源/结果核验及首次产物哈希之后、回执序列化之前；不声称完整父生命周期，不与子峰值相加，也不声称同时总峰值。
完整输出逻辑字节包含日志、失败临存和回执，门为 1 GiB；全部 JSON/JSONL 及其临存加回执为 16 MiB。回执序列化固定点核自身字节，随后无覆盖发布，再核完整产物字节及前后哈希一致。
回执不自哈希；成功终端摘要另给回执 SHA 和含回执的完整清单 SHA。最终封口异常可能发生于回执发布后，故接纳必须同时要求监督器退出 0、回执 PASS 和成功终端摘要，不能单看早已落盘的 PASS 字段。
父 PASS 仅表示完成、身份/来源和资源门通过；不表示数值不等式、真实 NS 门、严格时间误差或机制结论。实际计算、worker 非作者审查、源锁和根的最终准入均未由此源码准备支付。
