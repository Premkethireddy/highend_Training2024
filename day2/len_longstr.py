l=input()
b=1
max=0
for i in range(len(l)-1):
    if (ord(l[i])==ord(l[i+1])-1):
        b+=1
    else:
        if max<b:
            max=b
        b=1
print(max if max else max)
        
