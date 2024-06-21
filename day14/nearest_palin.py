n=int(input())
if str(n)==str(n)[::-1]: print('yes')
else:
    while n>0:
        n+=1
        if str(n)==str(n)[::-1]:
            print(n)
            break
