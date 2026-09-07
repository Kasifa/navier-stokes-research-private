#!/usr/bin/env ruby
# PRIVATE_CORE. Independent full-support exact driver algebra through order three.
# Independent scalar-polynomial differentiation and pressure projection.
# No execution/import of the frozen first-cycle implementation.
require 'json'
require 'digest'

ROOT = File.expand_path(__dir__)
ZERO = Complex(Rational(0), Rational(0))
I = Complex(Rational(0), Rational(1))
ZK = [0,0,0].freeze
def clean(s)
  s.reject { |_k,v| v == 0 }
end
def scalar_add(*terms)
  out = Hash.new(ZERO)
  terms.each { |factor,s| s.each { |k,v| out[k] += factor*v } }
  clean(out)
end
def product(f,g)
  out = Hash.new(ZERO)
  f.each do |p,fp|
    g.each { |q,gq| out[3.times.map { |j| p[j]+q[j] }] += fp*gq }
  end
  clean(out)
end
def derivative(f,j)
  clean(f.to_h { |k,v| [k,I*k[j]*v] })
end
def vf_add(*terms)
  3.times.map { |j| scalar_add(*terms.map { |factor,f| [factor,f[j]] }) }
end
def laplacian(f)
  f.map { |fj| clean(fj.to_h { |k,v| [k,-k.sum { |x| x*x }*v] }) }
end
def advective(f,g)
  3.times.map do |j|
    scalar_add(*3.times.map { |h| [1,product(f[h],derivative(g[j],h))] })
  end
end
def bilinear(f,g,project=true)
  raw=advective(f,g)
  return vf_add([-1,raw]) unless project
  div=scalar_add(*3.times.map { |j| [1,derivative(raw[j],j)] })
  pressure=clean(div.reject { |k,_| k==ZK }.to_h { |k,v| [k,v/k.sum { |x| x*x }] })
  3.times.map { |j| scalar_add([-1,raw[j]],[-1,derivative(pressure,j)]).reject { |k,_| k==ZK } }
end
def support(f)
  f.flat_map(&:keys).uniq.sort
end
def vector(f,k)
  f.map { |fj| fj.fetch(k,ZERO) }
end
def valid(f)
  support(f).all? do |k|
    v=vector(f,k)
    k!=ZK && 3.times.sum { |j| k[j]*v[j] }==0 && vector(f,k.map { |x| -x })==v.map(&:conj)
  end
end
def upper(f)
  f.sum { |fj| fj.values.sum { |z| z.real.abs+z.imag.abs } }
end
def squared_l2(f)
  f.sum { |fj| fj.values.sum { |z| z.real*z.real+z.imag*z.imag } }
end
def rat(x)
  x.denominator==1 ? x.numerator.to_s : "#{x.numerator}/#{x.denominator}"
end
def packed_vector(v)
  v.map { |z| {'re'=>rat(z.real),'im'=>rat(z.imag)} }
end
def packed_field(f)
  support(f).map { |k| {'k'=>k,'value'=>packed_vector(vector(f,k))} }
end
def stats(f)
  {'support_count'=>support(f).length,'component_real_imag_l1'=>rat(upper(f)),
   'normalized_L2_squared'=>rat(squared_l2(f)),'real_divfree_mean_zero'=>valid(f)}
end
def seed(mask)
  f=Array.new(3) { {} }
  [[[1,0,0],1],[[0,1,0],2],[[0,0,1],0]].each_with_index do |(k,j),h|
    next if mask & (1<<h)==0
    f[j][k]=Complex(1,0)
    f[j][k.map { |x| -x }]=Complex(1,0)
  end
  f
end
def jets(mask,project=true)
  a=seed(mask)
  b=vf_add([1,laplacian(a)],[1,bilinear(a,a,project)])
  c=vf_add([1,laplacian(b)],[1,bilinear(a,b,project)],[1,bilinear(b,a,project)])
  d=vf_add([1,laplacian(c)],[1,bilinear(a,c,project)],[1,bilinear(c,a,project)],[2,bilinear(b,b,project)])
  [a,b,c,d]
end
def mixed(all)
  4.times.map do |order|
    vf_add(*(0..7).map { |mask| [(-1)**(3-mask.digits(2).sum),all[mask][order]] })
  end
end

def ip(v,w)
  3.times.sum { |j| (v[j].conj*w[j]).real }
end
def sq(v)
  ip(v,v)
end
def decode(rows)
  3.times.map do |j|
    clean(rows.to_h do |row|
      z=row.fetch('value')[j]
      [row.fetch('k'),Complex(Rational(z.fetch('re')),Rational(z.fetch('im')))]
    end)
  end
end
def ordered_sources(f,g,k,scale=1)
  support(f).flat_map do |p|
    support(g).map do |q|
      next unless 3.times.map { |j| p[j]+q[j] }==k
      fp=3.times.map { |j| {p=>vector(f,p)[j]} }
      gq=3.times.map { |j| {q=>vector(g,q)[j]} }
      contribution=vector(vf_add([scale,bilinear(fp,gq)]),k)
      raw=vector(vf_add([scale,bilinear(fp,gq,false)]),k)
      {'p'=>p,'q'=>q,'projected'=>packed_vector(contribution),'unprojected'=>packed_vector(raw),
       'projected_nonzero'=>contribution.any? { |z| z!=0 }}
    end.compact
  end
end

started=Process.clock_gettime(Process::CLOCK_MONOTONIC)
a,b,c,d=jets(7)
n=bilinear(a,a)
cc=vf_add([1,bilinear(a,n)],[1,bilinear(n,a)])
g=bilinear(n,n)
sp=vf_add([Rational(1,2),bilinear(a,cc)])
sm=vf_add([Rational(1,2),bilinear(cc,a)])
combined=vf_add([1,g],[1,sp],[1,sm])
v=vf_add([Rational(1,3),combined])
q=[2,1,1]
expected_vectors={'g'=>[-2,2,2].map { |x| I*Rational(x,3) },
                  's_plus'=>[-2,-1,5].map { |x| I*Rational(x,6) },
                  's_minus'=>[1,-1,-1].map { |x| I*Rational(x,6) },
                  'd'=>[-5,2,8].map { |x| I*Rational(x,3) },
                  'v'=>[-5,2,8].map { |x| I*Rational(x,18) }}
fields={'a'=>a,'N'=>n,'C'=>cc,'b'=>b,'c'=>c,'d'=>d,'g'=>g,'s_plus'=>sp,'s_minus'=>sm,'v'=>v}
checks={}
expected_vectors.each { |name,expect| checks["q_#{name}_exact"]=vector(fields.fetch(name),q)==expect }
fields.each { |name,f| checks["full_#{name}_real_divfree_mean_zero"]=valid(f) }
checks['entire_B_N_a_zero']=support(bilinear(n,a)).empty?
checks['q_a_b_c_zero']=[a,b,c].all? { |f| vector(f,q).all?(&:zero?) }
checks['q_d_equals_two_combined']=vector(d,q)==vector(vf_add([2,combined]),q)
checks['q_v_equals_d_over_six']=vector(v,q)==vector(vf_add([Rational(1,6),d]),q)
g2=sq(vector(g,q));sp2=sq(vector(sp,q));sm2=sq(vector(sm,q))
net=vf_add([1,sp],[1,sm]);net2=sq(vector(net,q))
checks['q_g_norm_squared']=g2==Rational(4,3)
checks['q_s_plus_norm_squared']=sp2==Rational(5,6)
checks['q_s_minus_norm_squared']=sm2==Rational(1,12)
checks['q_net_seed_norm_squared']=net2==Rational(7,12)
checks['q_g_dominates_net_seed']=g2>net2
# For positive x,y,z, x<sqrt(y)+sqrt(z) follows from
# x^2-y-z<2sqrt(yz), checked below by rational squaring only.
excess=g2-sp2-sm2
checks['q_g_fails_sum_of_seed_channel_lengths']=excess>0 && excess**2<4*sp2*sm2
checks['q_v_inner_g']=ip(vector(v,q),vector(g,q))==Rational(5,9)
checks['q_v_inner_s_plus']=ip(vector(v,q),vector(sp,q))==Rational(4,9)
checks['q_v_inner_s_minus']=ip(vector(v,q),vector(sm,q))==Rational(-5,36)
checks['q_directional_driver_dominates_seed_net']=ip(vector(v,q),vector(g,q))>ip(vector(v,q),vector(net,q))
checks['q_directional_driver_fails_sum_absolute_seed']=ip(vector(v,q),vector(g,q))<ip(vector(v,q),vector(sp,q)).abs+ip(vector(v,q),vector(sm,q)).abs
old=JSON.parse(File.read(File.join(ROOT,'../first-cycle/algebra-result.json')))
{'seed'=>a,'N_Baa'=>n,'uprime0'=>b,'usecond0'=>c,'C'=>cc}.each do |name,f|
  checks["prior_python_full_#{name}"]=decode(old.fetch(name))==f
end
all=(0..7).map { |mask| jets(mask) }
mix=mixed(all)
previous_mix=JSON.parse(File.read(File.join(ROOT,'../next-mixed/mixed-result.json')))
checks['prior_python_all_mixed_coefficients']=(0..3).all? { |order| packed_field(mix[order])==previous_mix.fetch('mixed_jets')[order] }
checks['q_no_seed_group_can_be_deleted']=(0..6).all? { |mask| vector(all[mask][3],q).all?(&:zero?) }
sources={'g'=>ordered_sources(n,n,q),'s_plus'=>ordered_sources(a,cc,q,Rational(1,2)),
         's_minus'=>ordered_sources(cc,a,q,Rational(1,2))}
sources.each do |name,rows|
  sum=Array.new(3,ZERO)
  rows.each do |row|
    row.fetch('projected').each_with_index { |z,j| sum[j]+=Complex(Rational(z.fetch('re')),Rational(z.fetch('im'))) }
  end
  checks["ordered_source_sum_#{name}"]=sum==vector(fields.fetch(name),q)
end
a0,b0,c0,d0=jets(7,false)
n0=bilinear(a0,a0,false)
cubic0=vf_add([1,bilinear(a0,n0,false)],[1,bilinear(n0,a0,false)])
g0=bilinear(n0,n0,false)
sp0=vf_add([Rational(1,2),bilinear(a0,cubic0,false)])
sm0=vf_add([Rational(1,2),bilinear(cubic0,a0,false)])
checks['pressure_omission_changes_full_d']=d0!=d
checks['pressure_omission_changes_q_d']=vector(d0,q)!=vector(d,q)
checks['pressure_omission_changes_full_g']=g0!=g
checks['pressure_omission_breaks_divfree']=!valid(d0)
deleted=vf_add([1,d],[-2,g])
checks['deleting_B_N_N_changes_full_d']=deleted!=d
checks['deleting_B_N_N_changes_q_d']=vector(deleted,q)!=vector(d,q)
checks['deleting_B_N_N_q_equals_seed_channels']=vector(deleted,q)==vector(vf_add([2,net]),q)
# Recompute inherited full-PDE Taylor remainder hypotheses; no heat/seed split.
r2=vf_add([Rational(-1,2),laplacian(c)],[-1,bilinear(b,b)],
          [Rational(-1,2),bilinear(a,c)],[Rational(-1,2),bilinear(c,a)])
r3=vf_add([Rational(-1,2),bilinear(b,c)],[Rational(-1,2),bilinear(c,b)])
r4=vf_add([Rational(-1,4),bilinear(c,c)])
t0=Rational(1,10000)
t=Rational(1,1000000)
ma=2*(upper(r2)/3+upper(r3)*t0/4+upper(r4)*t0*t0/5)
first_certificate=JSON.parse(File.read(File.join(ROOT,'../first-cycle/certificate.json')))
checks['prior_M_exact_independently_recomputed']=ma==Rational(first_certificate.fetch('M_exact'))
checks['prior_contraction_condition']=256*upper(a)**2*t0<=1
checks['prior_U_ball_bound']=upper(a)+t0*upper(b)+t0*t0*upper(c)/2<=2*upper(a)
checks['prior_remainder_less_than_143']=ma<143
checks['N_l1_bound_12']=upper(n)<=12
qnorm_upper=Rational(5,2)
checks['q_norm_upper_5_over_2']=q.sum { |x| x*x }<qnorm_upper**2
checks['leading_s_plus_length_lt_one']=sp2<1
checks['leading_s_minus_length_lt_one']=sm2<1
checks['leading_g_length_lt_two']=g2<4
checks['leading_v_length_lt_one']=sq(vector(v,q))<1
f02=sq(vector(combined,q))
checks['leading_total_force_length_lt_two']=f02<4
checks['q_laplacian_eigenvalue_six']=q.sum { |x| x*x }==6
# Integral of (t-s)s^2 is t^4/12; 6*|F0|/12<=1.
checks['heat_kernel_target_integral_correction_le_one']=Rational(6*2,12)==1
pg0=Rational(5,9);psp0=Rational(4,9);psm0=Rational(-5,36);psnet0=psp0+psm0
# Independently chosen broad rational enclosures; primary tighter bounds are checked below.
g_lower=Rational(23,20);g_upper=Rational(7,6)
net_upper=Rational(77,100);sp_lower=Rational(9,10);sm_lower=Rational(2,7)
checks['sqrt_g_strict_rational_enclosure']=g_lower**2<g2 && g2<g_upper**2
checks['sqrt_net_strict_rational_upper']=net2<net_upper**2
checks['sqrt_sp_strict_rational_lower']=sp_lower**2<sp2
checks['sqrt_sm_strict_rational_lower']=sm_lower**2<sm2
checks['new_window_inside_prior_window']=0<t && t<=t0
seed_support=support(a)
ps=lambda { |f| f.map { |fj| fj.select { |k,_| seed_support.include?(k) } } }
poff=lambda { |f| f.map { |fj| fj.reject { |k,_| seed_support.include?(k) } } }
seed_sums=seed_support.product(seed_support).map { |p,r| 3.times.map { |j| p[j]+r[j] } }.uniq
seed_n_sums=seed_support.product(support(n)).map { |p,r| 3.times.map { |j| p[j]+r[j] } }.uniq
w2=vf_add([Rational(1,2),poff.call(c)])
checks['spectral_split_Ps_b_equals_minus_a']=ps.call(b)==vf_add([-1,a])
checks['spectral_split_Ps_c_equals_minus_a']=ps.call(c)==vf_add([-1,a])
checks['spectral_split_N_is_off_seed']=ps.call(n).all?(&:empty?)
checks['spectral_split_W2_A_bound_30']=upper(w2)==30
checks['spectral_split_q_outside_seed']=!seed_support.include?(q)
checks['spectral_split_q_outside_all_seed_pair_sums']=!seed_sums.include?(q)
checks['spectral_split_q_outside_all_seed_N_sums']=!seed_n_sums.include?(q)
checks['spectral_split_B_a_W2_q_equals_s_plus']=vector(bilinear(a,w2),q)==vector(sp,q)
checks['spectral_split_B_W2_a_q_equals_s_minus']=vector(bilinear(w2,a),q)==vector(sm,q)
checks['spectral_split_coefficient_1_minus_t_minus_half_t2_positive']=1-t0-t0*t0/2>0
checks['spectral_split_l_A_bound_6']=143*t0*t0<6
l_minus_a_majorant=6+3*t0+143*t0*t0
checks['spectral_split_l_minus_a_bound_7']=l_minus_a_majorant<7
wd_majorant=30+143*t0
checks['spectral_split_w_minus_tN_bound_31']=wd_majorant<31
eg_exact=qnorm_upper*(24*31+31**2*t0)
es_exact=qnorm_upper*(7*upper(w2)+6*143)
eg=1861;es=2670;ef=eg+2*es;mq=1802;ep=6000
checks['spectral_split_G_error_1861']=eg_exact<eg
checks['spectral_split_S_error_2670']=es_exact==es
checks['spectral_split_total_forcing_error_7201']=ef==7201
mq_exact=Rational(ef,4)+1
checks['spectral_split_mode_error_1802']=mq_exact<mq
pg_error=eg+2*mq+eg*mq*t
ps_error=es+mq+es*mq*t
checks['spectral_split_PG_error_6000']=pg_error<ep
checks['spectral_split_PS_error_6000']=ps_error<ep
checks['spectral_split_PG_positive']=pg0-ep*t>0
checks['spectral_split_PS_plus_positive']=psp0-ep*t>0
checks['spectral_split_PS_minus_negative']=psm0+ep*t<0
checks['spectral_split_PS_net_positive']=psnet0-2*ep*t>0
energy_net_margin=pg0-Rational(3,2)*psnet0-(ep+Rational(3,2)*2*ep)*t
energy_abs_margin=psp0-psm0-pg0-3*ep*t
checks['spectral_split_PG_gt_1p5_PSnet']=energy_net_margin>0
checks['spectral_split_PG_lt_abs_PSplus_plus_abs_PSminus']=energy_abs_margin>0
vector_net_margin=g_lower-eg*t-Rational(7,5)*(net_upper+2*es*t)
vector_abs_margin=sp_lower+sm_lower-g_upper-(2*es+eg)*t
checks['spectral_split_G_norm_gt_7_over_5_seed_net_norm']=vector_net_margin>0
checks['spectral_split_G_norm_lt_sum_seed_norms']=vector_abs_margin>0
time_contract={
  'decomposition'=>'S is the six initial wavevectors, l=P_S u, w=(I-P_S)u; both are projections of the same full solution.',
  'T0'=>rat(t0),'T'=>rat(t),'N_A_upper'=>rat(upper(n)),'W2_A_upper'=>rat(upper(w2)),
  'seed_projection_jets'=>{'b'=>'-a','c'=>'-a'},
  'l_A_upper'=>'6','l_minus_a_linear_bound_majorant'=>rat(l_minus_a_majorant),'l_minus_a_linear_bound'=>'7',
  'w_minus_tN_quadratic_bound_majorant'=>rat(wd_majorant),'w_minus_tN_quadratic_bound'=>'31',
  'off_seed_cubic_remainder_upper'=>'143','G_error_exact_majorant'=>rat(eg_exact),'G_error_upper'=>eg.to_s,
  'S_error_exact_majorant'=>rat(es_exact),'S_error_upper'=>es.to_s,
  'total_force_error_upper'=>ef.to_s,'mode_fourth_order_error_majorant'=>rat(mq_exact),'mode_fourth_order_error_upper'=>mq.to_s,
  'energy_G_error_majorant'=>rat(pg_error),'energy_S_error_majorant'=>rat(ps_error),'energy_common_error_upper'=>ep.to_s,
  'strict_positive_margins'=>{'energy_G_over_1p5_seed_net'=>rat(energy_net_margin),
    'energy_absolute_seed_sum_over_G'=>rat(energy_abs_margin),
    'vector_G_over_1p4_seed_net'=>rat(vector_net_margin),
    'vector_seed_norm_sum_over_G'=>rat(vector_abs_margin)},
  'sqrt_rational_enclosures'=>{'g_lower'=>rat(g_lower),'g_upper'=>rat(g_upper),'seed_net_upper'=>rat(net_upper),'s_plus_lower'=>rat(sp_lower),'s_minus_lower'=>rat(sm_lower)},
  'structural_zero'=>'q is absent from S+S and S+support(N), so B(l,l)_q=B(l,N)_q=B(N,l)_q=0 regardless of current seed amplitudes or phases.',
  'scope'=>'Exact inequalities certify constants in the accompanying full-PDE analytic argument. No closed spectral evolution, equal-amplitude assumption, or omitted off-seed tail is used.'
}
actual_sp=bilinear(a,w2)
actual_sm=bilinear(w2,a)
primary_fields={'a'=>a,'N'=>n,'C'=>cc,'b'=>b,'c'=>c,'W2'=>w2,'g'=>g,'s_plus'=>actual_sp,'s_minus'=>actual_sm}
primary_path=File.join(ROOT,'driver-certificate.json')
primary=JSON.parse(File.read(primary_path))
primary_fields.each do |name,f|
  checks["primary_all_coefficients_#{name}"]=decode(primary.fetch('fields').fetch(name))==f
  checks["actual_full_#{name}_real_divfree_mean_zero"]=valid(f)
end
primary_vectors={'g'=>vector(g,q),'s_plus'=>vector(actual_sp,q),'s_minus'=>vector(actual_sm,q),
                 's_net'=>vector(net,q),'F0'=>vector(combined,q),'v'=>vector(v,q)}
primary_vectors.each do |name,vec|
  checks["primary_target_vector_#{name}"]=primary.fetch('target_vectors').fetch(name)==packed_vector(vec)
  checks["primary_target_squared_norm_#{name}"]=Rational(primary.fetch('target_squared_norms').fetch(name))==sq(vec)
end
{'T0'=>t0,'T'=>t,'EG'=>eg,'ES'=>es,'MQ'=>mq,'EP'=>ep}.each do |name,value|
  checks["primary_constant_#{name}"]=Rational(primary.fetch(name))==value
end
primary_estimates={
  'newborn_first_difference_coefficient'=>wd_majorant,
  'seed_difference_coefficient'=>l_minus_a_majorant,
  'G_error_before_rounding'=>eg_exact,'S_error_before_rounding'=>es_exact,
  'mode_error_before_rounding'=>mq_exact,
  'power_G_error_before_rounding'=>pg_error,'power_S_error_before_rounding'=>ps_error
}
primary_estimates.each do |name,value|
  checks["primary_estimate_#{name}"]=Rational(primary.fetch('rational_estimates').fetch(name))==value
end
primary_powers={'g'=>pg0,'s_plus'=>psp0,'s_minus'=>psm0,'s_net'=>psnet0}
primary_powers.each do |name,value|
  checks["primary_power_#{name}"]=Rational(primary.fetch('leading_powers').fetch(name))==value
end
primary_brackets=primary.fetch('sqrt_brackets').transform_values { |bounds| bounds.map { |bound| Rational(bound) } }
primary_brackets.each do |name,(lo,hi)|
  checks["primary_sqrt_bracket_#{name}_independently_squared"]=0<lo && lo**2<sq(primary_vectors.fetch(name)) && sq(primary_vectors.fetch(name))<hi**2
end
plo=lambda { |name| primary_brackets.fetch(name)[0] }
phi=lambda { |name| primary_brackets.fetch(name)[1] }
primary_gaps={
  'vector_net_margin'=>plo.call('g')-Rational(7,5)*phi.call('s_net')-(eg+Rational(7,5)*2*es)*t,
  'vector_absolute_failure_margin'=>plo.call('s_plus')+plo.call('s_minus')-phi.call('g')-(eg+2*es)*t,
  'power_seed_net_positive'=>psnet0-2*ep*t,
  'power_net_dominance_margin'=>energy_net_margin,
  'power_absolute_failure_margin'=>energy_abs_margin,
  'power_g_positive'=>pg0-ep*t,
  'power_s_plus_positive'=>psp0-ep*t,
  'power_s_minus_negative_margin'=>-psm0-ep*t,
  'mode_energy_growth_margin'=>pg0+psp0+psm0-(3*ep+24)*t
}
primary_gaps.each do |name,value|
  checks["primary_gap_#{name}_independently_recomputed"]=Rational(primary.fetch('strict_gaps').fetch(name))==value && value>0
end
checks['actual_off_seed_norm_at_most_13t']=12+31*t0<=13
checks['actual_seed_norm_at_least_5']=6-7*t>=5
checks['actual_q_mode_norm_at_most_2t_cubed']=1+mq*t<=2
checks['actual_viscous_modal_energy_loss_at_most_24t6']=6*2**2==24
raw_actual_w2=vf_add([Rational(1,2),poff.call(c0)])
raw_actual_sp=bilinear(a0,raw_actual_w2,false)
raw_actual_sm=bilinear(raw_actual_w2,a0,false)
mutation_checks={
  'delete_newborn_self_interaction'=>vector(g,q).any? { |z| z!=0 },
  'delete_full_Leray'=>vector(g0,q)!=vector(g,q) || vector(raw_actual_sp,q)!=vector(actual_sp,q) || vector(raw_actual_sm,q)!=vector(actual_sm,q),
  'flip_seed_feedback_phase'=>ip(vector(v,q),vector(vf_add([-1,actual_sm]),q))>0 && psm0<0,
  'infer_absolute_dominance_from_net'=>plo.call('s_plus')+plo.call('s_minus')>phi.call('g'),
  'discard_s_minus'=>vector(net,q)!=vector(actual_sp,q),
  'inflate_window_invalidates_absolute_power_gap'=>Rational(1,36)-3*ep*t0<0
}
mutation_checks.each do |name,value|
  checks["primary_mutation_#{name}_independently_detected"]=value && primary.fetch('negative_mutations_detected').fetch(name)==value
end
fields.merge!({'C_tree_s_plus'=>sp,'C_tree_s_minus'=>sm,'W2'=>w2,'s_plus'=>actual_sp,'s_minus'=>actual_sm})
sources={'g'=>ordered_sources(n,n,q),'s_plus'=>ordered_sources(a,w2,q),'s_minus'=>ordered_sources(w2,a,q)}
report={
  'schema'=>'ReverseNS-driver-independent-ruby-v1','classification'=>'PRIVATE_CORE',
  'method'=>'Exact scalar Fourier polynomial products and physical derivatives, then solve periodic pressure; no primary imports, no cutoff.',
  'equation'=>"u'=Delta u-P((u dot grad)u), viscosity 1, unforced, fixed (R/(2*pi*Z))^3",
  'seed'=>'2*(cos(x3),cos(x1),cos(x2))','q'=>q,
  'definitions'=>{'N'=>'B(a,a)','C'=>'B(a,N)+B(N,a)','W2'=>'(I-P_S)c/2','g'=>'B(N,N)','s_plus'=>'B(a,W2)','s_minus'=>'B(W2,a)','C_tree_s_plus'=>'B(a,C)/2; equals s_plus only at q, not as a full field','C_tree_s_minus'=>'B(C,a)/2; equals s_minus only at q, not as a full field','v'=>'(g+C_tree_s_plus+C_tree_s_minus)/3; at q equals (g+s_plus+s_minus)/3=d_q/6'},
  'fields'=>fields.transform_values { |f| {'stats'=>stats(f),'coefficients'=>packed_field(f)} },
  'q_vectors'=>fields.transform_values { |f| packed_vector(vector(f,q)) },
  'q_squared_norms'=>{'g'=>rat(g2),'s_plus'=>rat(sp2),'s_minus'=>rat(sm2),'seed_net'=>rat(net2),'v'=>rat(sq(vector(v,q)))},
  'q_directional_pairings_with_v'=>{'g'=>rat(ip(vector(v,q),vector(g,q))),'s_plus'=>rat(ip(vector(v,q),vector(sp,q))),'s_minus'=>rat(ip(vector(v,q),vector(sm,q))),'seed_net'=>rat(ip(vector(v,q),vector(net,q)))},
  'ordered_sources_at_q'=>sources,
  'pressure_omission_negative_control'=>{'full_d'=>packed_field(d0),'q_d'=>packed_vector(vector(d0,q)),'q_g'=>packed_vector(vector(g0,q)),'q_s_plus'=>packed_vector(vector(raw_actual_sp,q)),'q_s_minus'=>packed_vector(vector(raw_actual_sm,q))},
  'B_N_N_deletion_negative_control'=>{'q_d'=>packed_vector(vector(deleted,q)),'full_d'=>packed_field(deleted)},
  'time_contract'=>time_contract,
  'revision_note'=>'An earlier auxiliary heat-seed decomposition was superseded by the actual current-support split. It is not part of this certificate or theorem.',
  'actual_spectral_split_algebra'=>{'seed_support'=>seed_support,'seed_pair_sums'=>seed_sums.sort,'seed_N_sums'=>seed_n_sums.sort,'W2'=>packed_field(w2)},
  'primary_comparison'=>{'path'=>'driver-certificate.json','sha256'=>Digest::SHA256.file(primary_path).hexdigest,
    'all_fields_compared'=>primary_fields.keys,'sqrt_brackets_independently_squared'=>primary.fetch('sqrt_brackets'),
    'strict_gaps_independently_recomputed'=>primary_gaps.transform_values { |value| rat(value) },
    'mutations_independently_recomputed'=>mutation_checks,
    'note'=>'Primary tighter square-root brackets are independently verified. Their margins need not equal the separately chosen broader independent bounds.'},
  'inherited_remainder_recomputation'=>{'M_exact'=>rat(ma),'A_remainder_bound'=>'143','residual_l1'=>{'r2'=>rat(upper(r2)),'r3'=>rat(upper(r3)),'r4'=>rat(upper(r4))}},
  'prior_inputs'=>['../first-cycle/algebra-result.json','../first-cycle/certificate.json','../first-cycle/PROOF.md','../next-mixed/mixed-result.json'].map { |path| {'path'=>path,'sha256'=>Digest::SHA256.file(File.join(ROOT,path)).hexdigest} },
  'checks'=>checks,'status'=>checks.values.all? ? 'PASS' : 'FAIL',
  'limits'=>['Bounded exact algebra and rational inequalities for the accompanying positive-time analytic contract only.','Norm dominance over net seed forcing does not imply dominance over the sum of absolute ordered channel lengths.','The infinite-dimensional remainder proof remains a mathematical input beyond finite coefficient checks.','No autonomous regeneration, iteration, infinite scale, or singularity conclusion.'],
  'environment'=>{'ruby'=>RUBY_VERSION,'platform'=>RUBY_PLATFORM,'workers'=>1,'arithmetic'=>'exact Rational/Complex','randomness'=>'none','spectral_truncation'=>false}
}
out=File.join(ROOT,'driver-independent.json')
payload=JSON.pretty_generate(report)+"\n"
if ARGV.include?('--check')
  raise 'driver-independent.json differs from exact recomputation' unless File.read(out)==payload
else
  File.write(out,payload)
end
puts JSON.generate({'status'=>report['status'],'checks'=>checks.size,'failed'=>checks.select { |_,ok| !ok }.keys,'q_vectors'=>report['q_vectors'].slice('g','s_plus','s_minus','d','v'),'q_squared_norms'=>report['q_squared_norms'],'seconds'=>Process.clock_gettime(Process::CLOCK_MONOTONIC)-started,'sha256'=>Digest::SHA256.file(out).hexdigest})
exit(checks.values.all? ? 0 : 1)
