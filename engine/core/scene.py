from engine.core.entity import Entity
from engine.components.transform import Transform
from engine.components.sprite import Sprite
from engine.math.vector2 import Vector2


class Scene:
    """
    Stores all the entities in a scene
    """

    def __init__(self):
        sprite = Entity()
        sprite.add_component(Transform(Vector2(150, 200), 50, Vector2(2, 1)))
        sprite.add_component(Sprite())

        self.entities = [sprite]