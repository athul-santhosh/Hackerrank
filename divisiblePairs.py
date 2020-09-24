def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n):                                
        for j in range(i+1,n):                        #O(n log n)
            if (ar[i] + ar[j]) % k == 0:              # checking for pairs to match if it is divisible by 5
                count += 1
                #print(ar[i],ar[j])                   # shows the pairs
    return count
