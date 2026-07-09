from engine.systems.input_system import InputSystem
from engine.components.transform import Transform



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
        return self.entity.get_component(Transform)

    @property
    def input(self):
        return InputSystem.instance()
