# 支撑与同轴极化：最终合并范围复核

2026-09-08，PRIVATE_CORE。**PASS：十五项新绑定及其字节数匹配；两项合并数学范围准确，未发现待修实质问题。** 这是最终范围和来源复核，不是新增独立证明、机制接纳或人类同行评议。

## 1. 身份、实读及独立性

我是两份主稿的前序非作者审查者，也是二阶平移 INDEPENDENT_PREFLIGHT 及旧 FULL_TAIL_SOURCE_READ 的作者。本次在已有主稿阅读之后首次全文读两份独立稿及其各自审查；不能称这次综合比较与此前审查互盲，也不新增一条独立推导计数。

本次全文读取 OUTCOME.md、ROOT_COMPARISON.md、SOURCES.md、acceptance.json、INDEPENDENT.md、INDEPENDENT_REVIEW.md、POLARIZATION_INDEPENDENT.md、POLARIZATION_INDEPENDENT_REVIEW.md 和相邻目录 PRIMARY_SCOPE.md。首次批量回显截断后，另行完整读取纯支撑独立稿、其审查及 acceptance，未把截断输出计作全文。两份合同、两份主稿和我的两份审查，沿用前序实际全文审过且本轮哈希未变的字节；二阶平移预检同样沿用本人此前全文自读的最终字节。

独立性记录准确分层：

- 两个合同都披露根在形成前已有有限结构预检，不能称结果未知的预注册或完全盲发现。
- 根是两份主稿作者，其 ROOT_COMPARISON 是作者实际对读。两份独立稿形成时未读取对应主稿的记录，与各稿披露一致。
- Hume 是极化独立稿及 PRIMARY_SCOPE 作者，随后审纯支撑独立稿；Gauss 是纯支撑独立稿及旧 SBI 作者，随后审极化独立稿。这是有相关作者经历的非作者审查，不是整个课题的互盲审查或第三路证明。
- 极化独立作者定位 SAL 时接触过纯支撑主稿/审查的少量 SAL 调用片段，已在独立稿和审查中披露；没有被改写为完全无接触，也未被用来替代相应证明。

本次核查的是这些实读文本及其明确接触记录，不以哈希证明人的阅读独立性。外部文献新颖性、同行评价或形式化认证不在本项通过范围。

## 2. 十五项新绑定

以下路径相对 research/reverse/。逐个运行文本文件 SHA-256 与字节计数，并与实读 acceptance.json 手工对照；十五项均一致，无重复路径或漏项。

| 文件 | 字节 | SHA-256 |
|---|---:|---|
| support-invariance/CONTRACT.md | 3776 | 6e1762229978d3238772594a7d0b87ee902c6002925a2b4ce1098c3382305b0c |
| support-invariance/PROOF.md | 10003 | 0757f3859ff4ecd09cae33326593599c1603be7ef28c294444f8115ee19fa356 |
| support-invariance/INDEPENDENT.md | 18031 | 1dc367a1f2480bf43e9df1a5ff50ae2cf86c74c8d858ffa26a7361c649b02a79 |
| support-invariance/MAIN_REVIEW.md | 6873 | 8fa537041efc80cfb2b7debe3c29fee3e47abf1ca2220ed648c7c2fce88bbdbe |
| support-invariance/INDEPENDENT_REVIEW.md | 10629 | 1871956fec27d6a459b49594b059842318a234e74af29e3ae94a6bb1e1415259 |
| support-invariance/POLARIZATION_CONTRACT.md | 3077 | de3df9e8df78d42f619996c411425b6ce6c66bedaf1a8285bbfc4e29076d7483 |
| support-invariance/POLARIZATION_PROOF.md | 6367 | 07cb56f95ba62ad2c6e8677f1e5568567ca5552466133db3f668e6a8268d8b43 |
| support-invariance/POLARIZATION_INDEPENDENT.md | 8699 | 21758a8ad18606f8cea2158a7a1cda3ab62976da530d1a395ab7fd8e618ce57e |
| support-invariance/POLARIZATION_REVIEW.md | 6647 | 0d5addda90800ab58e6bc8583c24ce26d85f2f31181dd43776f102dba0dc3870 |
| support-invariance/POLARIZATION_INDEPENDENT_REVIEW.md | 10057 | 11adce431ffab2f537e4fff88a67250d9cb8339ed4e1dcbbfd51d0380c12636c |
| support-invariance/SOURCES.md | 6533 | ac892ad6362ceb0a89ec860e42a84d215d9676985e4a9055e772416f4bf4bf81 |
| support-invariance/ROOT_COMPARISON.md | 6035 | ad2a4f0de0a91ab23800a2b5cbb18e0753d7350c0e91040c305202fabfd520a0 |
| support-invariance/OUTCOME.md | 3152 | 171284640b744d03bc677e0b976e3693e88a5856f5857f595be2f4abbf894d69 |
| symmetry-source-preflight/PRIMARY_SCOPE.md | 7130 | 5200cfc99a1fd2f4b88528e9a523628a0505e7496b8e65c730b24512558ddda3 |
| symmetry-source-preflight/INDEPENDENT_PREFLIGHT.md | 5470 | ebf24f46a42e1cc5314385121e86855c83072fc1f46d99897cb9a18bb47de592 |

所读 support-invariance/acceptance.json 自身 SHA-256 为
6b9b1c4464fa678767b2fc83f05f0a2d293b8a43af6489cac61125d1633af9e6。
其 FINAL_SCOPE_PENDING 是形成本记录前的门状态；本页完成该范围复核，不把“待最终范围”误写为待修数学问题，也不自行修改原记录。本页自身不作循环绑定。

## 3. 合并数学范围与两稿差别

**纯支撑。** 两稿确实证明相同的全极化 A/C/I 等价：对称 \(N\) 内允许每模全部横向方向，非共线和闭合是必要充分条件；实张成至少二维时，等价于 \(N\cup\{0\}\) 是整数加法子群。共线、空集、倍频、相反频率及非饱和子群均处理正确。有限非共线 \(N\) 的统一不变性失败，不能改成每个特定极化初值都泄漏。

本次另手核独立稿 SI.7 的完整初始输出号：\(p+q,p-q,-p-q,-p+q\) 依次为 \(-i\gamma V,+i\gamma V,+i\gamma V,-i\gamma V\)，其余初始有序项为零。它只是这份初值的完整初始输出列表，未限定之后解的支撑。SI.24 的压力负号与周期 Poisson 方程相符；初始压力零的观察不被提升为后续压力恒零。实张成至多一分支的热解全局性是单列的线性例外，不外推到至少二维。

主稿调用 SAL 的 \(A_1\) 入口；独立稿 SI.14–25 自行重建一般黏性下的 \(A_0\) 收缩及同窗高阶延拓。我核了 SI.21 的两个乘积与时间核因子，共为 \(4c_mM\sqrt{\ell/\nu}\)。其中低阶紧窗的有限 \(M\) 先由已存在分支取得，再支付高阶延拓，未以未知高阶全窗上界循环论证。每个阶保持在同一既有紧窗上，不把逐阶局部窗的交当成光滑窗。SOURCES 中根的 SAL 依赖记录不应覆盖掉独立稿自己声明并重推的 SBI 方法来源；两条分析路径须按各稿分别理解。

**同轴投影极化。** 两稿都固定任意非零实 \(\sigma\) 和全秩整数子群 \(L\)，只限制每模方向为 \(\mathbb C P_k\sigma\)，标量自由且负模共轭。主稿三重积 \(\Theta\) 与独立稿 \(D\) 相同，测试方向均为 \(k\times\sigma\)。P4 与 PI.6 同号，独立稿多保留任意非零复幅度乘积；没有把有序项改成相等的两项。

独立稿的频率存在路径确有区别：取 \(q_h=q_0+hp\) 保持三重积不变，其方向平方差分子中二次项抵消，PI.9 为仿射式。若它恒零，先由一次系数和非零 \(a\) 消元，再由常数项得到 Cauchy–Schwarz 等号，抵触非零三重积。此处不除以 \(b_0\)、\(C_0\) 或可能为零的一次系数；非零常数分支也成立。它与主稿的非恒零二次式都覆盖任意实轴和全秩子群，未用整数样本代替存在证明。

两稿只为存在性见证避开 \(E_k=0\)，没有用退化测试量的零值分类该分支。P9 另给复向量到极化线的精确 Hermitian 距离，PI.15 则保留更一般复幅度的线外测试下界；合并记录没有混用二者的系数。

**同一真实解。** 两项的非零初始导数都已接到完整无限维 NS，实际系数或固定线性测试具有 \(td+o(t)\)。其下界来自同一解的连续时间导数，黏性只是对初始为零的这一模不贡献初始值。压力、其它模及以后反馈继续保留。结论只给逐数据存在性正窗，未给显式或统一窗口，也没有把符号反例家族拼成一个初值的无限过程。

OUTCOME 与 acceptance 的范围恰限于上述两类指定不变性。不能用于排除其中某个特殊极化初值、特殊热解或非线性轨道、低秩同轴空间、其它极化丛、附加标量相干、离散对称、近似闭合；尤其不能未经资格检验移入 Miller 的实际壳集合及置换、奇偶、镜像共同约束的数据类，也不判断其奇性结论。两模见证可保持法向平移不变，不构成三维奇性初值。

## 4. 文献去重、预检及证据限制

本次全文读 SOURCES 和 PRIMARY_SCOPE 的实际阅读记录，没有重新访问外部 PDF；其外部页码、版本及阅读身份仍属于原阅读者。加法子群的充分支撑接口、完整两模算子和局部 Wiener 方法已明确承认既有来源，不把它们重新登记为首创。

PRIMARY_SCOPE 区分受限非线性投影、低耗散模型与普通 NS，也区分全空间 Euler 对称和固定环面变换资格。INDEPENDENT_PREFLIGHT 只说明所检二阶字符不能区分两类四叶根分拆，属于旧奇偶分级的重解释。这两份是来源/先验筛选记录，没有新增供给净化或定理。

Núñez 的正文访问成功与 PDF 字节哈希失败在 SOURCES 中分开记录：没有实测 PDF SHA，不以另一版本替代，也没有宣称视觉检查。该文只作已有充分接口的去重，主证明不依赖其外部存在定理；所以这一元数据缺口不妨碍本轮直接证明闭合。本次未重试下载或绕过 TLS。

Kishimoto–Yoneda 的持续共同有限支撑分类只沿用已识别的首轮阅读记录，不把仅初始有限支撑当作该定理的假设，也不另计一次原文全文审查。局部检索未命中不能证明没有全部历史先例，SOURCES 已保留这一限制。没有外部新颖性或整篇论文认证结论。

## 5. 旧原子文献读记：仅既有记录与当前字节

本次全文读 atom-pressure-input/source-review-record.json，并对目录内七份文件核 SHA 和字节数；没有再次全文读旧原文或重构 BP/BQ/BR。其六项 files 绑定均与当前字节一致，第七件是记录自身：

| atom-pressure-input/ 内文件 | 字节 | 当前 SHA-256 |
|---|---:|---|
| CONTRACT.md | 2457 | 7ae5f3b1d31f0b38c788c42b561a0a6ad7a31eb7c903a57e569d6dd306704155 |
| ROOT_HISTORY_AND_SCOPE.md | 4077 | 6f91be318150415b8687f70eeda81d91baeecb7b6b25d9f06e4070f400e9686a |
| inherited-inputs.json | 2561 | c54c41393b10d0ba4b7c9ac30fc8133462e8bd56cacb593eab59bf4d94319750 |
| PRESSURE_SOURCE_READ.md | 11946 | d6d67d144bcf84b1b758dbdf84a0d50887609f6104ba2b2f1e3c1a7773d0fcb7 |
| FULL_TAIL_SOURCE_READ.md | 8598 | 6cb169074e22c7a03572d358e02844506db41ce6bec22dc4cd6818eab2027fa0 |
| SCOPE_REVIEW.md | 14157 | 6a0a1c89067438ec5987b942fc4e34ff6661122e84b9d93c8a701c51a2084e57 |
| source-review-record.json | 2735 | b9d75aea83aa5b67b03bad8768df6e2dacfd0f45c96b90224ab5064f0c46f186 |

最后一项与本轮 acceptance 的附带记录哈希匹配。七件与科学源码 9b076e356222c24fa10f0c14916d54350923e7d9 的 Git 对象相等，是根已经完成并写入 acceptance 的核验；本次没有运行 Git，不冒称再次执行该对象比较，也不把记录内部的九份更早来源重新计为本次全文实读。

旧记录状态为已完成来源审议、无新增已付输入、无新定理；原子存在、实际第二代间隙、动态剖面更新及统一无限过程仍未支付。它们可以原样附带保存，不能作为新的定理或另一次正式读记成果重计。

## 6. 最终裁决

本轮通过 **PROVED BOUNDED INVARIANCE OBSTACLES / NO-CANDIDATE / NOT CLAY**。全部通过范围均为指定量词的不变性接口；没有实际两步供给成功、统一迭代、单初值无限尺度、跨代无限维余项、有限总时间或奇性证明。旧物理初值的证书缺口和六项失败证据没有修复。

未发现十五项新绑定、六项旧绑定、四份非作者审查或合并范围之间的矛盾。数值证书、科学数组与图档为 NOT APPLICABLE；没有将未运行的科学检查报告为成功。文件数只是绑定计数，不是科学价值指标。

本页只作文本、手工符号与哈希元数据复核，未运行科学程序、参数选择、Git、外发或发布。全文自读及最终来源复核完成后停止修改；本页最终 SHA-256 另报，不在正文自绑定。
