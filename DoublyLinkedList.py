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
            print("Node added succesfully to empty Linked list")
        else:
            print("List not empty")
    def insert_at_last(self,data):
        cur=self.start_node
        while cur.nref != None:
            cur=cur.nref
        new_node=Node(data)
        cur.nref=new_node
        new_node.pref=cur
        print("Node added succesfully to Linked list")

    def insert_at_start(self,data):
        new_node=Node(data)
        new_node.nref=self.start_node
        self.start_node.pref=new_node
        self.start_node=new_node

    def display(self):
        cur=self.start_node
        while cur.nref!=None:
            cur=cur.nref
            print(cur.item)

    def insert_after_item(self,data,value_in_list):
        # data  is input data in new node
        # value is already existing value in the list
        print("I am inside insert_after_item function")
        cur=self.start_node
        if cur.item is not value_in_list:
            print("I am inside insert_after_item function if part")
            cur=cur.nref


            new_node=Node(data)

            new_node.nref=cur.nref
            new_node.pref=cur
            cur.nref=new_node



my_list=DoublyLinkedList()



my_list.insert_in_empty('first')
my_list.insert_at_last(2)
my_list.insert_at_last(3)
my_list.insert_at_last(4)
#my_list.insert_at_last('last')



print()
print()
my_list.display()
my_list.insert_after_item('data to be inserted after last','last')



print()
print()
my_list.display()
