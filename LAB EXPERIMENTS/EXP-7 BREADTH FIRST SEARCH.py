from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

visited = []
queue = deque()

start = 'A'

visited.append(start)
queue.append(start)

print("BFS Traversal:")

while queue:

    node = queue.popleft()
    print(node, end=" ")

    for i in graph[node]:
        if i not in visited:
            visited.append(i)
            queue.append(i)
