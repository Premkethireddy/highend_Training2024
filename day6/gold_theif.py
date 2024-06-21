l=list(map(int,input().split(" ")))
def fun(l):
    if(len(l)==0):
        return 0
    if(len(l)==1):
        return l[0]
    if (len(l)==2):
        return max(l)
    le=l[0]+fun(l[2:])
    ri=l[1]+fun(l[3:])
    return max(le,ri)
print(fun(l))
    
