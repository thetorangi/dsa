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

    def insert(self,index,value):
        new_node = Node(value)
        if index < 0 :
            return False
        if self.length == 0 or index == 0 :
            self.prepend(value)
        elif self.length <= index :
            self.append(value)
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node=temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
            self.length+=1
        
    def search(self,value):
        if self.length == 0 :
            return "not Found"
        else:
            temp_node = self.head
            for _ in range(self.length):
                if temp_node.value == value :
                    return f"Found at index {_}"
                temp_node = temp_node.next
        return "not Foundd"


    def disp(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.value,end=" -> ")
            temp_node = temp_node.next


ll = LinkedList()

ll.append(10)
ll.append(40)
ll.prepend(90)
ll.append(102)
ll.insert(3,99)

print(ll.search(77))
print(ll.length)

print("\n ----- \n")
ll.disp()
print("\n ----- \n")