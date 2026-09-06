# arXiv 投稿准备

论文：**Heat-evolved Chebyshev edges and localized fluxes of sparse Fourier shears**。作者沿用 **C. K. Zeng**，ORCID **0009-0002-5402-3374**。

本目录是从研究冻结提交 `ee014e3d8d332282b6e708aaa73dec23ed275b69` 制作的独立投稿稿。原 v2 和此前导出的 PDF 保持原样。本次完成的是本地内容整理与技术预检，未登录、上传或提交 arXiv。

## 交付文件

- `output/heat-edge-arxiv-source.zip`：拟上传 arXiv 的源码包。解压根目录有 `main.tex`、10 个章节、`references.bib`、`main.bbl`、实际使用的矢量图，以及 `anc/` 中的数据和代码。不要将整个本目录作为上传包。
- `output/Heat-evolved-Chebyshev-edges-arxiv.pdf`：从投稿源码编译的 25 页预览。
- `metadata.txt`：可直接粘贴到投稿网页的字段；`abstract.txt` 是单独摘要。
- `metadata.json`：同一组结构化元数据。主类建议 `math.CA`，交叉类建议 `math.AP`；这是依据论文重点作出的编辑判断。
- `source-manifest.json`、`audits/`：文件哈希、编辑差异、数学内容保留检查及编译验证。它们不混入投稿 ZIP。

## 内容整理

保留题名、作者、全部数学假设、定理、证明、图和结论边界。摘要明确序列的每个成员各用一份初始数据，正文补明 `D=d/dx`。内部版本历史、未公开审计指针及过时的 PDF/提交状态说明移至本地记录。正文以独立论文的方式说明数据与代码。AI 协助声明及作者责任保留。

参考文献保留已核验的十条来源；增加 Erdelyi 原始 arXiv 版本链接，正确标示 Hall--Ho 的文章编号，统一 DOI 链接。没有添加未经验证的期刊录用信息、本文 DOI 或 arXiv 编号。

## 编译和验证

推荐投稿时选择 `main.tex`、`pdflatex`、TeX Live 2025。本机用 TeX Live 2025 最终仓库版本、pdfTeX 1.40.28 和 BibTeX 0.99d 实际构建；它并非 arXiv 的 2025-08-03 精确软件快照，因此本地通过不等同于 arXiv 服务器验收。[官方编译环境](https://info.arxiv.org/help/faq/texlive.html)

```sh
sh build.sh
python3 checks/validate_submission.py
```

`build.sh` 接受 `PAPER_PDFLATEX` 和 `PAPER_BIBTEX` 指定可执行文件。脚本禁用 shell escape，文中 PDF 图直接引用，不依赖即时格式转换。日志里预期出现一条 epstopdf 的 shell-escape-disabled 提示；这不影响本稿。参考文献、缺字、未解析引用和溢出另行检查。

`prepare_source.py` 是从冻结 v2 重建投稿稿的编辑脚本；若运行它，随后必须重新构建、校验和打包，以保持 BBL、元数据和 PDF 一致。

## 作者实际提交时

1. 用作者自己的账户建立新投稿；若此前已有同一论文的 arXiv 记录，应使用其替换版本流程。本地内部 v2 不自动意味着 arXiv v2。
2. 上传 `heat-edge-arxiv-source.zip`，选择上述主文件和引擎，粘贴 `metadata.txt`。本文未发表，Journal-ref、DOI 和 Report-no 留空。
3. 在账户中完成所需 endorsement，并由作者选择本版本的许可证。本准备包没有代选许可证，也没有添加版权转让声明。
4. 查看 arXiv 实际生成的 PDF，检查标题、作者、25 页内容、图、公式和链接，然后由作者决定是否最终提交。

arXiv 要求作者自提交并检查平台生成的 PDF；许可证授权不可撤销。相关账户操作尚未执行。[提交说明](https://info.arxiv.org/help/submit/index.html)、[endorsement](https://info.arxiv.org/help/endorsement.html)、[许可证](https://info.arxiv.org/help/license/index.html)

投稿形式准备不会替代专业数学同行评审。既有独立审计为自动化复核；尚未完成真人专家对证明及文献覆盖范围的评审。这个状态单独保留，不声称 arXiv 已批准或认可数学结论。

## 本次核验的官方规范

核验日期：2026-09-06。使用标准 `article` 单倍行距；无需第三方 arXiv 外观模板。源码包不含主论文 PDF、日志、隐藏文件或未使用的图。现行系统可以处理 BibTeX，也可优先使用预生成的同名 `main.bbl`。[TeX 源码要求](https://info.arxiv.org/help/submit_tex.html)

标题、作者及摘要字段为 ASCII；摘要 1619 字符，低于当前 1920 字符限制。`C. K. Zeng` 的姓名缩写格式受支持。Comments 使用实测页数和图数。[元数据要求](https://info.arxiv.org/help/prep.html)

数据和代码位于 `anc/`，供读者获取，不参与 TeX 编译。普通单主文件稿未手工设置 `00README.json`，由提交系统生成配置。[Ancillary files](https://info.arxiv.org/help/ancillary_files.html)、[00README](https://info.arxiv.org/help/00README.html)

数学主类选择依据是多项式、特殊函数及渐近分析；热方程和剪切流应用支持交叉至 PDE。最终分类仍由作者和 arXiv moderation 确定。[分类定义](https://arxiv.org/category_taxonomy)
