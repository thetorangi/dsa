print("Queue using Linked List")

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
class Queue :
    def __init__(self):
        self.ll = LinkedList()
    
    def enqueue (self,value):
        new_node = Node(value)
        if self.ll.head == None:
            self.ll.head = new_node
            self.ll.tail = new_node
            print("Value inserted At Head")
        else:
            self.ll.tail.next = new_node
            self.ll.tail = new_node
            print("Value inserted At Tail")

    def isEmpty(self):
        return False if self.ll.head else True
    
    def disp (self):
        if self.isEmpty():
            print("Empty Queue")
        else:
            temp = self.ll.head
            while temp :
                print(temp.value , end= " ")
                temp = temp.next

    def dequeue(self):
        if self.isEmpty():
            return "Empty Queue"
        elif self.ll.head == self.ll.tail :
            self.ll.head = self.ll.tail = None
        else:
            val = self.ll.head.value
            self.ll.head = self.ll.head.next
            return f"Removed {val} from Queue"

    def peek(self):
        if self.isEmpty():
            return "Empty Queue"
        else:
            return self.ll.head.value


queue = Queue()

queue.enqueue(10)

queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)

print("\n----------------")
queue.disp()
print("\n----------------\n")

queue.dequeue()
queue.dequeue()
queue.dequeue()

queue.enqueue(60)
queue.enqueue(70)
queue.enqueue(80)
queue.enqueue(90)
# queue.dequeue()
# queue.dequeue()

print("\n----------------")
queue.disp()
print("\n----------------\n")