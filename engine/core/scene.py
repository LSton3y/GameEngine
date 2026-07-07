from engine.core.entity import Entity
from engine.components.transform import Transform
from engine.components.sprite import Sprite
from engine.math.vector2 import Vector2

from engine.systems.input_system import InputSystem
from engine.systems.physics_system import PhysicsSystem
from engine.systems.render_system import RenderSystem


class Scene:
    """
    Stores all the entities in a scene
    Attributes:
        entities (list): List of the entites
    """

    def __init__(self):
        # TODO: Add a parameter that loads entities into the self.entities
        sprite = Entity()
        sprite.add_component(Transform(Vector2(150, 200)))
        sprite.add_component(Sprite())

        self._entities = [sprite]
        self._systems = [
            InputSystem(),
            PhysicsSystem(),
            RenderSystem()
        ]
    

    # Adds entity to scene
    def add_entity(self, entity):
        self._entities.append(entity)
    
    # Removes entity from scene
    def remove_entity(self, entity):
        self._entities.remove(entity)
    

    @property
    def entities(self):
        return self._entities

    @property
    def systems(self):
        return self._systems