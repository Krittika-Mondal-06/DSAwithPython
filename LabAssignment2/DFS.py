def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
graph = {
    'P': ['Q', 'S', 'T'],
    'Q': ['P', 'R', 'S'],
    'R': ['Q', 'S', 'U'],
    'S': ['P', 'Q', 'R', 'T', 'U'],
    'T': ['P', 'S', 'U'],
    'U': ['R', 'S', 'T']
}
print("Depth First Search Traversal:")
dfs(graph, 'P') 
print("\nDepth Second Search Traversal:")
dfs(graph, 'Q')
print("\nDepth Third Search Traversal:")
dfs(graph, 'R') 
print("\nDepth Fourth Search Traversal:")
dfs(graph, 'S') 
print("\nDepth Fifth Search Traversal:")
dfs(graph, 'T') 
print("\nDepth Sixth Search Traversal:")
dfs(graph, 'U') 
