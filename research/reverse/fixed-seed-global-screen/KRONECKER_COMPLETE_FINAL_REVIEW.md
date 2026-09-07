# 单个完整张量块的最终独立范围审查

2026-09-08。PRIVATE_CORE。有限范围 PASS：同一固定 n1280 节点的 96 位中心张量 c̃¹*c̃²，主 Kronecker 算法与直接有序对算法已实际完整计算并逐输出一致，相关成本和当前证据连接成立。本次关闭这个固定块的终审，不增加残差、原解或奇性结论，也不再要求重复本块计算。

本人不是两份科学实现、比较程序或 COMPLETE_OUTCOME 的作者。此前已审核主算法、主记录和启动恢复；本轮全文读独立实现 565 行、独立合同/根代码审查、比较源码、两份独立 run/result、实际比较记录及 KRONECKER_COMPLETE_OUTCOME.md。以下区别源码推导、已有实际算术执行和本人的最后记录核对。

本轮没有执行或导入两份科学核及根比较程序，没有解码节点数组、重建中心、作卷积或打包，也没有再对全部中心/输出/舍入见证作逐模算术。实际执行的 check_kronecker_complete_records.py 仅核当前文件字节、规范解压内容、共享元数据、已存聚合有理量、进度计数及资源。

## 1. 独立输入入口与算术独立性成立

独立核的读取路径只包含原 manifest、modes、n1280 所在 block、自己的来源/审查和自己生成的产物。源码不导入主实现、不读主中心或主张量，也不读主结果来决定输入或输出。三个数据 pin 格式先核为 64 位十六进制，随后在运行前后认证实际文件。

load_original 核原配置、完整字典序 G、数组 dtype/shape/nbytes/数据 SHA 及节点/时间序列。数学只使用已验证第 0 行的 n1280 原值；斜率和其它行只作档案认证。两种实现的原输入 pin 相同，当前字节也相同；没有选择新节点、初值、ν、环面、截断或参数。

project_fraction 对原整数先提升，再分别以实部和/虚部差除 2·2^52，用逐分量 Fraction 算 z−k(k·z)/|k|²。它没有重用主共同分母表示，且完整核原投影的共轭与无散。

round_fraction 将 2^96c 约分为 N/D，D>0，用 Euclidean divmod 决定最近整数和平局偶性。负值与正值适用同一分支；保存所有 29472 份 N,D,q,r,C，核半径、严格中心大小和全部共轭。舍入中心不要求无散。源码中逐标量的二进制编码仅用于保存，不进入卷积运算。

独立 result 的原状态仍为 NOT_PERFORMED_BLIND_OUTPUT_FROZEN_FIRST，这准确记录它封存时没有查看主结果；不应在事后把该历史字段改成已比较。后续完成比较由单独的根记录表示。

## 2. 直接循环确实覆盖全部有序输入

left 从完整中心列表取第一分量实虚，right 从同一完整模式表取第二分量实虚，二者长度均为 4912。外层逐个 p、内层逐个 q，没有零值跳过、半谱、对称折半、非相邻删除或先验筛选。每对执行

Re T[e(p)+e(q)] += U_pX_q−V_pY_q，

Im T[e(p)+e(q)] += U_pY_q+V_pX_q。

符号和复相位正确，都是 Python 整数运算；内循环没有 Fraction、浮点、FFT/NTT 或整数打包。空间索引 e(p) 的三个移位坐标在 0..16，和坐标在 0..32，所以普通数组下标 e(p)+e(q) 恰对应物理频率 p+q，无坐标进位混叠。

因此完整执行需要 4912²=24127744 个有序对，源码每对恰写四个标量乘法，合计 96510976 次。完成行数/对数只在整个内层结束后更新。所有实虚输出最终逐项检查严格 2^235 界、共轭和零频虚部，并按全 35937 个输出的顺序保存、回读 71874 个标量。

中心严格 2^109 界与每输出最多 4912 个贡献，给任意部分累加也小于所用保守整数界。即便某一对中途被外部中断，源码没有把实虚可能不同步的 partial 张量当作已认证部分和或恢复起点。当前实际运行没有进入这个失败分支。

末端共轭和零频条件只是附加不变量；完整独立复算来自上述实际全部有序对遍历，不能颠倒这个证明关系。

## 3. 比较源码核的是全部整数及舍入见证

check_kronecker_agreement.py 先要求两个完成状态和独立封存状态，再绑定来源/数据/产物、核固定节点、分量、分母及完成计数。两份中心和两份张量都按已声明的固定 signed 小端标量宽度解码。

compare 随后逐项检查：

- 29472 个主/独立中心整数相等，并满足中心严格界；
- 71874 个主/独立输出整数相等，并满足输出严格界；
- 全 29472 个独立舍入见证的 D>0、0≤r<D、N=Dq+r、Fraction 约分、平局取偶结果与独立中心一致，以及半整数舍入半径；
- 从见证独立求 M=Σ|N/D|/2^96、δ=Σ|N/D−C|/2^96，与主记录逐有理数相等，再组成 E₀、E₂。

见证与原节点的关系来自独立源码实际 Fraction 重建和原输入绑定，不是仅凭形式上合法的商余记录。根程序没有第三次投影节点；它复核已封存见证与主误差全和的连接，范围准确。

当前实际比较记录报告上述全部等式，ties=0，张量分母为 2^192，完整输出数为 35937；E₀<10^-23、E₂<8·10^-21 与主结果一致。这里是在已完成的另一份原节点重建上获得误差全和的一致性，仍只属于输入扰动预算。

六个负对照在内存副本中分别改变一个中心、张量实部、张量虚部、对数、分母和舍入余数。源码有相应的明确拒绝路径，记录中的六个拒绝原因与它们匹配。原文件字节未改。本轮只核这些源码和实际记录，没有再运行负对照或逐标量比较。

比较记录 SHA 为 5510285fed346165e428bac4dfcb572548283322937a712be6465829481b5779。本轮重新核其中全部 32 个输入文件 SHA，均与当前字节一致；其中中心和张量二进制的同 SHA 是额外的字节一致证据，未被用来替代根已执行的逐整数比较。

## 4. 实际运行、档案与最终资源

独立 run 的最终状态为 COMPLETE_DIRECT_GAUSSIAN_INDEPENDENT，result 的数学状态为 ONE_FIXED_DIRECT_GAUSSIAN_CONVOLUTION_RECOMPUTED。run/result 的 source_sha256、input_sha256、config_sha256、checkout 四个共享字段相同；run 中 result 文件 SHA 和字节数指向实际结果。

| 实际执行 | 执行提交 | 最终墙钟（秒） | 峰 RSS（字节） | 实际目录（字节） | 含外日志（字节） |
| --- | --- | ---: | ---: | ---: | ---: |
| 主 Kronecker 核 | 7943df9127f28ceda67cffcc9b60311ec1f635c1 | 1.6278625840786844 | 87228416 | 5813537 | 5814242 |
| 独立直接核 | 49bf28aad70bdcb4adde2fd2cccc0e6b84544f1c | 2.783710124902427 | 86786048 | 2772758 | 2786482 |

上述用时/RSS 是已存实际运行观测，不是本人再测速。最终 stdout 分别绑定当前 run 字节，本轮核实际目录大小与之相同。独立外日志共 13724 字节，stderr 为零；run 内较早的 2772563 字节、2.7834273749031126 秒快照不作为最终值。

独立进度文件中 39 份 DIRECT_CONVOLUTION_ROWS 记录按 128 行间隔及最后 4912 行覆盖全部外层，所存对数均为 4912×已完成行数；最终为 24127744。独立卷积内循环记录为 2.4238574157934636 秒，其余时间包括输入认证、重建、舍入与档案操作。代码、完成元数据和进度相互支持；这里没有把进度日志独自当作算术正确性证明。

本轮实际核独立中心文件 412608 字节、见证 gzip 181630 字节、张量 2156220 字节及 result.json 3123 字节的哈希/描述连接。见证规范解压 JSON 为 1436523 字节，内容哈希匹配；只核其头部与形状，没有再次作见证逐项算术。主五份二进制和旧主审查证据的字节也保持。

两次各在 60 秒、256 MiB、8 MiB 内，计入外日志后仍有元数据预留。这里关闭的是这两个实际单块实现的成本问题，不外推到其它张量、完整节点、Hermite 段或全窗。

## 5. 科学结论及历史边界

KRONECKER_COMPLETE_OUTCOME.md 准确说明：同一个固定 96 位中心的一个完整复张量分量，已经通过主打包算法与直接有序对算法两条实际路径验证一致。原 trial-01 因错写 pin 的启动失败及其勘误仍独立保留，没有被 trial-02 或独立结果覆盖。

中心一般不再精确无散，后续必须使用保守算子 C 及输入扰动合同。此块未合并其余五个自张量、输出频率收缩、完整 Leray、原精确值/斜率和黏性线性项；因此 E_j 不等于残差，r₀/r₂、任何连续时间误差上界和原 NS 控制都仍未得到。

原初值、ν、环面和唯一精确参照未变。没有以另一个初值族替代同一原解，也没有把有限块、一个已知参照的单段界或末端小范数拼成全局/奇性结论。NO-CERTIFICATE-YET-FOR-FIXED-a、无统一迭代/单初值无限尺度声明与现有证据一致。

本次终审完成这个固定块，不要求为同一已经通过的算术结果继续增加审查轮次或重复科学核。未来残差工作须按其自己的合同推进；本 PASS 不预先覆盖它。

## 6. 最后记录核对及完整绑定

实际命令：

    /Users/kasifa/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 -B research/reverse/fixed-seed-global-screen/check_kronecker_complete_records.py

exit 0，状态 PASS_FINAL_KRONECKER_METADATA_AND_BYTE_AUDIT。共核当前 44 项输入；其中包含比较记录的全部 32 个绑定，并复验本块既有主审查使用的证据。新结果 JSON 和 stdout 自身再纳入下表，共 46 项。没有重复逐模式中心、输出或见证算术。

| 实际输入/证据路径 | SHA-256 |
| --- | --- |
| `research/reverse/fixed-seed-global-screen/C1_RESIDUAL_CONTRACT.md` | `a001077c4e1828827a3e7738e154bdd1b02541ff44d63032a475e2f0b5017251` |
| `research/reverse/fixed-seed-global-screen/CONTINUOUS_RESIDUAL_COST_PREFLIGHT.md` | `0c7ea4b3d33d152f298058a909e446505150d1004529f1a4518c2e1fedc7f796` |
| `research/reverse/fixed-seed-global-screen/CONTINUOUS_RESIDUAL_COST_ROOT_REVIEW.md` | `4865cf0639e20bc6d8d6c2546e8382c08b59366814168ff2f0b309bc8ef4e5da` |
| `research/reverse/fixed-seed-global-screen/KRONECKER_BLOCK_CONTRACT.md` | `d8077701b347d35045d7f59ab39669a9e6bf07f6753db386e3d052dc8ab5ada3` |
| `research/reverse/fixed-seed-global-screen/KRONECKER_BLOCK_ROOT_REVIEW.md` | `39e2fd54305c68f9383c72f4da79282f315928b4b5eea0c89f978486ba333a21` |
| `research/reverse/fixed-seed-global-screen/KRONECKER_COMPLETE_OUTCOME.md` | `3e4673385d1fc1d076d4a0a9926bc4c2ff943da9ea945b5bf07a12ea262a5704` |
| `research/reverse/fixed-seed-global-screen/KRONECKER_DECODING_INDEPENDENT_REVIEW.md` | `16d36272c65f4e42040fcc7e79f4661a2b047d50c86dcabcf4b083281c3d82b9` |
| `research/reverse/fixed-seed-global-screen/KRONECKER_DIRECT_CODE_REVIEW.md` | `cb14b77d627ea5bb4f2b100629e28dd78bd16d8e58119ee0e48efac872af781d` |
| `research/reverse/fixed-seed-global-screen/KRONECKER_DIRECT_INDEPENDENT_CONTRACT.md` | `4693c1aed265dcd77a5d20b1d08eb715156d451379936cf012fdfa0749b76c12` |
| `research/reverse/fixed-seed-global-screen/KRONECKER_PRIMARY_COST_OUTCOME.md` | `b990f32d3239e4274def7bc2c8722be6dbe55e1de59aa8a4025ad2ebcb0c4683` |
| `research/reverse/fixed-seed-global-screen/KRONECKER_PRIMARY_RESULT_REVIEW.md` | `3ac40135870e8d7c9c7581c4c9f2fa6b42094cf845fdbc620f855757f59a0829` |
| `research/reverse/fixed-seed-global-screen/KRONECKER_STARTUP_RECOVERY.md` | `77d26c82f4a7a571543628488457e26289d96d5c2b380000944eecf407ac17bb` |
| `research/reverse/fixed-seed-global-screen/KRONECKER_STARTUP_RECOVERY_REVIEW.md` | `38d95c2826c81995f21f1aee2b7468567c16e5b5b335b92813d59a989abb69ef` |
| `research/reverse/fixed-seed-global-screen/audit_kronecker_block.py` | `b4d65f5a02211ff52f1a202b4e9ba25e9cee47e5a9468bb3a670aa5c381a5c08` |
| `research/reverse/fixed-seed-global-screen/audit_kronecker_direct_independent.py` | `057951051c5aeaf6d70d2d232811fd84731a6d81f32782156fdae30b48f9a499` |
| `research/reverse/fixed-seed-global-screen/check_kronecker_agreement.py` | `0504b93b06a8ba2237a28adf613b5e1bd9622a93a88e9f25b9a68d3119862ec0` |
| `research/reverse/fixed-seed-global-screen/check_kronecker_complete_records.py` | `56c54ca33291e9b93eaca78b6c5d3e2f1fd00c4b870998b824768deee86a16c7` |
| `research/reverse/fixed-seed-global-screen/check_kronecker_primary_records.py` | `069cc1fd338ec12e43c77a94373009082d3d3ef19c59d07027373b42a20abc89` |
| `research/reverse/fixed-seed-global-screen/kronecker-block-root-recovery-run.log` | `2cd3068af56aef5f48500dcb6ad4acf4cd46c407e144411b39e5fd8dc6626236` |
| `research/reverse/fixed-seed-global-screen/kronecker-block-trial-01/run.json` | `44d05321296a6b25b3997495601cc9623a8fd6562b6dfd13f08dedcbbd99fcbc` |
| `research/reverse/fixed-seed-global-screen/kronecker-block-trial-02/RUN_CLAIM.json` | `d1e1065b0fb80acb305daa119f19239c9087e4335f7986d78ac771bef5dff5f8` |
| `research/reverse/fixed-seed-global-screen/kronecker-block-trial-02/c96-centers.i112le.bin` | `c16d26dcbea14b63614d192da27a8b268fa49e689a02fb15499601cc1b611c9e` |
| `research/reverse/fixed-seed-global-screen/kronecker-block-trial-02/product-0.signed-le.bin` | `c9fe217c68e9c90f1113ee014205490137bf30d20906f7f3832d5008c2f0bbff` |
| `research/reverse/fixed-seed-global-screen/kronecker-block-trial-02/product-1.signed-le.bin` | `5d088b3151dc55a8b0d875d1937af067181c2ff24c3cb981de3ca376aef29190` |
| `research/reverse/fixed-seed-global-screen/kronecker-block-trial-02/product-2.signed-le.bin` | `827ebd49131500fb8260dc06e921b72461de9a0a85eb7842ca8b68ca6337d3ce` |
| `research/reverse/fixed-seed-global-screen/kronecker-block-trial-02/run.json` | `375921aff0ceae1294b7d79947d9dfeaf817ad65ce9edc6c02b9b152ac922d70` |
| `research/reverse/fixed-seed-global-screen/kronecker-block-trial-02/tensor12-complex.i240le.bin` | `795ce995481d41b1fd4c6810101b62d37b187a268eaba992e97ef6f3f79ca0e6` |
| `research/reverse/fixed-seed-global-screen/kronecker-complete-final-record-check.json` | `29f74fe5c3d545481be5e2ebcc2f19fe2e3b91345d3fd8a7641b065d8dcbd75e` |
| `research/reverse/fixed-seed-global-screen/kronecker-complete-final-record-check.stdout.txt` | `abeeac9b8166dd5599d9a48b48d514f79b1adff6c5617aa6b7d71351eb90ca8f` |
| `research/reverse/fixed-seed-global-screen/kronecker-direct-independent-trial-01/centers-independent.i112le.bin` | `c16d26dcbea14b63614d192da27a8b268fa49e689a02fb15499601cc1b611c9e` |
| `research/reverse/fixed-seed-global-screen/kronecker-direct-independent-trial-01/claim.json` | `7e801f94b92adff803ba68e558338f87508233415ae14aa0c0041a5a80a718dd` |
| `research/reverse/fixed-seed-global-screen/kronecker-direct-independent-trial-01/progress.jsonl` | `a16f7a6b878242e1169896e40ce69d301aaddc3951e89ae33bb4ae46e83dfb4b` |
| `research/reverse/fixed-seed-global-screen/kronecker-direct-independent-trial-01/result.json` | `af998444847ef90696cc5e18fb716d60f2625748a98d2d11438e0f73b009853f` |
| `research/reverse/fixed-seed-global-screen/kronecker-direct-independent-trial-01/rounding-witnesses.json.gz` | `637e467edbb178fa25e8f05cb5dcf9bc48a299fce2350e930153b6367007333c` |
| `research/reverse/fixed-seed-global-screen/kronecker-direct-independent-trial-01/run.json` | `e4d54cf0690702f54029b4c36412d9d922e14a632090e5a4ac88f2e8b8e293e7` |
| `research/reverse/fixed-seed-global-screen/kronecker-direct-independent-trial-01/tensor12-direct.i240le.bin` | `795ce995481d41b1fd4c6810101b62d37b187a268eaba992e97ef6f3f79ca0e6` |
| `research/reverse/fixed-seed-global-screen/kronecker-direct-independent.stderr.log` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `research/reverse/fixed-seed-global-screen/kronecker-direct-independent.stdout.log` | `2322dc422a2a396807828f37fd5b9b408752be80f4e138ecc03eeba83200e43b` |
| `research/reverse/fixed-seed-global-screen/kronecker-independent-agreement.json` | `5510285fed346165e428bac4dfcb572548283322937a712be6465829481b5779` |
| `research/reverse/fixed-seed-global-screen/kronecker-primary-record-check.json` | `5930307fdab6b82eea1de319b65c0a42aee609be7568cf5905bf34ce79ca0632` |
| `research/reverse/fixed-seed-global-screen/kronecker-primary-record-check.stdout.txt` | `56f664d283b7869e701619f7812247c4379d2989ec1798bdd12ef8a2d043d7cc` |
| `research/reverse/fixed-seed-global-screen/kronecker-primary-root-readback.json` | `9f673dd679d89e3f41af89975628686ba0a0c4fcb748c916aae3b1a81c94d6e3` |
| `research/reverse/fixed-seed-global-screen/kronecker-startup-recovery-root-check.json` | `c2f7291f6bbb1654b8812d1ac0bb0787897d6bc09632fd4b873b752444abcce0` |
| `research/reverse/fixed-seed-global-screen/node-trial-01/block-01280-01343.npz` | `abf3b33282ff0b08e995c6aa1f80e7d79dbd64a55137574b77d51356b236297e` |
| `research/reverse/fixed-seed-global-screen/node-trial-01/manifest.json` | `5ac2abdfb7a14a38904f2ef1c58d81cf90bea776ce5426a56a75c6f81622c1cd` |
| `research/reverse/fixed-seed-global-screen/node-trial-01/modes.npy` | `f184c97c52e561ac53b8936ee51e68690517ad65c79e8050c93a891ac8856896` |

这份最终审查、已完成的两个科学核和实际完整比较各自承担不同证据职责；不得将任何一份单独冒称完整 NS 证明。
