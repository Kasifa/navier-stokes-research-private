# 单段既有档案比较器：完整非作者源码审查

2026-09-08。PRIVATE_CORE。状态 `PASS_BOUNDED_ARITHMETIC_ONLY_COMPARATOR_SOURCE / COMPARISON_NOT_EXECUTED`。作者为 Pascal；本审查者完整分段实读其源码并独立核对数学映射、负对照及工程收束。以下固定字节未见剩余源码阻断；这不是已完成比较，不恢复两生产核的资源证书，也不使完整科学包就绪。

## 1. 最终字节与证据范围

`compare_one_segment_residual.py`：1054 行、58483 字节，SHA256：

`7e09b766feb86ac70bb1b05957903320d41069637d4c2ee23e8ebed88c6bd294`。

已依次读取初稿全部已有函数、完成后的 bounds/mutations、完整父端/CLI，并补读所有最终修订：独立实际来源/receipt/exit连接，实际区间收窄，隐藏 helper 分级，四 false 字段，三补充精确集合门，最后 receipt 峰值/尺寸失效路径。没有用旧草稿 hash 代替最终实读。

实际固定合同/补充：

| 文件 | SHA256 |
|---|---|
| `ONE_SEGMENT_RESIDUAL_COMPARISON_CONTRACT.md` | `e6a39b644953609429d5d2560dad500026f2db31dca6f40bd52dfe47bccc86db` |
| `ONE_SEGMENT_RESIDUAL_COMPARISON_INDEPENDENT_REVIEW.md` | `76be831347a8dcd4e4cf16721ad695497e88ab98d8a4c19f4a2fe91a20a6ac4e` |
| `ONE_SEGMENT_COMPARISON_RESOURCE_GAP_ADDENDUM.md` | `212df48b07648511024524ab746d41ec3e419914cb111862ae3569663ccf9355` |
| `ONE_SEGMENT_HIDDEN_HELPER_RESOURCE_AUDIT.md` | `c971a90e0c7d230bd25df1dd80b2e27c74b9af089ad6194099e217e981a77c87` |
| `ONE_SEGMENT_COMPARISON_RESOURCE_GAP_INDEPENDENT_REVIEW.md` | `36141219e713ed8a72cb1c6cef9609d00e86aed36f7fd7d80e242d0331562e06` |

审查者只读源码、合同、既存小元数据，并执行 ASCII/AST compile-only 和文件字节 hash；未导入比较模块、未执行任何 validator、--check-only 或 --run，未解码新科学二进制、计算新系数或执行数据比较。为核元数据字段，定向读取两源的结果 schema 和根退出验收记录；没有将相同 hash 的目视观察写成完整算术一致。

## 2. 来源及旧资源的准确门

固定两侧源码、run/result、根真实 exit0 记录、执行源提交、stdio 和独立 final receipt 均明确绑定。比较器还从已绑定的记录展开原 manifest/modes/block、旧 C0/rho、证明/审查、30 份主二进制和 11 份独立二进制的实际路径/hash/长度，逐字节认证；不能仅信一个完成字符串。

主/独立身份与模型均检查同一节点1280/1281、时间分母2048、QP=2^96、黏性1和完整 G/H。两侧记录的共享原输入 SHA 相同，runtime review 也实际连接。原 modes.npy 只解码固定 NPY v1 小整型模式表，完整确认4912个 G 模式及顺序，供原系数局部分母使用。

两侧 root 接受的 actual process exit0、实际 run/result SHA、实际归档总字节、全部二进制绑定与自身 stdout 最后一行分别连接；独立 receipt 还核其真实字节尺寸、run SHA、含自身总字节及 root 记录的末次观察。不能以 run 的早期成功字样替代这些门。

`check_primary_recorded_observations` 与 `check_independent_recorded_observations` 明确只核已记录的管理集合、退出和内部账目一致性。它们没有证明隐藏 platform helper 已计入；旧源码和根验收仍保持原 hash，资源含义被新补充撤回。最终三补充文件名要求精确集合相等，实际 SHA 逐一检查，并进入最终重新读取的 bindings。

## 3. 完整数学对象及计数

### 3.1 Df 到独立张量

主 D 的存储时间层0–5对应独立增量层1–6，二者文件均为6×H×2的signed31B标量序列。因此统一标量索引 i 直接对应，外部 theta 不应再平移一次数组。

对角取 D_j；非对角取 `(D_jl-D_j-D_l)/2`，先对差分子 divmod(...,2) 核零余数，再比较独立直接卷积整数。标量乘积的完整时间/空间卷积交换性支持这个极化身份；这里不是把有序 Fourier–Leray 双线性算子擅自对称化。源码不重算 C0*C0，也不把模相同当作值相同。

`compare_tensors` 遍历六张量、六层、全部35937模和实虚两项，精确计数2587464；没有跳零、只验共轭或选模代替全量比较。

### 3.2 W、S、原系数和中心

W 是7×H×6、signed34B，完整1509354整数；S 是13×H、signed68B，完整467181整数。两者逐个精确相等，零模另核全零。比较器没有第三次重算 W 的完整有序时间平方；它接受两套独立生产源码/实际回读证据，再核两份 S 全量相等。

主 hermite-b 与独立 AH 都是同一精确 `2^64 s a` 整数，故直接相等就是这里的精确同分母比较，无须再引入全局D。四层原幂系数覆盖117888实标量；三层新中心覆盖88416实标量；旧 C0 的29472标量另接原常数。逐项核主误差见证 `e=QP*b-C*2^64*s` 和独立商余 `b*2^32=floor*s+rem`，并按 0≤rem<s 与偶数平分规则核同一 C，完整117888份舍入连接。

### 3.3 范数、Bernstein、真实有理根和 Gamma

全 S 的二阶平方范数分母中 s² 正好消去，因此比较器按每时间层累加所有非零模 S/QP⁴；零阶则逐 signed S 对正 s² 作真正向下/向上取整，不能用截向零。共轭两侧已在完整 H 中，不能再乘2。所重组的 A2/floor/ceil/inexact 计数精确连接主记录。

主零阶每幂系数宽度≤35936/QP⁴；比较独立的13个精确有理值各自包含其中。正 Bernstein 权重 `comb(m,l)/comb(12,l)` 重建13层，每行/系数/实际传播宽度均核；零阶 Bernstein 包含宽度≤13×35936/QP⁴，二阶幂和 Bernstein 精确相同。它没有再算独立的全 Fraction 空间求和；这项来自已绑定的独立源码/档案，原合同只要求此处完整包含关系。

两侧最大 Bernstein 输入分别由各自完整系数确定。`validate_root` 用原有理输入乘 P² 后的真实分子/分母核整数 floor，ceil 只在真正有理平方相等时不加1；不会把整除商恰是平方误作原有理数平方。P固定2^128，保存的scaled/division/端点/equality均连接。E0/E2从相同四层 M/δ 精确计算并各加入一次；没有将 root 下端冒作原残差下界。

二阶输入相同使根号/原上界相同；零阶主上界≥独立上界。固定正因子3584/1023和max(rbar2,64rbar0)保持顺序，所以 Gamma_main≥Gamma_independent。两者按同一固定2/8085825严格比较；允许独立通过而较宽主界未认证，不能反过来统一改状态。没有选择新epsilon、求新指数、改变窗口或推到原NS解。

## 4. 七项实际变异及两个 synthetic 边界

每项先调用正常 validator 验 baseline，通过后把变异送入同一函数，只接受实际捕获 Mismatch；如果变异意外通过就停止整个比较。这里只确认源码义务正确，尚未执行，因此不声称实际九项都已拒绝。

| 实际项 | 正常及变异共用 validator | 非零来源/确定变异 |
|---|---|---|
| 新张量分量 | validate_tensor | 完整循环遇到的非零非对角输出，独立整数加1 |
| 奇数极化差分子 | validate_tensor | 同一有效非零见证，D_jl加1使差分子变奇 |
| W相位标量 | validate_equal | 完整循环中非零虚部，主整数加1 |
| signed S标量 | validate_equal | 实际非零S，主整数加1；不要求它恰为负值 |
| 新中心 | validate_equal | r=1..3实际非零中心，主整数加1 |
| q0包含端点 | validate_containment | 实际非零且非点区间；保持一端，只把另一端收窄到lower与truth或truth与upper的中点，得到排除truth的合法真子区间；宽度门保留 |
| 来源SHA | validate_digest | 实际已核源码SHA，确定翻转首位后与真实字节hash比较 |

所有必要非零见证均由完整已读对象中取得；缺见证必须报错，不能编造。初稿的区间变异是整体平移到truth+1..truth+2，不符合“原区间端点收窄”；审查指出后，作者按表中逻辑修正，最终源码已实际补读关闭。

synthetic 分列：(-3)/2的正确 floor/ceil=(-2,-1)，错误floor=-1必须拒绝；value=9/8、scale=2时scaled value=9/2，整数floor=4虽是平方，正确root整数边界仍为(2,3)，错误ceil=2必须拒绝。二者是通用边界单元，明确不冒称来自实际残差。总数固定7+2，无源文件变异或额外科学运行。

## 5. 自身资源、默认入口和最终失效路径

比较器只有标准库顺序解码/整数/Fraction/字节认证路径，不导入 NumPy、生产器、platform、subprocess 或线程/进程调度库；没有动态导入科学核、fork、Popen、system。环境只用 sys、os.uname 的五个明确字段和 os.cpu_count；checkout 仅读.git/HEAD/ref。已知 platform 隐式helper路径被删除，不能再拿旧资源报告证明它不存在。

最大同时主要数据块是两份W原始字节约103MB，或有限张量/模式缓冲，不把所有档案转成巨大整数/Fraction矩阵。该观察不是峰值或120秒可完成证明。实际单进程门为120秒、256MiB SELF峰RSS、8MiB全部新输出；START包含预核，首次算术前设置剩余报警时间，循环周期检查，写盘和最终receipt后仍检测。

默认/--check-only只解析源码、配置及已绑定metadata中的路径/hash/尺寸，实际核字节，不解码科学标量或调用比较函数。传递字节预核不是算术一致性检验；未给根源码审查时输出明确 SOURCE_REVIEW_NOT_BOUND。--run须有三补充锁、实际根源码审查、固定目录和两个外置普通/空日志的inode连接。根仍须用xb/noclobber创建日志；脚本不能从“空文件”证明启动前未被shell截断。

OUT排他创建，文件以xb或本目录唯一temp原子替换，实际全字节回读；失败保留，不自动重试。记录实际源、配置、commit和全部bindings。最终反查使用file_sha重新读取每个实际文件，未用Monitor.bind缓存冒充再次核验；源码、动态根审查及checkout也再核。

写run后及receipt后检查资源；receipt计自身精确字节定点，并在写后核实际总字节、峰值是否与所存观察相同。超限/晚期峰值未记录/字节不符会改写STOP/FAILED run、发出使旧receipt失效的末行并退出非零。最终验收须同时读exit0、最新stdout、匹配run/result/receipt及自身资源；不能只看早期comparison.json中的算术状态。flush/readback不作掉电持久性声称。

## 6. 永久携带生产资源缺口

唯一成功状态是 `ARITHMETIC_AGREEMENT_WITH_PRODUCER_RESOURCE_EVIDENCE_GAP`。result、run、final stdout及receipt均写 `producer_resource_complete=false`、`resource_complete=false`、`certificate_ready=false`、`release_ready=false`；初始/失败记录也不变成证书就绪。审查提出第四字段遗漏后作者补齐，最终版本已读。

因此即使未来执行全部算术一致和九项变异拒绝，本次仍只增加固定档案算术证据，不收取两生产核完整成本合同，不冻结完整研究包，不推断全窗条件、原初值全局性或奇性。旧源/档案/验收hash保持，隐藏helper审计和新补充的更正优先。

## 7. 实际静态检查

2026-09-07 20:48:19.344323 UTC，审查者以固定 bundled Python3.12 -B 读取源码，ASCII/AST compile-only，并从AST字面量提取22个固定pin逐文件核实际hash。生成code object未执行，未导入模块、未调用任何比较函数。实际输出：

```json
{"source_sha256":"7e09b766feb86ac70bb1b05957903320d41069637d4c2ee23e8ebed88c6bd294","bytes":58483,"lines":1054,"ASCII":"PASS","AST_COMPILE_ONLY":"PASS","module_imported":false,"code_object_executed":false,"comparison_executed":false,"actual_fixed_byte_pins":22,"out_exists":false}
```

作者另行实际 --check-only 的小记录已读：`one-segment-residual-comparison-static-check.json` 声明141个固定/传递SHA通过、stderr0、0.306208209秒、比较目录前后均不存在，源码同上，config=`c4a44731f0ce8f612533d1e76957bca7a8ca3705e03c05a8d08929281ecd382e`。这是作者的字节预核，不是本审查者的执行，更不是算术对照。该记录SHA `40be18d24a0ebcc2487231993664ece775ddaf6993adb9dc6f1aeeb606c470bf`，其stdout SHA `20872f609f1d7fdf6252c954fbb7876a4ad506daf2e07dc89899db0502236e62`。

最终源码或补充字节改变后须实际补读；本报告不自动覆盖修订版。当前没有执行比较、生成一致性结果或关闭完整证书。
