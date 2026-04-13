class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.items = [None] * size      #size fix ho rahi hai...
        self.front = -1
        self.rear = -1

    # ----------------------- check empty --------------------------------
    def is_empty(self):
        return self.front == -1

    # ----------------------- check full --------------------------------
    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    # ----------------------- insert element --------------------------------
    def enqueue(self, value):
        if self.is_full():
            print("Queue is full")

        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.items[self.rear] = value

    # ----------------------- delete element --------------------------------
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")

        value = self.items[self.front]

        # only one element
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

    # ----------------------- display queue --------------------------------
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return

        i = self.front
        while True:
            print(self.items[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()


# ----------------------- Testing --------------------------------

obj = CircularQueue(5)

obj.enqueue(10)
obj.enqueue(20)
obj.enqueue(30)
obj.enqueue(40)
obj.enqueue(50)

obj.display()

obj.dequeue()

obj.display()