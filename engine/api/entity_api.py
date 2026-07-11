from engine.core.game import Game
from engine.core.entity import Entity


def create_entity(name: str) -> Entity:
    """Creates a new entity into the scene and returns it"""
    return Game.instance().scene_manager.current_scene.add_entity(Entity(name))


def remove_entity(id: int):
    """Removes an entity from the scene based on id"""
    pass