from engine.ecs.systems.base_system import BaseSystem
from engine.managers.scene_manager import SceneManager
from engine.ecs.components.script import Script


class ScriptSystem(BaseSystem):
    """
    Handles the execution of scripts attached to entities
    """

    def start(self):
        for entity in SceneManager.instance().current_scene.entities:
            for component in entity.get_components():
                if isinstance(component, Script):
                    component.start()
                    

    def update(self, dt):
        for entity in SceneManager.instance().current_scene.entities:
            for component in entity.get_components():
                if isinstance(component, Script):
                    component.update(dt)