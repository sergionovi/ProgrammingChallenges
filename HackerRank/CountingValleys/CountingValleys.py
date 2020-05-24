#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    #Lets Track the altitude after each step
    soma=[0];
    for i in range(n):
       if s[i]=='U':
           soma.append(soma[-1]+1);
       else:
           soma.append(soma[-1]-1);
    #Find amplitudes equal to zero. Next, we veirfy if the subject came from a valley (denoted by negative value) or a mountain (denoted by positive value)
    valley=0
    for i in range(1,len(soma)):
        if soma[i]==0:
            if soma[i-1]<0:
                valley=valley+1;
    return valley
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
