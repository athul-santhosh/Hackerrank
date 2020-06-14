#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    res = []
    res_final = [] 
    for i in range(arr[-1],brr[0]+1):              # Time : O((brr[0] - arr[-1])*(n+m)) Space O(n)
        for j in range(n):
            if i % arr[j] == 0:
                res.append(i)

        for k in range(m):
            if brr[k] % i == 0 and res.count(i) == n:
                res_final.append(i)
    p = []
    for i in res_final:                              #Time :O(n) Space : O(n)
        if res_final.count(i) == m and i not in p:
            p.append(i)
    return len(p)
                
        
    
                



           

    
    
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
