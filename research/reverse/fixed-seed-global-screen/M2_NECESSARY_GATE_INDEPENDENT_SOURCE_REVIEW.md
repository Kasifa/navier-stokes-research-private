# M₂必要门执行合同与源码的非作者审查

2026-09-08。PRIVATE_CORE。**PASS_BOUNDED_STATIC_SOURCE_REVIEW_NOT_RUN**。已全文读取根执行合同及 Pascal 的最终425行源码，未发现需修订的阻断项。本稿接受一次被审范围内的执行准备，不证明必要门已触发或运行成本已经支付。

锁定源码 audit_m2_necessary_gate.py，23144 B，SHA256：

`a3a7cd37cf21a4322ed710bb1281908bd3332589a83d4acd7205e3f425f920cd`。

本人是 NI 范围审计的作者，故此处不把 NI.1–4 重读称为它的另一份独立证明。根是执行合同作者，Pascal是代码作者；本次非作者审查针对合同如何使用 NI，以及完整源码、停止/收据路径和实际来源连接。

## 1. 固定算术路径

- 唯一科学数组输入是硬绑定的原 hermite-b.i96le.bin；先认证完整1414656字节，只解码首353664字节。29472次 signed little-endian、12字节读取恰覆盖 b₀ 的全部 G、三分量和实虚两项，未解码后三层或第二种表示。
- 每项检查被2048整除；这只是附加一致性检查，来源还连接到已经完成的117888个原幂系数标量比较。代码不以整除或总和代替原系数来源。没有额外2⁸⁸筛选门。
- component=(i//2)%3 正确，各分量9824项；每个值只平方一次，包括零。B₀由三个小计相加，没有第二次完整求和。完整正负谱已计入，不再乘2。
- Q₂的固定未约分分母为2¹²⁸；gcd仅供额外约分显示，不改变门。P₃₂从已硬绑定的旧独立结果取出，核 x=[5,4]、32阶、正分子分母，不调用 exp 或新增指数精度。
- 唯一差值 D=25B₀pₙ−361·2¹²⁸p_d；D>0 才返回 FIXED_REFERENCE_M2_ENVELOPE_REFUTED，D≤0均为 UNDECIDED_FOR_LINF。正、负边界通过同一 validator；零边界的错误“拒绝包络”声明须被同一 validator 拒绝。另一个负对照仅变异实际来源 SHA 的一个字符。审查中没有执行这些测试。

拒绝范围仅为同一参照的固定 M₂指数包络，亦适用于 S.2 保留的同一 M₂要求；不把 σ 当成完整 M₁，不对真实 NS 作结论。未触发不是空间上界。两种结果均保留四个 false 标志。

## 2. 来源、入口与资源边界

默认/--check-only 只读字节、SHA、ASCII/AST及配置，不调用 evaluate；源码中只有一个实际 evaluate 调用。--run 要求精确四个 FINAL_PINS 名称、被审合同、最终源码的动态根审查 SHA及其中的源码/合同绑定，并锁 Python3.12.14、反向工作树、空且对应真实文件描述符的外置日志。排他目录防止重跑；根另负责 noclobber 排他创建日志。

本轮另读取旧 comparison/run/receipt/根实际退出验收的小字段，确认源码所用字段实际存在并相互对应：固定比较提交、comparison/run/receipt SHA、工具exit0、117888计数及 b 文件绑定正确。它们的状态均为 ARITHMETIC_AGREEMENT_WITH_PRODUCER_RESOURCE_EVIDENCE_GAP，四项标志均为false。此读取不是重跑比较或重新验算原系数。

源码全程无 NumPy、platform、subprocess、fork、线程创建、FFT、卷积、根号或PDE入口；元数据使用 sys、os.uname 五个命名字段、os.cpu_count 及直接读取工作树 HEAD/ref。没有隐式 uname/file 命令的已知调用路径。旧生产核资源缺口的审计/补充/独审均硬绑定，本小核的单进程成本检查不能修复旧成本；producer_resource_complete、resource_complete、certificate_ready、release_ready在成功、失败、运行记录、结果和收据路径均保持false。

计时从模块入口开始。科学循环逐512项观察60秒、256 MiB SELF峰值、16 MiB全部新输出门，并有计算阶段计时信号。最终字节重验不重做科学求和；源、全部固定输入、动态根审查与提交位置均再核。异常或资源失败不重试，已有失败/部分结果保留。

收据在stdout完整冲刷后绑定日志和既有输出，固定点迭代只解决收据自身字节计数，不构造自身SHA。其实际写入后再次回读全部输出/日志SHA及字节；末端总字节、预算或峰值记录不一致会使旧收据失效并返回非零。最终接纳必须同时有实际exit0与一致收据，不能只读较早的 COMPLETED 字样。所存各 elapsed 字段仅代表其注明的观测时点；最后 after 观测用于退出预算门，不能将较早字段冒称函数返回时刻的精确总墙钟。根仍需保留实际调用退出/耗时证据。

## 3. 实际静态操作及绑定

审查者实际只用标准库读取源码为ASCII、AST解析并 compile-only，未导入目标模块或执行其任何入口；从AST提取28个固定PINS/FINAL_PINS并逐文件核真实字节，全部匹配。科学输出目录当时不存在，B₀未求。作者另执行的 --check-only 记录只作为来源证据，未冒称本人运行。

下表中执行合同、NI根审查和最终源码已全文读；既有算术记录仅按上述字段读取，其余运行依赖仅进行字节绑定，不能从此表推称重新全文审查所有旧代码或科学二进制。没有新增科学测试、数值结果或完整研究证书。

| 实际输入路径（相对反向树） | SHA-256 |
| --- | --- |
| `research/reverse/fixed-seed-global-screen/audit_m2_necessary_gate.py` | `a3a7cd37cf21a4322ed710bb1281908bd3332589a83d4acd7205e3f425f920cd` |
| `research/reverse/fixed-seed-global-screen/ONE_SEGMENT_NEXT_INPUT_SCOPE_AUDIT.md` | `cecb56ff8cabe10bbce3d77fb1cef18458e4c32830f16220c1da69566937d490` |
| `research/reverse/fixed-seed-global-screen/NODE_GATE_LEMMA.md` | `177fe82983bb8d6d3e172615c716176338bdc7e31cd546e0416b502b80dd76fb` |
| `research/reverse/fixed-seed-global-screen/FULL_NODAL_RESIDUAL_OUTCOME.md` | `223c963e10ae14c93a231901dfe1554b8c61b63324537ebc250ddb7ae15d32ee` |
| `research/reverse/fixed-seed-global-screen/FULL_NODAL_RESIDUAL_FINAL_REVIEW.md` | `6d191cdb7be53601617754769b55b50be6346e5abfc2ca93083bf0518be7bc69` |
| `research/reverse/fixed-seed-global-screen/full-nodal-agreement.json` | `f2ccad0d3a963e1a0bdbf0e9695e2979271807201ef3427964b2a11052511ed8` |
| `research/reverse/fixed-seed-global-screen/full-nodal-independent-trial-01/result.json` | `e637e7fcde5f2fa8ac7cf55d635ada579f6fae189ebf903b6a7a018c351e393b` |
| `research/reverse/fixed-seed-global-screen/one-segment-residual-trial-01/hermite-b.i96le.bin` | `ba831967f4eeaa69bd7d16674c1f3a0cda913c14ac864d1dcfc6518e3ed1067c` |
| `research/reverse/fixed-seed-global-screen/node-trial-01/manifest.json` | `5ac2abdfb7a14a38904f2ef1c58d81cf90bea776ce5426a56a75c6f81622c1cd` |
| `research/reverse/fixed-seed-global-screen/node-trial-01/modes.npy` | `f184c97c52e561ac53b8936ee51e68690517ad65c79e8050c93a891ac8856896` |
| `research/reverse/fixed-seed-global-screen/node-trial-01/block-01280-01343.npz` | `abf3b33282ff0b08e995c6aa1f80e7d79dbd64a55137574b77d51356b236297e` |
| `research/reverse/fixed-seed-global-screen/ONE_SEGMENT_HIDDEN_HELPER_RESOURCE_AUDIT.md` | `c971a90e0c7d230bd25df1dd80b2e27c74b9af089ad6194099e217e981a77c87` |
| `research/reverse/fixed-seed-global-screen/ONE_SEGMENT_COMPARISON_RESOURCE_GAP_ADDENDUM.md` | `212df48b07648511024524ab746d41ec3e419914cb111862ae3569663ccf9355` |
| `research/reverse/fixed-seed-global-screen/ONE_SEGMENT_COMPARISON_RESOURCE_GAP_INDEPENDENT_REVIEW.md` | `36141219e713ed8a72cb1c6cef9609d00e86aed36f7fd7d80e242d0331562e06` |
| `research/reverse/fixed-seed-global-screen/one-segment-residual-comparison-trial-01/comparison.json` | `c0e454ac4fd980344c29704bdabb3e7dd8c00e00daac8942f3621d2c2428eba8` |
| `research/reverse/fixed-seed-global-screen/one-segment-residual-comparison-trial-01/run.json` | `1130f56738d77a57f0227a2289b7a56fe543c49c5f86b2ba0a3dbc839247557a` |
| `research/reverse/fixed-seed-global-screen/one-segment-residual-comparison-trial-01/final-receipt.json` | `2943f90b98b34513d225e4cfe7447444d13287c369e16677f6e84dd84d8f389a` |
| `research/reverse/fixed-seed-global-screen/compare_one_segment_residual.py` | `7e09b766feb86ac70bb1b05957903320d41069637d4c2ee23e8ebed88c6bd294` |
| `research/reverse/fixed-seed-global-screen/ONE_SEGMENT_RESIDUAL_COMPARATOR_INDEPENDENT_REVIEW.md` | `14bc674a61adca842a0cf09005451b1988800ef51bf5781abc3d290909421771` |
| `research/reverse/fixed-seed-global-screen/ONE_SEGMENT_RESIDUAL_DENOMINATOR_LEMMA.md` | `de6b150813559e6d0856b3df8db77491c9a3da4cad1f07a3d94282cd29642104` |
| `research/reverse/fixed-seed-global-screen/ONE_SEGMENT_RESIDUAL_DENOMINATOR_INDEPENDENT_DERIVATION.md` | `a9d6b288917eb98123afce1bd0f07bf879e530b53701ad9eb9e00f4c5a099171` |
| `research/reverse/fixed-seed-global-screen/audit_one_segment_residual.py` | `f8f871684d68303de24a8901abb35266969d2f978d218ca9d14cd16ce45fac63` |
| `research/reverse/fixed-seed-global-screen/audit_one_segment_residual_independent.py` | `1e9c9ee576049bd444ed07e858175b113bdb09d3719f1ab69820a3536564ca79` |
| `research/reverse/fixed-seed-global-screen/one-segment-primary-root-execution-acceptance.json` | `c4c8ea70c33918ddea1d7cce74b89e7e97e99ff9be7aa3f74e73e3633562770b` |
| `research/reverse/fixed-seed-global-screen/one-segment-independent-root-execution-acceptance.json` | `5265d2ebe8a3af7bd822ecdcef2f68a6e20a567f4d84135af2ccabd10f154c49` |
| `research/reverse/fixed-seed-global-screen/M2_NECESSARY_GATE_EXECUTION_CONTRACT.md` | `7ee3b897fd2c7cabd7fbeedb8c0c053130bcdd7e46fbc1dd1c602fa3a454e9cd` |
| `research/reverse/fixed-seed-global-screen/ONE_SEGMENT_NEXT_INPUT_ROOT_REVIEW.md` | `ad5c06c2e1da43f46ab6d74abc73db3987af9e9090b6911e46a6985ed13a0049` |
| `research/reverse/fixed-seed-global-screen/one-segment-comparison-root-execution-acceptance.json` | `35da6abd32a7b3cec346c11ca43661f5cadb7896dc37a24de6f19f76fed594ee` |
| `research/reverse/fixed-seed-global-screen/ONE_SEGMENT_COMPARISON_EXECUTION_INDEPENDENT_REVIEW.md` | `fe1986c2fc9fe78cc47663278296e10f76429bc399b1f784db3f361c4f9a0afd` |
| `research/reverse/fixed-seed-global-screen/m2-necessary-gate-static-check.json` | `338640f282011c4905bfe1118dce789a390667d2fd7b6a59dba97d24e50d3a09` |
| `research/reverse/fixed-seed-global-screen/m2-necessary-gate-static.stdout.log` | `6f8196a0ca457fd67b7a3af1e1dd954b0889d17807719269a0d488f5132fe9ca` |
| `research/reverse/fixed-seed-global-screen/m2-necessary-gate-static.stderr.log` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
