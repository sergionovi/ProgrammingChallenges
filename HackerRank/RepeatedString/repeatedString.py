#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    # The fastest way to count the frqeuency of 'a' is to find 
    # the frequency over string 's' then muntiply it by the number 
    # of times that we will need to repeat string 's'
    if n>len(s):
        lst1 = list(s);
        counter = s.count('a');
        counter = counter*(n//len(s));#Number of times that 's' will bre repeated
        counter = counter + (s[0:n%len(s)]).count('a')
    else:
        counter =(s[0:n]).count('a');  
       
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
