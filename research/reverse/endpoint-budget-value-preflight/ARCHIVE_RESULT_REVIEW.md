# 唯一字节归档结果元数据审查

2026-09-09，PRIVATE_CORE。结论：**PASS FOR ARCHIVE RESULT METADATA**。四件、23 块的来源/覆盖/恢复记录及完整监督资源相容，未发现阻断项。本审查未打开、哈希或解压 NPZ/gzip，实际恢复由唯一已审字节程序完成；不是第二次独立恢复或科学复算。
本人为此前本归档源码静审及本题科学/结果审查作者，不是归档程序、监督器或根现场观察作者；这是非盲、非作者 AI 元数据审查。根对现场退出与 Git 的证言不能冒称本人实际执行。
本轮读取 manifest 的全部文件/块/前提/自身源/资源字段，execution 的身份/起终来源/输出清单/资源字段，全文读 50 行 progress（首次合并输出截断后补读末四行）、stdout/空 stderr、根观察及 live-gate；新锁按完整 bindings 比较，旧科学双清单定向复读。不冒称重新全文审读锁内 65 份资料。

| 本轮实际小文本绑定 | SHA-256 |
|---|---|
| `value-data-archive-v1/manifest.json`，31514 B | `5222ffe99e18ca9720886c69d219b2392e766b658076b654ed383136b314ef41` |
| `value-data-archive-v1/progress.jsonl`，18424 B | `ff140211bf1195eb17c8f9699e9224ee859f8c9ce193886d2f76065119eaa899` |
| `archive-supervision-v1/execution.json`，30896 B | `bab27692ddbbee63edf467f4613c4af5c364beb8d6e80d807434a718964854d2` |
| `archive-supervision-v1/stdout.log`，403 B | `b9f094196014f1ad770be406d66ae35c5be47db5f7c97568ea4f28b0756599b5` |
| `archive-supervision-v1/stderr.log`，0 B | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `ROOT_ARCHIVE_OBSERVATION.json` | `e4355653c975a3e9512a205b175d100727e6164a253dfcab401d6f48bc77dff8` |
| `archive-source-lock.json` | `71e7619e824e48fdbbda293f9b6ef60d1c8cbc9b4d0cf551ede7ceaf7e568da4` |
| `archive-live-gate.json` | `754d982cadb25dd6ac534bb7d683a849bf2bcf1ae6d709cef8fa4326b1ede1dd` |

1. manifest.selected 的四件 path/bytes/SHA 与原 result `a2092ea5…`、execution `670d621d…` 的两份 NPZ 清单逐项一致；四件 before/stream/after/whole-restored 均等于各自 expected，status 全为 VERIFIED。旧科学清单沿此前已实核停定字节，本轮仅比较 JSON，不读取原件。
2. full-B216 为 15 块、quadrature 为 1 块、reconstruction 为 1 块、terminal-compact 为 6 块，共 23 块；序号从 0 连续、offset 为此前块末端，各非末块 33554432 B。两大件末块分别 13969604 B、8635920 B；逐件长度和与最后 offset+length 都精确到原件末端，无间隙或重叠。
3. 全 23 块 raw/restored 的长度和 SHA 逐项相同、状态 VERIFIED；所有 gzip 长度严格小于 41943040 B。每块压缩 bytes/SHA 有实际程序记录，gzip 参数为 level=6、mtime=0、空 filename。此前已审程序在真实 gzip EOF/CRC 后才形成这些状态；本审查确认记录相容，不把元数据比较冒称再做 CRC 或解压。
4. 四件 gzip 字节和依次为 466359429、9268、7473499、166350373 B，与根观察相同。progress 有 23 对 chunk_start/chunk_verified 和 4 个 file_verified，共 50 条；全部 chunk_verified 的序号/offset/raw/compressed/restored 字段与 manifest 完整相同。父输出清单的全部 23 gzip 路径/长度也逐项匹配，未见失败临存条目。
5. 新锁为 65 项，父 sources_start/end 全部 bytes/SHA map 均等于其 bindings，起终锁身份相同；manifest 自身脚本/合同起终记录一致且对应此前审定 `9dc9b322…`/`897c4733…`。旧 48 源/四份原前提保留在字节程序记录中；没有把新锁计数与原科学锁计数混同。
6. 子 PID 1909、父 PID 1907 在 manifest、子 stdout 及父 execution 一致；byte_child_invocations=1，所有 scientific_worker_invocations=0，child_exit_code=0、reaped=true、timed_out=false。manifest/子终端/父回执均 PASS；根另记 session67319 父工具退出 0、成功封口及关闭，终端 execution/manifest SHA 与本轮实际小文本哈希相符。本审查未接管原会话，未把字节执行算科学执行。
7. 父完整 Popen→reap 为 16.542058124905452 秒，CHILDREN 峰值 30179328 B，通过 180 秒/256 MiB；manifest 序列化前 16.484661125112325 秒/29900800 B，子清单回读后 16.485494208987802 秒/30130176 B，均为较早内部采样。父 SELF 22839296 B 单列，不相加为并发峰值。完整新输出 640273806 B 与父清单加实际回执字节相符，小于 1 GiB；子目录 640242507 B 没有冒称包含外层日志/回执。
8. live-gate 记录当时磁盘 1319855468544 B、四件常规文件与长度相符、两个新目录不存在、解释器及既定并发检查通过；这是当时根观测。源 commit `37bdca0bce1c7493a101ec8a95fff6a5153a8164`、锁 commit `9f17cb0c5c400d01004c9f75b44a6d97979c86a1` 为根外层绑定，本审查不核 Git 对象。根观察中的 Git 保存 pending 是其记录时刻局部状态，后续真实 Git 保存应另以新证据绑定。
9. PASS 限已审程序报告的无损字节保全及元数据/资源一致；原文件保留，不替代独立数组科学一致性检查、单边舍入/求积误差或 NS 门。失败不重跑边界保持，本轮不授权追加恢复、计算或参数变更。

八份小文本 SHA 实际核验；字节元数据的相等、计数和长度检查用 jq，一个初始元数据查询语法错误已更正，未触发字节/科学程序或数组读取。全文自读后停稿；新增科学/归档执行、NPZ/gzip 读取/哈希、Git、外发均为 0。
