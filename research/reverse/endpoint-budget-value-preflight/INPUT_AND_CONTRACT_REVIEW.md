# 固定输入映射与执行草案预审

2026-09-09，PRIVATE_CORE。结论：**PASS FOR INPUT METADATA / IMPLEMENTATION PREPARATION ONLY**。未发现阻止按固定设计准备实现的转录冲突；没有数组字节重验、运行许可或真实 NS 输入/门的新认证。
本人是旧输入/轨迹部分源码作者、本题求积与 helper 静审人，非 INPUT_MAP、两份映射或执行草案作者；本次为有明确历史的非盲 AI 非作者预审，不称新独立算术验证。

本轮全文读 `INPUT_MAP.md` 1–45 行、`bindings.json` 1–990 行、`input-bindings.json` 1–363 行、旧 `input-acceptance.json` 1–123 行及 `trajectory-archive-acceptance.json` 1–54 行、原 `checkpoints.jsonl` 全 17 行；结合上一轮已全文读的 EXECUTION_CONTRACT_DRAFT 1–27 行。
定向读原 `input-preparation.json` 4198–4295 行、独立 `verify-input-output.json` 1–84 行与 status 字段；比较 JSON 仅核 trajectory160_512 所有重复出现的端点身份、U 头、准确 time；manifest 仅核该轨迹 17 项 original/archive/restored 字段。初次单行比较 JSON 的截断输出不计全文；随后用 jq 定向取字段并核重复记录，没有复算比较值。
本轮另实际核两映射中全部 25 项文本的当前 SHA/长度及路径相符；这些是文本字节检查，不是 25 份科学内容全文或逐式重审。NPZ/gz 仅用 stat 核 17+17 个规则文件及长度；未打开、哈希、恢复或解码任一个二进文件。

| 本题停稿文件 | SHA-256 |
|---|---|
| INPUT_MAP.md | c098a6cd92976b269d1290223a86353d4798a108cabd857ecc836711425fe58a |
| bindings.json | 4e9755de7e6c1fdfac25d1e6f589e0acfb3374553d1f50d93bc02e3a865e9fab |
| input-bindings.json | 4285c18b4def69ac450cb0c7f10f44f640aa34ce4364241fdb3dabf2a413ccd6 |
| EXECUTION_CONTRACT_DRAFT.md | b44b689db1066ced1632be7fd033ead81fa398b89f1194249190b0b00f0936f6 |

**IC.1 全 17 项。** 逐项核端点序号 \(\ell=0,\ldots,16\) 对应原 \(j=0,32,\ldots,512\)，没有漏项、重复或换成 256 步轨迹。新相对路径加唯一仓库根后，逐项等于旧绝对 original_path；原 checkpoints 的文件名/j/SHA/bytes 与两映射及 manifest original/restored 一致。归档路径/SHA/bytes 与 manifest 及旧映射一致，当前 34 个文件的 stat 长度亦逐项相符；这不证明当前大文件 SHA 仍相同。
旧比较记录内同一 j 的所有重复 left/right 证据，其路径、SHA、bytes、time_exact 与新映射完全相同，U 头均为 `<c16`、非 Fortran、\((3,160,160,160)\)。两映射的每个准确 time 的十进字符串对象也逐项相同；首项是 0/1，末项与准确 T 对象相同。没有以小数显示、旧 G/W 或数值比较误差代替身份字段。
从原标签规则 \(jT/512\) 和 \(j=32\ell\) 得 \(t_\ell=\ell T/16\)；这里只核标签与字符串转录，不重新求值大有理数。旧 metadata.h 是原步长 \(T/512\)，未来重建须使用 \(T/16\)，且准确标签不抹除旧轨迹浮点推进/节点偏移，也不将保存态说成准确时刻的 NS 解。

**IC.2 T/M² 及原接纳。** 主 `/fixed_observation/T` 与独立 `/mathematics/fixed_observation/T`，主 `/original_norm_bounds/M_squared_interval_normalized` 与独立 `/mathematics/initial_error_and_original_norm_bounds/M_squared_interval_normalized` 均已实际定向读；逐个 numerator/denominator 字符串对象相等，并等于两映射的复制字段。没有做有理运算、转换、开方、根求值或区间重建。
主输出 SHA 为 `3f51705fbd934ce76d503c1c856566405ee3deb1760474b1c73ef6a6f481c61f`，独立输出为 `4ef16c30bb85b24f5ed6f6be973106764df26b33c3da0180ba4c531954fc32f1`；当前 SHA/长度与 `input-acceptance.json` 的绑定一致。接纳文件 SHA 为 `dbd34732c073507b6162a273fcf1ff6100cc3f723c24487ede079fba3f22d827`，明确接纳原范数区间与同一 C/T/转换类别，并明确 NS 到 T 存在及来源门均未认证。
主原输出保存的 PENDING_INDEPENDENT_VALIDATION 是当时状态；独立输出 VERIFIED 和上述后续接纳并不要求改写原输出。M² 采用原 normalized 平方范数区间的元素 0 作下端，不采用相邻 energy 区间、任何保存态能量或原 A0 上界；后续 M_- 浮点开方仍非严格下界证书。

**IC.3 直接元数据链。** 原 checkpoints SHA `c09ec65bb333d80622e80820ca3d6fe6f1b4a4e49e298681bd84df0eeb3128e2`；旧比较 JSON SHA `54b10d02c711086e838633b371eb601732f2bcd6a86ac02beeb99eee0cd650e1`；归档 manifest SHA `3b6405f0b35983a0906dc4838e0d5d2b769ffbf07f7bb5ac1e528db7763e1f61`；归档接纳 SHA `4ed22a75d682107e11597057736227221276aa7c10379eb1963290016079013c`。这些当前文本字节与映射一致；归档接纳只认证历史无损字节，不认证新重建或 NS。
两映射的 25 项 sources 在 absolute→repo-relative 的路径转录后，path/SHA/bytes 完全一致，且当前文本实测也全部吻合；可复核完整逐项表为上述已绑定 `bindings.json` 的 sources。原轨迹锁 `1db9488f94d01200377ac94cc57e17161091a87f7b0632ba03dc85b6924fa354` 只作为历史来源；本轮未核 Git 对象，不把旧 source-commit 声明转成新源码锁。

**IC.4 尚须在最终实现/合同付清。** 原映射 run_id 是 trajectory160_512，新适配 run_id 是 value-scout-160-512，schema 也不同；这是记录来源与新任务的明确区分，不可让 worker 误用旧启动器。两映射都不是最终 source-lock，25 项来源清单也不自动覆盖尚待运行前绑定的 worker、监督、helper、最终合同和本题映射本身；它们的准确字节与严格相对路径资格须另锁。
最终 worker 必须在唯一受监督生命周期内实际核 17 原件的读前/读后 SHA、长度、zip/NPY 头和 U 资格；当前 stat 不能省去这些动作，gz 不得暗中恢复替代原件。准确 T/M² 须与已绑定原字段核同，再从准确 \(T/16\) 和各准确时差作转换并保留误差；全 signed H₀/H₁、Hermitian/Leray 投影、共享物理斜率及所有完整差仍待源码审查。
执行草案的固定一次、无新配置、完整来源、失败保留、NUMERICAL_VALUE_ONLY 与当前映射相容。helper 调用资格见已停 FORMULA_SOURCE_REVIEW；草案末段的输入映射/64 点审查待付状态可在最终定稿绑定停稿证据，但不得提前宣告主 worker、监督、资源封顶或即时准入 PASS。未发现为准备实现必须换数据或补选参数的缺口。

仅使用文本读取、jq 字段选择/相等比对、文本 SHA/长度与二进文件 stat；科学 worker、科学模块导入/编译、NPZ/gz 打开/哈希/解码、FFT、科学数值求值、Git 与外发均 0。只写本审查，全文自读后停稿并另报 SHA。
