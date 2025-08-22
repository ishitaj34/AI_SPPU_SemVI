def add_edge(adj, v, w):
    adj[v].append(w)
    adj[w].append(v)
    
    return adj

def graph_coloring(graph):
    V = len(graph)
    
    # -1 for no colors assigned yet
    result = [-1] * V
    
    # To assign first color to first vertex
    result[0] = 0
    
    # To store availability of colors
    available = [False] * V
    
    # To assign colors to remaining V-1 vertices
    for i in range(1, V):
        for j in graph[i]:
            if result[j] != -1:
                available[result[j]] = True
                
        color = 0
        while color < V:
            if available[color] == False:
                break
            color += 1
        
        # To assign color to vertex in result list   
        result[i] = color       
        
        # To reset values back to False for next iteration
        for k in graph[i]:
            if result[k] != -1:
                available[result[k]] = False

    # To print result
    for i in range(V):
        print(f"Vertex {i} ---> Color {result[i]}")


if __name__ == '__main__':
    
    # Generating graph
    graph = [ [] for i in range(5)]
    graph = add_edge(graph, 0, 1)
    graph = add_edge(graph, 0, 2)
    graph = add_edge(graph, 1, 2)
    graph = add_edge(graph, 1, 3)
    graph = add_edge(graph, 2, 3)
    graph = add_edge(graph, 3, 4)
    print("\nGraph:", graph)
    
    print("\nGraph coloring:")
    graph_coloring(graph)
    print("\n")
