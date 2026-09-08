# 双对称局部压力问题：来源、去重与实际读取

2026-09-08。PRIVATE_CORE。根记录；主推导作者身份不隐去，未主张外部新颖性。读取文件或哈希不能代替推导，也不构成外部同行认证。

本项在固定正黏性、标准三维环面上只检验一项精确局部决定性。与旧一般外部压力结果的区别，是同时支付坐标置换等变、中心奇性、共同速度邻域、指定混合 Hessian 及各自真实解的初始应变差。一般压力非局部性、周期 Green 核的距离指数、静态外环能量锐性、原点梯度形状与局部存在方法都不是新结果。

## 实际本地数学输入

以下相对路径均在本科学工作树 research/ 下。根本轮全文读 exterior-pressure 的 PROOF、OUTCOME 和 SOURCE_ATTRIBUTION_LEMMA；AE 只读所列段。预检作者与非作者审查者的其它历史阅读不能改写成根的本轮实读。

| 本地来源 | 根本轮实际范围与用途 | SHA-256 |
|---|---|---|
| reverse/exterior-pressure/PROOF.md | 全文；直接调用 §1–2 完整周期压力和 Q 光滑性，辨明后续一般外环及静态量词 | 50df7a60076567acac9cbad6588132c3e0f49e77f84f17ee68e740a8a32478b9 |
| reverse/exterior-pressure/OUTCOME.md | 全文；旧 NON-NS 对照、已付持留和停止静态变体边界 | 17024e2a79907d19f6d25c2d3261f58b899f9f269626f30cb841e22ccd301d7e |
| reverse/reconnection-preflight/SOURCE_ATTRIBUTION_LEMMA.md | 全文；§2、4 的完整 Fourier–Leray 收缩、同窗高阶正则和唯一性 | d22bcca237977647b54ebbe13288c63a24a7c610a52a7c2265f4e3cfe366607a |
| clay_b_longitudinal_strain_preflight_20260906.md | 第1–153行；AE.1–13，单位黏性梯度结构与 q>0 公式区分 | 732df392fc9d426e572190f05d6d72bb9bf09922a09a9b9ca7712b598c413967 |
| reverse/symmetry-pressure-preflight/PREFLIGHT.md | 全文；Gauss 的定向历史及原文范围筛选 | abf66039c0c6d158d88c3b293c7bffbd93d9ebc043a327fe357dc9f84f867150 |
| reverse/symmetry-pressure-preflight/PREFLIGHT_REVIEW.md | 全文；Hume 的非作者复核，仅允许开启窄合同 | 6c71b9682f58fa1d0aa808548bad08aafdbf959b4136e8eb8919c5b4a7643b99 |
| reverse/symmetry-pressure-preflight/ROOT_SOURCE_LOCATOR.md | 根自写全文自读；当时只有原文陈述和定位上下文 | bbd8c3d57ad138a123f5dcb32e5599ac013bf7442636e3a01ed31bd96edf350b |

本项没有复算旧外场的数值实例，没有继承其压力对角探针作当前混合分量，未重认证整套旧 NON-NS 路径。独立稿若使用不同旧方法，应以其自己的实际依赖表为准。

## 本轮官方原文读取及其限度

根先定位 [Miller 2404.01505v3 §3.1，PDF第25–28页](https://arxiv.org/pdf/2404.01505v3#page=25) 的陈述；主稿停改后又补读该节完整提取文字，包括 Theorem 3.2 的证明。矩阵形状已有来源，积分明确属于全空间瞬时 Biot–Savart。本文不引入该积分、外引 Euler 奇性或主值消去证明。Remark 3.4 也提醒其特定径向形状属于无旋流轴对称类。当前十二元群只含置换和中心反演，不能冒称已满足文中另加平面镜像的完整类别。

以上是定向正文阅读，无本轮 PDF 字节重取或视觉检查，也不是整篇外引、正则性细节或新颖性认证。先前 PRIMARY_SCOPE 记录的 PDF 哈希只保留为历史版本身份，不计本轮实测。PROOF 成稿时写“只读陈述”是当时真实接触记录，本页明确后来补读的次序，不重写已停改主稿。

## 当前差异和仍未付清的输入

原点 β 的一个正小窗仅用于见证局部输入不唯一；它不等于文献启发中的长期平面拉伸，也不认证任何集中结构。当前合同不追加镜像群、局部纤维、符号、振幅或外环参数的变体；若之后再检验机制，必须直接给同一真实解的非局部动力学输入及可审核余项。

所有科学证据仅为手工符号推导，数值证书及图档不适用。既有旧失败证据和原物理初值证书缺口未改。两条比较解不是一条无限尺度原解。NO-CANDIDATE / NOT CLAY。
