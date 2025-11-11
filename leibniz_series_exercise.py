def approximate_pi(n_terms):
  total_sum = 0
  denominator = 1
  sign = 1
 for i in range(n_terms):
     corrent_term =  sign / denominator
     total_sum = total_sum + correct_term
     denominator = denominator + 2
     sign = sign * -1
     result = total_sum * 4
  return result
    


