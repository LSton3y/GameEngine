from engine.math.vector2 import Vector2


class Transform:
    """
    Stores position, rotation and scale of an entity
    Attributes:
        position (Vector2): Vector2 representation of entity position
        rotation (int | float): Rotation of entity
        scale (Vector2): Vector2 representation of entity scale
    """
    
    def __init__(self, position: Vector2 = None, rotation: int | float = 0, scale: Vector2 = None) -> None:
        self.position = Vector2(0, 0) if position is None else position
        self.rotation = rotation
        self.scale = Vector2(0, 0) if scale is None else scale