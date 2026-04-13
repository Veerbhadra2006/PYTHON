class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

# inserting the element i the BST - binary search Tree
def insert(root, value):
    if root == None:
        return Node(value)
    if root.data == value:
        return root
    if value < root.data:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

# Searhing the  element in BINARY SEARCH TREE
def search(root, value):
    if root is None:
        print("\n Element was not found")
        return
    
    if root.data == value:
        print("\n Element was found")
        return
    
    if value < root.data:
        search(root.left, value)
    else:
        search(root.right, value)

#Print function to display the node
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

# input the value in node
root = insert(None, 20)
root = insert(root, 15)
root = insert(root, 30)
root = insert(root, 40)
root = insert(root, 12)
root = insert(root, 18)
root = insert(root, 25)
root = insert(root, 50)

# call print fucntion to display the node/ element
inorder(root)

# searchig the 30 element in the Binary search Tree 
search(root,100)