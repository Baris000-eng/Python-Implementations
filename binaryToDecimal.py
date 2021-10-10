def customPowerFunc(num1,num2):
  a= 1
  if(num2<0):        
    num1=1/num1       
    num2= -num2
  for i in range(0,num2):
    a= num1*a
  return a
  
  
def binaryToDecimal(k):
     summation=0
     numberList=[]
     for number in reversed(str(k)):
         numberList.append(number)
     for num in reversed(range(0,len(str(k)))):
                 summation= summation+int(numberList[num])*customPowerFunc(2,num)
     return summation
     

print(binaryToDecimal(101))
print(binaryToDecimal(11100))
print(binaryToDecimal(101))
print(binaryToDecimal(111))