# 固定旋流包的历史与来源边界审计

2026-09-07。PRIVATE_CORE。独立来源/历史审查；不是数学全文审查，不代替 Rawls 对最终证明和常数的复核。裁决：**PASS FOR BOUNDED ATTRIBUTION AND SCOPE；NO NOVELTY CLAIM。** 本报告绑定下列实际草稿字节，后续改稿不自动继承审查。

本轮复用已经冻结的同一个球形旋流形状 W。其局部对流旋度和非零点也有直接冻结先例；不能把这些重新称为发现。当前对象改为一次固定初值产生的真实周期 NS 短时解，因而不是旧 NON-NS 路径的又一次残差判否。原模板反馈为零这一现象另有 first-cycle 的更强恒等式先例。中心应变公式在本次定向历史检索中没有定位到相同旧命题，但这个未命中不支持领域新颖性或优先权。

## 1. 实际阅读和检索范围

本轮全文读取本目录 CONTRACT.md、CENTER_STRETCH_CONTRACT.md、INDEPENDENT_DERIVATION.md、LOCAL_REMAINDER_DRAFT.md、CENTER_STRETCH_PROOF_DRAFT.md、CENTER_STRAIN_DERIVATION.md。这些对象均使用同一次固定 δ=1/100、ν=1、无外力和 T³=(R/2πZ)³。主模板门与中心拉伸门分别保留各自合同，没有把后者解释为前者成功。

历史方面，全文读取 first-cycle/SOURCES.md、exterior-pressure/PROOF.md、OUTCOME.md 和 RESCALED_EXIT_PROOF.md；定向读取 first-cycle/PROOF.md §1–2、§5–7，JOINT_TEST_PROOF.md §6–7 并核对其对象/依赖段。对旧来源台账中的“已读原文”只按历史记录处理，不把该记录里的全部文献算作本审计重新读过。已实际核对两个旧 freeze.json 中下文四份证明的字节哈希，与当前文件相符。

继承史检索仅覆盖 public/notes/r0-1.html 至 r0-20.html，以及 research/ 顶层匹配 r073*.md 的262份 Markdown。前一组提取全部标题并检索相关标题/段落；后一组作定向关键词检索，再读取相关命中和 R0.73Y、Z-B 的指定命题段。没有把262份文件称为全文通读，没有扫描其图档、数值数据、PDF或全仓文件。R0.1–20/R0.73 的整体路线分类复用 first-cycle/SOURCES.md 的既有有界台账，不在这里重新认证它们全部证明或证书。

实际两组检索式如下，大小写不敏感。检索是文本定位，不是科学数值实验：

```text
swirl|旋流|球形|球对称|中心应变|center.{0,20}strain|central.{0,20}strain|toroidal|poloidal|模板回[馈饋]|template.{0,12}feedback
旋流|涡核|球对称|toroidal|poloidal|spherical.{0,20}swirl|spherical.{0,20}vortex|curl.{0,10}psi|3P.{0,15}tr|1,-2,1|1, -2, 1|1/20|1/800
```

## 2. 直接复用和真正不同的对象

| 当前内容 | 实读历史定位 | 可以复用的内容 | 不能迁移的结论 |
|---|---|---|---|
| W=curl(ψe₂)，ψ=h((1/20)²−|y−(3/2)e₂|²)，h(s)=exp(−1/s) 的平坦延拓 | exterior-pressure/PROOF.md §4，式(7)及 J_W 定义 | 完全相同的光滑、实值、无散、零均值、非零固定形状与支撑 | 不是新初值形状；旧外环的尺度族没有认证真实可达性 |
| 原始对流为纯径向，curl((W·∇)W) 有方位分量；y*=(1/40,61/40,0)，q*=(1/100)h′(1/800)h″(1/800)>0 | JOINT_TEST_PROOF.md §6，132–148行 | 同一个局部代数及非零见证；当前 n≠0 使用它经过固定缩放、符号及 Leray/旋度恒等式后的结果 | 不应把同一个 q* 又记作新数值或新几何；旧时间路径的 R≠0 不代表由当前 a 出发的真实解不存在 |
| 完整周期压力、G−Φ 的光滑修正及四阶核 | exterior-pressure/PROOF.md §1–2、§4–5，式(1)、(8)、(14) | 复用周期 Green 定义、压力符号、四阶 Newton 核与 M_G 的原定义 | 旧外场在原点离源的 H_W=diag(−η/2,η,−η/2) 不是当前涡核中心的应变公式 |
| 固定外形在真实解中的持留限制 | RESCALED_EXIT_PROOF.md §1–5 | 已有真实 NS 条件定理；局部 C³ 持续接近固定 V 时，一次对数时间持留受限；压力取旋度后精确消去 | 不能称此前只有静态或 NON-NS 计算；该定理没有求出本轮 a 的初值导数或模板配对，也不限制全部再进入次数 |
| 当前完整局部解、m=P_Mu，m′(0)=n≠0，模板反馈 O(t³) | 当前 LOCAL_REMAINDER_DRAFT.md §1–4 | 针对这个已固定 a 的完整 Wiener 压缩构造和显式解析余项；无限频率从开始即保留 | 不是沿用旧 u_app 的时间律；不存在将其人为缩放路径默认为真实 NS 演化的步骤 |

旧 JOINT_TEST_PROOF 的路径同时含内核和三个外壳，并反求幅度以满足能量；当前 a 是单个缩放归一化 W，没有那些另行指定的时间、内核或外壳。两者的初值也不同。“各自有一个固定允许初值”不能抹平这一差别。旧非 NS 路径不是真实轨道，本轮解则必须由完整局部存在证明产生。相反，RESCALED_EXIT_PROOF 已经是从真实方程推出的条件障碍，不能为了强调本轮而删去这项先例。

## 3. first-cycle 的精确碰撞：本轮标量零值的现象已有先例

令 a_cyc=2(cos x₃,cos x₁,cos x₂)，N=B(a_cyc,a_cyc)。first-cycle/PROOF.md §5 式(16)，224–229行，已经严格给出

\[
 -(N\cdot\nabla)a_{\rm cyc}
 =8\nabla(\sin x_1\sin x_2\sin x_3),
 \qquad B(N,a_{\rm cyc})=0.
\]

这不仅是“反序可能相消”的一般提醒。对这里同一符号约定 B(f,g)=−P_L[(f·∇)g]，周期分部积分还立即给

\[
 \langle a_{\rm cyc},B(N,N)\rangle
 =-\langle N,B(N,a_{\rm cyc})\rangle=0.
\]

所以“第一代自作用对精确原模板的这个标量反馈为零”在旧循环初值上已由更强的全场恒等式蕴含。当前不应把这个观察原则、Leray 压力吸收或模板零门一般现象称为首次发现。

但两个具体命题并不相同。旧式是特定三角多项式初值的三次向量场 B(N,a_cyc) 恒零；当前证明的是不同球形旋流初值的五次标量 Q=〈a,B(n,n)〉为零，所用关系为 curl n=γa。当前没有证明 B(n,a)=0，不能借旧循环场的结论补上它，也没有证明 B(n,n)=0 或 P_TB(n,n)=0。这里的次数仅说明代数对象不同，不是一项新增 Taylor 阶计算。

本轮可准确记载的包内增量是：把同一类型的标量筛选施于已经固定的 W 初值，保留完整周期压力，证明 n 确实是此真实原解的第一代，并给出正时间 O(t³) 配对余项。这是一个新的有界应用对象，未据此主张新的通用再生障碍。

## 4. R0.1–20/R0.73 的定向去重结果

| 实际定位 | 历史内容 | 本轮边界 |
|---|---|---|
| R0.7，public/notes/r0-7.html 529行；R0.10，r0-10.html 263–278、481行 | “球形”命中都是 Fourier 变量中的频谱包或球形频率叶 | 不等于物理空间中的紧支撑球形旋流 W；不能仅凭相同形容词认定相同命题 |
| R0.8，r0-8.html §coordinates，335–369行；§identities | 有限蝶形 Fourier 网络已研究涡量拉伸，观测为全域分量积分 ∫ω_j(ω·∇)u_j | “检查涡量拉伸”这个研究手段已有；并非本轮固定 x_c 的 Π′(0) 或球形核中心公式 |
| R0.13，r0-13.html 234–250行 | (1,−2,1)/3 是一个输入波矢的偏移 | 与当前 diag(1,−2,1) 的中心梯度形状只是字符碰撞 |
| R0.1–20 的标题与 first-cycle/SOURCES.md §2–3 | Fourier–Leray、局部/非相邻作用、相位、泄漏、等长门、完整树与有限参数极值已反复研究 | 本轮没有重获“必须保留全部作用”这一原则；这些历史也没有按当前球形旋流合同直接给出所需结论 |
| research/r073v_claim_source_ledger.md V16，31行 | “centered pressure--strain coefficient”指中心化滤波协方差，且是选定输出系数 | 不是空间涡核中心的应变；其 selected coefficient 与 whole field 的边界提醒仍适用 |
| research/r073y_exact_shear_no_go.md，开头范围段、Theorem 1.1，66–113行；§4 | 精确热剪切的两个热滤波生产量 Π_s、S_s 为零，而正梯度协方差非零 | 已有“观测零值不控制正量或全方程”的明确先例；Π_s=−τ_s:∇P_su 不是本轮 Π(t)=ωᵀS(u)ω，也不是 Q |
| research/r073z_pressure_active_kernel.md，Theorem 2.1；§5，436–465行 | 压力活跃的二维精确零生产族，以及不按纯热流演化的三维循环快照 | 初始/瞬时几何核与真实轨道不变性必须分开；其两模/三模场都不是当前 W |

上述精确对象关键词在指定语料中没有定位到相同的球形旋流 Q 恒等式或中心公式 ∇B_R³(W,W)(b)=g₀diag(1,−2,1)/5。检索中的 1/20 等其余数值命中是谱隙、图范数或自相关系数，不支持对象一致性。本结论严格是有界未命中；不同符号、未检索附件、旧证明中未显式写出的推论及外部文献仍可能包含相同内容。尤其第3节已从旧全场恒等式提取出直接相关标量推论，说明关键词未命中本身不等于数学去重完成。

## 5. 当前中心应变结果的来源与适用范围

CENTER_STRAIN_DERIVATION.md §1–2 及 CENTER_STRETCH_PROOF_DRAFT.md §2 使用 W=c(|z|)Az、A²=−P、P=diag(1,0,1)，把完整全空间 Leray 投影化为径向 Fourier 积分，再用球面二、四阶矩得到

\[
 \nabla B_{\mathbb R^3}(W,W)(b)
 =\frac{g_0}{5}(3P-\operatorname{tr}(P)I).
\]

这是本包自给步骤的初等向量/Fourier 推导，球面矩常数在稿内计算。它不需要某个未读“涡核中心公式”作为黑箱，也不能被称为全体涡核的通用定理。球形径向权重、固定轴、完整投影与紧支撑/快速衰减是实际条件。

本轮新增的 M_G<2 是对已冻结周期 Green 修正的显式粗界，来自四阶像和、完整81分量界和整数壳尾部比较；四阶 Newton 核本身已经冻结。其角色是对已经选定的 δ=1/100 确定压力修正不会翻转中心符号，不是事后以“取足够小尺度”换一份新初值。这里没有把旧外场探针原点的压力 Hessian 符号，移到速度支撑内的 x_c。

Π(0)=0、Π′(0)<0 以及 Π(t)<0 的严格正时间段分别依赖中心局部代数、完整周期压力修正、黏性中心对称梯度的精确消失和同一原解的二阶时间余项。这些合成步骤的实际正确性由另一个全文审查支付。本来源审计只确认其依赖写出而未援引不相容的模型。

“中心压缩”限于固定观测点 x_c 的涡量拉伸标量和规定初始时间窗；它不是全空间符号、所有位置、所有时间的结论，更不是全局正则性。初值在小球内具有连续轴旋转几何，也不意味着整个固定三维环面及其非局部压力具有相同连续旋转不变性。不能从初始几何直接套用一个未经检查的轴对称全局定理。

## 6. 原文账目、量词和最终可用表述

本轮新增结论的证明路线自包含于周期 Fourier/Leray 代数、球面矩、热核估计和完整 Wiener 局部构造。使用通常的 Banach 压缩原理等基础分析工具，局部存在及时间余项的具体估计在稿内支付；没有新增外部 NS 分类、奇性排除或自相似定理依赖。因此本审计没有启动新的外部文献检索，也没有新增外部原文阅读记录。

first-cycle/SOURCES.md §6 中的 Tsai 1998/1999、Kishimoto–Yoneda、Tao 等条目是以前的已读来源账目。本轮不是精确后向自相似路径，不从 Tsai 的定理导出当前模板或中心结果；未读过 NRS 原文，不能将 Tsai 对 NRS 的转述或任何本地引用计为 NRS 原文核验。R0.73Y/Z-B 所列外部文献同理：这里只读了本地命题以定位历史对象，不继承其“本轮已读原文”身份。

最终表述应保留：

- a、δ、ν 和环面固定一次，u 是由它产生的同一个完整真实局部解；两个门检验各自的量词以 CONTRACT 和 CENTER_STRETCH_CONTRACT 为准。
- n≠0 不等于再生成功；Q=0 只否定指定二阶领先模板门，完整 P_T 场和高阶、晚时反馈均未判定。压力仅在全域配对中因自伴性/分部积分消去，不能声称 a·B(n,n) 逐点为零。
- 中心正时间负拉伸不证明奇性机制被一般排除；不自动追算更高时间阶、更换径向形状或扫描尺度。
- 没有统一可迭代机制、固定初值无限尺度、跨代无限维误差、有限总时间或有限时奇性证明。不得把 ∀N∃u₀,N 换成 ∃u₀∀N。这里也没有通过有限截断替代真实方程。

可用阶段措辞是：“复用固定旋流形状，对同一真实 NS 短时解完成指定模板反馈与涡核中心拉伸的有界筛选；该模板门失败，指定中心初始时间窗中的拉伸为负。两项均不裁决其他再生成机制。”这仍须以最终数学全文审查通过为前提。没有领域新颖性、优先权、完整构造或 Clay 主张。

## 7. 实际输入绑定

下方由本次实际文件读取生成。逐文件 SHA-256 绑定被直接用于本报告的对象；另以排序的相对路径和原始文件 SHA-256 绑定完整定向检索语料，避免将有限关键词检索标成全文审读。哈希只认证所指字节，不认证定理。没有运行 PDE、参数扫描或数值积分；本审计的 Python 只用于文本标题提取及文件哈希。

```json
{
  "schema": "source-history-input-binding-v1",
  "generated_at_utc": "2026-09-07T14:17:28.799428+00:00",
  "worktree": "/Users/kasifa/Documents/Math/navier-stokes-reverse",
  "directly_used_inputs": [
    {
      "path": "research/reverse/swirl-regeneration/CONTRACT.md",
      "bytes": 2285,
      "sha256": "c887d8cc20495f0cf2e80585e66f92663f82c605f923194d49df5dda44bc9e12"
    },
    {
      "path": "research/reverse/swirl-regeneration/CENTER_STRETCH_CONTRACT.md",
      "bytes": 1424,
      "sha256": "4502487b1379740ea169e1e5d5f5faffd5e7c1d8ecd225dfd19516be7c574280"
    },
    {
      "path": "research/reverse/swirl-regeneration/INDEPENDENT_DERIVATION.md",
      "bytes": 8701,
      "sha256": "1ee6495178a4d6def57e733765ae0b778a3c90abf3456c352776c77e6db39581"
    },
    {
      "path": "research/reverse/swirl-regeneration/LOCAL_REMAINDER_DRAFT.md",
      "bytes": 5383,
      "sha256": "c0346e98e776e7a5526727fde1572f1fc543d66b8fd3c31450ca791ea7297f8c"
    },
    {
      "path": "research/reverse/swirl-regeneration/CENTER_STRETCH_PROOF_DRAFT.md",
      "bytes": 6262,
      "sha256": "1eaf197ab6c8b443792cefadfbaac3d96bad3771a281fded32ca2d15d5c92283"
    },
    {
      "path": "research/reverse/swirl-regeneration/CENTER_STRAIN_DERIVATION.md",
      "bytes": 10837,
      "sha256": "65dcbe9cbafffc13289cb774426f6e18bf7edab230bb03324a7ea894f01c3bcc"
    },
    {
      "path": "research/reverse/first-cycle/SOURCES.md",
      "bytes": 15374,
      "sha256": "53fa41805fa419f49a6ad5b3cf5b89b9649c1f59b4e94601049bf0672ea9257b"
    },
    {
      "path": "research/reverse/first-cycle/PROOF.md",
      "bytes": 14336,
      "sha256": "a87672a035f1c80a0225ce8956fca53ffc2eb07fdd4e83092505b4ac657f6120"
    },
    {
      "path": "research/reverse/first-cycle/freeze.json",
      "bytes": 5904,
      "sha256": "e00899dc38023cdddf3336c2b527d30dd24f99191b426753f9995d6889ebe081"
    },
    {
      "path": "research/reverse/exterior-pressure/PROOF.md",
      "bytes": 10163,
      "sha256": "50df7a60076567acac9cbad6588132c3e0f49e77f84f17ee68e740a8a32478b9"
    },
    {
      "path": "research/reverse/exterior-pressure/OUTCOME.md",
      "bytes": 3212,
      "sha256": "17024e2a79907d19f6d25c2d3261f58b899f9f269626f30cb841e22ccd301d7e"
    },
    {
      "path": "research/reverse/exterior-pressure/JOINT_TEST_PROOF.md",
      "bytes": 8081,
      "sha256": "9d0100f62ec6ef25ef2552348120d2b7b1e802aba49167bf4115edad02a3cd91"
    },
    {
      "path": "research/reverse/exterior-pressure/RESCALED_EXIT_PROOF.md",
      "bytes": 4565,
      "sha256": "e96f1bce6d2076d560191211e208bd43f33e0db2d5c21de8abc6dfd31b361e78"
    },
    {
      "path": "research/reverse/exterior-pressure/freeze.json",
      "bytes": 12310,
      "sha256": "71e22006160b590fec66908265f644f8749894cd96ab8df6a4d26e7153e782db"
    },
    {
      "path": "research/r073y_exact_shear_no_go.md",
      "bytes": 21563,
      "sha256": "2574f2caf19248a17d25f811488db1c7b30295efd07e59852c3afa17cf8f69e4"
    },
    {
      "path": "research/r073z_pressure_active_kernel.md",
      "bytes": 12375,
      "sha256": "faa6e2e475e7ce4f5663a0cc13647a14f414157abfae4b9582ced56726f86a68"
    },
    {
      "path": "research/r073v_claim_source_ledger.md",
      "bytes": 13118,
      "sha256": "e060fe21a58c1d1da2a1fd3edd35cedb52f1ef2ced6c4ea75e1977b526d24c86"
    },
    {
      "path": "public/notes/r0-7.html",
      "bytes": 32919,
      "sha256": "009f6f14cc220315da02f1c512fc0d897a223af655ec7c89a89da4198eea5d31"
    },
    {
      "path": "public/notes/r0-8.html",
      "bytes": 31614,
      "sha256": "2b33d5a6f7d44f8eb78abbed8e9f4b24cbcd48d5c83f62d1f302ec6e2f5481a2"
    },
    {
      "path": "public/notes/r0-10.html",
      "bytes": 31861,
      "sha256": "d7566fd57a4b8198a866ff3d317ef15bcd1b6671054c964f8875b00635145a0a"
    },
    {
      "path": "public/notes/r0-13.html",
      "bytes": 31105,
      "sha256": "e5ad43432fb040c60aa51a3716bdd1b606c297f47df45e60722ae7e83903675e"
    }
  ],
  "search_corpora": [
    {
      "selector": "public/notes/r0-{1..20}.html",
      "read_depth": "targeted_text_search_not_full_read",
      "files": 20,
      "bytes": 595274,
      "manifest_sha256": "4af845d22fb59242a58fd7cd106e7046a9145d9d1dabdf6888a83e37861ee346"
    },
    {
      "selector": "research/r073*.md (top-level only)",
      "read_depth": "targeted_text_search_not_full_read",
      "files": 262,
      "bytes": 2823704,
      "manifest_sha256": "d5b21ec6bca411d5e05fde46c585a471b1711ee526f785e965a6ec82d276ebbe"
    }
  ],
  "corpus_manifest_encoding": "UTF-8/ASCII JSON list of {path,bytes,sha256}, sorted by relative path; json.dumps(records,ensure_ascii=True,sort_keys=True,separators=(comma,colon)); no trailing newline",
  "external_originals_newly_read": [],
  "new_scientific_computation": false
}
```
