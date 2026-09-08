# 独立输入核验源码与最终字段适配

2026-09-09，PRIVATE_CORE。**源码已形成并完成作者静态全文自读；尚未执行、导入、编译或试探运行，尚无独立核验结果。** 本文只说明 VERIFY_METHOD 如何落实到 verify_input.py，以及实际主原输出到达后的字段适配。执行仍须根与非作者审查、运行前保存及根的明确启动；本文件不是该启动。

## 1. 形成次序与身份

本人是 VERIFY_METHOD 和 OBSERVATION_ERROR 的作者，曾审过第 24 包有关 B/C 接口，未参与本次生产核心编写。根在方法形成前已披露组织预见，方法并非全课题盲推。方法 f0798c5d 停定且经根全文读后，才编写独立核验核心。首先按根提供的字段说明写核心，当时未读取主原 JSON；其后根告知唯一主执行已停止并提供实际 hash，才定向读取原 JSON、全文读取监督记录，完成元数据字段适配。

没有读取 prepare_input.py 或 run_input.py 的源码内容，没有复制或导入生产核心，也没有读取或导入旧 A/B/C 程序。两个生产源的 SHA 来自主原记录，仅纳入未来核验的字节绑定；字节哈希不等于全文源审。监督器也自行编写，未复用生产监督源码。单子进程、Popen 前至 wait 后计时、事后 RUSAGE_CHILDREN 和独占写入这些共同原则来自同一合同，不声称它们是两套不同数学原理。

## 2. 未改变的数学对象与覆盖

源码只核原 P 在原隔离区间中的同一根，不重新支付旧全根唯一性。P、r、s 由 CA.5、CB.3 正文逐项转录。其余责任如下。

| 类别 | 独立组织与严格匹配范围 |
|---|---|
| 规定二分 | 正公分母清成整数系数，在每个 dyadic 点用整数齐次和求准确 P 值及符号；独立生成全部路径，再逐步比较 before/midpoint/P_midpoint/branch/after，核起终点、嵌套、步数及宽度。 |
| 五项 Horner | 先从原系数组成 −s、r、−3s+5r、2s、−2r，分别作合同唯一 Horner；整数分子分母乘加及交叉比较，保留全部四乘积和各步区间。四乘积按含重复项的多重集比较，因为合同不规定四项展示次序；各步区间仍要求完全相同。 |
| q=36 | 中点多项式点值用整数齐次和，负数亦用 Euclidean 向下商；同时核最近格点距离、等距时偶数和准确格点有理值。主日志的缩放余数可能已约分，故比较 remainder/remainder_denominator 的准确比值，而非要求其未约分整数表示相同。 |
| 重建与浮点 | 独立构造 U/V、三次循环和正负共轭，共十二模逐条核频率、系数、整数点积乘项及固定坐标顺序的全部部分和。显式核构造分子、乘项及中间和的 2^53 界；不是只核最后零和。 |
| 物理 binary64 | 核代表 U/V 的全部记录、十二模全部系数 hex 以及各浮点点积零值。由 IEEE 位分解重建准确有理数，再交叉核 as_integer_ratio；所有物理 dyadic 坐标必须准确回到原有理系数。 |
| 时间 binary64 | 分别核 T、a 的准确原值、hex、回读、有符号及绝对转换误差；用相邻 binary64 的准确有理中点及尾位奇偶检查最近偶数转换，不把它们当无误差 dyadic 坐标。 |
| 初始误差与终点 | 按原坐标区间到重建坐标的最大端点距离，精确匹配 eU_i/eV_i、eU/eV 和三范数上界；精确匹配原 C、T=8/C、a=T/2，无窗口优化。 |

核心保留“恰遇准确中点根立即停止”的数学分支。最终元数据适配只接受现已停止的这个非点、恰 80 步记录；若独立路径得出其它分类，直接失败。不能以这一固定记录的核验声称已实际执行或认证所有可能停止分支。

主端的可选原范数字段由根在本核验执行前明确其准确算法，不从显示小数推断。取 U 的三个坐标区间为 [0,0]、[1,1]、I，V 的三个区间为直接五项 Horner 中后三项。区间平方在跨零时下端为 0，否则为两个端点平方的较小值，上端为较大值。M² 区间为六个平方区间对应端点和的六倍，能量区间为其一半；A0_upper 为六个坐标区间最大绝对端点之和的六倍。源码对这三项作**精确等值比较**，不降为只检查包含关系。它们均为区间或上界，不是原范数已求成准确单值。

## 3. 实际 schema 与证据边界

实际主输出是 annular-input-v1，原状态仍为 INPUT_PREPARATION_PASS_PENDING_INDEPENDENT_VALIDATION。原监督记录状态仍为 EXECUTION_PASS_PENDING_INDEPENDENT_INPUT_VALIDATION。这些是主执行当时的历史阶段标签；源码保持原字节并检查其身份，不能据标签直接接受数学内容，也不能据 pending 阻止以后独立证据解除条件。

科学输入浮点责任已经覆盖 dyadic_reconstruction.binary64 的 U/V、twelve_modes 的全部 float_hex 与 dot_product_float_hex，以及 fixed_observation 的 T_binary64/a_binary64。各 decimal_display_only 仅为展示，不作为数学证据。serialization_guards 的 scalar_nodes 与 maximum_rational_bits 没有重算，也不用于任何数学接纳；实际原文件字节界 1048576 会检查。没有因覆盖纯展示字段增加额外执行。

原监督记录只作来源、身份、源 hash、原输出 hash/bytes、启动次数、退出、完整状态、环境单位及资源字段一致性核对。其所报完整子生命周期 0.041177708 秒、事后 CHILDREN RSS 16187392 bytes 是原记录，不是本核验者重新测量主运行。源码不会调用 Git、ps、platform.platform 或生产程序。

## 4. 唯一执行接口与资源责任

监督与 worker 同在 verify_input.py。父进程仅作参数、字节绑定和监督元数据，只有一个新鲜科学子进程执行数学核验。默认不带 --authorized-run 时不能启动；该显式旗标也不自行构成授权，须由根在静审与保存后使用。子入口还核实际父 PID。源码最终不需为启动再修改 ADAPTER_READY 或其它字节。

最终调用接口如下，尖括号字段由根在实际运行前填入真实值；这只是接口说明，本文形成中未执行此命令：

```text
/Library/Developer/CommandLineTools/usr/bin/python3 /Users/kasifa/Documents/Math/navier-stokes-reverse/research/reverse/annular-source-observation/verify_input.py
  --authorized-run
  --input /Users/kasifa/Documents/Math/navier-stokes-reverse/research/reverse/annular-source-observation/input-preparation.json
  --input-sha 3f51705fbd934ce76d503c1c856566405ee3deb1760474b1c73ef6a6f481c61f
  --producer-receipt /Users/kasifa/Documents/Math/navier-stokes-reverse/research/reverse/annular-source-observation/input-execution.json
  --producer-receipt-sha a1557535b1beec08f1a80e22444e811bff78a4dba91a5ea7adbfe267f3fed13b
  --source-sha f9696e242d1eed0a2135870730d5100731dc80283f13fd8cdc0547e20eea04b0
  --adaptation-sha <本最终适配说明的实际SHA-256>
  --source-commit <根保存的本核验运行前提交>
```

最后一项只是根提供的来源标签，核验器不自行访问 Git。运行时同时核自身源与本说明的真实 SHA，避免自绑定循环。输出固定为本目录 verify-input-output.json 与 verifier-execution.json，均独占创建。已有输出时阻断、不覆盖；启动前的参数/来源/路径阻断在 stderr 报错，科学子进程未启动，不伪记一次已完成核验。监督记录在唯一 Popen 之前独占预留；一旦尝试启动，后续异常、超时或失败均不得触发重跑。启动结果无法确认时保留 unknown，而不伪报 0 次。

计时从 Popen 前到 communicate/wait 返回，5 秒期限从同一个起点扣除启动用时，覆盖子进程启动、读取、算术、完整序列化、写盘及退出。超时终止并回收，再记录含回收开销的实际时间。新鲜父进程须无既往子进程；事后按 Darwin bytes 读取该唯一子进程的 RUSAGE_CHILDREN 峰值，验收不超过 256 MiB。它不是实时 RSS 硬限制，也不是父子同时总峰值；父端回收后的结果解析、哈希及监督记录写盘不在此子生命周期界内。

根与非作者静审初版 bfe712e6 后，都指出 METHOD §8 要求父进程自身 CPU/RSS 另列，而初版未存 SELF 字段。最终仅在监督器 receipt 序列化前新增第 1063–1076 行：RUSAGE_SELF 用户/系统累计 CPU、Darwin bytes 峰值 RSS、父 PID 与明确截止说明。该采样排除之后的序列化、写盘、关闭及退出，不是完整父生命周期或同时父子总峰值，绝不与子峰值相加。算术核心、主输入字节、物理输出字段与执行预算均未改。作者已实际重读最终监督器第 973–1106 行，关闭此项遗漏；没有以静审修改为由运行程序。

任何数学不一致、缺字段、源变动、异常、回读失败或预算失败均停止。worker 的 VERIFIED 还必须结合监督记录的退出 0、完整状态、PID、未超时及墙时/RSS 通过才可接纳。独立输出本身不能覆盖监督失败。该计划是主一次、独立核验一次中的第二次科学执行，不能降格成元数据；当前核验端实际科学执行数仍为 0。

## 5. 实际阅读、字节与停稿

本轮全文读 INPUT_CONTRACT 与 VERIFY_METHOD；此前形成当前方法/观测接口时已读 CONTRACT 当前相关全文。原 CA.5 与 CB.3 在写源和最终自读时按下表范围重核。原 JSON 只为实际字段适配定向阅读，没有手读其全部中间数组；完整数组核验责任由上述未来唯一 worker 承担，不提前报告一致。

| 文件（均在 research/reverse 下） | 实际阅读范围或字节核范围 | SHA-256 |
|---|---|---|
| annular-source-observation/CONTRACT.md | 当前全文的先前实读；本次复核字节 | 4ae019c3aac7d23a2392273a8cfb52ba08cf5131c35f8bc9e56918dae41c68d8 |
| annular-source-observation/INPUT_CONTRACT.md | 全文，1–30 行 | 2d02549be48f26001c794b06f8d7ecb74e46be3ed051e72019860a56eab6768d |
| annular-source-observation/VERIFY_METHOD.md | 全文，1–190 行 | f0798c5d4fa8b798af3c59d8159e150ac6e30950a95a064253f8da3f7d81a3d6 |
| cyclic-six-carrier/ALGEBRA_A.md | 99–119 行 CA.5；另作标题定位 | a5dad046a56e3f6d6a9a417304635c23c9e84871528baffbfd5dbedf6cfea32b |
| cyclic-six-carrier/ALGEBRA_B.md | 7–60 行，旧单根责任与 CB.3；不重新执行旧证书 | 2321cea6a0b066e5356b98c22198bf389180e4a53181c4e5bb3ab9825093c499 |
| annular-source-observation/input-preparation.json | 1–43、202–286、2774–2839、3415–3673、4080–4318 行；另用键名定位。实际核 133961 bytes | 3f51705fbd934ce76d503c1c856566405ee3deb1760474b1c73ef6a6f481c61f |
| annular-source-observation/input-execution.json | 全文；实际核 2935 bytes | a1557535b1beec08f1a80e22444e811bff78a4dba91a5ea7adbfe267f3fed13b |
| annular-source-observation/verify_input.py | 初版作者全文静态自读 1–1092 行，再定向核原系数；补 SELF 后实际读最终监督器 973–1106 行，其它源码未变；没有语法执行检查 | f9696e242d1eed0a2135870730d5100731dc80283f13fd8cdc0547e20eea04b0 |

生产两个源 hash 7010b49e1d13693a963963824d2c6b00ada707b197e899806a719fc4f4dc5cf1 与 ee83bb8f6c0ce50aae9e45553ce7e9e59d84bb641aed5b3fd9ed9c080c74f028 仅取自主记录并在代码中锁定，本文不把它们列作本人已读源码。后续 worker 会实际读字节哈希，但仍不会解析或导入它们。

源码和本说明完成作者全文自读及来源字节复核后停止修改，送交非作者静态审查；本文不自绑定自身 hash。当前没有运行、导入、compile、测试探针、科学求值、Git 或外发。输入若后续获核验，只支付同一 a_* 的近似输入准备、误差上界与固定观察端点；未支付 H³ 全窗证书、真实 NS 存在窗或任一来源门。
