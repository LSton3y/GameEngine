from typing import ClassVar

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


    # Overides standard "*" tuple multiplication
    def __mul__(self, scalar: int | float) -> Vector2:
        if isinstance(scalar, (int, float)):
            # Return new Vector2 with multiplied components
            return Vector2(self.x * scalar, self.y * scalar)
        
        return NotImplemented


    # Handles reverse multiplication
    def __rmul__(self, scalar: int | float) -> Vector2:
        return self.__mul__(scalar)


    # Handles how Vector2 is outputted
    def __repr__(self) -> str:
        return f"Vector2({self.x}, {self.y})"



# Static default Vector2 tuples
Vector2.up = Vector2(0, 1)
Vector2.down = Vector2(0, -1)
Vector2.right = Vector2(1, 0)
Vector2.left = Vector2(-1, 0)