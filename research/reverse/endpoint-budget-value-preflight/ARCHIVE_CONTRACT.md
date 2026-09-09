# 四件数值派生文件的分块字节归档合同

本合同仅准备一次无损字节归档，不启动科学 worker，不重算数值，不改任何原 NPZ。根已实际完成唯一数值运行；本作者本轮只解析小 JSON 的身份/资源/来源/产物字段并哈希这些 JSON，没有打开或哈希 NPZ、导入、编译或执行归档源码。归档仍待非作者静审、源锁和外层监督准入。
原三条件由固定 `ROOT_RUN_OBSERVATION.json` 记录：根观察监督退出 0、父回执 PASS 和成功终端摘要；脚本再次将实际 execution/result 字节与此观察交叉核对，不仅相信布尔标签。原数值完成仍只是 NUMERICAL_VALUE_ONLY，不是 NS 门、严格单边量或时间误差证书。

| 固定元数据（实际读取所需字段并核字节） | bytes | SHA-256 |
|---|---:|---|
| `ROOT_RUN_OBSERVATION.json` | 1477 | `8496f6a0e32e09f23556edc82af0d45cc686a2b607f483940bbc822f0fc2cb13` |
| `numerical-runs/value-scout-160-512/execution.json` | 40208 | `670d621d6bc0f4c90f84c22d4cbb86e388c9339f6b0a2b084ae6cad419050007` |
| `numerical-runs/value-scout-160-512/result.json` | 67590 | `a2092ea5fbf9eff92afc43616bf60938a94a6a8a6ab804b5aa5b4b9ff48c7252` |
| `source-lock.json`（原数值运行的 48 项） | 10163 | `99908cbb6de3512db00feb819220ae958277fadc190a52549fb0ba73914bae7e` |

| 唯一允许的原 NPZ（只转录并交叉核两份 JSON，当前未读原文件） | bytes | SHA-256 |
|---|---:|---|
| `reconstruction.npz` | 15531558 | `a2676b5b028ba780e72ea426716d7d5d8a5c496dcb53385ccc6b2ea2aae12e85` |
| `terminal-compact.npz` | 176408080 | `739532d39cb410eafa9d3f996750effec02f8ab852afcf87004f997bf4586e1d` |
| `full-B216.npz` | 483731652 | `bf8ee1402dcf1c69bf1f1d1b0bdd13de268fb2eff0ac3aa0a26112fdbb75ec60` |
| `quadrature.npz` | 14490 | `225d39de3be8ced28812cfe4c76144d7a41e6e6c3fa1d13aa96676d6d9be0cc2` |

字节程序为 `archive_value_data.py`，CLI 无参数：`/Users/kasifa/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 -B /Users/kasifa/Documents/Math/navier-stokes-reverse/research/reverse/endpoint-budget-value-preflight/archive_value_data.py`。只由根另锁的短标准库外层监督执行一次；无辅助科学调用、数组解析、子代理计算、Git 或网络。
唯一输出目录是本目录 `value-data-archive-v1`；存在即拒绝，失败不得重试/复用。输出为四件对应的 `原名.part0000.gz` 等分块、`progress.jsonl` 和 `manifest.json`；临存 `.tmp` 失败时保留，原件始终完整保留。不输出新图、PDF 或恢复 CLI。
每原文件按连续 32 MiB 原字节区间分块，末块取余；1 MiB 缓冲流写，gzip level=6、mtime=0、空 filename。单 gzip 实际长度必须严格小于 40 MiB；达到门即 FAIL，不改变块长、重压或删除证据。独占 xb 临存、fsync、同目录 hard-link 无覆盖发布，只移除已成功发布的临时名。
原件分别核 before、压缩流、after 的总 bytes/SHA；每块记录序号、offset、原 bytes/SHA、gzip bytes/SHA，并实际流式解压核块长/摘要/CRC至EOF，同时连续累计整文件恢复 SHA/长度。末端要求无多余原字节、块数/区间穷尽、整件恢复与固定原记录一致；不落盘拼接大文件。
未来恢复按 manifest 的序号/offset 顺序逐 gzip 解压，只在原路径不存在时独占写临时文件；实际核完整 bytes/SHA 后无覆盖发布。各块摘要不能替代整文件恢复摘要，本合同不允许覆盖现有原件。
脚本核原数值 PID/父 PID、固定调用计数、实际资源回执、完整终端目录摘要、48 项父子来源 map 和当前文字源字节；所有源和前提末端再核，自身/本合同起终记录一致。两份原清单必须恰有上述四件，无重复、多余或漏项。
历史数值锁由字节脚本消费；新的归档源锁由外层监督消费，格式沿 `schema:1, bindings:[{path,sha256,bytes}]`，path 为反向树内规范相对路径。新锁至少包含本字节脚本、本合同、外层监督、归档审查、上述四份原元数据；不把 NPZ/gzip 放进外层源哈希，数组字节读取均留在归档生命周期内。新锁自身另绑定，不自绑定；外层须核起终来源和唯一字节进程身份。
执行前实际可用磁盘至少 2 GiB；字节任务独立墙时上限 180 秒、单归档进程 SELF 事后 RSS≤256 MiB、全部新输出（包括临存、进度、清单及外层回执/日志）≤1 GiB。外层核后两者的完整总量，不借用数值任务 120 秒/6 GiB，不相加不同进程峰值。
内部 `START` 在导入 time 后、其余标准库导入前；循环检查包括原件哈希、压缩/解压和末端来源复核，清单 fsync/无覆盖发布及实际清单回读后再次检查时间/RSS/目录字节。manifest 内 SELF/时间样本截止在清单序列化前，终端样本截止在清单回读后；两者都不是整个进程生命周期。
必须另由根短监督器从 Popen 前到 reap 后核完整 180 秒、超时终止/回收同一字节进程，并记录实际退出/事后RSS/全部输出。单进程内部 deadline 属协作式检查，不是阻塞 I/O 的硬限；超时可能使失败清单不完整，已有进度/临存和外层失败回执必须保留。没有这层监督不得声称完整 180 秒验收。
成功须 manifest.status=PASS、字节程序成功终端 JSON.status=PASS、退出 0，以及外层完整资源/来源回执通过；后序封口可失败，早落盘 PASS 不单独成立。失败时尽力写错误和全部已形成块状态/临存长度，不把部分 VERIFIED 当整包成功；磁盘写失败时不保证清单可写全，外层实际非零/超时仍为 FAIL。
复用 `ARCHIVE_PREFLIGHT.md` 的方法和其绑定的两份旧标准库归档组织；我是旧轨迹归档脚本及本适配脚本作者，不能称本稿独立盲审。形成中仅小 JSON 元数据读取/核验，源码全文静态自读后交非作者审查，不执行测试或压缩探针。归档完成只证明字节保全，不改变旧失败记录或数学状态。
