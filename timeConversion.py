#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

#My solution to the function converting 12 hour AM/PM format of time to the 24-hour (military) time

#Given a time in -hour AM/PM format, convert it #to military (24-hour) time.

#Note: - 12:00:00AM on a 12-hour clock is #00:00:00 on a 24-hour clock. 

#- 12:00:00PM on a 12-hour clock is 12:00:00 on a #24-hour clock.

#Function Description
#Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.
#timeConversion has the following parameter(s):
#string s: a time in  hour format



#Returns
#string: the time in  hour format

#Input Format
#A single string  that represents a time in -hour #clock format (i.e.:  or ).

#Constraints
#All input times are valid

#Sample Input 0
#07:05:45PM
#Sample Output 0
#19:05:45
def timeConversion(s):
  if(s[len(s)-2:len(s)]=="AM"):
    my_int=int(s[0:2])
    if(my_int==12):
        my_int=my_int-12
    my_str=str(my_int)
    if(my_int==0):
        my_str=str(my_int)+"0"
    else:
        my_str="0"+str(my_int)
    final_str=my_str+s[2:len(s)-2]
    return final_str
  elif(s[len(s)-2:len(s)]=="PM"):
     my_int_2=int(s[0:2])
     if(my_int_2<12):
        my_int_2=my_int_2+12
     my_str_2=str(my_int_2)
     final_str_2=my_str_2+s[2:len(s)-2]
     return final_str_2
      
  
  
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
