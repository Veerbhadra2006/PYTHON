# FULL DOUBLY LINKED LIST- ALL OPERATION IMPLEMENTED 
# INSERT - BEGINNING , ENDING , SPECIFIC POSITION , 
# DELETE - BEGINNING , ENDING , SPECIFIC POSITION
# TRAVERSING - FORWORD , BACKWORD


class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None
        
# created a head node
class doubly_linked_list:
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
        
        if self.head is None:  # FIX: empty list -> new node becomes head
            self.head = new_node
            return
        
        temp = self.head
        while temp.next is not None:
            temp = temp.next
            
        temp.next = new_node
        new_node.prev = temp
        
    def insert_position(self, data, position):
        new_node = Node(data)
        
        if position == 0:  # FIX: position 0 should insert at beginning
            self.insert_beginning(data)
            return
        
        if self.head is None:
            print("List is empty")  # FIX: cannot insert at position if list is empty
            return
        
        temp = self.head
        count = 0 
        while temp is not None and count < position - 1:
            temp = temp.next 
            count = count + 1
        
        if temp is None:
            print("List is empty")
            return 
        if temp.next is None:  # FIX: inserting at end
            temp.next = new_node
            new_node.prev = temp
            return
        new_node.next = temp.next
        temp.next.prev = new_node
        temp.next = new_node
        new_node.prev = temp  # FIX: set prev for middle insert
        
    
    def  delete_beginning(self):
        if self.head is None:   
            print("list is empty");
            return
        
        if self.head.next is None:  # FIX: single node list
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None
        
    def delete_ending(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:  # FIX: single node list
            self.head = None
            return
        
        temp = self.head
        while temp.next is not None:
            temp = temp.next
            
        temp.prev.next = None
        
    def delete_position(self, position):
        if self.head is None:
            print("List is empty")
            return
        if position == 0:  # FIX: delete head
            self.delete_beginning()
            return
        
        temp = self.head  # FIX: start from head
        count = 0 
        
        while temp is not None and count < position:
            temp = temp.next  # FIX: move to next node
            count = count + 1  # FIX: increment count
            
        if temp is None:
            print("List is empty")
            return
        
        # agar temp (current) ponintng node next none hai to temp ke pahale wale node ke prev mein yo store hai usko none kar do taki last node se connection tut jaye and finally node delte ho jaye
        if temp.next is None:
            temp.prev.next = None
        # agar agar nodes hain and hum biche mein hai - node delete karna hai temp ke prev ke next mein temp ke next mean temp ke aage wale node ki value store ho jayegi , and temp ke aage wale node mein temp ke piche wale node ki value store ho jayegi jisse temp se saree connection tut jayenge and temp delete ho jayega
        else:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
        
        
    # forword traverse (FIX: moved to class scope)
    def forword(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end = " --> ")
            temp = temp.next
        print("None")
        
    
    def backword(self):
        temp = self.head
        if temp is None:  # FIX: empty list check
            print("None")
            return
        while temp.next is not None:
            temp = temp.next
        
        while temp is not None:
            print(temp.data, end=" <-- ")
            temp = temp.prev
        print(None)      
        
    
# obj created (FIX: moved out of class/method)

obj = doubly_linked_list()

obj.insert_ending(20)
obj.insert_ending(30)
obj.insert_ending(40)
obj.insert_ending(50)

obj.insert_beginning(5)

obj.insert_position(90,2)

obj.forword()

obj.delete_beginning()
obj.delete_ending()
obj.delete_position(3)


obj.forword()
obj.backword()
