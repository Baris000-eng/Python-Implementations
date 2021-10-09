#Custom Math Functions implemented by me!
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

def customPowerFunc(num1,num2):
  a= 1
  if(num2<0):        
    num1=1/num1       
    num2= -num2
  for i in range(0,num2):
    a= num1*a
  return a

print(customAbsoluteValue(-12.292992))
print(customAbsoluteValue(0))
print(customAbsoluteValue(-2.4))
print(customRoundFunction(12.5))
print(customRoundFunction(12.4))
print(customRoundFunction(12.6))
print(customPowerFunc(3,-2))
print(customPowerFunc(3,2))
print(customPowerFunc(-3,-2))
print(customPowerFunc(-3,2))

  