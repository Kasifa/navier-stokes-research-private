# 固定十七检查点的只读输入映射

2026-09-09，PRIVATE_CORE。**METADATA-MAP-ONLY；不是执行合同或新的数组证书。** 本人是 DESIGN 作者及旧数值源码/结果的审读者。本轮只转录、交叉核对文本元数据和文件 stat；未打开 NPZ/gz、未哈希大数组、未求根/时间/范数新值，科学 worker 0。

完整机器映射在同目录 bindings.json，schema 为 endpoint-budget-input-map-v1，SHA-256 为 **4e9755de7e6c1fdfac25d1e6f589e0acfb3374553d1f50d93bc02e3a865e9fab**。它含17个原 NPZ 与17个归档的绝对路径、原 j、端点序号、SHA/长度、原时间记录、U 头记录及25项实际文本来源绑定；它不是未来监督器的 source-lock。

下表文件统一位于 **/Users/kasifa/Documents/Math/navier-stokes-reverse/research/reverse/annular-source-observation/numerical-runs/trajectory160_512/**。原节点 j 与 AP 端点序号 ℓ 区分：j=32ℓ，准确 tℓ=ℓT/16；只有17个完整状态。原 metadata.h 是 T/512，不能把它当新16段重建的物理 h=T/16。

| ℓ / 原 j | 原 NPZ 文件 | 原记录 bytes | 原记录 SHA-256 |
|---|---|---:|---|
| 0 / 0 | checkpoint-000000.npz | 206343430 | 1fd52e997d7f1fff87fdbbe3aaf3141ed8d0ad05a740f776e92117ff1b38d417 |
| 1 / 32 | checkpoint-000032.npz | 206347734 | 976d99d0a2c36d717f90342c927c76540f4e4cb376a13339b931a1a0725b3719 |
| 2 / 64 | checkpoint-000064.npz | 206347738 | f2cc452cf84041614a9ad02c879d74e45dc7a00a694b94cf6b5b65728b1faff6 |
| 3 / 96 | checkpoint-000096.npz | 206347762 | ae989b9560d7adccc1f97bcc60b58a952259a881344edb089bb2fe673729e20d |
| 4 / 128 | checkpoint-000128.npz | 206347786 | 4fb0ddf437f678f3d104f8bbb8d4c6da8287c996ed2ff35ee9453a0c631dad9c |
| 5 / 160 | checkpoint-000160.npz | 206347798 | 31e5282718b2f731e6d8b110edad2625b2c1d43c2c90ead10bf726068eb3b92f |
| 6 / 192 | checkpoint-000192.npz | 206347790 | 9c8da8b8f57672d3eeb8ab72ac5d065293e99a098c847685652274e9391ae390 |
| 7 / 224 | checkpoint-000224.npz | 206347794 | a1c1d8dc9703bffec26233a3a5793f737d6d7c17160343ca3f25ecb1aaf5df8c |
| 8 / 256 | checkpoint-000256.npz | 206347790 | 05d16280c03c5177d6cec7eb3e6f42c4d9f7cf2a33c5aec3e38aaa56788f52ca |
| 9 / 288 | checkpoint-000288.npz | 206347830 | 842aeed2d6c55c3d3d4e6e9a7662f914538881929ba1cab43a0da83824855cd1 |
| 10 / 320 | checkpoint-000320.npz | 206347818 | b0942e7ed3df0eb44900a6b4ba4bcee7e0c2c9905a41efe3a145f10662526604 |
| 11 / 352 | checkpoint-000352.npz | 206347794 | 4048394320b3d8abc0e61c0fecd389b5ab4e1b3766a485720f89ffd24aae2ec8 |
| 12 / 384 | checkpoint-000384.npz | 206347814 | 1760201165ef4349afa8fc805c6050e0a6e55176e0d20dbe8dd5f5e241da4d44 |
| 13 / 416 | checkpoint-000416.npz | 206347822 | e1f2ce3b21d1883bd3bf004e24ab74a0dda30ecc8d9f2c346ac4ab7794a4eccd |
| 14 / 448 | checkpoint-000448.npz | 206347818 | 5afc228f088c63b5a9c1ab987672e6d9491a783926e53b44171b9fcd0bead15d |
| 15 / 480 | checkpoint-000480.npz | 206347838 | 4c404085048d517672950dd006b0bbad384c0d08c205f82fe5abfc4c993f68f6 |
| 16 / 512 | checkpoint-000512.npz | 206347814 | f0bbb17fd6f48f0c095a12210ca61a15f46eb04bb716115c500048666bbf894d |

原 checkpoints.jsonl、归档 manifest 的 original/restored_record、旧比较表的左右端点证据已逐17项相互核同。当前17原件及17 gz均存在，stat长度均与记录一致；**本轮没有重新核验它们的字节 SHA**。归档在同一 annular 目录下 trajectory-data-archive/trajectory160_512-checkpoint-NNNNNN.npz.gz。原件无需恢复；若将来缺失，只按旧 manifest 的不覆盖恢复规则另办并核原 SHA/长度，不用 gz 的 SHA 替代原 NPZ 的 SHA。

原比较记录中17个 U 头完全相同：成员 U.npy、dtype=<c16（complex128）、shape=(3,160,160,160)、fortran_order=false、无对象。原 NPZ 恰六成员 U/G/W/band1_modes/band2_modes/metadata_json，各加.npy；metadata_json 是0维 Unicode。模式轴为 0,…,79,−80,…,−1，整数 k 映射 k mod160；三分量轴0，双向 FFT norm=forward，保留cube K53，ν=1。此处是已记录资格转录，不是本轮解码验证；准确 AP 投影仍不可省，G/W 不是新连续历史。

准确 T 的唯一原字段是 annular-source-observation/input-preparation.json 的 **/fixed_observation/T**；其 numerator/denominator 均十进整数字符串。/fixed_observation/T_binary64 是旧转换记录，仅作对照。原 M² 区间在 **/original_norm_bounds/M_squared_interval_normalized**，元素0/1分别下/上端；不是相邻 energy_interval_normalized。DESIGN 的 m_- 直接指元素0，本轮没有开方或转浮点。

绑定链：原 input-preparation SHA **3f51705fbd934ce76d503c1c856566405ee3deb1760474b1c73ef6a6f481c61f**；独立 verify-input-output SHA **4ef16c30bb85b24f5ed6f6be973106764df26b33c3da0180ba4c531954fc32f1**。独立对应字段为 /mathematics/fixed_observation/T 和 /mathematics/initial_error_and_original_norm_bounds/M_squared_interval_normalized，已按原字符串对象核同。input-acceptance SHA **dbd34732c073507b6162a273fcf1ff6100cc3f723c24487ede079fba3f22d827** 绑定两原输出/回执并接纳上述类别；没有重作其精确算术。

轨迹原锁 /Users/kasifa/Documents/Math/navier-stokes-reverse/research/reverse/annular-source-observation/trajectory-source-lock.json 的 SHA 为 **1db9488f94d01200377ac94cc57e17161091a87f7b0632ba03dc85b6924fa354**；原回执声明运行前提交3922902291f1d3992d5568a2730391c9633cbfed。本轮只核元数据，未运行 Git，不能把此旧锁自动当新 worker 的锁。

原已测解释器为 **/Users/kasifa/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3**；trajectory160_512/result.json.environment 记录 Python3.12.14、NumPy2.3.5、Darwin arm64，NumPy路径也已复制到bindings.runtime。此次只核路径存在，未执行解释器版本探针；旧输入准备的CLT Python3.9.6不是本次浮点后处理运行时，旧线程环境记录null不证明新进程线程数。

可作为新适配参考的监督源码为 **/Users/kasifa/Documents/Math/navier-stokes-reverse/research/reverse/annular-source-observation/run_trajectory.py**，SHA **1ca483526338a3fc843403fec9e163bc06ab93cbc1a9b7ca4ab1e1704ed3cf5d**。可复用的是fresh父进程、唯一Popen/-B、排他目录、timeout kill/reap、身份/锁前后检查、CHILDREN事后RSS与分列SELF、失败保留。旧CLI的五个run-id/预算/依赖不能直接执行新任务；新监督与worker仍须按新合同审定。

本轮实际全文读旧主CONTRACT、INPUT_CONTRACT、input-acceptance、archive-acceptance及17行checkpoints；定向读input原/独立的T/M²字段和状态、全部17归档记录、比较表17端点头/身份、原trajectory环境/规范/回执锁。源码实读driver244–345、compare486–514/653–715及必要定位段、supervisor1–80/290–445；旧设计阶段已读的文档不冒称本轮重审。bindings.sources的25项文本均本轮实测SHA/长度，部分只作来源字节绑定，不声称全文阅读。

INPUT_MAP 与 bindings 已自读；DESIGN 9c6a9e66原字节未改。该映射不选择新配置、不授权重建/数组读取/FFT或任何科学运行，也不进入第30包。仅写这两个映射文件，停稿后由根另锁实现来源。
