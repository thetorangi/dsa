#dijkstra Algorithm 
from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes=set()
        self.edges=defaultdict(list)
        self.distance={}

    def addNode(self,node):
        self.nodes.add(node)
    
    def addEdge(self,fromNode,toNode,dist):
        self.edges[fromNode].append(toNode)
        self.distance[(fromNode,toNode)]=dist


customGraph = Graph()
customGraph.addNode("A")
customGraph.addNode("B")
customGraph.addNode("C")
customGraph.addNode("D")
customGraph.addNode("E")
customGraph.addNode("F")
customGraph.addNode("G")
customGraph.addEdge("A", "B", 2)
customGraph.addEdge("A", "C", 5)
customGraph.addEdge("B", "C", 6)
customGraph.addEdge("B", "D", 1)
customGraph.addEdge("B", "E", 3)
customGraph.addEdge("C", "F", 8)
customGraph.addEdge("D", "E", 4)
customGraph.addEdge("E", "G", 9)
customGraph.addEdge("F", "G", 7)

print("Nodes : ")
print(customGraph.nodes)

print("\nEdges : ")
print(customGraph.edges)

print("\nDistance : ")
print(customGraph.distance)