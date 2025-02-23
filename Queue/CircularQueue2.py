print("---Circular Queue using Front & Rear ---")

class Queue :
    def __init__(self,maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize 
        self.start = -1
        self.top = -1
    
    def isFull(self):
        if self.start == (self.top +1)% self.maxSize and self.items[self.start] != None :
            return True
        else:
            return False
    
    def isEmpty(self):
        if self.top == self.start == -1:
            return True
        if self.items[self.start] == None:
            return True
        else:
            return False
    
    def disp (self):
        if self.isEmpty():
            print("Empty Queue ")
        else:
            for s in self.items:
                print(s , end="  ")
    

    def enqueue(self,value):
        if self.isFull():
            print( "Queue is Full ")
        else:
            if self.start == -1:
                print("Once")
                self.start = 0
                self.top = 0
                self.items[self.start] = value
            else:
                print("Added")
                self.top = (self.top +1 )  % self.maxSize
                self.items[self.top] = value
    def dequeue(self):
        if self.isEmpty():
            print( "Empty Queue")
        else:
            if self.start == self.top:
                print(self.items[(self.start)] , "Removed")
                self.items[self.start] = None
                self.top = (self.top +1 ) %self.maxSize
                self.start = (self.start +1 ) %self.maxSize
            else:
                print(self.items[self.start] , "Removed")
                self.items[self.start] = None
                self.start =( self.start + 1 )%self.maxSize

queue = Queue(5)

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)

print("\n-------------------\n")
queue.disp()
print("\n-------------------\n")
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()


print("\n-------------------\n")
queue.disp()
print("\n-------------------\n")

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
# queue.enqueue(50)

print("\n-------------------\n")
queue.disp()
print("\n-------------------\n")



print("\n")