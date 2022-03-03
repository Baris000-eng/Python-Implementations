#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

#My implementation to the function printing a staircase with the height given to the inside of the function
def staircase(n):
    for i in range(0,n):
        print(" " * (n-(i+1)) + "#"*(i+1))
      
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
