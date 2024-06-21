n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
l_sum=sum(l)
print(n*(n+1)//2 - sum(l))