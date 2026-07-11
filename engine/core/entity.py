from engine.serialization.serializable import Serializable
from engine.ecs.components.component import Component
from engine.serialization.registry import Registry


class Entity(Serializable):
    """
    Base object in the game engine.
    
    Can store components like Transform, Sprite, etc.
    """

    def __init__(self, name="Entity"):
        self.name = name
        self.enabled = True # TODO: Add functionality to this
        self._components = {} # type -> component reference
    

    # Adds component to entity
    def add_component(self, component):
        self._components[type(component)] = component

        setattr(
            self,
            type(component).__name__.lower(),
            component
        )   

        return component # Allows for chaining, e.g. entity.add_component(Transform).x

    # Removes component from entity
    def remove_component(self, component_type) -> None:
        self._components.pop(component_type, None)
    
    # Gets component from entity
    def get_component(self, component_type):
        return self._components.get(component_type)

    # Gets all components from entity
    def get_components(self):
        return self._components.values()

    # Checks if component is in entity
    def has_component(self, component_type):
        return component_type in self._components
    

    # Returns Entity class from dict properties
    @classmethod
    def from_dict(cls, data):
        entity = cls(data["name"]) # Initialise entity class

        # Add all components in dict to entity 
        for component_name, component_values in data.get("_components", {}).items():
            component_class = Registry.get(component_name)
            component = component_class.from_dict(component_values, entity)

            entity.add_component(component)
        
        return entity
