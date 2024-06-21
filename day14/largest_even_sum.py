# p='tu5g2k1h8'
# q='g5g8gd6h3'
# r=[]
# for i in p:
#     if i.isdigit() and i not in r:
#         r.append(i)
# for i in q:
#     if i.isdigit() and i not in r:
#         r.append(i)
# r.sort(reverse=True)
# # print(r)
# if int(r[-1])%2!=0:
#     # r=int("".join(i for i in r))
#     # print(r)
#     r1=r[::-1]
#     for i in range(1,len(r1)):
#         if int(r1[i])%2==0:
#             r1[i],r1[0]=r1[0],r[i]
#             break
#     r=r1[::-1]
# r=int("".join(i for i in r))
# print(r)
    


u='tu5g2k1h8'
v='g5g8gd6h3'
n=[]
for i in u:
    if i.isdigit() and i not in n:
        n.append(i)
for i in v:
    if i.isdigit() and i not in n:
        n.append(i)
n.sort(reverse=True)
if int(n[-1])%2!=0:
    n1=n[::-1]
    for i in range(1,len(n1)):
        if int(n1[i])%2==0:
            n1[i],n1[0]=n1[0],n1[i]
            break
    n=n1[::-1]
n=int("".join(i for i in n))
print(n)

