# Function to check whether a queen can be placed safely
def safe(board, row, col, n):
    
    # Check left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower-left diagonal
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


# Function to place queens
def solve(board, col, n):

    if col == n:
        return True

    for row in range(n):

        if safe(board, row, col, n):

            board[row][col] = 1

            if solve(board, col + 1, n):
                return True

            board[row][col] = 0

    return False


# Function to print the board
def display(board, n):

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# Main Program
n = int(input("Enter the number of queens: "))

board = [[0] * n for i in range(n)]

if solve(board, 0, n):
    print("\nSolution Found:\n")
    display(board, n)
else:
    print("No Solution Exists")
