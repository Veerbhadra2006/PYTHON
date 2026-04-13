#circular linked list - singly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_ending(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=" --> ")
            temp = temp.next
            if temp == self.head:
                break
        print("back to head")
        
        
    

obj = CircularLinkedList()

obj.insert_ending(10)
obj.insert_ending(20)
obj.insert_ending(30)
obj.insert_ending(40)
obj.insert_ending(50)

obj.display()