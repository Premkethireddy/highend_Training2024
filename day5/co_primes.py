n=4
m=6
# a=[]
# b=[]
for i in range(2,min(n,m)//2+1):
    # if n%i==0:
    #     a.append(i)
    # if m%i==0:
    #     b.append(i)
    if n%i==0 and m%i==0:
        print("not coprime")
        break
# print(a)
# print(b)
# for i in a:
#     if i in b:
#         print("not coprime")
else:
    print("coprime")