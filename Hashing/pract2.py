class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def getHash(self,key):
        total = 0
        for s in key:
            total+=ord(s)
        return total % self.MAX
    
    def __getitem__(self,key):
        pass

    def __setitem__(self,key,value):
        h = self.getHash(key)
        found =False
        for i , num in enumerate(self.arr[h]):
            if num[0] == key:
                self.arr[h][i]=(key,value)
                found = True 
                break
        if not found:
            self.arr[h].append((key,value))


t = HashTable()

t['march 6'] = 6
t['march 16'] = 16
t['march 26'] = 26

for i , num in enumerate(t.arr):
    print(i , " " , num , end="\n")

print("\n\n")

t['march 6'] = 100

for i , num in enumerate(t.arr):
    print(i , " " , num , end="\n")