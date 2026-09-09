"""One bounded byte-only archive child. No science, array decoding or retry."""
import sys
sys.dont_write_bytecode = True
import hashlib, json, os, resource, subprocess, time, traceback
from pathlib import Path, PurePosixPath
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTROL = HERE/'archive-supervision-v1'
ARCHIVE = HERE/'value-data-archive-v1'
LOCK = HERE/'archive-source-lock.json'
PYTHON = '/Users/kasifa/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3'
PREFIX = HERE.relative_to(ROOT).as_posix()+'/'
NEEDED = {PREFIX+n for n in ('archive_value_data.py','run_archive_value.py','ARCHIVE_CONTRACT.md',
    'ARCHIVE_SOURCE_REVIEW.md','ARCHIVE_SUPERVISOR_REVIEW.md','ROOT_RUN_OBSERVATION.json','source-lock.json',
    'numerical-runs/value-scout-160-512/execution.json','numerical-runs/value-scout-160-512/result.json')}
def need(ok, why):
    if not ok: raise ValueError(why)
def encoded(obj):
    return (json.dumps(obj,ensure_ascii=True,sort_keys=True,indent=2,allow_nan=False)+'\n').encode()
def record(path):
    need(path.is_file() and path.resolve(strict=True)==path,'regular nonsymlink source')
    b=path.read_bytes()
    return {'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}
def snapshot():
    lock_record=record(LOCK); data=json.loads(LOCK.read_text())
    need(type(data['schema']) is int and data['schema']==1,'lock schema')
    out={}
    for row in data['bindings']:
        need(set(row)=={'path','sha256','bytes'},'binding schema')
        n=row['path']; q=PurePosixPath(n)
        need(not q.is_absolute() and '..' not in q.parts and q.as_posix()==n and n not in out
             and q.suffix in ('.py','.md','.json','.jsonl','.txt'),'unique normalized text source')
        path=ROOT/n
        need(path!=LOCK and not path.is_relative_to(ARCHIVE) and not path.is_relative_to(CONTROL),'no output/self binding')
        out[n]=record(path)
        need(out[n]=={k:row[k] for k in ('sha256','bytes')},'changed source '+n)
    need(NEEDED<=out.keys(),'missing required sources')
    return {'lock':lock_record,'sources':out}
def inventory():
    rows=[]
    for directory in (CONTROL,ARCHIVE):
        if not directory.exists(): continue
        for f in sorted(directory.rglob('*')):
            need(not f.is_symlink(),'symlink output')
            if f.is_file() and f != CONTROL/'execution.json.tmp':
                rows.append({'path':f.relative_to(HERE).as_posix(),'bytes':f.stat().st_size})
    return rows
def main():
    need(sys.platform=='darwin','Darwin RSS units')
    need(not CONTROL.exists() and not ARCHIVE.exists(),'existing archive/control: no retry')
    CONTROL.mkdir()
    started=time.monotonic()
    r={'status':'FAIL','scope':'LOSSLESS_BYTES_AND_RESOURCE_ONLY','scientific_worker_invocations':0,
       'byte_child_invocations':0,'supervisor_pid':os.getpid(),'timed_out':False,'child_reaped':False}
    try:
        before=resource.getrusage(resource.RUSAGE_CHILDREN)
        need(not(before.ru_utime or before.ru_stime or before.ru_maxrss),'fresh byte supervisor')
        r['sources_start']=snapshot()
        command=[PYTHON,'-B',str(HERE/'archive_value_data.py')]
        r['command']=command
        with (CONTROL/'stdout.log').open('xb') as out,(CONTROL/'stderr.log').open('xb') as err:
            begin=time.monotonic(); child=None
            try:
                child=subprocess.Popen(command,cwd=ROOT,stdout=out,stderr=err)
                r.update(byte_child_invocations=1,child_pid=child.pid)
                child.wait(timeout=max(0,180-(time.monotonic()-begin)))
            except subprocess.TimeoutExpired:
                r['timed_out']=True
                if child is not None: child.kill(); child.wait()
            except BaseException:
                if child is not None and child.poll() is None: child.kill(); child.wait()
                raise
            finally:
                r['child_wall_seconds']=time.monotonic()-begin
                if child is not None: r.update(child_exit_code=child.returncode,child_reaped=child.returncode is not None)
        need(r['child_exit_code']==0 and r['child_reaped'] and not r['timed_out'],'child failed')
        lines=(CONTROL/'stdout.log').read_text().splitlines()
        need(len(lines)==1,'one terminal summary')
        summary=json.loads(lines[0]); manifest=json.loads((ARCHIVE/'manifest.json').read_text())
        r.update(child_terminal=summary,manifest_record=record(ARCHIVE/'manifest.json'))
        need(summary['manifest']==r['manifest_record'],'terminal manifest identity')
        for item in (summary,manifest):
            need(item['status']=='PASS' and item['pid']==r['child_pid']
                 and item['supervisor_pid']==os.getpid() and item['scientific_worker_invocations']==0,'child identity/status')
        need(len(manifest['files'])==4 and all(x['status']=='VERIFIED' for x in manifest['files']),'four restored files')
        r['status']='PASS'
    except BaseException:
        r['error']=traceback.format_exc(); r['status']='FAIL'
    finally:
        child_usage=resource.getrusage(resource.RUSAGE_CHILDREN)
        r['child_peak_rss_bytes']=child_usage.ru_maxrss
        r['child_cpu_seconds']={'user':child_usage.ru_utime,'system':child_usage.ru_stime}
        try:
            r['sources_end']=snapshot()
            need(r['sources_start']==r['sources_end'],'source start/end differ')
        except BaseException:
            r['source_error']=traceback.format_exc(); r['status']='FAIL'
        if r.get('child_wall_seconds',181)>180 or child_usage.ru_maxrss>256*1024**2: r['status']='FAIL'
        r['output_inventory_before_receipt']=inventory()
        r['parent_seconds_to_receipt']=time.monotonic()-started
        own=resource.getrusage(resource.RUSAGE_SELF)
        r['parent_self_pre_receipt_rss_bytes']=own.ru_maxrss
        r['resource_scope']='Popen-before to reap child; CHILDREN full peak, not RSS hard limit. Parent SELF separate pre-receipt sample, not concurrent sum.'
        raw=encoded(r)
        total=sum(x['bytes'] for x in r['output_inventory_before_receipt'])+len(raw)
        if total>1024**3: r['status']='FAIL'; raw=encoded(r)
        with (CONTROL/'execution.json.tmp').open('xb') as f: f.write(raw); f.flush(); os.fsync(f.fileno())
        os.link(CONTROL/'execution.json.tmp',CONTROL/'execution.json'); (CONTROL/'execution.json.tmp').unlink()
    actual=inventory()
    need([x for x in actual if x['path']!='archive-supervision-v1/execution.json']==r['output_inventory_before_receipt'],'output size inventory changed')
    total=sum(x['bytes'] for x in actual)
    need(total<=1024**3,'complete output over budget')
    need(record(CONTROL/'execution.json')=={'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()},'receipt readback')
    print(json.dumps({'status':r['status'],'scope':r['scope'],'byte_child_invocations':r['byte_child_invocations'],
        'scientific_worker_invocations':0,'execution':record(CONTROL/'execution.json'),
        'complete_output_bytes':total},sort_keys=True))
    return 0 if r['status']=='PASS' else 1
if __name__=='__main__':
    raise SystemExit(main())
