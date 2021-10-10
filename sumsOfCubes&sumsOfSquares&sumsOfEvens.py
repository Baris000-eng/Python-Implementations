def sums_of_squares(upper_bound):
  return (upper_bound*(2*upper_bound+1)*(upper_bound+1))/6

def sums_of_cubes(upper_bound):
  return (((upper_bound)*(upper_bound+1))/2)**2

def sums_of_evens(upper_bound):
    return upper_bound/2*(upper_bound/2+1)






print(sums_of_squares(5))
print(sums_of_cubes(5))
print(sums_of_evens(6))



