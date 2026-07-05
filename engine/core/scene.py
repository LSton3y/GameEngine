from engine.core.entity import Entity
from engine.components.transform import Transform
from engine.components.sprite import Sprite


class Scene:
    """
    Stores all the entities in a scene
    """

    def __init__(self):
        sprite = Entity()
        sprite.add_component(Transform(50, 50))
        sprite.add_component(Sprite())

        self.entities = [sprite]