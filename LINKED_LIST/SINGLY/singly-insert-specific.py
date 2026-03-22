class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# creating the node
node1 = Node(10);
node2 = Node(20);
node3 = Node(30);
node4 = Node(40);

# linked node
node1.next = node2;
node2.next = node3;
node3.next = node4;


# creating the node
new_node = Node(80)


# insert node after the second node

current = node1
while current is not None and current.data != 20:
    current = current.next

new_node.next = current.next
current.next = new_node


# printing the linked list
temp = node1
while temp is not None:
    print(temp.data, end=" -> ")
    temp = temp.next

