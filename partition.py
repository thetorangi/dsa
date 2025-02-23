class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None

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
    
    def prepend(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1



            



    def disp(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.value,end=" -> ")
            temp_node = temp_node.next
    
ll = LinkedList()

ll.append(70)
ll.append(20)
ll.append(60)
ll.append(30)
ll.append(40)
ll.append(50)
ll.append(10)

print("------")

ll.disp()

ll.sortt(40)

print("------")

ll.disp()