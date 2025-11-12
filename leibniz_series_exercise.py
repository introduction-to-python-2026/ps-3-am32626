def approximate_pi(n_terms):
  total_sum = 0
  denominator = 1
  sign = 1
  for i in range(n_terms):
    corrent_terms = sign / denominator
    total_sum += corrent_terms
    denominator += 2
    sign *= -1
  return total_sum * 4

print(approximate_pi(1000000))
    
