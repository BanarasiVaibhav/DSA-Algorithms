class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class queue:
    
    def __init__(self):
        self.head=node()
    
    
    # there is some bug in this is_empty() method
    def is_empty(self):
        cur=self.head
        if cur.data==None:
            return True
        else:
            return False
        
        
    def top(self):
        cur=self.head
        while cur.next!=None:
            cur=cur.next
        return cur.data
    
    
    def enqueue(self,data):
        cur=self.head
        while cur.next!=None:
            cur=cur.next
        new_node=node(data)
        cur.next=new_node
        new_node.next=None
        return new_node.data
    
    def dequeue(self):
        cur0=self.head
        self.head=cur0.next
    
    
    def display(self):      
        cur=self.head    
        while cur.next!=None:
            print(cur.data)
            cur=cur.next
        print(cur.data)
        
        
q=queue()
            
