class Entity:
    """
    Base object in the game engine.
    
    Can store components like Transform, Sprite, etc.
    """

    def __init__(self):
        self.components = {} # type -> component reference

    
    # Adds component to entity
    def add_component(self, component) -> dict:
        self.components[type(component)] = component
        return component # Allows for chaining, e.g. entity.add_component(Transform).x

    # Removes component from entity
    def remove_component(self, component_type) -> None:
        self.components.pop(component_type, None)
    
    # Gets component from entity
    def get_component(self, component_type):
        return self.components.get(component_type)

    # Checks if component is in entity
    def has_component(self, component_type):
        return component_type in self.components