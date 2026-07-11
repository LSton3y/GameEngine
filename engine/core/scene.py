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
    
    # Retuns all the entites that have certain components
    def query(self, *components):
        for entity in self._entities:
            if all(entity.has_component(c) for c in components):
                yield entity

    @property
    def entities(self):
        return self._entities
    

    # Creates scene from properties
    @classmethod
    def from_dict(cls, data):
        obj = cls()

        # Loop through each entity in dict
        for entity in data.get("_entities", {}):
            obj.add_entity(Entity.from_dict(entity))
        
        return obj