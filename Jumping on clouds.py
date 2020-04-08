def jumpingOnClouds(c):

    c.append("H")
    c.append("I")
    count=0
    i=0
    while i<n:
        if c[i+1] == "H":
            return count
        elif c[i]==0 and c[i+1]==1:
            i+=2
            count +=1
        elif c[i]==0 and c[i+2]==0:
             i+=2
             count +=1
        elif c[i+1]==0 and c[i+2]==1:
             i+=1
             count+=1
        elif c[i]==0 and c[i+1]==0:
             i+=1
             count+=1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
