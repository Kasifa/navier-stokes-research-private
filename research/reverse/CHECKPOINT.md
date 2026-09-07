# Reverse research checkpoint

2026-09-07。ACTIVE_RESEARCH_CHECKPOINT。仅反向树 `navier-stokes-reverse`、`codex/ns-reverse`。

首轮研究已通过：固定原解有限两代模态产生及严格无限维余项；完整压力使一阶新生场对种子的主动输运为零，同一低阶目标出现于全局光滑三角负对照，指定三元组不复制。未接受可迭代奇性机制。精确问题、全证明、来源和独立审查在 `research/reverse/first-cycle/`。本轮没有图形、仿真或远程任务。

科学源提交：90c44d1703486e3983d12b87ed54f22c8c677982。首轮RESEARCH_COMPLETE，冻结信封见 `first-cycle/freeze.json`。

首轮冻结提交：b72d4627bfbed913214d01514ba1696ce68632af。PRIVATE_ARCHIVE已一次投递，见HANDOFF_LOG.json；不重投、不查询存档或网页。

交接后已实际完成下一项有限预检：全部三组种子的混合导数在0–2阶为零，第3阶非零；Python/Ruby逐系数一致，独立18项检查通过。当前资料在 `research/reverse/next-mixed/`。这只是有限代数诊断，没有新正时间PDE余项，没有新增正式release，不属于首轮冻结包。

下一步不是自动增加Taylor阶数：先在混合目标上规定一个有界的正时间驱动占优合同，保留全部同阶替代树、完整压力和无限维误差，审查它是否增加了超出有限激活的信息；可接受、收窄或停止。未证明自主再生、统一迭代、单一固定初值无限尺度或奇性。恢复时先读该预检与首轮NO-CANDIDATE，不把非零混合系数当成可迭代机制。

## 恢复授权及保留历史

- 科学继承基线：d58abdd9390ef8ced52f1807a956a663853f7680。
- 初始启动只建立记录；随后用户“先暂停一下”，反向独立暂停，未科学冻结。管理保存重复入口暂停记录于 `PAUSE_DUPLICATE_ENTRY_20260907.md`。
- 管理治理提交d16d669123c2965694e4203a7618dc569da51438只更新AGENTS，不是科研来源。
- 2026-09-07 18:59迁移/隐私管理独立验收后的正式派发恢复本任务。之后没有新的用户暂停。新的用户暂停始终优先。
- 不运行正向research helper，不改正向索引/检查点，不读取发布队列或发布索引，不push或监控网站。完整新成果PRIVATE_CORE。
