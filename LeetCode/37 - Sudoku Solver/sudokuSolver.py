from typing import List


def solveSudoku(self, board: List[List[str]]) -> None:
    # As per the instructions, I shall not return anything and modify the board in place instead.
    def isValid(row: int, col: int, candidate: str) -> bool:
        # Checks if candidate (e.g. "2") exists in row/col

        vertical_bl = row // 3
        horizontal_bl = col // 3
        for i in range(9):
            # Checking row
            if board[row][i] == candidate: return False
            # Checking column
            if board[i][col] == candidate: return False
            # Checking 3x3 block
            if board[3 * vertical_bl + i // 3][3 * horizontal_bl + i % 3] == candidate: return False
        return True

    def solve(row: int, col: int) -> bool:
        if row == 9: return True  # If we get here, that means we solved the Sudoku
        if col == 9: return solve(row + 1, 0)  # Once we reach the final column, we go to the next line
        if board[row][col] != '.': # If the spot isn't empty,
            return solve(row, col + 1) # We skip to the next
        elif board[row][col] == '.':  # If the spot is empty
            for i in range(1, 10):  # We start the process of trying out candidates 1-9
                if isValid(row, col, str(i)):  # verifies if the candidate is adequate
                    board[row][col] = str(i)  # puts the candidate in the empty spot
                    if solve(row, col + 1): return True  # We keep going until we get a dead end
                    board[row][col] = '.'  # If we run into a dead end, we backtrack
            return False
        else:
            return False  # If it's not a valid input value nor an empty coord,
            # then it is an invalid input value, we are hitting a
            # dead end and it must call for a backtrack

    solve(0,0)