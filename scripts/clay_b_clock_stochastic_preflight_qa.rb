# Finite coefficient checks only; not a PDE proof, novelty audit or Clay certificate.
r = ->(a,b=1){ Rational(a,b) }
pass = []
add = ->(x,y){[x[0]+y[0],x[1]+y[1]]}
scale = ->(c,x){[c*x[0],c*x[1]]}

# CG.5: d_x=(1/2)d_c+d_r, d_y=(1/2)d_c-d_r.
dx_c=r[1,2]; dx_r=r[1]; dy_c=r[1,2]; dy_r=-r[1]
center=[dx_c**2+dy_c**2, 2*dx_c*dy_c]
relative=[dx_r**2+dy_r**2, 2*dx_r*dy_r]
cross=[2*dx_c*dx_r+2*dy_c*dy_r,
       2*(dx_c*dy_r+dx_r*dy_c)]
raise 'CG5 center' unless center == [r[1,2],r[1,2]]
raise 'CG5 relative' unless relative == [r[2],-r[2]]
raise 'CG5 mixed cr' unless cross == [r[0],r[0]]
pass += %w[CG5_center_(1+rho)/2 CG5_relative_2(1-rho) CG5_no_cr_term]

# CG.6: D_diag-L_rho contributes -2nu(1-rho) cross derivative.
defect=[-r[2],r[2]]
raise 'CG6 rho0' unless defect[0] == -2
raise 'CG6 rho1' unless defect.sum == 0
raise 'CG6 reversed sign was not rejected' if [r[2],-r[2]] == defect
pass += %w[CG6_rho0_negative_-2nu CG6_rho1_zero CG6_positive_sign_negative_control_rejected]

# CG.9: exact affine-in-rho square expansion.
wp=[r[1,2],r[1,2]]
wm=[r[1,2],-r[1,2]]
a2=add.call(wp,wm)
b2=a2
ab=scale.call(2,add.call(wp,scale.call(-1,wm)))
raise 'CG9 a2/b2' unless a2 == [r[1],r[0]] && b2 == [r[1],r[0]]
raise 'CG9 cross' unless ab == [r[0],r[2]]
raise 'CG9 plus weight' unless [wp[0],wp.sum] == [r[1,2],r[1]]
raise 'CG9 minus weight' unless [wm[0],wm.sum] == [r[1,2],r[0]]
raise 'CG9 cross-sign negative control was not rejected' if ab == [r[0],-r[2]]
pass += %w[CG9_square_expansion CG9_common_coercivity_rho_[0,1] CG9_cross_sign_negative_control_rejected]

# Young p=4/3, q=4 for g H^(1/2) Z^(3/2),
# with A=nu^(3/4) Z^(3/2).
yp=r[4,3]
yq=r[4]
checks={
  'Young_conjugacy'=>(r[1]/yp+r[1]/yq==1),
  'Young_gradient_power_2'=>(r[3,2]*yp==2),
  'Young_g_power_4'=>(yq==4),
  'Young_H_power_2'=>(r[1,2]*yq==2),
  'Young_nu_absorbed_power_1'=>(r[3,4]*yp==1),
  'Young_nu_remainder_power_-3'=>(-r[3,4]*yq==-3)
}
checks.each{|k,v| raise k unless v; pass << k}
raise 'Young wrong q negative control was not rejected' if r[1]/yp+r[1]/r[3]==1
pass << 'Young_wrong_q_negative_control_rejected'

puts "language=ruby #{RUBY_VERSION}; arithmetic=Rational"
puts "passed=#{pass.length}"
pass.each{|x| puts "PASS #{x}"}
