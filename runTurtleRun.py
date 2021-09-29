#RACING THE TURTLES IN PYTHON, example usages of time.time() function of time module, the Turtle() function of the turtle module are displayed.
import turtle
import random
import time 

def findMinTime(a,b,c,d):
  if a<=b and a<=c and a<=d :
    return a
  elif b<=a and b<=c and b<=d:
    return b
  elif c<=a and c<=b and c<=d:
    return c
  else: 
    return d

def findMaxTime(a2,b2,c2,d2):
  if a2>=b2 and a2>=c2 and a2>=d2 :
    return a2
  elif b2>=a2 and b2>=c2 and b2>=d2:
    return b2
  elif c2>=a2 and c2>=b2 and c2>=d2:
    return c2
  else: 
    return d2




starting_time = time.time()#gets the starting time 
t = turtle.Turtle()

  
r = 50
t.circle(r)

t.goto(0,-45)
t.goto(0,15)


sec1= time.time()-starting_time
print("The runtime of the turtle-1 is: "+str(sec1)+" seconds")#Here, time.time() call gives the end time. 



starting_time2=time.time()
x= turtle.Turtle()
x.goto(0,0)
r= r+15
x.circle(r)
sec2= time.time()-starting_time2
print("The runtime of turtle-2 is: "+str(sec2)+" seconds")

starting_time3=time.time()
y= turtle.Turtle()
y.goto(0,-15)
r= r+15
y.circle(r)
sec3= time.time()-starting_time3
print("The runtime of turtle-3 is: "+str(sec3)+" seconds")

 

starting_time4=time.time()
z= turtle.Turtle()
z.goto(0,-30)
r= r+15
z.circle(r)
sec4= time.time()-starting_time4
print("The runtime of turtle-4 is: "+str(sec4)+" seconds")

min_sec= findMinTime(sec1,sec2,sec3,sec4)

if min_sec==sec1:
  print("Congratulations turtle-1, you won the race! ")
elif min_sec==sec2:
  print("Congratulations turtle-2, you won the race! ")
elif min_sec==sec3:
  print("Congratulations turtle-3, you won the race! ")
else:
  print("Congratulations turtle-4, you won the race! ")

max_sec= findMaxTime(sec1,sec2,sec3,sec4)

if max_sec==sec1:
  print("Turtle-1, you are in the last place in the turtle race! ")
elif max_sec==sec2:
  print("Turtle-2, you are in the last place in the turtle race! ")
elif max_sec==sec3:
  print("Turtle-3, you are in the last place in the turtle race! ")
else:
  print(" Turtle-4, you are in the last place in the turtle race! ")
