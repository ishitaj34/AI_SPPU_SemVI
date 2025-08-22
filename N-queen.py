def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_safe(board, row, col, n):
    # To check vertical column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # To check upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # To check upper right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens_util(board, row, n, solutions):
    if row == n:
        solutions.append(["".join(r) for r in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'
            solve_n_queens_util(board, row + 1, n, solutions)
            board[row][col] = '.'  

def solve_n_queens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    return solutions

# Main function
n = int(input("\nEnter the number of queens(N): "))
solutions = solve_n_queens(n)
print(f"Total solutions for {n}-Queens: {len(solutions)}")
for sol in solutions:
    print_board([list(row) for row in sol])
