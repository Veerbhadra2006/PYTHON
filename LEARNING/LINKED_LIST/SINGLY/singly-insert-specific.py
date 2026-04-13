class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
       
        
# creating the node
head = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)


# linking the node each other
head.next = node2
node2.next = node3
node3.next = node4


# creating a new node 
new_node = Node(80);


# Inserting a node after the second node
current = head
while current is not None and current.data != 20:
    current = current.next

new_node.next = current.next
current.next = new_node



# print the node
temp = head
while temp is not None:
    print(temp.data, end=" -> ")
    temp = temp.next
    
print("None")