# 完整背景交叉的自由热算子没有全晚时 X_beta 界

2026-09-22，PRIVATE_CORE。根作者稿，待非作者审核。只使用合同中已接纳的同一V_h及其核心极限，不对它再做残差定号诊断。本证明给出一个具体重构方法的障碍，不声称真实非自治传播器不稳定。

## HP.1 对象与准确结论

固定一次t_*<1、lambda=lambda_p、h>0、A=1/2+h，tau(t)=lambda²(1−t)。设0≤beta<1/2。X_beta取合同的sup tau^beta L∞范数，向量用Euclidean长度。考虑光滑实值无散零均值、时间支撑紧包含于(t_*,1)的辅助输入e。每个这样的输入只在一个严格早于1的紧时间窗与V_h相乘，故K_V e由完整周期热/投影定义良好，之后只自由热延续；它属于X_beta。

**待审结论：** 对每一个固定t_*及beta，存在同一固定a、phi和固定时间包络，形成e_tau，使

    ||e_tau||_X ≤ C_beta，
    tau^beta ||K_V e_tau(t_tau)||∞ ≥ c tau^(−h)，
    t_tau=1−tau/lambda²， tau→0。                         (HP.1)

常数均为有限正数，不要求在beta或原构造参数上统一。这里e_tau是检验算子界的一族方向，不是声称从不同初值构造原解。全部e_tau(t_*)=0，未知实际u若研究则仍取同一b_*=V_h(t_*)；没有证明它的全晚时存在。

## HP.2 实际非零性，不能只数尺度

既有全像核心极限为W0(Y)=lambda Psi(Y)，在每个固定紧集上一致。W0光滑有界、无散、独立Y3，形如f0(r)e_theta+g0(r)e3；旧增长见证给f0(R_w)>0。记其轴向涡量zeta(r)=f0'(r)+f0(r)/r，按光滑轴延拓。

若partial_1 zeta在整个空间恒0，径向性使zeta为常数。解(r f0)'=r zeta且轴上光滑，得到f0=zeta r/2；全域有界再迫使zeta=0及f0=0，与见证矛盾。因此存在一个离轴小球B，使partial_1 zeta在B有严格同号。

选eta∈C_c∞(B)，使int eta partial_1 zeta不为0，令phi=curl(eta e3)。phi实值、无散、紧支撑，积分为0。选择chi∈C_c∞，在supp(phi)的开邻域恒1；令

    a=curl(chi Y2 e3)。

则a同样实值、无散、紧支撑、均值0，且在该邻域恰为e1。完整有序张量T(W,a)=W⊗a+a⊗W满足

    int T(W0,a):grad phi
      =−int phi·[(a·grad)W0+(W0·grad)a]
      =−int phi·partial_1 W0
      =−int eta partial_1 zeta ≠0。                      (HP.2)

最后一步用curl的积分自伴性，非梯度的涡量见证支付非零性。若需要将phi反号，固定后记此值b0>0；a、phi以后不随tau改变。不把裸P当作L∞有界算子。

## HP.3 整个有限时间窗的严格余量

对theta≥0定义

    W^theta(Y)=(1+theta)^(-A) W0(Y/sqrt(1+theta))，
    B(theta)=int T(W^theta,a):grad(exp(theta Delta_R3)phi) dY。

因a紧支撑，W0光滑且有界，热流在theta↓0时在其支撑上以C1趋phi；B连续且B(0)=b0。固定一次delta>0足够小，使B(theta)≥b0/2于[0,delta]。再固定非负非零chi_t∈C_c∞((0,delta))，记m=int chi_t>0。delta只是测试输入的相对时间窗，不改rho或实际背景热尺度。

令L_tau=lambda/sqrt(tau)，把a、phi以L_tau为周期延拓。充分小tau时其支撑均位于中心基本胞内。对s_theta=t_tau−tau theta/lambda²，准确有tau(s_theta)=(1+theta)tau，故

    W_tau^theta(Y):=tau^A V_h(sqrt(tau)Y/lambda,s_theta)
      =(1+theta)^(-A) W_((1+theta)tau)(Y/sqrt(1+theta))。

既有W_epsilon→W0的局部一致收敛，给W_tau^theta→W^theta在[0,delta]×supp(a)上一致：epsilon∈[tau,(1+delta)tau]全趋0，空间自变量在固定紧集，不需要未付的时间导数界。

同时，在同一紧集及0≤theta≤delta上，完整周期热作用的grad exp(theta Delta_TL)phi_L一致趋grad exp(theta Delta_R3)phi。理由是把整个周期核写成所有R3像：零像精确给R3项，非零像与两个固定紧支撑的距离至少cL_tau|n|；Gaussian导数的全部像和被C exp(−cL_tau²/delta)控制。靠theta=0的负幂由该正间隙的指数吸收，theta=0处两者本来相同。未采用有限像截断。

因此完整张量配对

    B_tau(theta)=int T(W_tau^theta,a):grad(exp(theta Delta_TL)phi_L) dY

在[0,delta]上一致趋B(theta)。被积积分只涉及固定supp(a)；周期压力虽非局部，下一步通过完整自伴投影精确保留，不用局部压力替换它。存在同一tau0>0，使0<tau<tau0时B_tau(theta)≥b0/4全窗成立。这个严格余项控制不是只有形式主项。

## HP.4 固定初端与完整周期Duhamel配对

定义

    e_tau(s,x)=tau^(-beta) chi_t(lambda²(t_tau−s)/tau)
                         a_L(lambda x/sqrt(tau))，
    phi_tau(x)=phi_L(lambda x/sqrt(tau))。

包络以0延拓；充分晚时整个支撑落在(t_*,t_tau)内。每一输入都光滑实值、周期、无散、零均值，且e_tau(t_*)=0。零均值来自紧支撑curl的积分为0，不是改变P0。准确有

    ||e_tau||_X ≤ (1+delta)^beta ||chi_t||∞ ||a||∞=:C_beta。 (HP.3)

用phi_tau在完整周期K_V公式中配对。P自伴、P phi_tau=phi_tau且与热流交换，负散度通过周期分部积分变为正张量梯度配对。因此P和压力是精确消去于此无散测试，而非从方程删除。

用dx=tau^(3/2)lambda^(-3)dY、grad_x=lambda tau^(-1/2)grad_Y、ds=−tau lambda^(-2)dtheta，定义归一化输出

    Q_tau=tau^beta lambda³ tau^(-3/2)
                 int_T3 (K_V e_tau)(t_tau,x)·phi_tau(x) dx。

保留全部有序项、相位和周期作用的精确公式为

    Q_tau=lambda^(-1) tau^(-h) int_0^delta chi_t(theta) B_tau(theta)dtheta
         ≥ b0 m/(4 lambda) tau^(-h)。                    (HP.4)

另一方面|Q_tau|≤tau^beta ||K_V e_tau(t_tau)||∞ ||phi||L1(R3)。由此HP.1取c=b0m/(4lambda||phi||1)>0成立。C_beta>0，因为非零配对已保证a和包络非零。将每个输入除以C_beta，可令范数≤1，而输出仍趋∞。

固定t_*无论多晚，均能放入这一族越来越晚的窗口。辅助测试族改变的只是算子检验方向，不能把它们误称同一原解轨道或声称exists u0 forall尺度已构造。

## HP.5 对实际非线性固定点候选的准确影响

完整自由热积分映射形式为

    T(e)=Z+K_V e−int exp((t−s)Delta) P div(e⊗e)(s)ds，
    Z=−int exp((t−s)Delta)G_h(s)ds。

Z是否属于X_beta并未支付。即便支付，也不能在整个X_beta球上把T作为局部Lipschitz收缩：如果它在0邻域有有限Lipschitz常数，对每个固定光滑紧时支撑e_tau先令方向幅度epsilon→0，二次项除epsilon后趋0，得到K_V的有限界，与HP.4矛盾。每个固定方向的二次响应在X_beta有限，因所有输入乘积的时间支撑严格早于1。

还可在任一E∈X_beta附近作同一反检，只要该完整映射在那里有定义。方向导数中的背景换成V_h+E；在检验窗和supp(a)上，tau^A|E|≤C||E||_X tau^(A−beta)→0。于是HP.4的核心B_tau只添一致o(1)，原正下界仍在。固定输出配对中先令epsilon→0即可从假设Lipschitz界导出矛盾，无需假定真实解存在或该映射先有全域Frechet导数。这里A−beta>0；这一附带结论仍仅限本合同误差空间的自由热表示，不排其它空间/预条件传播方法。

**通过的障碍不会等于完整重构失败。** 该结果至多删除一个具体的全晚时收缩方案：仅靠取更晚t_*，不能把完整背景交叉在X_beta里变成小扰动。它没有排除真实非自治L_V传播器的有界/振荡相消，也未求实际−G_h受迫响应，更未排除完整非线性修正。不能把K_V的检验输入当作实际误差，或从无界算子范数推出特定响应发散。下一步若研究L_V，必须有真正新输入，不能只再命名同一临界范数。

## 来源与执行范围

根本轮全文复读同树heat-signed-pairing-preflight/ROOT_PAIRING（79行）及heat-vorticity-tail-preflight/MAIN_TERM_AND_IMAGES（81行）；只复用后来的full-acceptance/growth-acceptance已接纳范围。HP.2非零见证、HP.3联合极限与HP.4完整算子下界为本稿新推导，不以外部论文名义背书。没有对原166页/Lean作新完整认证。合同已在证明前落盘；根已向Gauss披露缩放思路，Hume在独立稿中反检同一命题，双方不是盲评。

本稿没有科学程序/数组/FFT/数值求值/扫描/新图，仅解析推导和文本写读。全文自读后停稿待非作者审核；当前尚不接纳为证明或新冻结包。
