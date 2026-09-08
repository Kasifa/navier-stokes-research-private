#!/usr/bin/env python3
"""One fixed chart; exact full signed Fourier convolution, no NS truncation claim."""
from fractions import Fraction as F
from itertools import combinations_with_replacement
import json, os, platform, resource, sys, time

P = [(1,0,0),(0,1,0),(0,0,1),(2,3,5)]
TARGET = (3,4,6)
ZERO = (F(0),)*3

def add(x,y): return tuple(a+b for a,b in zip(x,y))
def neg(x): return tuple(-a for a in x)
def scale(c,x): return tuple(c*a for a in x)
def dot(x,y): return sum(a*b for a,b in zip(x,y))
def project(k,x): return add(x, scale(-F(dot(k,x),dot(k,k)),k))
def merge(a,b):
    out = dict(a)
    for k,x in b.items(): out[k] = add(out.get(k,ZERO),x)
    return {k:x for k,x in out.items() if x != ZERO}
def scaled(c,a): return {k:scale(c,x) for k,x in a.items() if x != ZERO}
def q(a,b,only=None):
    out = {}
    for r,x in a.items():
        for s,y in b.items():
            k=add(r,s)
            if k == (0,0,0) or (only is not None and k not in only): continue
            z=scale(dot(x,s),y)
            out[k]=add(out.get(k,ZERO),z)
    return {k:z for k,x in out.items() if (z:=project(k,x)) != ZERO}

def evaluate(alpha,which):
    u=[(0,1,alpha),(0,0,1),(1,0,0),[(3,-2,0),(5,0,-2)][which]]
    a={}
    for p,x in zip(P,u):
        a[p]=tuple(map(F,x)); a[neg(p)]=tuple(map(F,x))
    assert all(dot(k,x)==0 for k,x in a.items())
    h1=q(a,a)
    h2=scaled(F(1,2),merge(q(a,h1),q(h1,a)))
    w=scaled(F(1,3),q(h1,h1,{TARGET,neg(TARGET)}))
    m=scaled(F(1,3),merge(q(a,h2,{TARGET,neg(TARGET)}),q(h2,a,{TARGET,neg(TARGET)})))
    for field in (h1,h2,w,m): assert all(dot(k,x)==0 for k,x in field.items())
    for field,n in ((h1,1),(h2,2),(w,3),(m,3)):
        assert all(field.get(neg(k),ZERO)==scale((-1)**n,x) for k,x in field.items())
    return {'W':w.get(TARGET,ZERO),'M':m.get(TARGET,ZERO),
            'nonzero_support_sizes':[len(a),len(h1),len(h2),len(w),len(m)]}

def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0: p.pop()
    return p
def pa(p,q):
    return trim([(p[i] if i<len(p) else F(0))+(q[i] if i<len(q) else F(0)) for i in range(max(len(p),len(q)))])
def ps(p,c): return trim([c*x for x in p])
def pm(p,q):
    out=[F(0)]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q): out[i+j]+=x*y
    return trim(out)
def rem(p,d):
    p=trim(p)
    while p != [0] and len(p)>=len(d):
        n=len(p)-len(d); c=p[-1]/d[-1]
        p=pa(p,[F(0)]*n+ps(d,-c))
    return p
def enc(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,dict): return {str(k):enc(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)): return [enc(v) for v in x]
    return x

def main():
    start=time.monotonic()
    signed=P+[neg(p) for p in P]
    # Exhaust finite signed multisets, independently of the Fourier coefficient recursion.
    hits={}
    for n in range(1,5):
        hits[n]=[list(idx) for idx in combinations_with_replacement(range(8),n)
                 if tuple(sum(signed[j][d] for j in idx) for d in range(3))==TARGET]
    assert hits == {1:[],2:[],3:[],4:[[0,1,2,3]]}
    L={add(r,s) for r in signed for s in signed}-{(0,0,0)}
    assert not L.intersection(signed)
    results={f'{a},{j}':evaluate(F(a),j) for a in (0,1,-1) for j in (0,1)}
    mat={name:[] for name in ('W','M')}
    for name in mat:
        for component in range(3):
            row=[]
            for j in range(2):
                z=results[f'0,{j}'][name][component]
                slope=results[f'1,{j}'][name][component]-z
                assert results[f'-1,{j}'][name][component]==z-slope
                row.append(trim([z,slope]))
            mat[name].append(row)
    m=mat['M']
    det=pa(pm(m[0][0],m[1][1]),ps(pm(m[0][1],m[1][0]),-1))
    kernel=[ps(m[0][1],-1),m[0][0]]
    if kernel == [[0],[0]]: kernel=[ps(m[1][1],-1),m[1][0]]
    residuals={}
    if det != [0]:
        for name in mat:
            residuals[name]=[rem(pa(pm(row[0],kernel[0]),pm(row[1],kernel[1])),det) for row in mat[name]]
    info={'status':'EXACT_COEFFICIENTS_ONLY_PENDING_ROOT_AND_NS_CERTIFICATION',
          'normalization':'actual W0=i*W_real and M0=i*M_real at positive target',
          'p':P,'target':TARGET,'finite_leaf_hits':hits,'L_cardinality':len(L),
          'samples':results,'matrices_constant_first_polynomials':mat,
          'det_first_two_components':det,'kernel_v_w':kernel,
          'remainders_mod_det':residuals,
          'resource':{'command':'python3 research/reverse/four-carrier-source-test/exact_screen.py',
                      'python':sys.version,'platform':platform.platform(),'cpu_count':os.cpu_count(),
                      'processes':1,'threads':1,'precision':'arbitrary precision exact Fraction',
                      'solver_tolerance':None,'random_seed':None,'wall_seconds':time.monotonic()-start,
                      'max_rss_bytes_macos':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}}
    print(json.dumps(enc(info),ensure_ascii=False,indent=2))

if __name__=='__main__': main()
