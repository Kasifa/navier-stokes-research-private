#!/usr/bin/env python3
"""PRIVATE_CORE. Finite third-jet diagnostic only; no PDE remainder claim."""
import sys,json,argparse
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'first-cycle'))
import exact_algebra as x

def calc():
    sums=[{} for _ in range(4)]
    rows=[]
    for mask in range(8):
        amplitudes=tuple(int(bool(mask&(1<<i))) for i in range(3))
        a=x.prune(x.cyclic_seed(amplitudes));b=x.fadd(x.L(a),x.B(a,a))
        c=x.fadd(x.L(b),x.B(a,b),x.B(b,a))
        d=x.fadd(x.L(c),x.B(a,c),x.B(c,a),x.fmul(2,x.B(b,b)))
        sign=(-1)**(3-sum(amplitudes))
        jets=[a,b,c,d]
        sums=[x.fadd(s,x.fmul(sign,j)) for s,j in zip(sums,jets)]
        rows.append({'mask':mask,'sign':sign,'amplitudes':amplitudes,'support_sizes':[len(v) for v in jets]})
    af=x.cyclic_seed(); nf=x.B(af,af); cf=x.fadd(x.B(af,nf),x.B(nf,af)); q=(2,1,1)
    channels={'2B_N_N':x.fmul(2,x.B(nf,nf)),'B_a_C':x.B(af,cf),'B_C_a':x.B(cf,af)}
    channel_data={name:x.pack_vec(field.get(q,x.ZERO)) for name,field in channels.items()}
    checks={'derivatives_0_1_2_all_three_mixed_zero':all(not v for v in sums[:3]),'third_mixed_nonzero':bool(sums[3]),'third_mixed_real_divfree_mean_zero':x.allowed(sums[3])}
    out={'classification':'PRIVATE_CORE','status':'FINITE_DIAGNOSTIC_NOT_REGENERATION','max_derivative_order':3,'viscosity':'1','masks':rows,'mixed_jets':[x.pack_field(f) for f in sums],'q_target':q,'q_quartic_channels':channel_data,'support_sizes':[len(f) for f in sums],'component_l1_upper':[str(x.component_l1_upper(f)) for f in sums],'checks':checks,'interpretation':'Inclusion-exclusion of derivatives of different deleted-seed solutions isolates polynomial terms using all three groups. This combination is not itself a Navier-Stokes solution or an autonomous subsystem. No new positive-time remainder or regeneration claim.'}
    return out

def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();d=calc();out=Path(__file__).with_name('mixed-result.json');s=json.dumps(d,ensure_ascii=False,indent=2,sort_keys=True)+'\n'
 if a.check:assert out.read_text()==s
 else:out.write_text(s)
 print(json.dumps({k:d[k] for k in ['status','support_sizes','component_l1_upper','checks']}))
if __name__=='__main__':main()
