# Kronecker 输入绑定启动失败的独立恢复审查

2026-09-08。PRIVATE_CORE。有限范围 PASS：现有失败证据支持“输入 pin 错写、科学核尚未开工”的判断；当前修复严格只改 manifest pin 和下一份记录目录。没有节点或科学参数变更，没有把原失败改为成功。

本人不是本块实现或恢复说明的作者。本轮全文读旧块合同、失败 run.json/claim/stdout 和 KRONECKER_STARTUP_RECOVERY.md，实际检查源码的启动、输入认证、节点加载、中心计算、乘法及异常封口路径，并以字节差异核对修复范围。未重审整个 Kronecker 数学算法，未执行该实现、check-only、节点/根号/乘法、FFT、PDE 或 git。

## 1. 失败位置有直接证据

原 run.json 的执行状态是 FAILED，数学状态是 COST_NOT_PAID；错误准确为

    original archive SHA mismatch: node-trial-01/manifest.json

products=[]、artifacts={}，maximum_small_integer_bits_observed=0。原目录只有 RUN_CLAIM.json 和 run.json；没有中心、乘法、张量或部分科学输出文件。

旧源码所用 ARCHIVE 字典的第一项就是 manifest。Python 3.12 按插入顺序执行该循环：先以 sha(HERE/filename) 和固定字符串比较，不相等即抛出这个 ValueError。正确的 SHA-256 十六进制输出有 64 个字符，所用旧常量只有 61 个字符，故此项必然失败。

源码调用顺序是：写 claim/初始运行记录；导入 NumPy；读取环境与本树 HEAD；检查三个输入文件 SHA；解析 manifest JSON；首次 np.load(modes.npy)；加载节点块；构造精确投影及 96 位中心；最后进入三次大整数乘法。失败发生在第一项输入 SHA，因此没有到达 manifest JSON 解析、首次 np.load、节点解码、投影、舍入、打包或任一科学乘法。

NumPy 已经导入且环境已记录，不能说“没有加载 NumPy”。在三个原节点档案中仅 manifest 做了流式文件 SHA；启动前另读过源码/证明和运行环境，也不能说整个进程没有任何读取或计算。

这不靠 products 空表单独推断：报错位置、源流程与空科学证据互相一致。原记录的 SHA 为 44d05321296a6b25b3997495601cc9623a8fd6562b6dfd13f08dedcbbd99fcbc，与最终 stdout 指向的 SHA 一致。最终 stdout 的资源为 0.06192362494766712 秒、RSS 40271872 字节、目录 4851 字节；这是一次启动失败的实际资源，不能作为乘法性能。

## 2. 三份原输入实际未变

本人本轮用标准库流式重新计算以下三个文件 SHA，没有解码 NumPy 数组：

- manifest.json：5ac2abdfb7a14a38904f2ef1c58d81cf90bea776ce5426a56a75c6f81622c1cd。
- modes.npy：f184c97c52e561ac53b8936ee51e68690517ad65c79e8050c93a891ac8856896。
- block-01280-01343.npz：abf3b33282ff0b08e995c6aa1f80e7d79dbd64a55137574b77d51356b236297e。

三项与此前已固定的正确值完全一致。错写的是新块合同和实现中的清单字符串，不是旧节点清单、数据、参照或物理初值改变。

旧串为

    5ac2abdfb7a14a38904f2ef1c58d81cf90bea776ce5426a75c6f81622c1cd

正确串为

    5ac2abdfb7a14a38904f2ef1c58d81cf90bea776ce5426a56a75c6f81622c1cd

即漏掉了 56a。旧合同仍保留其原错误串，恢复说明对此作了显式勘误，不把旧审查重解释成已认证正确 pin。

## 3. 旧新源码只差两个字面量

旧失败 run 绑定源码 SHA：

    daa1e5e38b95b7e1893b47ceb1d4d522ff6258af5fe622d6f00eeea9bbbdff02

当前恢复源码 SHA：

    b4d65f5a02211ff52f1a202b4e9ba25e9cee47e5a9468bb3a670aa5c381a5c08

本人没有运行 git 获取旧文件，而是对当前源码字节作两项明确的逆替换：正确 pin 换回旧错误串，trial-02 换回 trial-01。先检查每个待替换串各恰出现一次，然后计算恢复出的旧源码 SHA；它严格等于失败 run 的上述旧源码 SHA。由此，当前全文与该已绑定失败版本的差异就是：

    - OUT = HERE / "kronecker-block-trial-01"
    + OUT = HERE / "kronecker-block-trial-02"

以及 ARCHIVE 中 manifest 的一行 61 字符到 64 字符修正。其余源码字节相同。

因此节点 1280、96 位中心、原 Q52、空间基 33、240 位数位、分量 1/2、三次一般乘法、35937 个输出和算法均未变。60 秒、256 MiB、8 MiB、128 KiB 预留、整数限制、所有拒绝覆盖/停止规则也未变。CONFIG 中 run_directory 及包含 archive_pins 的配置哈希随两个字面量修复而变化是预期结果，不代表科学预算改动。

## 4. 恢复的授权及停止边界

恢复说明明确保留旧源码提交、旧合同/审查、原目录名及失败文件；它仅勘误旧合同中的 manifest pin 和下一份记录目录。当前核查时 trial-02 尚不存在。该有限恢复不覆盖 trial-01，也不把其 FAILED/COST_NOT_PAID 状态改写成 COMPLETE。

原合同禁止对成功运行重跑、对科学计算失败或超限自动扩大/重试的约束仍保留。这里审查通过的理由仅为：首次实际命令在输入认证的第一关停下，尚未取得科学结果或支付科学成本；修复不改变被固定的数学对象、算法或预算，并由新的目录单独记录。它不是对任意失败重试的许可，也不允许在后续超限时继续重试。

恢复说明要求完成根差异检查和本独立审查后，才由根代理决定一次明确执行。本审查只确认这项有限启动修复可继续，未执行它、未预填 trial-02 的成功、用时或科学结果。完整独立乘法复算、其余张量、Leray、连续残差及原 NS 结论均不在这里获得认证。

## 5. 实际输入绑定

以下绑定本轮实际阅读或仅流式 SHA 核对的文件。节点三文件属于后一类；未解码数组。源码差异以失败 run 的旧源码 SHA 及上述逆替换验证连接，不更改失败记录或制造一份新的“原始”证据。

| 实际输入路径 | SHA-256 |
| --- | --- |
| `research/reverse/fixed-seed-global-screen/KRONECKER_STARTUP_RECOVERY.md` | `77d26c82f4a7a571543628488457e26289d96d5c2b380000944eecf407ac17bb` |
| `research/reverse/fixed-seed-global-screen/KRONECKER_BLOCK_CONTRACT.md` | `d8077701b347d35045d7f59ab39669a9e6bf07f6753db386e3d052dc8ab5ada3` |
| `research/reverse/fixed-seed-global-screen/audit_kronecker_block.py` | `b4d65f5a02211ff52f1a202b4e9ba25e9cee47e5a9468bb3a670aa5c381a5c08` |
| `research/reverse/fixed-seed-global-screen/kronecker-block-trial-01/run.json` | `44d05321296a6b25b3997495601cc9623a8fd6562b6dfd13f08dedcbbd99fcbc` |
| `research/reverse/fixed-seed-global-screen/kronecker-block-trial-01/RUN_CLAIM.json` | `a445afd5f6bf925e0124c238156a0dccc36a707ccb76b17f53b23a6da36a2172` |
| `research/reverse/fixed-seed-global-screen/kronecker-block-root-run.log` | `7874ccd7a971d6ff5b6dcf7126daf31e62f8c5dc0ccd0c684f12cab893b09b0c` |
| `research/reverse/fixed-seed-global-screen/node-trial-01/manifest.json` | `5ac2abdfb7a14a38904f2ef1c58d81cf90bea776ce5426a56a75c6f81622c1cd` |
| `research/reverse/fixed-seed-global-screen/node-trial-01/modes.npy` | `f184c97c52e561ac53b8936ee51e68690517ad65c79e8050c93a891ac8856896` |
| `research/reverse/fixed-seed-global-screen/node-trial-01/block-01280-01343.npz` | `abf3b33282ff0b08e995c6aa1f80e7d79dbd64a55137574b77d51356b236297e` |

本次 PASS 是失败归因、字节修复及恢复范围审查，不是 Kronecker 科学核的执行证书。
