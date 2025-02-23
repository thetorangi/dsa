print("--- Circular Queue Without Start & End ---")

class Queue:
    def __init__(self , maxSize):
        self.items = []
        self.maxSize = maxSize

    def disp(self):
        if self.items == []:
            print("Empty Queue")
        else:
            for s in self.items:
                print(s , end=" ")

    

    def enqueue(self,value):
        if len(self.items) > self.maxSize:
            print("Queue is Full")
        else:
            self.items.append(value)
            print(f"Value {value} added to Queue")
    
    def dequeue(self):
        if self.items == []:
            print("Empty Queue")
        else:
            print(f"{self.items.pop(0)} is Removed")

queue = Queue(5)

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)


print("-------")
queue.disp()
print("-------")
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
print("-------")
queue.disp()
print("-------")