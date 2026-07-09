from engine.math.vector2 import Vector2
from engine.serialization.serializable import Serializable


class Transform(Serializable):
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
        self.scale = Vector2(1, 1) if scale is None else scale


    # Returns class with properties inherited from dict
    @classmethod
    def from_dict(cls, data):
        return cls(
            position=Vector2.from_dict(data["position"]),
            rotation=data["rotation"],
            scale=Vector2.from_dict(data["scale"])
        )