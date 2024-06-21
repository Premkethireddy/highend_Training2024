def f(x):
    if (x==0):
        return 0
    return x+f(x-2)
n=13
if(n%2==0):
    print(f(n))
else:
    print(f(n-1))
    
# print (f(10))

        