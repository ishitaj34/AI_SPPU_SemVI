import heapq

class Node:
    def __init__(self, name, g = 0, h = 0, parent = None):
        self.name = name
        self.g = g  
        self.h = h  
        self.f = g + h  
        self.parent = parent

    def __lt__(self, other):
        return self.f < other.f     # For priority queue sorting

def a_star(graph, start, goal, heuristic):
    open_list = []
    closed_set = set()

    start_node = Node(start, g = 0, h = heuristic[start])
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.name == goal:
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1]       # Return reversed path from start to goal

        closed_set.add(current_node.name)

        for neighbor, cost in graph[current_node.name].items():
            if neighbor in closed_set:
                continue

            new_g = current_node.g + cost
            neighbor_node = Node(neighbor, g = new_g, h = heuristic[neighbor], parent = current_node)

            heapq.heappush(open_list, neighbor_node)

    return None     # No path found

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1, 'E': 3},
    'E': {'D': 3}
}

heuristic = {'A': 7, 'B': 6, 'C': 2, 'D': 1, 'E': 0}

start_node = 'A'
goal_node = 'E'

shortest_path = a_star(graph, start_node, goal_node, heuristic)

print("\nShortest Path:", shortest_path, "\n")
