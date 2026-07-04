class Vector2:

    # # Static default Vector2 tuples
    # up = Vector2(0, 1)
    # down = Vector2(0, -1)
    # right = Vector2(1, 0)
    # left = Vector2(-1, 0)

    
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


    # Overides standard "*" tuple multiplication
    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            # Return new Vector2 with multiplied components
            return Vector2(self.x * scalar, self.y * scalar)
        
        return NotImplemented


    # Handles reverse multiplication
    def __rmul__(self, scalar):
        return self.__mul__(scalar)


    # Handles how Vector2 is outputted
    def __repr__(self):
        return f"Vector2({self.x}, {self.y})"

