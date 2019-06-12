import random
class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class linked_list:

    def __init__(self):
        self.head=node()
    
    # please check its indentation 
    def insert(self,index,data):
        new_node=node(data)
        cur_node=self.head
        for i in range(index):
            cur_node=cur_node.next
        new_node.next=cur_node.next
        cur_node.next=new_node


        
        
    def append(self,data):
        new_node=node(data)
        cur=self.head
        while cur.next!=None:
            cur=cur.next
        cur.next=new_node

    def length(self):
        cur=self.head
        total=0
        while cur.next !=None:
            total+=1
            cur=cur.next
        return total

    def display(self):
        elems=[]
        cur_node=self.head
        while cur_node.next !=None:
            cur_node=cur_node.next
            elems.append(cur_node.data)
        print(elems)
    def erase(self,index):
        if index>=self.length():
            print("Index out of range")
            return
        cur_idx=0
        cur_node=self.head
        while True:
            last_node=cur_node
            cur_node=cur_node.next
            if cur_idx==index:
                last_node.next=cur_node.next
                return
            cur_idx+=1
my_list=linked_list()

for i in range(10):
    j=random.randint(0,99)
    my_list.append(j)
my_list.display()
my_list.erase(4)
my_list.display()
my_list.append(1729)
my_list.display()

my_list.insert(2,'new_insert_at_position_2')
my_list.display()
