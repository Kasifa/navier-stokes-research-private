# PGR：来源、独立审查与有限复算范围

2026-09-07（Asia/Shanghai）。基准提交 454ace62fd12a720c411230649331c6364d864f0。内部来源接口关闭记录，不是科学 release、外部同行评议或发布回执。

## 1. 本轮问题与去重

前一轮 MSD 已有解析结果、独立审查、有限复算及本地提交，属于完成了具体检查的进展，而非状态复述。本轮按照其停止条件，不再重做谱偏离单调性、两频热剪切 energy-only 费用或 HN 修正能量调参。实际检查完整原 NS 的高阶应变余项，并跟进一条来源明确的全域压力四次关系；G 与一般正则性的已证范围没有增加。

A 定向检索并读取最近邻：R0.70X §4 只消去 omega tensor omega；R0.70A §5/§11 已有低阶生产的压力-Hessian/黏性与时间修正账本；R0.69I 的局部化留下同尺度边界；R0.70L §10.6 的 deformation pullback 要付累计应变。没有在所检索源中找到完整 M=Gram(partial S)+2 sum(partial S)^2 公式。该有限仓内去重不是领域新颖性证书。

根任务实际全文读当前 MSD 主稿、clay_b_strategy_logic、vorticity_stretching_sign_structure（R0.69P）和 vorticity_direction_budget；读取 R0.70X 225–295行的完整零恒等式证明、HN 100–165行含HN.9–11、R0.70A 290–390行、R0.69H pressure_hessian_pointwise_obstruction 的1–300行、R0.69I localized_strain_pressure_commutator 的1–100行、R0.70L 690–790行含完整10.6及其费用。历史来源没有被改写，点态压力反例没有被误当作全域有符号压力关系的反例。

针对 Carbone–Wilczek 的精确 arXiv ID 2112.12820、DOI 10.1017/jfm.2022.680、标题，以及 Piola/cofactor/adjugate 的有限文本检索没有命中此前对应推导；命中的其它 Carbone/Wilczek 文献是不同文章。没有把该有限去重扩展为全领域首创判断。

## 2. 主要原著及使用边界

Miller, *On the interaction of strain and vorticity for solutions of the Navier–Stokes equation*, [arXiv:2407.02691v2](https://arxiv.org/html/2407.02691v2)，官方 v2 日期2026-04-13。根任务本轮重读引言相关陈述、第5节完整 Theorem 5.3/5.4 及证明与邻近模型接口；B 读取必要定义、第3节证明、第5–6节。第5节的 residual norm/ratio 比较是条件估计，第6节谱偏离机制已在 MSD 核验。本轮没有重证模型局部存在性全依赖，也没有声称出版版逐字认证。

Carbone–Wilczek, *Only two Betchov homogeneity constraints exist for isotropic turbulence*, JFM 948 (2022), R2, [出版社正文与 DOI](https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/article/only-two-betchov-homogeneity-constraints-exist-for-isotropic-turbulence/B7E010E18EEE8B1B0646E28DB86A4398)。出版社列 online date 2022-09-20、卷期日2022-10-10；没有把搜索索引的近期抓取日期当作论文日期。根任务读引言相关段、第3节尾段、第4节显示推导、第5节全文及第7节结论；没有独立复算其81方程分类系统或读全所有附录。B 独立读取第5节及所需范围。本文只借其第5节关系定位来源，并在固定周期域直接重证 PGR.5–9；不依赖其统计各向同性完整性分类。

CW 的分类对象是单点速度梯度标量的统计齐次/各向同性约束，不能外推成包含 grad A、非局部或时间相关结构的全分类。压力平方项的符号是真实恒等式，但完整 Betchov 动态预算中的同量惯性项符号相反、系数相同。本文只确认这一零和拆分，不声称所有压力方法或高阶恒等式已被排除。

本轮为普通原著核读与解析检验，没有使用 Deep Research 工作流、PDF 阅读、外部同行评议、模型全依赖或独立新颖性认证。

## 3. 解析结果与贡献角色

根任务直接推导 PGR.1–3，A/B 独立取得相同的 M 公式。M 半正定、trace M=3|gradS|²，只消去与 S 配对的各向同性部分；常规上界仍需未付的累计应变。B 用既有 HN 场确认 I/V=12,J/V=0；该场是旧的兼容初值，不是新流型或 NS 爆破。

根任务从 CW 第5节的来源关系直接重推 Piola 列散度、任意周期 w 的积分恒等式及 PGR.6，再由非对称迹零矩阵的 Cayley–Hamilton 得到 PGR.7。代入同一条原 NS 梯度方程得到 PGR.9 的精确零和。B 独立核验这些指标、压力符号、黏性零项及四次系数。A/B 因此是本轮局部贡献者，不计为完整非作者数学审查者。

## 4. 有限计算及一次检测范围修正

根任务执行只读内联 Python Fraction 的完整有限 Fourier 多项式运算。两个指定实无散场各15项检查，加HN值12的一项检查，共31个指定检查实例；无空间/时间数值积分、DNS、模态截断演化或随机抽样。代码将在 checks 中逐字归档，可独立重放。

样本一是 HN 的六模态场：I/V=12,J/V=0，mean(q²)=384，mean tr(A²H)=-192，mean tr(A⁴)=192。样本二是 checks 指定的全三维八模态场：I/V=24,J/V=60，mean(q²)=608，mean tr(A²H)=-304，mean tr(A⁴)=304。两场都保留所有卷积输出；这些有限结果不证明任意场的指标恒等式、PDE 延拓或累计估计，后者分别依赖正文解析证明或继续保持 OPEN。

首轮预设的“Piola 散度方向互换”负对照在平面 HN 样本上未能检测：该样本的 cofactor 特殊形状使两个方向都无散。这是对照样本的退化，不是数学恒等式失败。没有将这个 false 伪装成 PASS：最终输出明确保留 HN_orientation_swap_detected=false，并只在确能区分方向的三维样本上要求该负对照通过。

最终有5种指定错误机制、7个有效负对照实例：反转压力符号与错写各向同性迹系数各在两场检查；散度方向互换在三维场检查；漏输运在HN场检查；漏2K系数在三维场检查。两次最终完整输出逐字相同。它们是代数错误检测，不是PDE求解器的突变测试，也不代表31项/7对照全部有第二实现认证。

B 独立使用系统 Ruby 2.6.10 的 Rational/Complex，从题面八个正负模态重新枚举全部有序卷积，未读取或导入根任务 PGR 检查源或主稿；精确复得三维场 mean(q²)=608、mean tr(A²H)=-304、I/V=24、J/V=60、I+J=84。正确 Piola 列散度的归一化平方均值为0，故意交换指标后为1216；根任务随后在归档 Python 输出中也复得这两个值。该独立范围只覆盖列明的有限量及一项定向负对照，不升级为全部31项/7对照双实现认证。

## 5. 完整非作者审查

C 是本轮唯一完整非作者数学审查者，已全文独立重推 PGR.1–9，PASS，无阻断或修改。接受实际主稿145行8401B，SHA256 9b57c0228517efb0653b7be41dbb39ff98de6f3e9607ecc037a52b2e91114813。确认高阶能量1/2因子、M/traceM、HN值12V及初始配对边界、Piola列散度与任意周期w、非对称迹零矩阵CH、同解四次零和。根任务也从磁盘全文核读主稿。

C 实际读取新稿全文、HN.9–11、R0.70X第4节完整零恒等式证明、Miller v2第5节完整余项/高阶能量/比较判据证明接口，以及CW出版版第5节与第7节结论范围。没有认证CW全部张量分类或Miller模型存在性依赖；本轮只计一次完整非作者数学审查，不是有限计算、外部同行评议或新颖性认证。

## 6. 状态与停止条件

基准 checkpoint 的36个既有 review 字段、私人论文对象和17个科学 release/source/freeze/once-only 身份必须逐值保留；本轮仅追加一个内部 review。最近真实科学冻结仍为已交接一次的 FA，不重发。用户 AGENTS 的预存未暂存修改保持 SHA256 80959a5c6d2db01543f8f1ae1ddc2e1ba7430c1b14d1b4ef658dcc965efecfab。

另纠正 checkpoint 中仍指向 FCB 的旧 current_internal_work 定位信息：先把原对象逐值保留到 historical_internal_work_records，再把当前对象更新为已审查的 PGR。该定位修正不改历史数学结论、review 字段、科学发布身份或私人论文状态。

研究角色的当前源、下一步与必要指针在自然检查点更新，随后 refresh 并验证；刷新不替代审查。只提交本轮研究记录，不推送、部署、查看或维护发布任务/索引/队列/CI。没有新科学 release、发布交接、仿真、DGX、科学附图、读者HTML/PDF或累计recap。

收尾期间协议连续更新。根任务先读中间版本 4feaae1a，再全文读取迁移须先认可的更正版 389b3fa1；最终又全文读取增加逐篇确认白名单的现行版本（135行12804B，SHA256 e1210c07b55c429a35a10eab1b56e574eff840e5e3b3e42c7d56cdc578424aab）。最新规则覆盖此前迁移执行措辞：私有科研源与公开纯产物 Pages 目前仅为待用户认可的方案，没有迁移实施授权。“前沿成果 / Frontier Results”栏目执行单篇用户确认白名单；研究完成、冻结审计或 arXiv 格式准备均不自动取得公开授权，本任务不核验或扩大该白名单。本轮不检查迁移、旧远端或发布状态，不改 remote、凭据或部署配置，不等待、不 push，也不重复论文交接。保留的 paper 对象是历史科研登记，不作为当前网站公开授权的判断；恢复索引在内容审阅后绑定现行协议哈希。

完成本次来源接口后，停止把 Miller/CW 运动学正交、残余范数优化或零和压力四次项当作自动闭合。不得把未知累计应变或终端高阶范数换名后循环开节。目标仍是一般三维原 NS；尚未接受下一项无条件动态控制候选，G、R216–R217、一般终端缺口与一般正则性仍 OPEN / NOT CLAY。

用户随后要求先做策略优化，并在完成手头工作后暂停。本包只完成既有 PGR 审查、记录与本地提交，暂停状态同步写入 checkpoint 和研究恢复索引；不启动下一候选、不自动调整研究路线。后续先与用户讨论策略，再按新的明确指示恢复。
