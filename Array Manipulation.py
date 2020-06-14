 #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    res = []
    k = 0
    #res_matrix = [[0 for x in range(n+2)] for y in range(m+1) ]
    res_matrix = {}
    res_final = []
    p = 0
    for i in range(len(queries)):            # O(n)
        a = queries[i][0]
        b = queries[i][1]
        k = queries[i][2]
        if a in res_matrix:
            res_matrix[a] += k
        else:
            res_matrix[a] = k

        if b+1 in res_matrix:
            res_matrix[b+1] += -k
        else:
            res_matrix[b+1] = -k
        
    res_matrix_items = res_matrix.keys()
    h = sorted(res_matrix_items)
    #print(res_matrix)
    # for i in range(n+2):                      #O(n+2 * m+1)
    #     k = 0
    #     for j in range(m+1):
    #         k += res_matrix[j][i] 
    #     res.append(k)
    print(h)
    s = 0
    for k in h:
        res_matrix[k] = res_matrix[k] + s
        s = res_matrix[k]
        res_final.append(res_matrix[k])
    print(max(res_final))


   
    
  
            
    
     

    
    

if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)










				





	

		
		

