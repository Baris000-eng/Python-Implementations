while True:
 inp= input("Enter a number: ")
 if int(inp)<0:
   print("Program ends!")
   break
 else:
  mult= 1
  for i in range(1,(int(inp)+1)):
    mult= mult*i;
  print("The factorial of "+str(inp)+" is: "+str(mult))

