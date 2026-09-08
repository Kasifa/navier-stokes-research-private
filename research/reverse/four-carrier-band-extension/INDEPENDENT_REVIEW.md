# 同一四载波接收带的非作者核验

2026-09-08。PRIVATE_CORE。**静态数学与代码审查完成；唯一独立证书运行尚未授权执行，结果仍待核验。**

本记录当前不记代数证书 PASS。review_band.py 的最终比较适配器已完成并全文自读580行，尚未运行；review-band-output.json 尚未由本核验产生。根保存最终代码并另外授权后，才使用同一代码一次运行，同时核全部16行与主证明的有理时间窗。不运行受审程序、不覆盖受审输出。

## 1. 作者关系和形成顺序

我为 GENERAL_SOURCE_BRIDGE.md 作者、本项合同预审者及前项独立代数非作者审查者，不是本项主代数作者。先全文重读本项 CONTRACT.md、SOURCE_WINDOW.md，重读旧 INDEPENDENT_ALGEBRA.md 第158–270行的固定根及规范 w，形成显式有序五树、24个标签排列、双叉积 Leray、有理数对算术的核验核心。当时尚未读取本项 exact_band.py、原 JSON、ALGEBRA.md 或根 PROOF.md。

准备核心期间根已告知原作者运行报告的 G/秩摘要，因此不称结果盲审。核心停改后，取得作者最终停稿消息和根允许读取的指令，实际全文读取原程序603行、原始 JSON 全部3645行，以及 ALGEBRA、PROOF、OUTCOME、SOURCES、BAND_SCOPE_NOTE，再完成比较适配器。此为独立组织的非作者证书复核，不是第三路盲构造。BAND_SCOPE_NOTE 的作者已接触根的乘子观察，其身份也不改写为盲推导。

## 2. 静态数学与代码审查

**唯一叶与全序求和。** 四载波整数关系为整数倍 (−2,−3,−5,1)，非零关系的最小一范数为11。两个至多四叶表示的差一范数至多8，故同一 K4 接收不能有不同净标签数；其四个净标签绝对值之和已经为4，四叶表示不能另含抵消叶。少于四叶也不能表示它。这同时保证16个接收互异、非零、低阶空目标，并使显式四异叶树与全八模卷积在 K4 上等价；不把 K4 说成全部四叶输出。

**主程序完整性。** exact_band.py 对全八初始模计算 H1、H2 与完整第三门，先求全部有序卷积再取 K4。两个三叶方向分别保留，根门同时保留 Q(H1,H1)、Q(a,H2)、Q(H2,a)。每次 Leray 投影作用于完整原始向量；导数因子为左幅值与右频率点积。零频输出利用无散条件严格为零，没有以除零规则删掉潜在非零项。只在完整和之后删除精确零向量。没有把带外频率从原解或这些卷积中截掉。

**时间和相位。** 无黏性领先系数的二、三、四叶门因子分别为1、1/2、1/3；显式五树中平衡树总因子1/3，四个梳树各为1/6。实偶初始 Fourier 系数依次给物理相位 −i、−1、+i，四叶向量剥去共同 i 后为所选实嵌入中的实向量。于是 Hermitian 模平方为剥相位后各实分量平方之和；C²−64Z² 判据在此域正确。相反模的剥相位向量取负，恢复 i 后满足真实共轭性。

**实代数证书。** 二次商域的乘法使用已锁定二次式约化，不更换根。固定有理区间位于抛物线顶点左侧，端点异号隔离较小根；仿射值按两端点给上下界。零商余式、非零有理常数和严格同号区间分别处理，未定不能当失败或删去。主 JSON 的实际16行均声明严格符号；这些具体大有理系数及端点等式将由唯一独立运行逐个复核，不以肉眼阅读替代算术验证。

**来源窗。** BR.2 的下界来自一个分量的绝对值下界乘2，因共轭双模的 A0 范数为2|Ck|；这是合法的双模因子，不是再对已含双模的 S_k 求和两遍。BW.1 对每个对称投影使用同一个 E，不按接收个数放大或缩小常数。两份误差分别是 S−t³W0 与 P_Du−S−t³M0，不能混同。逐对供给下界和共同最小时间保证每个通过方向实际非零，聚合结论由不重复的相反模态对拼合得到。

令 w_k=||P_{±k}W0||、||P_{±k}M0||≤w_k/8，Et≤ell_min/32≤w_k/32，则 S 下界为31w_k t³/32，目标减来源上界为5w_k t³/32，目标下界为13w_k t³/16，比值至多5/31<1/4，严格余量11/124。t≤1/1624 保证既有全阶收敛窗，t≤1/76484296 保证既有第一带非零下界。这是已审源桥的同一真实原解推论，不重启投影、不移植奇偶性。主 ell 和主 T_G 将单独核算，不能以复核者更小的窗代替主窗。

**范围。** 原结果报告只有 ±(3,4,6) 通过、秩1，在独立算术确认之前仍作为受审证书内容。秩未到3时按合同跳过形式自作用，不是算完后删掉结果。七对未过1/8首项门不等价于实际来源在任意时间都不满足1/4，也不否定其它目标或一般再生成。BAND_SCOPE_NOTE 中秩1投影 h 的 B(h,h)=0 来自同线频率与无散点积，对同一经典解存在期间有效；完整 u 的外部交叉供给依然保留，h 不是独立热解。

该说明的复标量乘子结论只用四异叶唯一性：同一接收的所有四叶树共有 Π_{σj=+1}c_j Π_{σj=−1}conj(c_j)，非零乘子保持该首项比值与 G。它不支付改变初值后的同一个数值时间窗、高阶项、完整模板或无限迭代。本轮未实施乘子参数选择。秩2/秩3的条件边界未升级为这份秩1数据的额外计算证据。

以上静态审查未发现需作者修订的实质问题，不提前确认全部机器算术字段，也不补称全 H3 带外数组由复核程序重算。

## 3. 独立核验代码已停改，尚未运行

review_band.py 对16个接收分别计算五种有序形状、每种24个标签排列，共1920个根树项；随后才核正负共轭。每个门用 −k×(k×y)/|k|² 形式的 Leray，科学算术仅 Fraction 与整数。完整 C、Z、M13、M31、H3 三分量、两模平方、差式及每个作者区间证书逐项比较，不只比较成功者或秩。

独立 G 的秩用有理行消元，另核原证书基位于 G 并张成 G。每个通过对保留唯一 σ₁=+1 代表，核主证书的非零分量、端点绝对值下界及双模因子。独立核心的保守单分量 ell 与主证明的双模 ell 分别保存；同一次运行计算各自 T_G，对主 BR.3 保存三个候选有理时间、最终最小值及预算余量。

独立程序不重算 H1/H2 中间全数组或 K4 外根数组；这些本次实际全文读取、程序组织静态审查，K4 的完整系数由唯一叶定理与显式树独立支付。未运行的退化/秩3代码分支不记为经过实际运行验证。

代码要求根另给运行授权与审查源码提交标识；主程序源码标识和审查程序源码标识分字段记录，均不由本审查执行 Git 核验。已有 review-band-output.json 即拒绝运行，最终输出用独占 xb；资源或输出超限一致标为 NOT_CERTIFIED，不覆盖失败证据或重跑。60秒、256 MiB、1 MiB 与每个符号最多128次二分不改变合同数据。资源仅 RUSAGE_SELF/当前进程，标明首次序列化前后边界，不声称含最终写入或全进程树成本。环境字段不调用 platform 模块或外部元数据子进程。

最终准备代码580行已全文自读，未做 Python 导入、编译或任何试运行。尚未执行的命令模板为：

```text
/usr/bin/python3 research/reverse/four-carrier-band-extension/review_band.py --run-once-after-parent-authorization --reviewer-source-commit ROOT_SUPPLIED_40_HEX
```

这不是运行凭证，根须保存最终字节后提供40位审查源码提交标识并明确授权。

## 4. 本次实际来源字节

路径相对于 /Users/kasifa/Documents/Math/navier-stokes-reverse/。

| 文件 | 实际范围 | SHA-256 |
|---|---|---|
| research/reverse/four-carrier-band-extension/CONTRACT.md | 全文重读 | 8687b89a22dd0788e826453f143d8aaef2fd566446f23319cfdb734a3494225e |
| research/reverse/four-carrier-band-extension/SOURCE_WINDOW.md | 全文重读，BW.1–4手核 | 16a38027facd09455fb9e9b241a377e5867d82664d4367f5fe7dc7d279ed9285 |
| research/reverse/four-carrier-band-extension/exact_band.py | 全文603行静态审查；未运行 | 2498b4d0ad430f467a48c15e5ca7d7891cbf44b97e35e506ba8d8642f1a8dc2c |
| research/reverse/four-carrier-band-extension/exact-band-output.json | 全文3645行；分六段实读 | 672265033fcbc05fb7881374d703a673bc2779d20b0612e67adb14f4dd068668 |
| research/reverse/four-carrier-band-extension/ALGEBRA.md | 全文 | 1874c7c34d24c52572f2d046d0786a853942e15f6acd28b8c9bb25b80d4262e7 |
| research/reverse/four-carrier-band-extension/PROOF.md | 全文，BR.1–4手核 | ef58ab47c42ecb77d1854b7af56ec371dc06f44cbbeedaa971ad8f0b4546705c |
| research/reverse/four-carrier-band-extension/OUTCOME.md | 全文范围审查 | 98211024b66cac8d5e1050a26b65ba45fa83807359941405f7dd172e0d863eb7 |
| research/reverse/four-carrier-band-extension/SOURCES.md | 全文来源历史核对 | cab14c17b22a58633c246916628602d21064e1cd58c2f01898af8e248338f2d9 |
| research/reverse/four-carrier-band-extension/BAND_SCOPE_NOTE.md | 全文；未冒称重读其全部旧引文 | e49d298c04d2a7f47caf84762ed9510235dd0bd5916e6c7641b02748d2ff7779 |
| research/reverse/four-carrier-source-test/INDEPENDENT_ALGEBRA.md | 本次第158–270行重读；此前已非作者全文审查 | a87cdef2cc2517e391ee193c3ad17b0e6776af3d7b8dff8f0427c2b063e08d1a |
| research/reverse/four-carrier-source-test/independent-output.json | 本次仅哈希；前项已全文读取 | de084e897e08c7faa48dd49dbb00af61f0449587b34e8a4890711c4a176a0bc7 |
| research/reverse/four-carrier-band-extension/review_band.py | 本人独立组织及比较适配器；全文自读580行，未运行 | 8bda24ef7cf580b7e81e08fadefcb57ccbf6666eb1eaccf7e2fd75f58bf5157a |

准备核心旧哈希3ff72a73a5cee4c33c614fee4cde30328211a5a905e658aed00ee16876de4327只记录形成顺序，不冒称当前运行源码。根提供的主程序运行前提交1dea1d349b6073bec9e2afacff927044184b2586只按消息记录。当前未产生审查运行输出、资源或新数据选择，无 Git、外发、发布和状态修改。本记录全文自读后暂时停改，待根另行授权唯一运行后只依据实际结果补齐最终结论。
