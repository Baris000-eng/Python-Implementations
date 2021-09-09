
def add(x,y):
  a=x+y
  return a #Writing a function called add to add the numbers inside of the function

def subtract(c,d):
  sub=c-d
  return sub#Writing a function called subtract to subtract the second number inside of the subtract() function from the first number. 

def multiply(k,m):
 return k*m#Writing a function called multiply to multiply the numbers inside of the function

def divide(firstNum,secondNum):
  if(secondNum!=0):
    result=firstNum/secondNum
    return result
  else:
    print("Invalid division")#Writing a function called divide to divide the first number with the second number inside of the function 

def cubeANumber(num1):
  num1= num1*num1*num1
  return num1#Return the cube of the number passed inside of the function called "cubeANumber"


print(add(1,2))#Calling add(x,y) function
print(add(2,3))
print(subtract(4,2))#Calling subtract(c,d) function
print(add(2,add(2,3)))#Calling add function inside of the add function
print(add(add(3,9),subtract(6,2)))#Calling add and subtract functions inside of the add function
print(add(multiply(add(2,3),3),subtract(multiply(2,4),subtract(3,5))))
print(divide(6,3))
print(cubeANumber(3))








