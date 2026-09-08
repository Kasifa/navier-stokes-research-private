# 耗散控制低输出截断缺陷：有界历史去重

2026-09-09，PRIVATE_CORE。本轮只查既有接口，不证明新估计、不给常数、不开科学执行。根先披露拟研究的遗漏配对及 K−b 思路；本人有前阶段来源、能量与数值审读历史，不称盲推导。结论是：已有三项基础接口可复用，但本次限定检索未定位到完整相同的低输出耗散累计接口；这不是全树或外部新颖性声明。

拟审对象仅为同一原解的有限目标带 H⊂{|k|<b}、b<K 上，P_H[B(u,u)−B(P_Ku,P_Ku)] 的热累计；P_K 为坐标立方投影。根给出的“两输入均在 max|p_i|>K−b 尾部”目前在本稿只登记为下一合同待核几何，未在本轮证明或用来计算新界。

以下三项是最接近的已存精确接口；路径均相对于 research/reverse：

| 旧接口与实际读取段 | 可复用内容及不重复范围 | 当前文件 SHA-256 |
|---|---|---|
| fixed-seed-global-screen/SOURCE_PREFLIGHT.md：1–110、155–180；重点 S.1–2 与159–178 | 对精确 Galerkin 轨道，旧 Lemma 6.8 接口为 e_G=−(I−P_G)B(u_G,u_G)，漏出支撑 dG=(G+G)∖(G∪{0})；数值重建还须付域内 ODE/重建缺陷。它控制近似场的完整残差并经控制函数传到真解，不等同于本题用真实 u 定义的输入截断差。 | 9328d3b37fa35989149c02d9097f4c3279f5f366636c91eb1b6d79ef3c650192 |
| annular-source-observation/OBSERVATION_ERROR.md：72–170；重点 OE.6–10 | 已有完整有序 Leray 系数界 ∣B̂(f,g)(k)∣≤∣k∣‖f‖₂‖g‖₂、有限输出热核及历史误差积分，保留复相位和两有序交叉。旧应用输入为固定有限环带；本轮不将它自动改称无限尾输入的已审新定理。 | 5823a2e03e4e176eb2ab444f58fce1797ebef6aafc5f84ada594b359e44c1b05 |
| received-state-reuse/PREFLIGHT.md：70–203；重点 RU.15–20 | 同一 C3 原解中 h/z 两份能量账的交换项反号，相加恢复全场能量耗散；适用已有经典区间、归一化 Haar 范数、ν=1。它未给尾部受限配对的低输出累计，也未将外场全部归为初始种子。 | ec8b135412146869a68e12791f6b0d91cc38e93c4ce3510b41b3a8bf75a44462 |

明确的非适用命中：route-screen/ENERGY_SCREEN.md 第1–100行，尤其 E.3–4（48–71行）的有限模式数自作用/黏性比较，不能赋予未知完整原解尾部稀疏性；它不是本题需对无限尾配对求和的耗散界。该稿 SHA 为 12e1ad7ec85b2e46c91bc6dc525c88d4ab688ffcd1b556ab96004125573ec6cc。

继承 R0.73 的定向结果如下；只用于排除关键词同名造成的误用，不作为第四项新候选公式：

- research/r073o_global_orbit_stability_proof.md 实读1–72、230–278行；其中“finite tail”是预先全局强解在晚时刻后的 H⁴ 时间积分尾，不是坐标频率尾。SHA 1cf123b6a44f35e85156278d9d38a01abf4ec6cc1868c014268f38aa96a81a44。
- research/r073q_heat_flow_stability_proof.md 实读1–110行；“translated tail”是已假定全局强解的时间平移，不能支付当前原解存在至任意观测终点。SHA dba6d93ba3be0837f014b8f157afb8a7a6175ac6312e09cc3d10afdfc17fa1be。
- research/r073r_lp_caloric_certificate_proof.md 实读273–298行；该段要求删 Fourier 尾另给界，没有提供本题真实 u 的截断差累计。SHA f1d1377b502ff736ee9bedb2572c553255600d061612a4d4590da66a091b0eee。

搜索界限：先对已知 SOURCE_PREFLIGHT、OE、旧环带合同草案和 ENERGY_SCREEN 作关键词定位；再仅在 fixed-seed-global-screen、route-screen、cyclic-sum-chain、cross-edge-source-gates、received-state-reuse 的 Markdown 中搜索 tail/尾部/耗散等，每文件最多返回3处。另作 R0.73 文件名清单，定向搜索上述 O/Q/R、H 的 harmonic_energy_proof 和已知 Z 的 pressure_active_kernel；H/Z 未用作数学来源。没有全库全文扫描。

定位路径时只看 cyclic-six-carrier/SOURCES、cyclic-six-carrier-preflight/PREFLIGHT、four-leaf-preflight/HISTORY_SCOPE 中的 rg 命中行，未重读其全篇。三文件当前 SHA 依次为 b92dba7deca47304a1f308f1389932a5a2a67ea4986203a16380d324567c9074、39cabe5efa8e32f7475bd9974bc91bfa38a0db16cfb7b3c4c87cd91977a8437f、2defac57333290c574f9cb1f1e16adb4905d1baa918a6d513fd023faf847b19d。旧后验原文只按 SOURCE_PREFLIGHT 的实读记录继承，本轮未打开 PDF 或重证其外引常数。

有价值但尚未支付的有界对象：在已有原解区间，先严核立方边界、有限输出、遗漏有序对及其重数，再把准确受限卷积接到原能量耗散，明确时间累计范数、热权重、ν 和端点。若最终只是旧估计的直接应用，应登记为应用接口，不另称新一般定理。此处不预判该界足以分离已观察门的误差。

尤其，此缺陷仅比较 u 与自身 P_Ku；即使它的累计获得控制，也不控制 P_Ku−v。后者仍涉及初始近似差、保留域内非线性轨迹误差及数值时间重建缺陷。不能把两种差混作一个残差，也不能以本项替换 OE.1 的全窗真实存在/状态证书或来源历史和评估误差。

本轮没有重开 LocalPressureScreen、早期 T2 树或新数据搜索。只写本 HISTORY；无 NS 轨迹、FFT、数组/常数/参数求值、科学程序导入/运行/编译、Git 或外发。全文自读后停稿；后续是否立项由新有界合同决定，OPEN / NOT CLAY。
