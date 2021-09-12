sayı= input("Bir sayı giriniz: ")
while True:
 if int(sayı)<0:
    sayı= input("Yanlış sayı girdiniz, lütfen tekrar sayı girin: ")
    if int(sayı)>0:
     break

for i in range(1,int(sayı)+1):
  if(i%15==0):
    print("AburCubur")
  if(i%3==0 and i%15!=0):
    print("Cubur")
  if(i%5==0 and i%15!=0):
    print("Abur")
  elif((i%15!=0) and (i%3!=0) and (i%5!=0)):
    print(i)



  #A python implementation of a game which is a division learning game for kids. 
  #Firstly, program wants from user to enter a number to which the program will iterate. After that, program iterates over all integers up to the boundary integer entered by the user. if an integer which is between 0 and the boundary integer entered is only divisible by 3, it prints "Cubur". If this integer is only divisible by 5, it prints "Abur". If this integer is only divisible by 15, it prints AburCubur. For the other cases, it prints the integer itself. 

