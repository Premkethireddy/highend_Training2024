class node:
    def __init__(self,x):
        self.prev=None
        self.data=x
        self.next=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def addend(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            # self.tail.next=node(x)
            # self.tail.next.prev=self.tail
            # self.tail=self.tail.next
            t=node(x)
            self.tail.next=t
            t.prev=self.tail
            self.tail=t
    def addfront(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            t.next=self.head
            self.head.prev=t
            self.head=t
    def search(self,x):
        if self.head==None:
            return None
        else:
            c=0
            b=0
            h=self.head
            t=self.tail
            while (h!=t and h!=t.next):
                c+=1
                b-=1
                if h.data==x:
                    return "yes",c
                if t.data==x:
                    return "yes",b
                h=h.next
                t=t.prev
            if t.data==x:
                return "yes",c
    def even_odd(self):
        h=self.head
        t=self.tail
        c=0
        while t!=h:
            c=c+2
            h=h.next
            t=t.prev
        return "even" if(c+1)%2==0 else "odd"
    def palin(self):
        h=self.head
        t=self.tail
        while h!=t:
            if h.data!=t.data:
                return "not palindrome"
            h=h.next
            t=t.prev
        return "palindrome"
    def halfreverse(self):
        f=self.head
        s=self.head
        while (f!=None and f.next!=None):
            f=f.next.next
            s=s.next
        h=self.head
        t=s
        while t!=None:
            t.data,h.data=h.data,t.data
            t=t.next
            h=h.next
        a.display()
    def parenthesis(self):
        stack = []
        temp = self.head
        c = 0
        f = 0
        while temp!=None:
            if temp.data in  "[{(":
                stack.append(temp.data)
                c = c+1
            else:
                if len(stack)>0 and ((temp.data == ')' and stack[-1] == '(') or (temp.data == '}' and stack[-1] == '{') or (temp.data == ']' and stack[-1] == '[')):
                    c =c+1
                    stack.pop()
                else:
                    f = 1
                    break 
            temp = temp.next
        

        if f==1 or stack:
            print("\nposition = ",c+1)
        else:
            print("\n-1")
        
    def recdiff(self):
        temp=self.head
        def cal(temp,even,odd):
            if not temp:
                return abs(even-odd)
            if temp.data%2==0:
                even+=temp.data
            else:
                odd+=temp.data
            return cal(temp.next,even,odd)
        return cal(temp,0,0) 
    def primecount(self):
        temp=self.head
        def isprime(val,i):
            if val==1:
                return False
            if i>=val//2:
                return True
            if val%i==0:
                return False
            return isprime(val,i+1)
        def solve(temp,count):
            if not temp:
                return count
            if isprime(temp.data,2):
                count+=1
            return solve(temp.next,count)
        return solve(temp,0)  
    def display(self):
        t=self.head
        while t:
            print(t.data,end="->")
            t=t.next
        print()
    def reversedisplay(self):
        t=self.tail
        while(t!=None):
            print(t.data,end="->")
            t=t.prev
        print() 

a=dll()
a.addend(20)
a.addend(10)
a.addfront(90)
a.addfront(56)
a.addfront(9)
a.addfront(4)
a.display()
a.reversedisplay()
print(a.search(90))
print(a.even_odd())
print(a.palin())
print(a.halfreverse())
print(a.recdiff())