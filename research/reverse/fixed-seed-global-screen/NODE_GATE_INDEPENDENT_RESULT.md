# 两个固定参照节点的独立执行结果

2026-09-08。PRIVATE_CORE。状态 TWO_FIXED_REFERENCE_NODES_COMPUTED，进程实际退出码 0。这是对已固化整数档案的一次有限精确算术核验，未重新积分，也没有读取、导入或使用根代理审计结果来计算。

执行前合同和源码已先落盘并作静态编译，随后依据根代理的完成授权执行一次。输入 manifest 的预先固定 SHA-256 为 5ac2abdfb7a14a38904f2ef1c58d81cf90bea776ce5426a56a75c6f81622c1cd；运行中实际匹配，并在计算完成后再次匹配。只打开节点 640 与 5120 所在的两个块，未复核其余块的实际数组。

## 节点 640：三阶点值成本靶标被否定

在 t=5/16、x*=(π/2,π/2,π/2)，逐 Fraction 系数共轭平均和 Leray 投影，再直接枚举全部 27 个有序三阶空间指标，得到完整 Frobenius 平方

q =

474203934554459310838411197903302656193746253274734127213484477592895673935334850116112313144006856810782198137876393

/

37771079623803812631796061594411518878216684519747738003712512017820361894938491180399815341387705730215224279040000。

独立阶乘闭式求和给

P₃₂(5/8) =

21675419709545690518569794705957316692032397640010904679971

/

11602016117480102857784191119697601264715744559181737230336。

保存的 qP₃₂(5/8)−16 的整数分子严格为正；完整分子分母在结果 JSON 中。另从实际结果作有理数大小复核，12<q<13 且 7<qP₃₂−16<8。

这独立否定该固定参照在此节点满足 M₃≤4e^-t。计算使用有序指标，没有复用根实现的共同 LCM 分母或多重指标重数。结果保存了全部 4912 个投影后复系数的实、虚分子分母、27 个有序三向量及其平方、P₃₂ 的 33 项及最终 margin。它没有给 M₃ 的空间上界，更没有给原 NS 解的导数。

## 节点 5120：参照终点范数门成立

在 t=5/2，用固定 B=2^80 精度逐模式作有理平方根夹逼，完整正负频谱的结果为

31851828405389920269747 / 75557863725914323419136

≤ A_-1(v(5/2)) ≤

63703656810779840539707 / 151115727451828646838272

< 1/2。

总闭区间宽度为 213 / 151115727451828646838272。结果逐模式保存 |c_k|²、|c_k|²/|k|² 的分子分母、isqrt 上下整数、共同分母 B 与精确平方等号标记；未给全正负频谱再乘 2。

这里只支付参照终点范数这一项。三阶成本靶标已经在较早节点被否定；终点范数门成立不能补回未验证的连续残差，也不能直接使用原先假定该成本靶标的上解。更宽系数的 Y.25 控制是否可行，本次没有检验。结论不涉及原解的存在区间、全球性或有限时奇性。

## 实际执行与证据

实际命令是 bundled Python 3.12.14 -B 运行 independent_node_gates.py，源码未导入根代理模块。完整 argv、工作目录、PID、UTC 起止时间、平台、线程环境、版本与 RSS 单位记录于 run 文件；stdout、stderr 均保留。stderr 为空。

数学计算墙钟 0.830630750162527 秒；结果证据写入阶段另记录约 0.201555 秒。最高原生 RSS 为 103088128 字节。计算没有触及固定 60 秒截止；没有重启、参数变化或附加节点。

本次实际输入/来源共 8 条绑定，计算后逐一再次核对。运行记录中的结果 SHA 也实际复核。该字节检查不增加新的节点算术结论，也不证明独立实现与根实现已经逐项相等；后者需要另行比较实际输出。

下表绑定执行前合同、源码、静态检查、claim、实际输出及所读科学文本与档案。源码中的排他 claim 会拒绝自动第二次运行；需要审读时直接读取现有结果，不重新执行节点核。

| 实际证据路径 | SHA-256 |
| --- | --- |
| `research/reverse/fixed-seed-global-screen/NODE_GATE_INDEPENDENT_RUN_CONTRACT.md` | `56dc24b236fe6eeec1209a121534f9ba01137cb401089b2370055abd30100936` |
| `research/reverse/fixed-seed-global-screen/NODE_GATE_LEMMA.md` | `177fe82983bb8d6d3e172615c716176338bdc7e31cd546e0416b502b80dd76fb` |
| `research/reverse/fixed-seed-global-screen/NODE_PRODUCTION_CONTRACT.md` | `9f2ff230ef8a569c3b3b70f4a8de37aece19db52439227f1269fc53f183e4fb8` |
| `research/reverse/fixed-seed-global-screen/independent_node_gates.py` | `63c4d325af6773fc82c1f2faf9acc86b16fa7b81cc143f7d8f7e7d22e89d6669` |
| `research/reverse/fixed-seed-global-screen/node-trial-01/block-00640-00703.npz` | `0baf9f82b18c9d056a17d5bb7b246f1743ac297650ab5849983da8808a38c52a` |
| `research/reverse/fixed-seed-global-screen/node-trial-01/block-05120-05120.npz` | `2f85a5204ba7af0bd9493d79baa257fc42ec2f9468396df94bad9cf39f88e23a` |
| `research/reverse/fixed-seed-global-screen/node-trial-01/manifest.json` | `5ac2abdfb7a14a38904f2ef1c58d81cf90bea776ce5426a56a75c6f81622c1cd` |
| `research/reverse/fixed-seed-global-screen/node-trial-01/modes.npy` | `f184c97c52e561ac53b8936ee51e68690517ad65c79e8050c93a891ac8856896` |
| `research/reverse/fixed-seed-global-screen/independent-node-gates-static-review.json` | `7192ce0db8062ace0b98d76ec1235ff648c9a6e70681fbeddd68aa424ce13f20` |
| `research/reverse/fixed-seed-global-screen/independent-node-gates-claim.json` | `732009f158185eb9526366631dc0c3a87f7328dc8ee4075678c6eabd335d9ebc` |
| `research/reverse/fixed-seed-global-screen/independent-node-gates-result.json` | `5cf6fcb0cb92e5acbdec208ebf2addc709e069a82e176b17951d2036d90174db` |
| `research/reverse/fixed-seed-global-screen/independent-node-gates-run.json` | `813ef2374f030911e9c9ed43ec74513d9d4d74a2df160de178a59221b745bb6c` |
| `research/reverse/fixed-seed-global-screen/independent-node-gates.stdout.txt` | `cec48642101aaba751716bddc00d4308b401c08d817b02bb16380cc1f729440c` |
| `research/reverse/fixed-seed-global-screen/independent-node-gates.stderr.txt` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
