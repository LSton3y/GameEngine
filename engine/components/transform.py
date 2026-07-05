# Transform class

# Stores Vector2 position and scale
# Stores rotation as a float

# Handles appearance and location of an entity

from engine.math.vector2 import Vector2



class Transform:
    
    def __init__(self) -> None:
        self.position = Vector2(0, 0)
        self.rotation = 0
        self.scale = Vector2(0, 0)