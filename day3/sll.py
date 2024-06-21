class node:
    def __init__(self,x):
        self.data=x
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insert_at_end(self,b):
        if self.head==None:
            self.head=node(b)
        else:
            t=self.head
            while (t.next):
                t=t.next
            t.next=node(b)
    def insert_at_beg(self,b):
        if self.head==None:
            self.head=node(b)
        else:
            t=node(b)
            t.next=self.head
            self.head=t
    def delete_at_end(self):
        if self.head==None or self.head.next==None:
            self.head=None
        t=self.head
        while t.next.next:
            t=t.next
        t.next=None
    def delete_at_begin(self):
        if self.head.next==None:
            self.head=None
        else:
            self.head=self.head.next
    def search(self,a):
        if self.head==None:
            return None,None
        t= self.head
        c=0
        while t:
            c+=1
            if t.data==a:
                return True,c
            t=t.next
        return False,None
    def find_middle_node(self):
        if self.head==None:
            return self.head
        else:
            slow=self.head
            fast=self.head
            while  fast and fast.next :
                fast=fast.next.next
                slow=slow.next
            return slow.data 
    def even_odd(self):
        fast=self.head
        c=0
        while fast and fast.next:
            c+=2
            fast=fast.next.next
            return "even" if c%2==0 else "odd"
    def longest_sequence(self):
        t=self.head
        c=1
        max=1
        while(t.next!=None):
            if t.data+1==t.next.data:
                c+=1
                if max<c:
                    max=c
            else:
                c=1
            t=t.next
        return max 
    def allpairs(self):
        t=self.head
        a=self.head.next 
        while t.next:
            while a:
                print(t.data,a.data)
                a=a.next
            a=t.next
            t=t.next
    def bubblesort(self):
        # t=self.head
        # while t:
        #     a=t
        #     while a:
        #         if t.data>a.data:
        #             a.data,t.data=t.data,a.data
        #         a=a.next
        #     t=t.next      
        c=0
        t=self.head
        p=None
        while(t.next!=None):
            f=0
            t=self.head
            while(t.next!=p):
                if(t.next>t.next.data):
                    f=1
                    t.data,t.next.data=t.next.data,t.data
                t=t.next
                c=c+1
            if(f==0):
                break
    def chg_link(self):
        curr=self.head 
    def sum_ll(self):
        t=self.head
        s=0
        while t:
            s+=t.data
            t=t.next
        return s
    def display(self):
        t=self.head
        while t:
            print(t.data,end=" ")
            t=t.next
a=sll()
a.insert_at_end(10)
a.insert_at_end(20)
a.insert_at_end(40)
a.insert_at_beg(29)
print(a.sum_ll())
a.display()
# a.delete_at_end()
# a.delete_at_begin()
# a.find_middle_node()
print("\nmiddle node element is " ,a.find_middle_node())
print(a.search(20))
print(a.even_odd())
print(a.longest_sequence())
a.allpairs()
a.bubblesort()










# class node:
#     def __init__(self,u):
#         self.data=u
#         self.nxt=None
# class sll:
#     def __init__(self):
#         self.head=node
#     def display(self):
#         t=self.head
#         while(t!=None):
#             print(t.data,end=" ")
#             t=t.nxt
#     def addend(self,x):
#         if self.head==None:
#             self.head=node(x)
#         else:    
#             t=self.head
#             while(t.nxt):
#                 t=t.nxt
#                 t.nxt=node(x)
#     def search(self,a):
#         t=self.head
#         while(t!=None):
#             if t.data==a:
#                 return True
#             t=t.nxt
#         return False
#     def middle_node(self):
#         t=self.head





            