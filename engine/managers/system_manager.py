from engine.ecs.systems.input_system import InputSystem
from engine.ecs.systems.physics_system import PhysicsSystem
from engine.ecs.systems.render_system import RenderSystem
from engine.ecs.systems.script_system import ScriptSystem


class SystemManager:
    """
    Stores all the systems
    
    Controls the update loop of the systems
    """

    def __init__(self):
        self._systems = [
            InputSystem(self),
            PhysicsSystem(self),
            ScriptSystem(self),
            RenderSystem(self)
        ]
    
    
    # Runs on the first frame
    def start(self):
        for system in self._systems:
            system.start()


    # Runs the update loop for each system
    def update(self, dt):
        for system in self._systems:
            system.update(dt)