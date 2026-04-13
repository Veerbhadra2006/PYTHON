class stack:
    def __init__(self):
        self.s = []
        
    # find length
    def length(self):
        return len(self.s)
    
    # insert element
    def push(self,value):
        self.s.insert(0, value)
      
    # check length is empty  
    def peek(self):
        if len(self.s) == 0:
            raise Exception("Stack is Empty")
        return self.s[0]
    
    # delete the element
    def pop(self):
        if len(self.s) == 0:
            raise Exception("Stack is Empty")
        return self.s.pop(0)
    
    def stackPrint(self):
        for x in self.s:
            print(x, end=" ")
            

obj = stack()

obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
obj.push(50)
obj.push(60)
obj.push(70)


obj.stackPrint()
print("\n\nPOP Element is :",obj.pop(),"\n")

obj.stackPrint()