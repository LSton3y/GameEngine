from typing import ClassVar
from math import sqrt


class Vector2:

    # Type hinting for instance variables
    x: int | float
    y: int | float

    # Type hinting for static class variables
    up: ClassVar[Vector2]
    down: ClassVar[Vector2]
    left: ClassVar[Vector2]
    right: ClassVar[Vector2]


    
    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = x
        self.y = y


    # region Vector2 Operations
    # Overrides standard "*" multiplication
    def __mul__(self, scalar: int | float | Vector2) -> Vector2:
        if isinstance(scalar, (int, float)):
            # Return new Vector2 with multiplied components
            return Vector2(self.x * scalar, self.y * scalar)
        
        elif isinstance(scalar, Vector2):
            # Return new Vector2 with multiplied vectors
            return Vector2(self.x * scalar.x, self.y * scalar.y)
        
        return ValueError


    # Handles reverse multiplication
    def __rmul__(self, scalar: int | float | Vector2) -> Vector2:
        return self.__mul__(scalar)
    


    # Overrides standard "/" division
    def __truediv__(self, scalar: int | float | Vector2) -> Vector2:
        if isinstance(scalar, (int, float)):
            # Return new Vector2 with divided components
            return Vector2(self.x / scalar, self.y / scalar)
        
        elif isinstance(scalar, Vector2):
            # Return new Vector2 with divided vectors
            return Vector2(self.x / scalar.x, self.y / scalar.y)

        return ValueError
    

    # Handles reverse division
    def __rtruediv__(self, scalar: int | float | Vector2) -> Vector2:
        return self.__truediv__(scalar)

    

    # Overrides standard "+" addition
    def __add__(self, addition: Vector2) -> Vector2:
        if isinstance(addition, Vector2):
            # Return new Vector2 with result of addition
            return Vector2(self.x + addition.x, self.y + addition.y)

        return ValueError
    

    # Overrides standard "-" subtraction
    def __sub__(self, subtraction: Vector2) -> Vector2:
        if isinstance(subtraction, Vector2):
            # Return new Vector2 with result of subtraction
            return Vector2(self.x - subtraction.x, self.y - subtraction.y)
        
        return ValueError
    #endregion
    

    # Normalizes vectors
    def normalize(self) -> Vector2:
        magnitude = sqrt(self.x ** 2 + self.y ** 2)

        # Avoid division by zero error
        if magnitude == 0:
            return Vector2(0, 0)
        
        return Vector2(self.x / magnitude, self.y / magnitude)



    # Handles how Vector2 is outputted
    def __repr__(self) -> str:
        return f"Vector2({self.x}, {self.y})"



# Static default Vector2 tuples
Vector2.up = Vector2(0, 1)
Vector2.down = Vector2(0, -1)
Vector2.right = Vector2(1, 0)
Vector2.left = Vector2(-1, 0)