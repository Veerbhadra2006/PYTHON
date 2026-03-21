class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
# creating a nodes 
node1 = Node(10);
node2 = Node(20);
node3 = Node(30);
node4 = Node(40);
node5 = Node(50);
node6 = Node(60);
node7 = Node(70);
node8 = Node(80);
node9 = Node(90);
node10 = Node(100);



# connecting a nodes each other to form a singly linkd list
node1.next = node2;
node2.next = node3;
node3.next = node4;
node4.next = node5;
node5.next = node6;
node6.next = node7;
node7.nex = node8;
node8.next = node9;
node9.next = node10;


# printing the singly linked list

current = node1;
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
    
print("NONE")
