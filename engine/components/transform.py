from engine.math.vector2 import Vector2


class Transform:
    """
    Stores position, rotation and scale of an entity
    Attributes:
        position (Vector2): Vector2 representation of entity position
        rotation (int | float): Rotation of entity
        scale (Vector2): Vector2 representation of entity scale
    """
    
    def __init__(self, position: Vector2 = Vector2(0, 0), rotation: int | float = 0, scale: Vector2 = Vector2(0, 0)) -> None:
        self.position = position
        self.rotation = rotation
        self.scale = scale