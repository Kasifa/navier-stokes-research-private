# 梯度纪录之后的路线筛选：内部来源与判断

2026-09-08。对象：本人及后续数学复核。私有研究源记录，不是读者网页或论文。
本次按已获授权的 Deep Research 流程在当前任务完成有界原文筛选；没有后台研究任务。
目的：找能约束同一周期 NS 来源的非零仿射极限，或绕开 GRC 时间紧性缺项的输入。
固定正黏性、正龄、任意原初值；不额外假设对称性、临界范数、加权尾或无限未来。

## 结论

新核查的三个文献接口均保留未能从当前原解推出的条件，不作为新的已证输入。
本地能量 Euler 核算取得有限推进：纪录选择给局部梯度帽、含顶端的速度紧性，
以及正比率／零比率二分。证明只写在
[科学记录](../clay_b_gradient_record_energy_euler_20260908.md)，这里不重复。
这个二分尚不能排除 NS 奇点；不宣称查新穷尽或方法不可能。

## 文献判断与唯一来源台账

以下文献均于 2026-09-08 实际访问指定作者版本。定理条件由原文支持，
“不能由 GRC/GPH 直接使用”是与本地已证范围比较后的判断。

| 来源、版本及日期 | 所支持的命题与限制 | 实际访问与复核范围 |
|---|---|---|
| Xinghong Pan、Zijin Li，*Liouville theorem of axially symmetric Navier-Stokes equations with growing velocity at infinity*，[arXiv v2，2019-09-04](https://arxiv.org/html/1908.11591v2) | Theorem 1.1 要求光滑轴对称无旋古老解、全古老域一致的抛物型增长 (1.6)，即速度分量绝对值之和不超过 C(√−t+空间距离)^α、α<1，以及 (1.7) 相对轴值的径向 Lipschitz 界，结论仅空间常量。当前缺对称性与该增长条件。证明 (2.29) 的衰减在 α=1 时消失；不是有限能量周期来源定理。 | B 读陈述、§2 全证明及线性例说明；主代理读 Theorem 1.1、(1.6)--(1.7)、§2 至 (2.30) 及调和结尾。原文 (2.14) 的半径幂和 (2.15) 后引用号存在排印风险，未照抄。 |
| Zhen Lei、Qi S. Zhang、Na Zhao，*Improved Liouville theorems for axially symmetric Navier-Stokes equations*，[arXiv v1，2017-01-03](https://arxiv.org/html/1701.00868v1) | Theorem 1.2 要求光滑 ancient mild、轴对称无旋及涡量比值的全负时刻一致远轴衰减；先得调和，再以额外一致次线性得空间常量。GRC 未给 mild 类或次线性，不能借用该文平移强紧性。 | B 读定义、Theorems 1.1--1.3、§2.3、§4；主代理核定义、Theorem 1.2 及 §4 主证明。未认证其所有上游紧性或有旋证明。 |
| Alex Encinas-Bartos、George Haller，*Vorticity Alignment with Lyapunov Vectors and Rate-of-Strain Eigenvectors*，[arXiv v1，2023-10-26](https://arxiv.org/html/2310.17267v1) | Theorem 2 使用全轨道有界涡量、初始应变单谱与 (38) 的应变振幅界；该界不是时间 BV。证明还用含黏性项的全时源上界，取双向无限时间极限。有效对齐需要归一化指数加权轨迹积分小。无外力不删除黏性或应变项，故不提供当前平均应变的时间模量。 | A 读 §2--3、§4 定理相关部分、§5 和附录 A；主代理核 §5 的 (38)--(51)、Theorem 2 及附录 (68)--(78) 的源上界使用。未审数值实验或期刊版全部修改。 |

主代理原文核验是上述指定陈述和证明环节，不冒称三篇全文及全部依赖已独立认证。
不从原文未完整核查的细节推出其他新命题。未复制其线性例子作为本项目新反例。

## 本地去重和缺口表

主代理完整读 BL（268 行）、BM（125 行）、BN、BO 以及两份相关旧原文阅读记录。
GRC/GPH 与恢复索引哈希匹配；本次沿用其已审范围，没有将重复核对计新成果。
A 定向读 R0.70M、R0.71H、R0.70J、R0.71N 的相关旧方向/形变记录；
B 回读 GRC 仿射段和 GPH 准入段；C 定向读 BL/BM/BJ 并独立核算尺度。

| 候选问题 | 本轮证据 | 尚缺证据／决定 |
|---|---|---|
| 增长型古老解刚性 | 上述两篇严格次线性、轴对称结论 | 当前没有这些结构；不扩搜同义线性例子 |
| 真实涡量轨迹对齐 | 上述轨迹定理及实际积分项 | 双向历史和黏性／应变积分未控；不将表示式当估计 |
| 能量尺度绕过压力时间项 | GRE 的闭顶端紧性及比率二分 | 非退化梯度或原子排除仍缺；本次精确测试完成 |
| 已有能量测度无原子工具 | BN 的附加强端点、BO 的趋零耗散成本 | 旧稿已记录 Leslie--Shvydkoy、Shvydkoy 原文范围，本轮不重称新发现 |

## 检索与停止理由

主代理第一批三条 arXiv 定向查询使用 NS 与 Euler limit／energy concentration、
affine／blow-up／ancient、Type II／gradient／Euler 组合，命中多为无关材料。
第二批三条查询为：

1. `Navier Stokes Euler rescaling blowup energy concentration Chae Shvydkoy`
2. `Navier Stokes blowup affine strain ancient solutions linear growth`
3. `Navier Stokes 2025 2026 regularity gradient geometric depletion finite energy`

结果中的能量测度、线性增长流、修改模型与旧稿重复或不适用；摘要仅作定位。
B 的三条查询：

1. `Navier Stokes ancient solutions sublinear growth velocity Liouville 3D 2010 2026`
2. `Navier Stokes ancient solutions linear growth affine Liouville bounded gradient periodic blow up limit`
3. `"ancient" "Navier-Stokes" "sublinear" -site:reddit.com -stationary -steady`

A 的三条查询：

1. `Navier Stokes "Lagrangian" "deformation" "regularity" pressure Hessian`
2. `Navier Stokes vorticity direction evolution estimates Lagrangian alignment dynamics 2025 2026`
3. `"Vorticity alignment with Lyapunov vectors and rate-of-strain eigenvectors"`

合并首轮证据后只回读上述原文与旧稿，不再作泛检索。每个重要候选已明确适用条件
和当前缺项，继续扩搜相邻词预计只会重复；这是有界停止理由，不是不存在定理。
未采用搜索结果中的未经核实全局正则性宣称或修改方程模型作为原 NS 证据。

计划按发现、定向核验、实际核算、保存验证四阶段执行。当前没有可调用的
`update_plan` 工具，计划保存在当前会话记录；不声称调用过不存在的工具。
材料只作私有 Markdown 科学记录与来源台账；不生成网页、PDF、译文、仿真或发布。
交付只承诺完成结构、链接和数学范围复核；未做浏览器视觉验收。
