# Clock / stochastic preflight：内部审读与记录验收

日期：2026-09-07。研究角色；内部预检，不是科学 release。
基线提交：d85b480d8cecec7a781bc3581eea3816c23d689b。
本记录不证明新颖性、外部同行认可、G、无原子或全局正则性。

## 1. 实际研究范围

主任务完整读取 13 份已列入文献台账的历史文件，随后核查三篇原著的
相关部分，并构造主记录 CG.1--11。
A 参与历史去重、Constantin--Iyer 原著读取和双噪声计算。
B 参与历史去重、Drivas--Eyink 原著读取及有限有理数复算。
A、B 均不是本轮唯一非作者审稿人。

C 是本轮唯一完整非作者内部审读者。
C 全文审读实际主记录、report-source 和文献台账，独立重推 CG.1--11。
历史部分是 9 份相关原文件的关键锚点及所需完整证明段落；
另核验台账 13/13 文件的实际哈希、长度及基线原始字节。
这不等于 C 全文重审 13 份文件，更不是全仓库重新认证。

C 直接读取的官方 HTML 范围为：
CI 表示定理与第 4 节推导；
DE 第 5 节、尤其式 (53)--(54) 及解释；
均值—协方差预印本的光滑假设和第 2--4 节相关定理证明。
没有把选读扩张为全文、所有外部依赖或新颖性认证。
预印本的页面日期差异保留未决。

## 2. 非作者审读结论及修订

C 接受了以下精确界限：

- 交叉 Itô 变差为正；协方差源为正；对角修正为负。
- rho=0 的独立乘积、rho=1 的原始均值及周期 Leray 投影一致。
- 相对扩散消失不等于物理对角无扩散。
- 合法周期坐标 z=y、r=x-y 给统一 rho 的共同方向强制性。
- GN--Young 仍要求未支付的时间四次应变成本。
- 函数空间迹反例不是实际 NS 随机流反例，也不排除直接对角估计。

发现并改正两处文字精度问题：
主记录明确 DE 为“一半方差”的体积平均；
报告明确对角均值须经周期 Leray 投影才能恢复速度。
每次 apply_patch 还规范了一个额外 EOF 空行。
两文件逐句逆改后再补一个末尾换行，分别精确恢复先前已审哈希：

- 主记录旧版：29ae3bece379dc3b6bfbea0c61f429298109205d52f2037c51ff95bb54ed314b。
- 报告旧版：ed9ee246e0d5769967ae180b132a8ee9189184f96e18baae5bd09a9d15e8c20c。

C 与 B 均已验收修订后的实际文字和字节。
只计一次完整 CG 非作者审读，加上述增量验收，不重复计轮次。
C 对台账的完整审读版本为 fd21dfd1180341082da883cbebb83382eedf79b0dfc745bade6f922b0ac9ea35。
其后主任务仅把 artifact_verification 状态从 in_progress 改为 complete，
得到下表台账哈希；该状态不是数学证明的替代品。

## 3. 复算及结构检查

B 独立执行 Ruby 2.6.10 内建 Rational 的 16 项命名系数检查。
其完整实现已保存为 scripts/clay_b_clock_stochastic_preflight_qa.rb。
主任务执行保存的同一实现并再次运行，输出逐字节相同。
这是同一实现的可复现性，不声称两套独立程序。

16 项包含 3 个系数/指数负对照：
对角缺陷反号、交叉项反号、Young 共轭指数换成 3，均被拒绝。
它们不是对完整数学文稿进行变异，也不是 PDE 证明证书。
完整命名结果及输出在配套 QA JSON 中。

主任务另检查：UTF-8/LF、11 个连续唯一 CG 标签、
11 对显示公式定界、行文禁词、原著 URL、3 个来源和 13 个历史条目、
13 个实际文件与基线字节身份，以及 git diff --check。
未生成读者 HTML/PDF，未作渲染或视觉验收；不把结构检查写成视觉检查。

## 4. 记录保护的实际核对

更新研究 checkpoint 后，主任务逐个比较基线解析值：

- 22 个旧 review 字段原值完全保留；新增本轮 review 后共 23 个。
- paper 对象完全相同；其排序键 JSON 的 SHA256 为
  c9755ea86f93575cc96c28ac5b3caa1a059bddec2b58a448d09d9cc54d6431c5。
  序列化明确为 Python `json.dumps(paper, sort_keys=True)` 的默认形式：
  ensure_ascii=True，separators=(', ', ': ')，UTF-8 编码，不另加末尾换行。
  它不是紧凑 JSON；独立比较的首要保护仍是解析对象完全相同。
- 最新及历史 release、source/freeze commit、单次交接及收据字段不变。
  历史加上最近两项共 16 个不重复 release。
- 用户的 AGENTS.md 仍为
  80959a5c6d2db01543f8f1ae1ddc2e1ba7430c1b14d1b4ef658dcc965efecfab；
  该用户改动不纳入本轮提交。
- 除研究 checkpoint 和用户 AGENTS.md 外，已有 tracked 文件未变。

当前工作对象、内部结论和下一步已更新；没有把历史 pending 文字事后重写。
下一项投影问题仍是待筛选问题，没有被登记成已经完成的推导。

## 5. 绑定的实际文件

下表是记录提交前的实际字节；不使用包含自身哈希的循环清单。

| 文件 | 字节 | 行数 | SHA256 |
| --- | ---: | ---: | --- |
| research/clay_b_clock_stochastic_screen_20260907.md | 12014 | 260 | ed8d6ee53e35d5097fd96858832542925b0d8fbf3454841ad2ff047f5b7f8f46 |
| research/clay_b_clock_stochastic_report-source_20260907.md | 2477 | 44 | 0bc14ab22af8030b96752a285beb68daf26bfa18caaa7ccc3d7bc5d5d177502c |
| research/clay_b_clock_stochastic_literature_ledger_20260907.json | 18502 | 422 | 1a8909992e369e1f081628d2e66dd54282a7e75448ce5ccdea60a2215439013d |
| scripts/clay_b_clock_stochastic_preflight_qa.rb | 2207 | 56 | aa7d661894c2087668f2882b995456ddc4e4c030c551dbdc392743617cc1d6f2 |
| research/clay_b_clock_stochastic_preflight_qa_20260907.json | 8159 | 197 | d1fed3d2f56b8a2b82ed69cb0d29c89bb177156e86849e3f0a223def2ae51e1d |
| research/clay_b_active_checkpoint_20260906.json | 54377 | 170 | 637b192ec66f98677c10240ab14d3b6ac51da7b40ffaac7cf5e35dbc4c1a2981 |

## 6. 分工与完成边界

本轮记录的是内部去重、原著适用性审查和条件预检。
没有降低 G 或 R.216--217 的输入，因此不创建新科学冻结或发布交接。
最近完成小节仍是 ClayB-SourceEnstrophy-20260907，既有收据保留；
本轮没有重发。

没有读取发布任务、发布索引、队列、状态或 CI；
没有等待、轮询、部署、推送或报告发布结果。
没有模拟、DGX、科学附图、新读者 PDF 或全站 recap。
这是一次本地研究记录提交，不是网站发布完成证据。
