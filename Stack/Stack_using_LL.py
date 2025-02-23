print("Stack using Linked List")

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

class Stack:
    def __init__(self):
        self.ll = LinkedList()

    def push(self,value):
        new_node = Node(value)
        new_node.next = self.ll.head 
        self.ll.head = new_node
    
    def peek(self):
        print(self.ll.head.value)

    def pop(self):
        if self.ll.head == None:
            print("Empty Stack")
        else:
            print(f"Removed Element is {self.ll.head.value}")
            self.ll.head = self.ll.head.next
            
    def disp(self):
        if not self.ll.head:
            print("Empty Stack")
        temp = self.ll.head
        while temp :
            print(temp.value)
            temp = temp.next


stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

stack.disp()
print("--------")

stack.peek()

print("--------")    
stack.disp()
print("--------")
