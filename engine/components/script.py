from engine.systems.input_system import InputSystem
from engine.managers.input_manager import InputManager

from engine.components.transform import Transform
from engine.math.vector2 import Vector2


class Script:
    def __init__(self, entity):
        self.entity = entity


    def start(self):
        """Called the first frame the script runs."""
        pass

    
    def update(self, dt: float):
        """Called every frame."""
        pass

    
    @property
    def transform(self):
        self.entity.get_component(Transform)
