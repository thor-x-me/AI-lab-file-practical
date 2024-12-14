from collections import deque

def bfs(graph, start):
    # Create a queue for BFS
    queue = deque([start])
    # Set to keep track of visited nodes
    visited = set()
    # List to store the order of traversal
    traversal_order = []

    # Mark the start node as visited
    visited.add(start)

    while queue:
        # Dequeue a node from the queue
        current_node = queue.popleft()
        traversal_order.append(current_node)

        # Get all adjacent nodes of the current node
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                # If a neighbor has not been visited, mark it visited and enqueue it
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}

# Perform BFS traversal starting from node 'A'
start_node = 'A'
result = bfs(graph, start_node)
print("Breadth-First Search Traversal:", result)
