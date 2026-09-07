# Projected-Lamb 中文前半稿独立语义复核

审校日期：2026-09-07。

**结论：PASS，限定于下述快照的摘要、分类与关键词、第 1–5 节中文译文相对于英文源稿的数学语义忠实性。必须修正项为 0。** 已逐段对照条件、量词、否定、符号与公式周围的论证文字，以及引用所归属的具体主张。此结论不表示重新证明或独立验证了论文定理，不覆盖第 6 节及以后、最终 HTML 转换、渲染或线上发布。

## 审校快照

- 英文源稿：/Users/kasifa/Documents/Math/tmp/results-column/projected-lamb/source/main.tex，第 54–517 行。
- 中文译稿：/Users/kasifa/Documents/Math/tmp/results-column/projected-lamb/translation/part-1-5.zh.tex，第 1–407 行。
- 英文完整文件 SHA-256：897049f700b8209a42185729000be195917fee2ee30844278645fad60db9ec20。
- 英文被审段落 SHA-256（按原文件第 54–517 行，保留行尾）：8281c586d331bc8e755603b8a265c199a4de707e46f7536bac0e8b7b597f05b8。
- 中文完整文件 SHA-256：8823c474632dc4847377ab0878060309fbe0bcf92cf6d77460bc6195e40e2ec6。

未修改英文源稿、中文译稿、转换器或网站。

## 独立机械核对

此处另外提取原 TeX 并按出现顺序逐字节比较；不是照抄译写阶段的“167 项保护片段”结论。以下分类可能彼此包含，例如显示公式内部的标签，因此不应相加为保护片段总数。

| 类别 | 英文 | 中文 | 顺序及原文匹配 |
| --- | ---: | ---: | --- |
| 行内数学 | 80 | 80 | 全部一致 |
| 显示数学（独立公式环境及方括号显示公式） | 43 | 43 | 全部一致 |
| 标签命令 | 31 | 31 | 全部一致 |
| 交叉引用命令 | 26 | 26 | 全部一致 |
| 文献引用命令 | 11 | 11 | 全部一致 |
| 摘要、正式陈述、证明及 Remark 的开始/结束标记 | 18 | 18 | 全部一致 |

范围内的 3 项正式陈述、3 个证明、2 个 Remark 均存在并保持原有顺序。所有中文章节标题均与相应英文内容相符。

## 逐段语义记录

下表按中文行号定位；跨显示公式连续展开的同一论述作为一个检查单元。所有单元均已对照英文阅读。

| 中文行 | 英文开头或定位 | 检查结论 |
| --- | --- | --- |
| 2–6 | For the three-dimensional incompressible ... | PASS。拉伸与输运合并为投影 Lamb 向量的旋度；有限时间区间、每个周期 Leray–Hopf 解、涡量平方积分归一化及物理时间上的可积性均保留；局部延拓明确为有条件。 |
| 8–17 | The bulk estimate does not recover ... | PASS。固定框架、二进频率、精确因子、匹配分解、内部柱体、正时间整壳零点与非零驱动均保留；两个缩放阶数及裸预算不能一致支付的方向正确。零水平占据密度未受控制、未证明全局正则性或构造奇性、浮点计算仅作核查均译出。 |
| 21–26 | 2020 Mathematics Subject Classification / Keywords | PASS。三个分类号和七项关键词完整。 |
| 30–36 | Let u be a divergence-free velocity field ... | PASS。三维涡拉伸功及其控制途径无扩大；三篇代表文献仍归于经典正则性理论；本文目标仍限于区分 Leray 能量不等式可推出和不可推出的部分。 |
| 38–46 | The starting identity is classical ... | PASS。Bernoulli 梯度项与无散投影的区别保留；经典分解的引用归属正确，未将其本身宣称为本文新贡献。存在一处非必改的中文句法润色，见末节。 |
| 50–82 | Fix a real-even scalar tight Fourier frame ... | PASS。“固定”译为数学中的选定；完整壳注入、正部壳平方函数、Y 为零时的零值约定，以及无条件体积估计和有条件局部判据的区别正确。 |
| 84–98 | The bottom value ... is different | PASS。每个二进频率、每个非零非负光滑截断函数、固定正比例均保留；独立全空间论证置于严格内部容许柱体，排除的是仅依赖几何的较小阶因子；临界因子被饱和而非排除。 |
| 100–115 | Section ... addresses a temporal objection ... | PASS。精确局部流、整个目标壳在指定正时间为零、驱动仍非零、单重内部入壳、整数缩放和两种初始量趋零及初始涡量平方积分有界均正确。未将正时间内部事件译成初始面事件。 |
| 117–119 | The final positive statement ... | PASS。所有孤立有限阶入壳事件的表示、密度集中于零水平及当前论证未提供一致占据估计均保留。 |
| 123–129 | The heat-extension viewpoint ... | PASS。Koch–Tataru 范数与本文量的区别正确；Yang 的几何理论、Vasseur–Yang 的导数估计用途及热方程迹估计使用更强内部导数范数的归属没有交换；没有将覆盖定理译成足以恢复独立热高度边界迹。 |
| 131–135 | The closest filtered-vorticity comparison ... | PASS。Yu 工作的正近场项与附加远场、交换子、局部化可求和性条件均保留；没有从交换子恒等式直接推出缺陷消失，额外紧性或正则性输入及相关引用均正确。 |
| 137 | The paper makes no priority ... | PASS。不作优先权或穷尽文献主张的双重否定完整。 |
| 141–148 | The periodic part of the paper ... | PASS。周期域、归一化空间测度、速度零均值、零模态乘子为零以及 Leray 投影记号均保留。 |
| 150–158 | A real-even scalar tight frame ... | PASS。可数标量乘子族、实偶性、非零模態上的紧框架条件、有限和与非负项无限和的截断解释均正确。 |
| 160–164 | At energy regularity ... | PASS。正热高度才将热平滑后的 Lamb 场视为平方可积场；底部壳系数需要 Lamb 场平方可积；几乎处处强解时刻与其余零测集约定没有被改成每个弱解时刻皆可取底部迹。 |
| 166–193 | The rotational form ... / For s greater than or equal to zero ... | PASS。旋转形式、Bernoulli 项、Lamb 场的符号、取旋度步骤、无散性所给的两个耗散范数相等及热扩展方程均忠实。 |
| 197–211 | At heat height ... / This includes stretching ... | PASS。完整壳功包含拉伸和输运–滤波交换子；消失的是整个空间域上的平流配对；压力仍是梯度补项，没有新增独立涡量功项。 |
| 213–220 | At s equal to zero, write ... | PASS。正部、正分母求和与 Y 为零时取零均保留。 |
| 222–228 | Conditional shell continuation | PASS。极大周期强解、整个极大时间区间上的系数可积性、延拓结论的条件结构无遗漏。 |
| 230–246 | Set D ... and ... | PASS。紧性给出的求和关系、正部次可加性、加权 Cauchy、Gronwall、Y 有界和耗散时间可积的分工均准确；三篇强解延拓引用仍置于相同结论处。 |
| 248–251 | Proposition ... is a scale-critical conditional reduction ... | PASS。明确为尺度临界的有条件归约，未将其写为无条件正则性结论。 |
| 255–259 | For s greater than or equal to zero, set ... | PASS。热高度平方函数定义及正分母限制保留。 |
| 261–276 | Global heat-bulk estimate | PASS。每个具有所需空间正则性的时刻、正热高度、底部另需平方可积、周期 Leray–Hopf 解及每个有限 T 的量词与条件均准确。 |
| 278–296 | Shellwise Cauchy ... | PASS。逐壳估计、紧框架求和、Lamb 场零均值、全热高度积分恒等式、矩阵场 Frobenius 范数到向量场的算子范数界，以及最终速度四次方范数界均正确。 |
| 298–314 | The three-dimensional interpolation ... | PASS。插值与 Sobolev、除以涡量平方积分后的量、Leray 控制速度及时间耗散、最后时间 Cauchy 的依赖关系正确；没有将归一化体积量误作底部系数。 |
| 316–319 | For weak solutions ... | PASS。有限壳与热高度截断、几乎处处时间、Tonelli/Fatou 和不向弱形式插入依赖解的检验函数的否定均保留。 |
| 321–330 | The factorization of the unresolved trace ... | PASS。分母为正时定义、否则置零、乘积分解及仅控制体积量而未控制迹因子的区分均正确。 |
| 334–355 | Let ... be a nonnegative smooth partition ... | PASS。匹配尺度、环带频率支集、一致导数界、重叠上界、正分母与零分母约定，以及截断过渡环带贡献被精确保留均正确。 |
| 357–378 | Local packing and criterion | PASS。每个正的热权参数、重叠因子、参数为 1 时归一化后的时间可积性和时间积分界均保留；底部局部量在极大强解区间可积才推出延拓，没有把无条件堆积直接等同于无条件延拓。 |
| 380–387 | Cauchy in ... gives ... | PASS。支集局部化、重叠求和、框架紧性及谱积分分别给出相应估计，未漏掉截断支集限制。 |
| 389–399 | For the criterion, the matched annular Bernstein ... | PASS。环带 Bernstein 与截断过渡区控制、单位分解下局部功求和、加权 Cauchy 及从局部系数控制全域系数的方向均正确。 |
| 401–406 | The local criterion is not claimed ... | PASS。未声称优于既有判据；Serrin 端点条件蕴含本文局部条件，译文没有反转这一充分条件关系。 |

## 边界说明

摘要沿用英文的 “every periodic Leray–Hopf solution” 表述，并由第 2 节统一规定周期部分的零均值设定。译文第 141–148 行明确保留这一设定，因此没有发生翻译造成的均值假设遗漏。

局部命题中“左端归一化”与英文一样指以 Y 归一化；前文已定义 Y 及其零值约定。该处译文没有把归一化量与未归一化量混用。若为网页独立摘录该命题，需要连同定义和适用设定一起引用，此为摘录范围问题，不是本次连续正文的误译。

源稿摘要中的“每个有限阶入壳事件”与引言中的“所有孤立的有限阶入壳事件”分别如实译出。本次审校没有私自改写英文源稿的抽象层次，也没有据此扩大正式定理的适用范围。

## 可选措辞润色（均不阻碍上述 PASS）

1. 中文第 38 行，英文开头 “The starting identity is classical. Modulo a Bernoulli gradient ...”。

   当前句子少了常用介词“在”，但数学意思仍可辨识。可将该行替换为：

   作为出发点的恒等式是经典的。在相差一个 Bernoulli 梯度项的意义下，

   随后的“Navier--Stokes 非线性项就是无散 Lamb 向量”与公式保持不动。

2. 中文第 33 行，英文 “by adding geometric coherence ...”。

   “几何一致性”不构成条件反转或漏译，但数学文献语境中“几何相干性”更直接对应 coherence。可将该行替换为：

   经典正则性理论通过附加几何相干性、临界空间中的小性条件，或可积的强范数来控制这一功项；

本次没有必须替换的数学语义段落。
