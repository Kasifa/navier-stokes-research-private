# 单段主核系统路径：非作者源码审查

2026-09-08。PRIVATE_CORE。状态 `PASS_BOUNDED_PRIMARY_SYSTEM_SOURCE_REVIEW / NO_SCIENTIFIC_EXECUTION`。本审查仅负责资源、I/O、来源和失败路径；根代理另作数学与完整实现审查。审查者未参与主核编写，发现的问题均由作者修复；实际补读修订后，在以下固定字节范围内没有剩余工程阻断。本审查不授权运行、不替代数学全审，也不证明该核能在候选预算内完成。

## 1. 实际覆盖与绑定

被审文件为 `audit_one_segment_residual.py`，最终 1361 行、75363 字节，SHA256：

`f8f871684d68303de24a8901abb35266969d2f978d218ca9d14cd16ce45fac63`。

执行合同 `ONE_SEGMENT_RESIDUAL_EXECUTION_CONTRACT.md`，21723 字节，SHA256：

`7687786631b17cb9f8e21b3f9723f3eeb8d6e16cf3415a246544cb5c4df9d8eb`。

合同的独立数学/成本边界审查 `ONE_SEGMENT_RESIDUAL_EXECUTION_INDEPENDENT_REVIEW.md`，13032 字节，SHA256：

`92af668f2a3fdfe081eb99123af63d781a7e2de90fbba158c70c852b9d868afc`。

分次实读覆盖完整源码：常量/pins、CLI/preflight、Context 和 ParentContext、原两端重建的档案接口、六 worker 的入口/调度/等待/验收、W/S/Bernstein 的 I/O 和停止接口、父端最终收束；最后逐项补读 dispatch 修复、日志句柄立即登记、helper 退出竞态、元数据回读和宽限期逐 PID 回收。数学公式及全谱结论的正确性由另行数学全审承担，不能由本报告中的工程 PASS 代替。

只执行了固定 bundled Python 对源码字节的 ASCII decode、`ast.parse`、`compile(...,'exec')` 以及小 JSON/日志/hash 核对。生成的 code object 没有执行；没有导入被审模块，没有运行其默认入口、`--check-only`、`--run` 或 worker，没有调用重建、舍入、FFT、乘法、积分或数学函数。作者实际 `--check-only` 的留档在第 7 节另行注明，不冒称本审查者运行过该入口。

## 2. 入口、唯一执行和来源

默认、`--check-only`、`--describe` 经同一 `preflight` 返回；该路径检查平台/Python、源码 ASCII/AST、27 个证明/输入实际字节 SHA 和配置 hash，不加载 NumPy 或调用科学函数。`--run` 必须额外提供根源码审查文件的实际路径和 SHA，且该文件实含当前源码及最终执行合同 SHA；通过这些检查后才进入排他 OUT 创建。

源码不把自己最终 hash 或自己的审查文件 hash 硬嵌进配置，因此没有源与审查互相要求预先固定的循环。根审查是外部人/代理的实际审读证明，代码中“包含两个 hash”只是运行连接检查，不能自动判定审查正文通过。运行者须传入根实际最终审读的审查文件。

固定 OUT 使用 `mkdir(exist_ok=False)`，已有空目录也拒绝；RUN_CLAIM 使用 `open('x')`，已有失败目录不复用。两份外置 stdout/stderr 在启动前要求与 fd 1/2 的实际 inode 一致。启动者仍须依最终 CONFIG 以 `xb` 或 shell noclobber 排他创建这些日志；被调脚本不能回溯阻止 shell 在它启动前截断旧日志。此启动条件现在已明确记录，不可用普通覆盖式重定向替代。

worker 必须持有父端固定 request SHA、实际父 PID、claim、配置及源码 SHA，独立排他创建各自 claim。固定六个新 Python 子进程通过文件取得原 C0 和新 C 输入；没有大型数组/整数的 IPC，也没有递归启动 worker。父端只读调用 `git rev-parse HEAD`，cwd 为反向工作树，用于记录实际源码提交；最终 source byte pin 仍独立核验。记录 HEAD 本身不替代根在执行前固定源码的责任。

正常完成前再次核验全部 27 个输入/证明、主源码及根源码审查文件实际 SHA。worker 也反查本身来源与 request/input。输出中保存源与配置快照、原证据连接、各 worker request/record/artifact SHA；研究范围仍是同一固定有理 Hermite 参照段。

## 3. 六进程资源和计时

所有子进程由 `wait4` 独占回收，Popen 对象登记 returncode，运行期间没有 `poll`/`wait` 抢先消费退出资源。父端保存每个 worker/helper 的 PID、argv、起止、退出码、CPU 和 wait4 高水位；Darwin ru_maxrss 按字节，Linux 按 KiB 转换。周期 `ps` 只查询父进程及受管存活 worker 的 PID/RSS，不保存其他用户进程命令行。

资源检查包括父进程自身峰值、存活进程同次采样和采样 helper 的峰值，以及父峰值加全部已经创建的子进程高水位的保守和。退出子进程峰值没有丢弃；每个子进程最终都须 wait4 收齐。保守峰值和可以高于真实同时使用量，尤其会累计多次短 helper 的峰值；报告不能把它叫作同时物理 RSS。代码按这一更保守量拒绝超限，符合合同的候选资源语义。

600 秒从模块最早 `import time` 后的 monotonic 点开始，包含预核、重建、worker、合并和最终回读/记录；不声称覆盖解释器启动之前的时间。父与 worker 的计时连接到同一父起点，SIGALRM/SIGINT/SIGTERM 转为受控停止。辅助 OS 命令有独立 2 秒截止；运行中约每 8 秒采样/记录进展。操作完成后和最终写盘后继续实测，任一被观察到的 600 秒、2 GiB 或 512 MiB 超限不能保留完成状态。

这不是 OS 防止短暂超分配的承诺，也不是 600 秒执行时间证明。静态审查不能替代实际每个进程的峰值和完整运行日志；本轮没有测速、调整参数、安装或改变线程环境。

## 4. 档案、回读和失败留存

所有新科学二进制写到固定 OUT 的直接文件；原子写使用独有临时名、`xb`、flush/fsync 和改名，新科学档案拒绝覆盖。预算计入 OUT 的临时文件、所有日志/元数据和两份固定外置 stdio。并发写入可能使瞬时预估并不精确，但当前代码持续观察总字节并在 quiescent 最终阶段重新实测，不能在观察到超限后成功。16 MiB 元数据余量用于失败收束，不能理解成磁盘永不会写满的保证。

每个科学 artifact 写后实际全字节回读并比较内容及 SHA；worker 的 raw 乘积、解码 Df 和正负回打包有完整字段连接。父端逐 worker 验完成身份、退出、记录、固定四份档案/三个乘法，再作合并。W/S 的完整字段回读/连接保留，最终再次验证全 30 个二进制档案尺寸/hash，合计必须恰为 288713460 字节。这些数学字段连接仍须根数学审查和未来独立复算，不能只凭 hash 判数学正确。

小元数据现在也有实际回读：Context 的每次 checkpoint 对照期望 canonical bytes；配置快照对照 canonical bytes；源快照对照固定源码 SHA；result 由实际 JSON 解析后比较。run 记录源/配置快照大小、SHA 和回读状态。run 不内嵌自身 hash；最终 stdout 绑定实际 run 文件，外置日志在 run 内注明只绑定最终行之前的前缀，避免自引用。最后观察还包括上一条 final stdout 的字节。

受控失败路径先保留异常及状态，最终统一 TERM、短宽限、KILL、逐 wait4 回收，再 flush/fsync/close 子日志并记录其实际字节/hash。每个清理操作的错误均累积，继续处理其他 PID/日志，然后禁止成功。原 partial/temp 文件保留，没有自动删除、重试或换目录补跑逻辑。启动 claim 前后失败可能只有完整外置 stderr/stdout 和 partial 目录，不能要求尚未创建的 run 已存在。

若终端/磁盘本身拒绝最终写入，最外层给出非零退出和 `scientific_completion_admitted:false`（在仍可写时），不能保证不可写存储上的完整新记录；实际验收必须同时检查最终 stdout、退出码和被绑定的 run/result，不能只看到较早 result 或中间完成字样就收取证书。不可捕获的进程/系统故障也不属于静态源码能保证完整留档的范围。

## 5. 实际发现及修复关闭

B01（草稿控制流阻断，已关闭）：在 1132 行未完成稿，dispatch 只 spawn/记 request 即返回，而等待六 worker、完整验收和 18 次计数块误置于 `norms_and_bernstein` 的 `return result` 后，成为不可达代码。未运行即由控制流文本发现并报告。作者将整块恢复到 `dispatch_workers`；最终实读确认合并只能在等待与完整验收之后开始。

B02（小元数据回读缺口，已关闭）：早版配置快照缺少实际回读/绑定，checkpoint 只原子写。作者补 canonical bytes 实际回读，源/配置快照元数据绑定；已读最终实现。没有添加额外大核或重算。

B03（清理异常会提前中断其余清理，已关闭）：后版已对 KILL/wait4/日志操作收集错误，但宽限期 `reap` 仍可直接抛出、跳过之后的收束。作者在最终 f8f 版逐 PID 捕获并累计，继续其余 PID 及 KILL/log 路径；已读该实际补丁。

作者自查的相邻修复也已实读：每次打开日志立即登记句柄，第二次 open/spawn 失败仍可收束已开句柄；helper 超时 kill 与正常退出的 ProcessLookup 竞态被处理；日志 flush/close/hash 错误逐项保留后继续。上述修复均未通过科学运行“测试”；证据是最终实际源码文本和静态检查。

## 6. 完成语义与范围

正常路径完成算术和全部文件/来源反查后先进入 `VERIFIED_FINALIZING`，收齐所有子进程和资源后才可进入 `PRIMARY_COMPLETE_PENDING_INDEPENDENT_REVIEW`。写最后 run、final stdout 后仍有资源检查；超限会改 STOP 并发出替代先前 final 行的记录，返回非零。

因此这里的 scoped PASS 只表示未发现剩余工程阻断。它不是已执行、不是独立对照通过，也不是全窗连续残差或原初值全局结论。根数学/全实现审读和一次固定执行的实际参数、排他日志、最终字节及资源验收仍须单独成立；后续独立核及完整逐输出对照仍须完成。没有新的科学运行结果，也没有推送、发布或提交。

## 7. 实际静态证据

审查者实际命令入口：

`/Users/kasifa/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 -B -`

cwd：`/Users/kasifa/Documents/Math/navier-stokes-reverse`。2026-09-07 20:13:06.686855 UTC，Python 3.12.14。stdin 只读取源码/已存小 JSON/日志，执行 ASCII decode、AST parse、编译成未执行 code object、SHA 和 JSON 一致性断言。实际输出：

```json
{"source_lines":1361,"source_bytes":75363,"ascii":"PASS","ast_compile_only":"PASS","module_imported":false,"generated_code_executed":false,"scientific_execution":false,"author_static_log_and_stdout_binding":"PASS","out_directory_exists":false}
```

作者另存、审查者实际读取并校验日志字节绑定的记录：

| 文件 | 实际字节 | SHA256 |
|---|---:|---|
| `one-segment-residual-primary-static-check-02.json` | 1661 | `39ca4f42f39c4fa707fc233e67a0ead7323dc1d70e45a0a0b17120e2fbe677a6` |
| `one-segment-residual-primary-static-check-02.stdout.log` | 5690 | `7ec028a3c58113e78eaf056d2760bc03da3d1c8026d58afa4bd1e3a140b5141d` |
| `one-segment-residual-primary-static-check-02.stderr.log` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

作者记录的实际 `--check-only` 为 exit 0、27 pins PASS、0.147955083 秒、stderr 0、科学目录运行前后均不存在。审查者对该 JSON/实际 stdout 中相同源码与配置 SHA、27 pin 数及日志 SHA 做了实际交叉检查；没有把作者记录改写为自己的运行。固定 config SHA 为 `d67fb54134a11fb93ca56e4ed8bafe6094840e5d4e327a2a90a1f4479c051372`。源码、配置或启动约束改变后，本报告不能自动迁移到新字节。
