class Graph:
    def __init__(self,gdict=None):
        if not gdict:
            self.gdict = {}
        self.gdict = gdict
    
    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)

    def bfs(self,vertex):
        visited=set(vertex)
        queue = [vertex]
        while queue :
            x = queue.pop(0)
            print(x)
            for adj in self.gdict[x]:
                if adj not in visited:
                    queue.append(adj)
                    visited.add(adj)

cust = { 'a':['c'] , 'b':['a'] , 'c' : ['a'] }

graph = Graph(cust)

# print(graph.gdict)

graph.addEdge('b','c')

graph.bfs('b')