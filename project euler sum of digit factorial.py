# Enter your code here. Read input from STDIN. Print output to STDOUT
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def digits(n):
    p =[]
    factorial_sum = 0
    while n > 0:
        r = n%10
        p.append(r)
        n = n//10
    for i in p:
        factorial_sum += factorial(i)
    print(factorial_sum)
    return sfn(factorial_sum)



def sfn(n):
    sumd = 0
    while n > 0:
        r = n% 10
        sumd += r
        n = n//10
    return sumd
# print(digits(25))

def gi(n):
    temp = n
    p = []
    for i in range(1,n):
        if digits(i) == digits(temp):
            p.append(i)
    print(p)
    k = min(p)
    # sgi
    sumg =0
    while k > 0:
        r = k%10
        sumg += r 
        k = k//10
    return sumg



print(digits(342))
    

  