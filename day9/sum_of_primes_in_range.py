def isprime(x):
    for i in range(2,(x//2)+1):
        if x%i==0:
            return False
    return True
def lprime(n,m):
    for i in range(m-1,n,-1):
        if isprime(i):
            return i
    return 0
                     
l=list(map(int,input().split(" ")))
sum=0
for i in range(len(l)-1):
    # for j in range(len(l)-2):
    #     if isprime(j):
    #         sum=sum+j
    sum=sum+lprime(l[i],l[i+1])
print(sum)        



