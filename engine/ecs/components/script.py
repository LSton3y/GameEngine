from engine.ecs.systems.input_system import InputSystem
from engine.ecs.components.transform import Transform
from engine.ecs.components.component import Component


class Script(Component):
    _exclude = {"entity"}


    def __init__(self, entity):
        self.entity = entity


    def start(self):
        """Called the first frame the script runs."""
        pass

    
    def update(self, dt: float):
        """Called every frame."""
        pass

    
    # Converts data properties to Script class
    @classmethod
    def from_dict(cls, data, entity):
        obj = cls(entity)

        for key, value in data.items():
            setattr(obj, key, value)

        return obj

    
    @property
    def transform(self):
        return self.entity.get_component(Transform)
