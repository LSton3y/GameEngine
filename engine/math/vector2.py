from typing import ClassVar
from math import sqrt


class Vector2:
    """
    Stores an x and y value that can be used for position or scale
    Attributes:
        x (int | float): X coordinate value
        y (int | float): Y coordinate value
    """

    # Type hinting for instance variables
    x: int | float
    y: int | float

    # Type hinting for static class variables
    up: ClassVar[Vector2]
    down: ClassVar[Vector2]
    left: ClassVar[Vector2]
    right: ClassVar[Vector2]


    # region Vector2 Dunders
    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = x
        self.y = y

    # Handles how Vector2 is outputted
    def __repr__(self) -> str:
        return f"Vector2({self.x}, {self.y})"
    

    # Handles how Vector2 is compared
    def __eq__(self, other):
        if not isinstance(other, Vector2):
            return NotImplemented
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))
    #endregion


    # region Vector2 Operations
    # Overrides standard "*" multiplication
    def __mul__(self, scalar: int | float | Vector2) -> Vector2:
        if isinstance(scalar, (int, float)):
            # Return new Vector2 with multiplied components
            return Vector2(self.x * scalar, self.y * scalar)
        
        elif isinstance(scalar, Vector2):
            # Return new Vector2 with multiplied vectors
            return Vector2(self.x * scalar.x, self.y * scalar.y)
        
        raise ValueError("Value must be either an integer, a float, or a Vector2.")


    # Handles reverse multiplication
    def __rmul__(self, scalar: int | float | Vector2) -> Vector2:
        return self.__mul__(scalar)
    


    # Overrides standard "/" division
    def __truediv__(self, scalar: int | float | Vector2) -> Vector2:
        if isinstance(scalar, (int, float)):
            if scalar == 0:
                raise ValueError("Cannot divide by zero.")
            else:
                # Return new Vector2 with divided components
                return Vector2(self.x / scalar, self.y / scalar)
        
        elif isinstance(scalar, Vector2):
            if scalar.x == 0 or scalar.y == 0:
                raise ValueError("Cannot divide by zero.")
            else:
                # Return new Vector2 with divided vectors
                return Vector2(self.x / scalar.x, self.y / scalar.y)

        raise ValueError("Value must be either an integer, a float, or a Vector2.")
    

    # Handles reverse division
    def __rtruediv__(self, scalar: int | float | Vector2) -> Vector2:
        # Reverse division with int or float
        if isinstance(scalar, (int, float)):
            if self.x == 0 or self.y == 0:
                raise ValueError("Cannot divide by zero.")
            return Vector2(scalar / self.x, scalar / self.y)

        raise ValueError("Value must be either an integer, a float, or a Vector2.")

    

    # Overrides standard "+" addition
    def __add__(self, addition: Vector2) -> Vector2:
        if isinstance(addition, Vector2):
            # Return new Vector2 with result of addition
            return Vector2(self.x + addition.x, self.y + addition.y)

        raise ValueError("Value must be a Vector2.")
    

    # Overrides standard "-" subtraction
    def __sub__(self, subtraction: Vector2) -> Vector2:
        if isinstance(subtraction, Vector2):
            # Return new Vector2 with result of subtraction
            return Vector2(self.x - subtraction.x, self.y - subtraction.y)
        
        raise ValueError("Value must be a Vector2.")
    #endregion
    

    # region Vector2 Methods
    # Normalizes vectors
    def normalize(self) -> Vector2:
        magnitude = sqrt(self.x ** 2 + self.y ** 2)

        # Avoid division by zero error
        if magnitude == 0:
            return Vector2(0, 0)
        
        return Vector2(self.x / magnitude, self.y / magnitude)
    

    # Converts Vector2 to tuple
    def to_tuple(self) -> tuple:
        return (self.x, self.y)
    #endregion



# Static default Vector2 tuples
Vector2.up = Vector2(0, 1)
Vector2.down = Vector2(0, -1)
Vector2.right = Vector2(1, 0)
Vector2.left = Vector2(-1, 0)