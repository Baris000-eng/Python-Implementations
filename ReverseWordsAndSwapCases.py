#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

#Reverses the words order in a sentence and swap the case of # each letter in each of the words in the sentence
def reverse_words_order_and_swap_cases(sentence):
    lst = sentence.split()
    reversed_lst = reversed(lst)
    rev_sent = " ".join(reversed_lst)
    return rev_sent.swapcase()
        

        
            
       
        
        
        
       
    
   
    
    
    
      
       

   
            
   
    
     
    # Write your code here
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)

    fptr.write(result + '\n')

    fptr.close()