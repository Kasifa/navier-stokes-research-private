from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
root=Path('research/reverse/exterior-pressure')
for name in ['JOINT_TEST_PROOF.md','PROOF.md','RESCALED_EXIT_CONTRACT.md','RESCALED_EXIT_PROOF.md']:
 print(name,sha256((root/name).read_bytes()).hexdigest())
checks={'test_ball_inside_shell': F(2,40**2)<(F(1,20)-F(1,400))**2,'test_ball_off_axis':F(1,40)>F(1,400),'point_l1':F(1,40)+F(61,40)==F(31,20),'bump_argument':F(1,20)**2-2*F(1,40)**2==F(1,800),'q_coefficient':16*F(1,40)**2==F(1,100),'h_double_prime_positive':1-2*F(1,800)>0,'linear_error':2+F(2,5)*F(31,20)*2+6==F(231,25),'linear_error_lt_10':F(231,25)<10,'rescale_linear_sum':F(3,5)+F(2,5)==1,'rescale_viscous_power':F(8,5)-F(7,5)==F(1,5)}
print({'rational_checks':checks,'PASS':all(checks.values())})
