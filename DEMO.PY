class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data 
        self.next = None
        

class doublylinkedlist:
    def __init__(self):
        self.head = None
        
        
    def insert(self , data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while
    
    
    
    
    
    
    
    
    class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # insert at end
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    # forward traversal
    def forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # backward traversal
    def backward(self):
        temp = self.head

        # go to last node
        while temp.next:
            temp = temp.next

        # traverse backward
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.prev
        print("None")