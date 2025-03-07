def solve_n_queens(n):
    def is_safe(row, col, board):
        # Check if placing a queen at (row, col) is safe
        for i in range(row):
            # Check same column or diagonal
            if board[i] == col or abs(row - i) == abs(col - board[i]):
                return False
        return True

    def backtrack(row, board, solutions):
        # Base case: All queens are placed
        if row == n:
            solutions.append(board[:])  # Add a copy of the board to solutions
            return

        # Try placing a queen in each column of the current row
        for col in range(n):
            if is_safe(row, col, board):
                board[row] = col  # Place the queen
                backtrack(row + 1, board, solutions)  # Move to the next row
                board[row] = -1  # Backtrack (remove the queen)

    # Initialize the board with -1 (no queens placed)
    board = [-1] * n
    solutions = []
    backtrack(0, board, solutions)  # Start from row 0

    return solutions

def print_solutions(solutions, n):
    # Print all solutions in a readable format
    for solution in solutions:
        for row in range(n):
            line = ["."] * n
            line[solution[row]] = "Q"
            print(" ".join(line))
        print()

# Example usage
n = 4
solutions = solve_n_queens(n)
print(f"Total solutions for {n}-Queens problem: {len(solutions)}")
print_solutions(solutions, n)