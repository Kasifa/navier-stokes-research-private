# 固定剩余时间热补全：完整解析与残差接口

2026-09-09，PRIVATE_CORE。Gauss（`coherence_independent_resumed`）独立手推合同第1–3项，未读 root 未来证明。本人参与前两题的周期/规范补全推导；合同已披露 root 的热乘子与链式法则预见，不称全课题盲发现。本稿不审第4项实际卷积增长来源，不改原数据、λ、截止或固定 ρ。科学程序、数组、FFT、Lean、新图、Git、外发均0。

**交付范围。** 对同一完整原周期场作固定热操作，能得到全域解析场及“原切片非零 ⇒ 涡量没有恒零开集”的严格资格。完整残差与热张量交换差为下列精确式，并有全频 H⁻¹ 上界。它们不证明热补全保留临终无界、无力性或奇性稳定，不认证实际范数小量；原文构造仅作为明列条件来源。

## HTI.1 对象与完整 Fourier 规范

条件使用原文固定单位环面 `T³=R³/Z³`、ν=1、T=1 的同一平滑实值无散 U，`mean U(t)=0`，及它的完整方程
\[
 U_t-\Delta U+\operatorname{div}(U\otimes U)+\nabla p_U=F,
 \qquad U_t-\Delta U+\mathbb P\operatorname{div}(U\otimes U)=\mathbb PF.
 \tag{HTI.1}
\]
p_U 为真周期压力；所有场在任意 `[a,b]⊂[0,1)` 上平滑，足以逐式取 Fourier/时间导数。原 U 早期为零。这里不重新选择初值，也不把该场当成旧2π环面 a* 的轨道。

取 `ξ_k=2πk`、`â(k)=∫_{T³}e^{-iξ_k·x}a(x)dx`、`||a||₂²=Σ_k|â(k)|²`。单位胞体积为1，积分即归一化 Haar；向量/张量分别用 Hermitian Euclidean/Frobenius 范数。`P_k=I−ξ_k⊗ξ_k/|ξ_k|²`（k≠0）、`P₀=I`，全部正负频率与相位均保留。
\[
 S_s=e^{s\Delta},\qquad \rho(t)=1-t>0,\qquad
 V(t)=V_h(t)=S_{\rho(t)}U(t),\qquad
 \widehat V(k,t)=e^{-\rho(t)|\xi_k|^2}\widehat U(k,t).
 \tag{HTI.2}
\]
s 是热积分的辅助变量；实际补全始终使用锁定的 ρ=1−t，不比较不同 ρ 以筛选结果。对 s>0，其完整周期核是 `H_s(x)=Σ_{n∈Z³}(4πs)^{-3/2}exp(−|x+n|²/(4s))`，严格为正且全胞积分1；Gaussian 周期化的 Fourier 系数为 `e^{-s|ξ_k|²}`，故与 HTI.2 同一算子。下文的正性和卷积界使用这整个核，不用有限像点近似。

## HTI.2 全域资格、解析性及零涡量开集

HTI.2 逐模保实值共轭、无散与零均值；`curl V=S_ρ curl U`，其 Fourier 乘子为 `iξ_k×` 与标量热乘子相乘。均值保持来自热零模为1，不是删除 P₀。U 早期为零使 V 同样早期为零。每个紧物理时间窗上 ρ>0，原 U 光滑，故 V 的所有空间/时间导数在该窗光滑；没有据此断言 t=1 时有有界延拓。

固定一个 t<1 和任意有限 R≥0。Cauchy–Schwarz 给
\[
 \sum_k e^{-\rho|\xi_k|^2+R|\xi_k|}|\widehat U(k,t)|
 \le \|U(t)\|_2
 \left(\sum_k e^{-2\rho|\xi_k|^2+2R|\xi_k|}\right)^{1/2}<\infty.
 \tag{HTI.3}
\]
任意固定次空间导数多出的频率幂仍被 Gaussian 控制。故完整 Fourier 逆和在每个有界复管域绝对局部一致收敛，V(t) 及 curl V(t) 全域空间实解析，事实上其周期提升有整个复空间的延拓；这仅是每个固定 ρ>0 的结论，不给临终统一解析范数。
若 curl V(t) 在非空开集恒零，连通环面的解析恒等原理使其全域为零。再用 `div V=0`：k≠0 时 `ξ_k×V̂(k)=0` 与 `ξ_k·V̂(k)=0` 共同给 V̂(k)=0；零模由 mean V=0 给0。因此 V(t)=0。热乘子对每个 k 都严格非零，故 HTI.2 进一步给 U(t)=0；只用其逐模单射性，没有把逆热算子当成有界算子。
于是 **U(t)≠0 时，curl V(t) 不可能在任何非空开集恒零**。这不等于涡量每一点都非零，不声称每个实际时刻 U(t) 非零，也不抹掉早期零场分支。此结论来自热作用于完整涡量，不沿用上题仅投影/均值修正仍保留涡量支撑的论证。

## HTI.3 完整压力与 ρ′ 项

取零均值周期 q_V，解 `−Δq_V=∂_i∂_j(V_iV_j)`。非零 Fourier 模式为 `q̂_V(k)=−ξ_{k,i}ξ_{k,j}widehat(V_iV_j)(k)/|ξ_k|²`，零模0。因此 `∇q_V=−(I−𝓟)div(V⊗V)`，完整残差是
\[
 G_V=V_t-\Delta V+\operatorname{div}(V\otimes V)+\nabla q_V
     =V_t-\Delta V+\mathbb P\operatorname{div}(V\otimes V).
 \tag{HTI.4}
\]
链式法则及 HTI.1 给
\[
 V_t=S_\rho U_t+\rho'\Delta V
     =(1+\rho')\Delta V-\mathbb P\operatorname{div}S_\rho(U\otimes U)
                              +S_\rho\mathbb PF,
 \qquad \rho'=-1.
 \tag{HTI.5}
\]
热、空间导数和完整 Leray 在同一物理频率上交换，但热不与二次乘积交换。记
\[
 C_\rho=S_\rho(U\otimes U)-(S_\rho U)\otimes(S_\rho U).
 \tag{HTI.6}
\]
将 HTI.5 代入 HTI.4，精确得到
\[
 \boxed{G_V=S_\rho\mathbb PF-\Delta V-\mathbb P\operatorname{div}C_\rho.}
 \tag{HTI.7}
\]
在 V_t 中原热项被 ρ′ 抵消，不代表完整 NS 残差中可以删除 −ΔV。原周期方程积分给 mean F=0，故 mean G_V=0 与上式相容；仍是 P₀=I，没有改用删除力均值的投影。

为显示全部修改项，令 E=V−U，不假设其在终端 L∞ 有界。另有等价完整身份
\[
 G_V-\mathbb PF=E_t-\Delta E+
 \mathbb P\operatorname{div}(U\otimes E+E\otimes U+E\otimes E).
 \tag{HTI.8}
\]
两个有序交叉与误差自作用均在，没有支撑分离或局部角平均。若需比较压力，零均值周期 Green 满足 `−ΔG_T=δ_per−1`，则
\[
 q_V-p_U=G_T*\operatorname{div}F+
 \partial_i\partial_jG_T*(V_iV_j-U_iU_j)
 \quad\text{模仅依赖时间的常数}.
 \tag{HTI.9}
\]
使用完整周期 Lebesgue 卷积；第一项保留原受迫压力的散度差，并非可忽略的局部压力修正。

## HTI.4 二次热交换差的精确积分与符号

此段固定物理 t，只对同一个完整 U(t) 作热积分。令 `u_s=S_sU(t)`，`0≤s≤ρ`，并置 `A(s)=S_{ρ−s}(u_s⊗u_s)`。由乘积 Laplacian，
\[
 A'(s)=-2S_{\rho-s}\sum_{\ell=1}^3
                  (\partial_\ell u_s)\otimes(\partial_\ell u_s).
\]
端点分别为 `A(0)=S_ρ(U⊗U)`、`A(ρ)=V⊗V`，故
\[
 \boxed{C_\rho=2\int_0^\rho S_{\rho-s}
       \sum_{\ell=1}^3\partial_\ell S_sU\otimes\partial_\ell S_sU\,ds.}
 \tag{HTI.10}
\]
这是真正的完整三维、有序张量恒等式；物理场为实值，各张量在点态是半正定，正热核保留该性质。也可由质量1周期热核 H_ρ 写成 `C_ρ(x)=∫H_ρ(x−y)(U(y)−V(x))⊗(U(y)−V(x))dy`，核对正号。归一化迹积分给 `∫tr C_ρ=||U||₂²−||V||₂²=2∫₀^ρ||∇S_sU||₂²ds`，与 HTI.10 的系数2一致。
半正定只指 C_ρ 作为物理点态实对称张量。它没有赋予 `𝓟div C_ρ` 向量序或符号，也不决定能量方向：对无散 V，`⟨V,−𝓟div C_ρ⟩=∫∇V:C_ρ=∫sym∇V:C_ρ`，而应变不是已知正矩阵。这些式没有提供无力、小残差或有利能量通量。

## HTI.5 无截断的全域弱界

定义完整 `||a||_{H⁻¹}²=Σ_k(1+|ξ_k|²)⁻¹|â(k)|²`。对任意张量 T，频率缩并及 `||P_k||op≤1` 给 `||𝓟div T||_{H⁻¹}≤||T||₂`，常数1；全部零模与非零模按此规范处理。周期热在 L² 和点态范数的 L∞ 上收缩，故 HTI.10 给
\[
 \|\mathbb P\operatorname{div}C_\rho\|_{H^{-1}}
 \le\|C_\rho\|_2
 \le2\int_0^\rho\|\nabla S_sU\|_\infty\|\nabla S_sU\|_2\,ds
 \le2\rho\|\nabla U\|_\infty\|\nabla U\|_2.
 \tag{HTI.11}
\]
梯度点态用完整三乘三 Frobenius 范数；`|Σ_ℓ a_ℓ⊗a_ℓ|F≤Σ_ℓ|a_ℓ|²` 支付无额外分量常数的估计。每个固定 t<1 上右侧有限，但未认证其临终有界或趋零。亦可用全频 `A₁(U)=Σ_k|ξ_k||Û(k,t)|` 代替 `||∇U||∞`；它不是有限求和输入。

另给只用完整 L² 的固定 ρ 界。令
\[
 K_\rho=\left(\sum_{k\in\mathbb Z^3}e^{-2\rho|\xi_k|^2}\right)^{1/2}
        =\|H_\rho\|_2<\infty.
 \tag{HTI.12}
\]
Young 与 Cauchy–Schwarz 给 `||S_ρ(U⊗U)||₂≤K_ρ||U||₂²`、`||V||∞≤K_ρ||U||₂`、`||V||₂≤||U||₂`。所以
\[
 \|\mathbb P\operatorname{div}C_\rho\|_{H^{-1}}
 \le\|C_\rho\|_2\le2K_\rho\|U\|_2^2.
 \tag{HTI.13}
\]
Kρ 是整格解析求和条件量，没有数值求值或模式截断。其零模1来自热核质量，不可暗删。HTI.11 与13各自有效，可取较小右端；都不是交换差的符号结论。

由 `||ΔV||_{H⁻¹}≤||∇V||₂` 及手工上界 `sup_{r≥0}r e^{-ρr²}=(2eρ)⁻¹ᐟ²`，完整残差进一步满足
\[
 \|G_V-S_\rho\mathbb PF\|_{H^{-1}}
 \le {\|U\|_2\over\sqrt{2e\rho}}+2K_\rho\|U\|_2^2,
 \qquad
 \|G_V\|_{H^{-1}}
 \le\|F\|_{H^{-1}}+{\|U\|_2\over\sqrt{2e\rho}}+2K_\rho\|U\|_2^2.
 \tag{HTI.14}
\]
若只用原文统一 L² 上界，可把各 `||U(t)||₂` 换成该上界；仍不能删去 `ρ=1−t` 依赖或宣布终端弱残差一致有界。对比上题的有界光滑 H，这里没有假设 `E=(S_ρ−I)U` 的终端 L∞ 或全导数有界；即使其 L² 由乘子给 `||E||₂≤||U||₂`，也不能因此得到 L∞ 有界或转移原速度的临终无界。

## 来源与停止范围

本次实际全文读 `CONTRACT.md`，SHA-256 `bfc58223bd5d9cbefb3e0d6b4c815019187d52ad14df4ea844a79b4efe8e863b`。HTI.1 的原文来源资格按任务作为完整条件，未增读原 PDF、未读 root 新稿或另一作者第4项来源审查。经典 Fourier 热核、周期 Hodge、压力和全域范数估计均在此重列所需推导，不冒称新一般定理或机器认证。
第1–3项已形成自含条件接口：热补全在非零原切片没有开零涡量；完整残差含必要的 −ΔV 和全部交换差；HTI.10–14 给精确积分及可复查弱界。**第4项实际卷积增长未由本稿支付**，并非已证明增长失败。即使它另获证，无力残差、强误差、同固定初值轨道与奇性稳定仍独立未付；本稿不宣布 NS 候选成功或一般 NO-CANDIDATE。全文自读后停止修改。
