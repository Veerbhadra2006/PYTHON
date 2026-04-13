class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value
        
#insertin the elemnent in the BST
def insert(root , value):
    if root == None:
        return Node(value)
    if root.data == value:
        return root
    if value < root.data:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

#searching the element in binary serch tree
def search(root, value):
    if root is None:
        print("element was not foundd"
              return 