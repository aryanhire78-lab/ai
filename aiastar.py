import heapq

# Graph with costs
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

# Heuristic values
heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 3,
    'E': 1,
    'F': 0
}

# A* Algorithm
def astar(start, goal):
    pq = []
    heapq.heappush(pq, (0, start))

    cost = {start: 0}
    parent = {start: None}

    while pq:
        f, current = heapq.heappop(pq)

        if current == goal:
            break

        for neighbor, weight in graph[current]:

            new_cost = cost[current] + weight

            if neighbor not in cost or new_cost < cost[neighbor]:

                cost[neighbor] = new_cost

                priority = new_cost + heuristic[neighbor]

                heapq.heappush(pq, (priority, neighbor))

                parent[neighbor] = current

    # Path reconstruction
    path = []
    node = goal

    while node:
        path.append(node)
        node = parent[node]

    path.reverse()

    print("Shortest Path :", " -> ".join(path))
    print("Total Cost :", cost[goal])

# Run
astar('A', 'F')
