# PySudokuSolver
This project embraces object-oriented programming principles to create a modular and interactive Sudoku game. It features a grid generator, a solver using backtracking algorithms, and a user-friendly interface.


## Description

This Sudoku Solver is a Python-based application that allows users to solve Sudoku puzzles. It features a graphical user interface (GUI) created with Tkinter, and it utilizes a backtracking algorithm for puzzle solving. Users can input Sudoku puzzles manually or generate new puzzles with varying difficulty levels. In this project, I used backtracking to solve Sudoku puzzles. Backtracking is like trying to solve a maze: you go down a path until you can't go any further, then you go back and try a different path. For the Sudoku game, I made my program fill in the empty spots with numbers. If it puts a number that doesn't work later on, it goes back, changes the number, and tries again. It keeps doing this until it finds the right numbers for all the spots, and that's how it solves the puzzle. It's a cool way to solve problems by trying different possibilities until you find the right one.

## Features

- Generate Sudoku puzzles with different difficulty levels (easy, medium, hard).
- Manually input custom puzzles.
- Solve puzzles using an efficient backtracking algorithm.
- Graphical user interface for easy interaction.

## Unit Testing
I have included some basic tests to make sure our Sudoku game works right. These tests check the main parts of our game, like making puzzles, solving them, and the undo/redo feature. Running these tests is easy and helps us make sure everything in the game is doing what it's supposed to. They're really helpful for keeping the game running smoothly and making sure any new changes don't break things.

## Requirements

- Python 3.x
- Tkinter library (usually comes with Python)

## Installation

No additional installation is required if you have Python installed. Simply clone the repository or download the source code to your local machine.

```
git clone https://github.com/FrancescoGiacinto/PySudokuSolver
```

## Usage

To run the Sudoku solver, navigate to the project directory and run:

```
python run.py
```

Once the application starts:
1. Choose the difficulty level and click 'Start Game' to generate a new puzzle.
2. To input a puzzle manually, simply click on a cell and type a number.
3. Click 'Solve' to solve the current puzzle.

## Contributing

Contributions to the Sudoku Solver are welcome. Please ensure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
