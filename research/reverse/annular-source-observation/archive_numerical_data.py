"""Lossless byte archival only: no array interpretation or science rerun.

Retain original immutable npz files in their run directories. Store gzip copies
outside those directories, verify decompressed original size/SHA, and write an
explicit restoration manifest. Existing archive directory is never overwritten.
"""
import datetime
import gzip
import hashlib
import json
from pathlib import Path
import sys
import time
import zlib

HERE = Path(__file__).resolve().parent
RUNS = ('validation', 'bench128', 'bench160')


def record(path):
    digest, size = hashlib.sha256(), 0
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(block)
            size += len(block)
    return {'bytes': size, 'sha256': digest.hexdigest()}


def main():
    started = time.perf_counter()
    archive = HERE / 'numerical-data-archive'
    archive.mkdir()
    manifest = {'scope': 'LOSSLESS_BYTE_ARCHIVE_ONLY_NO_SCIENTIFIC_EXECUTION',
        'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'script': record(Path(__file__).resolve()), 'python': sys.version,
        'zlib_version': zlib.ZLIB_VERSION, 'zlib_runtime_version': zlib.ZLIB_RUNTIME_VERSION,
        'gzip_compresslevel': 6, 'gzip_mtime': 0, 'files': []}
    for run in RUNS:
        directory = HERE / 'numerical-runs' / run
        receipt_path = directory / 'execution.json'
        receipt = json.loads(receipt_path.read_text())
        if receipt['status'] != 'PASS':
            raise ValueError('archive expects all three accepted executions')
        for row in receipt['artifact_inventory_before_receipt']:
            if not row['path'].endswith('.npz'):
                continue
            source = directory / row['path']
            original = record(source)
            if original != {'bytes': row['bytes'], 'sha256': row['sha256']}:
                raise ValueError('immutable raw array bytes differ from receipt')
            target = archive / (run + '-' + source.name + '.gz')
            with source.open('rb') as src, target.open('xb') as dst:
                with gzip.GzipFile(filename='', mode='wb', compresslevel=6, mtime=0,
                                   fileobj=dst) as compressed:
                    for block in iter(lambda: src.read(1024 * 1024), b''):
                        compressed.write(block)
            restored_hash, restored_size = hashlib.sha256(), 0
            with gzip.open(target, 'rb') as stream:
                for block in iter(lambda: stream.read(1024 * 1024), b''):
                    restored_hash.update(block)
                    restored_size += len(block)
            if {'bytes': restored_size, 'sha256': restored_hash.hexdigest()} != original:
                raise ValueError('lossless restoration failed')
            manifest['files'].append({'original': str(source.relative_to(HERE)),
                'original_record': original, 'archive': str(target.relative_to(HERE)),
                'archive_record': record(target), 'restoration_verified': True,
                'execution_receipt': record(receipt_path)})
    manifest['archive_wall_seconds'] = time.perf_counter() - started
    manifest['restoration'] = 'gzip-decompress each archive to original path only when absent; verify original byte count and SHA256. Never overwrite an existing run file.'
    with (archive / 'manifest.json').open('x') as stream:
        json.dump(manifest, stream, indent=2, allow_nan=False)
        stream.write('\n')
    print(json.dumps({'scope': manifest['scope'], 'files': len(manifest['files']),
        'original_bytes': sum(x['original_record']['bytes'] for x in manifest['files']),
        'archive_bytes': sum(x['archive_record']['bytes'] for x in manifest['files']),
        'restoration_verified': True, 'seconds': manifest['archive_wall_seconds']}))


if __name__ == '__main__':
    main()
