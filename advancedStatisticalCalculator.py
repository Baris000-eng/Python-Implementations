import math
import time
from random import seed
from random import randint
#EXTENSIVE STATISTICAL CALCULATOR IN PYTHON
def findMaxInArray(arr):
  max= arr[0]
  for i in range(0,len(arr)):
    if(arr[i]>=arr[0]):
      max= arr[i]
  return max

def findMinInArray(arr):
  min= arr[0]
  for i in range(0,len(arr)):
    if(arr[i]<=arr[0]):
      min= arr[i]
  return min

ls= []
inp= input("How many elements of which \nyou want to calculate the statistical values?: ")
print()
for i in range(int(inp)):
  statPut= input("Number"+str(i+1)+": ")
  ls.append(int(statPut))
  print()

upperBoundSleep= input("Please input the upper bound of the sleeping time of the program: ")
def countNums(arr):
  counter=0
  l= len(arr)
  for h in range(0,l):
    if(arr[h]!=None):
     counter+=1
  return counter

print("****Welcome to The Advanced Statistical Calculator Program******")
print()
time.sleep(randint(0,int(upperBoundSleep)))
print("Program loading ...")
time.sleep(randint(0,int(upperBoundSleep)))
print()
print("...")
print()
time.sleep(randint(0,int(upperBoundSleep)))
print("...")
time.sleep(randint(0,int(upperBoundSleep)))
print()
p= input("Please enter a number: ")
print()
if(int(p)==1):
  l= len(ls)
  summation=0
  for i in range(0,l):
    summation=summation+ls[i]
  print("The sum of the elements in the ls array is : "+str(summation))
elif(int(p)==2):
  s=0
  counter=0
  average=0
  a= len(ls)
  for k in range(0,a):
    counter=counter+1
    s=s+ls[k]
  average= (s/counter)
  print("The average of the elements in the ls array is: "+str(average))
elif(int(p)==3):
   ls.sort()
   c= countNums(ls)
   if(c%2==0):
      sumForMedian= ls[(int)((len(ls)-1)/2)]+ls[(int)(((len(ls)-1)/2)+1)]
      sumForMedian=sumForMedian/2
      print("The median for an array including even number of elements is: "+str(float(sumForMedian)))
   elif(c%2==1):
      print("The median for an array including odd number of elements is: "+str(float(ls[(int)((len(ls)-1)/2)])))
elif(int(p)==4):
  t= len(ls)
  arr= []
  for w in range(0,t):
    arr.append(ls.count(ls[w]))
    number= findMaxInArray(arr)
    if(arr[w]==number):
      print("The mod of the elements in the ls array is "+str(ls[w]))
      break
elif(int(p)==5):
  s=0
  counter=0
  sumForStandardDev=0
  average=0
  a= len(ls)
  for k in range(0,a):
    counter=counter+1
    s=s+ls[k]
  average= (s/counter)
  differenceSq= []
  for y in range(0,a):
    differenceSq.append(((ls[y]-average)**2))
  totalMinus1= counter-1
  for d in range(0,len(differenceSq)):
    sumForStandardDev= sumForStandardDev+differenceSq[d]
  div= sumForStandardDev/totalMinus1
  standardDev= math.sqrt(div)
  print("The standard deviation of the elements in the ls array is "+str(standardDev))
elif(int(p)==6):
  s=0
  counter=0
  sumForStandardDev=0
  average=0
  a= len(ls)
  for k in range(0,a):
    counter=counter+1
    s=s+ls[k]
  average= (s/counter)
  differenceSq= []
  for y in range(0,a):
    differenceSq.append((ls[y]-average)**2)
  totalMinus1= counter-1
  for d in range(0,len(differenceSq)):
    sumForStandardDev= sumForStandardDev+differenceSq[d]
  div= sumForStandardDev/totalMinus1
  standardDev= math.sqrt(div)
  variance= standardDev**2
  print("The variance of the elements in the ls array is "+str(variance))
elif(int(p)==7):
   maximum= findMaxInArray(ls)
   print("The maximum number in array ls is: "+str(maximum))
elif(int(p)==8):
  minimum=findMinInArray(ls)
  print("The minimum number in array ls is: "+str(minimum))
elif(int(p)==9):
   maximum2= findMaxInArray(ls)
   minimum2=findMinInArray(ls)
   ran= maximum2-minimum2
   print("The range of the elements in the ls array is  : "+str(ran))
elif(int(p)==10):
  total= countNums(ls)
  print("There are "+str(total)+" elements in the ls array in total. ")
elif(int(p)==-1):
  print("Program ends!")





  

    
