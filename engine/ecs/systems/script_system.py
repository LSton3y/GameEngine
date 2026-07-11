from engine.ecs.systems.base_system import BaseSystem
from engine.managers.scene_manager import SceneManager
from engine.ecs.components.script import Script


class ScriptSystem(BaseSystem):
    """
    Handles the execution of scripts attached to entities
    """
    
    def __init__(self, game):
        self.game = game


    def start(self):
        for script in self.game.scene_manager.current_scene.components():
            script.start()
                    

    def update(self, dt):
        for script in self.game.scene_manager.current_scene.components():
            script.update(dt)