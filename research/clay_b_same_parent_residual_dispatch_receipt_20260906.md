# 对齐残差小节：研究冻结与一次交接回执

2026-09-06（UTC）。**RESEARCH COMPLETE / HANDED OFF ONCE / G OPEN / NOT CLAY。**

## 1. 冻结身份

- release_id：ClayB-SameParentResidual-20260906。
- 前序：ClayB-ConvexPressureTrace-20260906。
- 研究仓库：/Users/kasifa/Documents/Math/navier-stokes-r074m。
- base：281d36f1d55254dc13b0bc5c3b5b80ccf94467a0。
- source：9708a86053d507a51b0c3843211774ede954efea。
- 包含 manifest 的 freeze：6da74e5e62930a5b4b44d09962915f7e4e551541。
- manifest：research/clay_b_same_parent_residual_release_20260906.json。
- manifest SHA256：511286836b23b8f3507f09d300709777c264d1be009f44f8475aa208bc91c227。
- manifest 大小：38308 B、837 行。

源提交只新增清单指定的六份科学文件。
清单绑定 6 个当前源和 143 个依赖，共 149 个唯一路径；
依赖的映射和顺序精确等于前序 142 行加前序 manifest。
主代理与 C 分别实际验证全部 149 行工作树/source 原始字节、SHA256 与大小，
并分别验证 143 个依赖与 base 字节相同。
严格 JSON、重复键、非自绑定、交叉引用与提交空白检查通过。

C 的这次验收止于 source 与未提交的清单字节。
之后主代理提交清单，再实际核验上述 freeze 中的清单等于工作树 38308 B。
不把这一稍后的 containing-commit 检查归给 C。
此回执和可变 checkpoint 不在科学清单内，也不自绑定。

## 2. 研究结论和复核范围

BU.1--20 在 BP 的额外正原子及同一原解条件下完成：
无目标原子的残差能量测度、带已付源的正向残差能量、
全局混合张量消失及完整周期混合压力小量。
BU.17 的普通时间 little-o 不给临界速率、联合缩球控制或幅度一致配对。
自压力保留，BT 的半单位贡献尚不能单独归给某个压力分量。
这不证明原子存在或排除、强初迹、G、一般正则性或 Clay 结论。

主代理为作者，A/B 为构造接口参与者，C 为唯一非作者完整数学审查者。
完整审阅及光滑截止、题头的两次字节增量接受见 audit，
不重复计审阅轮次。A 完整接受 reading、report 和 audit 的范围。
B 独立 Ruby Rational 20/20、三源/20 标签、142 前序原始行、
四项真实限定负控、三项保护以及新 5918 B/旧 5442 B 的现场复跑一致性均通过。
有限 QA 不是 PDE 证明或外部同行评审。

## 3. 一次交接

固定接收任务：发布任务，01a06480-0532-7fd0-bdf0-57571465a2d4。
仅发送本 release 的一次消息，包含 release、前序、source、freeze、
manifest 路径/哈希、研究边界及 HTML-only 约束。
发送工具返回 isError=false，响应中的 threadId 与固定接收任务一致。
调用返回后的时钟为 2026-09-06 16:07:11 UTC。

这只记录交接调用被接受，不表示网页已排完队、部署或在线验收。
没有读取发布任务、发布索引、队列或 CI；没有等待、重试、push、部署或代管发布。
无新读者 PDF、第三方 PDF 再分发、仿真、科学图、DGX 或累计 recap。
私有热演化论文和专门修订任务不在此次公开授权内。

## 4. 恢复记录

current checkpoint 改为 ClayB-signed-mixed-pressure-amplitude-20260906。
保留全部 19 个既有 review 字段和解析后的 private paper 对象，
新增本节的审阅记录；研究冻结历史包含 14 个不重复 release。
AGENTS 的用户工作树仍为
80959a5c6d2db01543f8f1ae1ddc2e1ba7430c1b14d1b4ef658dcc965efecfab，
source/base 未改动其已提交版本。

下一项是实际自压力/混合压力分解下的有符号幅度功。
先判断能否从 BU 小量和方程得到不随幅度增长的混合功估计；
即使混合贡献能去掉，自压力也不能略过。
尚无下一项的完成证明或审阅，不把缺失的临界范数、一致可积性或缩球速率视作已付。
研究不等待网站发布；当前总目标保持 active，未解决项仍 OPEN。
