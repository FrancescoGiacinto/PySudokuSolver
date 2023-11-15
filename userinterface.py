import tkinter as tk
from tkinter import messagebox
from typing import Optional
from sudoku import Sudoku 
from controller import Controller


class UserInterface:
    """
    Graphical User Interface for the Sudoku game using Tkinter.

    Attributes:
        game (Sudoku): The instance of the Sudoku game.
        window (tk.Tk): The main window of the application.
        cells (list): A 2D list of Entry widgets representing the Sudoku grid.

    Methods:
        start(): Starts the GUI application.
        update_grid(): Updates the grid display based on the current game state.
        on_cell_input(row, col, event): Handles input into a cell.
        solve_puzzle(): Solves the current puzzle.
    """

    def __init__(self, game: Sudoku, controller: Optional[Controller] = None) -> None:
        """
        Initializes the UserInterface with a Sudoku game instance.
        """
        self.game = game
        self.controller = controller

        self.window = tk.Tk()
        self.window.title("Sudoku")

        self._init_difficulty_selection()
        self._init_grid()
        self._init_controls()

        # Start the game with the default difficulty
        self.start()

    def _init_difficulty_selection(self)-> None:
        """
        Initializes the difficulty selection UI components.
        """
        self.difficulty_var = tk.StringVar(self.window)
        self.difficulty_var.set("medium")  # default value
        self.difficulty_menu = tk.OptionMenu(self.window, self.difficulty_var, "easy", "medium", "hard")
        self.difficulty_menu.grid(row=0, column=0, columnspan=3)

        self.start_button = tk.Button(self.window, text="Start Game", command=self.start_game)
        self.start_button.grid(row=0, column=3, columnspan=3)

    def _init_grid(self)-> None:
        """
        Initializes the Sudoku grid UI components.
        """
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                cell = tk.Entry(self.window, width=2, font=('Arial', 18), justify='center')
                padx, pady = (1, 1)
                if i % 3 == 2:  
                    pady = (1, 5)
                if j % 3 == 2:
                    padx = (1, 5)
                cell.grid(row=i+1, column=j, sticky="nsew", padx=padx, pady=pady)
                cell.bind("<KeyRelease>", lambda event, row=i, col=j: self.on_cell_input(row, col, event))
                self.cells[i][j] = cell

    def _init_controls(self)-> None:
        """
        Initializes other control UI components, like the Solve button.
        """
        solve_button = tk.Button(self.window, text="Solve", command=self.solve_puzzle)
        solve_button.grid(row=10, column=0, columnspan=9)  

    def start_game(self)-> None:
        """
        Starts a new game with the selected difficulty and updates the grid.
        """
        difficulty = self.difficulty_var.get()
        self.game.start_game(difficulty)
        self.update_grid()

    def start(self)-> None:
        """
        Starts the GUI application.
        """
        self.window.mainloop()


    def update_grid(self)-> None:
        """
        Updates the grid display based on the current game state.
        """
        for i in range(9):
            for j in range(9):
                cell_value = self.game.grid.cells[i][j].value
                entry = self.cells[i][j]
                entry.delete(0, tk.END)
                if cell_value != 0:
                    entry.insert(0, cell_value)
                    if self.game.grid.cells[i][j].fixed:
                        entry.config(bg='light grey')
                    else:
                        entry.config(bg='white')

    def on_cell_input(self, row: int, col: int, event: tk.Event) -> None:
        """
        Handles input into a cell.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
            event: The event that triggered this method.
        """
        try:
            value = int(self.cells[row][col].get())
            self.controller.update_cell(row, col, value)
        except ValueError:
            self.show_message("Error", "Please enter a valid number (1-9)")

    def show_message(self, title: str, message: str) -> None:
        tk.messagebox.showinfo(title, message)

    def solve_puzzle(self)-> None:
        """
        Solves the current puzzle and updates the grid.
        """
        if self.game.grid.solve():
            self.update_grid()
        else:
            messagebox.showinfo("Sudoku", "No solution exists for this puzzle.")

    def set_controller(self, controller)-> None:
        """
        Sets the controller for the user interface.

        Args:
            controller (Controller): The controller to be used with this UI.
        """
        self.controller = controller