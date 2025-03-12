class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
    
    def getHash(self,key):
        return sum([ord(x) for x in key]) % self.MAX

    def __setitem__(self,key,value):
        h = self.getHash(key)
        found = False
        for i , num in enumerate(self.arr[h]):
            if len(num)==2 and num[0]==key:
                self.arr[i][h]=(key,value)
                found = True
                break
        if not found:
            self.arr[h].append((key,value))
        
    def __getitem__(self,key):
        h = self.getHash(key)
        for i , num in enumerate(self.arr[h]):
            if num[0]==key:
                return num[1]
    
    def __delitem__(self,key):
        h = self.getHash(key)
        for i , num in enumerate(self.arr[h]):
            if num[0]==key:
                del self.arr[h][i]




t = HashTable()

t['march 6'] = 120
t['march 17'] = 126
t['march 19'] = 125


for i , num in enumerate(t.arr):
    print(i  , " " , num)


del t['march 17']


print(f"\nAfter Deletion \n")

for i , num in enumerate(t.arr):
    print(i  , " " , num)