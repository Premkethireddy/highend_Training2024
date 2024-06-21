a=input()
b=int(input())
b=b%26
for i in a:
    c=ord(i)
    if ord(i)-b<97:
        c=ord(i)+26
    print(chr(c-b),end="")

          