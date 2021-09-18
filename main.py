choices= ["rock","paper","scissors"]
user1Count=0
user2Count=0
winNum=3

while True:

  user1= input("My choice is : ")
  user2= input("My choice is : ")
  print()
  if(user1==choices[0] and user2==choices[1]):
    user2Count+=1
  elif(user1==choices[0] and user2==choices[2]):
    user1Count+=1
  elif(user1==choices[2] and user2==choices[1]):
    user1Count+=1
  elif(user1==choices[1] and user2==choices[0]):
    user1Count+=1
  elif(user1==choices[2] and user2==choices[0]):
   user2Count+=1
  elif(user1==choices[1] and user2==choices[2]):
   user2Count+=1
  elif(user1==choices[0] and user2==choices[0]):
    print("Choices are same ! ")
    continue
  elif(user1==choices[1] and user2==choices[1]):
    print("Choices are same ! ")
    continue
  elif(user1==choices[2] and user2==choices[2]):
    print("Choices are same ! ")
    continue
  if(user1Count>user2Count and user1Count==winNum):
   print("User1 has won ! ")
   print("The final score is User1: "+str(winNum)+" and User2: "+str(user2Count)+"")
   break
  if(user2Count>user1Count and user2Count==winNum):
   print("The final score is User2: "+str(winNum)+" and User1: "+str(user1Count)+"")
   print("User2 has won ! ")
   break
 
 #ROCK, PAPER, SCISSORS GAME IN PYTHON
   
 