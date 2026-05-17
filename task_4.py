from collections import deque

# Define the graph using an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

#Breadth first search

def bfs_path(graph, start, goal):
    # Initialize the queue with the starting node and its path
    queue = deque([(start, [start])])
    # Keep track of visited nodes to avoid infinite loops
    visited = set([start])
    
    while queue:
        # Dequeue the oldest node and its corresponding path
        current_node, path = queue.popleft()
        
        # Check if we have reached the goal state
        if current_node == goal:
            return path
            
        # Explore the immediate neighbors of the current node
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                # Append the neighbor and the updated path to the queue
                queue.append((neighbor, path + [neighbor]))
                
    return None # Return None if no path exists

# Run and output the result
initial_node = 'A'
goal_node = 'F'
search_path = bfs_path(graph, initial_node, goal_node)

print("--- Breadth-First Search (BFS) ---")
print(f"Initial State: {initial_node}")
print(f"Goal State: {goal_node}")
print(f"Search Path: {' -> '.join(search_path) if search_path else 'No path found'}")

#depth first search

def dfs_path(graph, current_node, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = [current_node]
        
    # Mark the current node as visited
    visited.add(current_node)
    
    # Check if we have reached the goal state
    if current_node == goal:
        return path
        
    # Recursively visit unvisited neighbors deeply
    for neighbor in graph[current_node]:
        if neighbor not in visited:
            # Construct the potential path through this neighbor
            result_path = dfs_path(graph, neighbor, goal, visited, path + [neighbor])
            # If the recursive call found the goal, pass the path back up
            if result_path:
                return result_path
                
    return None # Return None if it hits a dead end

# Run and output the result
initial_node = 'A'
goal_node = 'F'
search_path = dfs_path(graph, initial_node, goal_node)

print("--- Depth-First Search (DFS) ---")
print(f"Initial State: {initial_node}")
print(f"Goal State: {goal_node}")
print(f"Search Path: {' -> '.join(search_path) if search_path else 'No path found'}")