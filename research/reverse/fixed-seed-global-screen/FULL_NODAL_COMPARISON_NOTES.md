# 完整单节点档案比较器说明

2026-09-08。PRIVATE_CORE。比较器已写入，**尚未执行**。本阶段仅根据两份稳定源码、实际 run/result 元数据的字段和文件名准备；未读取新二进制科学数组，未执行其任何数学比较。后续运行须由根代理全文审源码后发起。本说明不记录预设 PASS。

比较器为 check_full_nodal_agreement.py。默认只显示使用说明；必须显式 --run、两份已冻结 run SHA 及四个外部日志路径。输出固定为 full-nodal-agreement.json，独占创建；已有文件时拒绝覆盖。两核和原输入一律只读，不导入两核脚本、不加载 NumPy、不恢复原节点、不执行卷积或积分。

实际验收逻辑：

- 认证两核固定源码、数学合同/审查、两份根代码审批，以及运行记录中的全部来源和输入。主审批在外部固定绑定，独立审批还须与独立 run 的来源表相同。验证两种配置各自的实际规范化 JSON 哈希、完整24份主二进制和6份独立二进制、独立 result/run 相同字段及实际输出清单。
- 五个新张量各71874个有符号整数标量全部相等并满足共轭。原十五打包乘积只认证已存文件及其来源、尺寸和记录连接，不重新相乘、解包或复证旧打包引理。
- 在完整 H 上比较主 \(V/(Ds2^{192})\) 与独立215622个约分 Fraction 分量；零频为0/1。核全部 V 共轭、无散、S等于六标量平方和，并从已保存分量重新组成完整零阶和有序二阶平方范数。这里重算档案的有限平方和，不是重算非线性或原节点。
- 独立二阶精确平方和等于 A2/H0；独立零阶精确平方和落入主 A0 下上端/H0。分别验证两核根号、原参照的 ±E 范数区间和固定32阶指数有理包围。主零阶外包可能更宽，不要求区间端点同字节；不同宽度可能使一方未定，不能据此误判算术矛盾。两者若给出相反的严格通过/拒绝则拒绝验收。
- M、δ、E 与旧已接受精确记录相同，E 的表达式另作有理核对。原参照 R 仍通过扰动界连接；完整直接对照的场是中心残差 Rhat。节点门只限同一个参照节点。
- 最后连接外部 stdout 末项的 run SHA、完成状态和最终写后资源；实际目录与外部日志字节合计须在64MiB内。记录中的写前快照不被冒充最终目录大小。源码、输入、输出在比较末尾再核字节未漂移。

10个负对照只改内存小对象：来源 pin、缺少输出、张量实部和虚部、残差公共分母和符号、二阶 s²权重、根号真有理等号、E 的下端和上端符号。公共分母控制保持实际非零约分 N/D 不变，将主公共分母改成 common+1，核交叉乘法确实不相等，不仅检测零分母入口。除根号边界外均取实际被比较记录或标量。根号控制明确构造 \(3/(2P^2)\)：缩放后 floor 为1但原有理数不是1；这是微型合成边界，不是对原数据的新测量。负对照不再调用全档案比较，更不会重跑大核。

根代理给出的固定运行调用如下；写入本说明时没有执行：

    /Users/kasifa/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 -B research/reverse/fixed-seed-global-screen/check_full_nodal_agreement.py --run \
      --primary-run-sha256 1f2f85bc1fc2c6e48f37a525c8ce1b790b873be532176cff7f00c9a0b7bb0dd7 \
      --independent-run-sha256 b197dc3cf405e191a7f4b7ca5076e7f04b2c812c22f6610e878972ff9957039e \
      --primary-stdout full-nodal-primary.stdout.log \
      --primary-stderr full-nodal-primary.stderr.log \
      --independent-stdout full-nodal-independent.stdout.log \
      --independent-stderr full-nodal-independent.stderr.log

工作目录为 /Users/kasifa/Documents/Math/navier-stokes-reverse。四个日志参数相对本比较器目录解析。比较结果、实际负对照拒绝数及输出 SHA 只能由后续实际执行产生。任何节点结论均不外推到连续时间余项、原 NS 解或奇性。
