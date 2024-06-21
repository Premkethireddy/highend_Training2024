a=[4,9999,2,4,4,8,4]
c=1
p=a[0]
for i in range(1,len(a)):
    if (a[i]==p):
        c=c+1
    else:
        if(c!=0):
            c=c-1
        if(c==0):
            c=c+1
            p=a[i]
print(p)