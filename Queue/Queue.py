print("---Queue---")

class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self,value):
        self.items.append(value)
        print(f"Value {value} added")
    
    def dequeue(self):
        if self.items == []:
            print("empty Queue")
        else:
            print("removed " , self.items.pop(0))

    def disp(self):
        if self.items == []:
            print("Empty Queue")
        else:
            for s in self.items:
                print(s , end=" ")
        
    def peek(self):
        if self.items == []:
            print("Empty Queue")
        else:
            print("Peek is " , self.items[0])

queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)

queue.disp()

print("---------")
queue.peek()
queue.dequeue()
queue.dequeue()
queue.dequeue()

queue.disp()


print()