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


t = HashTable()

t['March 9'] = 120
t['March 9'] = 125

print(t.arr)
        