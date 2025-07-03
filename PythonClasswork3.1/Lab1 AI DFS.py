# Define the graph as a dictionary
graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : [] 
}
# Set to keep track of visited nodes
visited = set()
# DFS Function
def dfs(visited, graph, node):
    if node not in visited:
        print(node) # Print the current node
        visited.add(node) # Mark the node as visited

        # Recursively visit all the neigbours 
        for neigbour in graph[node]:
            dfs(visited, graph, neigbour)
    # Call the DFS function strarting from node 'A'
    dfs(visited, graph, 'A')
