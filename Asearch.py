import heapq

def a_star_search(graph, start, goal, heuristics):
    # Priority queue stores (priority, current_node, path, actual_cost)
    frontier = [(heuristics[start], start, [start], 0)]
    visited = {}

    while frontier:
        f_score, current, path, g_score = heapq.heappop(frontier)

        if current == goal:
            return path, g_score

        if current in visited and visited[current] <= g_score:
            continue
        
        visited[current] = g_score

        for neighbor, weight in graph.get(current, {}).items():
            new_g = g_score + weight
            new_f = new_g + heuristics.get(neighbor, 0)
            heapq.heappush(frontier, (new_f, neighbor, path + [neighbor], new_g))

    return None, float('inf')

# Example Usage
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 1, 'E': 4},
    'C': {'D': 1},
    'D': {'G': 2},
    'E': {'G': 1}
}
heuristics = {'A': 5, 'B': 3, 'C': 4, 'D': 2, 'E': 1, 'G': 0}

path, cost = a_star_search(graph, 'A', 'G', heuristics)
print(f"Optimal Path: {path} with cost {cost}")