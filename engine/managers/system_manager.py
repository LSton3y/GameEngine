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
        self.input_system = InputSystem()
        self.physics_system = PhysicsSystem()
        self.script_system = ScriptSystem()
        self.render_system = RenderSystem()

        self._systems = [
            self.input_system,
            self.physics_system,
            self.script_system,
            self.render_system,
        ]
    
    
    # Runs on the first frame
    def start(self):
        for system in self._systems:
            system.start()


    # Runs the update loop for each system
    def update(self, dt):
        for system in self._systems:
            system.update(dt)
