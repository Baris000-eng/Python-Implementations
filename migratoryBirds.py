#Description:
#Given an array of bird sightings where #every element represents a bird type id, #determine the id of the most frequently #sighted type. If more than 1 type has #been spotted that maximum amount, return #the smallest of their ids.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
   count = [0,0,0,0,0,0]
   for i in arr:
        count[i] += 1
        
   maxCount=0
   for j in range(0,len(count)):
    if count[j]>=maxCount:
        maxCount=count[j]
        
   return count.index(maxCount)
    
    
   
       
    
    
   
    
              
           
            
   
                                                                             
        
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()