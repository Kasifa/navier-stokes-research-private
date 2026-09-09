# 唯一值侦察：结果与来源元数据审查

2026-09-09，PRIVATE_CORE。结论：**PASS FOR RUN METADATA AND REPORTED SCOPE ONLY**。未发现本次完成、来源身份、资源或结果解释的元数据矛盾；不是独立科学复算、浮点误差证书或真实 NS 结论。
本人为此前公式、输入、worker 科学及最终合同审查作者，不是本次 worker、监督器、运行观察或 OUTCOME 作者；这是有先前源码接触的非盲、非作者 AI 结果审查。本轮未执行科学、导入模块、打开/哈希 NPZ、复算 FFT/求积或运行 Git。
实际全文读 source-lock、live-launch-gate、ROOT_RUN_OBSERVATION、57 条 progress、stdout/空 stderr 及 OUTCOME；对 result/execution 定向读取全部身份、源映射、输入记录、头信息、完成计数、资源、产物清单、标量与诊断字段，并读 T/h/PH 及 17 节点时间记录。用 jq 仅作既存 JSON 字段/列表相等比较；不冒称逐项重新计算时间分数或全部 16 个 κ 延迟，也未复读锁内 48 份科学全文。

| 本轮实际小文本绑定（运行文件前缀为 `numerical-runs/value-scout-160-512/`） | SHA-256 |
|---|---|
| `result.json`，67590 B | `a2092ea5fbf9eff92afc43616bf60938a94a6a8a6ab804b5aa5b4b9ff48c7252` |
| `execution.json`，40208 B | `670d621d6bc0f4c90f84c22d4cbb86e388c9339f6b0a2b084ae6cad419050007` |
| `progress.jsonl`，57 行 / 10082 B | `575926a06c1a2a582ae72fbbcb7a63ae9fd80a332ba71c493cd84cdf9a3d283d` |
| `stdout.log`，110 B | `6a9abe7c49eaf51d37e0c771a26faad8a041137beb39d9e703b12548a4d4f602` |
| `stderr.log`，0 B | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| 本目录 `ROOT_RUN_OBSERVATION.json` | `8496f6a0e32e09f23556edc82af0d45cc686a2b607f483940bbc822f0fc2cb13` |
| 本目录 `live-launch-gate.json` | `8eeba79d80ff552bd92527b404f897cfc4fffd1fba6c9e3ae4f99de236b538f6` |
| 本目录 `input-bindings.json` | `4285c18b4def69ac450cb0c7f10f44f640aa34ce4364241fdb3dabf2a413ccd6` |
| 本目录 `source-lock.json` | `99908cbb6de3512db00feb819220ae958277fadc190a52549fb0ba73914bae7e` |
| 本目录 `OUTCOME.md`，本轮全文 | `d9fc8771ee5496c49828516e5e275d201444d5d25e9f7f3061a7177761f7607a` |

1. 17 个前记录和 17 个后记录的 path/SHA/bytes 列表均逐项等于 input-bindings；原 j 为 0、32、…、512。17 个报告 U 头均为 `<c16`、C 顺序、`(3,160,160,160)`、NPY 1.0。它们是唯一 worker 的实际哈希/解码报告；本审查不独立核旧 NPZ 字节。
2. 子 start/end 两个完整 48 项 map 均等于 source-lock；父 before/after 各 48 项的 path/SHA/bytes 与锁逐项相等，所有 match 为 true。当前小文本锁 SHA 与父、子、live 记录一致；源码 commit `97cdd8ca4cb849802709d283aba28ca344bfef8c` 和锁 commit `43231b9866e56cc6202a93b0602409ae4016d8eb` 是根外层 Git 核验记录，本审查未运行 Git 或重新哈希锁内全部源文件。
3. 子 PID 97788、父 PID 97786 在两份结果中一致；Popen、父 scientific_execution_count、子 scientific_worker_invocations 均为 1。子完成状态、completion_verified、源/计数门与父回执 PASS 一致；父回收子退出码 0。根观察记录另给 session28105 父工具退出 0、成功终端 PASS 摘要和已关闭状态，其 execution SHA/bytes 与本轮实际小文本哈希相符。最后一项是根现场证言，本审查未接管或重开原会话。
4. 17 次 RHS160、1 次 RHS216、54 批/162 标量 FFT 与原计数计划、父字段和进度递增相容；FFT 字典为逆160=34、正160=17、逆216=2、正216=1。规则生成 1 次、Φ 调用 2 次；57 事件包含 17 起点/完成对、全部 17 次后哈希及最终完成。这些记录与根唯一运行、未重跑的现场证言一致，本审查不据此冒称读过全部外层会话历史。
5. T、M² 区间和 17 个准确节点对象与 input-bindings 完全相同，PH_delay_scale 与 h 转换记录相同；浮点 hex、符号转换误差另存，不能把准确时间标签当无舍入的实际计算。报告原 M² 下端转换有正向舍入误差，`M_minus_num` 的命名不构成浮点严格下界。
6. 父 Popen→reap 为 17.748699583113194 秒，Darwin CHILDREN 峰值 4496424960 B；before 子资源为零，timeout=false，分别通过 120 秒/6 GiB。父 SELF 24051712 B、父序列化前 18.001250124769285 秒为独立采样；子内部 17.645842582918704 秒不替代完整父计时。完整目录 675803770 B、JSON 117880 B 与根终端记录相容；本审查不重哈希整个产物目录或将两峰值相加。
7. 启动前记录为内存可用 55%、磁盘 1320958500864 B、解释器可执行、17 文件长度符合、既定并发检查无匹配、run 目录未存在；均为根当时观测，不宣称现在仍有同样资源。worker/父报告 Python 3.12.14、NumPy 2.3.5、Darwin 与五线程控制值 1 相同。
8. 四份 NPZ 的文本 path/SHA/bytes 在子 artifacts 与父完整清单完全相同：reconstruction 15531558 B、terminal-compact 176408080 B、full-B216 483731652 B、quadrature 14490 B。progress/result/stdout/stderr 的实际本轮小文本 SHA 也与父/子相应记录一致。NPZ 双清单相符只认证所存元数据相容，不替代数组内容、一致性差或独立恢复哈希核验。
9. 原报告 Ū_num=81170397.46015947，B_BF,num=14.029969284966706，J_num=44.24470035614878，B_PH,num=69.33584473015269；Ū−B_PH=81170328.12431474、Ū/B_PH=1170684.4818299327。相同值在 result、progress 和 OUTCOME 转录一致。已存数的大小关系没有满足预锁浮点方向 Ū_num≤B_PH,num；没有重算比值、引入事后容差或由大间隔推出准确对象的反向不等式。
10. OUTCOME 的 `NUMERICAL_VALUE_ONLY / NO-NEW-CANDIDATE` 收口限本配置价值筛选，方向准确：不认证指定 RE 方法的严格阻断，也不认证其可行/不可行、真实 NS 门或寿命。它保留同一原 a_*、原 T、Π 后共享斜率重建、c_b=0，以及未付早先残差/完整历史/真实解至 T 的前提，未将旧 G/W 混作本重建历史。
11. 尚未支付的数值证据范围明确：完整 Hermite 身份差、两种 Gram/Bernstein 组织差及 64 点派生向量只报告已存 NPZ，本审查与根均未另行解码核验；C53 差 4.922544809863958e−6、C106 外尾 6.943272984837841e−7、权重和偏差 −1.3322676295501878e−15、Φ 端点差 0 均仅浮点诊断。若欲声称独立数值一致性或严格单边预算，尚须相应证据；现有限定报告并未声称这些，故不阻碍本次元数据接纳，也不授权追加试算。

以上十份小文本 SHA 实际核验；本轮新增科学运行 0、数组读取/哈希 0、代码修改/Git/外发 0。全文自读后停稿，保留所有原始结果不变。
