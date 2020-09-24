# Enter your code here. Read input from STDIN. Print output to STDOUT
def issuper(A,B,m,u):
    k =[]
    k.append(A.issuperset(B))

    if m == u-1:
        for i in range(len(k)):
            if k[i] == True:
                continue
            elif k[i] == False:
                print("False")
                break
        else:
        	print("True")
            



            
        
    
     

SS = set(map(int,input().strip().split()))                 #the main part 
t = int(input())
for i in range(t):
    S = set(map(int,input().strip().split()))
    #S = set(map(int, input().rstrip().split()))
    issuper(SS,S,i,t)



