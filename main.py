import math

firstX= input("Please enter an x value in the coordinate system: ")
firstY= input("Please enter a y value in the coordinate system: ")
firstPoint=(firstX,firstY)
print()
secondX= input("Please enter an x value in the coordinate system: ")
secondY= input("Please enter a y value in the coordinate system: ")
secondPoint=(secondX,secondY)
differenceX= int(secondX)-int(firstX)
differenceY= int(secondY)-int(firstY)
sumOfSquares= differenceX**2+differenceY**2
result= math.sqrt(sumOfSquares)
print()
print("The distance between the points specified is : "+str(result))

