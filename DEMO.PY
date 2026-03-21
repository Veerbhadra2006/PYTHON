class Node:
    def __init__(self, data ):
        self.data = data
        self.next = None
        
# creatign a node
node1 = Node(50)
node2 = Node(40)
node3 = Node(30)
node4 = Node(20);
node5 = Node(10);


# coonecting / link list to each other to from a singly linked list

node1.next = node2;
node2.next = node3;
node3.next = node4;
node4.next = node5;


# adding ne node in singly linked list ----- inserting node at the begining
head = node1;
new_node = Node(90)
new_node.next = node1;
head = new_node;



# printig the nodes singly liked list 
current = head;
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
    
print("NONE") 