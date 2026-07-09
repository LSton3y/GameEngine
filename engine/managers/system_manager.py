from engine.systems.input_system import InputSystem
from engine.systems.physics_system import PhysicsSystem
from engine.systems.render_system import RenderSystem


class SystemManager:
    """
    Stores all the systems
    
    Controls the update loop of the systems
    """

    def __init__(self):
        self._systems = [
            InputSystem(),
            PhysicsSystem(),
            RenderSystem()
        ]
    

    # Runs the update loop for each system
    def update(self,dt):
        for system in self._systems:
            system.update(dt)