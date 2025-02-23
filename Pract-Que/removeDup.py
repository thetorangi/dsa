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
        
    def removeDup(self):
        temp = self.head
        item = set([temp.value])
        while temp.next:
            if temp.next.value in item :
                temp.next = temp.next.next
            else:
                item.add(temp.next.value)
                temp = temp.next
        return item

    def remDup(self):
        curr = self.head
        while curr:
            nxt = curr
            while nxt.next:
                if curr.value == nxt.next.value :
                    nxt.next = nxt.next.next
                else:
                    nxt = nxt.next
            curr = curr.next

    #return Nth from Last Using List
    def retN(self,idx):
        lst = []
        temp = self.head
        while temp:
            lst.append(temp.value)
            temp= temp.next
        if idx<=0 or idx > len(lst):
            return "Index Out of Range"
        return lst[len(lst)-idx]

    #return Nth from Last Without Using any other
    def retN2(self,idx):
        ptr1 = self.head
        ptr2 = self.head
        for i in range(idx):
            if ptr2 is None :
                return None
            ptr2 = ptr2.next
        
        while ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1.value

ll = LinkedList()

ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
ll.append(60)
ll.append(70)

ll.disp()

print("\nReturnd value is ",end="")
print(ll.retN(7))


print("\nReturnd value is ",end="")
print(ll.retN2(7))
