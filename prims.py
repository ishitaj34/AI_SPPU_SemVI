# Prims Algorithm for Minimum Spanning Tree

# adjacency matrix with -1 representing no edge between vertices
graph = [
    [-1, 3, 2, 8, -1],
    [3, 5, -1, 7, -1],
    [2, -1, -1, 4, 9],
    [8, 7, 4, -1, 6],
    [-1, -1, 9, 6, -1]
]

def prims_algorithm(graph):
    n = len(graph)      # number of vertices
    
    visited = [0] * n   # initialise visited array
    
    visited[0] = 1      # mark the first vertex as visited
    min_cost = 0        # initialise minimum cost to 0
    
    for _ in range(n - 1):      # run n-1 times to include n-1 edges in MST
        min_weight = float('inf')       # to find the minimum weight in each iteration
        row = col = -1          # to store the row and column of the minimum weight

        for i in range(n):      # iterate over all vertices
            for j in range(n):    # iterate over vertices with connections with i
                if visited[i] == 1 and visited[j] == 0 and graph[i][j] != -1:       # i is part of MST, j is not part of MST, connection exist bw i and j
                    if graph[i][j] < min_weight:
                        min_weight = graph[i][j]
                        row, col = i, j

        visited[col] = 1
        min_cost += min_weight
        
        print(f"\nEdge {row + 1} - {col + 1} : Weight = {min_weight}")
        
    print(f"\nMinimum cost of the spanning tree is {min_cost}.\n")
    
prims_algorithm(graph)
