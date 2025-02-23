print("Circular LinkedList \n")

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
            self.tail.next = new_node
        else:
            self.tail.next = new_node
            self.tail=new_node
            new_node.next = self.head
    
    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
            self.tail.next = new_node
        else:
            new_node.next = self.head
            self.tail.next=new_node
            self.head = new_node

    def ins(self,index,value): # 0 for inserting at first -1 for inserting at last
        if index == 0 :
            self.prepend(value)
            return "done"
        elif index == -1:
            self.append(value)
            return "done"
        else:
            new_node = Node(value)
            temp=self.head
            for i in range(index-1):
                temp = temp.next
            new_node.next = temp.next
            temp.next =new_node
        
    def trav(self):
        if self.head is None:
            return "Empty List"
        else:
            temp = self.head
            while temp.next :
                print(temp.value,end=" -> ")
                temp =temp.next
                if temp == self.head:
                    break
                
    def search(self,value):
        if self.head is None:
            return "Empty List"
        else:
            temp = self.head 
            while temp.next:
                if temp.value == value:
                    return f"Value {value} found"
                temp=temp.next
                if temp ==self.tail.next:
                    break
            return f"Value {value} not found"

    def delete(self,value):
        if value == self.head.value:
            self.popF()
            return "Hogaya"
        elif value == self.tail.value:
            self.pop()
        else:
            temp = self.head
            while temp.next:
                if temp.next.value == value:
                    break
                temp=temp.next
                if temp.next == self.head :
                    return "Not Found"
            temp.next=temp.next.next
            return "Done"
        return "Not Found"
    
    def popF(self):
        if self.head is None:
            return "Empty"
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head=self.head.next
            self.tail.next = self.tail.next.next      
            return "Done"

    def pop(self):
        if self.head is None:
            return "Empty"
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next:
                if temp.next == self.tail:
                    break
                temp=temp.next
            self.tail=temp
            temp.next=temp.next.next
        return "Done"
    

cll = CSLinkedList()

cll.append(10)
cll.append(20)
cll.append(30)
cll.append(40)
cll.prepend(90)
cll.prepend(100)

# cll.ins(2,25)
# cll.insert(3,25)

# print(cll.delete(10))

print("")

cll.trav()
print("")
# cll.pop()
# cll.pop()
# cll.pop()
# cll.pop()
print(cll.delete(40))
# cll.popF()
print("After")
print(cll.trav())
# print(cll.search(10))

