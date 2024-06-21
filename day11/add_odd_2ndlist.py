def sum(l1, l2, i=0, j=0, res=[],c=[]):
    if i<len(l1) and j<len(l2):
        if l1[i] % 2 == 0 and l2[j] % 2 != 0:
            res.append(l1[i] + l2[j])
        return sum(l1,l2,i,j+1,res)
    elif i < len(l1):
        return sum(l1,l2,i+1,0,res)
    else:
        return res

l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
print(sum(l1, l2))
