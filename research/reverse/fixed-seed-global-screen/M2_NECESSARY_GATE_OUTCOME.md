# 二阶导数必要门：最终收据失败，结果不接纳

2026-09-08。PRIVATE_CORE。**NOT_ADMITTED_FAILED_FINAL_RECEIPT**。这是一次真实执行的失败记录，不是数学反例或已通过的必要条件。

唯一源码提交 `ca8d379a9496c4c6aadb1d6a1c8cffaf262b153c`，源码 SHA `a3a7cd37cf21a4322ed710bb1281908bd3332589a83d4acd7205e3f425f920cd`。根与非作者完整源码审查、28项固定来源静态检查均在执行前完成并提交。根随后只执行一次 --run；工具返回 chunk `7a3b03`、exit_code=1，原样证据存于 `m2-necessary-gate-root-tool-exit.json`。

运行确实完成了规定29472项原整数平方和并写出临时 `result.json`，其内部判定为 UNDECIDED_FOR_LINF。但最终实际退出不是0，收据也已失效，**这个临时判定和数值均不纳入已接受的科学结论**。这里不依据它继续放宽参数、变换节点或生产新的必要门。

失败原因准确为 `LATE_PEAK_ABSENT_FROM_RECEIPT`。收据中SELF峰值为32,669,696B，最后一次校验观察为32,702,464B，增加32,768B。最后一次记录观察耗时0.049166791秒，内存也低于256MiB；这不是实际资源上限超限。它违反的是已锁定的末端收据一致性条件。程序随即把run改为FAILED，stdout第二行明确 `invalidates_earlier_receipt=true`，退出1；早期成功字样不可覆盖最后结果。

旧 `final-receipt.json` 仍记录旧run SHA `bf733ea922730ea00a172eadd29d33deab070b0260b5710bf6d67cbaac091262`，最终run已为 `c71eab10927c1a8e31e93045cfb06e3b2220dccd3eb1ad6cc909e7f303c38578`。失效后完整本次目录加外层stdout/stderr共49,568B。根已实读最终记录、末行stdout、旧收据和实际工具退出证据，并保存 `m2-necessary-gate-root-nonadmission.json`；没有重新求和或把失败记录改写成成功。

这次失败说明当前收据设计的“末次峰值必须与较早收据完全相等”并未在本次实际写后路径保持。后续SHA/元数据操作也可能抬高进程高水位；执行前静态通过不等于运行接纳。失败出口发挥了预定作用。此处不修改冻结源码、收据、资源阈值或接纳标准，不追认临时结果，不重跑这个科学核，也不以换名称再次执行同一科学工作。

两个原生产核另有未补齐的隐式helper资源证据缺口，仍保持原更正。producer_resource_complete、resource_complete、certificate_ready、release_ready全部为false。此次失败不撤销已经完成的单段残差限定算术对照，也不撤销独立的纯解析控制预算单调性证明；它没有新增可接受的M₂数值障碍。

后续研究转到不依赖本次临时值的解析问题：对符号μ₂≥19/5，严格审议同一控制函数族的全窗最小门是否仍在终点。须另给证明，不能把旧固定参数结论自动外推；不读取新数组、不选择m/ε、不把全窗数学输入当作已支付。固定原初值继续 NO-CERTIFICATE-YET-FOR-FIXED-a。本项不正式冻结发布。

实际失败证据绑定：

- `m2-necessary-gate-root-tool-exit.json`：`b95206a428a7dd8bda1c36964067120349f55f673cd3875c5102caf97add2a8b`。
- `m2-necessary-gate-root-nonadmission.json`：`a7fb6824507ee7b9cc3726f276eb0bdaa1be2587df5c1b653f38149e872baaaf`。
- `m2-necessary-gate-trial-01/final-receipt.json`：`767c1f52bf39fb95612cfef066cf3d959b9acf4b7dfc1c1a3ed5429c30c0ceb5`（失效历史收据）。
- `m2-necessary-gate-trial-01/result.json`：`6c3b5670b15a0a8c7cc596c66a152441849964c65245255e7930e33a35cb2da4`（未接纳的临时结果）。
- `M2_NECESSARY_GATE_FAILED_EXECUTION_REVIEW.md`：`0689cc2730ef9e046d8085308698ca35834bb6692acfd46acab6bbc2b51f2d3e`。根已全文读取并接受独立只读审查的NOT_ADMITTED结论；这不是对暂存数值的独立复算或追认。
