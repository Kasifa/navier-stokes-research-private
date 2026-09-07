#!/usr/bin/env ruby
# Independent implementation: scalar polynomial products/differentiation,
# then one pressure/Leray solve per output. No imports from primary code.
require 'json'
require 'digest'
require 'rbconfig'

ROOT = File.expand_path(__dir__)
ZERO = Complex(Rational(0), Rational(0))
I = Complex(Rational(0), Rational(1))
ZK = [0, 0, 0].freeze
def clean(s)
  s.reject { |_k, v| v == 0 }
end
def scalar_add(*terms)
  out = Hash.new(ZERO)
  terms.each { |factor, s| s.each { |k, v| out[k] += factor * v } }
  clean(out)
end
def product(f, g)
  out = Hash.new(ZERO)
  f.each do |p, fp|
    g.each do |q, gq|
      out[3.times.map { |j| p[j] + q[j] }] += fp * gq
    end
  end
  clean(out)
end
def derivative(f, j)
  clean(f.to_h { |k, v| [k, I * k[j] * v] })
end
def vf_add(*terms)
  3.times.map { |j| scalar_add(*terms.map { |factor, f| [factor, f[j]] }) }
end
def laplacian(f)
  f.map { |fj| clean(fj.to_h { |k, v| [k, -k.sum { |x| x*x } * v] }) }
end
def advective(f, g)
  3.times.map do |j|
    scalar_add(*3.times.map { |h| [1, product(f[h], derivative(g[j], h))] })
  end
end
def B(f, g)
  raw = advective(f, g)
  divergence = scalar_add(*3.times.map { |j| [1, derivative(raw[j], j)] })
  pressure = clean(divergence.reject { |k, _| k == ZK }.to_h do |k, v|
    [k, v / k.sum { |x| x*x }]
  end)
  3.times.map do |j|
    scalar_add([-1, raw[j]], [-1, derivative(pressure, j)]).reject { |k, _| k == ZK }
  end
end
def B_without_pressure(f,g)
  vf_add([-1,advective(f,g)])
end
def support(f)
  f.flat_map(&:keys).uniq.sort
end
def vector(f, k)
  f.map { |fj| fj.fetch(k, ZERO) }
end
def upper(f)
  f.sum { |fj| fj.values.sum { |z| z.real.abs + z.imag.abs } }
end
def valid(f)
  support(f).all? do |k|
    v = vector(f, k)
    k != ZK && 3.times.sum { |j| k[j] * v[j] } == 0 &&
      vector(f, k.map { |x| -x }) == v.map(&:conj)
  end
end
def decode(rows)
  3.times.map do |j|
    clean(rows.to_h do |row|
      v = row.fetch('value')[j]
      [row.fetch('k'), Complex(Rational(v.fetch('re')), Rational(v.fetch('im')))]
    end)
  end
end
def rational_json(x)
  x.denominator == 1 ? x.numerator.to_s : "#{x.numerator}/#{x.denominator}"
end
def vector_json(v)
  v.map { |z| {'re' => rational_json(z.real), 'im' => rational_json(z.imag)} }
end

started = Process.clock_gettime(Process::CLOCK_MONOTONIC)
a = Array.new(3) { {} }
[[[1,0,0],1], [[0,1,0],2], [[0,0,1],0]].each do |k, j|
  a[j][k] = Complex(Rational(1), Rational(0))
  a[j][k.map { |x| -x }] = Complex(Rational(1), Rational(0))
end
n = B(a,a)
b = vf_add([1,laplacian(a)],[1,n])
c = vf_add([1,laplacian(b)],[1,B(a,b)],[1,B(b,a)])
cc = vf_add([1,B(a,n)],[1,B(n,a)])
r2 = vf_add([Rational(-1,2),laplacian(c)],[-1,B(b,b)],
            [Rational(-1,2),B(a,c)],[Rational(-1,2),B(c,a)])
r3 = vf_add([Rational(-1,2),B(b,c)],[Rational(-1,2),B(c,b)])
r4 = vf_add([Rational(-1,4),B(c,c)])
primary_path = File.join(ROOT,'algebra-result.json')
primary = JSON.parse(File.read(primary_path))
fields = {'seed'=>a,'N_Baa'=>n,'uprime0'=>b,'usecond0'=>c,'C'=>cc}
checks = fields.to_h { |name,f| ["all_coefficients_#{name}", decode(primary.fetch(name)) == f] }
checks.merge!(fields.to_h { |name,f| ["real_divfree_mean_zero_#{name}", valid(f)] })
{'t2'=>r2,'t3'=>r3,'t4'=>r4}.each do |name,f|
  checks["all_coefficients_residual_#{name}"] = decode(primary.fetch('residual_coefficients').fetch(name)) == f
  checks["real_divfree_mean_zero_residual_#{name}"] = valid(f)
end
j, k = [1,1,0], [2,1,0]
s = support(a)
pair_sums = s.product(s).map { |p,q| 3.times.map { |h| p[h]+q[h] } }.uniq
checks['targets_initially_empty'] = !s.include?(j) && !s.include?(k)
checks['k_absent_from_all_signed_seed_pair_sums'] = !pair_sums.include?(k)
checks['j_N_equals_minus_i_e3'] = vector(n,j) == [ZERO,ZERO,-I]
checks['j_c_equals_4_i_e3'] = vector(c,j) == [ZERO,ZERO,4*I]
checks['k_c_equals_minus_e3'] = vector(c,k) == [ZERO,ZERO,Complex(-1,0)]
checks['k_B_N_a_zero'] = vector(B(n,a),k).all?(&:zero?)
checks['B_N_a_entire_field_zero'] = B(n,a).all?(&:empty?)
checks['B_N_a_full_primary_matches'] = decode(primary.fetch('B_N_a_full')) == B(n,a)
checks['k_B_a_N_minus_e3'] = vector(B(a,n),k) == [ZERO,ZERO,Complex(-1,0)]
checks['jet_residual_constant_zero'] = vf_add([1,b],[-1,laplacian(a)],[-1,B(a,a)]).all?(&:empty?)
checks['jet_residual_linear_zero'] = vf_add([1,c],[-1,laplacian(b)],[-1,B(a,b)],[-1,B(b,a)]).all?(&:empty?)
# Independent scalar-polynomial recomputation of the full residual powers.
u_poly = [a,b,vf_add([Rational(1,2),c])]
conv = (0..4).map do |degree|
  terms = (0..2).map do |p|
    q = degree-p
    [1,B(u_poly[p],u_poly[q])] if (0..2).include?(q)
  end.compact
  vf_add(*terms)
end
checks['residual_degree2'] = r2 == vf_add([-1,laplacian(u_poly[2])],[-1,conv[2]])
checks['residual_degree3'] = r3 == vf_add([-1,conv[3]])
checks['residual_degree4'] = r4 == vf_add([-1,conv[4]])
n_without = B_without_pressure(a,a)
c_without = vf_add([1,B_without_pressure(a,n_without)],[1,B_without_pressure(n_without,a)])
pk = [1,1,-1]
checks['pressure_negative_control_full_zero'] = vector(cc,pk).all?(&:zero?)
checks['pressure_negative_control_omission_nonzero'] = vector(c_without,pk) == [2,2,-2]
checks['target_only_cannot_detect_pressure_omission'] = vector(c_without,k) == vector(cc,k)
qtriple = [[2,1,0],[0,2,1],[1,0,2]]
gram = qtriple.map { |p| qtriple.map { |q| 3.times.sum { |h| p[h]*q[h] } } }
checks['three_mode_gram_not_scaled_identity'] = gram == [[5,2,2],[2,5,2],[2,2,5]]
checks['three_mode_gram_matches_primary'] = gram == primary.fetch('specific_three_mode_similarity_obstruction').fetch('frequency_gram')
a_red = a.map(&:dup)
a_red[0] = {}
n_red = B(a_red,a_red)
b_red = vf_add([1,laplacian(a_red)],[1,n_red])
c_red = vf_add([1,laplacian(b_red)],[1,B(a_red,b_red)],[1,B(b_red,a_red)])
checks['reduced_seed_allowed'] = valid(a_red)
checks['reduced_seed_has_no_e3_wavevector'] = support(a_red).all? { |p| p[2] == 0 }
checks['reduced_seed_j_jet_identical'] = vector(a_red,j) == vector(a,j) && vector(b_red,j) == vector(b,j) && vector(c_red,j) == vector(c,j)
checks['reduced_seed_k_jet_identical'] = vector(a_red,k) == vector(a,k) && vector(b_red,k) == vector(b,k) && vector(c_red,k) == vector(c,k)
checks['reduced_seed_no_pressure_in_second_jet'] = c_red == vf_add([1,laplacian(b_red)],[1,B_without_pressure(a_red,b_red)],[1,B_without_pressure(b_red,a_red)])
red_primary = primary.fetch('globally_smooth_reduced_seed_negative_control')
checks['reduced_primary_seed_matches'] = decode(red_primary.fetch('seed')) == a_red
{'j_N'=>vector(n_red,j),'j_c'=>vector(c_red,j),'k_C'=>vector(vf_add([1,B(a_red,n_red)],[1,B(n_red,a_red)]),k),'k_c'=>vector(c_red,k)}.each do |label,v|
  checks["reduced_primary_#{label}_matches"] = vector_json(v) == red_primary.fetch(label)
end
t = Rational(1,10000)
mm = 2*(upper(r2)/3+upper(r3)*t/4+upper(r4)*t*t/5)
checks['time_contraction_squared'] = 256*upper(a)**2*t <= 1
checks['time_approximation_ball'] = upper(a)+t*upper(b)+t*t*upper(c)/2 <= 2*upper(a)
checks['remainder_constant_less_than_143'] = mm < 143
checks['j_uniform_lower_bound'] = 1-2*t-143*t*t >= Rational(1,2)
checks['k_uniform_lower_bound'] = Rational(1,2)-143*t >= Rational(1,4)
certificate_path = File.join(ROOT,'certificate.json')
certificate = JSON.parse(File.read(certificate_path))
checks['certificate_T_matches'] = Rational(certificate.fetch('time')) == t
checks['certificate_exact_M_matches'] = Rational(certificate.fetch('M_exact')) == mm
checks['certificate_algebra_hash_matches'] = certificate.fetch('algebra_sha256') == Digest::SHA256.file(primary_path).hexdigest
checks['certificate_residual_bounds_match'] = certificate.fetch('residual_upper') == {'D2'=>upper(r2),'D3'=>upper(r3),'D4'=>upper(r4)}.transform_values { |x| rational_json(x) }
report = {
  'schema'=>'ReverseNS-independent-ruby-crosscheck-v1',
  'classification'=>'PRIVATE_CORE',
  'method'=>'Ruby exact Rational/Complex; scalar physical derivatives and polynomial products; pressure recovery once per output; no primary imports or cutoff.',
  'primary_sha256'=>Digest::SHA256.file(primary_path).hexdigest,
  'certificate_sha256'=>Digest::SHA256.file(certificate_path).hexdigest,
  'checks'=>checks,
  'coefficient_l1_upper_bounds'=>{'A'=>upper(a),'b'=>upper(b),'c'=>upper(c),'D2'=>upper(r2),'D3'=>upper(r3),'D4'=>upper(r4)}.transform_values { |x| rational_json(x) },
  'support_counts'=>{'a'=>a,'N'=>n,'b'=>b,'c'=>c,'r2'=>r2,'r3'=>r3,'r4'=>r4}.transform_values { |f| support(f).size },
  'target_j'=>{'N'=>vector_json(vector(n,j)), 'c'=>vector_json(vector(c,j))},
  'target_k'=>{'N'=>vector_json(vector(n,k)), 'c'=>vector_json(vector(c,k))},
  'reduced_seed_control'=>{'physical'=>'(0,2*cos(x1),2*cos(x2))','j_b'=>vector_json(vector(b_red,j)),'j_c'=>vector_json(vector(c_red,j)),'k_b'=>vector_json(vector(b_red,k)),'k_c'=>vector_json(vector(c_red,k)),'scope'=>'The same selected first and second jets occur in a globally smooth triangular 2D3C solution; the main seed itself is not in that class.'},
  'time_contract'=>{'T'=>rational_json(t),'M_exact'=>rational_json(mm),'certified_upper'=>'143'},
  'environment'=>{'ruby'=>RUBY_VERSION,'platform'=>RUBY_PLATFORM,'workers'=>1,'arithmetic'=>'exact rational complex','randomness'=>'none','spectral_cutoff'=>'none'},
  'status'=>checks.values.all? ? 'PASS' : 'FAIL'
}
output_path = File.join(ROOT,'independent-crosscheck.json')
payload = JSON.pretty_generate(report)+"\n"
if ARGV.include?('--check')
  raise 'Independent report differs from exact recomputation' unless File.read(output_path) == payload
else
  File.write(output_path,payload)
end
elapsed = Process.clock_gettime(Process::CLOCK_MONOTONIC)-started
if ARGV.include?('--run-log')
  File.write(File.join(ROOT,'independent-crosscheck-run.json'),JSON.pretty_generate({'command'=>'ruby research/reverse/first-cycle/independent_crosscheck.rb '+ARGV.join(' '),'elapsed_seconds'=>elapsed,'environment'=>report['environment'],'status'=>report['status'],'checks'=>checks.size,'report_sha256'=>Digest::SHA256.file(output_path).hexdigest})+"\n")
end
puts JSON.generate({'status'=>report['status'],'checks'=>checks.size,'bounds'=>report['coefficient_l1_upper_bounds'],'failed'=>checks.select { |_,v| !v }.keys})
exit(checks.values.all? ? 0 : 1)
