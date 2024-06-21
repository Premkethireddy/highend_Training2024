# def rev(n,r,s):
#     r=0
#     if num==0:
#         return 0
#     else:
#         s=s%n
#         r=r*10+s
#         return rev(n//10,r)
# n=int(input())
# print(rev(n))

def rev(n):
    if n==0:
        return 0
    return (n%10)*(10**(len(str(n))-1)) +rev(n//10)
n=int(input())
print(rev(n))
    