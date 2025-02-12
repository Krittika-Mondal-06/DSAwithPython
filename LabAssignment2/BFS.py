from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

# Graph Representation (Same as Above)
graph = {
    'P': ['Q', 'S', 'T'],
    'Q': ['P', 'R', 'S'],
    'R': ['Q', 'S', 'U'],
    'S': ['P', 'Q', 'R', 'T', 'U'],
    'T': ['P', 'S', 'U'],
    'U': ['R', 'S', 'T']
}
print("Breadth First Search Traversal:")
bfs(graph, 'P')  
print("\nBreadth Second Search Traversal:")
bfs(graph, 'Q')  
print("\nBreadth Third Search Traversal:")
bfs(graph, 'R')  
print("\nBreadth Fourth Search Traversal:")
bfs(graph, 'S')  
print("\nBreadth Fifth Search Traversal:")
bfs(graph, 'T')  
print("\nBreadth Sixth Search Traversal:")
bfs(graph, 'U')  
