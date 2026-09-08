#!/usr/bin/env python3
"""Exact real-root isolation and rational same-datum short-window certificate."""
from fractions import Fraction as F
from math import gcd, isqrt
from functools import reduce
from pathlib import Path
import hashlib, json, platform, resource, sys, time
from exact_screen import pa, pm, ps, rem, enc

def plus(x,y): return (x[0]+y[0],x[1]+y[1])
def times(x,y):
    z=[a*b for a in x for b in y]
    return (min(z),max(z))
def reciprocal(x):
    assert x[0]*x[1]>0
    return (1/x[1],1/x[0])
def interval(p,x):
    z=(F(0),F(0))
    for c in p[::-1]: z=plus(times(z,x),(c,c))
    return z
def pe(p,x): return sum(c*x**i for i,c in enumerate(p))
def boundabs(x): return max(abs(x[0]),abs(x[1]))
def lowerabs(x):
    assert x[0]*x[1]>0
    return min(abs(x[0]),abs(x[1]))
def lcm(a,b): return a*b//gcd(a,b)
def ceil(x): return -((-x.numerator)//x.denominator)

def main():
    start=time.monotonic(); root=Path(__file__).resolve().parent
    src=root/'exact-output.json'; raw=json.loads(src.read_text())
    det=list(map(F,raw['det_first_two_components']))
    assert len(det)==3 and det[2]>0
    den=reduce(lcm,[x.denominator for x in det],1)
    ints=[int(x*den) for x in det]; g=reduce(gcd,ints)
    primitive=[x//g for x in ints]
    c,b,a=map(F,primitive); disc=b*b-4*a*c
    assert disc>0 and disc.denominator==1
    assert isqrt(disc.numerator)**2 != disc.numerator  # two irrational simple real roots
    scale=2**40; sqlo=F(isqrt(disc.numerator*scale**2),scale); sqhi=sqlo+F(1,scale)
    assert sqlo**2<disc<sqhi**2
    rminus=((-b-sqhi)/(2*a),(-b-sqlo)/(2*a))
    rplus=((-b+sqlo)/(2*a),(-b+sqhi)/(2*a))
    assert rminus[1]<-b/(2*a)<rplus[0]
    assert pe(primitive,rminus[0])>0>pe(primitive,rminus[1])
    assert pe(primitive,rplus[0])<0<pe(primitive,rplus[1])
    mats={name:[[list(map(F,p)) for p in row] for row in mat]
          for name,mat in raw['matrices_constant_first_polynomials'].items()}
    m=mats['M']; wmat=mats['W']
    # All real roots: row one is nonzero and the prescribed v=1 kernel is valid.
    roots=[]
    for x in (rminus,rplus):
        denominator=interval(m[0][1],x)
        assert denominator[0]*denominator[1]>0
        wi=times(interval(ps(m[0][0],-1),x),reciprocal(denominator))
        residual=[]; numerators=[]
        for row in m:
            z=pa(pm(row[0],m[0][1]),ps(pm(row[1],m[0][0]),-1))
            residual.append(rem(z,det))
        assert residual==[[0],[0],[0]]
        out=[]
        for row in wmat:
            z=pa(pm(row[0],m[0][1]),ps(pm(row[1],m[0][0]),-1))
            numerators.append(rem(z,det))
            out.append(plus(interval(row[0],x),times(interval(row[1],x),wi)))
        nonzero=[j for j,z in enumerate(out) if z[0]*z[1]>0]
        assert nonzero
        roots.append({'alpha_interval':x,'normalized_v':F(1),'w_interval':wi,
                      'M_residuals_mod_det':residual,'W_numerators_mod_det':numerators,
                      'W_real_component_intervals':out,'certified_nonzero_components':nonzero})
    chosen=roots[0]  # predeclared increasing-root rule, no posterior adjustment
    x=chosen['alpha_interval']; wi=chosen['w_interval']
    Abar=ceil(16+2*boundabs(x)+14*boundabs(wi))
    Kbar=7; assert Kbar*Kbar>38
    # A >= 0 is the full signed Fourier Wiener norm. Its bound uses vector l1 >= l2.
    bbar=4*Abar*Kbar
    wlower=lowerabs(chosen['W_real_component_intervals'][chosen['certified_nonzero_components'][0]])
    Etail=3*Abar*bbar**4
    Eheat=80*Abar**4*Kbar**5
    E=Etail+Eheat
    first_birth_error=4*Kbar**2+2*Abar*bbar**2
    tsb=F(1,8*Abar*Kbar)
    tsource=wlower/(8*E)
    tbirth=F(1,2*first_birth_error)
    tstar=min(tsb,tsource,tbirth)
    assert tstar>0 and 4*Abar*Kbar*tstar<=F(1,2)
    assert E*tstar<=wlower/8
    assert first_birth_error*tstar<=F(1,2)
    certificate={'status':'EXACT_ALGEBRA_AND_RATIONAL_BOUNDS_PENDING_INDEPENDENT_MATHEMATICAL_REVIEW',
      'input_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
      'primitive_det_constant_first':primitive,'discriminant':disc,'roots_in_increasing_order':roots,
      'selected_root_index':0,'fixed_datum_definition':'alpha=smaller root; v=1; w=-M00(alpha)/M01(alpha)',
      'A_upper':Abar,'K_upper':Kbar,'W0_A0_lower':wlower,
      'error_other_and_source_upper_coefficient':E,
      'first_birth_error_upper_coefficient':first_birth_error,
      'T_full_NS':tsb,'T_source':tsource,'T_first_birth':tbirth,'T_star':tstar,
      'certified_inequalities':{'source_lower_fraction_of_wlower_t3':'7/8',
          'other_upper_fraction_of_wlower_t3':'1/8','relative_other_source_upper':'1/7 < 1/4',
          'first_birth_at_p1_plus_p2_lower':'t/2', 'range':'all 0 < t <= T_star'},
      'scope':'One fixed smooth real full-NS datum; finite source attribution only; no template regeneration or singularity.',
      'resource':{'command':'python3 research/reverse/four-carrier-source-test/certify_root.py',
          'python':sys.version,'platform':platform.platform(),'processes':1,'threads':1,
          'precision':'exact Fraction and integer isqrt','tolerance':None,'random_seed':None,
          'wall_seconds':time.monotonic()-start,'max_rss_bytes_macos':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}}
    print(json.dumps(enc(certificate),ensure_ascii=False,indent=2))

if __name__=='__main__': main()
