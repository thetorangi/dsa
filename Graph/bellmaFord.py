class Graph:
    def __init__(self):
        self.graph = []
        self.nodes = []
        self.V = 0

    def addNode(self,node):
        self.nodes.append(node)
        self.V += 1

    def addEdge(self,s,d,w):
        self.graph.append([s,d,w])

    def bellmanFord(self,src): 
        dist = { i : float('inf') for i in self.nodes }
        dist[src]=0

        #calculating the distance untill V-1 relaxatation 
        for _ in range (self.V-1) :
            for s,d,w in self.graph :
                if dist[s] != float('inf') and dist[s] + w < dist [d]:
                    dist [d] = dist [s] + w
        
        #calculating the distance untill V^th relaxatation and comapring 
        for s,d,w in self.graph :
            if dist[s] != float('inf') and dist[s] + w < dist [d]:
                print("Negative Cycle Detected ! ") #if any distance reduced in V^th , then Negative Cycle is present for sure !
                return # return as futhur operations are useless 
        
        print(dist)


g = Graph()
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.addEdge("A", "C", 6)
g.addEdge("A", "D", 6)
g.addEdge("B", "A", 3)
g.addEdge("C", "D", 1)
g.addEdge("D", "C", 2)
g.addEdge("D", "B", 1)
g.addEdge("E", "B", 4)
g.addEdge("E", "D", 2)
g.bellmanFord("E")