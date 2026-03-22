from typing import List

def reverse_submatrix(grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
    """
    Flips the square submatrix by reversing the order of its rows vertically

    Args:
        grid (List[List[int]]): The integer matrix to reverse
        x (int): The row index of the top-left corner of the square submatrix
        y (int): The column index of the top-left corner of the square submatrix
        k (int): The size (side length) of the square submatrix

    Returns:
        List[List[int]]: The updated matrix
    """

    for i in range(k//2):
        grid[x+i][y:y+k], grid[x+k-i-1][y:y+k] = grid[x+-i-1][y:y+k], grid[x+i][y:y+k]

    return grid