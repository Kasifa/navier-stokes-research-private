# 指定控制族临界参数的符号对数夹界

2026-09-08，PRIVATE_CORE。独立解析推导，待根代理非作者复核。仅从已接受的 MB 参数单调性与 UE 全窗标量门推出符号夹界；不求新的指数或对数数值，不选择 m、ε，不读取失败 M2 结果或新数组，不运行科学核。

## 1. 对数导数的一致严格界

沿用
\[
m_0=\frac{19}{5},\quad T=\frac52,\quad
A(m)=\frac{1839+60m}{160},\quad d=\frac{15}{128},\quad C=\frac{49}{128},
\]
\[
f_T=\frac32-\frac12e^{-2T},\quad q=1-e^{-T}>0,\quad
k=\frac{3q}{8}>0,\quad h=\frac{e^{-2T}}{f_T},
\quad y(m)=e^{-qA(m)+dT}.
\]
对每个 \(m\ge m_0\)，MB 已证 \(0<y<1\)、\(y'=-ky\)、\(0<h<2/431\)，以及
\[
E(m)^2=\frac{2}{441f_T^2}y^2(C+h-hy),\qquad E(m)>0.
\]
取自然对数并微分，
\[
\frac{d}{dm}\log E(m)
=-k\left[1-\rho(m)\right],\qquad
\rho(m):=\frac{hy}{2(C+h-hy)}.
\tag{CB.1}
\]
因 \(0<y<1\)，分子为正且小于 h，分母严格大于 \(2C\)，故
\[
0<\rho(m)<\frac{h}{2C}
<\frac{2/431}{2(49/128)}
=\frac{128}{21119}.
\tag{CB.2}
\]
记
\[
\gamma:=1-\frac{128}{21119}=\frac{20991}{21119}\in(0,1).
\]
于是对整个参数半轴，
\[
-k<\frac{d}{dm}\log E(m)<-\gamma k<0.
\tag{CB.3}
\]
这里没有把负号乘法后的大小方向省略：\(0<\rho<1-\gamma\) 给
\(\gamma<1-\rho<1\)，再乘负数 \(-k\) 才得到 CB.3。

## 2. 任意两个参数间的 E 比值

任取有限 \(m_0\le m_1<m_2\)，记 \(s=m_2-m_1>0\)。
CB.3 在这个正长度区间上连续且处处严格成立，所以
\[
-ks<\log\frac{E(m_2)}{E(m_1)}<-\gamma ks,
\]
即
\[
e^{-ks}<\frac{E(m_2)}{E(m_1)}<e^{-\gamma ks}.
\tag{CB.4}
\]
两端严格号均保留。若 \(m_1=m_2\)，比值为 1，两个包围端也为 1；
该零长度情况应写等号，不能继续使用 CB.4 的严格形式。
不需要给邻域选择新的中心或宽度，此式对任意上述两参数均成立。

## 3. mcrit 的夹界与端点

令 \(\eta>0\) 是与 m 无关的同一参照节点必要预算；本节只在条件
\[
\ell:=\log\frac{E(m_0)}{\eta}>0
\quad\text{即}\quad 0<\eta<E(m_0)
\tag{CB.5}
\]
下讨论临界参数。MB 的连续严格递减及 \(E(m)\to0\) 已保证存在唯一有限
\(m_{\rm crit}>m_0\)，满足 \(E(m_{\rm crit})=\eta\)。
令 \(\Delta=m_{\rm crit}-m_0>0\)。在 CB.4 取 \(m_1=m_0\)、\(m_2=m_{\rm crit}\)，
或者直接积分 \(-(\log E)'\)，得到
\[
\gamma k\Delta<\ell<k\Delta.
\tag{CB.6}
\]
所有除数均为正，故准确夹界为
\[
\boxed{\quad
\frac{\ell}{k}<\Delta<
\frac{1}{\gamma}\frac{\ell}{k}
=\frac{21119}{20991}\frac{\ell}{k}.
\quad}
\tag{CB.7}
\]
左界来自 \(\ell<k\Delta\)，右界来自 \(\gamma k\Delta<\ell\)；
两边方向和严格性与 CB.6 相容。

这两端本身不等于临界点。例如，符号位置
\(m=m_0+\ell/(\gamma k)\) 已有 \(E(m)<\eta\)，因为 CB.4 的上界仍严格；
\(m=m_0+\ell/k\) 则有 \(E(m)>\eta\)。这只解释开夹界的端点，不是选择或试算两个新参数。

若 \(\eta=E(m_0)\)，则临界点为 \(m_0\)、\(\ell=\Delta=0\)，应单独处理；
CB.7 的严格式不适用。若 \(\eta>E(m_0)\)，则在 \(m\ge m_0\) 没有该临界点，
而且节点必要预算与该指定族门已经无交。
本稿没有判定实际 \(\eta\) 落在哪一种情形，也没有求 \(\ell\) 或 \(m_{\rm crit}\) 的数值。

## 4. 与全窗控制及实际输入的关系

UE 已另行证明，对所有 \(m\ge m_0\)，\(E(m)\) 是当前显式函数
\(\beta=\varepsilon L_m f,\alpha=\beta/64\) 对取满包络的**精确全窗标量门**。
因此在 CB.5 的条件下，节点预算与该标量门的交集为
\[
m_0\le m\le m_{\rm crit},\qquad \eta\le\varepsilon\le E(m).
\]
CB.7 只夹住这个符号交集的参数端点。
它不证明实际参照满足导数或残差的全窗包络，不支付其它节点、各时间段或终点小数据条件，
也不产生原 NS 解的全局性或奇性结论。
若只掌握 \(\eta\) 的一个严格下端，不能将它不加说明地当作准确 \(\eta\) 来宣称准确 mcrit；
可对该下端另定义放宽后的必要边界，但本文不作新的数值比较。

本项是已有控制公式的内部解析推论，无新颖性声明。失败 M2 运行仍为 NOT_ADMITTED，
其中任何 Q2/D 或派生值均不参与本证明。

实际来源绑定（相对此目录）：

| 输入 | SHA256 |
|---|---|
| M2_CONTROL_BUDGET_MONOTONICITY.md | 750262253c2e90f35ea15713438bf76bf08c752eed2ed94d2370d83d30f0b3ba |
| M2_CONTROL_FAMILY_UNIFORM_ENDPOINT_LEMMA.md | 9170e28436fdf0ee9c47978a66f6df23000cc2bafe2b58c08d75abb989dfcf4c |

本作者已在紧邻前项写成并全文核对上述推导；本项重新定位读取实际定义与结论并核对字节 SHA。
工具仅作文件读取、SHA 与写本文件。所有常数化简、微分与积分不等式均已在正文显式列出。

