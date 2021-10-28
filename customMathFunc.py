def customCeilFunction(j):
  int_part= j//1
  return int_part+1
def customLogBase2OfANumber(k):
  divCount=0
  while k>1:
    k= k/2
    divCount=divCount+1
  return divCount

def customAbsoluteValue(n):
  if n<0:
    n=-n
  return n

def customRoundFunction(n):
 if((n-n//1)>=0.5):
    return n//1+1
 else: 
    return n//1

print(customAbsoluteValue(-12.292992))
print(customAbsoluteValue(0))
print(customAbsoluteValue(-2.4))
print(customRoundFunction(12.5))
print(customRoundFunction(12.4))
print(customRoundFunction(12.6))


  
