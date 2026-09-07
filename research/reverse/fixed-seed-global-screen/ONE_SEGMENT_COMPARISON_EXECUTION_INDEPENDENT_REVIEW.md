# 单段比较执行的独立审查

状态：**ARITHMETIC_AGREEMENT_WITH_PRODUCER_RESOURCE_EVIDENCE_GAP**。

本报告为既有固定单段档案的执行记录审查。比较器的完整算术对照通过，生产器资源证据缺口继续保留。不得据此称完整科学证书、完整资源验收或可发布冻结包。

## 1. 实读与执行范围

审查者全文读取本次 `run.json`、`comparison.json`、`final-receipt.json`、配置与两份外层标准输出/错误记录，逐项检查全部九条变异记录及汇总有理数接口；另实际字节读取本次六项输出文件计算长度和 SHA。未导入或执行比较器，未执行任何空间核、时间积分或科学数组解码，未第三次逐元素比较两个生产器的档案。

本次完整逐元素对照由已非作者全文审查的固定比较器执行。这里结合其冻结源、实际执行记录、全部计数、变异证据、最终收据与外部退出证据，验收其限定执行结果；不把这份元数据审查称为第三套完整算术复算。

元数据与小型 Fraction 断言实际执行于 2026-09-07 21:03:08.244290 UTC，结果 PASS；准确执行脚本保存于本报告附录。之后另对根代理的外部退出验收 JSON 作 SHA/JSON 断言：其 session 82913、exit_code 0、源提交及 run/result/receipt SHA 与实读文件相符。审查者没有亲自取得该工具会话的退出事件，外部事件由根代理见证，来源在第 7 节单列。

## 2. 源与最终状态闭合

本次源码 SHA 为 `7e09b766feb86ac70bb1b05957903320d41069637d4c2ee23e8ebed88c6bd294`，源提交为 `2e7ded4313eddbe7c2d7cbefc503d7bcb671b154`。实际源快照、当前比较器文件与 run/result 的源绑定一致。固定配置 SHA 为 `c4a44731f0ce8f612533d1e76957bca7a8ca3705e03c05a8d08929281ecd382e`；落盘 configuration JSON 等于 run 的 preflight。

运行实际绑定的根源审查是 `ONE_SEGMENT_COMPARATOR_ROOT_SOURCE_REVIEW.md`，SHA `2b4d1a885d74cd9eb0b87aba92c4e32edd88e1109f380014e53fa79c24ed611d`，本审查实际核验了该文件字节。

run、comparison、末行 stdout、receipt 均为本报告顶端的限定状态，以下四项均是 JSON 布尔值 false：

- `producer_resource_complete`
- `resource_complete`
- `certificate_ready`
- `release_ready`

stdout 与 receipt 指向实际 run SHA，三处结果描述均指向同一个 comparison JSON 的实际字节、SHA。stderr 为空；外部退出证据为 exit 0。run 保存的 UTC 起止为 20:53:47.936396 至 20:53:51.368922；成本采用包含预核在内的单调时钟观测，不以这两个 UTC 字段之差代替。

## 3. 完整对象计数与区间接口

run 和 comparison 的完整计数一致：

| 对象 | 实际计数 | 固定覆盖解释 |
|---|---:|---|
| tensor_scalars | 2,587,464 | 6 张量 × 6 增量幂层 × 35,937 输出 × 实虚 2 |
| W_scalars | 1,509,354 | 7 幂层 × 35,937 输出 × 6 实虚分量 |
| S_scalars | 467,181 | 13 幂层 × 35,937 输出 |
| new_center_scalars | 88,416 | 3 新幂层 × 4,912 输入 × 6 实虚分量 |
| original_power_scalars | 117,888 | 4 原幂层 × 4,912 输入 × 6 实虚分量 |
| old_center_scalars | 29,472 | 4,912 输入 × 6 实虚分量 |
| rounding_witnesses_connected | 117,888 | 全部四层舍入见证 |

比较结果记录全量张量、W、S、中心和原始系数一致。H2 的 13 项幂系数与 13 项 Bernstein 系数相等；H0 的相应精确值包含于主核给出的区间。所有输出模式保留，计数未只取独立半谱、零频或选定模式。

已实读结果记录的空间核/求解器调用数及生产重复次数均为 0，`whole_W_square_recomputed=false`。这对应已审比较算法的范围；本审查不重新计算 W 平方。

## 4. 全部七项实际与两项合成负对照

九项记录均满足 baseline_passed=true、mutation_rejected=true。记录的 validator 与错误码如下，和已审来源中的同一验证函数路径相符：

| 类型与变异 | 同一 validator | 实际拒绝码 |
|---|---|---|
| 实际非零新张量分量 | validate_tensor | SCALAR_MISMATCH: TENSOR_12 |
| 实际极化分子改成奇数 | validate_tensor | POLARIZATION_ODD_NUMERATOR |
| 实际 W 虚部相位 | validate_equal | SCALAR_MISMATCH: W |
| 实际有符号 S | validate_equal | SCALAR_MISMATCH: S |
| 实际新中心 | validate_equal | SCALAR_MISMATCH: center |
| 实际零阶区间收窄后排除真值 | validate_containment | INTERVAL_EXCLUDES_EXACT_VALUE: mutated interval |
| 实际来源文件 SHA 不匹配 | validate_digest | SHA_MISMATCH: audit_one_segment_residual.py |
| 合成负数错误截断 | validate_floor | SIGNED_FLOOR |
| 合成有理根号错误等号 | validate_root | ROOT_TRUE_RATIONAL_CEIL |

实际见证的进一步核验：张量 12 在 scalar_index=4 的非零独立值为 15327801026608959401063673；W 的 scalar_index=25 为虚部且非零；S 的 scalar_index=3 非零；新中心 power=1、local_scalar=6 的两边基线均为 −59353050881。源 SHA 见证绑定实际旧主源的字节。

区间变异不是任意平移的伪例。对已保存的非零真值 x，原区间 [l,u] 满足 l≤x≤u；实际变异保留 l，将上端改为 (l+x)/2。小型 Fraction 断言核实这是原区间的真子区间，且排除 x，原端点与原区间宽度限制不被绕过。附录脚本也允许原合同中另一端的对称分支，但本次记录落在上述分支。

两项合成边界均有 synthetic=true：−3/2 的正确 floor/ceil 为 −2/−1；9/8 在 scale=2 下真实放大有理数为 9/2，取整值 4 为完全平方不能推出真实有理数根号恰为整数。本审查核验记录及其小有理数关系，未重跑 mutation validator 或根号核。

这些负对照证明实际比较验证路径识别了所规定的七类具体档案错误及两类边界错误；不推广成任意错误都会被发现。

## 5. Gamma 与固定阈值

读取保存的有理上界后，本审查仅对已有汇总分数作精确 Fraction 断言：

Γ_main = (3584/1023) max(r̄₂_main, 64 r̄₀_main)，

Γ_independent = (3584/1023) max(r̄₂_independent, 64 r̄₀_independent)。

两边原残差上界逐项相等，因而两边 Γ 精确相等，且

Γ_main = Γ_independent < 2/8085825。

两边均记录 `SEGMENT_UPPER_BOUND_WITHIN_EXISTING_SUFFICIENT_THRESHOLD`，same_threshold_status=true。完整精确分子/分母保存在第 7 节绑定的 comparison JSON，本报告不使用小数近似替代不等式。

这仅检查固定原 Hermite 单段的既有充分阈值接口。没有选择新 epsilon；没有支付其余时间段的导数/残差预算，也没有得到全时间窗真实 NS 控制结论。两个生产器的资源证据缺口进一步阻止把该有限结果称为完整科学证书。

## 6. 本次比较器的字节与资源收据

实际输出六文件加外层 stdout/stderr 共 154,601 字节。分阶段精确账目为：

- run 写入前 131,866 字节，加 run 的 20,958 字节，得 152,824。
- 加实际 stdout 的 646 字节，得 receipt 写入前 153,470。
- 加 receipt 的 1,131 字节，得最终 154,601；stderr 为 0 字节。

末次收据观测耗时 3.706704084062949 秒、SELF 峰值 RSS 199,491,584 字节，低于固定 120 秒、256 MiB、8 MiB 上限。stdout 与 receipt 的峰值相同；run 写入前的较早峰值 199,475,200 字节较低，不是不一致。run/receipt 的单进程无子进程记录与该冻结比较器已审调用路径相符。本次自身资源验收依据该路径、实际收据、输出字节和外部 exit 0；不是仅凭一个 JSON 布尔字段。

源码在 receipt 写后还检查实际总字节和峰值是否仍与收据一致，并检查预算；不通过则使成功 run 的绑定失效。因而 receipt 与外部 exit 0 必须共同使用。这里报告的是可记录的末次观测，不另造退出后未采样的耗时或 RSS 数值。

**生产器缺口未修复。** 两个此前生产器使用 platform 标准库触发的 uname/file 路径缺少逐子进程身份、峰值和完整日志；本次单进程比较费用不能替它们补证。原始源、数据和旧验收字节保持历史事实，新限定状态更正其可解释范围，不事后豁免预算，不猜测未观测的内存。

## 7. 实际输入字节绑定

下表路径均相对于 `research/reverse/fixed-seed-global-screen/`。

| 文件 | 字节 | SHA256 |
|---|---:|---|
| one-segment-residual-comparison-trial-01/comparison.json | 34573 | c0e454ac4fd980344c29704bdabb3e7dd8c00e00daac8942f3621d2c2428eba8 |
| one-segment-residual-comparison-trial-01/run.json | 20958 | 1130f56738d77a57f0227a2289b7a56fe543c49c5f86b2ba0a3dbc839247557a |
| one-segment-residual-comparison-trial-01/final-receipt.json | 1131 | 2943f90b98b34513d225e4cfe7447444d13287c369e16677f6e84dd84d8f389a |
| one-segment-residual-comparison-trial-01/configuration.json | 18774 | af73a80a240be29d13391e886d45975d5f737df381a4b4b254ec59abc7ebdb79 |
| one-segment-residual-comparison-trial-01/claim.json | 20036 | 74a3cf07266e8e8f81fd76904ebe3eab166695f8e6d52735f3105daae67b7575 |
| one-segment-residual-comparison-trial-01/source-snapshot.py | 58483 | 7e09b766feb86ac70bb1b05957903320d41069637d4c2ee23e8ebed88c6bd294 |
| one-segment-residual-comparison.stdout.log | 646 | 6d4e44fc429d63a6aa6921218710d22af6d7763abfb7f5d872b00ac52d3a54dd |
| one-segment-residual-comparison.stderr.log | 0 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| one-segment-comparison-root-execution-acceptance.json | 29126 | 35da6abd32a7b3cec346c11ca43661f5cadb7896dc37a24de6f19f76fed594ee |

根验收文件中的源/档案大哈希表是根代理的实际字节复核记录；本审查未重做其全部 141 项科学来源哈希。实际重新核的是本节文件、当前比较器和运行时根源审文件。根验收记录一次元数据写入时路径修正，明确没有重复科学核或比较器；该说明不被计作第三次科学运行。

来源限定继续受已冻结的三项补充约束：

- ONE_SEGMENT_HIDDEN_HELPER_RESOURCE_AUDIT.md：c971a90e0c7d230bd25df1dd80b2e27c74b9af089ad6194099e217e981a77c87。
- ONE_SEGMENT_COMPARISON_RESOURCE_GAP_ADDENDUM.md：212df48b07648511024524ab746d41ec3e419914cb111862ae3569663ccf9355。
- ONE_SEGMENT_COMPARISON_RESOURCE_GAP_INDEPENDENT_REVIEW.md：36141219e713ed8a72cb1c6cef9609d00e86aed36f7fd7d80e242d0331562e06。

这些三项是之前已实读审查的来源限定；本次实际执行输入还通过比较器的固定 pins 连接。未为本报告重算旧科学档案。

## 8. 审查结论

未发现本次限定算术对照的未解决阻断。完整对象计数、七项实际变异拒绝、两项合成边界拒绝、精确 Gamma 阈值关系及比较器自身最终账目相容。唯一允许的执行状态仍为 **ARITHMETIC_AGREEMENT_WITH_PRODUCER_RESOURCE_EVIDENCE_GAP**，四个 false 不变。

未解决项是两次生产的资源证据缺口，以及本单段以外仍未支付的数学/计算合同。没有全窗证书、全局判定或 NS 奇性结论。

## 附录：实际执行的元数据/Fraction 断言

以下为实际执行源码，未导入比较器或科学核。执行器为 bundled Python 3.12.14，参数 `-B -`，cwd 为反向工作树。其输出摘要为 metadata_fraction_assertions=PASS、7+2 变异记录、Gamma 精确相等并严格低于固定阈值、four_flags_false=true、output_bytes=154601、kernels_or_comparator_imported_or_executed=false。这是实际一次只读断言记录，不是待运行脚本。

```python
from pathlib import Path
from fractions import Fraction
from hashlib import sha256
import json,datetime
b=Path('research/reverse/fixed-seed-global-screen')
d=b/'one-segment-residual-comparison-trial-01'
j=lambda p:json.loads(p.read_bytes())
h=lambda p:sha256(p.read_bytes()).hexdigest()
run=j(d/'run.json'); c=j(d/'comparison.json'); rec=j(d/'final-receipt.json')
stdout=b/'one-segment-residual-comparison.stdout.log'; stderr=b/'one-segment-residual-comparison.stderr.log'
out=json.loads(stdout.read_text().splitlines()[-1])
S='ARITHMETIC_AGREEMENT_WITH_PRODUCER_RESOURCE_EVIDENCE_GAP'
flags=['producer_resource_complete','resource_complete','certificate_ready','release_ready']
for obj in [run,c,rec,out]:
    assert obj['status']==S
    assert all(obj[k] is False for k in flags)
assert run['source_sha256']==c['source_sha256']==h(d/'source-snapshot.py')==h(b/'compare_one_segment_residual.py')=='7e09b766feb86ac70bb1b05957903320d41069637d4c2ee23e8ebed88c6bd294'
assert run['checkout']==c['checkout'] and run['checkout']['commit']=='2e7ded4313eddbe7c2d7cbefc503d7bcb671b154'
assert j(d/'configuration.json')==run['preflight']
review=run['preflight']['runtime_root_source_review']
assert h(Path(review['path']))==review['sha256']
assert c['config_sha256']==run['config_sha256']==run['preflight']['config_sha256']
assert out['run_sha256']==rec['run_sha256']==h(d/'run.json')
for obj in [run,out,rec]:
    assert obj['result']=={'file':'comparison.json','bytes':(d/'comparison.json').stat().st_size,'sha256':h(d/'comparison.json')}
counts={'tensor_scalars':2587464,'W_scalars':1509354,'S_scalars':467181,'new_center_scalars':88416,'original_power_scalars':117888,'old_center_scalars':29472,'rounding_witnesses_connected':117888}
assert run['counts']==c['counts']==counts
a=c['mutation_controls']['actual_nonzero_archive_mutations']
s=c['mutation_controls']['synthetic_boundary_mutations']
expected=[
('actual_new_tensor_component','validate_tensor','SCALAR_MISMATCH: TENSOR_12'),
('actual_polarization_odd_numerator','validate_tensor','POLARIZATION_ODD_NUMERATOR'),
('actual_W_imaginary_phase','validate_equal','SCALAR_MISMATCH: W'),
('actual_signed_S','validate_equal','SCALAR_MISMATCH: S'),
('actual_new_center','validate_equal','SCALAR_MISMATCH: center'),
('actual_zero_order_interval_excludes_truth','validate_containment','INTERVAL_EXCLUDES_EXACT_VALUE: mutated interval'),
('actual_source_sha_mismatch','validate_digest','SHA_MISMATCH: audit_one_segment_residual.py')]
assert [(x['name'],x['validator'],x['actual_error']) for x in a]==expected
assert len(s)==2 and run['actual_mutations_rejected']==7 and run['synthetic_boundary_mutations_rejected']==2
assert all(x['baseline_passed'] is True and x['mutation_rejected'] is True for x in a+s)
for item in a[:2]: assert int(item['evidence']['independent_value'])!=0
for item in a[2:5]: assert int(item['evidence']['left'])==int(item['evidence']['right'])!=0
assert a[2]['evidence']['scalar_index']%2==1
assert a[4]['evidence']['power'] in (1,2,3)
F=lambda v:Fraction(int(v[0]),int(v[1]))
w=a[5]['evidence']; lo,x,hi,bl,bh=map(F,[w['lower'],w['actual'],w['upper'],w['mutated_lower'],w['mutated_upper']])
assert x!=0 and lo<=x<=hi and lo<=bl<=bh<=hi and not(bl<=x<=bh)
assert (bl==lo and bh==(lo+x)/2) or (bh==hi and bl==(x+hi)/2)
assert w['strict_original_subinterval'] is True and w['one_original_endpoint_unchanged'] is True
assert a[6]['evidence']['sha256']==h(b/'audit_one_segment_residual.py')
assert [(v['validator'],v['actual_error']) for v in s]==[('validate_floor','SIGNED_FLOOR'),('validate_root','ROOT_TRUE_RATIONAL_CEIL')]
assert all(v['evidence']['synthetic'] is True for v in s)
assert F(s[0]['evidence']['fraction'])==Fraction(-3,2)
assert F(s[1]['evidence']['argument'])*s[1]['evidence']['scale']**2==F(s[1]['evidence']['true_scaled_argument'])==Fraction(9,2)
n=c['norms_and_fixed_control_interface']
assert n['H2_power_and_Bernstein_equal'] is True and n['H0_power_and_Bernstein_contained'] is True
assert n['power_coefficients_compared_each_order']==n['Bernstein_coefficients_compared_each_order']==13
rm={k:F(v) for k,v in n['original_segment_upper_main'].items()}
ri={k:F(v) for k,v in n['original_segment_upper_independent'].items()}
gm,gi=F(n['Gamma_main']),F(n['Gamma_independent_derived_here'])
assert gm==Fraction(3584,1023)*max(rm['2'],64*rm['0'])
assert gi==Fraction(3584,1023)*max(ri['2'],64*ri['0'])
assert gm==gi<Fraction(2,8085825) and rm==ri
assert n['Gamma_main_status']==n['Gamma_independent_status']=='SEGMENT_UPPER_BOUND_WITHIN_EXISTING_SUFFICIENT_THRESHOLD'
assert n['same_threshold_status'] is True and n['new_epsilon_selected'] is False and n['full_window_or_NS_claim'] is False
assert c['spatial_kernel_or_solver_invocations']==c['independent_productions_repeated']==0 and c['whole_W_square_recomputed'] is False
for path in [stdout,stderr]:
    assert rec['external_stdio'][str(path.resolve())]=={'bytes':path.stat().st_size,'sha256':h(path)}
assert stderr.stat().st_size==0
total=sum(p.stat().st_size for p in d.iterdir() if p.is_file())+stdout.stat().st_size+stderr.stat().st_size
assert rec['receipt_bytes']==(d/'final-receipt.json').stat().st_size==1131
assert rec['observed_after_stdout_flush']['all_output_bytes']+1131==rec['all_output_bytes_including_receipt']==total==154601
assert out['post_run_write_observation']['all_output_bytes']+stdout.stat().st_size==rec['observed_after_stdout_flush']['all_output_bytes']
assert out['post_run_write_observation']['peak_rss_bytes']==rec['observed_after_stdout_flush']['peak_rss_bytes']==199491584
for obs in [run['resources_before_run_record_write'],out['post_run_write_observation'],rec['observed_after_stdout_flush']]:
    assert obs['single_process_no_children'] is True and obs['elapsed_seconds']<120 and obs['peak_rss_bytes']<=256*1024**2 and obs['all_output_bytes']<=8*1024**2
assert run['preflight']['resource_lock']=={'wall_seconds':120,'rss_bytes':256*1024**2,'output_bytes':8*1024**2}
print(json.dumps({'audit_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'metadata_fraction_assertions':'PASS','status':S,'counts':counts,'actual_mutations':len(a),'synthetic_mutations':len(s),'Gamma_main_equals_independent_below_fixed_threshold':True,'four_flags_false':True,'output_bytes':total,'receipt_elapsed_seconds':rec['observed_after_stdout_flush']['elapsed_seconds'],'peak_rss_bytes':rec['observed_after_stdout_flush']['peak_rss_bytes'],'run_sha256':h(d/'run.json'),'comparison_sha256':h(d/'comparison.json'),'receipt_sha256':h(d/'final-receipt.json'),'review_runtime_sha256':review['sha256'],'kernels_or_comparator_imported_or_executed':False},indent=2))

```

附录执行后，另一次只读 JSON/SHA 核验将根外部退出验收的 session_id=82913、exit_code=0、源 SHA/提交、run/result/receipt SHA、154601 字节、四个 false 绑定到上表实际文件，输出 `root_external_exit_attestation_binding: PASS`。该补充不调用 Fraction 或科学运算。

