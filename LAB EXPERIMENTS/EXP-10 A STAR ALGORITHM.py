# A* Algorithm

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 6)],
    'C': [('F', 2)],
    'D': [],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 4,
    'E': 2,
    'F': 1,
    'G': 0
}

open_list = [('A', 0)]
visited = []

while open_list:

    open_list.sort(key=lambda x: x[1] + heuristic[x[0]])

    node, cost = open_list.pop(0)

    if node == 'G':
        print("Goal Reached")
        print("Cost =", cost)
        break

    visited.append(node)

    for neighbour, value in graph[node]:

        if neighbour not in visited:
            open_list.append((neighbour, cost + value))
