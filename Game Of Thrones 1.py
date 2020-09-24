#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gameOfThrones function below.
def gameOfThrones(p):
    p = p.lower().replace(" ","")

    # print(p)
    P_dict = dict()
    for i in p:
        if i in P_dict:
            P_dict[i] += 1
        else:
            P_dict[i] = 1
    # print(P_dict)
    count = 0
    for value,occurence in P_dict.items():
        if occurence % 2 == 0:
            count += 0
        else:
            count += 1
    # print(count)
    if count > 1:
        return("NO")
    return("YES")


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    p = input()

    result = gameOfThrones(p)

    fptr.write(result + '\n')

    fptr.close()
