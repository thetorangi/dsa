class Node:
    def __init__(self,value):
        self.value = value 
        self.next = Node

class LinkedList : 
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1
    
    def disp(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.value)
            temp_node = temp_node.next


ll = LinkedList()

ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

print(ll.length)
print(ll.head.value)
print(ll.tail.value)


print("\n ----- \n")
ll.disp()
print("\n ----- \n")