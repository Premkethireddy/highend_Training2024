# l=list(map(int,input().split()))
# n=len(l)
def subsets(l,k):
    def fun(curr,start):
        if len(curr)==k:
            print(curr)
            return
        for i in range(start,len(l)):
            fun(curr + [l[i]],i+1)
        return  
    fun([],0)
a=[3,5,1,6]
k=3
subsets(a,k)