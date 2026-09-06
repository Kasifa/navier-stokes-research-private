# 源项与梯度能量成本：研究冻结与一次交接回执

2026-09-07（本地日期）。**RESEARCH COMPLETE / HANDED OFF ONCE / G OPEN / NOT CLAY。**

## 1. 冻结身份

- release_id：ClayB-SourceEnstrophy-20260907。
- 前序：ClayB-SignedMixedPressure-20260907。
- 研究仓库：/Users/kasifa/Documents/Math/navier-stokes-r074m。
- base：363bb4b83b2b3c3db605e42e05491072cb073bf5。
- source：53f167438c058c77aa218216a014c3e504300300。
- 包含 manifest 的 freeze：6c6186d86d22c925eb2f7e7d03ad39f291f4dfac。
- manifest：research/clay_b_source_enstrophy_release_20260907.json。
- manifest SHA256：9f90254f6dcbcce7c6066b4f90d6fae63d797502901ef35014531700f63eae58。
- manifest 大小：41497 B、910 行。

源提交只新增声明的七份文件。
清单包含 7 个当前源、157 个依赖，共 164 个唯一路径；
依赖顺序精确为前序 156 行加前序 40526 B manifest。
主代理与 C 各自核验 164 行工作树/source 原始字节、SHA256 和大小，
并各自核验 157 个依赖与 base 的字节一致。
严格 JSON、嵌套重复键、非自绑定、提交父链、声明路径和空白检查通过。

C 在清单中指出时间量词应明确限制为 \(0<\delta\le L\)。
仅把 “for every delta>0” 改为
“for every 0<delta<=L in the time domain”，增加 22 B；
逆还原精确恢复原 41475 B、
9236c40dcdd853e7d59c8813ce65c2266645fc6c0176c6ec11a1e853d42fe4c2。
源正文与依赖没有改变。C 接受该最小增量，没有重计一轮数学审阅。

C 的验收止于 source 与未提交清单。
其后主代理提交清单，并实际核验上述 freeze 中的清单与工作树 41497 B 逐字节一致；
这一后续 containing-commit 检查不归给 C。
本回执和可变 checkpoint 不在科学清单内，也不自绑定。

## 2. 研究结论和复核范围

BW.1--18 完成条件性的同一原解源项/梯度能量成本审查。
全周期线性测试的压力消去不能移植到非线性或局部截断；
相反黏性、自应变、源项、二阶成本和端点均被保留。
常系数正定二次型的障碍仅限对任意 Hessian 方向的共同耗散，
不是一般 NS 或特定真实轨道的不可能性定理。

在 BP/BU 的正原子假设下，对每个 \(0<\delta\le L\)，
\(\int_0^\delta\|\Delta w\|_2^{4/3}=+\infty\)。
若有限，已有 \(b\in L^4_\rho L^3_x\) 会使 \(w_\rho\in L^1_\rho L^2_x\)，
给出与弱零迹、极限单位范数冲突的强迹。
这排除的是一个额外条件，不是原子本身。
不能由充分上界的右端无限反推 \(\mathcal W_z\) 发散，
也没有得到范数等价或混合功不可控。

主代理为作者，A/B 参与，C 为唯一非作者完整数学审查者。
第五节的实质修订和题头增量、实际来源范围、A 的 scope 验收见 audit。
B 独立 Ruby Rational 25/25、三源/18 标签、156 前序原始行、
5 项限定负控、3 项保护，以及新 6773 B/旧 6524 B 现场复跑一致性通过。
有限 QA 不是连续 PDE、极限、矩阵正定性、文献新颖性或外部同行评审。

Deep Research 技能用于有界第一手来源核查和 provenance 记录；
实际只读所列 v4 设置、定理陈述、Section 4 及另一篇元数据/摘要，
没有云端研究运行、新 PDF 阅读、额外定理导入或周期迁移证明。
没有穷尽性或文献新颖性主张。

## 3. 一次交接

固定接收任务：发布任务，01a06480-0532-7fd0-bdf0-57571465a2d4。
本 release 仅发送一次，包含 release、前序、source、freeze、
清单身份、科学边界和 HTML-only 约束。
发送工具返回 isError=false，响应 threadId 与固定接收任务一致。
调用返回后的时钟为 2026-09-06 17:31:01 UTC。

这只记录交接调用被接受，不表示排队、网页部署或在线验收完成。
没有读取发布任务、发布索引、队列或 CI；没有等待、监督、重试、push 或部署。
无新读者 PDF、第三方 PDF 再分发、仿真、科学图、DGX 或累计 recap。
私有热演化论文、专门修订任务及其未公开授权状态不变。

## 4. 恢复记录与下一项

checkpoint 改为 ClayB-general-centre-clock-dedup-20260907。
保留全部 21 个既有 review 字段的解析值和 private paper 对象，
另加本节审阅字段，共 22 项；历史包含 16 个不重复 release。
AGENTS 的用户工作树保持 4589 B、
80959a5c6d2db01543f8f1ae1ddc2e1ba7430c1b14d1b4ef658dcc965efecfab；
source/base 的已提交 AGENTS 也未改变。

本节没有减少 G 的未证输入，停止自动延伸常二次梯度组合。
下一项回到一般指定中心的 G 量词，
先读 R arbitrary-clock 与 S signed-collar、boundary-mismatch clock、
weighted-Abel 和 one-sided-clock 的相关原文，
判断相邻尺度有符号时钟候选是否已被旧障碍覆盖。
这五项目前只定位；没有新完成的后续推导、证明或完整审阅。
只有确实未测过、且可能减少未付输入的真实 NS 项才进入新计算。
不预设任意奇点都产生正能量原子，不把旧 telescoping 恒等式重新记为强制估计。
G、R.216--R.217、原子生成/排除和一般三维正则性均 OPEN；总目标保持 active。
