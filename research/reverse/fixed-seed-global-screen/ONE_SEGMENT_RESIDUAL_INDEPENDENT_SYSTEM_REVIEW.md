# 单段独立核：系统与资源非作者审查

2026-09-08。PRIVATE_CORE。状态 `PASS_BOUNDED_INDEPENDENT_SYSTEM_SOURCE_REVIEW / NO_SCIENTIFIC_EXECUTION`。本审查完整读取 Rawls 编写的独立源码，只负责入口、fork、资源、I/O、来源与失败收束；根代理另审全部数学和实现。实际补读作者最终工程修订后，下面的停止路径和来源问题均已关闭，工程范围内没有剩余阻断。本报告不是运行授权、数学全审、预算可完成性证明或科学结果。

## 1. 实读来源与静态范围

最终绑定 `audit_one_segment_residual_independent.py` 共 1135 行、55015 字节，实际 SHA256：

`1e9c9ee576049bd444ed07e858175b113bdb09d3719f1ab69820a3536564ca79`。

初审完整读取的是 1060 行、50966 字节 `92cb79e0af4ddd3ef1f817fbce6f1221609bf680a85fb64e5aef2b82de2cca5c`；此后实际补读最终 Resources 初始化/回收/report、fork 观测、CONFIG/CLI、final_receipt 和主异常路径改动，不把旧版结论只靠刷新 hash 迁移。

实际读取全部函数和 CLI，包含 SOURCE/INPUT pins、Resources、原节点/Fraction 重建、worker/六 fork、W、S、Bernstein 的工程接口以及父端最终 receipt。数学正确性及独立性全审不由本工程 PASS 替代。本轮不读取主核新结果来验证独立结果，不改作者代码，不执行 git、安装或科学核。

已读独立执行合同 `ONE_SEGMENT_RESIDUAL_INDEPENDENT_EXECUTION_PREFLIGHT.md` 的资源/入口/I/O/失败章节 §7–9 及对应根合同审查；初始源码固定的合同 SHA 为 `fd77dcc9ac5f1ed822d3d14cd1eb8ca33eb242d5f2322f862b170bbbdf6ce8ea`，合同根审查 SHA 为 `8244f7b4d2137c71c60f169b022d5cf238bebef50b00692a40d48cb32e00fb24`。最终静态核验从 AST 的两个字面量 pin 字典提取并逐文件实际核对全部 21 个 SHA，包括上述合同/审查；没有执行源代码求值。

审查者实际只对源码字节 ASCII decode、ast.parse 和 compile 成未执行 code object，并读取本地 C 头文件和计算小文件 SHA；没有 import 被审模块，没有执行它的默认入口、--check-only、--run，没有调用 Resources/native API、构造科学数组、复算系数/张量或测速。静态代码对象也没有执行。

## 2. 默认入口、唯一目录与来源

默认和 --check-only 在任何 NumPy import、原数组读取或 reconstruct 之前返回。顶层仅加载标准库、声明 ctypes 结构、常数/有限配置，不运行科学函数。静态入口实际检查 ASCII/AST、固定计数以及全部 INPUT/SOURCE 文件字节 hash，输出不等于已运行。平台和 --run 的原生日志/线程条件须在真正启动时另行满足；一次 check-only 成功不能预认运行环境条件通过。

--run 先检查实际根审查文件、其 SHA、当前源和合同 SHA，以及 PASS 文本连接。该字符串检查只负责来源连接，根必须传入真实完成的审查文件，不能将任意包含这些字符串的文本当作独立审查。源不内嵌自身/动态根审查的最终 hash，避免自引用循环。

OUT 用 mkdir(exist_ok=False) 排他创建，成功、失败、空目录都不复用。随后 claim 保存配置、源码/输入 hash、身份与启动阶段，再作全 pins 和数学输入来源认证。失败前科学是否真正开始可由 stage 区分；尚未开始的绑定失败不是残差或数学失败。

源码只读反向 worktree 的 .git 指针、HEAD、commondir 和 loose/packed branch ref，确认 codex/ns-reverse，记录实际 commit；不启动额外 git 进程，不变更 Git。最终会复查实际来源 pins、当前源和 checkout。动态根审查的最终复核已在最终源补齐，见 §6。

## 3. fork、NumPy 与线程条件

NumPy 只在 --run 后载入；原科学数组和 Fraction/中心在父进程构造完成，六个 worker 使用 os.fork 继承这些只读输入。没有 multiprocessing queue、完整 G² 矩阵或大型结果 IPC；每个 worker 保存自己的六层增量张量，父端逐文件读取和合并。NumPy object 向量的元素仍为 Python 整数，源码没有 BLAS/dot/FFT 或内部并行后端调用；此处只审运行路径，不代替根对全有序对计数的数学审查。

启动要求全部六个线程环境变量为字符串 1；fork 前同时要求 threading.active_count()==1 和实际 proc_taskinfo.threadnum==1。后一条件检查原生线程，不把 Python 层单线程或环境值单独当作充分证据。最终版保存这次两个实际读数、UTC、PID 至 fork_preflight，并由资源 report 带出。若 NumPy/动态库已启动其他原生线程，代码拒绝 fork。检查后的父端代码没有显式创建线程；仍不应将此具体路径的受检条件推广为任意 macOS 库在 fork 后普遍安全的定理。

每次 fork 前屏蔽 ALRM/TERM/INT，父端登记实际 child PID 后恢复屏蔽，避免受管中断落在 PID 已创建但未登记的窗口。child 进入单独 try/finally 并用 os._exit；即使 worker 自己的异常记录失败，也不能落回监督进程异常路径重新调度/清理其他孩子。worker 移除父报警计时器、按行/序列化阶段检查本身时间和 RSS，监督进程负责统一 600 秒截止和全部孩子回收。

## 4. 本地 proc_pidinfo ABI 原文核对

本次只定向读取已安装 SDK 原头，没有网络检索、安装、编译 C 探针或调用该 API。MacOSX26.5.sdk 的实际内容与 Python ctypes 声明一致：

- sys/proc_info.h:124–143：proc_taskinfo 前六项 uint64_t，后十二项 int32_t；resident_size 明写 bytes；第十个 int32_t 是 pti_threadnum。
- 同文件 :726–727：PROC_PIDTASKINFO=4，返回大小为 sizeof(proc_taskinfo)。
- libproc.h:96：proc_pidinfo(int,int,uint64_t,void*,int) 返回 int，匹配 argtypes/restype。
- sys/fcntl.h:258：F_GETPATH=50，支持源码对实际 stdout/stderr fd 路径的读取。

按声明大小为 6×8+12×4=96；resident 偏移 8、threadnum 偏移 84。代码同时要求 ctypes.sizeof==96 和每次 proc_pidinfo 返回完整尺寸，读取失败不得成功。实际执行中的数值/可调用性尚未在本审查测试；本地头文件核对不是未来运行观测。

| 本地原头绝对路径 | 字节 | SHA256 |
|---|---:|---|
| `/Library/Developer/CommandLineTools/SDKs/MacOSX26.5.sdk/usr/include/sys/proc_info.h` | 31262 | `e427fa96b348537b21552b9de71e01039410bcad2cedee5584c5e5fddafd70fc` |
| `/Library/Developer/CommandLineTools/SDKs/MacOSX26.5.sdk/usr/include/libproc.h` | 7575 | `246d87709fc6b9157ce5cf3c475656ac48e0e1ae8bbdc46cf45acd34294448cd` |
| `/Library/Developer/CommandLineTools/SDKs/MacOSX26.5.sdk/usr/include/sys/fcntl.h` | 26949 | `805fd8c695f8e5e1c327b6852382cc5533738bbfd8f18bc11f850531166e4fe8` |

## 5. 资源、文件与最终完成语义

每次采样记录父进程与存活孩子的 proc_pidinfo resident 总和；各孩子退出都由 wait4 保存退出码和 Darwin ru_maxrss 字节数，加入持续保留的高水位账目。父进程 highwater 加全部孩子 highwater 的和是保守量，可能重复计算 fork 共享页面或不同时出现的峰值；不能冒称它为同时物理使用量。完成要求同轮采样总和的峰值和最终高水位和均不超过 2 GiB；缺少任意孩子退出资源不能成功。各 PID 的 proc_pidinfo 调用依次发生，不是跨全部 PID 的原子瞬时快照；完整 wait4/父 SELF 高水位保守和是另一个必要门，不依赖把这些分次采样说成真正同一瞬间。源码没有额外监控进程或创建线程，避免漏计旁路 helper。

计时 START 位于最早 import time 后，600 秒包括绑定、原数组/系数、fork、全部 direct 工作、合并、完整磁盘回读和元数据/最终 receipt。候选成本没有由有限源码审查证明；2,171,496,960 个 Gaussian 产品不因为六进程而减少。代码约每 0.2 秒在监督可执行时采样，worker 每固定 128 行记录进度。长 Python/C 操作与调度可使实际采样间隔大于名义间隔，记录中有实际时间戳；不宣称 OS 防止瞬间越界。

总输出统计遍历本 OUT 全部文件并计入外置 stdio；按 inode 避免重复计算实际同一外置文件，含进度/资源日志和部分文件。元数据/外置日志独立 8 MiB 门、失败预留 1 MiB，总 512 MiB 门；11 个固定二进制合计 169192128 字节只是档案尺寸，不是对象 RSS。新二进制使用 xb，逐全字节回读并核完整标量；小 JSON 写后也作实际字节与解析对照。失败文件保留，没有自动清理、重试或改变参数。

最终版要求 stdout/stderr 为普通且空的文件，并明确根启动者须用 xb/noclobber 排他创建；regular/empty 检查不能自行证明排他创建，不能让 shell 在脚本拒绝旧目录前截断旧日志。普通 flush/readback 证明当前文件字节回读，不等于掉电持久性；最终版 final_receipt 已在注释与 persistence_scope 明确不作 fsync/掉电持久性声称。

成功路径先完成所有科学/来源/子进程资源，写 run 后再采样/写后检查。stdout 明示验收还要求 final-receipt.json 和退出 0。receipt 在 stdout flush 后计算其自身字节定点、排他写入并回读，再观察实际全部字节、墙钟和峰值；晚期父峰值变化也拒绝成功。若这之后任一受控异常发生，FAILED_COST_NOT_PAID 的 run 和非零退出覆盖早期成功判断。不能只读较早 run/status 或 stdout 的 COMPLETE 字符串；须核最终 receipt 所绑定的实际 run SHA 以及最终退出码。

磁盘/终端本身不再可写或进程被不可捕获地终止时，任何源码都不能承诺完整新证据落盘；缺 final receipt/资源/成功退出即不接收证书。本报告没有将静态 I/O 设计写成已完成的运行或独立结果对照。

## 6. 实际发现与修复关闭

B01（阻断，已关闭）：初版 finish_children(terminate=True) 的 TERM、宽限期 reap、KILL/wait4 对单个 PID 抛出异常时直接退出，外层只记录 resource_accounting_incomplete，其余活孩子可能未被尝试终止或回收。作者最终改为每 PID 累积异常；先遍历全部 TERM，2 秒宽限逐 PID 非阻塞 wait4，随后先向全部未回收 PID 发 KILL，再作 2 秒逐 PID 非阻塞回收和末次扫描。重复错误只累计 attempts，不无界复制日志；清理 sleep 的受控异常也记下并继续。全部 PID 尝试结束才统一判失败，未回收 PID 明确列出，不能收作完整资源证据。OS 拒绝回收时不会为等待单个 PID 无限阻塞其他收束。父异常路径将 cleanup_errors 与全部 child 账户先保存，再分别尝试失败资源采样/report，不因一次后续报告异常丢掉已经获得的孩子账目。上述实际修改已读。

B02（来源完善，已关闭）：初版最终 pins_check 不含动态 root-review。最终版在完整科学工作之后、完成状态之前，对该审查文件重新核其实际 SHA，连接启动时已核的同一审查字节。

小澄清均已关闭：CONFIG/CLI 明示外置日志由根 xb/noclobber 创建，运行前检查普通/空文件；final_receipt 精确限定 flush/readback；fork 前两个线程数及 UTC/PID 落入资源记录。没有因此安装、改变数学参数、扩大窗口、运行线程探针或执行任何科学测试。

## 7. 实际静态检查

2026-09-07 20:21:14.035821 UTC，固定 bundled Python3.12.14，以 -B 和 stdin 小脚本读取源码文本、三份本地头文件，作 ASCII/AST compile-only 和 SHA：

```json
{"source_sha256":"92cb79e0af4ddd3ef1f817fbce6f1221609bf680a85fb64e5aef2b82de2cca5c","source_bytes":50966,"source_lines":1060,"ASCII":"PASS","AST_COMPILE_ONLY":"PASS","code_object_executed":false,"module_imported":false,"science_executed":false,"output_dir_exists":false}
```

初次检查没有加载或执行作者模块，也没有初始化 ctypes 资源查询。最终版另于 2026-09-07 20:24:53.759059 UTC 实际作同一固定 bundled Python -B 文本检查；从 AST 提取 INPUT_PINS/SOURCE_PINS 字面量并实际读取每个文件字节，比对全部 21 个 hash。未执行被审代码对象、默认入口、--check-only 或 --run，也没有解码旧科学二进制。实际输出：

```json
{"source_sha256":"1e9c9ee576049bd444ed07e858175b113bdb09d3719f1ab69820a3536564ca79","source_bytes":55015,"source_lines":1135,"ASCII":"PASS","AST_COMPILE_ONLY":"PASS","code_object_executed":false,"module_imported":false,"science_executed":false,"actual_byte_pins_pass":21,"output_dir_exists":false}
```

当前科学目录仍不存在。上述证据只支持此固定字节的工程审查；源/config/启动约束改变后必须补读，不能自动沿用。任何未来完成仍须根数学/完整源码审、唯一执行的最终 exit/run/receipt/resource 字节验收及完整独立结果对照分别成立。
