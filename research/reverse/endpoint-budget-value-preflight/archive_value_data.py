"""Fixed lossless byte archive. No arrays, science, subprocess, Git or retry.

Internal 180s checks are cooperative. Root must additionally supervise the whole
Popen-to-reap lifecycle at 180s; exit 0 AND the final summary AND manifest matter.
"""
import time
START = time.monotonic()
import sys
sys.dont_write_bytecode = True
import gzip
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import resource
import shutil
import traceback
import zlib

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RUN = HERE / 'numerical-runs/value-scout-160-512'
OUT = HERE / 'value-data-archive-v1'
MIB, BLOCK, CHUNK = 1024**2, 1024**2, 32*1024**2
NAMES = {'reconstruction.npz', 'terminal-compact.npz', 'full-B216.npz', 'quadrature.npz'}
FIXED = {
    HERE/'ROOT_RUN_OBSERVATION.json': '8496f6a0e32e09f23556edc82af0d45cc686a2b607f483940bbc822f0fc2cb13',
    RUN/'execution.json': '670d621d6bc0f4c90f84c22d4cbb86e388c9339f6b0a2b084ae6cad419050007',
    RUN/'result.json': 'a2092ea5fbf9eff92afc43616bf60938a94a6a8a6ab804b5aa5b4b9ff48c7252',
    HERE/'source-lock.json': '99908cbb6de3512db00feb819220ae958277fadc190a52549fb0ba73914bae7e'}


def need(ok, message):
    if not ok:
        raise ValueError(message)


def tick():
    need(time.monotonic()-START <= 180, '180s internal deadline; retain failure, never retry')


def record(path):
    need(path.is_absolute() and path.resolve(strict=True) == path and path.is_file(), 'regular nonsymlink file required')
    sha, size = hashlib.sha256(), 0
    with path.open('rb') as stream:
        while True:
            tick()
            block = stream.read(BLOCK)
            if not block:
                break
            sha.update(block)
            size += len(block)
    return {'bytes': size, 'sha256': sha.hexdigest()}


def encoded(value):
    return (json.dumps(value, ensure_ascii=True, sort_keys=True, indent=2, allow_nan=False)+'\n').encode('ascii')


def listed(rows):
    out = {r['path']: {'bytes': r['bytes'], 'sha256': r['sha256']} for r in rows}
    need(len(out) == len(rows), 'duplicate metadata path')
    return out


def prerequisites():
    evidence = {str(p.relative_to(ROOT)): record(p) for p in FIXED}
    need(all(evidence[str(p.relative_to(ROOT))]['sha256'] == s for p, s in FIXED.items()), 'fixed evidence changed')
    obs, receipt, result, lock = [json.loads(p.read_text()) for p in FIXED]
    terminal = obs['successful_terminal_summary']
    need(obs['supervisor_tool_exit_code'] == 0 and terminal['status'] == receipt['status'] == 'PASS'
         and obs['root_checks']['parent_exit0_receiptPASS_terminalPASS'] is True, 'three original success conditions')
    er, rr = record(RUN/'execution.json'), record(RUN/'result.json')
    need(er == obs['execution_record'] == terminal['execution'] and rr == obs['result_record'], 'observed exact records')
    need(receipt['returncode'] == 0 and receipt['child_reaped'] and not receipt['timed_out']
         and receipt['scientific_execution_count'] == result['scientific_worker_invocations'] == 1
         and receipt['worker_output_status'] == result['status'] == 'COMPLETED_NUMERICAL_VALUE_ONLY'
         and result['completion_verified'] is True, 'original worker completion')
    need(receipt['pid'] == result['pid'] and receipt['supervisor_runtime']['pid'] == result['supervisor_pid']
         and terminal['run_id'] == receipt['run_id'] == result['run_id'] == RUN.name, 'original identity')
    need(all(receipt[k] is True for k in ('sources_unchanged', 'worker_identity_and_source_maps_match',
         'worker_completion_counts_match', 'non_output_gates_pass')) and all(receipt['budget_pass'].values()), 'original gates')
    counts = {'processed_checkpoints': 17, 'rhs160_calls': 17, 'rhs216_calls': 1,
              'fft_batched_api_calls': 54, 'fft_scalar_3d_transforms': 162}
    need(receipt['worker_completion_counts'] == counts and all(type(result[k]) is int and result[k] == v for k, v in counts.items()), 'actual recorded counts')
    need(receipt['budget'] == {'seconds':120, 'rss_bytes':6*1024**3, 'output_bytes':1024**3, 'json_bytes':16*MIB}
         and 0 <= receipt['child_wall_seconds'] <= 120 and 0 <= receipt['children_after_reap']['peak_rss_bytes'] <= 6*1024**3
         and receipt['output_total_bytes_including_execution_receipt'] <= 1024**3
         and receipt['json_bytes_including_execution_receipt'] <= 16*MIB, 'recorded resource limits')
    rows = lock['bindings']; expected = listed(rows)
    need(lock['schema'] == 1 and len(rows) == 48, 'fixed source coverage')
    maps = {n:r['sha256'] for n,r in expected.items()}
    need(receipt['source_lock_sha256'] == result['source_lock_sha256'] == FIXED[HERE/'source-lock.json']
         and result['source_hashes_start'] == result['source_hashes_end'] == maps, 'source maps/lock')
    for stage in ('sources_before', 'sources_after'):
        need(listed(receipt[stage]) == expected and all(r['match'] is True and r['bytes'] == r['expected_bytes']
             and r['sha256'] == r['expected_sha256'] for r in receipt[stage]), 'parent source evidence')
    for name, identity in expected.items():
        p = PurePosixPath(name)
        need(not p.is_absolute() and '..' not in p.parts and p.as_posix() == name
             and p.suffix in ('.py','.md','.json','.jsonl','.txt'), 'source path must be text metadata')
        need(record(ROOT/name) == identity, 'source no longer equals run evidence')
    inv, arts = listed(receipt['artifact_inventory_before_receipt']), listed(result['artifacts'])
    need(inv['result.json'] == rr and {n for n in inv if n.endswith('.npz')} == NAMES
         and {n for n in arts if n.endswith('.npz')} == NAMES, 'exact four NPZ set')
    need(all(inv[n] == arts[n] and inv[n]['bytes'] > 0 for n in NAMES), 'two artifact inventories differ')
    full = sorted([{'path':n, **r} for n,r in inv.items()]+[{'path':'execution.json', **er}], key=lambda r:r['path'])
    need(hashlib.sha256(encoded(full)).hexdigest() == terminal['complete_directory_manifest_sha256']
         and sum(r['bytes'] for r in full) == terminal['complete_directory_logical_bytes'], 'terminal manifest binding')
    return evidence, expected, {n:inv[n] for n in sorted(NAMES)}


def main():
    need(sys.platform == 'darwin', 'SELF RSS uses Darwin bytes')
    need(not OUT.exists() and not OUT.is_symlink(), 'archive exists: refuse, never retry')
    need(shutil.disk_usage(HERE).free >= 2*1024**3, 'at least 2GiB free required')
    OUT.mkdir()
    manifest = {'schema':1, 'status':'FAIL', 'scope':'LOSSLESS_BYTES_ONLY_NOT_SCIENCE', 'files':[],
        'pid':os.getpid(), 'supervisor_pid':os.getppid(),
        'scientific_worker_invocations':0, 'original_files_preserved':True, 'chunk_bytes':CHUNK,
        'gzip':{'level':6,'mtime':0,'filename':'','strict_size_limit':40*MIB},
        'python':sys.version, 'zlib_runtime':zlib.ZLIB_RUNTIME_VERSION, 'automatic_retry':False}
    progress = (OUT/'progress.jsonl').open('xb')
    def event(kind, **fields):
        progress.write(encoded({'event':kind, 'seconds':time.monotonic()-START, **fields}).replace(b'\n', b' ')+b'\n')
        progress.flush()
    try:
        own = {str(p.relative_to(ROOT)):record(p) for p in (Path(__file__).resolve(), HERE/'ARCHIVE_CONTRACT.md')}
        manifest['archive_sources_start'] = own
        evidence, sources, selected = prerequisites()
        manifest.update(prerequisites=evidence, selected=selected, source_records=sources)
        for name, identity in selected.items():
            src = RUN/name; item = {'original':str(src.relative_to(ROOT)), 'expected':identity, 'status':'PENDING', 'chunks':[]}
            manifest['files'].append(item)
            item['before'] = record(src); need(item['before'] == identity, 'original before hash')
            streamed, restored, offset = hashlib.sha256(), hashlib.sha256(), 0
            with src.open('rb') as handle:
                while offset < identity['bytes']:
                    length = min(CHUNK, identity['bytes']-offset); index = len(item['chunks'])
                    filename = name+f'.part{index:04d}.gz'; target = OUT/filename; temporary = OUT/(filename+'.tmp')
                    part = {'index':index, 'offset':offset, 'raw_bytes':length, 'gzip':filename, 'status':'COMPRESSING'}
                    item['chunks'].append(part); event('chunk_start', original=name, **part)
                    rawhash, left = hashlib.sha256(), length
                    with temporary.open('xb') as dst:
                        with gzip.GzipFile(filename='', mode='wb', compresslevel=6, mtime=0, fileobj=dst) as gz:
                            while left:
                                tick(); block = handle.read(min(BLOCK,left)); need(bool(block), 'early original EOF')
                                gz.write(block); rawhash.update(block); streamed.update(block); left -= len(block)
                        dst.flush(); os.fsync(dst.fileno())
                    part['raw_sha256'] = rawhash.hexdigest(); part['compressed'] = record(temporary)
                    need(part['compressed']['bytes'] < 40*MIB, 'gzip size gate; no recompression')
                    os.link(temporary,target); temporary.unlink(); part['status'] = 'COMPRESSED'
                    digest, count = hashlib.sha256(), 0
                    with gzip.open(target,'rb') as gz:
                        while True:
                            tick(); block = gz.read(BLOCK)
                            if not block: break
                            count += len(block); need(count <= length, 'restored chunk too long')
                            digest.update(block); restored.update(block)
                    part['restored'] = {'bytes':count, 'sha256':digest.hexdigest()}
                    need(part['restored'] == {'bytes':length,'sha256':part['raw_sha256']}
                         and record(target) == part['compressed'], 'chunk restoration or gzip identity')
                    offset += count; part['status'] = 'VERIFIED'; event('chunk_verified', original=name, **part)
                need(handle.read(1) == b'', 'original grew during compression')
            item['stream'] = {'bytes':offset,'sha256':streamed.hexdigest()}
            item['restored'] = {'bytes':offset,'sha256':restored.hexdigest()}; item['after'] = record(src)
            need(item['stream'] == item['restored'] == item['after'] == identity, 'whole file restoration/original changed')
            need(len(item['chunks']) == (identity['bytes']+CHUNK-1)//CHUNK, 'chunk coverage')
            item['status'] = 'VERIFIED'; event('file_verified', original=name)
        evidence_end, sources_end, selected_end = prerequisites()
        need((evidence_end,sources_end,selected_end) == (evidence,sources,selected), 'end evidence differs')
        manifest['archive_sources_end'] = {n:record(ROOT/n) for n in own}
        need(manifest['archive_sources_end'] == own, 'archive source changed')
        need(len(manifest['files']) == 4 and all(f['status'] == 'VERIFIED' for f in manifest['files']), 'incomplete archive')
        manifest['status'] = 'PASS'
    except BaseException:
        manifest['error'] = traceback.format_exc(); event('archive_failed', error=manifest['error'])
    finally:
        progress.flush(); os.fsync(progress.fileno()); progress.close()
        manifest['inventory_before_manifest'] = [{'path':p.name,'bytes':p.stat().st_size} for p in sorted(OUT.iterdir())]
        usage = resource.getrusage(resource.RUSAGE_SELF)
        manifest['self_pre_manifest'] = {'user_seconds':usage.ru_utime,'system_seconds':usage.ru_stime,'peak_rss_bytes':usage.ru_maxrss}
        manifest['seconds_pre_manifest'] = time.monotonic()-START
        manifest['scope_of_samples'] = 'Entry after time import to sample before manifest; not full Popen-to-reap. Root outer 180s supervision required.'
        if usage.ru_maxrss > 256*MIB or manifest['seconds_pre_manifest'] > 180: manifest['status'] = 'FAIL'
        raw = encoded(manifest)
        if sum(r['bytes'] for r in manifest['inventory_before_manifest'])+len(raw) > 1024**3:
            manifest['status'] = 'FAIL'; raw = encoded(manifest)
        with (OUT/'manifest.json.tmp').open('xb') as dst:
            dst.write(raw); dst.flush(); os.fsync(dst.fileno())
        os.link(OUT/'manifest.json.tmp', OUT/'manifest.json'); (OUT/'manifest.json.tmp').unlink()
    actual_manifest = record(OUT/'manifest.json')
    need(actual_manifest == {'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}, 'manifest readback differs')
    seconds = time.monotonic()-START; usage = resource.getrusage(resource.RUSAGE_SELF)
    total = sum(p.stat().st_size for p in OUT.iterdir())
    passed = manifest['status'] == 'PASS' and seconds <= 180 and usage.ru_maxrss <= 256*MIB and total <= 1024**3
    print(json.dumps({'status':'PASS' if passed else 'FAIL','manifest':actual_manifest,
        'pid':os.getpid(),'supervisor_pid':os.getppid(), 'scientific_worker_invocations':0,
        'seconds_after_manifest':seconds,'rss_after_manifest':usage.ru_maxrss,'output_bytes':total,
        'scope':'Internal closure only; root must observe exit0 and full 180s Popen-to-reap separately'},sort_keys=True),flush=True)
    return 0 if passed else 1


if __name__ == '__main__':
    raise SystemExit(main())
