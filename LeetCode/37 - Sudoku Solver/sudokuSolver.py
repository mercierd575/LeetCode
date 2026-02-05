from typing import List


def solveSudoku(self, board: List[List[str]]) -> None:
    # As per the instructions, I shall not return anything and modify the board in place instead.

    # Creating Census containers
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    block_values = [set() for _ in range(9)]

    box_idx = 0

    # Performing the Census
    for r in range(9):
        for c in range(9):
            if ord(board[r][c]) != '.':
                val = board[r][c]
                rows[r].add(val)
                cols[c].add(val)
                blox_idx = (r // 3) * 3 + c // 3
                block_values[blox_idx].add(val)

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
        if board[row][col] != '.':  # If the spot isn't empty,
            return solve(row, col + 1)  # We skip to the next

        blox_idx = (row // 3) * 3 + col // 3

        for i in range(1, 10):  # We start the process of trying out candidates 1-9
            value = str(i)

            # CENSUS
            if value not in rows[row] and value not in cols[col] and value not in block_values[blox_idx]:
                # Updating Census
                board[row][col] = value
                rows[row].add(value)
                cols[col].add(value)
                block_values[blox_idx].add(value)

                if solve(row, col + 1): return True  # We keep going until we get a dead end

                # BACKTRACK
                board[row][col] = '.'  # If we run into a dead end, we backtrack
                rows[row].remove(value)
                cols[col].remove(value)
                block_values[blox_idx].remove(value)

        return False

    solve(0, 0)
