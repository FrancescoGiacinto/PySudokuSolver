import unittest
from grid import Grid
from solver import Solver
from puzzlegenerator import PuzzleGenerator
from moveshistory import MovesHistory


class TestSudokuComponents(unittest.TestCase):

    def test_moves_history_add_move(self):
        history = MovesHistory()
        history.add_move(0, 0, 0, 1)
        self.assertEqual(history.history, [(0, 0, 0, 1)])
        self.assertEqual(history.current_index, 0)

    def test_moves_history_undo(self):
        history = MovesHistory()
        history.add_move(0, 0, 0, 1)
        history.add_move(1, 1, 0, 2)
        undo_move = history.undo()
        self.assertEqual(undo_move, (1, 1, 0))
        self.assertEqual(history.current_index, 0)

    def test_moves_history_redo(self):
        history = MovesHistory()
        history.add_move(0, 0, 0, 1)
        history.add_move(1, 1, 0, 2)
        history.undo()
        redo_move = history.redo()
        self.assertEqual(redo_move, (1, 1, 2))
        self.assertEqual(history.current_index, 1)

    def test_solver_solves_correctly(self):
        grid = Grid()
        solver = Solver()
        self.assertTrue(solver.solve(grid))
    
    def test_grid_initialization(self):
        grid = Grid()
        for row in grid.cells:
            for cell in row:
                self.assertEqual(cell.value, 0, "Grid should be initialized with all cells set to 0")


    def test_solver(self):
        grid = Grid()
        solver = Solver()
        # You might need to set up a specific puzzle state here
        # Then test if the solver can solve it
        self.assertTrue(solver.solve(grid))

    def test_puzzle_generator(self):
        grid = Grid()
        generator = PuzzleGenerator(grid)
        puzzle = generator.generate(difficulty="easy")
        # Test the generated puzzle for correct difficulty, 
        # such as the number of prefilled cells

    def test_undo_redo_functionality(self):
        # Test the functionality of MovesHistory
        # by simulating some moves and then undoing and redoing them
        pass

    # Add more tests for other components and functionalities

if __name__ == '__main__':
    unittest.main()
