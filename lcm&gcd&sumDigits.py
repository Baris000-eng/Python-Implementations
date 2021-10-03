def sum_digits(n):#A function that sums the digits of the inputted integers
    sumOfDig = 0
    while n>0:
        i= n%10
        sumOfDig += i
        n = n//10
    return sumOfDig

def gcd(a,b):#A function that finds the greatest common divisor of the two integers.
  max_divisor=1
  if a>b:
    for i in range(1,b+1):
      if a%i==0 and b%i==0:
        if i>max_divisor:
          max_divisor=i
  elif b>a:
     for i in range(1,a+1):
      if a%i==0 and b%i==0:
        if i>max_divisor:
          max_divisor=i
  elif b==a:
    return a
  return max_divisor

def lcm(num1,num2):#A function that finds the least common multiple of the two integers.
   i= num2
   j= num1
   if num2>num1:
     if num2%num1==0:
       return num2
     while True:
       i= i+1
       if i%num2==0 and i%num1==0:
         return i
   elif num1==num2:
     return num1
   elif num1>num2:
     if num1%num2==0:
       return num1
     while True:
       j= j+1
       if j%num2==0 and j%num1==0:
         return j

  

print(lcm(0,0))
print(lcm(3,1))
print(lcm(15,2))
print(lcm(30,45))
print(lcm(20,25)) 
print(lcm(10,12))
print(gcd(0,0))
print(gcd(3,6))
print(gcd(40,45))
print(gcd(100,80))
print(gcd(100,140))
print(sum_digits(229))
print(sum_digits(1234554321))
print(sum_digits(38109542))

