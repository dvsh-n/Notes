# Recursive DFS implementation

# Perform a depth-first search (DFS) on a graph recursively.
#
# Args:
#     graph (dict): A dictionary representing the adjacency list of the graph.
#     start (str): The starting node for the DFS.
#     visited (set, optional): A set to keep track of visited nodes. Defaults to None.
#
# Returns:
#     None
#
# Example:
#
# Time Complexity: O(V + E)
#     - V is the number of vertices (nodes)
#     - E is the number of edges
# Space Complexity: O(V)
#     - Due to the recursion stack and the visited set

# function implementation

# Perform a depth-first search (DFS) on a graph iteratively using a stack.
#
# Args:
#     graph (dict): A dictionary representing the adjacency list of the graph.
#     start (str): The starting node for the DFS.
#
# Returns:
#     None
#
# Example:
#
# Time Complexity: O(V + E)
#     - V is the number of vertices (nodes)
#     - E is the number of edges
# Space Complexity: O(V)
#     - Due to the stack and the visited set

# function implementation
def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# Iterative DFS implementation using a stack
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            stack.extend(reversed(graph[vertex]))  # Add neighbors in reverse order to maintain order

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("Recursive DFS:")
dfs_recursive(graph, 'A')

print("\nIterative DFS:")
dfs_iterative(graph, 'A')