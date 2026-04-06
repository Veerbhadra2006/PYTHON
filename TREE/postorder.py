class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value
        
#inserting the node in the binary tree form of POST ORDER STRUCUTRE
def postOrder(root):
    if (root != None):
        postOrder(root.left)
        postOrder(root.right) 
        print(root.data, end=" ")
       
#input value in the node 
root = Node(1)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(8)
        
# call the function to disply the elements from the binary tree
postOrder(root)