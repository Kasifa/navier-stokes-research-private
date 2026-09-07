#!/usr/bin/env python3
"""Compare two actually computed finite residual records; never integrate."""
from fractions import Fraction as F
from pathlib import Path
import copy
import hashlib
import json

HERE=Path(__file__).resolve().parent

def require(ok,label):
    if not ok: raise ValueError(label)

def fraction(obj):
    return F(int(obj['numerator']),int(obj['denominator']))

def digest(path):
    h=hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda:stream.read(1<<20),b''): h.update(block)
    return h.hexdigest()

def compare(p,i):
    require(i['execution_status']=='COMPLETE','independent execution incomplete')
    require(p['node']==i['node']==1280,'wrong fixed node')
    require(len(p['outputs'])==len(i['mode_results'])==24,'wrong output count')
    D=int(p['D']);D2=D*D;D4=D2*D2
    require(int(p['D4'])==D4,'D4 mismatch')
    contributions=F(0);pair_count=0
    for a,b in zip(p['outputs'],i['mode_results']):
        require(a['k']==b['k'],'mode sequence mismatch')
        s=sum(k*k for k in a['k'])
        require(s==a['squared_frequency']==b['k_squared'],'frequency weight mismatch')
        require(a['ordered_pair_count']==b['ordered_pairs']==2*b['unordered_distinct_pairs']+b['diagonal_pairs'],'pair count mismatch')
        require(a['ordered_pair_sequence_sha256']==b['ordered_pair_stream_sha256'],'ordered pair coverage mismatch')
        pair_count+=a['ordered_pair_count']
        component_square=F(0)
        for j in range(3):
            re=F(int(a['F_real'][j]),D2);im=F(int(a['F_imag'][j]),D2)
            require(re==fraction(b['F_unprojected'][j]['real']) and im==fraction(b['F_unprojected'][j]['imag']),'unprojected F mismatch')
            rr=F(int(a['T_real'][j]),D2*s);ri=F(int(a['T_imag'][j]),D2*s)
            require(rr==fraction(b['R'][j]['real']) and ri==fraction(b['R'][j]['imag']),'residual component mismatch')
            # Independent saved projection and linear pieces must sum to R.
            require(rr==fraction(b['linear_d_plus_k2c'][j]['real'])-fraction(b['F_projected'][j]['imag']),'real assembly mismatch')
            require(ri==fraction(b['linear_d_plus_k2c'][j]['imag'])+fraction(b['F_projected'][j]['real']),'imaginary assembly mismatch')
            component_square+=rr*rr+ri*ri
        weighted=s*s*component_square
        require(weighted==F(int(a['squared_H2_contribution_numerator_over_D4']),D4)==fraction(b['weighted_R_squared']),'mode contribution mismatch')
        contributions+=weighted
    require(len({tuple(a['k']) for a in p['outputs']})==24,'duplicate mode')
    require(contributions==F(int(p['N']),D4)==fraction(p['r2_squared_lower'])==fraction(i['result']['Lambda']),'Lambda mismatch')
    term=P=F(1)
    for j in range(1,33):term*=F(5,2*j);P+=term
    require(P==fraction(p['P32'])==fraction(i['result']['P32_of_5_over_2']),'P32 mismatch')
    necessity=contributions*P
    require(necessity==fraction(p['necessary_epsilon_squared_lower'])==fraction(i['result']['necessary_epsilon_squared_lower']),'epsilon necessity mismatch')
    require(int(p['integer_left'])==10**14*int(p['N'])*P.numerator and int(p['integer_right'])==D4*P.denominator,'primary cross-products mismatch')
    require(int(p['integer_margin'])==int(p['integer_left'])-int(p['integer_right']),'primary margin mismatch')
    b=i['result']['old_threshold_comparison']
    require(int(b['lhs'])==necessity.numerator*10**14 and int(b['rhs'])==necessity.denominator,'independent cross-products mismatch')
    require(int(b['difference'])==int(b['lhs'])-int(b['rhs']),'independent margin mismatch')
    require(necessity>F(1,10**14),'old threshold not refuted')
    require(p['status']==i['mathematical_status']=='OLD_REFERENCE_R2_ENVELOPE_REFUTED','verdict mismatch')
    return {'modes':24,'complex_F_components':72,'complex_R_components':72,'ordered_pairs':pair_count,
            'Lambda':p['r2_squared_lower'],'necessary_epsilon_squared_lower':p['necessary_epsilon_squared_lower']}

def main():
    ppath=HERE/'nodal-residual-trial-01/exact-result.json'
    ipath=HERE/'nodal-residual-independent-trial-01/run.json'
    primary=json.loads(ppath.read_text());independent=json.loads(ipath.read_text())
    run=json.loads((HERE/'nodal-residual-trial-01/run.json').read_text())
    require(run['status']=='COMPLETE_FIXED_NODE_LOWER_TRIAL','primary execution incomplete')
    bindings={}
    for name,entry in run['files'].items():
        path=HERE/'nodal-residual-trial-01'/name
        require(digest(path)==entry['sha256'],'primary file hash '+name)
        bindings[str(path.relative_to(HERE))]=entry['sha256']
    for name,sha in run['sources'].items():
        require(digest(HERE/name)==sha,'primary source/input '+name)
        bindings[name]=sha
    for name,sha in independent['authenticated_file_sha256'].items():
        require(digest(HERE/name)==sha,'independent input '+name)
        bindings[name]=sha
    for name,sha in independent['inputs']['source_sha256'].items():
        path=Path(name)
        require(digest(path)==sha,'independent source '+name)
        bindings[str(path.relative_to(HERE.resolve()))]=sha
    selection=json.loads((HERE/'nodal-residual-trial-01/selection.json').read_text())
    require(primary['selection_sha256']==digest(HERE/'nodal-residual-trial-01/selection.json'),'selection hash mismatch')
    require(primary['selected_modes']==selection['selected_modes']==[x['k'] for x in primary['outputs']],'frozen selection mismatch')
    result=compare(primary,independent)
    controls=[]
    for label in ('F','R','weight','coverage','N','P32'):
        changed=copy.deepcopy(primary)
        if label=='F':changed['outputs'][0]['F_real'][0]=str(int(changed['outputs'][0]['F_real'][0])+1)
        elif label=='R':changed['outputs'][0]['T_real'][0]=str(int(changed['outputs'][0]['T_real'][0])+1)
        elif label=='weight':changed['outputs'][0]['squared_frequency']+=1
        elif label=='coverage':changed['outputs'][0]['ordered_pair_count']+=1
        elif label=='N':changed['N']=str(int(changed['N'])+1)
        else:changed['P32']['numerator']=str(int(changed['P32']['numerator'])+1)
        try:compare(changed,independent)
        except ValueError as exc:controls.append({'in_memory_mutation':label,'rejected_by':str(exc)})
        else:raise ValueError('mutation unexpectedly accepted: '+label)
    for path in (Path(__file__).resolve(),ppath,ipath,HERE/'nodal-residual-trial-01/run.json'):
        bindings[str(path.relative_to(HERE))]=digest(path)
    output=HERE/'nodal-residual-independent-agreement.json'
    with output.open('x') as stream:
        json.dump({'status':'PASS_ACTUAL_INDEPENDENT_EXACT_RECOMPUTATION','comparison':result,
                   'negative_controls':controls,'input_sha256':bindings,
                   'scope':'Same fixed reference and 24 outputs; no continuous upper bound or true NS conclusion'},stream,indent=2)
        stream.write('\n')
    print(json.dumps({'status':'PASS','modes':24,'ordered_pairs':result['ordered_pairs'],
                      'negative_controls_rejected':len(controls),'output':str(output),'sha256':digest(output)}))

if __name__=='__main__':main()
