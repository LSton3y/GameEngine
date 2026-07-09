from engine.systems.input_system import InputSystem
from engine.components.transform import Transform



class Script:
    # Attributes which shouldn't be serialized
    _exclude_from_dict = {"entity"}


    def __init__(self, entity):
        self.entity = entity


    def start(self):
        """Called the first frame the script runs."""
        pass

    
    def update(self, dt: float):
        """Called every frame."""
        pass

    
    # Serialization
    def to_dict(self):
        data = {}
        for key, value in self.__dict__.items():
            if key in self._exclude_from_dict:
                continue
            # Handle nested objects that know how to serialize themselves (e.g. Vector2)
            data[key] = value.to_dict() if hasattr(value, "to_dict") else value

        return data

    @classmethod
    def from_dict(cls, data, entity):
        instance = cls(entity)
        instance.__dict__.update(data)

        return instance

    
    @property
    def transform(self):
        return self.entity.get_component(Transform)

    @property
    def input(self):
        return InputSystem.instance()
