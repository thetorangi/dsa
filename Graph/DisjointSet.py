class Disjoint:
    def __init__(self,vertices):
        self.vertices = vertices
        self.parent = {}
        self.rank = {}
        self.nV = 0 
        for p in vertices:
            self.parent[p] = p
            self.rank[p] = 0 
            self.nV+=1
        
    def find(self,item):
        if self.parent[item] == item :
            return item
        else :
            return self.find(self.parent[item])
    
    def union(self , a , b):
        xroot = self.find(a)
        yroot = self.find(b)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] +=1