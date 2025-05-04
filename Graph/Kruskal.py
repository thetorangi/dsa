import DisjointSet as dst

class Graph :
    def __init__(self):
        self.nV = 0 
        self.graph = []
        self.nodes = []
        self.MST = []
        
    def addNode(self,node):
        self.nodes.append(node)
        self.nV+=1
        
    def addEdge(self,s,d,w):
        self.graph.append([s,d,w])
        
    def Kruskal(self):
        ds = dst.Disjoint(self.nodes)
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item:item[2])
        while e < self.nV -1 :
            s,d,w = self.graph[i]
            i+=1
            x = ds.find(s)
            y = ds.find(d)
            if x != y :
                self.MST.append([s,d,w])
                e+=1
                ds.union(s,d)
        for row in self.MST : print(row)
        
        

g = Graph()
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.addEdge("A", "B", 5)
g.addEdge("A", "C", 13)
g.addEdge("A", "E", 15)
g.addEdge("B", "A", 5)
g.addEdge("B", "C", 10)
g.addEdge("B", "D", 8)
g.addEdge("C", "A", 13)
g.addEdge("C", "B", 10)
g.addEdge("C", "E", 20)
g.addEdge("C", "D", 6)
g.addEdge("D", "B", 8)
g.addEdge("D", "C", 6)
g.addEdge("E", "A", 15)
g.addEdge("E", "C", 20)

g.Kruskal()


