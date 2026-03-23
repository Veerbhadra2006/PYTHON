class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None
        
# creating a node
head = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)


# linking the node
head.next = node2
node2.prev = head
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3



# traversing 


print("\nForword Traversing")

current = head
while current is not None:
    print(current.data , end=" -> ");
    current = current.next
print("None")
    
    
    
print("\n\n Backword Traversing")

current = head;
while current.next is not None:
    current = current.next
    
while current is not None:
    print(current.data , end=" -> ")
    current = current.prev
print("None")
    
# current = node4
# while current is not None:
#     print(current.data, end=" -> ")
#     current = current.prev
# print("None")