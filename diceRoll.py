import random
#The usage of randint(a,b) function of the random() module is displayed in this mini dice rolling simulator program.

while True: 
 inp= input("Please enter the number of \nfaces in the dice that you want to use: ")
 inpPlus1= 1+int(inp)
 randomInt= random.randint(1,inpPlus1)
 print("The dice gives: "+str(randomInt))

