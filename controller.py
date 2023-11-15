from sudoku import Sudoku
from userinterface import UserInterface


class Controller:
    """
    Controller for the Sudoku game, acting as an intermediary between the UserInterface and the Sudoku game logic.

    Attributes:
        game (Sudoku): An instance of the Sudoku game.
        ui (UserInterface): The graphical user interface for the game.

    Methods:
        start(): Initializes and starts the game.
        handle_cell_input(row, col, value): Handles input from the user into a Sudoku cell.
        solve_puzzle(): Solves the current puzzle.
    """

    def __init__(self, game: Sudoku, ui: UserInterface) -> None:
        """
        Initializes the Controller with the game and UI instances.

        Args:
            game (Sudoku): An instance of the Sudoku game.
            ui (UserInterface): The graphical user interface for the game.
        """
        self.game = game
        self.ui = ui

        # Set up the UI to use this controller for handling events
        self.ui.set_controller(self)

    def start(self) -> None:
        """
        Starts the Sudoku game.
        """
        self.game.start_game(difficulty='medium')
        self.ui.start()

    def handle_cell_input(self, row: int, col: int, value: int) -> bool:
        """
        Handles input from the user into a cell of the Sudoku grid.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
            value (int): The value entered into the cell.
        """
        if self.game.grid.is_valid_move(row, col, value):
            self.game.grid.cells[row][col].value = value
            if self.game.check_solution():
                self.ui.show_message("Congratulations! You solved the puzzle.")
            return True
        else:
            self.ui.show_message("Invalid move.")
            return False

    def solve_puzzle(self) -> None:
        """
        Solves the current puzzle and updates the UI with the solution.
        """
        if self.game.grid.solve():
            self.ui.update_grid()
            self.ui.show_message("Puzzle solved.")
        else:
            self.ui.show_message("No solution exists for this puzzle.")

    def update_cell(self, row:int, col:int, value:int) -> None:
        """
        Updates the value of a cell and checks if the move is valid.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
            value (int): The value to be placed in the cell.
        """
        if value in range(1, 10) and self.game.grid.is_valid_move(row, col, value):
            self.game.grid.cells[row][col].value = value
            if self.game.grid.is_solved_correctly():
                self.ui.show_congratulations()
        else:
            self.ui.show_error("Invalid move")

    def show_congratulations(self)-> None:
        self.ui.show_message("Congratulations!", "You solved the Sudoku puzzle!")

    def show_error(self, message: str)-> None:
        self.ui.show_message("Error", message)