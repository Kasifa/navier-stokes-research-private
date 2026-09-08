# MPS 内部方法检查：审读与来源范围

2026-09-08。PRIVATE_CORE。只审查本次内部记录，不是研究发布、真人同行评审或一般正则性认证。

## 数学与量词

主任务从原周期 NS 重推 MPS.1–3、MPS.5–10，实际全文读回 207 行 12665 B 稿，并核对最终全部文字差异。压力零模、投影非线性项与物质加速度的区别、黏性交叉系数、核分部积分、空间／时间指数、两端切片及全部截止项均保留。

- MPS.2 与 MPS.3 等价；它们不产生两个独立估计。
- MPS.4 的 Hölder 指数不足，不等于证明真实 NS 乘积不可积。光滑恒等式向能量弱解传递仍有未核验的乘积／缺陷问题。
- MPS.7 是周期化单壳 Schwartz 核的直接界，不是全 Riesz 算子的同一强范数界；未无损求和。
- MPS.8 的右侧为 g³，基本能量只控制 g² 的积分；这一步没有时间 L1 结论，不排除更细抵消。
- MPS.9–10 保留局部测试、两端切片及换物质压力导数后恢复的两个正号输运项。
- 最终稿承认固定分离球的远压空间导数可由能量估计；未证的是所需尺度小量或严格增益，不是“全部尾项完全不可控”。

## 实际协作审读

A：good_scale_route_comparison。实际全文审读上述 207 行 12665 B 稿，SHA 759d7037b7e3c1f21dccccae501b4fe3cf3052b11d5acb7c2adc892663e8d743，数学与旧路线范围限定 PASS。最终核对 208 行 12866 B 稿及全部澄清；内存逆还原修改精确恢复旧哈希，接受最终字节。A 参与本轮旧路线判断和压力时间恒等式核算，不称全稿完全非作者审读；未认证外部原稿。

C：ma_freeze_review。实际全文审读同一旧稿并逐式核对 MPS.1–10，提出远压措辞需收窄。其 R073U §5 意见对应英文解析稿；主任务实查后明确中文报告 §6 链接，C 接受这一定位。最终同样经实际字节和逆还原检查接受全部澄清，无剩余必改项。C 参与 MPS.1–5 构思，此次不是全稿完全非作者复核。

B：variable_reference_check。本轮只完成 CG/LP 去重：全文读 clay_b_clock_stochastic_screen_20260907.md 1–260、clay_b_leray_paid_budget_20260907.md 1–304、clay_b_laplacian_defect_audit_20260907.md 1–54；没有读本 MPS 最终稿，不计为最终稿审读者。未重新获取随机表示原著，结论只为停止重复该分支。

主任务和审读者均为 AI 辅助；没有外部数学家审稿或新颖性认证。

## 本地与外部来源

A 全文读 BG（332 行）、BT（308）、BU（302）、BE（110）、AG（187）、MA（183）及 recent_source_screen_literature（57）；另读 AP18 115–202，含完整 §4（125–192）。具体文件依次为 clay_b_pressure_potential_energy_screen_20260906.md、clay_b_convex_pressure_trace_20260906.md、clay_b_same_parent_residual_20260906.md、clay_b_bernoulli_energy_gate_20260907.md、clay_b_bernoulli_shell_20260906.md、clay_b_mixed_absorption_calibration_20260908.md、clay_b_recent_source_screen_literature_20260906.md、clay_b_annular_propagation_prerequisites_20260908.md，均位于 research/。这些实读范围只用于去重，不能把伴随原子、非 NS 时间族或初端反例扩作原 NS 终端结论。

主任务本轮全文读 BE、LP、pressure_mechanism_screen_report、signed_mixed_pressure_reading、recent_source_screen_literature、pressure_regularity_literature_check、pressure_quotient_report-source 和 R073U evidence_gap_matrix；定点读 R073U 中文报告 §6 的相关完整方差部分，其他部分不称全文。C 另按其初始检查读 pressure quotient 全文、BE 1–59 和 tensor heat hierarchy 的 §1、§3、§6、§8、§10；最终章节核对不扩为该稿全读。

外部来源以主稿台账为准。主任务直接读取 Isett v9 共同假设及 Theorem 1.5 陈述、HTML §4 全部 497–722、§5.1 全部 725–802；没有重审全部上游 §2，不调用其定理证明 NS 新结论。Colombo–De Rosa 2020、Tran–Yu 2018 只读摘要／元数据；Tran–Yu–Dritschel 2021 只读摘要及导言片段。本轮没有重新认证任何整篇论文。Constantin 作者 PDF 只定位 URL，未进行页面核读或下载归档；PDF 技能仅检查，未生成／修改 PDF。

## 字节与结构检查

主稿最终为 208 行、12866 B，SHA256 5556ecd2fcfc95863c121fba07e9cbfb438f9b34fd1aa0cba26d07752bfc1aaf。最终新增一个远压边界句、收窄相邻句、澄清三个访问日期及一个中文来源链接；无公式变动。

结构检查通过：13 对展示数学分隔符、65 对行内分隔符、MPS.1–10 顺序唯一、4 个本地 Markdown 链接目标存在。首个简易链接检查误把数学交换式识别为链接；剔除数学块后复检通过，没有为此修改公式。主稿为私有 Markdown 源，未生成网页或进行浏览器／打印渲染，不声称视觉验收。

本轮不构成独立研究小节，不创建 release、科学图或发布消息。既有 QPS/EWT 源与 EWP 冻结／移交记录不修改。
