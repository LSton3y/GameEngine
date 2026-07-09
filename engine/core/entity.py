from engine.components.script import Script

class Entity:
    """
    Base object in the game engine.
    
    Can store components like Transform, Sprite, etc.
    """

    def __init__(self, name="Entity"):
        self.name = name
        self._components = {} # type -> component reference
    

    # Converts entity properties to dict
    def to_dict(self):
        return {
            "name": self.name,
            "components": {
                type(c).__name__: c.to_dict()
                for c in self._components.values()
            }
        }


    # Returns class created from dict properties
    @classmethod
    def from_dict(cls, data, registry):
        entity = cls(name=data.get("name", "Entity"))

        for name, component_data in data["components"].items():
            component_class = registry[name]

            # Different parameters if component is Script
            if issubclass(component_class, Script):
                component = component_class.from_dict(component_data, entity)
            else:
                component = component_class.from_dict(component_data)
                
            entity.add_component(component)

        return entity

    
    # Adds component to entity
    def add_component(self, component) -> dict:
        self._components[type(component)] = component
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