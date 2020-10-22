#!/bin/python3
from collections import Counter
import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    wild_card = False
    s_ = Counter(s)
    if len(s_) == 1:
        return "YES"
    
    keys = list(s_.values())
    minimus = min(keys)
    if 1 in keys:
        if keys.count(1) == 1:
            wild_card = True
    print(keys)
    if len(set(keys)) == 1:
        return "YES"
    if len(set(keys)) == 2 and keys.count(minimus+1) == 1:
        return "YES"
    if len(set(keys)) == 2 and wild_card:
        return "YES"


    else:
        return "NO"






if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
