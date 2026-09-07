#!/usr/bin/env python3
"""Exact finite node gates; no integration or continuum upper-bound claim.

NumPy is used only for authenticated integer archive decoding. Mathematical
arithmetic uses Python arbitrary-size ints, Fraction and isqrt. A stopped trial
is allowed: missing prescribed nodes are reported, never interpolated or rerun.
"""
from __future__ import annotations
import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path
import resource
import sys
import time
from fractions import Fraction as F

HERE = Path(__file__).resolve().parent
RUN = HERE / 'node-trial-01'
Q = 1 << 52
TARGETS = tuple(range(0, 5121, 640))

def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()

def canonical(x):
    return json.dumps(x, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()

def rat(x):
    x = F(x)
    return {'numerator': str(x.numerator), 'denominator': str(x.denominator)}

def decode(raw, modes, opposite, L):
    # Convert every scalar before addition, negation, multiplication or dot.
    z = raw.tolist()
    out = []
    for i, k in enumerate(modes):
        m = sum(x*x for x in k)
        S = [int(z[i][j][0]) + int(z[opposite[i]][j][0]) for j in range(3)]
        T = [int(z[i][j][1]) - int(z[opposite[i]][j][1]) for j in range(3)]
        ks, kt = sum(k[j]*S[j] for j in range(3)), sum(k[j]*T[j] for j in range(3))
        U = tuple((L//m)*(m*S[j]-k[j]*ks) for j in range(3))
        V = tuple((L//m)*(m*T[j]-k[j]*kt) for j in range(3))
        assert sum(k[j]*U[j] for j in range(3)) == 0
        assert sum(k[j]*V[j] for j in range(3)) == 0
        out.append((U, V))
    for i in range(len(modes)):
        assert out[opposite[i]][0] == out[i][0]
        assert out[opposite[i]][1] == tuple(-x for x in out[i][1])
    return out

def exact_values(coeff, modes, D, node):
    lower, upper, nonroots = 0, 0, 0
    for k, (U,V) in zip(modes, coeff, strict=True):
        m = sum(x*x for x in k)
        N = sum(x*x for x in U+V)
        a = math.isqrt(N//m)
        assert m*a*a <= N < m*(a+1)*(a+1)
        extra = int(N != m*a*a)
        lower += a
        upper += a+extra
        nonroots += extra
    s = F(node,1024)
    term, p32 = F(1), F(1)
    for n in range(1,33):
        term *= s/n
        p32 += term
    derivatives = {}
    for j in (1,2,3):
        total, weight_sum, tensor = 0, 0, []
        for alpha in itertools.product(range(j+1), repeat=3):
            if sum(alpha) != j:
                continue
            weight = math.factorial(j)//math.prod(math.factorial(a) for a in alpha)
            weight_sum += weight
            re, im = [0]*3, [0]*3
            for k, (U,V) in zip(modes, coeff, strict=True):
                mul = math.prod(k[d]**alpha[d] for d in range(3))
                r = (j+sum(k)) % 4
                A,B = ((U,V), (tuple(-x for x in V),U),
                       (tuple(-x for x in U),tuple(-x for x in V)),
                       (V,tuple(-x for x in U)))[r]
                for d in range(3):
                    re[d] += mul*A[d]
                    im[d] += mul*B[d]
            assert im == [0,0,0], ('nonreal exact derivative',node,alpha)
            total += weight*sum(x*x for x in re)
            tensor.append({'alpha':list(alpha),'multiplicity':weight,
                           'real_numerator':[str(x) for x in re], 'denominator':str(D)})
        assert weight_sum == 3**j
        q = F(total,D*D)
        margin = q*p32-16
        derivatives[str(j)] = {'squared_frobenius':rat(q), 'ordered_weight_sum':weight_sum,
            'tensor_components':tensor, 'q_times_P32_minus_16':rat(margin),
            'cost_envelope_refuted_at_this_point':margin > 0}
    if node == 0:
        assert lower == upper == 6*D
        for k,(U,V) in zip(modes,coeff,strict=True):
            expected=[0]*3
            if sum(x*x for x in k)==1:
                axis=next(j for j in range(3) if k[j])
                expected[(axis+1)%3]=D
            assert U==tuple(expected) and V==(0,0,0)
        assert [F(int(derivatives[str(j)]['squared_frobenius']['numerator']),
                  int(derivatives[str(j)]['squared_frobenius']['denominator']))
                for j in (1,2,3)] == [12,0,12]
    return {'node':node,'time':rat(F(node,2048)), 'P32_of_twice_time':rat(p32),
            'A_minus_1':{'lower':rat(F(lower,D)),'upper':rat(F(upper,D)),
                         'width':rat(F(nonroots,D)), 'upper_le_half':2*upper<=D},
            'derivatives_at_pi_over_2':derivatives, 'exact_reality_divergence':'PASS',
            'scope':'FIXED_REFERENCE_NODE_ONLY_NOT_ACTUAL_NS'}

def main():
    if sys.version_info < (3,10) or sys.flags.optimize:
        raise RuntimeError('Use Python >=3.10 without -O: exact assertions are mandatory.')
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, help='new output basename in this directory')
    args=parser.parse_args()
    if Path(args.output).name != args.output:
        raise ValueError('output must be a basename')
    output=HERE/args.output
    if output.exists():
        raise FileExistsError(output)
    started=time.perf_counter()
    import numpy as np
    bound = {}
    def bind(path):
        bound[str(path.relative_to(HERE))] = sha(path)
    manifest_path=RUN/'manifest.json'
    bind(manifest_path)
    manifest=json.loads(manifest_path.read_text())
    assert manifest['schema']=='reverse-fixed-seed-nodes-v1'
    config=manifest['config']
    assert config['cutoff']==8 and config['time_denominator']==2048 and config['quantization_denominator']==Q
    assert config['scale']==config['rho']==config['viscosity']==1
    assert hashlib.sha256(canonical(config)).hexdigest()==manifest['config_sha256']
    modepath=RUN/manifest['modes']['file']
    assert modepath.name=='modes.npy'
    assert sha(modepath)==manifest['modes']['file_sha256']
    modes_array=np.load(modepath,allow_pickle=False)
    assert modes_array.dtype.str=='<i8' and modes_array.shape==(4912,3)
    assert hashlib.sha256(modes_array.tobytes(order='C')).hexdigest()==manifest['modes']['array_sha256']
    modes=[tuple(map(int,k)) for k in modes_array.tolist()]
    assert modes==[k for k in itertools.product(range(-8,9),repeat=3) if k!=(0,0,0)]
    bind(modepath)
    index={k:i for i,k in enumerate(modes)}
    opposite=[index[tuple(-x for x in k)] for k in modes]
    L=math.lcm(*(sum(x*x for x in k) for k in modes))
    D=2*Q*L
    selected, next_node, all_files = [], 0, 0
    for entry in manifest['blocks']:
        assert entry['first_node']==next_node
        assert entry['last_node']==next_node+entry['node_count']-1
        assert 1<=entry['node_count']<=64
        path=RUN/entry['file']
        assert path.parent==RUN and path.name==f"block-{next_node:05d}-{entry['last_node']:05d}.npz"
        assert path.stat().st_size==entry['file_bytes'] and sha(path)==entry['file_sha256']
        assert hashlib.sha256(canonical(entry['arrays'])).hexdigest()==entry['data_sha256']
        bind(path)
        all_files+=1
        wanted=[n for n in TARGETS if next_node<=n<=entry['last_node']]
        if wanted:
            with np.load(path,allow_pickle=False) as data:
                assert set(data.files)==set(entry['arrays'])
                decoded={}
                for name, desc in entry['arrays'].items():
                    array=data[name]
                    assert list(array.shape)==desc['shape'] and array.dtype.str==desc['dtype']=='<i8'
                    assert array.nbytes==desc['nbytes']
                    assert hashlib.sha256(array.tobytes(order='C')).hexdigest()==desc['data_sha256']
                    decoded[name]=array
                assert decoded['node_index'].tolist()==list(range(next_node,entry['last_node']+1))
                assert np.array_equal(decoded['time_numerator'],decoded['node_index'])
                assert decoded['time_denominator'].tolist()==[2048]
                assert decoded['quantization_denominator'].tolist()==[Q]
                for name in ('value_q52','slope_q52'):
                    assert decoded[name].shape==(entry['node_count'],4912,3,2)
                for n in wanted:
                    coeff=decode(decoded['value_q52'][n-next_node],modes,opposite,L)
                    # Slopes also define shared exact transverse, real data.
                    decode(decoded['slope_q52'][n-next_node],modes,opposite,L)
                    selected.append(exact_values(coeff,modes,D,n))
                    print(json.dumps({'exact_node_done':n}),flush=True)
                del decoded
        next_node+=entry['node_count']
    assert next_node==manifest['stored_nodes']
    for path in (Path(__file__), HERE/'NODE_GATE_LEMMA.md', HERE/'NODE_PRODUCTION_CONTRACT.md'):
        bind(path)
    assert sha(manifest_path)==bound['node-trial-01/manifest.json']
    missing=[n for n in TARGETS if n not in [x['node'] for x in selected]]
    result={'kind':'EXACT_FINITE_REFERENCE_NODE_GATES_NOT_CONTINUOUS_NS_CERTIFICATE',
        'production_status':manifest['status'],'common_L':str(L),'common_D':str(D),
        'file_hashes_checked':all_files,'selected_block_arrays_checked':True,
        'unselected_block_arrays_recomputed':False,'stored_node_coverage':next_node,
        'prescribed_nodes':list(TARGETS),'missing_prescribed_nodes':missing,'nodes':selected,
        'input_sha256':bound,'wall_seconds':time.perf_counter()-started,
        'peak_rss_native':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        'python':sys.version,'numpy':np.__version__,
        'scope':'Any refuted cost envelope is only for this reference; non-refutation is not an upper bound. Endpoint gate alone does not control actual NS.'}
    with output.open('x') as stream:
        json.dump(result,stream,indent=2,sort_keys=True,allow_nan=False)
        stream.write('\n')
    print(json.dumps({'output':str(output),'sha256':sha(output),'nodes_checked':len(selected),
                      'missing':missing,'wall_seconds':result['wall_seconds']}),flush=True)

if __name__=='__main__':
    main()
