# 逐项回应新颖性尽调与任务书

日期：2026-09-06。基线：0a212f4e140e0c9875e740cb8ee23be32a5c05dd。

| 要求 | 已落实的具体修改 | 证据 |
|---|---|---|
| P1.1 压缩并归因已有空间结果 | 删除主稿长半平面重证；引用 Zhang v1 Thm 1.1/Prop 4.2；经典见证移入短附录；正幅度与任意相位不排除抵消已写明 | sections/upper-bound.tex、sharpness.tex；auxiliary-cross-audit.md |
| P1.2 时间上界文献化 | Theorem 3.1 + Lemma 12.5 导出；只要 Re ζ≥1；初始窗36N；给C* | sections/time-weighted.tex；time-cross-audit.md |
| P1.3 显式阶最优构造 | ε=N^-2；exact N nonzero coefficients；rates [1,5/4]；T=N；N1；单位质量归一化；下界1/128 | 同上；revision-algebra.json |
| P1.4 Galilean/完整区域/完整速度 | 独立章节完整证明原幅度速率 -9/20000；引言直说固定窗口；另证幅度重缩放边界，避免错误普适解释 | sections/frame-and-mass.tex；application-audit.md |
| P1.5 重写主线 | 改题；摘要和引言先呈现双尺度定量定理及固定初值完整时间实现；贡献与结论重定位 | main.tex；discussion.tex |
| P2.A 可核查误差界 | 振幅 O(ε+logμ/μ²)；位移比值 O(|Δc|(√ε+√logμ/μ))；显式常数、阈值、两负尾导数 | sections/quantitative-edge.tex；quantitative-cross-audit.md |
| P2.B 轮廓命题/有限推广 | 全局包络+局部下界抽象命题；T_n 和 U_(n-1)/n；反例说明不归一化的共同振幅问题 | 同上；research/quantitative-edge.md |
| 先查终止超几何/热边缘原文 | DLMF参数范围；Hile–Stanoyevitch；两类操作表示；Paris两篇相关渐近；4F2精确系数与0F2模型差别 | literature/novelty-update.md、search-log.md、source-metadata.json |
| 常数边界 | 20√2改12√2，充分κ阈值扩大5/3归因于文献输入替换；-2/11907归因外加权重 | upper-bound.tex、consequences.tex |
| 动态匹配有界探索 | 保持单初值、完整时间、全平台与代数项；未证匹配普适上界，明确OPEN | research/bounded-routes.md；discussion.tex |
| 无巨大漂移有界探索 | 同形有界漂移商趋零，包含任意幅度；B=0零通量；不排除其他轮廓 | frame-and-mass.tex、bounded-routes.md |
| 原始科学源和旧稿保护 | 阅读冻结J/K/L；v1字节不变；独立codex分支与工作树；不碰根仓库/主线索引 | provenance.md；source-manifest.json |
| 证据与交付 | 英文LaTeX、中文说明/完整新增证明、逐项回应、代码、原图归档、独立审计、清单与冻结commit | README.md；audits/final-audit.md；output/release-receipt.json |

本次实质修正中，独立审计发现并已解决两处表述作用域问题：Markov 文献输入应显式限定实频率；系数引理“恰好n+1频率”的断言应显式继承 real-rooted 条件。它们不是被数值掩盖的证明缺口。中文证明中的公式转录与源码排版也纳入文件质量检查。

未主张：最优误差阶、终止超几何文献的穷尽排重、全通量q^7最优、整数平方衰减率时间类最优、真实临界相变、任意Jacobi推广、统一初始能量、一般NS正则性、真人同行评审或发表接受。
