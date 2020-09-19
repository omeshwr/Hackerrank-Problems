#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the freqQuery function below.
def freqQuery(queries):
    res=[]
    d1=Counter()
    d2=Counter()
    for op,value in queries:
        if op==1:
            d2[d1[value]]-=1
            d1[value]+=1
            d2[d1[value]]+=1
        elif op==2:
            if d1[value]>0:
                d2[d1[value]]-=1
                d1[value]-=1
                d2[d1[value]]+=1
        elif op==3:
            res.append(1 if d2[value]>0 else 0)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
