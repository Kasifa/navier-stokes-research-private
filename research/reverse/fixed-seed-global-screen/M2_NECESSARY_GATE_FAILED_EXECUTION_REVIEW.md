# M₂必要门唯一失败运行的只读审查

2026-09-08。PRIVATE_CORE。结论：**NOT_ADMITTED / FAILED_FINAL_RECEIPT**。此次唯一运行不满足实际exit0与一致最终收据的联合接纳门；暂存科学判定不追认。没有重跑、重算B₀、构造新Fraction、修源或修改旧收据。

本审查者曾审过执行源码，但没有执行这次科学调用。现全文读取实际result/run/receipt/stdout、根保存的工具返回与非接纳记录，并定向复读源码末端失效分支。所做独立核对仅为SHA、字节、日志前缀、已记录资源整数及元数据连接，不是另一份科学求和。

## 已确认的失败连接

1. 根保全的工具返回记录实际chunk为7a3b03、exit_code=1。此处来源是该原样落盘记录；本人没有再次调用科学入口。其wall_time_seconds照原记录保存，不据此宣称程序的精确总墙钟。
2. 当前run.json为FAILED，SHA为c71eab10927c1a8e31e93045cfb06e3b2220dccd3eb1ad6cc909e7f303c38578。它保存 source_commit=ca8d379a9496c4c6aadb1d6a1c8cffaf262b153c、最终源码a3a7cd37…以及 final_receipt_invalid.reason=LATE_PEAK_ABSENT_FROM_RECEIPT。
3. 保留的旧final-receipt.json仍写COMPLETED_SINGLE_NI4_GATE，并绑定先前run SHA bf733ea922730ea00a172eadd29d33deab070b0260b5710bf6d67cbaac091262；该SHA与当前失败run不同。stdout第一行对应先前状态，第二行准确绑定当前失败run，并显式写invalidates_earlier_receipt=true。不能只读取第一行或旧收据接受计算。
4. 旧收据所绑定的stdout长度715 B及SHA，实际恰等于当前日志第一行的完整字节；当前两行stdout为972 B。这与后续追加失效通知一致。旧收据没有被静默改成新的成功记录。

## 失败原因与剩余边界

收据保存SELF峰值32669696 B；随后run内 final_receipt_invalid.actual_observation 保存32702464 B，增加32768 B。两者均小于固定268435456 B（256 MiB）上限。该后续观测的输出为49112 B、elapsed_seconds=0.04916679114103317，也没有触发源码的预算超限分支。

因此这次触发的是**后续峰值未被先前收据覆盖**，不是已记录的256 MiB、60秒或16 MiB预算超限。源码按事前规则使收据失效、将run降为FAILED并退出1；不因差额小或尚有余量而豁免。以上只是对已注明时点观测的解释，不反向补造解释器退出后的峰值或完整资源接纳。

失败记录写完后，本审查实际清点原调用目录全部六文件加stdout/stderr，合计49568 B；与根非接纳记录一致。此数包括保留的旧收据和失败通知，不包括随后生成的根/本审查文件，也不以旧收据的49112 B代替当前总量。stderr实际为空，但空stderr不抵消exit1或收据失效。

result.json已保存29472项求和后的字段和临时decision=UNDECIDED_FOR_LINF；它的字节SHA与run、旧receipt、stdout第一行的result指针一致。**此处只确认暂存结果存在及连接，未核算其B₀、Q₂、D或将它们纳入已接受的科学证据。** 既不能据此声称固定M₂包络通过，也不能据此声称必要门给出已接受的新障碍。

原NI条件公式及既有静态审查没有因此自动变成数学错误；静态PASS本来不保证实际出口通过。两个上游生产核的资源缺口仍在，当前结果、run、旧receipt、stdout两行与根记录中的producer_resource_complete、resource_complete、certificate_ready、release_ready四项均为false。本次没有完整新证书或发布就绪状态。

本审查仅确认应保留这份失败并拒收临时科学结论。禁止追认、改旧receipt、修源后自动重试、重算第二表示、换节点或另选参数；后续纯解析工作不把这次暂存值当成已支付输入。

## 实际字节绑定

下表仅绑定本轮读取的实际证据。前次源码全文审查的范围保持原样；本轮不重验其全部旧输入，也没有解码任何科学二进制。

| 实际输入路径（相对反向树） | SHA-256 |
| --- | --- |
| `research/reverse/fixed-seed-global-screen/m2-necessary-gate-trial-01/claim.json` | `2477990862808689a48d1fec87dc36266e31bb46e72ebdeee7f15a4993f1ed22` |
| `research/reverse/fixed-seed-global-screen/m2-necessary-gate-trial-01/configuration.json` | `71c13aacaca92018f44766033e55a283f83c2b0fb65f46650198a56c73b68702` |
| `research/reverse/fixed-seed-global-screen/m2-necessary-gate-trial-01/final-receipt.json` | `767c1f52bf39fb95612cfef066cf3d959b9acf4b7dfc1c1a3ed5429c30c0ceb5` |
| `research/reverse/fixed-seed-global-screen/m2-necessary-gate-trial-01/result.json` | `6c3b5670b15a0a8c7cc596c66a152441849964c65245255e7930e33a35cb2da4` |
| `research/reverse/fixed-seed-global-screen/m2-necessary-gate-trial-01/run.json` | `c71eab10927c1a8e31e93045cfb06e3b2220dccd3eb1ad6cc909e7f303c38578` |
| `research/reverse/fixed-seed-global-screen/m2-necessary-gate-trial-01/source-snapshot.py` | `a3a7cd37cf21a4322ed710bb1281908bd3332589a83d4acd7205e3f425f920cd` |
| `research/reverse/fixed-seed-global-screen/m2-necessary-gate.stdout.log` | `a0af8414a0fc2f3853a66a2969fb97597f2856048ba96c37823e3b1a9f6414bb` |
| `research/reverse/fixed-seed-global-screen/m2-necessary-gate.stderr.log` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `research/reverse/fixed-seed-global-screen/m2-necessary-gate-root-tool-exit.json` | `b95206a428a7dd8bda1c36964067120349f55f673cd3875c5102caf97add2a8b` |
| `research/reverse/fixed-seed-global-screen/m2-necessary-gate-root-nonadmission.json` | `a7fb6824507ee7b9cc3726f276eb0bdaa1be2587df5c1b653f38149e872baaaf` |
| `research/reverse/fixed-seed-global-screen/audit_m2_necessary_gate.py` | `a3a7cd37cf21a4322ed710bb1281908bd3332589a83d4acd7205e3f425f920cd` |
| `research/reverse/fixed-seed-global-screen/M2_NECESSARY_GATE_EXECUTION_CONTRACT.md` | `7ee3b897fd2c7cabd7fbeedb8c0c053130bcdd7e46fbc1dd1c602fa3a454e9cd` |
| `research/reverse/fixed-seed-global-screen/M2_NECESSARY_GATE_ROOT_SOURCE_REVIEW.md` | `9d2d56b52b547b3f4aa82f5baaa81f64a4eca67ff194af418f55fbb6e82bae23` |
| `research/reverse/fixed-seed-global-screen/M2_NECESSARY_GATE_INDEPENDENT_SOURCE_REVIEW.md` | `151cd8181364f0c7d1c06a83b4b2c2d74ff65b9bb46f527148a719009d0d9f4c` |
