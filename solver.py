import random
from grid import Grid

class Solver:
    """
    Solves a Sudoku puzzle using a backtracking algorithm.
    """

    @staticmethod
    def solve(grid: Grid) -> bool:
        """
        Solves the Sudoku puzzle using a backtracking algorithm.

        Args:
            grid (Grid): The Sudoku grid to be solved.

        Returns:
            bool: True if the puzzle is solved, False otherwise.
        """
        empty_cell = grid.find_empty_cell()
        if not empty_cell:
            return True  # Solved

        row, col = empty_cell
        numbers = list(range(1, 10))
        random.shuffle(numbers)
        for num in numbers:
            if grid.is_valid_move(row, col, num):
                grid.cells[row][col].value = num

                if Solver.solve(grid):
                    return True  # Solution

                grid.cells[row][col].value = 0  # Backtrack

        return False  # No solution found

