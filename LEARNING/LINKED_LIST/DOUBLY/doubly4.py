class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoublyLinkedlist:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_ending(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def insert_specific(self, data, position):
        new_node = Node(data)
        if self.head is None:
            self.insert_beginning = new_node
            return

        temp = self.head
        idx = 0

        while temp is not None and idx < position - 1:
            temp = temp.next
            idx = idx + 1

        if temp is None:
            print("Position you entered is out of range")
            return

        new_node = Node(data) 
        new_node.next = temp.next
        new_node.prev = temp
        temp.next.prev = new_node
        temp.next = new_node

    def forword(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" --> ")
            temp = temp.next
        print("None")

    def backword(self):
        temp = self.head
        if temp is None:
            print("None")
            return

        while temp.next is not None:
            temp = temp.next

        while temp is not None:
            print(temp.data, end=" <-- ")
            temp = temp.prev
        print("None")


obj = DoublyLinkedlist()

obj.insert_beginning(5)
obj.insert_beginning(6)

obj.insert_ending(20)
obj.insert_ending(30)
obj.insert_ending(40)
obj.insert_ending(50)
obj.insert_ending(60)

obj.insert_specific(101, 4)
obj.insert_specific(90, 2)



obj.forword()
obj.backword()
