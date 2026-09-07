#!/usr/bin/env python3
"""PRIVATE_CORE. Exact hypotheses of the current-support driver theorem.

No new fourth jet, time-stepper, or finite Galerkin evolution is used.
"""
import argparse,hashlib,json,sys
from fractions import Fraction as F
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'first-cycle'))
import exact_algebra as x
HERE=Path(__file__).resolve().parent

def norm2(v):
    return sum((z.re*z.re+z.im*z.im for z in v),F(0))
def inner(v,w):
    return sum((z.re*y.re+z.im*y.im for z,y in zip(v,w)),F(0))
def subfield(f,S,inside):return {k:v for k,v in f.items() if (k in S)==inside}

def calculate():
    a=x.cyclic_seed();S=set(a);N=x.B(a,a);C=x.fadd(x.B(a,N),x.B(N,a));b=x.fadd(x.L(a),N);c=x.fadd(x.L(b),x.B(a,b),x.B(b,a))
    W2=x.fmul(F(1,2),subfield(c,S,False));q=(2,1,1)
    fields={'g':x.B(N,N),'s_plus':x.B(a,W2),'s_minus':x.B(W2,a)}
    vv={name:field.get(q,x.ZERO) for name,field in fields.items()}
    ss=x.vadd(vv['s_plus'],vv['s_minus']);F0=x.vadd(vv['g'],ss);v=x.vmul(F(1,3),F0)
    t0=F(1,10000);t=F(1,1000000);EG=F(1861);ES=F(2670);MQ=F(1802);EP=F(6000)
    lower={'g':F(1154,1000),'s_plus':F(912,1000),'s_minus':F(288,1000),'s_net':F(763,1000)}
    upper={'g':F(1155,1000),'s_plus':F(914,1000),'s_minus':F(289,1000),'s_net':F(765,1000)}
    all_vectors={**vv,'s_net':ss}
    brackets={name:lower[name]**2<norm2(vec)<upper[name]**2 for name,vec in all_vectors.items()}
    power={name:inner(v,vec) for name,vec in vv.items()};power['s_net']=power['s_plus']+power['s_minus']
    gaps={
       'vector_net_margin':lower['g']-F(7,5)*upper['s_net']-(EG+F(7,5)*2*ES)*t,
       'vector_absolute_failure_margin':lower['s_plus']+lower['s_minus']-upper['g']-(EG+2*ES)*t,
       'power_seed_net_positive':power['s_net']-2*EP*t,
       'power_net_dominance_margin':power['g']-F(3,2)*power['s_net']-4*EP*t,
       'power_absolute_failure_margin':power['s_plus']-power['s_minus']-power['g']-3*EP*t,
       'power_g_positive':power['g']-EP*t,
       'power_s_plus_positive':power['s_plus']-EP*t,
       'power_s_minus_negative_margin':-power['s_minus']-EP*t,
       'mode_energy_growth_margin':sum(power[z] for z in ['g','s_plus','s_minus'])-(3*EP+24)*t,
    }
    estimates={
       'newborn_first_difference_coefficient':F(30)+143*t0,
       'seed_difference_coefficient':F(6)+3*t0+143*t0*t0,
       'G_error_before_rounding':F(5,2)*(24*31+31*31*t0),
       'S_error_before_rounding':F(5,2)*(7*30+6*143),
       'mode_error_before_rounding':(EG+2*ES)/4+1,
       'power_G_error_before_rounding':EG+2*MQ+MQ*EG*t,
       'power_S_error_before_rounding':ES+MQ+MQ*ES*t,
    }
    expected={'g':x.vmul(x.QI(F(0),F(1,3)),x.vec((-2,2,2))),'s_plus':x.vmul(x.QI(F(0),F(1,6)),x.vec((-2,-1,5))),'s_minus':x.vmul(x.QI(F(0),F(1,6)),x.vec((1,-1,-1)))}
    checks={
       'all_fields_real_divfree_mean_zero':all(x.allowed(f) for f in [a,N,C,b,c,W2,*fields.values()]),
       'seed_b_minus_a':subfield(b,S,True)==x.fmul(-1,a),
       'seed_c_minus_a':subfield(c,S,True)==x.fmul(-1,a),
       'N_seed_free':not subfield(N,S,True),
       'N_A_12':x.component_l1_upper(N)==12,
       'W2_A_30':x.component_l1_upper(W2)==30,
       'output_absent_in_S_plus_S':q not in {tuple(i+j for i,j in zip(p,r)) for p in S for r in S},
       'output_absent_in_S_plus_N_support':q not in {tuple(i+j for i,j in zip(p,r)) for p in S for r in N},
       'all_three_target_vectors':vv==expected,
       'target_phase_transversality':all(not x.dot(vec,q) for vec in [*vv.values(),F0,v]),
       'v_norm_at_most_one':norm2(v)<=1,
       'F0_norm_at_most_two':norm2(F0)<=4,
       'g_norm_at_most_two':norm2(vv['g'])<=4,
       's_norms_at_most_one':all(norm2(vv[z])<=1 for z in ['s_plus','s_minus']),
       'l_upper_ball':143*t0*t0 <= 6 and 1-t0-t0*t0/2>0,
       'l_difference_7':estimates['seed_difference_coefficient']<=7,
       'w_difference_31':estimates['newborn_first_difference_coefficient']<=31,
       'w_norm_13t':12+31*t0<=13,
       'l_norm_at_least_5':6-7*t>=5,
       'G_error_1861':estimates['G_error_before_rounding']<EG,
       'S_error_2670':estimates['S_error_before_rounding']<=ES,
       'mode_error_1802':estimates['mode_error_before_rounding']<MQ,
       'power_error_6000':max(estimates[z] for z in ['power_G_error_before_rounding','power_S_error_before_rounding'])<EP,
       'mode_norm_2t3':1+MQ*t<=2,
       'window_inside_inherited':0<t<=t0,
       'sqrt_brackets':all(brackets.values()),
       'exact_modal_powers':power=={'g':F(5,9),'s_plus':F(4,9),'s_minus':F(-5,36),'s_net':F(11,36)},
       'all_positive_time_gaps':all(gap>0 for gap in gaps.values()),
    }
    wrongG=x.ZERO
    wrong_phase=x.vmul(-1,vv['s_minus'])
    rawN=x.bilinear(a,a,project=False)[0]
    rawC=x.fadd(x.bilinear(a,rawN,project=False)[0],x.bilinear(rawN,a,project=False)[0])
    rawW=x.fmul(F(1,2),subfield(x.fadd(a,x.fmul(-4,rawN),rawC),S,False))
    rawfields=[x.bilinear(rawN,rawN,project=False)[0],x.bilinear(a,rawW,project=False)[0],x.bilinear(rawW,a,project=False)[0]]
    mutations={
       'delete_newborn_self_interaction':wrongG!=vv['g'],
       'delete_full_Leray':any(f.get(q,x.ZERO)!=vv[name] for f,name in zip(rawfields,['g','s_plus','s_minus'])),
       'flip_seed_feedback_phase':inner(v,wrong_phase)>0 and power['s_minus']<0,
       'infer_absolute_dominance_from_net':lower['s_plus']+lower['s_minus']>upper['g'],
       'discard_s_minus':ss!=vv['s_plus'],
       'inflate_window_invalidates_absolute_power_gap':F(1,36)-3*EP*t0<0,
    }
    assert all(checks.values()),checks;assert all(mutations.values()),mutations
    return {'schema':'ReverseNS-current-support-driver-certificate-v1','classification':'PRIVATE_CORE','release_id':'ReverseNS-20260907-DriverDominance','split':'l=P_S u,w=(I-P_S)u; S=the six initial signed axis modes','target':q,'T0':str(t0),'T':str(t),'EG':str(EG),'ES':str(ES),'MQ':str(MQ),'EP':str(EP),'source_dependencies':{'first_cycle_source_commit':'90c44d1703486e3983d12b87ed54f22c8c677982','mixed_checkpoint_commit':'b7ce9a3473ac01a7396c9d11751caf5a9b62a94e'},'fields':{name:x.pack_field(field) for name,field in {'a':a,'N':N,'C':C,'b':b,'c':c,'W2':W2,**fields}.items()},'target_vectors':{name:x.pack_vec(vec) for name,vec in {**all_vectors,'F0':F0,'v':v}.items()},'target_squared_norms':{name:str(norm2(vec)) for name,vec in {**all_vectors,'F0':F0,'v':v}.items()},'sqrt_brackets':{name:[str(lower[name]),str(upper[name])] for name in lower},'leading_powers':{k:str(v) for k,v in power.items()},'rational_estimates':{k:str(v) for k,v in estimates.items()},'strict_gaps':{k:str(v) for k,v in gaps.items()},'checks':checks,'negative_mutations_detected':mutations,'status':'PASS','meaning':'Finite exact algebra and hypotheses of the analytic full-PDE theorem; not a standalone proof of PDE or regeneration.','max_new_time_derivative_order':3,'spectral_truncation':False}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');args=ap.parse_args();result=calculate();payload=json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)+'\n';out=HERE/'driver-certificate.json'
    if args.check:assert out.read_text()==payload,'driver certificate changed'
    else:out.write_text(payload)
    print(json.dumps({'status':result['status'],'checks':len(result['checks']),'mutations':len(result['negative_mutations_detected']),'T':result['T'],'gaps':result['strict_gaps']}))
if __name__=='__main__':main()
