import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder(root):
    if root:
        print(root.value),
        preorder(root.left)
        preorder(root.right)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value)

def insert(root,node):
    if root is None:
        root=node
    if root.value > node.value:
        if root.left==None:
            root.left=node
        else:
            insert(root.left,node)
    if root.value < node.value:
        if root.right==None:
            root.right=node
        else:
            insert(root.right,node)

def maximum(root):
    while root.right != None:
        root=root.right
    return(root.value)

def minimum(root):
    while root.left != None:
        root=root.left
    return (root.value)

root = Node(50)

for i in range(20):
    insert(root,Node(random.randint(0,100)))


print("\npreorder traversal is:")
preorder(root)


print("\ninorder traversal is:")
inorder(root)


print("\npostorder traversal is:")
postorder(root)



print("\nminimum element is",minimum(root))


print("\nmaximum element is",maximum(root))





