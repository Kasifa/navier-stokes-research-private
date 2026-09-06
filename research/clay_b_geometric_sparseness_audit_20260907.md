# 几何稀疏性筛选：来源与审查记录

2026-09-07（Asia/Shanghai）。内部 ID：ClayB-GeometricSparsenessScreen-20260907。
基准：1fd4f6b37a115e5e03c922686fcddafd6c0812bd。
不是科学发布冻结；一般三维正则性 OPEN / NOT CLAY。

## 1. 本轮范围

本轮完成的是两篇原著的证明接口筛选和 GS.1–7 的静态尺度核验，没有新增真实 NS 动态控制。全文主稿为 research/clay_b_geometric_sparseness_screen_20260907.md。能量给出的已知半径不能直接满足文献的小半径要求；这不是实际最小稀疏半径下界，不是否定全部几何论证，也不是 NS 反例。

筛选前先作本地去重。耗散/决定波数已有定向原著阅读及周期复证，未重新列为新候选。BFG 1704.05546v4 没有本地实读命中；AB 2110.02187v2 在 r074q_problem_freeze.md 只有条件性接口概述，§1.2/§4 与证明此前未被记录为实读。既有 Grujić 几何/调和测度文献记录仍保留，因此不宣称本项目首次接触整个几何机制。

## 2. 根任务的实际原著阅读

只使用两篇新接口的官方 arXiv HTML 与摘要元数据，不扩展第三篇。参考文献中列出的其他工作未被当成本轮已读原著。

| 原著 | 版本与标识 | 实际阅读范围 |
| --- | --- | --- |
| Bradshaw–Farhat–Grujić | arXiv:1704.05546v4，2018-09-07；DOI 10.1007/s00205-018-1314-5 | 定义 1/3、向量范数；§2 Theorem 8 的草图、Theorem 10 的陈述与文内复化说明；§3 定义 12–15、Propositions 17–18 陈述、Theorem 19 及完整文内证明；§4 Lemma 24、Theorem 26 及完整证明、Remarks 25/27/28；引言相关尺度解释和 epilogue 相关段落 |
| Albritton–Bradshaw | arXiv:2110.02187v2，2022-04-05；DOI 10.1088/1361-6544/ac62de | §§1.1–1.2；Lemma 2.1/2.4 及完整证明，频率定义与 Lemma 2.3；§3 的 Proposition 3.1、Theorem 1.2、Corollary 1.3、Theorem 1.4 完整证明；同时读取 §3.2 相关频率结果，但不采用为新候选；§4 完整至结尾，包括 Proposition 4.1 的证明 |

链接：[BFG v4](https://arxiv.org/html/1704.05546v4)，[AB v2](https://arxiv.org/html/2110.02187v2)。这些是有界源接口核读，不是对两篇所有外部解析性、调和测度、局部存在理论及高阶文献的全文认证。未使用第三篇原著或数值图片来补充证明。

BFG HTML 内显示的日期与 arXiv 固定版本元数据不一致；本记录采用官方版本日期，不把 HTML 内动态日期当作修订日期。文内若干显示式也不直接复制为证据，例如 Lemma 24 外壳的带权/无权绝对值中间比较，以及 Theorem 26 证明的参数书写。GS.3–4 独立采用有效的绝对值上界与 curl 测试。这里没有查验原始 PDF/TeX 来区分排印与转换原因，故不宣布原定理被推翻或全文已修复。Theorem 19 的解析性/调和测度基础仍是文献条件接口。

## 3. 独立参与与完整非作者审查

A（r076l_proof_audit）独立作本地去重，检查已有耗散波数、决定波数、间歇维数、涡向几何与稀疏文献台账。它区分原著实际读取、定理范围核对及仅有题名概述，确认当前两篇的具体证明接口未被既有记录覆盖。A 不承担本轮完整主稿审查。

B（r076l_figure_audit）独立阅读 AB §§1.1–1.2、Lemma 2.1/2.4、§3 相关证明和完整 §4；并对照 BFG 的定义、尺度声明与 Theorem 19/26 陈述。B 的结论是给定稀疏性到 NS 范数下降的动态出口有效地仍以该稀疏性为前提；能量输出没有生成所需的小尺度条件。B 未声称 BFG 全证明复核，也未阅读本轮主稿全文。

C（euler_rigidity_screen）为唯一完整非作者主稿审查者，对实际终稿给出 PASS，无剩余阻断项：

- 路径：research/clay_b_geometric_sparseness_screen_20260907.md。
- 接受字节：85 行，6396 B，SHA256 4caebe8af8683e28d59329a96c81ebe67fb8992596f6aa91743126a19cf60dc2。
- C 独立重推 GS.1–7，包括 curl 符号、严格正负区/外壳下界、尺度比较、两种缩放及所有否定边界。
- 三类精度补充是：涡量时间连续空间明确为 \(C([0,T_*);L^\infty)\)，固定文献中的 \(M,c(M)\) 并统一 \(W(\tau)\)，以及正 \(\eta\) 和固定光滑截止剖面。C 逆还原后精确恢复初稿 8e145a406f0e6808fd8ccc96e529c9cddce16f8e27a0f1dbdc85a75b3e45986c（84 行，6177 B），没有其他修改。
- C 另实读 BFG 相关定义、Theorem 19 条件及相关段、Lemma 24 与 Theorem 26 完整证明；AB §1.2、Theorem 1.2/1.4、Lemma 2.1、Proposition 3.1 及 §4 Proposition 4.1 的必要完整论证。
- C 未认证两篇所有外部依赖，亦未声称 BFG 完整解析性—调和测度基础链获本轮重新证明。

完整审查接受的是有限的接口判断和静态核验，不是新颖性、全局正则性或几何路线不可能性。

## 4. 原始记录绑定

下列七份历史来源已逐项与基准提交原始字节比较相同。全文哈希不表示本轮全文重读。

| 路径 | 行 / bytes | SHA256 | 根任务本轮范围 |
| --- | --- | --- | --- |
| research/clay_b_strategy_logic_20260907.md | 152 / 10242 | 6cbebb0d6c9c53a37c68afff02c8f5ebab241413120c3ac9455beeac72625e2e | 全文 |
| research/clay_b_strategy_logic_audit_20260907.md | 83 / 9538 | eff969cde0d44ab93c8b679862defa4636af223a3b363455810e49ff65af094f | 全文 |
| research/clay_b_strategy_logic_checks_20260907.json | 139 / 5237 | 1a14b2d38d44dcd213dff9c6c8d79c6e528cb30e62d98aebcdcdaea265515d61 | 历史原始字节比较，不重新声称其数学认证 |
| research/clay_b_mature_frequency_literature_bridge_20260906.md | 49 / 2934 | ac52fde83f1a441c4933c0c9322e5e937fb4b5073f762eab2c09306b39c337e1 | 全文 |
| research/r074q_problem_freeze.md | 518 / 17181 | 42efa94f5310d8f7ce3cea1896ee1e0a8ddd9bddf5d588f9bb853c8696a1a962 | 445–480 行，AB 及相邻接口范围 |
| research/clay_b_source_enstrophy_release_20260907.json | 910 / 41497 | 9f90254f6dcbcce7c6066b4f90d6fae63d797502901ef35014531700f63eae58 | 仅科学冻结身份/原始字节保护，不检查发布 |
| research/clay_b_source_enstrophy_dispatch_receipt_20260907.md | 93 / 5236 | 19c7b704e0fa94477785878aef48b67c6591ef9adcce9f66c6219c4a03e42425 | 仅一次性交付记录/原始字节保护，不重投递 |

实际只读比较已通过，结果保存为 research/clay_b_geometric_sparseness_checks_20260907.json，绑定接受版本主稿、checkpoint 和上述来源，不绑定本说明或自身以避免自引用。检查只作 UTF-8/LF、标签/公式边界和记录保护比较，不是 PDE 或计算机辅助证明证书；本轮没有数值计算，不新建逐节专用 QA 脚本。

## 5. 状态、发布与后续

本轮保持内部 NO-CANDIDATE，不把静态 curl 核验或论文解释包装成新的研究发布小节。实际逐键比较表明，仅七个当前工作字段变化，另新增 geometric_sparseness_screen_review；此前 28 个 review 原值完整保留，当前为 29 个。private paper、16 个科学发布身份/源提交/冻结提交/一次性交付，以及用户 AGENTS.md 不变。

private paper 按 Python json.dumps(paper, sort_keys=True) 默认序列化（UTF-8，无追加换行）的 SHA256 为 c9755ea86f93575cc96c28ac5b3caa1a059bddec2b58a448d09d9cc54d6431c5；用户 AGENTS.md 为 4589 B，SHA256 80959a5c6d2db01543f8f1ae1ddc2e1ba7430c1b14d1b4ef658dcc965efecfab。没有暂存用户文件。

完整目标仍 active，但一般首次奇点排除的未付输入没有减少。这是有限的文献认识与筛选进展，不是正则性进展。筛选已经结束，没有预先接纳的下一条动态证明路线；不自动追加第三篇或相同机制的高阶/局部常数变体，不重复把本轮审查计作新进展。

没有新科学冻结或交付，不读取发布任务、索引、队列或 CI，不等待、监督、重试、推送、部署或报告发布。只有真正完成的新科学冻结才向固定发布任务交付一次。没有仿真、DGX、科学附图、读者 HTML/PDF 或 Deep Research 云任务。

## 6. 最终记录核对回执

C 对第 1–5 节实际版本（67 行、8126 B，SHA256 6d75bd93b4eeff7080d8625fe62a814e3c0a4d7d53280a83a39d8e70e9727bf2）、checks（112 行、3654 B，3e19e7d0275967b6f154a036d3cd90268793574c6db7ece52c50be70660d43bb）及 checkpoint（177 行、62885 B，ab31fe4fe895973ec5e41dcb2e9bcefb15df966b915b7bd220dc7dad8f4479ca）给出记录层 PASS，无需更正。

C 独立确认九个原始字节绑定（主稿、checkpoint、七份历史源）、七个当前字段变化、第 29 个 review 新增、28 个旧 review 全值和所有受保护对象不变；JSON 无重复键，用户 AGENTS 未暂存。记录检查不另计数学审查轮次。

本节由我依据实际回执追加，只记录事实；不把追加本身算作 C 预先审过的正文。
