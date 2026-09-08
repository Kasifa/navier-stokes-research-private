"""One locked implementation validation OR one complete-step cost worker.

Run only through run_numerical.py after static review and source commit binding.
No trajectory, actual annular gate, or rigorous floating-point bound is computed.
"""
import time
PROCESS_START = time.perf_counter()
import argparse
import contextlib
from fractions import Fraction
import hashlib
import io
import json
import math
import os
from pathlib import Path
import sys
import traceback
sys.dont_write_bytecode = True

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
FFT_TOL = 2e-12
TOY_TOL = 2e-13


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(block)
    return digest.hexdigest()


def json_default(value):
    if isinstance(value, complex):
        return {'real': value.real, 'imaginary': value.imag}
    if isinstance(value, Fraction):
        return {'numerator': str(value.numerator), 'denominator': str(value.denominator)}
    if hasattr(value, 'item'):
        return value.item()
    raise TypeError('unsupported JSON value: ' + type(value).__name__)


def safe_metadata(value):
    """Preserve nonfinite failure evidence as labels, never invalid JSON."""
    if isinstance(value, float) and not math.isfinite(value):
        return {'nonfinite': repr(value)}
    if isinstance(value, dict):
        return {key: safe_metadata(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [safe_metadata(item) for item in value]
    if isinstance(value, (complex, Fraction)) or hasattr(value, 'item'):
        return safe_metadata(json_default(value))
    return value


def write_json(path, value):
    with Path(path).open('x', encoding='utf-8') as stream:
        json.dump(safe_metadata(value), stream, default=json_default, ensure_ascii=False,
                  indent=2, allow_nan=False)
        stream.write('\n')


def locked_hashes(lock):
    result = {}
    for row in lock['bindings']:
        path = (REPO / row['path']).resolve()
        if not path.is_relative_to(REPO):
            raise ValueError('source binding outside worktree')
        digest = sha(path)
        if digest != row['sha256']:
            raise ValueError('source binding mismatch: ' + row['path'])
        result[row['path']] = digest
    return result


class FFTCounts:
    """Count the actual NumPy FFT calls, including their grid and components."""
    def __init__(self, np):
        self.counts = {}
        for name in ('fftn', 'ifftn'):
            original = getattr(np.fft, name)
            def wrapped(a, *args, _name=name, _original=original, **kwargs):
                if args or kwargs.get('axes') != (1, 2, 3):
                    raise ValueError('uncontracted FFT call signature')
                if kwargs.get('norm') != 'forward' or a.ndim != 4:
                    raise ValueError('uncontracted FFT normalization/shape')
                key = _name + ':' + 'x'.join(str(x) for x in a.shape[1:])
                record = self.counts.setdefault(key, {'batched_api_calls': 0,
                                                      'scalar_3d_transforms': 0})
                record['batched_api_calls'] += 1
                record['scalar_3d_transforms'] += a.shape[0]
                return _original(a, **kwargs)
            setattr(np.fft, name, wrapped)


class Experiment:
    def __init__(self, np, kernel, reference, output):
        self.np, self.kernel, self.reference, self.output = np, kernel, reference, output
        self.checks = []
        self.artifacts = []
        self.timings = {}
        self.progress_file = (output / 'progress.jsonl').open('x', encoding='utf-8')

    def progress(self, event, **values):
        self.progress_file.write(json.dumps({'event': event,
            'worker_elapsed_seconds': time.perf_counter() - PROCESS_START,
            **values}, default=json_default, allow_nan=False) + '\n')
        self.progress_file.flush()

    def require(self, name, passed, **evidence):
        self.checks.append({'name': name, 'passed': bool(passed), **evidence})
        if not passed:
            raise AssertionError(name)

    def compare(self, name, actual, reference, tolerance=FFT_TOL):
        np = self.np
        actual, reference = np.asarray(actual), np.asarray(reference)
        if actual.shape != reference.shape:
            raise AssertionError(name + ' shape mismatch')
        finite = bool(np.all(np.isfinite(actual)) and np.all(np.isfinite(reference)))
        error = float(np.max(np.abs(actual - reference))) if actual.size else 0.0
        scale = max(1.0, float(np.max(np.abs(reference))) if reference.size else 0.0)
        self.require(name, finite and error <= tolerance * scale,
                     finite=finite, max_component_error=error if finite else None,
                     reference_scale=scale if finite else None, tolerance=tolerance)

    def field(self, modes, N):
        result = self.np.zeros((3, N, N, N), dtype=self.np.complex128)
        for k, value in modes.items():
            if any(2 * abs(x) >= N for x in k):
                raise ValueError('reference mode cannot embed without Nyquist alias')
            result[:, k[0] % N, k[1] % N, k[2] % N] = value
        return result

    def spectral_defects(self, name, grid, field):
        np = self.np
        diagnostics = grid.diagnostics(field)
        scale = max(1.0, float(np.max(np.abs(field))))
        kscale = max(1.0, float(np.sqrt(np.max(grid.k2))))
        mean = float(np.max(np.abs(field[:, 0, 0, 0]))) / scale
        conjugacy = diagnostics['conjugacy_component_max_abs'] / scale
        divergence = diagnostics['divergence_max_abs'] / (kscale * scale)
        self.require(name, diagnostics['finite'] and max(mean, conjugacy, divergence) <= FFT_TOL,
                     normalized_mean=mean, normalized_conjugacy=conjugacy,
                     normalized_divergence=divergence, diagnostics=diagnostics,
                     c3_required=False, tolerance=FFT_TOL)

    def save_npz(self, name, **arrays):
        start = time.perf_counter()
        path = self.output / name
        # The enclosing run directory is exclusive; still refuse file overwrite.
        with path.open('xb') as stream:
            self.np.savez(stream, **arrays)
        self.artifacts.append({'file': name, 'bytes': path.stat().st_size,
                               'sha256': sha(path), 'format': 'lossless uncompressed npz'})
        self.timings[name + '_write_and_hash_seconds'] = time.perf_counter() - start

    def save_reference(self, name, evidence):
        path = self.output / name
        write_json(path, evidence)
        self.artifacts.append({'file': name, 'bytes': path.stat().st_size, 'sha256': sha(path)})

    def validation(self):
        np, k, ref = self.np, self.kernel, self.reference
        fixtures, references = {}, {}
        for label, N, lo, hi, high in [('H0', 32, 8, 16, (13, 1, 1)),
                                     ('H1', 64, 16, 32, (29, 1, 1))]:
            self.progress('source_test_start', label=label)
            fixture = ref.source_fixture(label)
            direct, exact = ref.ordered_rhs(fixture, return_evidence=True)
            fixtures[label], references[label] = fixture, direct
            self.require(label + '_high_sum_nonzero', any(z != 0 for z in direct[high]),
                         frequency=list(high), reference=direct[high])
            grid, band = k.FourierGrid(N), k.Band(lo, hi)
            source = self.field(fixture, N)
            actual, expected = grid.rhs(source), self.field(direct, N)
            self.compare(label + '_all_grid', actual, expected)
            self.compare(label + '_all_target_band', band.gather(actual), band.gather(expected))
            self.spectral_defects(label + '_defects', grid, actual)
            self.save_reference(label + '-exact-reference.json', exact)
            self.save_npz(label + '-source.npz', input=source, actual=actual,
                          reference=expected, target_modes=band.modes)
            del source, actual, expected, grid, band
        self.progress('joint_test_start', N=128, K=42)
        joint = {**fixtures['H0'], **fixtures['H1']}
        direct, exact = ref.ordered_rhs(joint, return_evidence=True)
        system = k.AnnularSystem(128, 42)
        state = self.field(joint, 128)
        actual = system.rhs(state)
        expected = self.field(direct, 128)
        expected *= system.grid.mask[None, ...]
        self.compare('joint_all_grid_including_outside_cube', actual[0], expected)
        self.spectral_defects('joint_defects', system.grid, actual[0])
        for i, label in enumerate(('H0', 'H1'), start=1):
            band = system.bands[i]
            target = np.asarray([references[label].get(tuple(int(x) for x in mode), [0j]*3)
                                 for mode in band.modes], dtype=np.complex128).T
            self.compare('joint_' + label + '_all_target_band', actual[i], target)
        # Full large RHS and input can be reconstructed from sparse exact reference.
        # Save the full actual RHS; avoid duplicating 100 MiB of reference zeros.
        self.save_reference('joint-exact-reference.json', exact)
        self.save_npz('joint-source.npz', actual_full=actual[0], actual_first=actual[1],
                      actual_second=actual[2], first_modes=system.bands[1].modes,
                      second_modes=system.bands[2].modes)
        del state, actual, expected, system, target
        self.progress('shear_test_start')
        grid = k.FourierGrid(16, 4)
        shear = self.field({(1, 0, 0): [0j, 1+0j, 0j],
                            (-1, 0, 0): [0j, 1+0j, 0j]}, 16)
        empty = np.empty((0,), dtype=np.complex128)
        shear_rhs = grid.rhs(shear)
        self.compare('shear_nonlinearity_zero', shear_rhs, np.zeros_like(shear_rhs))
        stage_count = [0]
        def shear_nonlinear(U):
            stage_count[0] += 1
            return grid.rhs(U), empty, empty
        heat = k.lawson_step((shear, empty, empty), (grid.laplacian, [], []),
                            shear_nonlinear, 1/64, True)
        self.compare('shear_pure_heat', heat[0], np.exp(-1/64) * shear)
        self.require('shear_four_stages_empty_histories', stage_count[0] == 4
                     and heat[1].size == heat[2].size == 0, stages=stage_count[0])
        self.spectral_defects('shear_output_defects', grid, heat[0])
        self.save_npz('shear.npz', input=shear, rhs=shear_rhs, output=heat[0])
        del grid, shear, shear_rhs, heat
        self.toy_tests()
        return {'scope': 'FIXED_IMPLEMENTATION_TESTS_ONLY',
                'coverage_limit': 'No dynamic large-cube edge stress or full 160-grid reference test; no NS certificate.'}

    def toy_tests(self):
        np, k, ref = self.np, self.kernel, self.reference
        self.progress('toy_tests_start')
        initial = ref.toy_initial_state()
        state = tuple(np.asarray(initial[name], dtype=np.complex128) for name in ('U', 'G', 'W'))
        laps = (np.array([-1., -4.]), np.array([-9.]), np.array([-16.]))
        stages = []
        def nonlinear(U):
            stages.append(U.copy().tolist())
            return np.array([U[0]*U[1], U[0]**2]), np.array([U[0]**2]), np.array([U[1]**2])
        def blocks_compare(label, actual, expected):
            for j, name in enumerate(('U', 'G', 'W')):
                self.compare(label + '_' + name, actual[j], expected[name], TOY_TOL)
        evidence = {'scope': 'generic time-integrator tests, not NS dynamics'}
        for phase in (0, 1):
            stages.clear()
            expected = ref.reference_step(*state, phase)
            actual = k.lawson_step(state, laps, nonlinear, 1/64, bool(phase))
            blocks_compare('toy_phase_' + str(phase), actual, expected)
            self.require('toy_four_stages_' + str(phase), len(stages) == 4)
            for j, stage in enumerate(stages):
                self.compare('toy_stage_' + str(phase) + '_' + str(j), stage,
                             expected['stages'][j]['X']['U'], TOY_TOL)
            evidence['phase_' + str(phase)] = {'reference': expected,
                'actual': {name: value.tolist() for name, value in zip(('U','G','W'), actual)},
                'actual_velocity_stages': list(stages)}
        pair = ref.reference_boundary_pair()
        start = (state[0], state[1], np.zeros_like(state[2]))
        first = k.indexed_step(start, laps, nonlinear, 1/64, 0, 2)
        blocks_compare('toy_pair_first', first, pair['phase0_step'])
        second = k.indexed_step(first, laps, nonlinear, 1/64, 1, 2)
        blocks_compare('toy_pair_second', second, pair['phase1_step'])
        fake_entry = (first[0], first[1], np.array([5+6j]))
        fake = k.indexed_step(fake_entry, laps, nonlinear, 1/64, 1, 2)
        for i, name in enumerate(('U', 'G', 'W')):
            self.compare('boundary_fake_W_only_reset_' + name, fake[i], second[i], TOY_TOL)
        base = k.lawson_step(state, laps, nonlinear, 1/64, True)
        changed = k.lawson_step((state[0], state[1] + (1-2j), state[2]),
                               laps, nonlinear, 1/64, True)
        self.compare('changed_G_does_not_feed_U', changed[0], base[0], TOY_TOL)
        self.compare('changed_G_does_not_feed_W', changed[2], base[2], TOY_TOL)
        self.compare('changed_G_heat_only', changed[1]-base[1],
                     np.array([np.exp(-9/64)*(1-2j)]), TOY_TOL)
        evidence['pair_reference'] = pair
        evidence['pair_actual'] = [[b.tolist() for b in x] for x in (first, second, fake)]
        evidence['changed_G_actual'] = {'base': [b.tolist() for b in base],
                                       'changed': [b.tolist() for b in changed]}
        self.save_reference('toy-evidence.json', evidence)

    def benchmark(self, run_id):
        np, k = self.np, self.kernel
        N, K = (128, 42) if run_id == 'bench128' else (160, 53)
        self.progress('cost_setup_start', N=N, K=K)
        data_path = HERE / 'input-preparation.json'
        data = json.loads(data_path.read_text())
        modes = {tuple(row['frequency']): [complex(float.fromhex(z), 0)
                                          for z in row['float_hex']]
                 for row in data['twelve_modes']}
        if len(modes) != 12:
            raise ValueError('expected twelve accepted coefficients')
        q = data['fixed_observation']['T']
        exact_h = Fraction(int(q['numerator']), int(q['denominator'])) / 256
        h = float(exact_h)
        readback = Fraction.from_float(h)
        h_record = {'exact': exact_h, 'float_hex': h.hex(), 'readback': readback,
                    'signed_conversion_error': readback - exact_h,
                    'absolute_conversion_error': abs(readback - exact_h)}
        system = k.AnnularSystem(N, K)
        state = (self.field(modes, N), np.zeros((3, system.bands[1].size), dtype=np.complex128),
                 np.zeros((3, system.bands[2].size), dtype=np.complex128))
        stages = []
        def nonlinear(U):
            self.progress('stage_start', stage=len(stages)+1)
            start = time.perf_counter()
            value = system.rhs(U)
            stages.append(time.perf_counter() - start)
            self.progress('stage_end', stage=len(stages), rhs_seconds=stages[-1])
            return value
        self.timings['worker_start_to_step_seconds'] = time.perf_counter() - PROCESS_START
        start = time.perf_counter()
        output = k.indexed_step(state, system.laplacians, nonlinear, h, 128, 256)
        self.timings['complete_augmented_step_seconds'] = time.perf_counter() - start
        self.require('cost_four_stages', len(stages) == 4, rhs_seconds=stages)
        self.progress('diagnostics_start')
        start = time.perf_counter()
        diagnostics = system.grid.diagnostics(output[0])
        compact = [{'finite': bool(np.all(np.isfinite(block))),
                    'a0': k.hermitian_a0(block), 'max_component_abs': float(np.max(np.abs(block)))}
                   for block in output[1:]]
        self.timings['diagnostics_seconds'] = time.perf_counter() - start
        self.require('cost_output_finite', diagnostics['finite'] and all(x['finite'] for x in compact))
        self.save_npz('cost-output.npz', U=output[0], G=output[1], W=output[2],
                      first_modes=system.bands[1].modes, second_modes=system.bands[2].modes)
        return {'scope': 'COST_ONLY_NONPHYSICAL_SEGMENT_STATE', 'N': N, 'K': K,
                'input_sha256': sha(data_path), 'step': h_record, 'index': 128, 'nsteps': 256,
                'physical_state_warning': 'Original approximate initial state used in post-a cost branch; not U(a) or original source integral.',
                'diagnostics': diagnostics, 'passive_block_diagnostics': compact}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--run-id', required=True, choices=('validation', 'bench128', 'bench160'))
    parser.add_argument('--output-dir', type=Path, required=True)
    parser.add_argument('--source-lock', type=Path, required=True)
    args = parser.parse_args()
    if args.output_dir.resolve() != HERE / 'numerical-runs' / args.run_id:
        raise ValueError('output directory must match fixed run ID')
    lock = json.loads(args.source_lock.read_text())
    start_hashes = locked_hashes(lock)
    result = {'schema': 1, 'run_id': args.run_id, 'status': 'FAIL',
              'pid': os.getpid(), 'supervisor_pid': os.getppid(),
              'scientific_worker_invocations': 1, 'source_lock_sha256': sha(args.source_lock),
              'source_hashes_start': start_hashes}
    experiment = None
    counter = None
    try:
        import numpy as np
        import numerical_kernel as kernel
        import numerical_reference as reference
        result['import_completed_worker_seconds'] = time.perf_counter() - PROCESS_START
        config = io.StringIO()
        with contextlib.redirect_stdout(config):
            np.show_config()
        result['environment'] = {'python': sys.version, 'executable': sys.executable,
            'sys_platform': sys.platform, 'uname': list(os.uname()), 'numpy_version': np.__version__,
            'numpy_configuration': config.getvalue(), 'cpu_count': os.cpu_count(),
            'thread_environment': {key: os.environ.get(key) for key in
                ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS')},
            'fft_function_module': np.fft.fftn.__module__,
            'dtype': 'complex128', 'fft_normalization_both_directions': 'forward'}
        counter = FFTCounts(np)
        experiment = Experiment(np, kernel, reference, args.output_dir)
        experiment.progress('imports_completed')
        details = experiment.validation() if args.run_id == 'validation' else experiment.benchmark(args.run_id)
        if args.run_id != 'validation':
            api = sum(x['batched_api_calls'] for x in counter.counts.values())
            scalar = sum(x['scalar_3d_transforms'] for x in counter.counts.values())
            experiment.require('cost_actual_transform_counts', api == 36 and scalar == 108,
                               batched_api_calls=api, scalar_3d_transforms=scalar)
        result.update(details)
        result['fft_actual_counts_by_grid'] = counter.counts
        result['source_hashes_end'] = locked_hashes(lock)
        if sha(args.source_lock) != result['source_lock_sha256']:
            raise ValueError('source lock changed during worker')
        result['status'] = 'PASS'
    except BaseException:
        result['exception'] = traceback.format_exc()
    finally:
        if counter is not None:
            result['fft_actual_counts_by_grid'] = counter.counts
        if experiment is not None:
            result['checks'] = experiment.checks
            result['artifacts'] = experiment.artifacts
            result['timings'] = experiment.timings
            experiment.progress('worker_finishing', status=result['status'])
            experiment.progress_file.close()
        result['worker_elapsed_before_result_serialization_seconds'] = time.perf_counter() - PROCESS_START
        result['worker_process_cpu_seconds'] = time.process_time()
        write_json(args.output_dir / 'result.json', result)
    print(json.dumps({'run_id': args.run_id, 'status': result['status']}), flush=True)
    return 0 if result['status'] == 'PASS' else 1


if __name__ == '__main__':
    raise SystemExit(main())
