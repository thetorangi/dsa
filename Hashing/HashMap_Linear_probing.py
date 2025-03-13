class HashTable:
    def __init__(self):
        self.MAX = 4
        self.arr = [None] * self.MAX
        self.DELETED = "DELETED"
    
    def getHash(self,key):
        total = 0
        for x in key:
            total+=ord(x)
        return total % self.MAX

    def __setitem__(self,key,value):
        h = self.getHash(key)
        x = h
        while True:
            if not self.arr[h] or self.arr[h] == self.DELETED :
                self.arr[h] = [key,value]
                return "Done"
            if self.arr[h][0] == key:
                self.arr[h][1] = value
                return "Updated"
            h = ( h+1 ) % self.MAX
            if h == x :
                break
        print("Table is Full ")
        return

    def display(self):
        for i , num in enumerate(self.arr):
            if num :
                print(f"{i} -> {self.arr[i][0]} = {self.arr[i][1] }")
            else:
                print(f"{i} is Empty")
            
    def __getitem__(self,key):
        h = self.getHash(key)
        x = h
        while self.arr[h] is not None :
            if self.arr[h][0] == key :
                return self.arr[h][1]
            h= (h +1)%self.MAX
            if h == x:
                break
        return "not Found"

    def __delitem__(self,key):
        h = self.getHash(key)
        x = h
        while self.arr[h]:
            if self.arr[h][0] == key :
                x = self.arr[h]
                self.arr[h] = self.DELETED
                return f"Deleted {x}"
            h= (h +1)%self.MAX
            if h == x:
                break
        return "not Found"

t = HashTable()

t['Rohit'] = 45
t['Virat'] = 18
t['MSD'] = 7
t['Pant'] = 17 


t.display()

del t["Pant"]

print("\n\n---\n\n")

t['KL Rahul'] = 1

t.display()

