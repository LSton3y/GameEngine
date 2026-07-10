from engine.systems.input_system import InputSystem
from engine.components.transform import Transform
from engine.serialization.serializable import Serializable


class Script(Serializable):
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

    @property
    def input(self):
        return InputSystem.instance()
