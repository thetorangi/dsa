class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.next = None
        self.length=0
    
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
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1

    def pop(self):
        if self.length == 0 :
            return "Empty"
        else:
            temp=self.head
            for i in range(self.length-1):
                temp=temp.next
            self.tail = temp
            temp.next=None
            self.length-=1

    def disp(self):
        temp = self.head
        while temp:
            print(temp.value,end=" -> ")
            temp=temp.next
        
ll = LinkedList()

ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
ll.append(60)
ll.prepend(9)


print(ll.length)

ll.disp()

ll.pop()


print(ll.length)

ll.disp()