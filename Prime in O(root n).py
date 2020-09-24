# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def prime(n):                             
    sq = int(math.sqrt(n))                      # square root  function 
    if n == 1:
        print("Not prime")
        return
    for i in range(2,sq+1):                     # Main logic checking wether i is in 2 to sqrt of the number ,else it wont be prime
        if n%i == 0:							# This reduces complexity from  O(n) to O(root n)
            print("Not prime")
            break
    else:
        print("Prime")

t = int(input())
for v in range(t):
    p = int(input())
    prime(p)       





