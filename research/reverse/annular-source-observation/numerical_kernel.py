"""Exploratory complex128 Galerkin and passive-source kernels; no run entry point.

Fourier coefficients use BOTH FFT directions with norm='forward'.  No physical
field is silently replaced by its real part.  For transverse retained inputs,
P(U cross curl U) is the full ordered Fourier--Leray nonlinearity B(U,U).

K=None means an UNMASKED CYCLIC FFT WORK GRID, not an alias-free operator on
arbitrary full-grid data.  Its caller must supply an alias-free support argument.
The source work grids below have that argument: H0 coordinate support <=7 gives
quadratic support <=14 on N=32; H1 support <=15 gives <=30 on N=64.
For a retained cube, 3*K<N excludes aliases back into that cube.

One rotational rhs uses two batched inverse transforms of 3 components and one
batched forward transform of 3 components: 6 inverse + 3 forward scalar FFTs.
Each AnnularSystem rhs ALWAYS evaluates three such products.  One four-stage
Lawson step therefore uses 72 inverse + 36 forward scalar FFTs, or 36 batched
FFT calls, in BOTH phases.  Diagnostics, allocations and linear algebra are
additional work.  This differs from the six-stress API-call organization in
TIME_METHOD_NOTE.md; the 108-scalar-transform total is unchanged for three sources.

This module chooses no datum, root, T, step count, tolerance, run or resource
budget, writes no files, and certifies no true-NS trajectory or source gate.
"""

import math
import numpy as np


def _integer(value, name, minimum=0):
    if isinstance(value, (bool, np.bool_)) or not isinstance(value, (int, np.integer)):
        raise TypeError(name + " must be an integer")
    value = int(value)
    if value < minimum:
        raise ValueError(name + " is too small")
    return value


def _complex_field(field, N=None):
    field = np.asarray(field)
    if field.dtype != np.dtype(np.complex128):
        raise TypeError("Fourier fields must already have dtype complex128")
    if field.ndim != 4 or field.shape[0] != 3:
        raise ValueError("Fourier field shape must be (3,N,N,N)")
    size = field.shape[1]
    if field.shape[2:] != (size, size) or (N is not None and size != N):
        raise ValueError("Fourier field grid does not match")
    return field


def hermitian_a0(field):
    """All represented modes, with the Euclidean Hermitian component norm."""
    field = np.asarray(field)
    if field.ndim < 1 or field.shape[0] != 3:
        raise ValueError("component axis must have length 3")
    return float(np.sum(np.sqrt(np.sum(np.abs(field) ** 2, axis=0))))


class FourierGrid:
    """Signed integer FFT grid and optional Galerkin cube mask.

    rhs computes P_K B(P_K U,P_K U) for transverse cube-supported U; it does
    not repair the input's divergence or conjugacy.  Initial off-cube values
    remain a caller error for a full time evolution and are measurable below.
    K=None makes no general de-aliasing claim.  Zero nonlinear mean is explicit.
    """

    def __init__(self, N, K=None):
        self.N = _integer(N, "N", 2)
        self.K = None if K is None else _integer(K, "K", 0)
        if self.K is not None and 3 * self.K >= self.N:
            raise ValueError("retained cube requires 3*K<N")
        index = np.arange(self.N, dtype=np.int64)
        self.frequencies = np.where(index < (self.N + 1) // 2, index, index - self.N)
        f = self.frequencies
        self.k = (f[:, None, None], f[None, :, None], f[None, None, :])
        self.k2 = self.k[0] ** 2 + self.k[1] ** 2 + self.k[2] ** 2
        self.laplacian = -self.k2.astype(np.float64)
        self.mask = None
        if self.K is not None:
            self.mask = ((np.abs(self.k[0]) <= self.K)
                         & (np.abs(self.k[1]) <= self.K)
                         & (np.abs(self.k[2]) <= self.K))
        self.negative_indices = (-index) % self.N

    def project(self, field):
        """Full bilinear k-dot Leray projection, output mask, and zero mean."""
        field = _complex_field(field, self.N)
        dot = sum(self.k[j] * field[j] for j in range(3))
        np.divide(dot, self.k2, out=dot, where=self.k2 != 0)
        dot[0, 0, 0] = 0
        result = field.copy()
        for j in range(3):
            result[j] -= self.k[j] * dot
        if self.mask is not None:
            result *= self.mask[None, ...]
        result[:, 0, 0, 0] = 0
        return result

    def curl(self, field):
        field = _complex_field(field, self.N)
        kx, ky, kz = self.k
        result = np.empty_like(field)
        result[0] = 1j * (ky * field[2] - kz * field[1])
        result[1] = 1j * (kz * field[0] - kx * field[2])
        result[2] = 1j * (kx * field[1] - ky * field[0])
        return result

    def rhs(self, U):
        U = _complex_field(U, self.N)
        spectrum = U if self.mask is None else U * self.mask[None, ...]
        curl_hat = self.curl(spectrum)
        velocity = np.fft.ifftn(spectrum, axes=(1, 2, 3), norm="forward")
        vorticity = np.fft.ifftn(curl_hat, axes=(1, 2, 3), norm="forward")
        del spectrum, curl_hat
        product = np.empty_like(velocity)
        product[0] = velocity[1] * vorticity[2] - velocity[2] * vorticity[1]
        product[1] = velocity[2] * vorticity[0] - velocity[0] * vorticity[2]
        product[2] = velocity[0] * vorticity[1] - velocity[1] * vorticity[0]
        del velocity, vorticity
        transformed = np.fft.fftn(product, axes=(1, 2, 3), norm="forward")
        del product
        return self.project(transformed)

    def diagnostics(self, U):
        """Raw numerical diagnostics; no tolerance, acceptance or repair.

        Norms use normalized Fourier measure.  Edge A0 means cube faces |ki|=K
        when a cube exists; it is None for an unmasked work grid.  Diagnostic
        temporaries and cost must be included if a driver uses this each step.
        """
        U = _complex_field(U, self.N)
        mode_square = np.sum(np.abs(U) ** 2, axis=0)
        mode_norm = np.sqrt(mode_square)
        dot = sum(self.k[j] * U[j] for j in range(3))
        neg = self.negative_indices
        conjugate_partner = np.conjugate(
            U[:, neg[:, None, None], neg[None, :, None], neg[None, None, :]])
        conjugacy = float(np.max(np.abs(U - conjugate_partner)))
        del conjugate_partner
        # At k, this is R U(R^{-1}k): component cycle plus inverse frequency cycle.
        rotated = U[[2, 0, 1], ...].transpose(0, 3, 1, 2)
        c3 = float(np.max(np.abs(U - rotated)))
        del rotated
        outside = edge = None
        if self.mask is not None:
            outside = float(np.sum(mode_norm[~self.mask]))
            face = self.mask & ((np.abs(self.k[0]) == self.K)
                                | (np.abs(self.k[1]) == self.K)
                                | (np.abs(self.k[2]) == self.K))
            edge = float(np.sum(mode_norm[face]))
        return {
            "finite": bool(np.all(np.isfinite(U))),
            "mean_hermitian_norm": float(np.sqrt(mode_square[0, 0, 0])),
            "divergence_max_abs": float(np.max(np.abs(dot))),
            "conjugacy_component_max_abs": conjugacy,
            "c3_component_max_abs": c3,
            "energy_normalized": float(0.5 * np.sum(mode_square)),
            "viscous_dissipation_normalized": float(np.sum(self.k2 * mode_square)),
            "a0": float(np.sum(mode_norm)),
            "off_cube_a0": outside,
            "cube_face_a0": edge,
        }


class Band:
    """All integer modes lo<=|k|<hi, in lexicographic compact order (3,m).

    Integer radii are compared by squared integers.  Embeddings require strict
    |ki|<N/2 and hence exclude every Nyquist plane; no folding or duplicate modes.
    """

    def __init__(self, lo, hi):
        self.lo = _integer(lo, "lo", 0)
        self.hi = _integer(hi, "hi", 1)
        if self.lo >= self.hi:
            raise ValueError("band requires lo<hi")
        axis = np.arange(1 - self.hi, self.hi, dtype=np.int64)
        x, y, z = np.meshgrid(axis, axis, axis, indexing="ij")
        squared = x * x + y * y + z * z
        selected = (self.lo ** 2 <= squared) & (squared < self.hi ** 2)
        self.modes = np.column_stack((x[selected], y[selected], z[selected]))
        self.size = len(self.modes)
        self.laplacian = -np.sum(self.modes ** 2, axis=1).astype(np.float64)
        self._index_cache = {}

    def indices(self, N):
        N = _integer(N, "N", 2)
        if 2 * (self.hi - 1) >= N:
            raise ValueError("band would reach a Nyquist plane or alias")
        if N not in self._index_cache:
            self._index_cache[N] = tuple(self.modes[:, j] % N for j in range(3))
        return self._index_cache[N]

    def gather(self, field):
        field = _complex_field(field)
        i, j, k = self.indices(field.shape[1])
        return field[:, i, j, k]

    def scatter(self, compact, N):
        compact = np.asarray(compact)
        if compact.dtype != np.dtype(np.complex128) or compact.shape != (3, self.size):
            raise ValueError("compact band must be complex128 with shape (3,m)")
        N = _integer(N, "N", 2)
        i, j, k = self.indices(N)
        result = np.zeros((3, N, N, N), dtype=np.complex128)
        result[:, i, j, k] = compact
        return result


class AnnularSystem:
    """Full retained velocity plus two compact, same-stage passive sources.

    Both source rhs blocks are always computed, even before a.  Only the time
    update suppresses the second block in the first segment.  No G enters rhs.
    """

    def __init__(self, N, K):
        K = _integer(K, "K", 32)
        self.grid = FourierGrid(N, K)
        self.bands = (Band(4, 8), Band(8, 16), Band(16, 32))
        for band in self.bands:
            band.indices(self.grid.N)
        self.first_work_grid = FourierGrid(32)
        self.second_work_grid = FourierGrid(64)
        self.laplacians = (self.grid.laplacian,
                           self.bands[1].laplacian, self.bands[2].laplacian)

    def rhs(self, U):
        U = _complex_field(U, self.grid.N)
        full = self.grid.rhs(U)
        first_input = self.bands[0].scatter(self.bands[0].gather(U), 32)
        first = self.bands[1].gather(self.first_work_grid.rhs(first_input))
        del first_input
        second_input = self.bands[1].scatter(self.bands[1].gather(U), 64)
        second = self.bands[2].gather(self.second_work_grid.rhs(second_input))
        return full, first, second


def lawson_step(state, laplacians, nonlinear_callback_only_U, h, second_active):
    """TM.6, with four callbacks of ONLY the full velocity stage.

    Inputs are not mutated; the callback must likewise not mutate its input.
    The three blocks may have unrelated shapes, including small toy arrays.
    Each real nonpositive Laplacian must broadcast to its own state block.
    Inactive W still heat-evolves, while its computed nonlinear source is unused.
    Streaming weighted sums avoid storing four full-grid nonlinear outputs.
    No projection, reality repair, acceptance threshold or reset is hidden here.
    """
    if len(state) != 3 or len(laplacians) != 3:
        raise ValueError("state and laplacians must each have three blocks")
    if not isinstance(second_active, (bool, np.bool_)):
        raise TypeError("second_active must be Boolean")
    h = float(h)
    if not math.isfinite(h) or h <= 0:
        raise ValueError("h must be finite and positive")
    blocks = tuple(np.asarray(block, dtype=np.complex128) for block in state)
    linear = []
    for block, lap in zip(blocks, laplacians):
        if np.iscomplexobj(lap):
            raise TypeError("Laplacians must be real")
        lap = np.asarray(lap, dtype=np.float64)
        if not np.all(np.isfinite(lap)) or np.any(lap > 0):
            raise ValueError("Laplacians must be finite and nonpositive")
        if np.broadcast_shapes(block.shape, lap.shape) != block.shape:
            raise ValueError("Laplacian does not broadcast to its block")
        linear.append(lap)
    E = tuple(np.exp(h * lap) for lap in linear)
    E_half = tuple(np.exp((h / 2) * lap) for lap in linear)
    result = [factor * block for factor, block in zip(E, blocks)]

    def evaluate(U):
        values = nonlinear_callback_only_U(U)
        if len(values) != 3:
            raise ValueError("nonlinear callback must return three blocks")
        values = tuple(np.asarray(value, dtype=np.complex128) for value in values)
        if any(value.shape != block.shape for value, block in zip(values, blocks)):
            raise ValueError("nonlinear callback block shapes differ from state")
        return values

    def accumulate(values, factors, weight):
        for j in range(3):
            if j != 2 or second_active:
                term = values[j] if factors is None else factors[j] * values[j]
                result[j] += weight * term

    U = blocks[0]
    values = evaluate(U)
    accumulate(values, E, h / 6)
    stage = E_half[0] * (U + (h / 2) * values[0])
    del values
    values = evaluate(stage)
    del stage
    accumulate(values, E_half, h / 3)
    stage = E_half[0] * U + (h / 2) * values[0]
    del values
    values = evaluate(stage)
    del stage
    accumulate(values, E_half, h / 3)
    stage = E[0] * U + h * E_half[0] * values[0]
    del values
    values = evaluate(stage)
    accumulate(values, None, h / 6)
    return tuple(result)


def indexed_step(state, laplacians, nonlinear_callback_only_U, h, index, nsteps):
    """One externally indexed step; half-time logic never uses floating time.

    nsteps is positive/even and index ranges from 0 through nsteps-1.  At the
    first post-a step ONLY W is reset; the accepted U(a), G(a), and h2(a) remain.
    The preceding step's fourth stage stays inactive even though its time is a.
    The caller supplies h converted from the fixed rational T and node ratio,
    and owns sequential indexing and the record of that conversion error.
    """
    nsteps = _integer(nsteps, "nsteps", 2)
    index = _integer(index, "index", 0)
    if nsteps % 2 or index >= nsteps:
        raise ValueError("need even nsteps and 0<=index<nsteps")
    if len(state) != 3:
        raise ValueError("state must have three blocks")
    if index == nsteps // 2:
        state = (state[0], state[1], np.zeros_like(state[2], dtype=np.complex128))
    return lawson_step(state, laplacians, nonlinear_callback_only_U, h,
                       second_active=(index >= nsteps // 2))
