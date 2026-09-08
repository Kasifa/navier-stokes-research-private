# 唯一实现验证与成本执行：原记录范围审查

2026-09-09，PRIVATE_CORE。**PASS，限原记录、来源绑定、执行资源及结论范围。** 三个唯一 run 的结果和监督回执一致，当前 21 项锁源及全部 25 件原产物字节匹配，预定资源界通过；未发现本轮需修订或重跑的事项。这不是第四次科学执行或真实 NS 误差证书。

本人是 numerical_reference.py、条件观测误差及输入核验接口作者，不是主核、worker、监督器或本轮运行作者；不能称全流程盲审或另一套独立科学复算。本次未读 numerical_kernel.py 源码，未导入 NumPy／参考／核、执行科学代码、解码 npz、FFT、重求科学量或访问 Git。

实际全文读执行合同、原 347 行监督器及最终 395 行 worker；又读最终监督器新增的 11 行及周围控制流。只在内存删除第 141、243、302–309、334 行，余字节 SHA 恢复为原已全文读的 349b12877cf4e59f21079cfd0a2d10e3531173e7d51397f9667df4a868f73ad4。最终 358 行源的父子身份、调用数和完整起终源映射门均已纳入回执及成本 validation 先决门；没有改盘或执行源码。

结果到达后，全文读三份 result.json（596／195／195 行）、三份 execution.json（435／411／411 行）及九份 progress/stdout/stderr。另定向读两份高和频准确参考输出、三份参考的有序对计数，以及 toy 两 phase 的初值／速度四 stage／终点和边界、改变 G 的原记录；没有逐式复证全部参考中间项。21 项锁内其余文本和主核仅核字节，不冒称全读。后段全文读 NUMERICAL_RESULT、运行前／pressure 记录及归档 manifest。

| run | worker 次数／退出 | 完整子生命周期秒 | CHILDREN 峰值 RSS bytes | 原目录总 bytes，含回执 | 已存检查 |
|---|---|---:|---:|---:|---|
| validation | 1／0 | 0.957062708 | 989593600 | 157095072 | 44 项，全部通过 |
| bench128 | 1／0 | 1.79805525 | 1173684224 | 110413073 | 3 项，全部通过 |
| bench160 | 1／0 | 2.764673625 | 2144698368 | 206357774 | 3 项，全部通过 |

标准库只做流式哈希、JSON 字段相等、PID、整数计数及资源元数据比较：21 锁源逐件匹配，三个 worker 起终映射、父子身份、单次调用和回收／退出一致；全部产物与回执清单、结果自列产物及含回执总字节一致。validation 的 45 秒／2 GiB／256 MiB 和各成本的 120 秒／6 GiB／1 GiB 均通过。记录没有重跑；旧输入两核和旧 A/B/C 不重新计数。

Popen 前至 wait 后覆盖完整子生命周期。SELF 采样截至源／结果检查后、最终产物哈希及回执序列化前，不是完整父生命周期；父子峰值及两个并行子峰值均不能相加冒充同时峰值，RSS 是 Darwin bytes 的事后验收。成本启动记录的 free=58% 满足预设 40% 门，其 validation 绑定与原文件相同；本人未重新测 memory_pressure。

三份 stderr 均保留同一 248-byte NumPy 配置展示提示，建议安装 pyyaml；未见 traceback，stdout 各为对应 PASS。不能称 stderr 为空。原环境为 Python 3.12.14、NumPy 2.3.5、complex128、双向 forward；18 逻辑 CPU 与线程变量未设置不说明实际占满 18 核。

44 项包含两来源完整小格和全目标带、合成 128 全格及来源、剪切、两 phase 非平凡 toy 和整数边界／历史不反馈。原报告的三种全格最大坐标误差依次为 3.96032326133344e−16、1.9860273225978185e−15、3.826307691200501e−15，固定尺度门通过；本人未从数组再求误差。两份准确参考各有 16 个不同有序对，合成有 64 个；高和频 (13,1,1)、(29,1,1) 的原准确输出非零。toy 比较终点三块及四个速度 stage，不能误称所有历史 stage 都另做了数值差检验。

实际整数 FFT 计数为 validation 30 批 API／90 标量三维变换；每个成本 36／108。每个成本的大网格、32³、64³各有 8 逆批／24 逆标量及 4 正批／12 正标量，四 stage 的 start/end 和 RHS 用时记录逐字段一致。108 不是等成本大 FFT，也不是裸 FFT 计时后推算出的端到端成本。

两个成本都绑定同一已核近似输入 3f51705f…，完整 step 对象逐字段相同。worker 从原十二模 hex 及 G=W=0 起点独立嵌入两格，用原 T/256、index=128,nsteps=256；没有跨格串联或另换 a_*。本审查不重新计算步长转换误差。完整 step 为 128 的 1.4676454169675708 秒、160 的 2.3002353329211473 秒，与完整子生命周期严格分列。

**COST_ONLY_NONPHYSICAL_SEGMENT_STATE 必须保留：** 后段分支中的初点负载不是 U(a)，产生的 W 不是原 [a,T] 来源积分，不能据其非零、大小或两格接近接受／否定来源门。能量、边界模量及结构缺陷也只是成本状态诊断。原近似仍负有相对于同一 a_* 的初值误差责任。

当前没有四份正式轨迹，没有动态大立方边缘测试、完整 160 格独立 RHS 数值参考或独立环带成员枚举。原 NS 至 T 延续、全窗齐次 H³ 误差、连续观测／求积误差、实际来源门及非零仍未付。实际成本可用于另锁预算，不能由此 PASS 自动启动轨迹或保证长时间成本；NOT CLAY。

下列均为本次实际 hash；三原目录的完整清单包含回执，定义为按 path 排序的 {path,bytes,sha256} 数组，经 ASCII、键排序、indent=2 JSON 加换行求 SHA。原日志、参考和 npz 各自 hash 均由已实核回执及这些清单绑定，不重复展开全部 25 行。

| run | result.json SHA-256 | execution.json SHA-256 | 完整目录清单 SHA-256 |
|---|---|---|---|
| validation | ec959e7f2ab3ac1f96f95bafbd0a13f3ff39748793914e35861d1b80ec3c61fe | 1f200a6d622dd79c515b8aa73e457fbb1089a4679d42d9b844717da217a71ff4 | 1a457a2881d5e1fbcbd4ec4b99d9c15985e8d385d34f8a11e247028c758b6b33 |
| bench128 | 253b55106075cec07f42c74d8a386a46e12a935b8427e75a7766ecaad10dbdb1 | ed8089868b3bcc916b0b66e936a5d7ce5cb7ead48234fb6dac878dbbf2442e8f | f265444718462266e815e286df02427ab774fd2f9aae1b229c3d937e89d140c5 |
| bench160 | 0afbed14a4e863b987c3bf723dda084a891f309a4a2924efebae6919a23fc4f1 | 377af0bb2d4d0657ffd47ab1370e2f099181274ad0b24921528289b521d61f6f | a21e800f69ef05b9b39f703238659be6d9c12d594d7ea4b787d3440b2b8a170f |

| 本目录直接来源 | SHA-256 |
|---|---|
| NUMERICAL_EXECUTION_CONTRACT.md | eee7c787aa17a939da9adb6fdab72a83e053e50d1d3f10e8a757287240382052 |
| run_numerical.py | 0ed3c383fca00253af2970665078be9e390da36fb21c684d67a92b75aeacc987 |
| numerical_experiment.py | f5c4900d33f710e836d09187c5a10bb229d2932c724d2287a05a7259620f8cee |
| numerical_reference.py（本人先前作者全文自读，本轮核字节） | ebc936f5eefd5804ace40c7e821e424aa6b703294ebbe259fbad2c7e4848d46c |
| numerical-source-lock.json | 060e72f189c2b6ecade7b6425509f68c2efb6d056b4f71e25b76c91fdb5ce3d2 |
| numerical-pre-run.json | ab195ce392d69c6cb0ca988638bbffe1a2aa6a41d9bcb7b2f72f5de0ab2e1615 |
| numerical-cost-launch.json | 6876748e8ca981d3a88df7eab7a39561491b7bd899ed9c1dd09ffc13c6541439 |
| NUMERICAL_RESULT.md | e6220f0612140ea64cbdb0b7acd016542cb22de55dc2de321468c695521ebda3 |
| numerical-data-archive/manifest.json | dd68302f7125cc7de04e26aa7c526a2bad9ea7de31f90b3c59fd2ec08f72bd9a |

运行前提交 c8f2712fe0cc06d5ec91c014d5030f7f45889c90 的 Git 对象证据属于根的 pre-run 记录；本人只核其 22 绑定等于当前 21 锁源加锁自身，不声称自行检查 Git 或远端。NUMERICAL_RESULT 当前范围与原记录吻合。

附带归档 manifest 的六份原 npz 共 473387726 bytes、六份 gzip 共 114684498 bytes，原／压缩／回执映射逐件实际哈希一致，原 run 保持不变。本人未读归档脚本、重压缩或重解压；restoration_verified 是根的已读还原记录，不冒称又独立还原。归档不新增科学执行或改变原资源账。

本文件全文自读与最终来源核对后停稿，不自绑定自身 hash，不改原结果、源码、源锁、回执或历史状态。本审查只闭合本合同的实现／成本记录范围，不新增科学结果或轨迹执行权限。
