

#A function that returns the indexes of the found numbers (return value is a tuple) such that the sum of these numbers is equal to a target value.

def findTarget1(arr,target):
  for i in range(0,len(arr)):
    for j in reversed(range(0,len(arr))):
      if arr[i]+arr[j]==target and i!=j:
        return (i,j)

    


 
    

lst= [19,2,3,4,59,99,7]

print(findTarget1(lst,9))
print(findTarget1(lst,21))
print(findTarget1(lst,5))
print(findTarget1(lst,6))
print(findTarget1(lst,7))
print(findTarget1(lst,158))
print(findTarget1(lst,29))



    
