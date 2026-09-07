# 固定一段导数上界的最终范围审查

2026-09-08。PRIVATE_CORE。有限范围 PASS：两份已完成的算术记录、完整比较逻辑、当前输入字节和 OUTCOME 的三个整段上界相符。未发现需要阻断这些有限结论的问题。

本审查者不是主核、独立核、比较程序或 OUTCOME 的作者，曾独立审核本项数学合同及一侧应变公式。本轮全文读比较源码、独立 Fraction 实现、两份完成运行记录、独立结果、根复核记录及 OUTCOME，并解析全部 12 组已存有理区间。主核实现沿用根代理的源码审查与已有独立数学审查；本人本轮没有把主实现重审或重跑一遍。

本轮实际执行的只是 check_one_segment_final_records.py：已存区间及有理表达式的后处理、文件/解压字节哈希、元数据连接和目录字节核对。没有导入或执行两份科学核、根比较程序，没有重新解码节点、投影、计算任何平方根、比较全部逐模平方值、FFT 或 PDE/ODE 积分。原始结果未改。它不是第三次独立科学重建。

## 1. 最终数学结论只覆盖同一固定段

在 I=[1280/2048,1281/2048] 的每个时刻，同一固定 Q52 档案定义的 Hermite 参照满足

σ_v(t)≤343/100，

||D²v(t)||∞,F≤3833/500，

||D³v(t)||∞,F≤6507/500。

本轮用 Fraction 从主记录的 Cχ、四组范数上端及 √2、√3 的有理上端重新组成三个包络表达式，确认与主结果逐有理数相等，并严格低于以上便于阅读的有理数。完整分子、分母及取整余量保存在本次记录核对 JSON；小数显示不参与判定。

这里 σ_v=sup_x[−λ_min(sym Dv)]，不是某个复 Fourier 矩阵的特征值。模板分解 v=χa+b、复横向对称梯度的 1/√2、模板二三阶 Frobenius 界 2√3，以及三次 Bernstein 凸包，已经在绑定的数学审查中逐式核验。因此这些数覆盖完整空间和闭时间段，包括端点；不是两个节点或空间采样的最大值。

固定 a、ν=1、无外力、固定环面、全 4912 个正负模式、原节点和共享物理斜率均保持。b 仍是完整模板差，不能被命名为纯第一代供给或真实新生频谱。有限 Fourier 参照也不是原 NS 解。

## 2. 实际独立性与根号路径

主记录绑定共同分母源码 5fcf49eb…，使用 D=2·2^52L、E=6144D 及整数 Bernstein 分子。独立记录绑定源码 6d599db9…，从原三个档案文件逐分量构造 Fraction 共轭平均及 P_k，不构造 L/D/E，不读取主源码或主运行/范数输出。实际读到的导入、文件读取和 compute 路径支持这种独立性说明。

独立四份场使用 c₀、c₀+d₀/6144、c₁−d₁/6144、c₁，χ 取规定的 +e₁ 第二分量实部；它重新核实值、无散和模板差约束。其被开方数直接为 s^j|b_{k,m}|² 的约分有理数，采用位长定位、精确比较和逐项归一化的 isqrt 区间。源码正确处理负指数、零值、二次幂边界和向上端；没有用浮点 log/sqrt 替代严格夹界。

两个核的“128 位”网格不同：主核对清分母整数缩放，再除 E；独立核对每项归一化后的有理数缩放。故上下端和 nonsquare_count 不必一致。特别是这个计数表示相应网格上根号是否精确命中，不是数学上“无理平方根的个数”。根比较没有错误地要求两个计数相等。

两次实际 HEAD 不同：主运行记录 ed412495…，独立记录 ecb67607…。这本身不表示参照变动；各自源码及共同原节点由逐文件 SHA 独立绑定，当前核对均相符。HEAD 只按运行记录作为执行位置说明，本终审没有另行运行 git。

## 3. 完整比较源码的范围与逻辑

全文读 check_one_segment_agreement.py 后确认，它按以下顺序连接证据：

- 检查两个完成状态、固定段、L/D/E 关系及四组/4912 模计数。
- 将主 B/E² 与独立约分模长平方逐项比较，共 19648 个精确等式，并逐项连接四个 χ。
- 从主保存的平方输入及固定字典序全 G，重算 58944 个移位整数根号输入、12 个完整和及主区间归一化。
- 核查每组主/独立区间交叠并计数包含关系；当前记录为全部 12 组主区间包含于独立区间。
- 核 √2、√3 的上下端平方、各组最大值、Cχ、应变乘子和三个包络表达式，最后用精确有理数检查可读上界。

固定模式顺序的适用前提来自两个已认证的原档案重建和共同文件绑定。原程序虽在根号后处理处使用固定 s 列表，后续仍检查每行完整计数；没有用半谱权重替换全正负谱。

该程序确实重算的是保存平方值的根号后处理，未再次从节点投影。它也没有只比对近似小数。主上端落在独立“包络表达式区间”内是正确的比较对象；独立表达式下端没有被用作真实 σ_v 或 M_j 的下界。

实际记录中的六个内存负对照分别改范数平方、χ、模式计数、根号和、应变乘子和 M₃ 上端。源码在独立深拷贝中改变它们，记录了各自被拒的具体检查，不会改原始文件。本轮仅核源码与六条已存记录的匹配，没有再执行这些变异。

本次另作的 12 组区间包含、主保存整数和的分母/宽度、三个表达式及有理取整复核均通过。它复核后处理连接，不替代前述 19648 项原始独立重建比较。

## 4. 完成状态、实际资源与回读

主 run.json 的最终 execution_status 是 COMPLETE；inputs 内的 scientific_execution=false 和 READY_FOR_ROOT_SOURCE_REVIEW 是启动预检快照，不能把它们误读成最终未执行状态。独立 run.json 的最终状态为 COMPLETE_FIXED_SEGMENT_INDEPENDENT_UPPER，四组均已完成。

独立 run 的 result 文件 SHA/字节数与实际 result.json 一致；run/result 的 source_sha256、input_file_sha256、checkout、config_sha256 四个共享字段相同。两份最终 stdout 都绑定当前 run 字节。以下采用最终写入后的观测，并已核对实际目录总字节：

| 运行 | 最终墙钟（秒） | 峰 RSS（字节） | 实际输出目录（字节） | 加外部 stdout 后（字节） |
| --- | ---: | ---: | ---: | ---: |
| 主共同分母核 | 0.3750704589765519 | 81117184 | 319289 | 320164 |
| 独立 Fraction 核 | 1.578954041004181 | 77332480 | 146820 | 181213 |

独立 stderr 是零字节。主 run 内的 319253 字节和独立 run 内的 140251 字节属于更早快照；OUTCOME 正确使用最终 stdout 的 319289 与 146820，未混淆两层观测。墙钟与 RSS 是所存实际运行记录，不是本人重新测量的结果。

两次均低于各自 60 秒、256 MiB、16 MiB 上限；即使计入已存外部 stdout，也低于扣除 256 KiB 预留后的输出限额。不能由此推算所有 5120 段或完整残差的成本已经可接受。

主一份 gzip 和独立四份 gzip 的文件哈希、规范解压 JSON 哈希及完整形状，本轮均实际复核。它们保存模长平方而非相位档案；原节点绑定、重建代码及约束核对仍是证明链中必要的部分。

## 5. OUTCOME 的结论边界

OUTCOME 正确把所得结果定位为已知固定参照的一段 σ、M₂、M₃ 输入。它没有由这个粗上界超过旧靶标推出实际导数超过靶标；也没有把初时刻 σ_a=2 推广成全程指数应变界。

尚未支付本段及全窗的完整 r₀/r₂、其他段输入、正控制函数及完整终点接口。旧参照末端 A_-1<1/2 不能与本单段界拼成原解全局证书。NO-CERTIFICATE-YET-FOR-FIXED-a 的状态与实际证据相符；没有统一迭代、单一初值无限尺度、有限总时间或奇性结论。

OUTCOME 末尾涉及后继连续残差成本稿的段落只说明下一任务及当前未执行状态。本终审不核验那份 96 位输入/卷积路径的数学内容，不把本 PASS 扩大到后继合同、实现或预算。当前包也没有被冒称新颖理论或一般奇性排除。

## 6. 实际记录与字节绑定

本次后处理命令为：

    /Users/kasifa/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 -B research/reverse/fixed-seed-global-screen/check_one_segment_final_records.py

实际 exit 0。确定性核对输出为 PASS_SAVED_ENDPOINT_ARITHMETIC_AND_BYTE_AUDIT，核了根比较记录的全部 27 个输入绑定；加本终审使用的文本、日志、根回读记录和核对源码，共 37 个输入。JSON 和 stdout 自身再纳入下表，形成 39 项当前绑定。

对节点二进制文件仅流式计算文件 SHA，没有解码或对节点值计算。对平方范数档案仅验证内容字节、JSON 和形状，没有重复逐模算术。对未在本轮重新推导的旧 C¹ 接口和主实现，依赖范围已在第 1、2 节及既有审查中明确。

| 实际输入/证据路径 | SHA-256 |
| --- | --- |
| `research/reverse/fixed-seed-global-screen/C1_RESIDUAL_CONTRACT.md` | `a001077c4e1828827a3e7738e154bdd1b02541ff44d63032a475e2f0b5017251` |
| `research/reverse/fixed-seed-global-screen/ONE_SEGMENT_DERIVATIVE_CONTRACT.md` | `a53006b424c2166ad943166abca8e284138e64d31a6d07131041f9da9afa229a` |
| `research/reverse/fixed-seed-global-screen/ONE_SEGMENT_DERIVATIVE_INDEPENDENT_CONTRACT.md` | `f3a382ffc6ba5770cb552b3c8192345d2e6ae1eb871c6ca68f39a0b926855689` |
| `research/reverse/fixed-seed-global-screen/ONE_SEGMENT_DERIVATIVE_OUTCOME.md` | `ac2e7737600b1584da1ed47197335e84dedae4dc61659eae667847391acaa81f` |
| `research/reverse/fixed-seed-global-screen/ONE_SEGMENT_DERIVATIVE_REVIEW.md` | `a4e5e12cd3d16ead0bf9081ab516c6f2afbc38cd1b76ae4199b5c550ef294b55` |
| `research/reverse/fixed-seed-global-screen/ONE_SEGMENT_DERIVATIVE_ROOT_REVIEW.md` | `cf108858f95dfdb193ab169fccbb4a8a45089660b6ea9f7244e80c410fc54691` |
| `research/reverse/fixed-seed-global-screen/ONE_SEGMENT_INDEPENDENT_CODE_REVIEW.md` | `086d6dbb7d7df220b999cc63f05582134935330956f2c3488b7249adbe46a704` |
| `research/reverse/fixed-seed-global-screen/STRAIN_CONTROL_INDEPENDENT_REVIEW.md` | `628ced02a9107039119dcb1744a718db7e2a4b692444c9867b3c62886e39c42e` |
| `research/reverse/fixed-seed-global-screen/STRAIN_CONTROL_REFINEMENT.md` | `d6ab251e47d5818078f045d3f0ab7aae778e8e624c468633c360a9ed08930e01` |
| `research/reverse/fixed-seed-global-screen/audit_one_segment_derivative.py` | `5fcf49eb5c2b8faad3ca40e632de9941d819530d9fd033f04d56866b539e36cc` |
| `research/reverse/fixed-seed-global-screen/audit_one_segment_derivative_independent.py` | `6d599db92eab6b9f1170b341ee8ba01108165eb50f68be0726e58965364015b8` |
| `research/reverse/fixed-seed-global-screen/check_one_segment_agreement.py` | `bcea7463660ea7f67a06bf2779603be88001afe1287a0a75bddcae08e3650039` |
| `research/reverse/fixed-seed-global-screen/check_one_segment_final_records.py` | `817a695738c0034023e0a1b5d4097ed30ed10a8782423e239281579ed6675e36` |
| `research/reverse/fixed-seed-global-screen/node-trial-01/block-01280-01343.npz` | `abf3b33282ff0b08e995c6aa1f80e7d79dbd64a55137574b77d51356b236297e` |
| `research/reverse/fixed-seed-global-screen/node-trial-01/manifest.json` | `5ac2abdfb7a14a38904f2ef1c58d81cf90bea776ce5426a56a75c6f81622c1cd` |
| `research/reverse/fixed-seed-global-screen/node-trial-01/modes.npy` | `f184c97c52e561ac53b8936ee51e68690517ad65c79e8050c93a891ac8856896` |
| `research/reverse/fixed-seed-global-screen/one-segment-derivative-independent-trial-01/claim.json` | `c8585a0097e3d771aff6d2e97687e4a9fe9978a8accddc7c9de764c968f26e4e` |
| `research/reverse/fixed-seed-global-screen/one-segment-derivative-independent-trial-01/norm-squares-m0.json.gz` | `efedc8b18d7d0b7700fe3d47cbc68fb757d78018a1c0a47e2751d6ddeef64181` |
| `research/reverse/fixed-seed-global-screen/one-segment-derivative-independent-trial-01/norm-squares-m1.json.gz` | `1f4fb5e1bb559e28ce230937bd3d20013fda47cb154c849a67079ff583817b9a` |
| `research/reverse/fixed-seed-global-screen/one-segment-derivative-independent-trial-01/norm-squares-m2.json.gz` | `dc974108a2d4fd162023fa5acf7f1671a032b65dcc3162fea762e7d62c9ad9eb` |
| `research/reverse/fixed-seed-global-screen/one-segment-derivative-independent-trial-01/norm-squares-m3.json.gz` | `61ba8f4bc24dd78b6fae00c7e8564b33887f4b2c10fa5f104227d99e3c85972f` |
| `research/reverse/fixed-seed-global-screen/one-segment-derivative-independent-trial-01/partial-sums-m0.json` | `4cfa82fb68eb651f93d58b4d1d1ee3e2ea9a33936d5940229b1a367bb7ad959f` |
| `research/reverse/fixed-seed-global-screen/one-segment-derivative-independent-trial-01/partial-sums-m1.json` | `aeb8b0f151ccd96c70e7926bf0299f0b4b7b5f2950e54dd631dbb88d959baab3` |
| `research/reverse/fixed-seed-global-screen/one-segment-derivative-independent-trial-01/partial-sums-m2.json` | `1839a87169e159499e8df7c4a3678c5d54c1ec1f2427b5ee7ab7d47fcefc754a` |
| `research/reverse/fixed-seed-global-screen/one-segment-derivative-independent-trial-01/partial-sums-m3.json` | `93126766eb8bbc4773fe997aa1375a758d559031ba88b457ec72b54e2895b78b` |
| `research/reverse/fixed-seed-global-screen/one-segment-derivative-independent-trial-01/progress.jsonl` | `6622c7962afcc98b064e75b286b9ef79b952faff6a5ef787fac5fd59f9f9b8c5` |
| `research/reverse/fixed-seed-global-screen/one-segment-derivative-independent-trial-01/result.json` | `5b720b8791ebc39c19d577c56903e5e0f18e4d20dc255ff5b4e6c6486d8d69ca` |
| `research/reverse/fixed-seed-global-screen/one-segment-derivative-independent-trial-01/run.json` | `f8cbfd035c7cf0bbcd1e405309cad1327e5d7c1d0e48c37635d65777d3183ebe` |
| `research/reverse/fixed-seed-global-screen/one-segment-derivative-independent.stderr.log` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `research/reverse/fixed-seed-global-screen/one-segment-derivative-independent.stdout.log` | `33282fe33af421999a5cd03c19596a0d6185eb873041f93bd7b8fbd294fd9643` |
| `research/reverse/fixed-seed-global-screen/one-segment-derivative-root-run.log` | `4e4de58fe6070e5c4e352c661ac1982487789c9698fdfa9770d6a170aba8692b` |
| `research/reverse/fixed-seed-global-screen/one-segment-derivative-trial-01/RUN_CLAIM.json` | `20ccca28dee7dd1c2e26e87327f158ae64517391b1f1459a562ddaa385e0cb91` |
| `research/reverse/fixed-seed-global-screen/one-segment-derivative-trial-01/norm-square-inputs.json.gz` | `42ade977e712f05f3243c3ab40c19a51f3219c8d4355d6278e38f216e1b07564` |
| `research/reverse/fixed-seed-global-screen/one-segment-derivative-trial-01/run.json` | `cf8cafeb3a36015e95da32cd372a9febdd19446af0ce449c577c2f83d6142a51` |
| `research/reverse/fixed-seed-global-screen/one-segment-final-record-check.json` | `0e54fd5210857d5ba135eb24cb1f3f00f8282e12ae74a2ab83da72a66c8eab90` |
| `research/reverse/fixed-seed-global-screen/one-segment-final-record-check.stdout.txt` | `32ee25921a2b16a9eca055b1bf49736b8b660fa4c9dd4729b74c47da2b57b48b` |
| `research/reverse/fixed-seed-global-screen/one-segment-independent-agreement.json` | `9a17cc31949592feca7176b620fda25065fa3a1928a37dd107e14c28eb684826` |
| `research/reverse/fixed-seed-global-screen/one-segment-independent-final-readback.json` | `8e3e472f7d7b041bf83eb1659cb5c6066f725ea18497618e4caba4fd31a39b1b` |
| `research/reverse/fixed-seed-global-screen/one-segment-root-readback.json` | `5fc0b35f5d3cfdf1ba8f16cc5d38165d73a79e589fce3bd88c87631a0dd788de` |

这些绑定固定本终审实际使用的证据版本，不以哈希代替数学证明或实际独立算术执行。
