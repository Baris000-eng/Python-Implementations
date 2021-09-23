import math

print("*****Welcome to the Perimeter & Area Calculator: ")
print()
inp= input("Please enter your choice: ")
print()
if(int(inp)==1):
  inpSq= input("Please enter the length of the edge of square: ")
  print()
  areaOfSq= float(inpSq)**2
  perimeterOfSq= 4*float(inpSq)
  print("The area of the specified square is: "+str(areaOfSq))
  print()
  print("The perimeter of the specified square is: "+str(perimeterOfSq))

elif(int(inp)==2):
  inpShortEdgeRec= input("Please enter the length of the short edge of the rectangle: ")
  print()
  inpLongEdgeRec= input("Please enter the length of the long edge of the rectangle: ")
  if(inpShortEdgeRec>=inpLongEdgeRec):
    print()
    print("Invalid edges !!!")
    print()
    inpShortEdgeRec= input("Please enter the length of the short edge of the rectangle: ")
    print()
    inpLongEdgeRec= input("Please enter the length of the long edge of the rectangle: ")
  areaOfRec= float(inpShortEdgeRec)*float(inpLongEdgeRec)
  perimeterOfRec= 2*(float(inpShortEdgeRec)+float(inpLongEdgeRec))
  print()
  print("The area of the specified rectangle is: "+str(areaOfRec))
  print()
  print("The perimeter of the specified rectangle is: "+str(perimeterOfRec))

elif(int(inp)==3):
  inpRadius= input("Please enter the radius of the circle: ")
  areaOfSq= (math.pi)*(float(inpRadius)**2)
  perimeterOfSq= 2*(math.pi)*float(inpRadius)
  print()
  print("The area of the specified circle is: "+str(areaOfSq))
  print()
  print("The perimeter of the specified circle is: "+str(perimeterOfSq))