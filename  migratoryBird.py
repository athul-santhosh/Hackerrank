#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
# def migratoryBirds(arr):
#     bird_dict =float("inf")
#     bird_dict = {}
#     for i in range(len(arr)):
#         if arr[i] in bird_dict:
#             bird_dict[arr[i]] += 1
#         else:
#             bird_dict[arr[i]] = 1
#     k = max(bird_dict.values())
#     print(bird_dict)
#     p =[]
#     for bird,count in bird_dict.items():
#         if count == k:
#             p.append(bird)
#     p.sort()
#     return p[0]
def migratoryBirds(arr):
    m = range(5)
    for b in ar:
        m[b-1] += 10
    return max(m) % 10
   




arr_count = int(input().strip())

arr = list(map(int, input().rstrip().split()))

result = migratoryBirds(arr)

print(result)



