from collections import deque

# Initial State
start = [1, 2, 3,
         4, 5, 6,
         0, 7, 8]

# Goal State
goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]

# Display the puzzle
def display(board):
    for i in range(0, 9, 3):
        print(board[i:i+3])
    print()

# Generate all possible moves
def move(board):

    blank = board.index(0)

    step = {
        0: [1, 3],
        1: [0, 2, 4],
        2: [1, 5],
        3: [0, 4, 6],
        4: [1, 3, 5, 7],
        5: [2, 4, 8],
        6: [3, 7],
        7: [4, 6, 8],
        8: [5, 7]
    }

    result = []

    for i in step[blank]:
        a = board.copy()
        a[blank], a[i] = a[i], a[blank]
        result.append(a)

    return result

# BFS Search
def solve():

    q = deque([start])
    seen = [start]

    while q:

        board = q.popleft()

        display(board)

        if board == goal:
            print("Goal State Reached!")
            return

        for x in move(board):
            if x not in seen:
                seen.append(x)
                q.append(x)

    print("No Solution")

# Main Program
solve()
