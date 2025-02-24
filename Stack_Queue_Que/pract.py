class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.minVal = value

class MinStack:

    def __init__(self):
        self.head = None        

    def push(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.head.minNext = val
        else:
            new_node.minVal = min(self.head.minVal , val)
            new_node.next = self.head
            self.head = new_node
            
    def pop(self) -> None:
        if not self.head :
           return False
        else :
           self.head = self.head.next
        

    def top(self) -> int:
        return self.head.value if self.head else None

    def getMin(self) -> int:
        return self.head.minVal if self.head else None
        
queue = MinStack()


print(queue.pop())
# queue.push(5)
# print(queue.head.value)
# print(queue.head.minVal)
# queue.push(10)
# print(queue.head.value)
# print(queue.head.minVal)
# queue.push(3)
# print(queue.head.value)
# print(queue.head.minVal)
