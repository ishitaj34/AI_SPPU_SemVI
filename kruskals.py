graph = [
    [-1, 3, 2, 8, -1],
    [3, 5, -1, 7, -1],
    [2, -1, -1, 4, 9],
    [8, 7, 4, -1, 6],
    [-1, -1, 9, 6, -1]
]

def sort_edges(graph):
    edges = []
    n = len(graph)
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] != -1:
                edges.append((i, j, graph[i][j]))
    
    edges.sort(key = lambda x: x[2])

    print("\nSorted Edges: ")
    for edge in edges:
        print(edge)

    return edges

def find_parent(parent, i):
    if parent[i] == i:
        return i
    return find_parent(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find_parent(parent, x)
    yroot = find_parent(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1
        
def kruskals_algorithm(graph):
    n = len(graph)
    edges = sort_edges(graph)
    parent = [i for i in range(n)]
    rank = [0] * n
    min_cost = 0
    mst = []

    for edge in edges:
            x, y, weight = edge
            xroot = find_parent(parent, x)
            yroot = find_parent(parent, y)
            
            if xroot != yroot:
                mst.append(edge)
                union(parent, rank, xroot, yroot)
                min_cost += weight
        
    print("\nMinimum Spanning Tree: ")
    for edge in mst:
        print(edge)
        
    print(f"\nMinimum cost of the spanning tree is {min_cost}.\n")
    
kruskals_algorithm(graph)

