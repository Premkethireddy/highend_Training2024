s="avfgresagtyuiofde"
c=0
maxc=0
for i in range(len(s)-1):
    j=i
    a=''
    c=0
    while j<len(s)-1:
        a+=(s[j])
        c+=1
        j+=1
        if s[j] in a:
            break
    print(a,c)
    maxc=c if c>maxc else maxc
print(maxc)
   