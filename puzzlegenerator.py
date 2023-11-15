import random
from typing import Optional
from grid import Grid 
from cell import Cell 

class PuzzleGenerator:
    """
    Generates Sudoku puzzles by first creating a complete valid grid
    and then removing a set number of cells to create the puzzle.
    """

    def __init__(self, grid: Grid) -> None:
        """
        Initializes the PuzzleGenerator with a reference to a Sudoku grid.

        Args:
            grid (Grid): The Sudoku grid on which to generate puzzles.
        """
        self.grid = grid

    def generate(self, difficulty: str = 'medium') -> Grid:
        """
        Generates a Sudoku puzzle by removing cells from a completed grid.

        The number of cells removed depends on the difficulty level.

        Args:
            difficulty (str): The difficulty level of the puzzle ('easy', 'medium', 'hard').
        
        Returns:
            Grid: The Sudoku grid with the generated puzzle.
        """
        self.randomly_fill_some_cells()
        self.grid.solve()

        # Determine the number of cells to remove based on difficulty
        cells_to_remove = 40 if difficulty == 'easy' else 50 if difficulty == 'medium' else 60

        # Randomly remove the specified number of cells
        for _ in range(cells_to_remove):
            row, col = random.randint(0, 8), random.randint(0, 8)
            while self.grid.cells[row][col].value == 0:
                row, col = random.randint(0, 8), random.randint(0, 8)
            self.grid.cells[row][col] = Cell()

        return self.grid

    def randomly_fill_some_cells(self) -> None:
        """
        Fills a few cells randomly with valid numbers.
        """
        some_random_number = random.randint(5, 10)
        for _ in range(some_random_number):
            row, col = random.randint(0, 8), random.randint(0, 8)
            if self.grid.cells[row][col].value == 0:
                numbers = list(range(1, 10))
                random.shuffle(numbers)
                for num in numbers:
                    if self.grid.is_valid_move(row, col, num):
                        self.grid.cells[row][col].value = num
                        break
