from engine.core.game import Game
from engine.core.entity import Entity


def create(name: str) -> Entity:
    """Creates a new entity into the scene and returns it"""
    return Game.instance().scene_manager.current_scene.add_entity(Entity(name))


def destroy(entity: Entity):
    """Removes an entity from the scene"""
    pass


def find(name: str):
    """Returns an entity based on name"""
    pass


def enable(entity: Entity):
    """Enables an entity"""
    pass


def disable(entity: Entity):
    """Disables an entity"""
    pass