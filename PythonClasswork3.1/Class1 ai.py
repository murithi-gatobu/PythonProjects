# Define the graph as a dictionary
graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}
# List to keep track of visited nodes
visited = []
# Initialize a queue
queue = []
# BFS Function
def bfs(visited, graph, node):
    # Mark the node as visited and add to the queue
    visited.append(node)
    queue.append(node)
    #Loop while queue is not empty
    while queue:
        # Pop the first node from the queue
        s = queue.pop(0)
        print(s, end=" ")

        #Visit all the unvisited neighbours of the current node
        for neigbour in graph[s]:
            if neigbour not in visited:
                visited.append(neigbour)
                queue.append(neigbour)

# Call the BFS function starting from node 'A'
bfs(visited, graph, 'A')

    
