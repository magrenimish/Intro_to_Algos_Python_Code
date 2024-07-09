from collections import deque

def bfs(graph, start):
    visited = set()  # Set to keep track of visited nodes.
    queue = deque([start])  # Initialize a queue

    while queue:
        vertex = queue.popleft()  # Pop a vertex from queue
        if vertex not in visited:
            print(vertex, end=' ')  # Print the vertex
            visited.add(vertex)
            # Queue all adjacent nodes
            queue.extend(n for n in graph[vertex] if n not in visited)

# Example:
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['F'],
#     'F': []
# }
# print("BFS starting from vertex 'A':")
# bfs(graph, 'A')
