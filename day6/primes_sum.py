# n=int(input())
# b=[]
# def bc(l, a, i):
#     if len(a) == 2 and sum(a)==n:
#         b.append(a[:])  
#         return
#     for j in range(i, len(l)):
#         a.append(l[j])
#         bc(l, a, j + 1)
#         a.pop() 
# print(b)
def isprime(x):
    if(x==1):
        return 1
    if(x==2):
        return 1
    for i in range(2,(x//2)+1):
        if(x%i==0):
            return 0
    return 1
a=int(input())
for i in range(1,(a//2)+1):
    if (isprime(i)and isprime(a-i)):
        print("yes")
        break
else: 
    print("No")
