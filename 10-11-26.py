def solve_n_queens_backtracking(n):
    board = [-1] * n

    def is_safe(row, col):
        for r in range(row):
            c = board[r]

            if c == col or abs(r - row) == abs(c - col):
                return False

        return True

    def backtrack(row):
        if row == n:
            return True

        for col in range(n):
            if is_safe(row, col):
                board[row] = col

                if backtrack(row + 1):
                    return True

                board[row] = -1

        return False

    print("N Queens Backtracking Report")
    print(f"Board Size: {n}")

    if backtrack(0):
        print("Solution Found: Yes")
        print("Board")

        for row in range(n):
            line = ""
            for col in range(n):
                if board[row] == col:
                    line += "Q"
                else:
                    line += "."
            print(line)

        print("Queen Positions")
        print("Row Column")

        for row in range(n):
            print(row + 1, board[row] + 1)

    else:
        print("Solution Found: No")
        print("No solution exists for the given board size.")

    print("Complexity: O(N!)")
    print("Observation: Backtracking places queens row by row and removes unsafe choices")

    return [col + 1 for col in board] if board[0] != -1 else []
