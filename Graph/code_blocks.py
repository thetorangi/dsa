gdict = { "a" : ["b","c"],
            "b" : ["a", "d", "e"],
            "c" : ["a", "e"],
            "d" : ["b", "e", "f"],
            "e" : ["d", "f", "c"],
            "f" : ["d", "e"]
               }

def bfs_org(vertex): #the one which i learned from Elshad
        visited=set(vertex)
        queue = [vertex]
        while queue :
            x = queue.pop(0)
            print(x)
            for adj in gdict[x]:
                if adj not in visited:
                    queue.append(adj)
                    visited.add(adj)


def bfs(vertex): #updated by me 
        visited=set()
        queue = [vertex]
        while queue :
            x = queue.pop(0)
            if x not in visited:
                visited.add(x)
                print(x)
                for adj in gdict[x]:
                    if adj not in visited:
                        queue.append(adj)

def dfs_org(vertex):
        visited = set(vertex)
        stack = [vertex]
        while stack:
            x = stack.pop()
            print(x)
            for adj in gdict[x]:
                if adj not in visited:
                    visited.add(adj)
                    stack.append(adj)



bfs_org('a')