class Graph:
    def __init__(self,gdict=None):
        if not gdict:
            self.gdict = {}
        self.gdict = gdict
    
    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)

        
    def bfs_org(self,vertex): #the one which i learned from Elshad
            visited=set(vertex)
            queue = [vertex]
            while queue :
                x = queue.pop(0)
                print(x)
                for adj in self.gdict[x]:
                    if adj not in visited:
                        queue.append(adj)
                        visited.add(adj)


    def bfs(self,vertex): #updated by me 
            visited=set()
            queue = [vertex]
            while queue :
                x = queue.pop(0)
                if x not in visited:
                    visited.add(x)
                    print(x)
                    for adj in self.gdict[x]:
                        if adj not in visited:
                            queue.append(adj)

    def dfs_org(self,vertex): #original
        visited = set(vertex)
        stack = [vertex]
        while stack:
            x = stack.pop()
            print(x)
            for adj in self.gdict[x]:
                if adj not in visited:
                    visited.add(adj)
                    stack.append(adj)

    def dfs(self,vertex): #offcourse me
        visited=set()
        queue = [vertex]
        while queue :
            x = queue.pop()
            if x not in visited:
                visited.add(x)
                print(x)
                for adj in self.gdict[x]:
                    if adj not in visited:
                        queue.append(adj)

cust = { "a" : ["b","c"],
            "b" : ["a", "d", "e"],
            "c" : ["a", "e"],
            "d" : ["b", "e", "f"],
            "e" : ["d", "f", "c"],
            "f" : ["d", "e"]
               }

graph = Graph(cust)


graph.dfs('a')

print("\n")

graph.dfs_org('a')