from engine.core.game import Game
from engine.core.entity import Entity


def add(entity: Entity, component):
    """Adds a component to specified entity"""
    return entity.add_component(component())


def remove(entity: Entity, component):
    """Removes a component from specified entity"""
    entity.remove_component(component)


def get(entity: Entity, component):
    """Returns the component in specified entity"""
    return entity.get_component(component)


def has(entity: Entity, component):
    """Returns if a component is in an entity"""
    return entity.has_component(component)