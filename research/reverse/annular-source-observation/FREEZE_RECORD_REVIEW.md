# 冻结证据元数据复审

2026-09-09，PRIVATE_CORE。结论：PASS，仅限本次根清单、来源绑定和范围陈述；未发现待修冲突。

本人是 compare_trajectories.py、archive_trajectory_data.py 作者，并有前序输入核验、独立参考及观测接口经历。本次是非作者根清单审读，不是第三份独立计算、全课题盲审或人类同行评审。

实际全文读 SOURCES.md、ROOT_FINAL_ACCEPTANCE.md、trajectory-acceptance.json；完整解析 certificate-manifest.json 全量清单、两归档 manifest、轨迹归档接纳及 Git 保全记录，定向读五路原 result/receipt 元数据。未重新审读全部旧科学正文。

证书为197项核心和14项直接依赖，路径规范、存在且无重复；四处顶层绑定与清单一致。153个非NPZ/gzip文件实际读取字节并核 SHA/bytes；58份gzip仅核文件大小及已存SHA映射，58份原NPZ同样仅stat大小及核回执映射，没有再次读取数组字节。

58组还原行与旧6份、新52份归档记录一一对应，原件路径、原SHA/bytes、gzip路径及SHA/bytes均一致；gzip全部列入核心、原NPZ未误列Git核心。52份选择与完成行对应，四组9/9/17/17及其字节合计与保全记录一致。Git blob验证仅引用根的已有记录，本次未调用Git或验证未来冻结对象。

接纳记录的10个科学worker（输入2、资格/成本3、轨迹4、比较1）、166194次标量三维FFT、0重跑及全部closed，与证书字段一致；这些科学数字是转录核对，未独立重新计算。五路原回执/结果的PASS及已列完成计数匹配；比较4组、44对完整检查点、1284对标量节点和0次FFT仍是原比较程序记录。

新归档原记录为52份逐件流式还原通过；本人未重复gzip解压。其63.18366670794785秒截止于manifest序列化前，SELF峰值30113792 bytes为Darwin进程峰值，未扩写成完整生命周期或并发总峰值。旧归档只保留自身原有计时字段，不补造RSS证书；归档不计新科学worker。

SOURCES、根接纳及JSON范围均保留：q36输入不替换原初值，成本后段状态非真实U(a)，结果仅固定Galerkin的NO-CANDIDATE观察。实际NS至T延续、连续时间重建/误差、全窗H³、历史求值误差、真实非零和真实门排除均未付；没有升级为再生、无限尺度、奇性、严格舍入或形式机器证明。

原pending/formal_release标签按形成历史保留，不能抵消后续已存有限接纳，也不能扩大接纳范围。本次没有科学执行、数组解码、重复还原、Git或外发；本稿不自绑定，之后冻结对象由根另核。

| 实际读取来源 | SHA-256 |
|---|---|
| SOURCES.md | b19b4a8111ed56be994560898435a43d3819749558151f7c4c9454286dd0ec87 |
| ROOT_FINAL_ACCEPTANCE.md | bd4b6f1c11f23ed2dbed26fc9926e91feb1ea09744419a3753c9dbdc0e32dead |
| trajectory-acceptance.json | f5f9ec5edf31670b013288f753058cb2ef2ad20fad6c398727c6a2b1cd8835e7 |
| certificate-manifest.json | da4a85988a1b862e88c01b630dc910523f9b0c421e30c261d6d38663acebce0c |
| numerical-data-archive/manifest.json | dd68302f7125cc7de04e26aa7c526a2bad9ea7de31f90b3c59fd2ec08f72bd9a |
| trajectory-data-archive/manifest.json | 3b6405f0b35983a0906dc4838e0d5d2b769ffbf07f7bb5ac1e528db7763e1f61 |
| trajectory-archive-acceptance.json | 4ed22a75d682107e11597057736227221276aa7c10379eb1963290016079013c |
| trajectory-data-git-preservation.json | 53b35bc384bbe1a60238f6719d158badd0b7bcafa7d415d1258bfbd84c73367f |

以上结论依本次实读与元数据核验范围形成；已全文自读本稿并停止修改。
