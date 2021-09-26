inp1= input("Please enter a number to be divided: \n")
inp2= input("Please enter the divisor number: \n")

print(""+str(inp1)+" divided by "+str(inp2)+" is: \n")
count1=0

while(int(inp1)>0):
  inp1= int(inp1)-int(inp2) # let inp1= 4 and inp2= 2, 4= 4-2 makes inp1=2 and inp2= 2. 2= 2-2 makes inp1= 0 and inp2=2. Since int(inp1)==0, the loop stops.
  count1+=1

print(""+str(count1))



