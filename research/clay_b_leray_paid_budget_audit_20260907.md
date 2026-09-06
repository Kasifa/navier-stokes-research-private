# Leray / paid budget：内部审读与记录验收

2026-09-07。基线：8aa141cac7027101f1bfc3301d18e1011e5040bb。
内部预检，不是新科学 release；G/R OPEN；NOT CLAY。

## 1. 审读对象和分工

根任务构造 LP.1--14、关键原著复核、证据综合及实文件。
A 是 Constantin 原著版本、逆矩阵问题及反核来源的调查参与者。
B 是 Pooley 来源调查和低阶均值预算的构造核算参与者。
A/B 均不记作本轮非作者完整审稿人。

C 是本轮唯一完整非作者内部审读者。
C 全文审读实际主稿、报告和台账，独立重推 LP.1--14，
未发现阻断性数学错误。主稿与报告不需数学修订，保持如下表字节。
C 全文读到的初始台账为 344 行、15675 字节，SHA256
9ff8c9c12fd05cd485803997b572b934baa72b23bdf7590d3c48086239434f13。
此后的台账只更新审读角色/范围、验证状态和相应置信措辞，不改来源结论或数学。

## 2. 关键接受结论

- 完整余切输运把梯度映为梯度；不是分别交换 P 与输运或应变。
  负乘积源、正协方差源，以及完整局部截止压力/扩散项一致。
- 商式 enstrophy 端点、黏性次数、两次时间 Hölder 和 Young 正确。
  结果是非临界速度时间可积界，不是 Serrin 临界输入。
- 位移与 N 的有界向量 GN 不需要零均值；初值梯度、最大值成本保留。
  T/PT 属于时空 \(L^{4/3}\)，Pm 在能量类并有 \(L^4\)；
  Pc 当前只有能量类，且该界用了原 NS 能量。
- 源的缩放和抽象标量例子正确；例子不是实际 NS/协方差源。
- 虚速度仅在平均 M 可逆区间使用；修改模型的最大值原理不能直接移用。
- 没有完成 G/R、扩大正则解类、证明新颖性或排除真实奇点。
  下一步策略复评没有被预批为一个新正面机制。

## 3. 实际来源阅读范围

C 检查 CI 表示定理和所需完整 Itô 证明，包括式 4.5 与第 4.1 节；
Constantin v1 的逆矩阵/虚速度原段、K-bounds 及证明、完整 Appendix A，
并检查更高阶界的额外四次时间成本；
Pooley Props.2--3 完整证明，Props.4--7 实际测试量词及所供证明，
模型式 11、Lemma 8 完整证明和式 22--24；
MSP Theorem 1.1 及第 2--5 节的拓扑、局部逆矩阵、旋转漂移和热松弛证明接口。

C 未读 Constantin 作者修订 PDF；A 的 PDF 阅读不记作 C 或根的 PDF 阅读。
Pooley 引用的完整 Prop.6 外部证明未读，不采用为本轮正面输入。
MSP 给定漂移结果不声称无外力周期 NS 反例，不采用其非严格概率讨论。

C 对历史仅阅读 CG、G 合同及策略/方向扩散的所需原段，
另独立核验台账 6/6 实际文件的哈希、长度和基线原始字节身份；
严格 JSON 无重复键通过。这不是六份历史全文重审或全部外部依赖认证。
根的全文/选读范围分别保存在台账，不扩张为全仓库认证。

## 4. 结构、保护与可复现性

脚本 scripts/clay_b_leray_paid_budget_record_qa.py 仅做记录验收。
首次执行时，15 项非计划状态检查通过；唯一未过项是刻意保留的
verification=in_progress。完成检查后才改为 complete。
最终 16/16 检查通过，两次同实现执行的完整输出逐字节相同。
三项内存负对照拒绝缺失 LP.14、重复 LP.7 和篡改旧 review；
它们不是数学文稿变异、PDE 证明证书或两套独立实现。

实际保护检查确认：

- 23 个旧 review 值逐个不变；只加一个本轮字段，共 24 个。
- 每个不属本轮当前状态/下一步的旧 checkpoint 解析值保留。
- 私有 paper 解析对象完全相同；排序键 JSON SHA256 为
  c9755ea86f93575cc96c28ac5b3caa1a059bddec2b58a448d09d9cc54d6431c5。
  明确使用 Python json.dumps(paper, sort_keys=True) 默认 ensure_ascii=True、
  separators=(', ', ': ')，UTF-8，无额外换行；不是紧凑 JSON。
- 16 个历史/最新 release 的身份、顺序、source/freeze 和单次收据保留。
- 用户 AGENTS.md 仍为
  80959a5c6d2db01543f8f1ae1ddc2e1ba7430c1b14d1b4ef658dcc965efecfab；
  不纳入本轮提交。
- 既有 tracked 文件除研究 checkpoint 和用户 AGENTS.md 外没有改动。

C 最后完成一次记录增量验收：台账状态/角色等值逆还原后精确恢复
9ff8c9c12fd05cd485803997b572b934baa72b23bdf7590d3c48086239434f13；
独立确认全部保护值、六行文件绑定和同脚本 16/16 输出。
其已审本 audit 版本为 101 行、6062 字节，SHA256
d190ae9b5c2a0d1d1c114a9f5f6ead1bc13e3d3a84698b8abcd3a83cf14bac39；
此后仅增加本段验收回执，不计第二次 LP 全文数学审读。

无数值实验或有限计算数学证书；没有生成读者 HTML/PDF，也没有渲染/视觉验收。
结构检查不冒充视觉检查，数学内部审读不冒充外部同行评审。

## 5. 绑定字节

本表不包含自身，避免自哈希循环。

| 文件 | 字节 | 行数 | SHA256 |
| --- | ---: | ---: | --- |
| research/clay_b_leray_paid_budget_20260907.md | 12346 | 304 | 788d06c56c61a4e68d609118cb50e114f5328c0c8e6c588463cac6bfd88a51fb |
| research/clay_b_leray_paid_budget_report-source_20260907.md | 2570 | 40 | cb0f2c12b0adba5cb2c9b833cd08782cae60629249b180672c95ec61c0f32553 |
| research/clay_b_leray_paid_budget_literature_ledger_20260907.json | 17158 | 351 | f8f9a8786fe2ad36fc82db96c99a78f5b556e3c75e600a2625da6eebcc658f8b |
| research/clay_b_active_checkpoint_20260906.json | 56006 | 173 | 012912d1be15b3a07e36801ded4276dd91001482449c8a9cc59e77ea639684ed |
| scripts/clay_b_leray_paid_budget_record_qa.py | 6127 | 128 | ee0857d1b39b80748acf169cf495548ed80bd369101da7cbbaea5b620bdbf4a5 |
| research/clay_b_leray_paid_budget_record_qa_20260907.json | 4130 | 152 | a0df46e46af7ad8d43828057de2eb1b21a4cd62f6dc637d2d98fcab15c80dcce |

## 6. 当前出口

本轮完成的是内部投影去重、已付范数补全与逆矩阵/模型适用范围纠正。
最近科学小节仍是 ClayB-SourceEnstrophy-20260907；既有单次交接记录保留。
本轮没有创建新的科学冻结或发布交接，没有重发旧 release。
未读取发布任务、发布索引、队列、状态或 CI，
没有等待、轮询、监督、部署、推送或报告发布结果。

研究恢复指针将在本地记录提交后只更新 research 索引。
下一步是有界策略复评，而非自动延伸已关闭的投影支线。
研究目标保持 active；本记录不是 Clay 完成声明。
