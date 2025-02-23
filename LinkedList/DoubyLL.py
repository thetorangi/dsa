print("Doubly LinkedList \n")

class Node:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node 
            node = node.next
        
    def prepend(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = None
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        return "Done"
    
    def append(self,value):
        if self.head == None:
            self.prepend(value)
        else:
            new_node = Node(value)
            new_node.next = None
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        return "Done"
    
    def insert(self,index,value):
        new_node = Node(value)
        temp = self.head
        for i in range(index-1):
            temp = temp.next
        new_node.prev = temp
        new_node.next = temp.next
        new_node.next.prev=new_node
        temp.next = new_node
        return "done"

    def disp(self):
        if self.head == None:
            return "Empty"
        else:
            res = ""
            temp = self.head
            while temp:
                res+=str(temp.value)
                temp = temp.next
                if not temp:
                    break
                res+=" -> "
            return res
        
    def search(self,value):
        if self.head is None:
            return "Empty List"
        else:
            temp = self.head
            while temp:
                if temp.value == value :
                    return "Value found"
                temp = temp.next
            return "Value Not found"
    
    def dispR(self):
        if self.tail == None:
            return "Empty"
        else:
            res = ""
            temp = self.tail
            while temp :
                res+=str(temp.value)
                temp=temp.prev
                if not temp:
                    break
                res+=" -> "
            return res

    def delALL(self):
        if self.head is not None:
            temp = self.head
            while temp:
                temp.prev = None
                temp = temp.next
            self.head = None
            self.tail = None
            return "Done"
        return "Nahi hua"
        
    def delete(self,value):
        if self.head is None:
            return "Empty list"
        if self.head == self.tail:
            self.head = self.tail = None
        elif self.head.value == value :
            self.head = self.head.next
            self.head.prev = None
            return "Done"
        elif self.tail.value == value:
            self.tail = self.tail.prev
            self.tail.next = None
            return "OKKK"
        else:
            temp = self.head
            while temp :
                if temp.value == value:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    return "Done"
                temp = temp.next
            return "Value not found"
        

dll = DLL()

dll.append(10)
dll.append(100)
dll.prepend(90)
dll.prepend(100)


# print(dll.delete(90))

# print(dll.disp())

# print(dll.delete(20))
# print(dll.disp())

# print(dll.delete(100))
# print(dll.disp())

# print(dll.delete(10))
print(dll.disp())
# print(dll.head.value)
# print(dll.delete(20))
# print(dll.delete(100))

# print(dll.delete(100))
# print(dll.delete(100))
# print(dll.delete(90))
# print(dll.delete(20))

print(dll.delALL())
print(dll.delALL())


print(dll.dispR())
print(dll.disp())


print([node.value for node in dll])
