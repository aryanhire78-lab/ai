from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

# Graph
graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}

# BFS
def bfs(start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])

    return visited

# DFS
def dfs(node, visited=[]):
    if node not in visited:
        visited.append(node)

        for n in graph[node]:
            dfs(n, visited)

    return visited

# Output
print("BFS :", " -> ".join(bfs('A')))
print("DFS :", " -> ".join(dfs('A')))

# Graph Visualization
G = nx.DiGraph(graph)

nx.draw(
    G,
    with_labels=True,
    node_color='lightblue',
    node_size=2000
)

plt.show()
