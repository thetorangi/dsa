import heapq

class Edge:
    def __init__(self,start,end,weight):
        self.start = start
        self.end = end
        self.weight = weight
    
class Node:
    def __init__(self,name):
        self.name = name
        self.visited = False
        self.neighbours=[]
        self.pre = None
        self.min_dist = float('inf')

    def __lt__(self,other):
        return self.min_dist < other.min_dist
    
    def add_edge(self,weight,end):
        edge = Edge(self,end,weight)
        self.neighbours.append(edge)
        
class Dijkstra:
    def __init__(self):
        self.heap = []
    
    def calculate(self,start_vertex):
        start_vertex.min_dist =0 
        heapq.heappush(self.heap,start_vertex)
        while self.heap :
            actual_vertex = heapq.heappop(self.heap)
            if actual_vertex.visited == True :
                continue
            for edge in actual_vertex.neighbours:
                start = edge.start
                end = edge.end
                new_dist = start.min_dist + edge.weight
                if new_dist < end.min_dist : 
                    end.min_dist = new_dist
                    end.pre = start
                    heapq.heappush(self.heap,end)
            actual_vertex.visited = True

    def get_short(self,end_vertex):
        print(f"Distance to end vertex is {end_vertex.min_dist}")
        while end_vertex:
            print(end_vertex.name , end=" ")
            end_vertex = end_vertex.pre
                

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
algorithm.get_short(nodeE)
