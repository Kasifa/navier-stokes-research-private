# C₃ 六载波：来源、实际阅读与当前证据范围

2026-09-08，PRIVATE_CORE。本文记录阶段 A/B 完成时的来源状态；**阶段 C 和具体完整 NS 应用证明的最终审查仍 pending**，不以本来源表提前接纳本包。

作者是本项 PREFLIGHT、阶段 A/B 程序及 ALGEBRA_A/B 的作者，曾审查一般 GS 来源桥，也有旧四载波工作经历。根在结构预筛前提供了坐标和思路，合同还披露其第一带系数先行手算；B 使用 Pasteur 已形成的方法预审。因此这是具有明确历史接触的来源记录，不是新一份互盲证明或非作者审查。

## 1. 旧科学来源与没有重新主张的内容

**R0.73Z-B 的循环低种子。** [原稿 §5](../../r073z_pressure_active_kernel.md) 已讨论 \((\sin x_3,\sin x_1,\sin x_2)\) 的三个轴向共轭组，并指出其对流项非梯度、纯热衰减不能当作实际 NS 轨道。这是循环种子与动态资格边界的本地先例；它没有在所读段落给出当前三个高载波或六目标的完整四叶相消证书。本项不宣称 C₃ 对称或循环低种子新颖。

**FA 的真实空带激活。** [FA 原科学稿](../../clay_b_frequency_activation_20260907.md) 使用两个正负 Euclidean 频率中心附近的四个光滑 bump，周期化并随 N 改变初值；FA.12–16 已支付正黏性实际原解的一次空带激活与余项。不能抹除该成果，也不能把它的初值族、中心主极化或时间窗冒作本次十二个离散初始模的数据。[旧返回接口](../return-interface/INDEPENDENT_INTERFACE.md) 所核中心极化障碍同样不直接排除本族，更不把有限带宽整体判零。

**有界去重，而非新颖性认证。** 本项 [PREFLIGHT §6–7](../cyclic-six-carrier-preflight/PREFLIGHT.md) 已记录对 research/r073*.md 的定向关键词检索及全部命中范围。七份命中文件中六份只在命中段讨论循环估计或循环 FFT 等文字，另一份为上面的 Z-B。关键词不覆盖所有数学等价表达，因此未命中不能证明本树或外部文献中不存在等价对象。本次不再广搜，也没有新读外部论文或 PDF；旧来源账目不自动授予本轮外部全文原读身份。

## 2. 一般来源桥与当前应用的分工

[GENERAL_SOURCE_BRIDGE.md](../four-leaf-preflight/GENERAL_SOURCE_BRIDGE.md)，GS.1–28，是本项直接使用的一般条件来源桥；本人此前逐式作了其[非作者审查](../four-leaf-preflight/GENERAL_SOURCE_BRIDGE_REVIEW.md)。该桥从同一固定有限 Fourier 初值出发，保留全部有序 Fourier–Leray 作用、热因子、完整叶数级数、空间导数尾、经典性、同数据唯一性及周期压力。

其直接投影条件是 \(P_Lv_0=0,\ P_Lv_1=v_1,\ P_Dv_0=P_Dv_1=P_Dv_2=0\)。真实 \(g=P_Lu\)、由 \(B(g,g)\) 定义的 S、纯二叶响应自作用 W，以及混合项 M 是不同对象。GS 分别控制实际来源尾、完整目标尾和四叶热森林误差；\(M_0=0,\ W_0\ne0\) 还必须由具体数据支付。它本身不提供当前数据，也不自动给指定第一生成模逐时非零。

本项预筛已在当前支持上手核上述投影条件及指定六目标的短叶唯一性。当前合同另规定新初值范数界、三对共同下界、第一带出生误差和原主窗；具体解析应用仍须与 A/B 规范和最终独立有限核验逐项接合。不能拼接旧四载波窗口，不能移植旧三基频奇偶增强，也不能把有限树当成完整原解。这里不宣称 Wiener 范数、Catalan 叶数界、热森林估计或 C₃ 协变方法本身新颖。

## 3. 当前新增的有界证据

**结构预筛。** 当前十二模族及固定三对目标满足完整 NS/Leray/热循环协变，目标频率行列式为 91；每个指定目标不超过四叶的表示只有合同所列四个叶，但其全部有序树和叶放置仍须求和。新支持已有长度 8 的关系，未继承旧图的全局最短关系 11。此处的“新增”仅指本有界记录的实际对象和证据，不是外部优先权主张。

**阶段 A。** [ALGEBRA_A.md](ALGEBRA_A.md) 和其原 JSON 保存六目标直接带标签递推的完整 C、M13、M31、Z 与总项，保留三分量、两符号线性幅度列、五种有序四叶树、Leray、循环关系及共轭。实际原混合行列式 P 为六次。它是指定目标计算，不是整个十二模全频卷积或完整 NS 谱求解；阶段 A 恰执行一次。

**阶段 B。** [ALGEBRA_B.md](ALGEBRA_B.md) 和其原 JSON 保存全部两个不同实根、单重性、原 M 行秩及固定规范。两根均秩一，完整 Z 为零、C 三分量均非零；依事先顺序选择较小根，并用未经行缩放的 \((v,w)=(-s,r)\) 形成唯一数据。所选根的非零坐标下界、完整初值范数上界和原正有理 T 已认证。平方自由 Q 未被当作不可约最小多项式或数域；零判使用同一指定实根的 gcd/Sturm 证书。方法来源是 [ROOT_METHOD_PREFLIGHT.md](ROOT_METHOD_PREFLIGHT.md)，具体选项先锁于 [STAGE_B_IMPLEMENTATION_GATE.md](STAGE_B_IMPLEMENTATION_GATE.md)。阶段 B 恰执行一次。

这些是本项已运行的精确有限证据，尚需阶段 C 的另一组织核验、具体 NS 余项证明的最终审查及根比较。本文不读取或预记尚未完成的 C/具体 PROOF 审查。没有 B(W₀,W₀)、真正下一代、模板复制、放大、统一迭代、固定初值无限尺度或奇性结论。

## 4. 阅读账目与当前字节

本次为撰写来源表，只重新全文读取已停改 PREFLIGHT 和本人旧 GS 审查，并核下列当前文件哈希；没有重新展开旧外部文献链。下表把此前实际阅读与本次元数据复核分开。路径相对本目录。

| 来源 | 实际阅读身份/范围 | 当前 SHA-256 |
|---|---|---|
| ../cyclic-six-carrier-preflight/PREFLIGHT.md | 本作者先前全文自读；本次重新全文读 | 39cabe5efa8e32f7475bd9974bc91bfa38a0db16cfb7b3c4c87cd91977a8437f |
| ../../r073z_pressure_active_kernel.md | 本项预筛实读 1–64、436–499 行；本次只复核字节，未称全文 | faa6e2e475e7ce4f5663a0cc13647a14f414157abfae4b9582ced56726f86a68 |
| ../../clay_b_frequency_activation_20260907.md | 本项预筛全文读 FA.1–17 及边界；本次只复核字节，未追读 AJ 依赖全证 | 42bbc2ba3abae7aa1eeb25ee0b29f896d7d8ddcafccb0da518dded4851dd897a |
| ../return-interface/INDEPENDENT_INTERFACE.md | 本项预筛全文读；本次只复核字节 | 610b9da62651deb5caed543bb8d2f9d721f98062f2719c3f82bc2d3220d5c787 |
| ../four-leaf-preflight/GENERAL_SOURCE_BRIDGE.md | 此前非作者逐式审查及本项预筛均全文读 GS.1–28；本次只复核字节 | 59354781b8d04087cf1d5383824dbe741d24b3c0fae8798caa6c50cae24a3ebe |
| ../four-leaf-preflight/GENERAL_SOURCE_BRIDGE_REVIEW.md | 本人旧非作者审查；本次重新全文读，不能算新增独立证明 | d1501ef46d0e4b126f3c659ace9c40fcfb40bce52536b3cd1f466ed26488b196 |
| CONTRACT.md | A/B 准备及最终执行门时全文读；本次只复核字节 | a441be9b7adf0ee900eeaa786119e7c6f8fecb4c3a01bc4678f1c23fddad1a9b |
| ROOT_METHOD_PREFLIGHT.md | B 源码准备时全文读；本次只复核字节 | 2fb88e7166ee62fa1b3df24415542970580bb3d520971386b482f5a5db80453a |
| STAGE_B_IMPLEMENTATION_GATE.md | B 源码准备时全文读；本次只复核字节 | af692a572eee828b7415e29fb784197c10329e3c98cdf0a5a765ec6b884fe39f |
| ALGEBRA_A.md | 本作者全文自读停稿；本次只复核字节 | a5dad046a56e3f6d6a9a417304635c23c9e84871528baffbfd5dbedf6cfea32b |
| exact-coefficients-output.json | 已实际读全部六目标根向量、primary C/Z/M/P、检查/资源；未称全部低阶子集数组人工全文读，详见 ALGEBRA_A §6 | 9329464c09faa50558bc090b3af8c3ec6f074619e01a9fe2d5eb6d0f1c079ae6 |
| ALGEBRA_B.md | 本作者全文自读停稿；本次只复核字节 | 2321cea6a0b066e5356b98c22198bf389180e4a53181c4e5bb3ab9825093c499 |
| exact-roots-output.json | 已实际读全部根/规范/六目标/窗口/零判、gcd 结构和全部 Sturm 链；其余中间商余式系数字典不冒称全文人读，详见 ALGEBRA_B §6 | 6fd933ebd18bdf8b129f7cabdbf1f02438de3fd95f9720b18e41887815f31bcb |

六份其它 R0.73 命中文本只曾读取关键词附近段落，其文件/行范围/哈希完整留在 PREFLIGHT §7；不提升为本轮全文科学来源。GS 的旧 SB/SAL 依赖实读范围留在其审查 §1、§7，也不提升为本轮重新全文原读。A/B 源码的全文自读、运行前版本、唯一命令及原资源边界分别记录在 ALGEBRA_A/B；本文没有执行或复跑科学程序。

只写 SOURCES.md，旧稿、源码、原始输出均不改。全文自读后另报本文哈希并停改；最终冻结状态须依据届时完成的 C、具体数学审查和根比较另行收口。
