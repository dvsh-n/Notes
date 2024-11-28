# Performs Breadth-First Search (BFS) on a graph starting from a given vertex.
# Args:
#     graph (dict): A dictionary representing the graph where keys are vertices and values are lists of adjacent vertices.
#     start: The starting vertex for the BFS traversal.
# Returns:
#     None
# Prints:
#     The vertices of the graph in the order they are visited by BFS.
# Example:
#     bfs(graph, 'A')  # Output: A B C D E F
# Time Complexity:
#     O(V + E), where V is the number of vertices and E is the number of edges in the graph.
#     This is because each vertex and each edge is processed once.
# Space Complexity:
#     O(V), where V is the number of vertices in the graph.
#     This is due to the space required for the visited set and the queue.


from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Perform BFS starting from vertex 'A'
bfs(graph, 'A')