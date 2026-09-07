# GD 实际证明与范围审查

2026-09-08，北京时间。PRIVATE_CORE。PASS IN STATED SCOPE / CONDITIONAL CONTINUATION / OPEN / NOT CLAY。

## 实际主稿与审读身份

主稿为 research/clay_b_gradient_rank_one_defect_20260908.md，218 行、11939 bytes，SHA256 78cdf5afa278894aa74cecc0cfd707bfba6b2148b1383c5cad8e5fa978c21b1a。

A、C 均完整读取实际主稿并确认最终哈希。C 首读 11798-byte 版本后，实际核对三行修改并逆还原其哈希；A 也接受三处最终增量。修改仅为定义 \(\xi_A\)、明确周期测试 M，以及规定 \(\chi\) 紧支撑于 P 光滑开区。主任务全文读回主稿并逐项独立复算；最终三处文字另外核对。

两位审读者均参与了本轮模块推导或去重，不能记为完全非作者独立审稿，更不是真人同行评审。模块复算、全文实读和最终增量核对是不同范围，不重复计作多次独立审核。

## 核验内容

- GD.3–5：完整速度梯度满足 \(LA=-A^2-H\)。九维 Frobenius 熵、受控源项、初始梯度费用、唯一非负零集余测度及端点排除均成立。联合界只在每个固定 T 上书写；分别取上确界不额外获得一个和的同常数界。
- GD.6–9：逐行无旋给精确退化径向恒等式。距离函数 1-Lipschitz，不需可微奇异向量。F 的非零阈值避开 Q=0，全域 H1 由强 L2／弱梯度极限得到。只控制 \(d/\sqrt Q\)，不控制整个 \(\sqrt Q\)，不宣称时间 BV。
- GD.10：最佳秩一矩阵未必迹零；\(|\operatorname{tr}M|\le\sqrt3d\) 已保留。两种 d/Q 情况均推出四倍 d 的向量与标量伸长界。Q=0、涡量零点均单独处理。
- GD.11–14：时间指数 \(2r/(2r-3)\)、黏性指数 \(-3/(2r-3)\)、周期涡量零均值、Gronwall 与标准 H1 延拓正确。\(r=\infty\) 单列，未包含无小性 \(r=3/2\) 端点。GD.14 的 \(\theta=0\) 按时间指数无穷解释。
- GD.15：代数矩阵的 d、Q、涡量与伸长均精确；只否定一个普遍点态二次替换，不当成实际周期 NS 反例。
- GD.16：cofactor 原函数的指标、系数、分部积分号、周期测试及合法截断正确。速度商和谱切换成本尚未支付，不算临界增益。

## 本地去重和外部来源

主任务全文读取 SC、SG；A 定点读取 SC.3、孤立谱线预算、SG.11–12、PGR.5、R0.69I 的权重部分并查找相应关键词。此前固定谱轴、标量权 Piola 和协方差秩一结果不是本稿完整梯度到秩一集合的距离接口。搜索未命中不等于原创性证明。C 全文读取 SC 及 SG 所需预算、零集和插值段。

本轮普通网页查询为“Navier Stokes regularity criterion second singular value velocity gradient matrix rank one”及“Navier Stokes gradient direction normalized gradient rank one curl entropy estimates”。没有开展全面 Deep Research 或新颖性认证，也没有采用搜索中其他论文或网帖的结论。

唯一打开的外部论文是 [Cao–Titi，arXiv:1005.4463v1](https://arxiv.org/html/1005.4463v1)，2010-05-25，Global regularity criterion for the 3D Navier–Stokes equations involving one entry of the velocity gradient tensor。主任务实际读取导言、周期说明、强解类别及 Theorem 1 证明中最大存在区间／H1 重启逻辑的片段；C 另定向核对相同接口。没有全文审读其单分量定理证明，也不将其假设移植给 d。GD 的主要不等式在本稿直接证明；标准局部强解理论是明确的外部输入，不作本轮新结果。

SE 的固定周期 Hardy 压力证明及 SG 的完整矩阵链式法则按冻结来源继承，未在本轮重审全部调和分析原著。完整来源绑定见冻结清单。

## 结构验收与完成边界

已执行 GD.1–16 唯一顺序标签、22 对展示公式定界符、行内定界符及隐私标签检查。它们不证明数学。主任务另读回最终全文和检查点 JSON，并核验三项冻结本地依赖，共 42280 bytes。源码文件的不可变提交、字节和 SHA256 将在交接前核验并记入冻结清单，不由本记录预先宣称完成。纯解析工作，没有数值证书、PDE 仿真、DGX、科学附图或第三方 PDF；没有视觉渲染或读者 HTML/PDF 验收，不能把这些未运行的项目写作通过。

正面完成项是无对数偏离空间预算和逐点伸长耗竭。d 的临界范数仍未得到；没有任意初值正则性、奇点构造、新颖性或 Clay 结论。完成本节不触发大里程碑复盘。

下一步只研究同一 d 的实际 NS 动力学和 GD.11 的时间缺口。先对 cofactor 旧代数去重，再保留压力、黏性乘积、归一化分母、零集与重奇异值。不能预设秩一类不变，或把未付量改名算作增益。研究获准运行；固定发布任务仅接收一次 PRIVATE_ARCHIVE，研究不执行或监督归档／发布，也不请求公开概要、计数、附件或读者版。
