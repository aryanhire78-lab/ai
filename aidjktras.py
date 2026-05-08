# Selection Sort

arr = [64, 25, 12, 22, 11]

n = len(arr)

for i in range(n):

    # Assume minimum
    min_index = i

    # Find smallest element
    for j in range(i + 1, n):

        if arr[j] < arr[min_index]:
            min_index = j

    # Swap
    arr[i], arr[min_index] = arr[min_index], arr[i]

print("Sorted Array:")
print(arr)



##minimum spanning tree
# Prim's Algorithm

INF = 999999

# Number of vertices
V = 5

# Graph
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

selected = [False] * V

selected[0] = True

print("Edge : Weight")

# MST will have V-1 edges
for i in range(V - 1):

    minimum = INF
    x = 0
    y = 0

    for a in range(V):

        if selected[a]:

            for b in range(V):

                if (not selected[b] and graph[a][b]):

                    if minimum > graph[a][b]:

                        minimum = graph[a][b]
                        x = a
                        y = b

    print(x, "-", y, ":", graph[x][y])

    selected[y] = True


### prims minimal spanning tree
# # Prim's MST Algorithm

INF = 999999

# Number of vertices
V = 4

# Graph Matrix
graph = [
    [0, 10, 15, 0],
    [10, 0, 20, 25],
    [15, 20, 0, 30],
    [0, 25, 30, 0]
]

selected = [False] * V

selected[0] = True

print("Edge : Weight")

# MST has V-1 edges
for i in range(V - 1):

    minimum = INF

    x = 0
    y = 0

    for a in range(V):

        if selected[a]:

            for b in range(V):

                if not selected[b] and graph[a][b]:

                    if minimum > graph[a][b]:

                        minimum = graph[a][b]
                        x = a
                        y = b

    print(x, "-", y, ":", graph[x][y])

    selected[y] = True


##djktras
# Dijkstra Algorithm

INF = 999999

# Graph Matrix
graph = [
    [0, 2, 4, 0],
    [2, 0, 1, 7],
    [4, 1, 0, 3],
    [0, 7, 3, 0]
]

V = 4

# Distance array
dist = [INF] * V

# Visited array
visited = [False] * V

# Source vertex
dist[0] = 0

for i in range(V):

    # Find minimum distance vertex
    min_dist = INF
    u = -1

    for j in range(V):

        if not visited[j] and dist[j] < min_dist:
            min_dist = dist[j]
            u = j

    visited[u] = True

    # Update distances
    for v in range(V):

        if graph[u][v] != 0 and not visited[v]:

            if dist[u] + graph[u][v] < dist[v]:

                dist[v] = dist[u] + graph[u][v]

# Output
print("Vertex : Distance from Source")

for i in range(V):
    print(i, ":", dist[i])
