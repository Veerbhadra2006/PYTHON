#BINARY SEARCH TREE - ALL 3 CASE IMPLEMENTED  AND ALL OPERATION PERFORM LIKE: INSERTING , SEARCHING , DELETING , PRITING , ETC

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

#inserting the element in the BST
def insert(root, value):
    if root == None:
        return Node(value)
    if root.data == value:
        return root 
    if value < root.data:
        root.left = insert(root.left , value)
    else:
        root.right = insert(root.right, value)
    return root

#Searching the element in binary search tree
def search(root, value):
    if root is None:
        print("\n Element was not found")
        return False
    if root.data == value:
        print("\n Element was found")
        return True
    if value < root.data:
        return search(root.left, value)
    else:
       return search(root.right, value)
  
#get successor value      
def get_succ(root):
    root = root.right
    while (root != None and root.left != None):
        root = root.left
    return root


#delting the node / element in the binary search tree
def delete(root, value):
    if root == None:
        return None
    if value < root.data:
        root.left = delete(root.left, value)
        return root
    elif value > root.data:
        root.right = delete(root.right, value)
        return root
    else:
        if(root.left == None):
            return root.right
        if(root.right == None):
            return root.left
        else:
            succ = get_succ(root)
            root.data = succ.data
            root.right = delete(root.right, succ.data)
        return root
        
# inorder function --> to display the element 
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
        
#input the value in the node
root = insert(None , 20)
root = insert(root , 15)
root = insert(root , 30)
root = insert(root , 40)
root = insert(root , 12)
root = insert(root , 18)
root = insert(root , 25)
root = insert(root , 50)

#call print function to display the node / element
inorder(root)

#searching the 30 element in th Binary search tree
search(root, 30)


#deleting the 12 element in the binary search tree
root = delete(root, 12)

#call print function to display the node / element
inorder(root)
