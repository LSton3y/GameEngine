from engine.core.game import Game
from engine.core.entity import Entity


def create(name: str) -> Entity:
    """Creates a new entity into the scene and returns it"""
    return Game.instance().scene_manager.current_scene.add_entity(Entity(name))


def destroy(entity: Entity):
    """Removes an entity from the scene"""
    Game.instance().scene_manager.current_scene.remove_entity(entity)


def find(name: str) -> Entity | None:
    """Returns an entity based on name"""
    for entity in Game.instance().scene_manager.current_scene.entities:
        if entity.name == name:
            return entity


def enable(entity: Entity):
    """Enables an entity"""
    entity.enabled = True


def disable(entity: Entity):
    """Disables an entity"""
    entity.enabled = False