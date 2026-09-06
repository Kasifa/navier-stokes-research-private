# 有符号混合压力功：研究冻结与一次交接回执

2026-09-07（本地日期）。**RESEARCH COMPLETE / HANDED OFF ONCE / G OPEN / NOT CLAY。**

## 1. 冻结身份

- release_id：ClayB-SignedMixedPressure-20260907。
- 前序：ClayB-SameParentResidual-20260906。
- 研究仓库：/Users/kasifa/Documents/Math/navier-stokes-r074m。
- base：ecc17ffc95f3399f0cca1289f4b1787c1bdba3a1。
- source：cb5acbb4416ca2d6502e9b7d48d19f91a150f2a0。
- 包含 manifest 的 freeze：cf4f8a27bc1ddab92f857945b229a24fb05d5517。
- manifest：research/clay_b_signed_mixed_pressure_release_20260907.json。
- manifest SHA256：b4d5090a3e365a0f298f2b8f9bd46db7f00a90d3c23e2507e79d3b72b9bceaa5。
- manifest 大小：40526 B、873 行。

源提交只新增清单指定的六份科学文件。
清单绑定 6 个当前源和 150 个依赖，共 156 个唯一路径；
依赖的映射和顺序精确等于前序 149 行加前序 manifest。
主代理与 C 分别实际核验全部 156 行工作树/source 原始字节、SHA256 与大小，
并分别核验 150 个依赖与 base 字节相同。
严格 JSON、重复键、非自绑定、提交父链和声明路径检查通过。
主代理另执行 source 提交及清单提交的空白检查。

C 的本次验收止于 source 与未提交清单的字节。
之后主代理提交清单，再实际核验上述 freeze 中的清单等于工作树 40526 B。
不把这一稍后的 containing-commit 检查归给 C。
此回执和可变 checkpoint 不在科学清单内，也不自绑定。

## 2. 研究结论和复核范围

BV.1--23 在 BP/BU 的额外正原子及同一原解条件下完成：
混合压力功的不依赖幅度的逐时上界、两个不同的充分时间控制接口，
以及联合截断的合法恒等式和有符号压力原函数极限。
加权时间成本和混合压力平方都尚未支付；
有符号原函数消失不能代替 \(L^1\)、全变差或一致可积性。
三个压力余量仍在；即使将来混合功消失，自压力及条件性半单位端点仍在。
累计耗散趋零不等于残差加权耗散控制。
本节不是原子生成或排除、G 闭合、一般正则性、新颖性或 Clay 结论。

主代理为作者，A/B 参与构造接口，C 是唯一非作者完整数学审查者。
完整审阅及措辞、题头两次字节增量接受见 audit，不重复计完整审阅轮次。
A 完整接受 reading、report 和 audit 的实际范围。
B 独立 Ruby Rational 25/25、三源/23 标签、149 前序原始行、
四项真实限定负控、三项保护以及新 6524 B/旧 5918 B 现场复跑一致性通过。
有限 QA 不替代连续数学；内部模型审查不是外部同行评审。
外部原著仅核 Berselli--Chiodaroli v3 元数据/摘要；
没有新 PDF 或外部定理证明重审。静态缩放脉冲未被采用，BV.8 仅是非 NS 标量例。

## 3. 一次交接

固定接收任务：发布任务，01a06480-0532-7fd0-bdf0-57571465a2d4。
仅发送本 release 的一次消息，包含 release、前序、source、freeze、
manifest 路径/哈希、研究边界和 HTML-only 约束。
发送工具返回 isError=false，响应中的 threadId 与固定接收任务一致。
调用返回后的时钟为 2026-09-06 16:52:38 UTC。

这只记录交接调用被接受，不表示网页已排完队、部署或在线验收。
没有读取发布任务、发布索引、队列或 CI；没有等待、重试、push、部署或代管发布。
无新读者 PDF、第三方 PDF 再分发、仿真、科学图、DGX 或累计 recap。
私有热演化论文和专门修订任务不在此次公开授权内。

## 4. 恢复记录与下一项

current checkpoint 改为 ClayB-source-enstrophy-cost-20260907。
保留全部 20 个既有 review 字段和解析后的 private paper 对象，
新增本节审阅记录；研究冻结历史包含 15 个不重复 release。
AGENTS 的用户工作树保持
80959a5c6d2db01543f8f1ae1ddc2e1ba7430c1b14d1b4ef658dcc965efecfab；
source/base 未改动其已提交版本。

下一项直接检查实际原解、残差的源项与梯度能量演化。
主代理随后完整读取了已有 BQ 二阶成本、BR 算子预算强度及其合并报告，
用于比较下一计划；没有把阅读旧稿计作新推导或完成的小节。
尤其不能把对所有初态的二阶预算有限，改名当作已经更弱的研究出口。
下一项尚无新完成的推导、闭合证明或独立审阅。
任何二阶、临界或加权时间输入都必须单独核算；
充分成本不能写成必要性，自压力不能在混合项控制后被略过。
研究不等待网站发布；当前总目标保持 active，未解决项保持 OPEN。
