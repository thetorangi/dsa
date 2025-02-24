print("---Circular Queue using Front & Rear ---")

class Queue :
    def __init__(self,maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize 
        self.start = -1
        self.top = -1
    
    def isEmpty(self):
        if self.top == -1 :
            return True
        else:
            return False
    
    def isFull(self):
        if self.start == (self.top+ 1) % self.maxSize :
            return True
        else:
            return False
    
    def enqueue(self,value):
        if self.isFull():
            return "Queue is Full"
        else:
            self.top = (self.top + 1) % self.maxSize
            if self.start == -1 :
                self.start = 0
            self.items[self.top] = value
            return f"Value {value} is added"
        
    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty "
        else:
            val = self.items[self.start]
            self.items[self.start] = None
            if self.start == self.top :
                self.start = -1
                self.top = -1
            else:
                self.start= (self.start + 1 ) % self.maxSize
            return f"Value {val} is removed"
            
    def peek(self):
        if self.isEmpty():
            return "Empty Queue"
        else:
            return f"Peek element is {self.items[self.start]}"
    
    def disp (self):
        print(self.items)
    

queue = Queue(5)

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.enqueue(60)

print("----------------")

queue.disp()

print("----------------")

queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.enqueue(60)
queue.enqueue(70)
queue.enqueue(80)
queue.enqueue(90)

queue.dequeue()
queue.disp()

print(queue.peek())