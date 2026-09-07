# 固定 Kronecker 主块的实际结果审查

2026-09-08。PRIVATE_CORE。有限范围 PASS：恢复后 trial-02 的主算法、完成记录、五份二进制证据及 KRONECKER_PRIMARY_COST_OUTCOME.md 相符。主块已经实际完成，成本门通过；另一条完整算术路径的逐输出复算不在本次通过范围内。

本人不是主实现、KD 解码稿或结果正文的作者。已实读固定块合同及恢复勘误、主源码全部科学路径、KD 解码证明、CR 扰动接口和根解析审查，另全文读实际 run、最终 stdout、根回读及结果正文。先前启动恢复审查亦由本人完成，旧失败仍单独保留。

本轮实际执行的 check_kronecker_primary_records.py 只作标准库记录核对：文件哈希/长度、三个已存大整数的符号和位长、记录中的末进位连接、已存 M/δ/E 的有理后处理、配置/输入绑定及最终目录字节。没有加载原 NumPy 数组，没有重建节点或 96 位中心，没有打包、逐位平衡解码、科学乘法、零频直接和、完整卷积、FFT、PDE/ODE 或 git。它不是主核重跑，更不是 Pauli 的完整独立计算。

## 1. 原节点、中心及扰动接口

主科学路径先认证三份原档案文件和块内数组，核完整字典序 G、时间/量化单位，只取 n1280 的值行进入数学。原始 int64 实虚标量在加减前提升为 Python int；共同分母 D=2·2^52L 的投影分子与 C¹ 参照定义一致。完整 4912 模的原精确无散及共轭检查位于舍入和乘法之前。

96 位中心逐标量使用 Euclidean divmod。对负数，q 仍是向下整数商、余数非负，故 2r 与 D 比较以及平局时 q 的奇偶分支同样正确。这个舍入关于取负是奇函数，共轭保持；源码另逐模核对它。舍入后中心一般不再无散，源码、记录和正文均未假设它无散。

M 是原系数全部实虚绝对值之和，δ 是原系数与中心的全部实虚绝对误差之和。它们上界相应 Euclidean Wiener 范数。对保守双线性算子 C(f,g)，输出 |k|≤16√3<28，Leray 收缩与完整 ℓ¹ 卷积界给

||D^j[C(c,c)−C(c̃,c̃)]||₂

≤28^(j+1)(2Mδ+δ²)，j=0、2。

这里展开为 C(c,e)+C(e,c)−C(e,e)，e=c−c̃。需要保守算子，是因为只有原 c 精确无散；不能把非无散中心的输出导数形式直接冒称 B(c̃,c̃)。

本人本轮从已存 sum_abs_A/D 和 sum_abs_QpA_minus_DC/(D·2^96) 连接 M、δ，再独立组成 E₀、E₂，逐有理数等于记录，并核

M<2^28，δ≤14736·2^-96<2^-82，

E₀<2^-47，E₂<2^-37，

以及正文中更紧的 E₀<1/10^23、E₂<8/10^21。

完整有理分子分母保存在本次记录核对 JSON。这里没有重新从节点求 M、δ 的全和，不能将其后处理称为第二次原数据重建。E_j 也只包输入扰动：当前仅计算一个张量分量，完整 C(c̃,c̃)、原线性项及中心残差还未形成。

## 2. 打包、相位与空间支持

每个输入索引 e(p)=(p₁+8)+33(p₂+8)+1089(p₃+8)。各坐标位在 0..16，配对相加在 0..32，因此 e(p)+e(q) 就是物理输出 p+q 的唯一平移索引；空间基 33 无进位混叠。输入 17969 个位置、输出 35937 个位置包括嵌入零项，G 内每个实际有符号模式均被保留。

源码的 pack(0..3) 对应分量一实/虚和分量二实/虚。正、负数位分别写字节数组后以两个无符号整数相减，精确等于有符号系数多项式。不同模式的 e 注入，30-byte 单位没有重叠。

U·X、V·Y、(U+V)(X+Y) 三次一般实乘法后，逐系数组成

Re T=P₀−P₁，Im T=P₂−P₀−P₁。

第三项减去前两项恰留下 U*Y+V*X；符号、复相位和同输出相消正确。这个代数包括所有有序 p+q=k 的项，不因采用整数乘法而把反序额外乘 2 或删掉非相邻作用。零输入模原本排除，嵌入处置零不是输出截尾。

原输入界保证每个中心标量 |C|<2^109，实虚和小于 2^110，每个输出最多 4912 项，所以各原始实卷积系数小于 2^233，最终实虚组合小于 2^235。它们远小于 B/2=2^239。该先验来自输入及项数，不是从解包得到小数位再反推正确性。

## 3. KD 负数解码及源码匹配

对固定 J=35937，若真系数 |w_j|<B/2 且为整数，则

|Σw_jB^j|≤(B/2−1)(B^J−1)/(B−1)<B^J/2。

所以一次全宽 signed 小端导出合法。补码的无符号数位满足 z=Σr_jB^j−sB^J，s=1 当 z<0。源码逐位以 t=r_j+c_j 取平衡代表，并在 t≥B/2 时减 B、保留 carry=1。t=B 正确输出 0 并保留进位，未错误丢掉这一分支。

r_j=w_j+Bc_{j+1}−c_j 望远镜求和给

z=Σw_jB^j+(c_J−s)B^J。

严格半基界按模 B 归纳唯一恢复真实系数；末商应为 c_J−s，负乘积的最终 carry 应为 1。源码额外逐数位检查严格 2^233 界，终端检查 carry==int(z_negative)，与 KD 证明相符。先验界、末商检查和完整独立卷积是不同要求，不能互相替代。

主算法从实际回读的三份补码字节解包，再保存最终张量的逐标量 signed 编码，没有混用两种格式。输出 j 的负频索引为 J−1−j，物理零频索引为 17968。源码检查完整共轭，并以全部 4912 个正负输入项另算该零频，公式正确；这仅是附加的一个输出检查。

## 4. 本轮实际字节与记录核对

五份文件的实际 SHA、记录 SHA 和固定长度全相符：

| 文件 | 实际字节 | 格式范围 |
| --- | ---: | --- |
| c96-centers.i112le.bin | 412608 | 4912×6 个 signed 14-byte 中心整数 |
| product-0.signed-le.bin | 1078110 | 一个全宽 signed 乘积 |
| product-1.signed-le.bin | 1078110 | 一个全宽 signed 乘积 |
| product-2.signed-le.bin | 1078110 | 一个全宽 signed 乘积 |
| tensor12-complex.i240le.bin | 2156220 | 35937×2 个 signed 30-byte 输出整数 |

合计 5803158 字节。中心分母为 2^96，最终张量分母为 2^192；记录和源码一致。尺寸与哈希通过只说明这些已存字节符合记录，不单独证明卷积值。

本人将三份原始乘积字节各作为一个有符号整数读取，独立核得它们都为负，绝对值位长分别为 8624252、8623777、8624252，与记录相符。各记录的 carry=1、末商=0 与实际符号及 KD 终端关系一致。没有在本轮重新扫描平衡数位；记录中的逐数位界和 carry 执行结果仍来自已审主算法的实际运行。

输入乘数的符号乘积、固定输入宽度、三次公式/索引、输出 SHA 和三条进度记录也连接一致。本人未重建乘数或重算它们的哈希，未把乘数元数据连接说成新的完整乘法验证。

全部源码、正确原档案 pin、配置 SHA 和当前文件字节匹配。原合同错误 pin 及 trial-01 目录以绑定的恢复勘误为准；旧失败 run 的 SHA 仍是 44d05321…，没有被新结果覆盖。

## 5. 完成状态与实际资源

trial-02 的最终状态为 COMPLETE / ONE_FIXED_COMPLEX_TENSOR_BLOCK_VERIFIED，run SHA 为 375921aff0ceae1294b7d79947d9dfeaf817ad65ce9edc6c02b9b152ac922d70。记录的执行 HEAD 是 7943df9127f28ceda67cffcc9b60311ec1f635c1，实际实现字节 SHA 是 b4d65f5a…；两者用途已区分。

最终 stdout 在完整写入后绑定该 run SHA，并给

- 墙钟 1.6278625840786844 秒；
- 峰 RSS 87228416 字节；
- 输出目录 5813537 字节。

本轮核实际目录大小亦为 5813537；外部完整日志 705 字节，合计 5814242。均在 60 秒、256 MiB、8 MiB 以及输出预留范围内。run 内较早快照 5813503 字节、RSS 87212032、1.627563667 秒没有被误用成最终观察。

三个一般乘法分别记录 0.4850544591899961、0.4664011658169329、0.46669308305718005 秒。它们是主运行测量，整体还含认证、重建、舍入、打包、解包和读写；本人没有再测速。不能据此预填 18 个乘法、全部张量或全窗成本。

NumPy/Python/CPU 环境记录及单进程使用方式与实现一致。inputs 中 scientific_execution=false 是启动预检快照；最终完成状态、产品和档案给实际执行结果，不能混读。

## 6. 正文与独立复算边界

KRONECKER_PRIMARY_COST_OUTCOME.md 准确保留 trial-01 的启动失败与 trial-02 的成功，使用最终资源，明确 E_j 只属于输入扰动。它没有把一个张量分量或零频检查当成完整非线性、残差或原解证书。

本轮可报告“已审主算法在固定输入上完成一个完整复张量分量，并有实际成本与完整输出档案”。要报告“另一算法完整复算一致”，还须由另一核从原档案独立重建全部 29472 个中心标量，直接累加完整 24127744 个有序对，冻结输出后比较全部 71874 个输出标量。此项不由本文的字节/标量预算审查完成。

独立复算即使随后成功，仍仅涉及这一 96 位中心张量分量；其余张量、物理频率收缩、完整 Leray、原线性项、连续 r₀/r₂、真实误差和终点门仍需另证。本文没有替后继独立实现、运行或最终比较预填 PASS。

## 7. 自有记录及绑定

实际命令为：

    /Users/kasifa/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 -B research/reverse/fixed-seed-global-screen/check_kronecker_primary_records.py

exit 0；输出 PASS_PRIMARY_SAVED_RECORDS_AND_BINARY_IDENTITIES。该程序的科学不执行范围在源码和 JSON 中明确；其 25 项实际输入绑定，加自身结果 JSON 与 stdout，形成下表 27 项证据。

| 实际输入/证据路径 | SHA-256 |
| --- | --- |
| `research/reverse/fixed-seed-global-screen/C1_RESIDUAL_CONTRACT.md` | `a001077c4e1828827a3e7738e154bdd1b02541ff44d63032a475e2f0b5017251` |
| `research/reverse/fixed-seed-global-screen/CONTINUOUS_RESIDUAL_COST_PREFLIGHT.md` | `0c7ea4b3d33d152f298058a909e446505150d1004529f1a4518c2e1fedc7f796` |
| `research/reverse/fixed-seed-global-screen/CONTINUOUS_RESIDUAL_COST_ROOT_REVIEW.md` | `4865cf0639e20bc6d8d6c2546e8382c08b59366814168ff2f0b309bc8ef4e5da` |
| `research/reverse/fixed-seed-global-screen/KRONECKER_BLOCK_CONTRACT.md` | `d8077701b347d35045d7f59ab39669a9e6bf07f6753db386e3d052dc8ab5ada3` |
| `research/reverse/fixed-seed-global-screen/KRONECKER_BLOCK_ROOT_REVIEW.md` | `39e2fd54305c68f9383c72f4da79282f315928b4b5eea0c89f978486ba333a21` |
| `research/reverse/fixed-seed-global-screen/KRONECKER_DECODING_INDEPENDENT_REVIEW.md` | `16d36272c65f4e42040fcc7e79f4661a2b047d50c86dcabcf4b083281c3d82b9` |
| `research/reverse/fixed-seed-global-screen/KRONECKER_PRIMARY_COST_OUTCOME.md` | `b990f32d3239e4274def7bc2c8722be6dbe55e1de59aa8a4025ad2ebcb0c4683` |
| `research/reverse/fixed-seed-global-screen/KRONECKER_STARTUP_RECOVERY.md` | `77d26c82f4a7a571543628488457e26289d96d5c2b380000944eecf407ac17bb` |
| `research/reverse/fixed-seed-global-screen/KRONECKER_STARTUP_RECOVERY_REVIEW.md` | `38d95c2826c81995f21f1aee2b7468567c16e5b5b335b92813d59a989abb69ef` |
| `research/reverse/fixed-seed-global-screen/audit_kronecker_block.py` | `b4d65f5a02211ff52f1a202b4e9ba25e9cee47e5a9468bb3a670aa5c381a5c08` |
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
| `research/reverse/fixed-seed-global-screen/kronecker-primary-record-check.json` | `5930307fdab6b82eea1de319b65c0a42aee609be7568cf5905bf34ce79ca0632` |
| `research/reverse/fixed-seed-global-screen/kronecker-primary-record-check.stdout.txt` | `56f664d283b7869e701619f7812247c4379d2989ec1798bdd12ef8a2d043d7cc` |
| `research/reverse/fixed-seed-global-screen/kronecker-primary-root-readback.json` | `9f673dd679d89e3f41af89975628686ba0a0c4fcb748c916aae3b1a81c94d6e3` |
| `research/reverse/fixed-seed-global-screen/kronecker-startup-recovery-root-check.json` | `c2f7291f6bbb1654b8812d1ac0bb0787897d6bc09632fd4b873b752444abcce0` |
| `research/reverse/fixed-seed-global-screen/node-trial-01/block-01280-01343.npz` | `abf3b33282ff0b08e995c6aa1f80e7d79dbd64a55137574b77d51356b236297e` |
| `research/reverse/fixed-seed-global-screen/node-trial-01/manifest.json` | `5ac2abdfb7a14a38904f2ef1c58d81cf90bea776ce5426a56a75c6f81622c1cd` |
| `research/reverse/fixed-seed-global-screen/node-trial-01/modes.npy` | `f184c97c52e561ac53b8936ee51e68690517ad65c79e8050c93a891ac8856896` |

本次 PASS 只完成主执行的算法、记录与范围审查，不替代尚待完成的独立全卷积证书。
