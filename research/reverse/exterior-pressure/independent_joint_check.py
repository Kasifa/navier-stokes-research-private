from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json

# Exact integer/Fraction calculation used in JOINT_TEST_REVIEW.md section 7.
# Run from /Users/kasifa/Documents/Math/navier-stokes-reverse.
Q = [
    [[0, 1, 0], [1, 0, 0], [0, 0, -1]],
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
    [[0, 0, 1], [1, 0, 0], [0, 1, 0]],
]


def det(a):
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


rots = []
for k, a in enumerate(Q):
    gram = [
        [sum(a[t][i] * a[t][j] for t in range(3)) for j in range(3)]
        for i in range(3)
    ]
    rots.append(
        {
            "i": k + 1,
            "det": det(a),
            "gram_identity": gram == Q[1],
            "Qe2": [a[t][1] for t in range(3)],
        }
    )

checks = {
    "rotations": rots,
    "T_less_bound": F(1, 100) < F(2, 3) ** 10,
    "inner_outer_gap_lower": str(F(29, 20) - F(4, 3)),
    "outer_radius_upper": str(F(31, 20) * F(2, 3) ** 4),
    "outer_d_less_quarter": F(2, 3) ** 4 < F(1, 4),
    "y_star_squared_from_ball_center": str(2 * F(1, 40) ** 2),
    "epsilon_squared": str(F(1, 20) ** 2),
    "s_star": str(F(1, 20) ** 2 - 2 * F(1, 40) ** 2),
    "q_prefactor": str(16 * F(1, 40) ** 2),
}
print(json.dumps(checks, ensure_ascii=False, indent=2))
for name in [
    "research/reverse/exterior-pressure/JOINT_TEST_CONTRACT.md",
    "research/reverse/exterior-pressure/JOINT_TEST_PROOF.md",
    "research/reverse/exterior-pressure/PROOF.md",
    "research/reverse/next-concentration/PROOF.md",
    "research/reverse/next-concentration/CONTRACT.md",
    "research/clay_b_frequency_cascade_budget_20260907.md",
]:
    b = Path(name).read_bytes()
    print(name, len(b), sha256(b).hexdigest())
