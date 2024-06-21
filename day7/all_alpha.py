
# l="abc defghijklmnopqrstuvwxyz"
# s=set(l)
# print(s)
# if len(s)==27:
#     print("yes")
# else:
#     print("No")

l="the 4quick br@#$567own foASx jumps over th,e lazy dog"
c=0
l=set(l)
for i in l:
    if i.isalpha() and i.islower():
        print(i,end="")
        c+=1
print("/n",c,"yes" if c==26 else "no")

l="the 4quick br@#$567own foASx jumps over th,e lazy dog"
d=[0]*26
for i in l:
    if i.islower():
        d[ord (i)-97]+=1
print(all(d))











# for i in range(l):
#     if i.isalpha()
