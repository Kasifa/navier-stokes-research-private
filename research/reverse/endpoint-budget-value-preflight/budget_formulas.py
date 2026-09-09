"""Fixed numerical-value formulas. No imports, arrays, or calls at import time.

The caller supplies NumPy inside the sole authorised worker. These floating
values have no certified enclosure direction or Gauss-quadrature error bound.
"""
def bernstein_segment(np, left, slope_left, right, slope_right, h):
    controls = np.stack((left, left + h * slope_left / 3,
                         right - h * slope_right / 3, right))
    gram = np.empty((4, 4), dtype=np.float64)
    for i in range(4):
        for j in range(4):
            gram[i, j] = np.vdot(controls[i], controls[j]).real
    bin3, bin6 = (1, 3, 3, 1), (1, 6, 15, 20, 15, 6, 1)
    ordered = np.zeros(7, dtype=np.float64)
    for i in range(4):
        for j in range(4):
            ordered[i+j] += bin3[i] * bin3[j] * gram[i, j] / bin6[i+j]
    explicit = np.array([
        gram[0, 0], gram[0, 1], (2*gram[0, 2] + 3*gram[1, 1])/5,
        (gram[0, 3] + 9*gram[1, 2])/10,
        (2*gram[1, 3] + 3*gram[2, 2])/5, gram[2, 3], gram[3, 3]],
        dtype=np.float64)
    # Preserve complete vector discrepancies, not just a rounded maximum.
    endpoint_checks = np.stack((controls[0]-left, controls[3]-right,
                               3*(controls[1]-controls[0])/h-slope_left,
                               3*(controls[3]-controls[2])/h-slope_right))
    return controls, gram, ordered, explicit, endpoint_checks


def legendre_rule64(np):
    indices = np.arange(1, 64, dtype=np.float64)
    off = indices / np.sqrt(4*indices*indices - 1)
    jacobi = np.diag(off, 1) + np.diag(off, -1)
    nodes = np.linalg.eigvalsh(jacobi)
    if not np.all(np.isfinite(nodes)) or not np.all((-1 < nodes) & (nodes < 1)):
        raise ValueError("64-point rule has nonfinite or exterior nodes")
    if not np.all(np.diff(nodes) > 0):
        raise ValueError("64-point rule nodes are not strictly ordered")
    previous, current = np.ones(64), nodes.copy()
    for n in range(1, 64):
        previous, current = current, ((2*n+1)*nodes*current-n*previous)/(n+1)
    derivative = 64*(nodes*current-previous)/(nodes*nodes-1)
    weights = 2/((1-nodes*nodes)*derivative*derivative)
    if not np.all(np.isfinite(weights)) or not np.all(weights > 0):
        raise ValueError("64-point rule has invalid weights")
    return nodes, weights, current, derivative


def phi6(np, rho, h):
    rho = np.asarray(rho, dtype=np.float64)
    if not np.all(np.isfinite(rho)) or not np.all((0 <= rho) & (rho <= 1)):
        raise ValueError("Phi arguments must lie in the closed unit interval")
    scaled = [np.ones_like(rho), 2-rho]
    for n in range(1, 6):
        scaled.append(((2*n+1)*(2-rho)*scaled[n]
                       - n*rho*rho*scaled[n-1])/(n+1))
    denominator = np.zeros_like(rho)
    for n in range(7):
        denominator += (2*n+1)*rho**(12-2*n)*scaled[n]*scaled[n]
    if not np.all(np.isfinite(denominator)) or not np.all(denominator > 0):
        raise ValueError("Phi denominator is not positive and finite")
    values = h*rho**13/denominator
    # Evaluate the endpoint identities with the same polynomial expression;
    # the caller preserves their differences from 0 and h/49.
    return values, np.stack(scaled), denominator
