# 热边缘英文 HTML 片段独立内容核对

结果：**数学内容清单与交叉引用 PASS；参考文献完整性需修复。** 对象是现有 `/tmp/heat-edge-en-normalized.html`，SHA-256 `5d0b319f6e0b90d1c2def1ce3913bc0e2227e87294e59a181547812b3064df1b`。这是转换中间片段，不是最终网页验收。未调用翻译网络、未改转换器/稿件/网站，未监控任务。

核对基准：`heat-edge-html-contract.json`，冻结准备提交 `9ff88b3455894a2ac27bbcec8ecd669435a58a4f` 的 `arxiv/source/`，以及同次构建的 `arxiv/tmp/build/main.aux`。没有重新审查数学定理。

## 通过项

- 7个正文章节、4个附录、3个小节、6个段落标题：共20个标题，顺序和编号对应契约；附录为A–D，段落标题不再错误编号。
- 36个正式陈述/证明块齐全：4定理、9命题、3引理、2推论、18证明；另5个Remark齐全。定理/命题等共享编号与PDF对应，18个证明均有结束方块。
- **139个显示公式、672个行内数学逐项、按全文顺序独立比较后，零数学差异。** 比较仅移除空白、显示外壳、label/tag，并展开原稿的R/C/N/T/Re/norm/abs/pos/dd等宏；没有把HTML上的data-source-sha256属性当成数学内容已经相同的证据。
- 100个源标签均有HTML目标；零重复id，零失效内部链接。
- 108处交叉引用逐项核对契约及实际LaTeX AUX：命令类型、目标标签、显示数字或括号均正确。没有残留未经处理的ref/eqref数学命令。
- 18处文献引用涵盖全部10个键；Theorem、Lemma、Proposition、DLMF section等行内引用定位文字保留，链接均指向存在的文献条目。
- 1幅三联图，使用已核验的SVG资产；完整图注保留三面板、纵轴单独放大、sigma=0.75有限网格不据此声称收敛、p代表sigma等限定。
- 局限性、Computer and AI assistance、Data and code availability段落存在；非最优误差阶、非真人同行评审、有限检查不证明连续极限、无一般Navier–Stokes正则性结论等关键限定仍在。

## 必须修复：CSL文献输出删除了来源字段

10个文献键存在不等于条目完整。当前作者年份制CSL输出忽略了原BibTeX的note及部分特定URL，导致以下已核验来源信息消失：

| 文献 | 当前缺失 | 冻结稿的必需信息 |
|---|---|---|
| BatahanShehata2014 | Publisher full text链接 | main.bbl中的出版社原文href |
| Erdelyi2017 | arXiv v1链接和版本定位说明 | `https://arxiv.org/abs/1602.02315v1`；Theorem numbers refer to arXiv version 1 |
| HallHo2025 | Article 60 | 卷115的文章编号60，不能只剩卷号 |
| DLMF | 所引章节和访问日期 | Sections 8.4, 16.2, 16.11 and 18.5；accessed 6 September 2026 |
| Paris2018 | 明确版本/日期 | Version 2, 14 October 2018（URL里的v2尚在） |
| Paris2021 | 明确版本/日期/首发年 | Version 2, 25 April 2021；first submitted 2020（URL里的v2尚在） |
| Zhang2026 | 版本限定URL、日期和preprint | `https://arxiv.org/abs/2607.10501v1`；Version 1, 11 July 2026; preprint。目前改成版本无关DOI |

其中Erdelyi/Zhang正文使用特定版本的定理编号，故版本链接丢失影响可复核性；Hall–Ho文章编号丢失影响书目识别。这不是最终导航或包装问题。

建议直接由冻结 `main.bbl` 生成完整条目，或显式保留上述note/版本URL；正文的文献键到条目映射保持不变。不要补猜测的出版信息。

## 引用样式说明

正文文献引用已从PDF的[1]–[10]改为作者年份制，文末也没有原数字编号。**这本身是样式变化，不是数学引用目标或定理编号错误**；但网页与PDF的读者互查会更困难。建议恢复冻结稿的10项编号及对应正文引用，并保留已有Theorem/Lemma等定位。若决定保留作者年份制，也必须修复上述实际元数据丢失。

## 仅留给最终包装/渲染验收

片段从MSC/关键词和引言开始；标题、作者/ORCID、摘要、PDF/源码下载、anc入口、站点导航、语言切换等可以由最终页面外壳提供，本次不据此报缺陷。辅助材料说明目前有`anc/README.md`文字，最终应有可用源码ZIP或直接辅助入口。

公式目前仍是MathJax待渲染TeX，编号徽标与公式同处显示块。这里确认的是数学源内容和数字正确；不宣称长公式在移动端、行对齐、编号位置、明暗主题、双语页面或实际线上内容已经通过。所有139公式和编号的最终渲染仍需浏览器检查。
