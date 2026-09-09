# 来源、实读范围与去重

2026-09-09。PRIVATE_CORE。正式冻结前仍须合并作者停稿和非作者审查。原PDF来源/字节/SHA、166页及抽取器见 sources/manifest.json。整本抽取不等于整本审读；保存的页图是原文阅读证据，无新研究图/读者PDF。外部仓库8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538仅固定为管理所给参考版本，本题不执行Git克隆、Lean/Comparator/nanoda或完整依赖审计。

官方公告 https://openai.com/index/navier-stokes-solution/ 本轮实际访问；原论文 https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf 使用管理保存原件，复制后实际核SHA=0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f、2959204字节。论文带光滑紧支撑外力的C/D声明是作者声明，不能因带力称非Clay；全文证明/形式化重检未验收。本题不用新闻代理数量或外部优先权争议作证据。

root本轮实际完整读取PDF文本页：1–8、11–15、116–118、125–126。实际看整页渲染：15、118、125、126；页125明确固定基本胞内支撑间隔与周期压力，页126确认缩放后终端路径、力支撑和同力唯一性，页118确认cutoff与完整受迫压力式，页15确认平坦范围与局部热外场。公式不能从抽取文本错序推断。其它证明细节的作者实读与视觉范围分别在 SOURCE_FORCE_MAP、PERIODIC_FORCE_AUDIT中记录，不归算为root全文实读。

有限历史检索覆盖 exterior-pressure、modulated-swirl-screen、support-invariance、relative-energy-error-preflight 四个既有目录中的解析/紧支撑/力关键词；不是全库新颖性调查。root本轮全文读 support-invariance/PROOF 和 relative-energy-error-preflight/PROOF。前者已有完整Wiener温和解与支撑筛选接口，后者已有完整残差相对能量/同寿命边界；本题不把它们重算为新定理。旧exterior-pressure、modulated-swirl具体命中段只用于定位，它们对指定外环/压力路径的限制不能用来否定新构造的精确热外场。

新输入只是对新原文“每切片固定空间开空区”与“非平凡零投影力尾段”的精确相容性检验；空间解析性与恒等原理是经典工具，不主张原创优先权。root给全频率局部证明与实际轨道识别，避免把外部小数据全局定理超范围用于这里。

本轮外部解析性检索的可用范围：Foias–Temam 1989 JFA Gevrey文章的出版社入口返回403，Lemarié-Rieusset 2000 R³ mild解析性文章入口429，均不称全文读过；仅有元数据定位，不列为本题证明依赖。实际打开 https://arxiv.org/abs/2205.12383 （v1，Ambrose–Lopes Filho–Nussenzveig Lopes）摘要，确认Wiener方法和周期解析性已有文献。没有用其小数据全局结论代替本题任意给定光滑切片的局部证明。

所有新增科学执行0、PDE模拟0、数组打开0、Lean构建0；有PDF抽取/必要渲染与字节校验。此前31包及所有旧worker不重跑、不重复交接。annular-third-order-preflight的非正式合同前推导原样另存未审记录，不算本题证书。
