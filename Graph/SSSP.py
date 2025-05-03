#Single Source Shortest Path 

class Graph:
    def __init__(self,gdict):
        self.gdict = gdict
    
    def sssp(self,start,end):
        queue=[]
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adj in self.gdict.get(node,[]):
                new_path=list(path)
                new_path.append(adj)
                queue.append(new_path)


customDict = { "a" : ["b", "c"],
               "b" : ["d", "g"],
               "c" : ["d", "e"],
               "d" : ["f"],
               "e" : ["f"],
               "g" : ["f"]
            }

graph = Graph(customDict)

print(graph.sssp('a','f'))

