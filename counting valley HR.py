s=['D','U','D','U','D','U','D','D','D','U','U','U']
n=len(s)
count =0
at=[]
i=0
j=0
p=0
while i<n:                 #Producing The graphic array
    if s[i] == "D":
         p -= 1
         at.append(p)
         i+=1
    else:
        p += 1
        at.append(p)
        i+=1
while j<len(at)-1:       #Checking for -1 0 combination in the array ,it represents a valley end
    if at[j]== -1 and at[j+1]== 0:
        count +=1
        j +=1
    else:
        j+=1
print(count)
print(at)












