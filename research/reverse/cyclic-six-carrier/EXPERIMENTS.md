# C₃ 六载波：阶段 A/B 执行账目草稿

2026-09-08，PRIVATE_CORE。本文仅整理已完成的两次有界科学执行：**A 一次，B 一次；独立阶段 C 明确 pending，未计为已完成实验。** 本文不增加科学执行，不报告本包的最终数学接纳。作者是 A/B 源码、代数记录和来源表作者；本账目不是非作者验证。

## 1. 事先固定的对象和限额

主合同 SHA-256 为
a441be9b7adf0ee900eeaa786119e7c6f8fecb4c3a01bc4678f1c23fddad1a9b。
它固定 \(\nu=1\)、标准三维环面、十二模 C₃ 初值族和六目标，禁止改图、插值探针、浮点求根、参数扫描及运行失败后的扩容重跑。

合同最多允许三个顺序科学阶段，各至多一次：

| 阶段 | 事先规定的科学对象 | 当前实际账目 |
|---|---|---|
| A | 六目标完整有限 C/Z 系数、全部有序根分裂及原行列式 P | 完成 1 次 |
| B | 仅以已存 A 系数，认证全部实根、原规范、唯一数据及有理下界/原时间窗 | 完成 1 次 |
| C | 非作者用另一组织，对同一有限对象作独立精确核验 | pending；不预填结果、资源或通过结论 |

每阶段一个科学 worker、一个科学线程；墙时限 60 秒，SELF 峰值 RSS 目标不超过 256 MiB，原输出严格小于 1 MiB。B 每根所有祖先隔离及后续细化共享至多 128 次二分。科学数值均为 Fraction/整数/有理多项式；资源时钟等元数据浮点不用于科学判别。

## 2. 阶段 A：唯一执行

运行前源码保存提交由根提供：
9e606f2d7d39969eb39b7e9088903c75a6909ee8。
最终源码 exact_coefficients.py：
7ce63da05ad2d2e51acfdc7cd51f6630191734574f62af000f3edba7221d9a64。
作者在执行前全文自读；根在明确授权消息中报告其全文读取和非作者静态审核已完成。本文作者未自行执行 Git 对象核验。

唯一命令：

    /usr/bin/python3 research/reverse/cyclic-six-carrier/exact_coefficients.py --source-commit 9e606f2d7d39969eb39b7e9088903c75a6909ee8 --contract-sha a441be9b7adf0ee900eeaa786119e7c6f8fecb4c3a01bc4678f1c23fddad1a9b

退出码 0；execution_status=completed；
scientific_execution_count_in_this_invocation=1；
scientific_stage_completed=true。
原输出 exact-coefficients-output.json 为 469369 字节、17026 行，SHA：
9329464c09faa50558bc090b3af8c3ec6f074619e01a9fe2d5eb6d0f1c079ae6。

实际结果是完整六目标系数通过所列精确断言，原 P 为六次，状态
COEFFICIENTS_CERTIFIED_ROOT_STAGE_PENDING。A 未求根、选候选或认证实际窗口。它按每目标唯一四叶表示做全部有序标签递推，不是完整十二模全频卷积。内部十二组“目标/幅度列”计算各有 58 次有序顶点调用，均属于这一次执行，不能另计 12 次或 58 次实验。

**首次运行前的元数据修正。** 静态审查指出固定写入执行计数 1，会在进入科学阶段前预算已耗尽的分支上失真。作者获准只修为局部计数初始 0、调用 scientific_stage 前置为 1，并单独记录阶段完成字段；科学算法不变。修订前版本没有运行、导入或作编译探针。上述最终源码才进行了唯一首跑；源码修订次数不等于科学执行次数。

## 3. 阶段 B：唯一执行

B 的唯一科学输入为上述原 A JSON；其保存提交由根提供为
1865656c86a4824069a32186d3928be226dc8d98。
方法和实现门在执行前另行固定：

- ROOT_METHOD_PREFLIGHT.md：2fb88e7166ee62fa1b3df24415542970580bb3d520971386b482f5a5db80453a。
- STAGE_B_IMPLEMENTATION_GATE.md：af692a572eee828b7415e29fb784197c10329e3c98cdf0a5a765ec6b884fe39f。

运行前源码保存提交由根提供：
f49ebe2a6ed7b7111ade1effaf3be253807e08e0。
最终 995 行 exact_roots.py：
4206577cf1464207899b7fa47741c2cff7ffac843221fb140d7f172a4b75de80。
作者全文自读并停止修改，根报告源码/实现门非作者静态审核及自身全文读取通过后，才给唯一执行授权。

唯一命令：

    /usr/bin/python3 research/reverse/cyclic-six-carrier/exact_roots.py --source-commit f49ebe2a6ed7b7111ade1effaf3be253807e08e0 --contract-sha a441be9b7adf0ee900eeaa786119e7c6f8fecb4c3a01bc4678f1c23fddad1a9b --a-input-sha 9329464c09faa50558bc090b3af8c3ec6f074619e01a9fe2d5eb6d0f1c079ae6

退出码 0；execution_status=completed；
scientific_execution_count_in_this_invocation=1；
scientific_stage_completed=true。
原输出 exact-roots-output.json 为 139696 字节、4561 行，SHA：
6fd933ebd18bdf8b129f7cabdbf1f02438de3fd95f9720b18e41887815f31bcb。

其状态为
EXACT_DATA_AND_WINDOW_CERTIFIED_PENDING_STAGE_C_AND_MATH_REVIEW。
实际全部两个实根均单重、原矩阵秩一，原规范下完整 Z 为零且 C 三分量非零；按规则选较小根。两根累计隔离深度均为 7，所选第一非零 C 坐标在初隔离区间已严格避零，无额外细化。原主窗的三个有理预算均通过，没有替换窗口或回选另一根。

B 的平方自由分解、全局半开 Sturm 隔离与指定根 gcd 零判都属于该唯一阶段。两个根、21 份 gcd 证据和 38 份零判是程序内证书对象，不另计为实验。对已存矩阵核 \(P=\det M\) 是 B 的输入一致性检查，不是重新生成 Fourier 系数或复跑 A。

## 4. 原始资源记录及测量边界

两次运行实际环境均为 Python 3.9.6、Clang 21.0.0，解释器实际路径
/Library/Developer/CommandLineTools/usr/bin/python3；os.uname 为 Darwin 25.6.0、arm64，可见逻辑 CPU 18。无第三方科学库，无新安装、子进程、分布式 worker 或科学浮点。

| 资源字段 | A | B |
|---|---|---|
| 首次完整 JSON 序列化前墙时（秒） | 0.166921334 | 0.067701125 |
| 首次完整 JSON 序列化后墙时（秒） | 0.174760334 | 0.069373958 |
| 前一边界 SELF 峰值 RSS（字节） | 17317888 | 19841024 |
| 后一边界 SELF 峰值 RSS（字节） | 19709952 | 19841024 |
| 后一边界用户 CPU（秒） | 0.177036 | 0.07208099999999999 |
| 后一边界系统 CPU（秒） | 0.011293 | 0.012211 |
| 记录边界检查 | PASS | PASS |

墙时起点是各模块最初导入 time 后，后一边界包括其余导入、输入读取、科学工作、断言、字节复核和首次完整序列化。最后补资源字段、最终序列化及唯一 xb 写盘不在这个后一边界内。CPU 与墙时起点不同，不能相减解释成科学耗时。Darwin RUSAGE_SELF 的 RSS 直接为字节，不冒称全进程树或完整生命周期证书。

两份原输出都未触发失败压缩记录或输出超限。源码、合同和相应输入在科学阶段前后进行了字节核验；本文撰写时再次核对原 A/B 源码和输出 SHA，均相同。计时比较本身不承担科学质量或方法优越性结论。

## 5. 与科学执行分开记录的两个事件

**B 后元数据脚本解析错误。** 根告知，在 B 已完成之后，一个独立的元数据 stdin 脚本出现 SyntaxError: Non-UTF-8，失败发生在解析阶段；后续以 ASCII 元数据脚本修复。原 B 输出保存版本为 cf524c65，修复版本为 42e65a5fd9f03610dbb687332ef97340a1cef067；这两项版本信息来自根消息，本文作者未核 Git 对象。该事件没有进入 A/B 科学阶段，不改变原科学源码或输出，不属于科学失败实验、参数重试或 B 重跑。

本文定向实读当时 ROOT_COMPARISON.md 第 19 行的元数据事件与字节边界说明，没有读取出错脚本或运行外日志，也不声称手审其解析修复。该文件当时快照 SHA 为
e3e105c49f079bcd70d06dfdd1c453bf546ad2ebbcbf9c58ed03095901f7286d；
这只是定向阅读出处的当时字节，不绑定该文件以后新增内容。检索定位还显示其第 5、15、21 行附近的有限匹配摘段，未将其扩充为全文阅读或阶段 C 接纳。

**根的原记录转录比较。** 根报告使用 stage-b-transcription-check 比较 ALGEBRA_B 的 17 个展示分数、6 个表值及具体 PROOF 的 5 个分数与原 JSON。该检查比较已存在的记录转录，没有新求 Fourier 系数、因子、根、参数或窗口，不计科学重跑，也不替代对数学公式及独立 C 证书的审查。本文作者只接收这一比较结果说明，未执行或声称全文审查该比较脚本。

## 6. 实际阅读与停止范围

本文撰写时重新全文读主合同，承接本人已经完成的 A/B 源码全文自读和原输出定向实读；ALGEBRA_A §6、ALGEBRA_B §6 逐段列出数组阅读范围。A 的其余低阶子集记录及 B 的其余中间商余式字典，不冒称人工逐项全文重算。

两份作者记录的当前 SHA 分别为：

- ALGEBRA_A.md：a5dad046a56e3f6d6a9a417304635c23c9e84871528baffbfd5dbedf6cfea32b。
- ALGEBRA_B.md：2321cea6a0b066e5356b98c22198bf389180e4a53181c4e5bb3ab9825093c499。

默认可见科学工作树中未定位旧 EXPERIMENTS 同名模板；本文直接按主合同字段整理，未为模板扩大读取其它状态资料。阶段 C 保持 pending，本文不预填其源码、提交、命令、执行次数或结果。本文只写本文件，没有新科学计算、扫描、测试或对既有源码/原输出的修改；全文自读后另报自身 SHA 并停止修改。
