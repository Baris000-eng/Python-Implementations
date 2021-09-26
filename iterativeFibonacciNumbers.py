def iterativeFibonacci(inputtedIndex):
    a= 0
    b= 1
    c= 1
    for i in range(0,inputtedIndex):   
        a=b 
        b=c   
        c=a+b  
    return a     

#Let's say we want to find iterativeFibonacci(2)

# 0 1 1 2 3 5 

# a b c

#   a b c 

#     a b c  (At the 2nd iteration, a is 1. So, iterativeFibonacci(2)=1)



inp= input("Please enter how many fibonacci numbers \nyou want to print: ")
print()
for i in range(1,int(inp)+1):
   print("The "+str(i)+"th fibonacci number is: "+str(iterativeFibonacci(i))+"")


