def mult_digits(a):
  mult=1
  while a>0:#3459
    i= a%10
    mult= mult*i
    a= a//10
  return mult

def hypotenus(a,b):
  return "{:.3f}".format((a**2+b**2)**0.5)




print(mult_digits(3459))
print(mult_digits(3409))
print(mult_digits(6479))
print(mult_digits(123219))
print(mult_digits(28379))
print(mult_digits(4883779))
print(hypotenus(3,4))
print(hypotenus(3,9))
print(hypotenus(8,6))






