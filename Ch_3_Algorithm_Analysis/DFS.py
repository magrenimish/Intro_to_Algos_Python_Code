def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    # Mark the node as visited
    visited.add(start)
    print(start, end=' ')  # Output the visited node
    # Recur for all the vertices adjacent to this vertex
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example:
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['F'],
#     'F': []
# }
# print("DFS starting from vertex 'A':")
# dfs(graph, 'A')
