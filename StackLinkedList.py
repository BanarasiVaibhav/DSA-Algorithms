class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.head=node()
        
    # there is some bug in this method
    def is_empty(self):
        if self.head==None:
            return False
        else:
            return True
    def length(self):
        cur=self.head
        total=0
        while cur.next!=None:
            total+=1
            cur=cur.next
        return total
    
    
    def insert(self,data):
        if self.head==None:
            new_node=node(data)
            cur.next=new_node
            new_node.next=None
        cur=self.head
        while cur.next!=None:
            cur=cur.next
        new_node=node(data)
        cur.next=new_node
        new_node.next=None
    
    
    def delete(self):
            cur0=self.head
            cur1=cur0.next
            while cur1.next!=None:
                cur1=cur1.next
                cur0=cur0.next
            cur0.next=None
            
    def display(self):
        cur=self.head    
        while cur.next!=None:
            print(cur.data)
            cur=cur.next
        print(cur.data)
            
    def top(self):
        cur=self.head
        while cur.next!=None:
            cur=cur.next
        print(cur.data)
obj=stack()
