import math
import os
import random
import re
import sys


# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    if n == m:
        return 0
    final = []
    temp = [0 for i in range(n)]
    for i in c:
        temp[i] = 1
    for i in range(len(temp)):
        if temp[i] == 0:
            j = i
            countj = 1
            while temp[j + 1] != 1 and j+1 > len(temp)-1:
                countj += 1
                j += 1
            k = i
            countk = 1
            while temp[k - 1] != 1:
                countk += 1
                k -= 1
            final.append(min(countj, countk))
            #print(countj,countk)
    return max(final)


nm = input().split()

n = int(nm[0])

m = int(nm[1])

c = list(map(int, input().rstrip().split()))

result = print(flatlandSpaceStations(n, c))