from engine.core.entity import Entity
from engine.components.transform import Transform
from engine.components.sprite import Sprite
from engine.math.vector2 import Vector2
from game.scripts.player_movement import PlayerMovement


class Scene:
    """
    Stores all the entities in a scene
    Attributes:
        entities (list): List of the entites
    """

    def __init__(self):
        self._entities = []
    

    # Adds entity to scene
    def add_entity(self, entity):
        self._entities.append(entity)
    
    # Removes entity from scene
    def remove_entity(self, entity):
        self._entities.remove(entity)
    

    @property
    def entities(self):
        return self._entities