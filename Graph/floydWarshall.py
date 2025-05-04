INF = float('inf')

def floydWarshall(graph , nV):
    dist = graph
    
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                dist[i][j] = min ( dist[i][j] , (dist[i][k] + dist[k][j]))
                
    for row in dist : print(row)

G = [[0, 8, INF,1],
    [INF, 0, 1,INF],
    [4, INF, 0,INF],
    [INF, 2, 9,1]
    ]

for g in G : print(g)

print("----------")

floydWarshall(G,4)
