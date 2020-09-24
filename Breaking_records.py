def breakingRecords(a):
    i = 1
    Dec = 0
    Max = Min = a[0]
    Inc = 0
    for i in range(1,len(a)):                  
        if a[i] > Max:                             # calucalting the improvement
            Inc += 1                      
            Max = a[i]                              # main logic in setting the max and min vlaue to a[i]
        if a[i] < Min:                              # calculating the decrement 
            Dec += 1
            Min = a[i]    
    return Inc,Dec
        



