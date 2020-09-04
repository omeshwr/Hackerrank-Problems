#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(n,c):
    no_of_jumps= 0
    i=0
    while(True):
        if(i+2<n and c[i+2]==0):
            i+=2
        elif(i+1<n):
            i+=1
        else:
            break
        no_of_jumps+=1
    return no_of_jumps
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(n,c)

    fptr.write(str(result) + '\n')

    fptr.close()
