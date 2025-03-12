#let's Start Hashing 

dates = {}

class Hash:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def getHash(self,key):
        total = 0
        for s in key :
            total += ord(s)
        
        return total % self.MAX
    
    def __getitem__(self,key):
        h = self.getHash(key)
        for num in self.arr[h]:
            if num[0]==key:
                return num[1]

    def __setitem__(self,key,value):
        h = self.getHash(key)
        found = False
        for i , num in enumerate(self.arr[h]):
            if len(num) == 2 and num[0]==key:
                self.arr[h][i] = (key,value)
                found = True
        if not found:
            self.arr[h].append((key,value))
                
    
    def __delitem__(self,key):
        h = self.getHash(key)
        self.arr[h] = None


t = Hash()

t['march 6']=6
t['march 6']=100
t['march 26']=26
t['march 16']=16

for i , num in enumerate(t.arr):
    print(i,num,end="\n")


print(t['march 26'])
print(t['march 6'])
print(t['march 17'])