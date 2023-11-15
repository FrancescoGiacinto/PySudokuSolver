from typing import Optional
from grid import Grid
from puzzlegenerator import PuzzleGenerator
from userinterface import UserInterface
from solver import Solver
from controller import Controller
from moveshistory import MovesHistory

class Sudoku:
    """
    The main class for the Sudoku game, integrating various components of the game.

    Attributes:
        grid (Grid): The Sudoku grid.
        generator (PuzzleGenerator): The puzzle generator used to create new puzzles.
        solver (Solver): The solver used to solve the puzzle.
        history (MovesHistory): The history of moves for undo/redo functionality.
        ui (UserInterface): The graphical user interface for the game.
        controller (Controller): The controller handling the logic between UI and game model.
    """

    def __init__(self) -> None:
        """
        Initializes the Sudoku game with the necessary components.
        """
        self.grid: Grid = Grid()
        self.generator: PuzzleGenerator = PuzzleGenerator(self.grid)
        self.solver: Solver = Solver()
        self.history: MovesHistory = MovesHistory()

        # Initialize the UI first with the game instance
        self.ui: UserInterface = UserInterface(self)

        # Then initialize the controller with the game and UI instances
        self.controller: Controller = Controller(self, self.ui)

    def start_game(self, difficulty: str = 'medium') -> None:
        """
        Starts a new game with a puzzle of the specified difficulty.

        Args:
            difficulty (str): The difficulty level of the puzzle ('easy', 'medium', 'hard').
        """
        self.generator.generate(difficulty)
        self.history = MovesHistory()

    def play(self) -> None:
        """
        Main method to start the game interaction.
        """
        self.controller.start()


