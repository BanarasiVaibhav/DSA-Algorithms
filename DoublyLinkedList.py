class Node:
    def __init__(self,data):
        self.item=data
        self.pref=None
        self.nref=None


class DoublyLinkedList:
    def __init__(self):
        self.start_node=None

    def insert_in_empty(self,data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node=new_node

        else:
            print("List not empty")

    def insert_at_start(self,data):
        new_node=Node(data)
        new_node.nref=self.start_node
        self.start_node.pref=new_node
        self.start_node=new_node




    def insert_at_last(self,data):
        cur=self.start_node
        while cur.nref != None:
            cur=cur.nref
        new_node=Node(data)
        cur.nref=new_node
        new_node.pref=cur


    def display(self):
        cur=self.start_node
        while cur!=None:
            print(cur.item)
            cur = cur.nref

    def insert_after_item(self,data,value_in_list):
        cur=self.start_node
        while cur.item != value_in_list:
            cur=cur.nref
        new_node=Node(data)
        new_node.nref=cur.nref
        new_node.pref=cur
        cur.nref=new_node

    def insert_before_item(self,data,value_in_list):
        cur=self.start_node
        while cur.item != value_in_list:
            cur=cur.nref
        new_node=Node(data)
        new_node.pref=cur.pref
        new_node.nref=cur
        cur.pref=new_node
        new_node.pref.nref=new_node
        
        # check for indentation
    def delete_from_last(self):
        cur=self.start_node
        while cur.nref != None:
            cur=cur.nref
        cur.pref.nref=None
        cur.pref=None  
    
    def delete_from_start(self):
        cur=self.start_node
        second_element=cur.nref
        cur=cur.nref
        cur.pref=None
        self.start_node=cur        

my_list=DoublyLinkedList()
my_list.insert_in_empty("start")
my_list.insert_at_last("last1")
my_list.insert_at_last("last2")
my_list.insert_at_last("last3")
my_list.insert_at_last("last4")
my_list.insert_at_last("last5")
my_list.insert_at_last("last6")
my_list.insert_at_start('start4')
my_list.insert_at_start('start3')
my_list.insert_at_start('start2')
my_list.insert_at_start('start1')
my_list.display()

print()
print()
print()

my_list.insert_after_item("inserted afer last6","last6")
my_list.insert_after_item("inserted afer last4","last4")


my_list.insert_before_item("inserted before last6","last6")
my_list.insert_before_item("inserted before last3","last3")


my_list.display()



print()
print()
print()
my_list.delete_from_last()
my_list.delete_from_last()
my_list.delete_from_last()
my_list.display()
