s=input()
b=[]
for i in s:
    if (i!='*'):
        b.append(i)
    else:
        b.pop()
print(''.join(b))