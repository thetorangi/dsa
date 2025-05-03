import heapq

#class for Edge

class Edge:
    def __init__(self,dist,fromNode,toNode):
        self.start_vertex = fromNode
        self.end_vertex = toNode
        self.weight = dist

#class for Nodes

class Node:
    def __init__(self,name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.neighbours = []
        self.min_dist = float('inf')

    def __lt__(self,otherNode):
        return self.min_dist < otherNode.min_dist

    def add_edge(self,dist,toNode):
        edge = Edge(dist,self,toNode)
        self.neighbours.append(edge)

class Dijkstra:
    def __init__(self):
        self.heap = []

    
    def calculate(self,startVertex):
        startVertex.min_dist = 0 
        heapq.heappush(self.heap,startVertex)
        while self.heap:
            actualVertex = heapq.heappop(self.heap)
            if actualVertex.visited:
                continue
            for edge in actualVertex.neighbours:
                start = edge.start_vertex
                end = edge.end_vertex
                new_dist = start.min_dist + edge.weight
                if new_dist < end.min_dist:
                    end.min_dist = new_dist
                    end.predecessor = start
                    heapq.heappush(self.heap,end)
            actualVertex.visited = True


    def get_shortest(self,vertex):
        print(f"The shortest distance to vertex {vertex.name} is {vertex.min_dist}")
        actual_vertex = vertex
        while actual_vertex:
            print(actual_vertex.name , end=" ")
            actual_vertex = actual_vertex.predecessor



# Step 1 - create nodes
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")
nodeG = Node("G")
nodeH = Node("H")

# Step 2 - create edges
nodeA.add_edge(6, nodeB)
nodeA.add_edge(10, nodeC)
nodeA.add_edge(9, nodeD)

nodeB.add_edge(5, nodeD)
nodeB.add_edge(16, nodeE)
nodeB.add_edge(13, nodeF)

nodeC.add_edge(6, nodeD)
nodeC.add_edge(5, nodeH)
nodeC.add_edge(21, nodeG)

nodeD.add_edge(8, nodeF)
nodeD.add_edge(7, nodeH)

nodeE.add_edge(10, nodeG)

nodeF.add_edge(4, nodeE)
nodeF.add_edge(12, nodeG)

nodeH.add_edge(2, nodeF)
nodeH.add_edge(14, nodeG)

algorithm = Dijkstra()
algorithm.calculate(nodeA)
algorithm.get_shortest(nodeE)


