#!/usr/bin/env python3
"""Exact finite certificate for the constants used in the full-PDE proof.

This verifies algebra and rational inequalities, not the analytic proof itself.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import copy
import hashlib
import json
import os
import platform
import subprocess
import sys
import time
import exact_algebra as alg

HERE = Path(__file__).resolve().parent

def calculate():
    raw = alg.calculation()
    bds = {k:F(v) for k,v in raw['component_l1_upper_bounds'].items()}
    T = F(1,10000)
    A,B,C = (bds[k] for k in ('a','b','c'))
    D2,D3,D4 = (bds[k] for k in ('t2','t3','t4'))
    M = 2*(D2/3+D3*T/4+D4*T*T/5)
    u_bound = A+B*T+C*T*T/2
    checks = {
        'exact_primary_checks': all(raw['checks'].values()),
        'A_6': A == 6,
        'contraction_T_condition': 256*A*A*T <= 1,
        'polynomial_ball': u_bound <= 2*A,
        'M_less_than_143': M < 143,
        'first_target_lower_bound': 1-2*T-143*T*T >= F(1,2),
        'second_target_lower_bound': F(1,2)-143*T >= F(1,4),
        'zero_forcing_fixed_viscosity': raw['forcing'] == '0' and raw['viscosity']=='1',
        'reduced_global_class_same_observations':raw['checks']['globally_smooth_control_same_jk_jets'],
    }
    a=alg.cyclic_seed();n=alg.B(a,a)
    fullC=alg.fadd(alg.B(a,n),alg.B(n,a))
    noP=alg.fadd(alg.bilinear(a,n,project=False)[0],alg.bilinear(n,a,project=False)[0])
    k=(2,1,0);pressure=(1,1,-1)
    contaminated=dict(a);contaminated[k]=alg.vec((0,0,1));contaminated[(-2,-1,0)]=alg.vec((0,0,1))
    plus_only={q:v for q,v in a.items() if sum(q)>0}
    mutations={
        'delete_Leray_projection': noP != fullC and noP[pressure]==alg.vec((2,2,-2)),
        'delete_return_to_seed_feedback': {q:v for q,v in fullC.items() if q not in a} != fullC,
        'set_viscosity_zero': alg.fadd(alg.L(a),n) != n,
        'delete_conjugate_seed_modes': not alg.allowed(plus_only),
        'preseed_second_target': alg.allowed(contaminated) and k in contaminated,
        'inflate_time_to_one': not (256*A*A*F(1) <= 1),
    }
    # Recomputed-object equality rejects a tampered exact residual and sign.
    def equal_to_recomputation(obj):
        return obj == raw
    bad=copy.deepcopy(raw);bad['component_l1_upper_bounds']['t4']='0'
    mutations['erase_nonzero_quartic_residual_bound']=not equal_to_recomputation(bad)
    bad=copy.deepcopy(raw);bad['target_usecond0'][2]['re']='1'
    mutations['flip_second_target_sign']=not equal_to_recomputation(bad)
    assert all(checks.values()), checks
    assert all(mutations.values()), mutations
    return {
        'schema':'ReverseNS-full-PDE-remainder-constants-v1',
        'classification':'PRIVATE_CORE',
        'release_id':'ReverseNS-20260907-TwoGeneration',
        'baseline_commit':'d58abdd9390ef8ced52f1807a956a663853f7680',
        'algebra_sha256':hashlib.sha256((HERE/'algebra-result.json').read_bytes()).hexdigest(),
        'time':str(T),'A':str(A),'b_upper':str(B),'c_upper':str(C),
        'residual_upper':{'D2':str(D2),'D3':str(D3),'D4':str(D4)},
        'M_exact':str(M),'M_upper':'143','U_upper':str(u_bound),
        'checks':checks,'negative_mutations_detected':mutations,
        'status':'PASS',
        'meaning':'Exact finite algebra and rational hypotheses for PROOF.md; infinite-dimensional existence and error bound require that analytic proof and independent review.',
        'accepted':'Finite two-generation creation in one fixed smooth solution',
        'not_accepted':'Autonomous regeneration, uniform iteration, fixed-datum infinite cascade, finite-time singularity, novelty',
        'spectral_truncation':False,'formal_figures':[],
    }

def main():
    p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');p.add_argument('--run-log',type=Path);args=p.parse_args()
    start=time.perf_counter();d=calculate();payload=json.dumps(d,indent=2,ensure_ascii=False,sort_keys=True)+'\n';output=HERE/'certificate.json'
    if args.check:
        assert output.read_text()==payload,'certificate.json differs from exact recomputation'
    else: output.write_text(payload)
    elapsed=time.perf_counter()-start
    if args.run_log:
        try: cpu=subprocess.check_output(['sysctl','-n','machdep.cpu.brand_string'],text=True).strip()
        except (OSError,subprocess.CalledProcessError): cpu=platform.machine()
        run={'command':'python3 research/reverse/first-cycle/certify.py'+(' --check' if args.check else ''),
             'python':platform.python_version(),'cpu':cpu,'logical_cpus':os.cpu_count(),
             'workers':1,'gpu':False,'arithmetic':'exact Fraction and rational-complex; no PDE time stepper',
             'random_seed':None,'solver_tolerance':None,'wall_seconds':elapsed,
             'status':d['status'],'checks':len(d['checks']),'negative_mutations':len(d['negative_mutations_detected']),
             'certificate_sha256':hashlib.sha256(output.read_bytes()).hexdigest()}
        args.run_log.write_text(json.dumps(run,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':d['status'],'checks':len(d['checks']),'negative_mutations':len(d['negative_mutations_detected']),'T':d['time'],'M_upper':d['M_upper']}))
if __name__=='__main__': main()
