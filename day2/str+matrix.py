n=int(input())
m=[]
s=[input()for i in range (n)] 
# c=0
# j=0
# a=input()
for i in range (len(n)):
    if (s[i] not in m[i%n]):
        print("no")
        f=1
        break
    else:
        m[i].remove(s[i])
if(f==0):
    print("yes")
#     if j==n:
#         j=0
#     if a[i]in s[j]:
#         c=0
#         j+=1
#     else:
#         c=1
# print("no" if c else "yes")