from engine.ecs.components.transform import Transform
from engine.core.entity import Entity
from engine.math.vector2 import Vector2

from typing import overload


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



@overload
def set_position(entity: Entity, position: Vector2) -> None: ...

@overload
def set_position(entity: Entity, x: int | float, y: int | float) -> None: ...


def set_position(
        entity: Entity,
        x: Vector2 | int | float, 
        y: int | float | None = None
    ) -> None:
    """Sets the position of an entity"""
    transform: Transform = entity.get_component(Transform)

    if transform is None:
        return
    
    if isinstance(x, Vector2):
        transform.position = x
    else:
        if y is None:
            raise TypeError("Y must be provided when X is not a Vector2.")
        transform.position = Vector2(x, y)



def set_rotation(entity: Entity, rotation: int | float):
    """Sets the rotation of an entity"""
    transform: Transform = entity.get_component(Transform)

    if transform is not None:
        transform.rotation = rotation



@overload
def set_scale(entity: Entity, scale: Vector2) -> None: ...

@overload
def set_scale(entity: Entity, x: int | float, y: int | float) -> None: ...


def set_scale(
        entity: Entity, 
        x: Vector2 | int | float, 
        y: int | float | None = None
    ) -> None:
    """Sets the scale of an entity"""
    transform: Transform = entity.get_component(Transform)

    if transform is None:
        return
    
    if isinstance(x, Vector2):
        transform.scale = x
    else:
        if y is None:
            raise TypeError("Y must be provided when X is not a Vector2.")
        transform.scale = Vector2(x, y)



@overload
def move(entity: Entity, position: Vector2) -> None: ...

@overload
def move(entity: Entity, x: int | float, y: int | float) -> None: ...


def move(
        entity: Entity, 
        x: Vector2 | int | float,
        y: int | float | None = None
    ) -> None:
    """Moves an entity by an x and y value"""
    transform: Transform = entity.get_component(Transform)

    if transform is None:
        return
    
    if isinstance(x, Vector2):
        transform.position += x
    else:
        if y is None:
            raise TypeError("Y must be provided when X is not a Vector2.")
        transform.position += Vector2(x, y)



def rotate(entity: Entity, rotation: int | float):
    """Rotates an entity by a value"""
    transform: Transform = entity.get_component(Transform)

    if transform is not None:
        transform.rotation += rotation



@overload
def scale_by(entity: Entity, scale: Vector2) -> None: ...

@overload
def scale_by(entity: Entity, x: int | float, y: int | float) -> None: ...


def scale_by(
        entity: Entity,
        x: Vector2 | int | float, 
        y: int | float | None = None
    ) -> None: 
    """Scales an entity by an X and Y value"""
    transform: Transform = entity.get_component(Transform)

    if transform is None:
        return
    
    if isinstance(x, Vector2):
        transform.scale *= x
    else:
        if y is None:
            raise TypeError("Y must be provided when X is not a Vector2.")
        transform.scale *= Vector2(x, y)


#TODO: Make parenting functions and actually implement it :< 