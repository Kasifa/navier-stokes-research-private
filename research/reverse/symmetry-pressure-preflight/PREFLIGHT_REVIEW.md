# 置换等变、中心奇性与局部压力资料：预检复核

2026-09-08。PRIVATE_CORE。**PASS FOR BOUNDED CONTRACT ONLY / CURRENT INTERFACE OPEN / NO-CANDIDATE / NOT CLAY。**

我实际全文读取 PREFLIGHT.md 与 ROOT_SOURCE_LOCATOR.md，核对下列历史科学来源后，认为可以开启一次所述精确问题的有限合同。所读旧记录没有直接回答它；这一判断限于列明的读取范围，不是全库或外部文献的新颖性保证，也没有预先接受一对反例数据。

受审 PREFLIGHT.md 实测 SHA-256 为
abf66039c0c6d158d88c3b293c7bffbd93d9ebc043a327fe357dc9f84f867150。
未发现需要修改受审预检结论的实质问题。

## 审查身份与任务边界

我不是 Gauss 的 PREFLIGHT.md 作者。我此前写过 Miller 来源范围稿 PRIMARY_SCOPE.md、本项相邻的 POLARIZATION_INDEPENDENT.md，并对 Gauss 的纯支撑独立稿作过非作者审查；另有本工作树较早阶段的推导和审核经历。本轮也读了根的定位稿。因此这是有历史背景的非作者来源与范围复核，不称盲审、第三证明或外部同行认证。

本轮只审核问题是否有必要进一步锁定。没有构造或对称化新初值，没有推导新压力标量方程，没有选择实际频率、参数、邻域或时刻，也没有运行科学程序、数组、数值求值、扫描、Git、外发或发布。仅写本文件；未接触其他任务状态或队列。

## 旧记录确已支付的内容

AE 原稿第1–153行实际包含单位黏性的完整梯度演化与压力 Poisson 关系。AE.10–11 的推导不含除以速度模长的操作；预检稿把它与仅在 \(q>0\) 适用的方向、纵向量公式分开，准确。停滞点不能支付那些除法，也不能自动消除黏性所需的局部高阶导数。一般固定正 \(\nu\) 的后续接口仍须按当前方程核清，不能把单位黏性旧式无注记移入。

旧 exterior-pressure/PROOF.md 已完整保留周期 Green 核、外部应力与四阶核积分、光滑周期修正及能量—距离界。它也已给一般外环的非零中心 Hessian 与旧对角探针符号。OUTCOME 明确区分静态压力接口、NON-NS 路径和真实解的有限持留结果。因此一般压力非局部性及一般远源改变中心压力，确实不能再算新输入。

我额外读了 JOINT_TEST_PROOF.md 第1–125行，以核清“完整中心压力矩阵也曾被匹配”的历史边界。所读对象是旧对角应变、三个既定外环及一条明确标记 NON-NS 的时间路径。三外环能够匹配其特定无迹对角矩阵，不能据此宣称已经完成当前双对称类中、共同局部速度资料下的混合 Hessian 比较。

AH 的所读入口是全空间常向量平台加远源压力，再服务于特定全域压力投影残差预算。AD 的所读目标是全环面 \(L^3\) 压力功的正负号。两份旧审查分别确认 AE/AH、BF/BG 的原范围与未付动力学；它们没有记载当前双对称比较命题。R0.71R §5.3 的 initial-jet 是另一 Fourier 观测的初始系数测试，并明确没有正时间 Duhamel 余项控制。first-cycle §6 也早已承认只给内区速度不足以决定周期压力。这些去重区分与受审稿一致。

## 为什么尚不能以旧记录回答当前问题

待检命题同时要求：固定标准三维环面、光滑实值无散零均值、全部坐标置换等变、中心奇性、两份数据在原点同一邻域完全一致，以及比较同一指定的 \(\partial_{12}p(0)\)。

旧外压稿直接验收的是其特定外环和压力探针，并没有核验上述全部约束。其全空间主 Hessian 的显式矩阵是对角的；这一旧非零性证据尤其不能直接当成当前混合分量的非零性证据。完整周期修正的存在也不自动补出所需混合分量。

对旧场作某种群平均，属于尚未完成的步骤。速度约束、二次应力的交叉项、压力响应及最终非零性都要重新核清；不能把“平均后满足对称”与“压力差仍非零”视为同一句话。当前预检没有越过这一缺口。

我本轮定向读了 [Miller 2404.01505v3 的 Proposition 3.1、Theorem 3.2 与 Corollary 3.3、3.5 陈述，PDF 第25、27–28页](https://arxiv.org/pdf/2404.01505v3#page=25)。原点梯度形状确有既有来源，所列 Biot–Savart 表达明确积分于 \(\mathbb R^3\)。它们没有在所读陈述中提供当前周期压力分量的局部资料判定。本轮未重读其全部证明或外引；没有将全空间核移作周期核。检索未命中的事实不承担这里的数学结论。

因此，准确判断是“列明旧记录没有提供当前精确量词下的答案”，而不是“已证明该问题此前无人解决”。

## 可以开启的范围，以及仍未接受的结论

值得锁定的是预检第3节写出的那一个问题：上述允许类中，原点邻域完全相同是否强制指定混合压力 Hessian 相同。它检验额外对称约束能否让一般非局部压力具有更强的局部决定性；这个约束兼容性问题尚不能由旧一般外场结果代替。其价值限于此项输入检验，不是新增机制或候选。

新合同应保留受审稿已说明的边界：

- 允许结论为不变、可变或尚未闭合，不预设反例存在。
- 若证明可变，完整周期压力与全部速度资格必须同时核验；只能接受实际证明的某个局部资料类，不能升级为每个局部资料类均可指定任意压力值或两种符号。
- 若连接初始演化，只能使用两份数据各自的同数据真实 NS 局部解，保留黏性、高阶局部项及严格小量。两条比较解不能拼成一条轨道。
- 即使局部资料不足成立，也只否定以这些资料为全部输入的普适局部闭合，不否定一般非局部闭合、长期机制或任何尚未研究的动力学。

本轮没有开启或代写该合同，更没有完成反例证明。预检的 CURRENT SCALAR CLOSURE OPEN、NO-CANDIDATE 与 NOT CLAY 状态应保留。

## 实际阅读与来源字节

以下路径相对于 /Users/kasifa/Documents/Math/navier-stokes-reverse/。均为本轮实际读取的文本及实测 SHA-256。旧稿中的具体实例只用于辨认已付范围，没有重新采用、计算或选择为本轮数据。

| 来源 | 本轮实际范围 | SHA-256 |
|---|---|---|
| research/reverse/symmetry-pressure-preflight/PREFLIGHT.md | 全文 | abf66039c0c6d158d88c3b293c7bffbd93d9ebc043a327fe357dc9f84f867150 |
| research/reverse/symmetry-pressure-preflight/ROOT_SOURCE_LOCATOR.md | 全文 | bbd8c3d57ad138a123f5dcb32e5599ac013bf7442636e3a01ed31bd96edf350b |
| research/clay_b_longitudinal_strain_preflight_20260906.md | 第1–153行，AE.1–13 及范围说明 | 732df392fc9d426e572190f05d6d72bb9bf09922a09a9b9ca7712b598c413967 |
| research/reverse/exterior-pressure/PROOF.md | 全文，只核历史对象与已付范围，不重新认证全部旧核估计 | 50df7a60076567acac9cbad6588132c3e0f49e77f84f17ee68e740a8a32478b9 |
| research/reverse/exterior-pressure/OUTCOME.md | 全文 | 17024e2a79907d19f6d25c2d3261f58b899f9f269626f30cb841e22ccd301d7e |
| research/reverse/exterior-pressure/JOINT_TEST_PROOF.md | 第1–125行，覆盖 §§1–4 及 §5 入口；不称本轮全文审查 | 9d0100f62ec6ef25ef2552348120d2b7b1e802aba49167bf4115edad02a3cd91 |
| research/clay_b_pressure_quotient_independent_audit_20260906.md | 全文 | 55be7e8b65281970a2ac6605794c361d9ecf3f8870295a0a1df93ce252e10dc3 |
| research/clay_b_pressure_mechanism_screen_internal_audit_20260906.md | 全文；其历史程序描述不表示本轮执行程序 | dcb9e4a3187a31b4d3b3e85f81f35eb088a4980324ac05b9e4f00997ddb69035 |
| research/clay_b_pressure_residual_obstruction_20260906.md | 第1–123行 | 12d1c6b1c658084ce9243e5ab985347acb49f1bb6bd06757fe82e2ff93da416a |
| research/clay_b_pressure_sign_20260906.md | 第1–132行 | c02090cf86979b1b8a6edb9fc6380d4bc254ee81d3e7bc688876442b80d5655f |
| research/r071r_report-source.md | 第525–610行，§5.3 全文及相邻范围 | fb9b0ee61b10d3f630e0b52f78fcca96e9d9e484e0410f324d41e20e76ed9e5f |
| research/reverse/first-cycle/PROOF.md | 第210–243行，含 §6 全文及相邻范围 | a87672a035f1c80a0225ce8956fca53ffc2eb07fdd4e83092505b4ac657f6120 |

官方 PDF 仅按上列固定版本定向读取陈述；工具附带的相邻轴对称、群和爆破片段不作为此次审核输入。未重取 PDF 二进制 SHA，也不以我此前 PRIMARY_SCOPE 的 PDF 哈希冒称本轮实测。没有复现受审作者的所有搜索命令，其搜索历史仅按作者披露保留。

本审查完成后实际全文自读，终核两份受审/定位文本字节，随后停改并报告本文件 SHA-256。
