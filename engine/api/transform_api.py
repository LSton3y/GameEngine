from engine.ecs.components.transform import Transform
from engine.core.entity import Entity
from engine.math.vector2 import Vector2


def position(entity: Entity):
    """Returns the transform position of an entity"""
    transform: Transform = entity.get_component(Transform)

    if transform is None:
        return None
    else:
        return transform.position


def rotation(entity: Entity):
    """Returns the transform rotation of an entity"""
    transform: Transform = entity.get_component(Transform)

    if transform is None:
        return None
    else:
        return transform.rotation


def scale(entity: Entity):
    """Returns the transform scale of an entity"""
    transform: Transform = entity.get_component(Transform)

    if transform is None:
        return None
    else:
        return transform.scale


def set_position(entity: Entity, x: int | float, y: int | float):
    """Sets the position of an entity"""
    transform: Transform = entity.get_component(Transform)

    if transform is not None:
        transform.position = Vector2(x, y)


def set_rotation(entity: Entity, rotation: int | float):
    """Sets the rotation of an entity"""
    transform: Transform = entity.get_component(Transform)

    if transform is not None:
        transform.rotation = rotation


def set_scale(entity: Entity, x: int | float, y: int | float):
    """Sets the scale of an entity"""
    transform: Transform = entity.get_component(Transform)

    if transform is not None:
        transform.scale = Vector2(x, y)


def move(entity: Entity, x: int | float, y: int | float):
    """Moves an entity by an x and y value"""
    transform: Transform = entity.get_component(Transform)

    if transform is not None:
        transform.position += Vector2(x, y)


def rotate(entity: Entity, rotation: int | float):
    """Rotates an entity by a value"""
    transform: Transform = entity.get_component(Transform)

    if transform is not None:
        transform.rotation += rotation


def scale(entity: Entity, x: int | float, y: int | float):
    """Scales an entity by an X and Y value"""
    transform: Transform = entity.get_component(Transform)

    if transform is not None:
        transform.scale *= Vector2(x, y)


#TODO: Make parenting functions and actually implement it :< 