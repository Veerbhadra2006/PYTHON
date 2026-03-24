class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None


    # ------------**       INSERT AT THE BEGINNING      ---------------------**
    def insertBeginning(self, data):
        new_node = Node(data)

        # case 1 - if head is none
        if self.head is None:
            self.head = new_node
            return

        # case 2 - if head already exists
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node






    # ------------**       INSERT AT THE ENDING      ---------------------**
    def insertEnd(self, data):
        new_node = Node(data)
            
        if self.head is None:
            self.head = new_node
            return
            
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        
        temp.next = new_node
        new_node.prev = temp


    # traversing
    def forword(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# function call
obj = DoublyLinkedList()


obj.insertEnd(10)
obj.insertEnd(20)
obj.insertEnd(30)
obj.insertEnd(40)
obj.insertEnd(5)


obj.insertBeginning(50)
obj.insertBeginning(90)


obj.forword()
