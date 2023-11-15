from cell import Cell
from typing import Optional, Tuple

class Grid:
    """
    Represents the 9x9 grid in a Sudoku game.

    Attributes:
        cells (list): A 9x9 matrix of Cell objects representing the Sudoku grid.

    Methods:
        is_full(): Checks if the grid is completely filled.
        is_valid_move(row, col, value): Checks if placing a value at a specific location is valid.
        find_empty_cell(): Finds an empty cell in the grid.
        solve(): Attempts to solve the Sudoku puzzle using backtracking.
        display(): Prints the grid in a readable format to the console.
    """

    def __init__(self) -> None:
        """
        Constructs a Grid for the Sudoku game.
        Initializes a 9x9 grid of cells, initially empty.
        """
        self.cells = [[Cell() for _ in range(9)] for _ in range(9)]

    def is_full(self) -> bool:
        """
        Checks whether the grid is full (no empty cells).

        Returns:
            bool: True if the grid is full, False otherwise.
        """
        return all(cell.value != 0 for row in self.cells for cell in row)

    def is_valid_move(self, row:int, col: int, value:int) -> bool:
        """
        Checks if it's valid to place a value in a specific cell.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
            value (int): The value to check.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        # Check row and column
        for i in range(9):
            if self.cells[row][i].value == value or self.cells[i][col].value == value:
                return False

        # Check 3x3 square
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.cells[i][j].value == value:
                    return False

        return True

    def find_empty_cell(self) -> Optional[Tuple[int, int]]:
        """
        Finds an empty cell in the grid.

        Returns:
            Optional[Tuple[int, int]]: The row and column index of the empty cell, 
                                    or None if the grid is full.
        """
        for i in range(9):
            for j in range(9):
                if self.cells[i][j].value == 0:
                    return (i, j)
        return None

    def solve(self) -> bool:
        """
        Attempts to solve the Sudoku puzzle using a backtracking algorithm.

        Returns:
            bool: True if the puzzle is solved, False otherwise.
        """
        empty_cell = self.find_empty_cell()
        if not empty_cell:
            return True  # Solved

        row, col = empty_cell
        for num in range(1, 10):
            if self.is_valid_move(row, col, num):
                self.cells[row][col].value = num

                if self.solve():
                    return True

                self.cells[row][col].value = 0  # Backtrack

        return False  # Trigger backtrack

    def display(self) -> None:
        """
        Prints the grid in a readable format to the console.
        """
        for row in self.cells:
            print(" ".join(str(cell.value) for cell in row))

    def is_solved_correctly(self) -> bool:
        """
        Checks if the Sudoku puzzle is solved correctly.

        Returns:
            bool: True if the puzzle is solved correctly, False otherwise.
        """
        # Check if all cells are filled
        for row in self.cells:
            for cell in row:
                if cell.value == 0:
                    return False
        return True
