# 同一原解的时间来源分解与有限窗口余项

2026-09-07。PRIVATE_CORE。独立数学审计；仅核验指定分解和条件预算，不提出新候选、不主张新定理或新颖性，不启动仿真或冻结。

结论：指定来源分解精确成立，九个有序通道无遗漏。若同一真实解在窗口上有独立给出的 A_(m+1) 上界M，则完整后续反馈R在A_m中具有明确的O((t−t₁)^(3/2))预算。该预算既不证明旧历史的自作用G占优，也不识别物理意义的“纯第一代涡管”。不能用未证M使合同循环成立。

## 1. 固定对象与精确恒等式

固定三维环面 T³=(R/2πZ)³、ν>0和一个光滑、实值、无散、零均值初值a。设u是由它产生的同一个光滑无外力NS解，在[0,t₂]存在，0≤t₁<t₂。约定

\[
 E(t)=e^{\nu t\Delta},\qquad
 B(f,g)=-P_L[(f\cdot\nabla)g],
 \qquad u_t=\nu\Delta u+B(u,u).
\]

B是有序双线性算子，完整周期Leray投影保留。对t∈[t₁,t₂]定义

\[
 h(t)=E(t)a,\qquad
 g(t)=E(t-t_1)[u(t_1)-E(t_1)a],
\]

\[
 v(t)=h(t)+g(t)=E(t-t_1)u(t_1),
 \qquad r(t)=u(t)-v(t).
\tag{1}
\]

最后一个v的等式来自热半群性质。它是同一轨道在t₁处的线性续演，并没有修改物理初值。完整mild式给

\[
 r(t)=\int_{t_1}^tE(t-s)B(u(s),u(s))\,ds,
 \qquad r(t_1)=0.
\tag{2}
\]

若把[0,t₁]的真实历史也展开，则

\[
 g(t)=\int_0^{t_1}E(t-s)B(u(s),u(s))\,ds.
\tag{3}
\]

因此g包含截止t₁的全部非线性历史，经热演化后得到；它不是一个事后自由指定的新种子。当t₁=0时g=0。

为避免“积分B”丢掉黏性传播，所有来源项明确写为

\[
 \mathcal G(t)=\int_{t_1}^tE(t-s)B(g(s),g(s))\,ds,
\]

\[
 \mathcal H(t)=\int_{t_1}^tE(t-s)
 [B(h,h)+B(h,g)+B(g,h)](s)\,ds,
\]

\[
 \mathcal R(t)=\int_{t_1}^tE(t-s)
 [B(r,h+g)+B(h+g,r)+B(r,r)](s)\,ds.
\tag{4}
\]

把u=h+g+r代入B(u,u)后，G含1项、H含3项、R含5项，合计全部9个有序项。因此对每个t∈[t₁,t₂]，特别是指定终点t₂，严格有

\[
 \boxed{u(t)=h(t)+g(t)+\mathcal G(t)+\mathcal H(t)+\mathcal R(t).}
\tag{5}
\]

不能将B(h,g)+B(g,h)写成2B(h,g)，也不能删去任一回流方向。一个便于估计而完全等价的表达是

\[
 \mathcal R(t)=\int_{t_1}^tE(t-s)
 [B(r(s),u(s))+B(v(s),r(s))]\,ds.
\tag{6}
\]

因为B(r,u)=B(r,v)+B(r,r)，(6)已经包含R里的二次r项，没有把它当作可忽略项。

## 2. Wiener范数与完整热核估计

使用Fourier系数 f̂(k)=(2π)^(−3)∫f(x)e^(−ik·x)dx，定义m≥0的绝对范数

\[
 \|f\|_{A_m}=\sum_{k\in\mathbb Z^3}(1+|k|)^m|\widehat f(k)|,
\]

其中向量长度为Hermitian Euclidean范数。光滑场的所有A_m有限。以下常数按这个范数给出，不混用归一化与未归一化L²。

因(1+|p+q|)^m≤(1+|p|)^m(1+|q|)^m、∥P_L(k)∥≤1，直接卷积给

\[
 \|B(f,g)\|_{A_m}\le\|f\|_{A_m}\|g\|_{A_{m+1}}.
\tag{7}
\]

若f无散，f̂(p)·q=f̂(p)·(p+q)，故可把导数放到输出频率k。对σ>0，利用

\[
 \sup_{r\ge0}r e^{-\nu\sigma r^2}
 =(2e\nu\sigma)^{-1/2}\le(\nu\sigma)^{-1/2}
\]

得到完整频率估计

\[
 \|E(\sigma)B(f,g)\|_{A_m}
 \le\frac{\|f\|_{A_m}\|g\|_{A_m}}{\sqrt{\nu\sigma}}.
\tag{8}
\]

零模的B为零。实值、无散和零均值在上述分解中保持；(7)–(8)也适用于r、v、h、g。半群在每个A_m上收缩。这里不截断卷积，不要求相邻频带，也不使用相位随机化。范数预算使用绝对值而失去有利相消，仅作为上界；精确恒等式(1)–(6)仍保留全部相位和压力。

## 3. 给定真实解上界时的明确R预算

设有独立可用的常数M、K，使

\[
 \sup_{t_1\le s\le t_2}\|u(s)\|_{A_{m+1}}\le M,
 \qquad
 \sup_{t_1\le s\le t_2}\|v(s)\|_{A_{m+1}}\le K.
\tag{9}
\]

K不是额外的动力学债务：由(1)及热收缩，可直接取

\[
 K=\|u(t_1)\|_{A_{m+1}}\le M,
\tag{10}
\]

或使用任何已认证的更粗上界。此处不需要分别控制可能相消的h和g来估计R。

记τ=t−t₁，T=t₂−t₁。由(2)、(7)及热收缩，所有0≤σ≤T满足

\[
 \|r(t_1+\sigma)\|_{A_m}\le M^2\sigma.
\tag{11}
\]

将(11)用于等价式(6)，再用(8)，得到

\[
 \begin{aligned}
 \|\mathcal R(t_1+\tau)\|_{A_m}
 &\le\frac{(M+K)M^2}{\sqrt\nu}
       \int_0^\tau\frac{\sigma}{\sqrt{\tau-\sigma}}\,d\sigma\\
 &=\boxed{\frac{4(M+K)M^2}{3\sqrt\nu}\tau^{3/2}}
 \le\frac{8M^3}{3\sqrt\nu}\tau^{3/2}.
 \end{aligned}
\tag{12}
\]

积分等式由σ=τz及∫₀¹z(1−z)^(−1/2)dz=4/3直接得到。端点热核奇性可积。这个界对整个指定窗口成立，不只是一项形式时间展开。由(5)，也有

\[
 \|u(t)-h(t)-g(t)-\mathcal G(t)-\mathcal H(t)\|_{A_m}
 \le\frac{4(M+K)M^2}{3\sqrt\nu}(t-t_1)^{3/2}.
\tag{13}
\]

若只用(9)提供的一阶导数余量，本审计不宣称同一A_m中的O(τ²)常数。若另外独立证明u、v在A_(m+2)的上界分别为M₂、K₂，则(11)可在A_(m+1)成立，再由(7)直接积分得到

\[
 \|\mathcal R(t_1+\tau)\|_{A_m}
 \le\tfrac12(M_2+K_2)M_2^2\tau^2.
\tag{14}
\]

这是付出更强空间导数上界后的替代预算，不是在本次追加时间Taylor阶。没有声称(12)的指数最优。

## 4. 如何提供非循环的M

式(12)是条件估计。把M定义成未知真实轨道的上确界，只能得到一个形式上正确但尚未认证数值/解析大小的常数；不能拿它证明该上确界受控，或说给定t₂已被局部存在覆盖。

一种充分且自包含的来源是完整Wiener压缩构造。令q=m+1，给定一个已知光滑无散起点b，A=∥b∥_(A_q)>0。对热mild映射的双线性积分，(8)给

\[
 \|D(f,g)\|_{C([0,T],A_q)}
 \le2\sqrt{T/\nu}\,
       \|f\|_{C A_q}\|g\|_{C A_q}.
\]

取

\[
 T_{\rm loc}=\frac{\nu}{256A^2},\qquad M=2A.
\tag{15}
\]

则半径2A球内，映射范数至多A+8A²√(Tloc/ν)≤3A/2；差值Lipschitz常数至多8A√(Tloc/ν)≤1/2。获得完整无限维mild解与∥u∥_(C A_q)≤2A。没有施加Galerkin截断。

光滑性可在这个同一窗口保持，而不是为每一导数另缩一个趋零窗口。具体地，对任意整数ℓ>q，tame权重不等式

\[
 (1+|p+q'|)^\ell\le2^{\ell-1}
 [(1+|p|)^\ell+(1+|q'|)^\ell]
\]

及各Picard项统一A₀≤2A，给高阶迭代范数z_j的界

\[
 z_{j+1}(t)\le\|b\|_{A_\ell}
 +c_\ell\int_0^t(t-s)^{-1/2}z_j(s)\,ds,
 \qquad c_\ell=2^\ell(2A)/\sqrt\nu.
\]

反复卷积的上界级数为

\[
 \|b\|_{A_\ell}
 \sum_{n\ge0}\frac{(c_\ell\sqrt\pi)^n t^{n/2}}
                       {\Gamma(1+n/2)},
\]

在有限Tloc上收敛。高一阶有界与A_q收敛的加权ℓ¹插值给各阶连续收敛，方程再给时间正则。因而对光滑b得到光滑真实解；唯一性来自局部压缩及重叠小区间续接。

有两种合法使用方式，不能混淆：

- **从原初值保证整个窗口：** 取b=a。若预定t₂≤ν/(256∥a∥²_(A_q))，可直接在[0,t₂]用M=2∥a∥_(A_q)，且K≤M。若t₂超过这个充分窗口，本构造没有证明那个t₂的上界，不能事后宣称已经覆盖。
- **从已知真实前段作局部延续：** 若同一原解已经到达t₁，并且其实际u(t₁)或一个A_q范数上界有独立认证，取b=u(t₁)。对t₂−t₁≤Tloc得到M=2A、K≤A，故(12)右端可写为16A³τ^(3/2)/√ν。唯一性保证是同一原解的延续。这是在分析中局部重写mild式，不是每代更换允许初值。若此前到达t₁或A本身未证，不能靠这句话付清前段历史。

若仅已知上界A≤Ā，可用Ā代替(15)中的A，窗口与预算更保守。A=0的零起点在后续窗口给唯一零解，不需除以A²。这里的范数可作为严格定义的解析常数，但没有报告其未经计算的数值或一个未经验证的数值时间窗。

## 5. 来源标签能说明什么

g不是某一代物理涡管、某个拓扑连通分量或一个唯一的“新生量”。式(3)含首次自作用、重复作用以及所有早于t₁的混合项；改变t₁会改变分账。它是固定热参照与时间切点下的精确定义。即使它非零，也可能含初始种子原有频率或返回到原频率的部分。

G只认证“截止t₁的全部非线性历史在随后热续演下的自作用”这一来源标签。g在t₁后的热续演不是独立的无外力NS解，不能把它的演化当成完整新涡管动力学。r携带t₁之后产生的全部真实非线性响应，R再包含它与旧历史、热种子和自身的反馈。

H并未由(12)证明很小。一般情况下，H与G都从窗口的一阶Duhamel积分开始；R小于某个量级不能推出G具有非零目标、净占优、绝对占优或返回到下一模板。若未来要求其中任一种性质，须指定观测/状态范数，实际估计G、H以及线性h+g的目标贡献，并同时付清已有余项预算的输入。当前没有这样一个通过的机制合同。

这套分解保留双向有序作用、共轭相位、非相邻作用和完整周期压力。压力是原方程中由Leray投影确定的全域响应，不是任意局部补项。这里没有正交代际投影，也不把各项能量相加而删去交叉项。

有限窗口界不提供跨代统一M、统一窗口长度、固定初值的全部尺度或有限总时间；若迭代时M变大，(15)允许窗口随之缩短。不能把独立初值族或不断重选热参照得到的账目直接命名为单个初值的无限级联。NOT CLAY。

## 6. 审计来源与状态

上述证明是对本次指定分解的独立直接推导，不从Kerr数值重联图或2017拓扑重联定理导入动力学归因。Wiener压缩方法在本树 swirl-regeneration/LOCAL_REMAINDER_DRAFT.md §2已有先例，本次重推一般m、ν及来源窗口的具体常数，没有将其称为新研究定理。

检查通过的仅是式(1)–(15)及其明确假设。M的具体认证、前代纯度、返回形态、G的实际供给强度和跨代统一性均未由此完成。不计算、不扫描、不冻结、不提交。

输入字节绑定随后列出；它们只定位工作范围及本地方法先例，不替代以上推导。

```json
{
  "schema": "source-attribution-analytic-audit-inputs-v1",
  "timestamp_utc": "2026-09-07T14:54:00.409621+00:00",
  "worktree": "/Users/kasifa/Documents/Math/navier-stokes-reverse",
  "inputs": [
    {
      "path": "research/reverse/reconnection-preflight/CONTRACT.md",
      "bytes": 2319,
      "sha256": "23eca817fca5500e6dc7e7ec5647272751929fd486c58ed3dd6f30d32a893cf4"
    },
    {
      "path": "research/reverse/swirl-regeneration/LOCAL_REMAINDER_DRAFT.md",
      "bytes": 5383,
      "sha256": "c0346e98e776e7a5526727fde1572f1fc543d66b8fd3c31450ca791ea7297f8c"
    }
  ],
  "review_scope": "Exact ordered decomposition; conditional Wiener remainder; noncircular sufficient local existence bounds",
  "external_mathematical_theorems_imported": [],
  "scientific_numerical_computation": false,
  "novelty_claim": false,
  "candidate_claim": false,
  "frozen_package": false
}
```
