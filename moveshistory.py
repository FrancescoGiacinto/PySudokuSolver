from typing import List, Tuple, Optional

class MovesHistory:
    """
    Maintains a history of moves for the Sudoku game to support undo and redo functionality.

    Attributes:
        history (list): A list of moves, where each move is a tuple (row, col, prev_value, new_value).
        current_index (int): The current position in the history for undo/redo operations.
    """

    def __init__(self) -> None:
        """
        Initializes the MovesHistory with an empty history.
        """
        self.history: List[Tuple[int, int, int, int]] = []
        self.current_index: int = -1

    def add_move(self, row: int, col: int, prev_value: int, new_value: int) -> None:
        """
        Adds a new move to the history.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
            prev_value (int): The previous value of the cell.
            new_value (int): The new value assigned to the cell.
        """
        if self.current_index < len(self.history) - 1:
            self.history = self.history[:self.current_index + 1]

        self.history.append((row, col, prev_value, new_value))
        self.current_index += 1
    

    def undo(self) -> Optional[Tuple[int, int, int]]:
        """
        Reverts the last move, if possible.

        Returns:
            Optional[Tuple[int, int, int]]: The move to be undone (row, col, prev_value), 
                                            or None if undo is not possible.
        """
        if self.current_index >= 0:
            move = self.history[self.current_index]
            self.current_index -= 1
            return move[0], move[1], move[2]  # row, col, prev_value
        return None

    def redo(self) -> Optional[Tuple[int, int, int]]:
        """
        Reapplies the next move, if possible.

        Returns:
            Optional[Tuple[int, int, int]]: The move to be redone (row, col, new_value), 
                                            or None if redo is not possible.
        """
        if self.current_index < len(self.history) - 1:
            self.current_index += 1
            move = self.history[self.current_index]
            return move[0], move[1], move[3]  # row, col, new_value
        return None

