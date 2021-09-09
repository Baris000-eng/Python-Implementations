def findMax(x,y,z):#Finding the maximum of three numbers
  if(x>=y and y>=z):
    return x
  elif(y>=x and x>=z):
    return y
  return z


print(findMax(2,3,4))#Gives 4

