# 支撑接口的原文、去重与不适用边界

2026-09-08。PRIVATE_CORE。根实际阅读记录。此页不替代 PROOF.md 的直接推导；没有外部新颖性声明。

## 新读取的原文范围

1. **Miller，2307.03434v5。** 官方版本与模型/对称范围见本轮已全文读的 `../symmetry-source-preflight/PRIMARY_SCOPE.md`，SHA-256 `5200cfc99a1fd2f4b88528e9a523628a0505e7496b8e65c730b24512558ddda3`。根另实际读固定 PDF 的 Remark C.22、C.23–C.24 相关段及 Appendix D 从开头到 D.11（PDF 第103–111页，正文定向提取），没有重审模型爆破证明。D.1–D.7 给整数加法支撑及完整 NS 的充分不变性；这些是已有接口。开头关于必要性的概述不代替本轮全极化证明，也不能单凭不封闭的集合判断特定极化场泄漏。D.10–D.11 的子群与缩放讨论不构成对本任务固定数据的迭代证据。[固定原文](https://arxiv.org/pdf/2307.03434v5#page=107)

2. **Núñez，2000，J. Math. Phys. 41, 6193–6197，DOI 10.1063/1.1287920。** 根实际读机构库 PDF 的六页正文提取（含首张出版信息页）；不是视觉检查。§III 用半群保证卷积支撑，子群对应平移对称。它的单向正频率类为复值，作者明确不能取实部变成原 NS；本任务不导入该单向级联结论。本文仅用其已有充分接口作去重，存在性证明仍依赖 SAL。原文全局措辞不作本轮三维光滑解全球存在依据。[机构记录](https://uvadoc.uva.es/handle/10324/39594)，[实际所读 PDF](https://uvadoc.uva.es/bitstream/handle/10324/39594/InvariantSubspaces.pdf?isAllowed=y&sequence=1)

该机构 PDF 的 web 正文访问成功；直接字节哈希尝试分别遇 Python TLS EOF 和 curl TLS 35 错误，所以本轮 **没有该 PDF 的实测 SHA-256**，不捏造或借其它版本替代。没有绕过 TLS，也没有保存/分发 PDF。其可访问的版本标识、页码和阅读范围足以定位去重；主证明不以该论文的未经检查外引为逻辑前提。

3. **Kishimoto–Yoneda，2110.08039。** 本轮搜索到官方摘要/期刊元数据，机构 PDF 打开重定向为空，因此没有计作新全文阅读。随后精确历史检索找到本树 `first-cycle/SOURCES.md` §6 已记录 Definition 1.1、Theorems 1.4/5.1 的原文范围。本轮实际重读该历史第108–136行；不重新领取已有“持续共同有限支撑”的分类成果，不把仅初始有限支撑当作永久有限支撑。这条现成文献也不是本轮 PROOF 的前提。[官方摘要](https://arxiv.org/abs/2110.08039)，[期刊元数据](https://doi.org/10.1007/s00021-022-00703-5)

## 实际继承阅读及与新问题的差别

| 本地来源 | 本轮实际范围 | 用途与不重复项 |
|---|---|---|
| `reconnection-preflight/SOURCE_ATTRIBUTION_LEMMA.md` | 全文；SHA-256 d22bcca237977647b54ebbe13288c63a24a7c610a52a7c2265f4e3cfe366607a | 完整 Fourier 算子、Wiener 压缩、同窗光滑性与唯一性。是本轮唯一直接分析依赖，不从模型近似构造真实解。 |
| `driver-dominance/SOURCES.md` | 第74–108行 | 旧坐标种子删除后落在缺坐标子群，早已使用子群充分性；该记录不证明一般全极化必要性。 |
| `r021_remainder_roadmap.md` | 第1–176行，历史阶段 | 旧生成子空间中的某个锐项不被其选择规则消灭；不把其旧下一步恢复为当前动作，不泛化到任意对称。 |
| `symmetry-source-preflight/INDEPENDENT_PREFLIGHT.md` | 最终全文 | 二阶负平移的四叶字符不能区分两种根分拆，重新解释旧 SBI 的叶数分级；没有净化混合来源，记录为 NO-CANDIDATE。 |
| `first-cycle/SOURCES.md` | 第108–136行 | 有限共同支撑分类及 FA/FCB 已有量词边界仅用于去重，不升级成本轮原文重审。 |

本轮先作几次有限定向 `rg`，包括两篇 Miller 编号/题名、支撑子群/非共线关键词、Núñez 题名/DOI、Kishimoto/Yoneda 和有限 Fourier 支撑。广泛 symmetry 搜索曾截断，不计为全库审阅；精确题名/编号未命中不证明所有历史从未读过。`r070y_report-source.md:275` 的 permutation-symmetric 只是另一三线性公式，根读检索上下文后判为假阳性。更早 R0.1–20、R0.73 与 FA/FCB 的完整首轮台账保持，未为本小接口再造一次原文阅读身份。

本轮新增工作是明确“所有横向极化”的量词后证明非共线闭合的必要性、共线例外、加法补齐和真实解的严格局部泄漏。不是重新命名已知子群充分性；也不声称这些简单代数事实有外部优先权。当前没有新的实际初值、再生成下界或支撑以外的完整动态约束。

没有科学程序、数组、扫描、图件或新 PDF。文件/来源字节哈希属于元数据工作；原文审读不构成同行评审或形式证明认证。

## 同轴投影后续的定向去重

POLARIZATION_CONTRACT 对应的是一个固定实向量在各 \(k^\perp\) 上的投影直线，和旧三对模板返回不同。根另实际读 `nonorthogonal-return/JOINT_PROOF.md` 第1–92行与 `mixed-polarization/COHERENCE_PROOF.md` 全文：旧稿已保留第一层两有序门、共轭及相干极化，因此新稿不能把完整两模算子或“相干输入必要”记为首次发现。本轮只特化一个明确的全秩极化类别，并检验其真实不变性。

针对 poloidal/toroidal、同轴投影、固定方向投影的局部定向检索未定位到相同的已审全秩分类；这不是穷尽性结论。根实际读取 `r070p_report-source.md:388–394` 及相关旧合同的命中上下文，前者是环面乘子术语，后者是局部旋流模板或检索式，不能算本项碰撞。旧高行、短窗与模板方向检索命中仅作定位，没有把未重读文件整体记作新审查。先前宽泛 sigma/σ 搜索输出截断且包含大量正负号索引，亦不作为全面去重证据。

本地来源字节：JOINT_PROOF.md 为 `057381db9781ad59d8957282f02b9c917d2a3901dcc0ca1ec0b881c1db115808`；COHERENCE_PROOF.md 为 `94d68f7b0303794e703cf6733dc9a2015a69b711a174831a6dc0b1a3093f8ce7`；driver-dominance/SOURCES.md 为 `433b16c92e6a1c7786aad0fb35e44e2067902630770bc1509d394a5293469b1b`；first-cycle/SOURCES.md 为 `53fa41805fa419f49a6ad5b3cf5b89b9649c1f59b4e94601049bf0672ea9257b`；r021_remainder_roadmap.md 为 `3737bb01910b5c313841d26c2545a1d1c286b244156779b251f5058c4659d5e7`。范围限上表和上述实际段落，哈希绑定不扩展阅读范围。
