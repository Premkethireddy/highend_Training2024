a=list(map(int,input().split(" ")))
m=[]
c=0
while (c!=len(a)):
    r=[]
    for i in range (len(a)):
        if(not str(a[i]).isalpha()):
            if(a[i] not in r):
                c=c+1
                r.append(a[i])
                a[i]='a'
    m.append(r)
print(m)


     