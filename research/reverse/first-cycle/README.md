# ReverseNS-20260907-TwoGeneration

PRIVATE_CORE。首轮有界问题已经得到两部分结果：一个固定允许三维周期初值的完整黏性原解有严格的有限两代 Fourier 产生；同样的目标观测却出现在全局光滑三角类，且所选三元输出不能直接复制初始模板。因此没有接受可迭代奇性机制。

正文与限制在 [PROOF.md](PROOF.md)；未接受候选的理由及下一项具体问题在 [NO-CANDIDATE.md](NO-CANDIDATE.md)。两代指不同消失阶数和树深度，不指两个分离的正等待时间。这里没有奇性、统一迭代、无限尺度或新颖性声明。

- `CONTRACT.md`：代数接受前固定的问题和无限维误差合同。
- `ALGEBRA.md`、`exact_algebra.py`、`algebra-result.json`：完整有限阶 Fourier–Leray 计算及压力/减种子对照。
- `certify.py`、`certificate.json`：精确有理数检验时间、余项、下界和错误变体。
- `independent_crosscheck.rb`、`independent-crosscheck.json`：不同实现逐系数复算。
- `INDEPENDENT_REVIEW.md`、`independent-final-review.json`：独立 AI 解析审查与最终字节绑定。
- `SOURCES.md`、`sources-evidence.json`：有界历史/原文去重及阅读深度。
- `VALIDATION.md`、运行JSON：实际执行和失败修正记录。

从专属工作树运行（只需系统Python和Ruby标准库）：

```sh
python3 research/reverse/first-cycle/exact_algebra.py --check
python3 research/reverse/first-cycle/certify.py --check
ruby research/reverse/first-cycle/independent_crosscheck.rb --check
```

程序只认证有限系数和解析定理的数值假设。无限维经典解及误差结论依赖正文证明与审查，不能用程序PASS替代。含运行时间的日志不要求逐字节重现，确定性科学JSON要求重现。

本轮没有科学图或大规模仿真，图档清单为空。冻结仅请求及时私有归档；不生成网站读者页面、PDF或公开核心附件。科学与冻结提交、完整文件哈希及依赖见独立 `freeze.json`。单轮局部基准未达到需要全面阶段回顾的里程碑。
