s=input()
c=0
c1=0
for i in s:
    if i=='m':
        c+=1
    else:
        c1+=1
if (c>c1):
    print('m')
elif (c==c1):
    print('0')
else:
    print('f')