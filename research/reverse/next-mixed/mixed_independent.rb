#!/usr/bin/env ruby
# PRIVATE_CORE. Bounded exact jets through order three; no time evolution.
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

started=Process.clock_gettime(Process::CLOCK_MONOTONIC)
all=(0..7).map { |mask| jets(mask) }
mix=mixed(all)
all_no_pressure=(0..7).map { |mask| jets(mask,false) }
mix_no_pressure=mixed(all_no_pressure)
nonzero_orders=(0..3).reject { |order| support(mix[order]).empty? }
chosen=support(mix[3]).find { |k| k.all? { |x| x!=0 } } || support(mix[3]).first
primary_path=File.join(ROOT,'mixed-result.json')
primary=JSON.parse(File.read(primary_path))
a=all[7][0]
n=bilinear(a,a)
cc=vf_add([1,bilinear(a,n)],[1,bilinear(n,a)])
channels={'2B_N_N'=>vf_add([2,bilinear(n,n)]),'B_a_C'=>bilinear(a,cc),'B_C_a'=>bilinear(cc,a)}
q=[2,1,1]
expected={'2B_N_N'=>[-4,4,4],'B_a_C'=>[-2,-1,5],'B_C_a'=>[1,-1,-1]}
channel_sum=vf_add(*channels.values.map { |f| [1,f] })
norm_histogram=Hash.new(0)
frequency_histogram=Hash.new(0)
support(mix[3]).each do |k|
  norm_histogram[rat(vector(mix[3],k).sum { |z| z.real*z.real+z.imag*z.imag })]+=1
  frequency_histogram[k.sum { |x| x*x }.to_s]+=1
end
checks={
  'eight_seed_subsets'=>all.length==8,
  'every_full_jet_real_divfree_mean_zero'=>all.flatten(1).all? { |f| valid(f) },
  'mixed_zero_through_order_two'=>(0..2).all? { |order| support(mix[order]).empty? },
  'mixed_order_three_nonzero'=>!support(mix[3]).empty?,
  'mixed_order_three_real_divfree_mean_zero'=>valid(mix[3]),
  'pressure_omission_creates_order_two_mixed_term'=>support(mix[2]).empty? && !support(mix_no_pressure[2]).empty?,
  'pressure_omission_changes_order_three'=>mix[3]!=mix_no_pressure[3],
  'all_mixed_coefficients_match_python'=>(0..3).all? { |order| packed_field(mix[order])==primary.fetch('mixed_jets')[order] },
  'all_subset_support_counts_match_python'=>(0..7).all? { |mask| all[mask].map { |f| support(f).length }==primary.fetch('masks')[mask].fetch('support_sizes') },
  'q_channel_sum_equals_mixed_third'=>vector(channel_sum,q)==vector(mix[3],q),
  'q_channel_sum_equals_full_third'=>vector(channel_sum,q)==vector(all[7][3],q),
  'q_combined_value'=>vector(channel_sum,q)==[-5,2,8].map { |x| I*Rational(x,3) },
  'q_primary_channels_match'=>channels.transform_values { |f| packed_vector(vector(f,q)) }==primary.fetch('q_quartic_channels'),
  'original_j_mixed_third_equals_2_i_e3'=>vector(mix[3],[1,1,0])==[ZERO,ZERO,2*I],
  'wiener_norm_histogram'=>norm_histogram=={'31/3'=>24,'4'=>12},
}
channels.each { |label,f| checks["q_#{label}_value"]=vector(f,q)==expected.fetch(label).map { |x| I*Rational(x,3) } }
report={
  'schema'=>'ReverseNS-mixed-third-jet-independent-ruby-v1',
  'classification'=>'PRIVATE_CORE',
  'equation'=>"u'=Delta u-P((u dot grad)u), fixed viscosity 1, unforced, (R/(2*pi*Z))^3",
  'seed_physical'=>'2*(cos(x3),cos(x1),cos(x2))',
  'groups'=>[{'bit'=>0,'wavevectors'=>[[1,0,0],[-1,0,0]],'polarization'=>[0,1,0]},
             {'bit'=>1,'wavevectors'=>[[0,1,0],[0,-1,0]],'polarization'=>[0,0,1]},
             {'bit'=>2,'wavevectors'=>[[0,0,1],[0,0,-1]],'polarization'=>[1,0,0]}],
  'jet_convention'=>'[a,b,c,d]=[u(0),u_prime(0),u_second(0),u_third(0)], not factorial-normalized Taylor coefficients',
  'inclusion_exclusion'=>'sum over mask in 0..7 of (-1)^(3-popcount(mask))*jet(mask)',
  'interpretation'=>'Finite difference under group deletion: retains polynomial monomials containing each seed group at least once; repeated groups are allowed. Not a chronological supply theorem.',
  'subset_jets'=>(0..7).map { |mask| {'mask'=>mask,'orders'=>all[mask].each_with_index.map { |f,n| {'order'=>n,'stats'=>stats(f),'coefficients'=>packed_field(f)} }} },
  'mixed_jets'=>mix.each_with_index.map { |f,n| {'order'=>n,'stats'=>stats(f),'coefficients'=>packed_field(f)} },
  'first_nonzero_order'=>nonzero_orders.first,
  'python_primary_sha256'=>Digest::SHA256.file(primary_path).hexdigest,
  'preflight_review'=>{'path'=>'PREFLIGHT.md','sha256'=>Digest::SHA256.file(File.join(ROOT,'PREFLIGHT.md')).hexdigest,'status'=>'PASS','scope'=>'Checked exact q channel sum, j third mixed derivative and finite-diagnostic/non-PDE claim boundary. No new positive-time theorem.'},
  'third_order_exact_norms'=>{'normalized_L2_squared'=>rat(squared_l2(mix[3])),'Euclidean_Wiener_A'=>'24+8*sqrt(93)','squared_vector_norm_histogram'=>norm_histogram.sort.to_h,'frequency_squared_histogram'=>frequency_histogram.sort.to_h,'component_real_imag_l1'=>'144'},
  'selected_nonzero_mode'=>chosen ? {'k'=>chosen,'third_derivative'=>packed_vector(vector(mix[3],chosen))} : nil,
  'quartic_channels_at_q'=>{'q'=>q,'channels'=>channels.transform_values { |f| packed_vector(vector(f,q)) },'sum'=>packed_vector(vector(channel_sum,q)),'scope'=>'Third time derivative only. Newly-generated/newly-generated interaction is nonzero, while both other quartic trees are also nonzero at the same order. No temporal dominance or regeneration follows.'},
  'pressure_omission_control'=>{'mixed_jets'=>mix_no_pressure.each_with_index.map { |f,n| {'order'=>n,'stats'=>stats(f),'coefficients'=>packed_field(f)} },'meaning'=>'This deliberately wrong unprojected model is a negative control, not Navier-Stokes.'},
  'checks'=>checks,'status'=>checks.values.all? ? 'PASS' : 'FAIL',
  'limits'=>['Only exact jets through order 3.','No fourth-order derivative computed.','No new positive-time PDE remainder certificate.','No autonomous regeneration, uniform iteration, infinite-scale or singularity theorem.'],
  'environment'=>{'ruby'=>RUBY_VERSION,'platform'=>RUBY_PLATFORM,'workers'=>1,'arithmetic'=>'exact Rational/Complex','randomness'=>'none','spectral_truncation'=>false}
}
path=File.join(ROOT,'mixed-independent.json')
payload=JSON.pretty_generate(report)+"\n"
if ARGV.include?('--check')
  raise 'mixed-independent.json differs from exact recomputation' unless File.read(path)==payload
else
  File.write(path,payload)
end
puts JSON.generate({'status'=>report['status'],'checks'=>checks.size,'first_nonzero_order'=>report['first_nonzero_order'],'mixed_stats'=>report['mixed_jets'].map { |j| {'order'=>j['order'],'stats'=>j['stats']} },'selected_nonzero_mode'=>report['selected_nonzero_mode'],'seconds'=>Process.clock_gettime(Process::CLOCK_MONOTONIC)-started,'sha256'=>Digest::SHA256.file(path).hexdigest})
exit(checks.values.all? ? 0 : 1)
