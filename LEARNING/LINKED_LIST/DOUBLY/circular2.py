# 🔹 Node class (double pointer)
class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    # 🔹 Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        # case 1: empty list
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
            return

        last = self.head.prev  # last node

        # connect new node
        last.next = new_node
        new_node.prev = last

        new_node.next = self.head
        self.head.prev = new_node

    # 🔹 Forward traversal
    def forward(self):
        if self.head is None:
            return

        temp = self.head

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print("(back to head)")

    # 🔹 Backward traversal
    def backward(self):
        if self.head is None:
            return

        temp = self.head.prev  # last node

        while True:
            print(temp.data, end=" -> ")
            temp = temp.prev

            if temp == self.head.prev:
                break

        print("(back to last)")

    # 🔴 Delete at beginning
    def delete_beginning(self):
        if self.head is None:
            return

        # only one node
        if self.head.next == self.head:
            self.head = None
            return

        last = self.head.prev

        # update links
        self.head = self.head.next
        self.head.prev = last
        last.next = self.head

    # 🔴 Delete at end
    def delete_end(self):
        if self.head is None:
            return

        # only one node
        if self.head.next == self.head:
            self.head = None
            return

        last = self.head.prev
        second_last = last.prev

        # update links
        second_last.next = self.head
        self.head.prev = second_last