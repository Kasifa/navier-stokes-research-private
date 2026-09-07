# ReverseNS-20260907-DriverDominance

PRIVATE_CORE。固定完整NS原解中的正时间驱动比较：新生频谱在指定目标上的净贡献更大，逐通道绝对占优却严格失败。这个局部结果尚未给可迭代再生成、撤种子或奇性。

正文 `PROOF.md`；合同 `CONTRACT.md`；结果范围与下一步 `OUTCOME.md`；历史去重 `SOURCES.md`。源码、证书、独立审查和冻结清单都只用于私有归档。

从专属反向树运行：

```sh
python3 research/reverse/driver-dominance/driver_certificate.py --check
ruby research/reverse/driver-dominance/independent_driver.rb --check
```

本轮没有四阶扫描、PDE时间步仿真或科学图。程序只复算有限代数和连续证明的参数条件。最终独立审查与逐文件哈希见 `independent-final-review.json`，科学/冻结提交与完整清单见 `freeze.json`。
