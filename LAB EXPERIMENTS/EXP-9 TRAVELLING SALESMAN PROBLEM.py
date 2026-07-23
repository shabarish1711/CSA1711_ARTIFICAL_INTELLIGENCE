# Travelling Salesman Problem

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

visited = [False, False, False, False]

city = 0
visited[city] = True
cost = 0

print("Path:", city, end=" ")

for i in range(3):

    minimum = 999
    next_city = -1

    for j in range(4):

        if graph[city][j] > 0 and visited[j] == False:

            if graph[city][j] < minimum:
                minimum = graph[city][j]
                next_city = j

    print("->", next_city, end=" ")

    cost = cost + minimum
    visited[next_city] = True
    city = next_city

cost = cost + graph[city][0]

print("-> 0")
print("Minimum Cost =", cost)
