print("Stack")

class Stack :
    def __init__(self,maxSize):
        self.listt  = []
        self.maxSize = maxSize
    def pop(self):
        if self.listt == []:
            return "Empty"
        else :
            return self.listt.pop()
    
    def push(self,value):
        if len(self.listt) < self.maxSize:
            print(f"Value {value} is added")
            return self.listt.append(value) 
        else:
            print("Stack Overflow")
    
    def peek(self,value):
        return self.listt[-1]
    
    def isEmpty(self):
        if self.listt == []:
            return True
        else:
            return False
        
    def deleteStack(self):
        self.listt = []
    
    def disp(self):
        if self.listt == []:
            print("Empty Stack")
        for s in reversed(self.listt) :
            print(s)
        

stack = Stack(5)
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.push(60)
print("---------")
stack.disp()
