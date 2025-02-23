print("Circular Doubly Linked List ")

class Node :
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None
    
class CDLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self,value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.head.prev = new_node   
            self.head.next = new_node
            self.tail.prev = new_node
            self.tail.next = new_node
        else:
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node
    
    def prepend(self,value):
        if not self.head:
            self.append(value)
        else:
            new_node =  Node(value)
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.head = new_node
    
    def insert(self,index,value):
        if index ==0 :
            self.prepend(value)
        else:
            temp = self.head
            for i in range(index-1):
                temp =temp.next
                if temp == self.tail and i == index-2:
                    return self.append(value)
                if temp == self.tail :
                    return "Index Out of range"
            new_node = Node (value)
            nxt = temp.next
            new_node.prev = temp
            new_node.next = nxt 
            temp.next = new_node
            nxt.prev = new_node
            return "Done"
        
    def popF(self):
        if not self.head:
            return "Empty"
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            value = self.head.value
            self.tail.next = self.tail.next.next
            self.head= self.head.next
            self.head.prev= self.tail
        return f"Value {value} is removed"

    def pop(self):
        if not self.head:
            return "Empty LL"
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            value = self.tail.value
            self.head.prev = self.head.prev.prev
            bfr = self.tail.prev
            bfr.next = self.head
            self.tail = bfr
        return f"Value {value} is removed"

    def delete(self,value):
        if not self.head :
            return "Empty LL"
        elif value == self.head.value :
            return self.popF()
        elif value == self.tail.value:
            return self.pop()
        else:
            temp = self.head
            while True:
                if value == temp.value:
                    nxt = temp.next
                    prv = temp.prev
                    nxt.prev = prv
                    prv.next = nxt
                    return f"Removed {value} sucessfully"
                temp=temp.next
                if temp == self.tail.next:
                    break
            return f"Value {value} not in List"
                
    def search(self,value):
        if not self.head :
            return "Empty LL"
        elif value == self.head.value :
            return "Found at Head"
        elif value == self.tail.value:
            return "Found At Tail"
        else:
            temp = self.head
            while True:
                if value == temp.value:
                    return f"Found {value} in LL"
                temp=temp.next
                if temp == self.tail.next:
                    break
            return f"Value {value} not in List"
    

    def disp(self):
        if not self.head:
            return "Empty"
        else:
            res=""
            temp = self.head
            while True:
                res+=str(temp.value)
                temp=temp.next
                if temp == self.tail.next:
                    break
                res+=" -> "
        return res
    

    #Trial test of CDLL
    def disp2(self):
        if not self.head:
            return "Empty"
        else:
            res=""
            temp = self.head
            n=7
            while n:
                res+=str(temp.value)
                temp=temp.next
                n-=1
                res+=" -> "
        return res
    
    def revDisp(self):
        if not self.head:
            return "Empty"
        else:
            res=""
            temp = self.tail
            while True:
                res+=str(temp.value)
                temp=temp.prev
                if temp == self.head.prev:
                    break
                res+=" -> "
        return res
    
    def deleteLL(self):
        if not self.head:
            return "Empty LL"
        else:
            self.head = None
            self.tail = None
            return "Doneee"
        
cdll = CDLL()

cdll.prepend(21)
cdll.append(10)
cdll.append(20)
cdll.append(30)
cdll.prepend(70)
print("---Straight---")
print(cdll.disp())
print(cdll.deleteLL())
print(cdll.disp())
# print(cdll.search(21))
# print("---Reverse---")
# print(cdll.revDisp())