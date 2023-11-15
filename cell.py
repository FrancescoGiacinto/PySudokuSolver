class Cell:
    """
    Represents a single cell in a Sudoku grid.

    Attributes:
        value (int): The number stored in the cell, 0 if the cell is empty.
        fixed (bool): Indicates whether the cell's value is fixed (part of the original puzzle) and cannot be changed.
        possible_values (set): A set of possible values that can be assigned to the cell based on the game rules.

    Methods:
        set_value(value): Sets the cell's value.
        remove_possible_value(value): Removes a value from the set of possible values.
    """

    def __init__(self, value: int = 0 , fixed : bool = False) -> None:
        """
        Constructs a Cell with a specified value and fixed status.

        Args:
            value (int, optional): The value to be assigned to the cell. Defaults to 0, indicating an empty cell.
            fixed (bool, optional): True if the cell's value is part of the original puzzle. Defaults to False.
        """
        self.value = value
        self.fixed = fixed
        self.possible_values = set(range(1, 10)) if not fixed else set()

    def set_value(self, value : int ) -> None:
        """
        Sets the cell's value. If the cell is fixed, raises a ValueError.

        Args:
            value (int): The value to be assigned to the cell.

        Raises:
            ValueError: If trying to set the value of a fixed cell.
        """
        if not self.fixed:
            self.value = value
            self.possible_values.clear()
        else:
            raise ValueError("Cannot change the value of a fixed cell.")

    def remove_possible_value(self, value: int) -> None:
        """
        Removes a possible value from the set of possible values for the cell.

        This method is useful in the process of solving the Sudoku, where
        the elimination of possible values is a common strategy.

        Args:
            value (int): The value to be removed from possible values.
        """
        self.possible_values.discard(value)
