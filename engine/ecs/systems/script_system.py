from engine.ecs.systems.base_system import BaseSystem
from engine.ecs.components.script import Script


class ScriptSystem(BaseSystem):
    """
    Handles the execution of scripts attached to entities
    """
    
    def __init__(self, game):
        self.game = game


    def start(self):
        for entity in self.game.scene_manager.current_scene.entities:
            for component in entity.get_components():
                if isinstance(component, Script):
                    component.start()
                    

    def update(self, dt):
        for entity in self.game.scene_manager.current_scene.entities:
            for component in entity.get_components():
                if isinstance(component, Script):
                    component.update(dt)