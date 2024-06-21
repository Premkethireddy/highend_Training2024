l=list(map(int,input().split()))
mp=0
buy=l[0]
for i in l:
    if i<buy:
        buy=i
    p=i-buy
    mp=max(mp,p)
print(mp)   