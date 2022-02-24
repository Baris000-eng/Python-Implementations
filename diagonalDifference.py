#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

#My solution to the function which computes the difference between the sums of the diagonals of a 2d matrix.
def diagonalDifference(arr):
    sum1=0
    sum2=0
    
    for i in range(0,len(arr)):
       sum1= sum1+arr[i][i]
    
    
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            if i+j==len(arr)-1:
                sum2=sum2+arr[i][j]
    
    diff= sum1-sum2
    
    if diff<0:
        diff=-diff
        
    return diff
                
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
