number1= input("Please enter the first number: ")
number2= input("Please enter the second number: ")
operatorType= input("Please enter the operator type: ")#Getting number1, number2, and operatorType from the user.


number1= float(number1)#Converting the string version of the number1 to float 
number2= float(number2) #Converting the string version of the number2 to float


if(operatorType=='+'): #Addition case
  print(number1+number2)
elif(operatorType=='-'):#Subtraction case
  print(number1-number2)
elif(operatorType=='*' or operatorType=='x'):#Multiplication case
  print(number1*number2)
elif(operatorType=='/' or operatorType==':'): #Division case
  if(number2!=0):
    print(number1/number2)
  else:
    raise Exception("Invalid division.")
else:
  print("Invalid operator type.") #Invalid cases
