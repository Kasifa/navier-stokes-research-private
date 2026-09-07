# 验证范围与运行记录

PRIVATE_CORE。2026-09-07。

- 主代数：Python 标准库复有理数；每次完整有限卷积，无 Fourier 截断。`exact_algebra.py --check` 逐字节重算 `algebra-result.json`。
- 连续合同常数：`certify.py --check` 重算9项假设和8个负例，检查时间、球半径、残差常数和两个非零下界。它不独自证明连续 PDE 定理；完整证明在 `PROOF.md`。
- 独立重算：Ruby Rational/Complex，不导入主实现；通过物理分量微分/多项式乘法和压力恢复计算全部导数与残差，逐系数比较。最终数量、主证书哈希及环境以 `independent-crosscheck.json` 为准。
- 独立解析审查：`INDEPENDENT_REVIEW.md`，覆盖经典性、完整余项、Duhamel来源、压力、简单不变类、负对照和主张边界。AI代理审查不等于人类同行评审或形式证明助手验证。
- 外部资料：`SOURCES.md` 与 `sources-evidence.json` 声明实际阅读范围；不把继承笔记中的候选状态当已证，不重认证全部历史证书。
- 本轮没有科学图、仿真、远端计算或训练。正式图清单为空；没有待补的PDF/SVG/PNG导出或图像QA。核心量由有理系数与证明直接表达。

保留的修正记录：初次主证书尝试把“删除 B(N,a)”设成应能检出的负例，该项返回false，程序因断言失败而退出。精确核查发现 B(N,a) 全场本来就为零；这不是证书故障，而是本种子的压力相消。该错误负例已替换为删除 C 在六个原种子模上的真实非零反馈，并在主证明加入全场梯度恒等式。未把第一次失败报告成通过。独立Ruby脚本初跑遇到旧Ruby不支持filter_map，已改为兼容写法后从头运行。

冻结前最后一次执行记录为 `run-environment.json`、`verification-run.json` 和独立证书；它们记录实际环境、工作线程、命令、时间及哈希。主证书数据为确定性JSON，含wall time的执行日志不是逐字节重现目标。
