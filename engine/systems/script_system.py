from engine.systems.base_system import BaseSystem
from engine.managers.scene_manager import SceneManager
from engine.components.script import Script


class ScriptSystem(BaseSystem):
    """
    Handles the execution of scripts attached to entities
    """

    def update(self, dt):
        for entity in SceneManager.instance().current_scene.entities:
            if entity.has_component(Script):
                entity.get_component(Script).update(dt)