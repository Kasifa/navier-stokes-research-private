# 固定价值侦察 worker 源码形成记录

2026-09-09，PRIVATE_CORE；SOURCE-ONLY，未获运行授权。本人是本 worker 与 DESIGN 作者，非独立代码审查者；既往 BF/RE/FG 作者及旧轨迹审读经历沿 DESIGN 披露。本轮科学 worker 0、数组打开/科学导入/编译/执行 0、Git/外发 0；只写文本、读元数据与标准库 AST 解析。

value_worker.py 最终 539 行 / 28515 B，SHA-256 `ea70c183436f6afa85a9b50bfe75d17f1807acd181fbd0a49c564a3487568af0`。已逐段全文静态自读，末次仅将三处 runtime 键统一为 environment 并读回，以匹配监督回执；随后对最终字节作标准库 AST parse，不执行 AST 或被审模块。

本轮全文读 DESIGN、执行草案、root 派生输入映射和 helper；旧 kernel 定向读 1–205 行（此前曾全文审），停定 supervisor 仅定位相关字段并读 175–220、235–320 行，不重称其全文独立审查。映射阶段已核原 T/M² 文本字段及既有来源，当前未重新打开任何 NPZ/gzip 或重求原根。

| 实际输入（本目录，除另注；SHA-256） | 字节绑定 |
|---|---|
| DESIGN.md | 9c6a9e660f2c1179b2ccf9dd79364b06e1ccfa65912bc9150ee1846325a0d7fd |
| EXECUTION_CONTRACT_DRAFT.md | b44b689db1066ced1632be7fd033ead81fa398b89f1194249190b0b00f0936f6 |
| input-bindings.json | 4285c18b4def69ac450cb0c7f10f44f640aa34ce4364241fdb3dabf2a413ccd6 |
| budget_formulas.py | e16b4a3d5eb32bcb578ebd01731d38a83c7374eec90b500324811d07ea79d883 |
| ../annular-source-observation/numerical_kernel.py | 1b29e919cf5faefe1e4a5193fee0f7e0fdd11901d8aed7b3e5ade752cd23f175 |
| run_value.py（仅上述定向阅读） | 7bd7d434aff19dd004503d400ab0146669d96dec950b3916001583e543b50d2c |

固定 CLI 为 --run-id value-scout-160-512 --output-dir ABS --source-lock ABS；只接受本目录固定唯一输出路径及父拥有的三个初始文件。source-lock schema 1、bindings 的 path/sha256/bytes 与完整起终映射均核；关键旧输入/依赖 SHA 内锁，源锁不允许二进产物后缀。父、子身份及 environment 字段和监督接口对齐，最终锁/Git对象验证仍归根。

运行时才核固定 Python 3.12.14、NumPy 2.3.5 路径与五个线程环境值1；逐份前哈希、NPY头及唯一 U 解码，然后在所有使用结束后逐份后哈希，共34次大文件读取均属于唯一子生命周期。原 T/M² 的映射/主原记录/独立记录须相等；准确节点、h 和各 κ 时差用 Fraction 转换并保存回读差，不以保存态能量替代原 M²。

17个端点逐一 Hermitian/Leray/去均值/保留域投影；N160/K53 完整 rhs 后只保存 H0 值/物理斜率和末端紧凑 C53/H1。全部 signed 标签核对；3K<N 只支付保留域，N216 无 mask 且按整数标签嵌入 C53，4K<216 支付完整 C106。浮点投影及旋转核不认证精确 AP 对象。

16段保存全控制向量、Gram、两组织七项 q 及复端点/物理导数差；helper 调用前核共同全 H0 shape、h>0且有限，返回后核全部有限。64规则只生成一次；Φ分别实际调用64内点及[0,1]，保存同表达式与0、h/49的差，未强写端点值。零 L 不作除法，比较分母0记 null，未添加数值通过容差。

原始派生输出为 reconstruction.npz、terminal-compact.npz、full-B216.npz、quadrature.npz 及 progress/result；完整 B216 保留 C106 外浮点尾，C53 差保留全复向量。FFT包装器实际计数：17次160 rhs及1次216 rhs，对应54批/162标量；计数是调用入口计数，完成还要求所有返回、源/输入复核及17端点验收，不把期望值直接写作完成证据。

显式寿命：每次仅一个原160状态；平均/投影临时随后释放，原 U 在 rhs 前释放，X/B 每端点后释放。小型 H0 序列和末端两份 C53 紧凑向量保留；160工作网格在创建216前删除，不常驻17个完整 U。一个216复向量为483729408 B，紧凑C53向量为58802064 B；这些是形状字节算术而非内存实测。

216 rhs 的显式峰段包括输入、curl、速度、涡量四个全向量，或输入、速度、涡量、乘积及分量乘法临时；投影另有复标量点积临时与输出。rhs 返回即删除输入，诊断逐分量取共轭；完整 B 序列化后删除216网格，才进入小型求积。此寿命组织与 DESIGN 的六向量加六实标量暂存目标相容，但 FFT工作区、序列化、分配器驻留仍未实测，不能保证 RSS≤6GiB。

正常产物采用独占临时、同目录 hard-link 无覆盖发布再移除临时名；科学/序列化失败不删已写原数据或临时证据。序列化失败强制 FAIL，必要时只独占写最小失败 result；不会以已有 COMPLETED 文件覆盖退出失败。worker预留父空间，最终完整1GiB/16MiB封口由监督计入其回执，必须同时核真实退出0、stdout与最终receipt，不能单读worker状态接纳。

当前剩余门：根及非作者源码静审、最终执行合同/完整source-lock/运行前Git、即时free≥40%与磁盘≥8GiB及无并发科学任务；之后才可能授权一次120秒/事后6GiB调用。当前没有运行结果、未知 L/Ū/J 数值或成本实测；未来完成也仅 COMPLETED_NUMERICAL_VALUE_ONLY，不认证单边预算、求积误差、原NS门/寿命或旧连续G/W历史。本文全文自读后与源码一起停稿。
