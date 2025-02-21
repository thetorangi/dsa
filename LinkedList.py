print("Linked List")

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

    def get(self,index):
        if index == 0 :
            return self.head.value
        elif index > self.length-1 or index < 0 :
            return "Index out of Range"
        else:
            temp_node = self.head
            for i in range(index):
                temp_node = temp_node.next
            return temp_node.value

    def set(self,index,value):
        if index == 0 :
            self.head.value = value
            return True
        elif index > self.length-1 or index < 0 :
            return False
        else:
            temp_node = self.head
            for i in range(index):
                temp_node = temp_node.next
            temp_node.value = value
            return True
        
    def popF(self):
        if self.length == 0:
            return "Empty LL"
        else:
            self.head = self.head.next
            self.length-=1
            return True
        
    def pop(self):
        if self.length == 0 :
            return "Empty LL"
        if self.length == 1 :
            self.head = self.head.next
            self.length-=1
            return "done"
        else:
            pop_node = self.tail
            temp_node = self.head 
            for i in range(self.length-2):
                temp_node = temp_node.next
            self.tail = temp_node
            temp_node.next = None
            self.length-=1
            return pop_node.value
        
    def remove(self,index):
        if index == 0 :
            self.popF()
            return "Done"
        if self.length == 0 :
            return "empty LL"
        elif index > self.length or index < 0 :
            return "Index Out of Range"
        else:
            temp_node=self.head
            for i in range(index-1):
                temp_node = temp_node.next
            x = temp_node.next
            temp_node.next = temp_node.next.next
            return x.value


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

# print(ll.search(77))
print(ll.length)

print("\n -----")
ll.disp()
print("\n")

# print(ll.remove(0))
print(ll.remove(4))


print( ll.length)
print("\n -----")
ll.disp()
print("\n")

