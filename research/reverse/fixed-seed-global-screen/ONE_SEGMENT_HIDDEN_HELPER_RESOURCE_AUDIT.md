# 同一段两核的隐式 platform helper 资源审计

2026-09-08。PRIVATE_CORE。状态 `PRODUCER_RESOURCE_EVIDENCE_GAP_CONFIRMED / NO_REPLAY / NO_COMPLETE_CERTIFICATE`。

根代理在比较执行前发现标准库隐藏子进程；本审查者定向实读本机 bundled Python3.12.14 的 platform.py/subprocess.py、两份实际源码和现存 run/根退出验收记录后确认：先前“全部后代均由自管 wait4 收齐”及独立核“没有 helper”的资源判断不成立。已记录的管理进程账目不能覆盖 platform 的隐藏调用。两次已保存的算术字节、已观察退出和墙钟保留，但完整成本证据不成立；不以经验“小 helper”补账，不重跑两核，不修改旧 hash。

## 1. 受影响的两次实际调用

| 对象 | 实际源码/提交 | 现存 run 的时间（UTC）与父 PID |
|---|---|---|
| 主核 `audit_one_segment_residual.py` | SHA `f8f871684d68303de24a8901abb35266969d2f978d218ca9d14cd16ce45fac63`；commit `31f7f4e382732fb9e20cc0a50293b19d056d2fb3` | started `2026-09-07T20:22:10.405120+00:00`；finished `2026-09-07T20:22:53.118057+00:00`；PID 12238 |
| 独立核 `audit_one_segment_residual_independent.py` | SHA `1e9c9ee576049bd444ed07e858175b113bdb09d3719f1ab69820a3536564ca79`；commit `616b7ec2f3f6e0578bf07b9ced2ad6ccb1bc9cc9` | started `2026-09-07T20:29:47.638702+00:00`；finished `2026-09-07T20:31:11.383411+00:00`；PID 14452 |

run 的起止 UTC 字段与最早 monotonic 计时点、最后写盘观察不是同一个字段；不能把两个 UTC 的差值替代最终 elapsed。根已观察的最终调用墙钟约为主 42.786 秒、独立 83.789 秒；该已观察墙钟不会因这次发现变成未知。源码 START/ENTRY_STARTED 在 import platform 之前，环境查询及其同步等待发生在这段计时内。

主源码 :1200 在构造 environment 时调用 `platform.platform()`，随后 `platform.machine()`；此位置在自管 helper 调用、首次资源采样及 arm_deadline 之前。ParentContext 对象虽已创建，platform 的内部 Popen 没有通过其 spawn/helper 登记。

独立源码 :1065–1066 在 NumPy import 之后、数学 fork 之前依次调用 `platform.platform()` 与 `list(platform.uname())`。Resources 已创建，但其 children 仅登记 run_workers 中的六次显式 fork；没有监控标准库内部 Popen 的注册钩子。

## 2. 本地原文的完整调用链

本次读取的标准库路径为：

`/Users/kasifa/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/platform.py`。

其直接相关原文如下；这里只列定位与代码语义，不运行这些函数。

1. `platform()` :1239–1245 先查 `_platform_cache[(aliased,terse)]`，未命中即解包六项 `uname()`。默认调用为 aliased=False、terse=False。
2. `uname_result.processor` :858–860 是 cached_property，调用 `_Processor.get()`；`uname_result.__iter__` :862–866 显式附加 `self.processor`。因此解包六项以及 list(uname_result) 都会触发惰性 processor 的求值，而读取 `.machine` 本身不会。
3. `_Processor.get` :796–800 选 `get_<sys.platform>`，本文件没有 get_darwin，故落入 :819–836 的 from_subprocess，实际调用 `subprocess.check_output(['uname','-p'], stderr=DEVNULL, text=True, encoding='utf8').strip()`。
4. `platform()` 的 Darwin 分支经 mac_ver 读取 plist 后将 system 改称 macOS；后续不是 Windows/Linux/Java，仍落入 :1283–1289 的 generic 分支。terse=False 时执行 `architecture(sys.executable)`。即使 mac_ver 未得到版本、system 保持 Darwin，也仍是这个 generic 分支。
5. `architecture` :675–773 的 executable 非空时调用 `_syscmd_file`；后者 :641–673 跟随解释器 symlink 后执行 `subprocess.check_output(['file','-b',target], stderr=DEVNULL, env=...)`。不存在 architecture 的结果缓存；外层完整 platform 字符串缓存可能避免后续重复调用。
6. `subprocess.check_output` :466–467 转入 run(stdout=PIPE,check=True)；run :548 起自行创建 Popen/communicate，并由内部 wait 路径收取退出。POSIX `_try_wait` :2008–2018 使用 os.waitpid，不使用两科学脚本的自管 wait4，也不保存它们需要的逐 child rusage。

`mac_ver` 的 plist/os.uname 路径本身不是这里发现的 subprocess；问题具体在 processor 与 architecture 的两条调用，不能混称所有平台字段都需要 helper。

## 3. 缓存能说明什么，不能说明什么

`_uname_cache=None` 与 `_platform_cache={}` 是本模块的进程内初值，缓存不由前一次独立 Python --check-only 进程传递。`uname_result.processor` 缓存在那个对象上；完整 platform 字符串另按参数缓存。

在正常、未改写的当前标准库路径下，首个未命中的 `platform.platform()` 会走 uname 与 file 两个 check_output 调用点。两份现存 run 都保存 `platform="macOS-26.6.2-arm64-arm-64bit"`，独立 run 另保存 processor 项为 `arm` 的六项 uname 列表。与代码结合，这不是可以用“只读 os.uname”解释的输出；非空 processor 经上述子进程返回路径取得或从同一进程先前已取得的缓存读取。

独立核后面的 `list(platform.uname())` 一般读取刚由 platform.platform 解析的同一 processor 缓存，**不能因此再算一份必然的 uname helper**。若 NumPy 的更早导入过程已经温热 platform 缓存，首次求值可能提前到导入期间，仍在该父进程本次计时内、仍不在自管 children 表。对 NumPy 的三个直接初始化文件作定向文本检索未见相关调用；这不是整个动态导入图或原生扩展的穷尽证明。

本次没有当时的缓存快照、进程创建 trace、helper PID 或完整原输出，故不宣称精确创建了几次 helper、不编造 PID/退出码/峰值。特别是 `file` check_output 遇到 OSError 会返回默认，最终 `64bit` 可来自 pointer size，不能仅凭该字符串证明 file helper 创建/执行成功。可以确定的是隐藏启动/等待路径真实存在，现存成功平台字段不能排除未登记 helper，完整成本证据因此缺失；不能用缓存为零额外进程作证。

当前实际读取的 platform.py 字节也未作为原科学 run 的独立输入 pin 保存；本审计绑定当前文件和已记录的同一 Python3.12.14/路径，不能反向伪称当时已经记录了它的文件 SHA。这一额外来源限制不会修复原 child 观测缺口。

## 4. 实际账目中的缺失

主 run 的 child_processes 共 14 项：git-head、cpu、六个数学 worker、六次 rss helper。其 wait4 高水位和为记录内的管理对象提供了证据；名单里没有 uname/file。`parent_plus_all_child_highwater_sum_bytes=1722073088` 只能按实际名单解释，不能继续解释为全部实际后代之和。

独立 run 的 Resources.children 只包含六个数学 worker，实际 fork_preflight 的 Python/native 线程数均为 1。该线程检查没有追溯已经启动并退出的环境查询进程。`all_process_highwater_sum_bytes=710754304` 同样只覆盖 SELF 和六个已登记 worker；“无 helper”不能由这个字段名证明。

两边的 SELF ru_maxrss 不含孩子的独立峰值；现存记录没有可用于补齐隐藏 PID 的逐 helper wait4 rusage。check_output 自行 waitpid 后，不能在已经结束的科学父进程上再补取这些原始逐 child 观察。也没有留存足以替代逐 child 证据的当时完整 RUSAGE_CHILDREN/系统追踪记录。

隐藏 stdout 通过 PIPE 被标准库读取并变成部分平台文本，stderr 指向 DEVNULL，未按主核自管 helper 方式保存完整 stdout/stderr 和哈希。现有 scientific/metadata/stdout 档案的实际字节计数仍成立，但它不等于遗漏 helper 的完整日志证据。

因此：

- 总墙钟和已登记进程/文件的实际观测保留；本发现不证明两次实际超过 600 秒或 2 GiB。
- 全后代 RSS、逐 helper 身份/退出/高水位、完整日志的成本合同没有被证明满足；已有余量不能用猜测补齐。
- 这是成本证据缺口，不是由此发现了某个已存算术标量错误。两套新完整数值是否一致仍须另做数据验收，不能在此预填一致。

## 5. 对旧审查/验收结论的明确更正

本审查者此前的 `ONE_SEGMENT_RESIDUAL_PRIMARY_SYSTEM_REVIEW.md` 关于 wait4 独占全部 child 的表述，以及 `ONE_SEGMENT_RESIDUAL_INDEPENDENT_SYSTEM_REVIEW.md` 关于无额外监控进程/helper 的判断，漏审了标准库内部 subprocess，现撤回其“全部后代资源完整”含义。清理已登记 child 的修复、数学及 I/O 路径的其他静态观察不因此自动变为错误，但不能拿原 scoped PASS 绕开此补充。

两份根 execution-acceptance JSON 的实际 exit0、run/result/档案字节绑定是已有证据；其中“全部资源已经闭合”的解释须更正。本审计以新文件覆盖该解释，保留全部旧源、旧报告、旧验收及数据 SHA，不覆写当时记录、不事后伪造补充峰值。

当前不得据这些记录冻结完整科学证书或发布包。后续如根明确锁定一次既存档案的数据对照，可将其定位为算术核对而非补证成本：即使数据全部通过，也必须同时显式保存 `ARITHMETIC_AGREEMENT_WITH_PRODUCER_RESOURCE_EVIDENCE_GAP`、resource_complete=false、certificate_ready=false、release_ready=false，并继续保留本缺口。具体补充合同和比较源码尚须独立审查；本报告不自行授权执行。

## 6. 本次实际输入字节与操作范围

2026-09-07 20:41:55.440636 UTC 实际核对如下 SHA；只读本地标准库/源码/现存小 JSON，未导入或运行两个科学核，未解码新科学数组、重建系数、作卷积/比较、安装 trace、重现平台函数或执行 uname/file 探针。

| 输入 | SHA256 |
|---|---|
| 当前 runtime `platform.py`（43388 B） | `f5ff83f15c841792be42709a6710dc8d7a9f72791c1ae4cad719b1fb0abe0a05` |
| 当前 runtime `subprocess.py`（88747 B） | `85d29b2bf0249f5436838298c9a60ee93508b1102e9ac43b001f8a7e7ae8f375` |
| 主源码 | `f8f871684d68303de24a8901abb35266969d2f978d218ca9d14cd16ce45fac63` |
| 独立源码 | `1e9c9ee576049bd444ed07e858175b113bdb09d3719f1ab69820a3536564ca79` |
| 主 run.json | `869be6550d833d7021b130915c0ecb69e22545d8c4c03f4e99c790f15ba6a500` |
| 独立 run.json | `85ef60b89269eb2aacde9d054ef7eb055b22495e8cc3e6662094b14d557fc082` |
| 主根退出验收 | `c4c8ea70c33918ddea1d7cce74b89e7e97e99ff9be7aa3f74e73e3633562770b` |
| 独立根退出验收 | `5265d2ebe8a3af7bd822ecdcef2f68a6e20a567f4d84135af2ccabd10f154c49` |
| 主系统审查 | `349d47827bb6411862e3740a865a05207fa364d87634c95ed0a519a4e53bcdcf` |
| 独立系统审查 | `4130f8232b7282dbfd4168ea71d1ea666e563b99a6348f2dac10fd4e1d1e687a` |

此表是本次原文和记录的绑定，既不伪造当时缺失的运行观测，也不把未运行比较的结果提前接受。
