from engine.serialization.serializable import Serializable
from engine.core.entity import Entity


class Scene(Serializable):
    """
    Stores all the entities in a scene
    Attributes:
        entities (list): List of the entites
    """

    def __init__(self):
        self._entities = []


    # Adds entity to scene
    def add_entity(self, entity):
        self._entities.append(entity)
    
    # Removes entity from scene
    def remove_entity(self, entity):
        self._entities.remove(entity)
    

    @property
    def entities(self):
        return self._entities
    

    # Creates scene from properties
    @classmethod
    def from_dict(cls, data, registry):
        obj = cls()

        # Loop through each entity in dict
        for entity in data.get("_entities", {}):
            obj.add_entity(Entity.from_dict(entity, registry))
        
        return obj