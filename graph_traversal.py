from collections import defaultdict, deque

""" defaultdict: a dictionary that automatically initializes lists for new keys. 
    deque: double ended queue for bfs. """

def create_graph(edges):
    graph = defaultdict(list)
    for src, dest in edges:
        graph[src].append(dest)
        graph[dest].append(src)  # undirected graph
    return graph

def dfs(graph, node, visited):
    if node not in visited:
        print(node, end = " ")
        visited.add(node)
        
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)
            
def bfs(graph, queue, visited):
    if not queue:
        return
    
    node = queue.popleft()
    
    if node not in visited:
        print(node, end = " ")
        visited.add(node)
        
        for neighbour in graph[node]:
            queue.append(neighbour)
        
    bfs(graph, queue, visited)

if __name__ == "__main__":
    edges = [
        (1, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 6)
    ]
    
    graph = create_graph(edges)
    
    print("\nDFS Traversal: ")
    visited_dfs = set()
    dfs(graph, 1, visited_dfs)

    print("\n\nBFS Traversal:")
    visited_bfs = set()
    queue = deque([1])
    bfs(graph, queue, visited_bfs)

    

        
