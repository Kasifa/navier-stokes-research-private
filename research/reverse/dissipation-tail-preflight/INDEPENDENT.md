# 耗散控制低目标截断尾的独立条件推导

2026-09-09，PRIVATE_CORE。**CONDITIONAL-TAIL-INTERFACE / NO-NEW-PAID-INPUT。** 仅在同一实际 NS 已有光滑存在区间内证明以下估计，不证明其存在至旧 T，不读取根后续稿或另一新稿。根事先披露了“遗漏对的两输入均在 K−b 外”的几何预见；本人此前是 GENERAL_SOURCE_BRIDGE 作者、OBSERVATION_ERROR 及数值观察接口审查者，不称全盲或新颖性发现。历史去重另由指定代理承担，本稿不据有限阅读宣称旧库没有同式。

## 1. 前提、归一化和完整遗漏和

在标准 2π 三维环面，原黏性固定 ν=1，无外力，同一实值无散解 u(0)=a_* 在 [0,t] 光滑，任意 0≤s≤t 均在该区间。写 u=∑u_k e^{ik·x}，向量范数为 Hermitian 长度，点积仍为复双线性；令
\[
\|f\|_2^2=(2\pi)^{-3}\int|f|^2=\sum_k|f_k|^2,\quad \|f\|_{A0}=\sum_k|f_k|,\quad M=\|a_*\|_2,\quad Z(r)=\sum_k|k|^2|u_k(r)|^2.
\tag{DTI.1}
\]
设 C_K={k∈Z³:max_j|k_j|≤K}、P=P_K；固定有限 H⊂{k:0<|k|<b}，K>b>0。H 可不关于原点对称，估计仍成立；若要投影实值则另取 H=−H。H=∅ 时所有目标量为零。对 k∈H，完整尾缺陷的准确系数是
\[
(D_H)_k=-i\mathbb P_k\!\sum_{\ell+m=k\atop (\ell,m)\notin C_K\times C_K}(u_\ell\cdot m)u_m,
\qquad \mathbb P_k=I-\frac{k\otimes k}{|k|^2},\quad D_H=P_H[B(u,u)-B(Pu,Pu)].
\tag{DTI.2}
\]
这是全部遗漏有序对的单一和，不分别估两个可重叠集合，也不删负模、相位、交叉项或 Leray；零输出不属于 H。无散给 u_ℓ·m=u_ℓ·k，且 ‖P_k‖≤1。

## 2. 一条尾部估计及其热累计

遗漏对中若 ℓ∉C_K，存在坐标 j 使 |ℓ_j|>K，故 |ℓ|>K、|m|≥|ℓ_j|−|k_j|>K−b；若 m 在 cube 外则交换角色。因此两输入均在 Euclidean 半径 K−b 外，而且 |ℓ||m|>K(K−b)。置 a_ℓ=|ℓ||u_ℓ|，在遗漏集合上应用 Cauchy，并用 ℓ↦k−ℓ 的双射，得到
\[
\sum_{\ell+m=k\atop\mathrm{omitted}}|u_\ell||u_m|
\le\frac{\sum_{\mathrm{omitted}}a_\ell a_m}{K(K-b)}
\le\frac{Z(r)}{K(K-b)},\qquad |(D_H)_k(r)|\le\frac{|k|Z(r)}{K(K-b)}.
\tag{DTI.3}
\]
常数为 1：两个顺序都已在该和中，没有再乘 2，也没有假设有利相消。同一遗漏和使用无权 Cauchy 另给 |(D_H)_k|≤|k|‖u(r)‖₂²≤|k|M²。所有卷积绝对收敛可直接由 Cauchy 保证；时间积分在光滑紧区间内有定义。定义有限热权重和实际尾历史
\[
\kappa_H(\tau)=\sum_{k\in H}|k|e^{-|k|^2\tau},\qquad J_H(s,t)=\int_s^t e^{(t-r)\Delta}D_H(r)\,dr.
\]
逐系数保留原热因子、有限求和并用积分三角不等式，得
\[
\|J_H(s,t)\|_{A0}\le\int_s^t\kappa_H(t-r)\min\!\left\{M^2,\frac{Z(r)}{K(K-b)}\right\}dr
\le\min\!\left\{\frac{\kappa_H(0)}{2K(K-b)}\bigl(\|u(s)\|_2^2-\|u(t)\|_2^2\bigr),\ M^2\sum_{k\in H}\frac{1-e^{-|k|^2(t-s)}}{|k|}\right\}
\le\frac{\kappa_H(0)M^2}{2K(K-b)}.
\tag{DTI.4}
\]
中间一步只用同解能量等式：以归一化体积内积乘原 NS，周期积分使输运项和压力项为零，故 (1/2)d‖u‖₂²/dr=−Z。因 κ_H(t−r)≤κ_H(0)，得到恰如上式的 1/2；没有体积因子遗漏，也没有删去压力的动力学作用。这里 K(K−b) 的分母比仅利用“两输入>K−b”所得粗分母更强，但仍是同一条尾预算。

第二个分支来自逐项准确积分 ∫_s^t|k|e^{−|k|²(t−r)}dr=(1−e^{−|k|²(t−s)})/|k|，因而还给 M²κ_H(0)(t−s) 的统一短时间上界。κ_H(t−r) 一般不能在整个积分上换成更小的 κ_H(t−s)；两个上界可取最小，不能由此把耗散分支再乘 (t−s) 或相应热因子。t=s 时 J_H=0；M=0 时能量等式给零解。没有取 K=b、没有声称 H³ 尾受控，也没有选择实际 K、H 或时刻。

## 3. 与同数据近似的完整接口

令任意合格实值无散时间重建 v=P_Kv，w=P_Ku，e=w−v，δ(r)=‖e(r)‖₂。它们只定义在同一已存在区间；v 不必是精确 Galerkin 解。准确双线性分解为
\[
P_H[B(u,u)-B(v,v)]=D_H+P_H[B(e,w)+B(v,e)].
\tag{DTI.5}
\]
因 w=v+e，后两个有序项完整包含 B(e,v)+B(v,e)+B(e,e)，不把它们合并为二倍同一向量。用 OE.6 的系数 Cauchy 界及 ‖w‖₂≤M、‖v‖₂≤M+δ，得同一来源差的全部预算
\[
\left\|\int_s^t e^{(t-r)\Delta}P_H[B(u,u)-B(v,v)](r)\,dr\right\|_{A0}
\le\int_s^t\kappa_H(t-r)\left[\frac{Z(r)}{K(K-b)}+\delta(r)(2M+\delta(r))\right]dr.
\tag{DTI.6}
\]
δ 尚未支付，不可由两网格差或采样一致令其为零。若进一步比较状态，准确 Duhamel 身份还包含 e^{(t−s)Δ}P_H[u(s)−v(s)] 和 −∫_s^t e^{(t−r)Δ}P_H R_v(r)dr，其中 R_v=∂_rv−Δv−P_KB(v,v)；其余积分正是 DTI.5。完整全场重建残差为 R_v−(I−P_K)B(v,v)，不可因当前 H 在 cube 内就从全解误差证书删除支持外漏出。

故本界只从实际原解能量支付遗漏高输入对的低目标热累计上界；仍未付 P_Ku−v、合格连续时间重建及其残差、原初值近似误差、历史求积/读取/相减/范数求值误差。它不以第一来源代替实际第二输入，不清空正起点已有场，不认证来源非零、真实全窗门或存在至 T。固定 H 的尾界随 K 增大变小也不能把有限网格族升级为同一初值的无限尺度奇性；科学状态为条件接口，没有新的已支付动态候选。

## 实读来源与停稿范围

本轮合同全文；GS 第 1–36 行（GS.1–2、完整有序符号）；OE 第 1–42、83–139、175–215、248–273 行（归一化/原能量、完整系数界、全余来源与求值责任）。此前读审经历已在开头披露；本轮未借未读新稿补证，不主张替代历史去重。

| 实际文件 | SHA-256 |
|---|---|
| `dissipation-tail-preflight/CONTRACT.md` | `3b5b18abd8b72aab06baf7badcfbfca93c3494987edc9d4ddd34ead43b1cb996` |
| `four-leaf-preflight/GENERAL_SOURCE_BRIDGE.md` | `59354781b8d04087cf1d5383824dbe741d24b3c0fae8798caa6c50cae24a3ebe` |
| `annular-source-observation/OBSERVATION_ERROR.md` | `5823a2e03e4e176eb2ab444f58fce1797ebef6aafc5f84ada594b359e44c1b05` |

只写本文件，科学 worker 0；无程序/数组/FFT/参数求值、Git 或外发。全文自读核源后停改，最终文件 SHA 由任务消息给出。
