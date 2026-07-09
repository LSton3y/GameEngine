from engine.core.entity import Entity

class Scene:
    """
    Stores all the entities in a scene
    Attributes:
        entities (list): List of the entites
    """

    def __init__(self):
        self._entities = []
    

    # Converts scene properties to dict
    def to_dict(self):
        return {
            "components": [e.to_dict() for e in self._entities]
        }

    # Returns class created from dict properties
    @classmethod
    def from_dict(cls, data, registry):
        scene = cls()
        scene._entities = [Entity.from_dict(e, registry) for e in data["entities"]]
        return scene


    # Adds entity to scene
    def add_entity(self, entity):
        self._entities.append(entity)
    
    # Removes entity from scene
    def remove_entity(self, entity):
        self._entities.remove(entity)
    

    @property
    def entities(self):
        return self._entities