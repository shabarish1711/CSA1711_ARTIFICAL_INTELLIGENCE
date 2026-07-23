from collections import deque

start = (3, 3, 'L')
goal = (0, 0, 'R')

moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

def safe(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False

    if m > 0 and m < c:
        return False

    mr = 3 - m
    cr = 3 - c

    if mr > 0 and mr < cr:
        return False

    return True

def bfs():
    q = deque()
    q.append((start, [start]))

    visited = []

    while q:
        state, path = q.popleft()

        if state == goal:
            return path

        if state in visited:
            continue

        visited.append(state)

        m, c, boat = state

        for x, y in moves:

            if boat == 'L':
                new = (m - x, c - y, 'R')
            else:
                new = (m + x, c + y, 'L')

            if safe(new[0], new[1]):
                q.append((new, path + [new]))

answer = bfs()

print("Solution:")

for i in answer:
    print(i)
