from engine.ecs.systems.base_system import BaseSystem

class PhysicsSystem(BaseSystem):
    
    def __init__(self, game):
        self.game = game