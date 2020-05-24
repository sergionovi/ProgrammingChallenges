#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):

    # Find Unique Values inside ar
    aux = []
    for x in ar:
        if x not in aux:
            aux.append(x)
    
   
    count=[];# List to add the number of socks per color
    for item in aux:
        cnt=0;
        for item2 in ar:
            if item==item2:
                cnt=cnt+1;
        count.append(int(cnt/2));
              
    return sum(count)






if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
