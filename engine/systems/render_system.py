from engine.components.sprite import Sprite
from engine.components.sprite import Transform

from engine.systems.base_system import BaseSystem
from engine.managers.scene_manager import SceneManager

from engine.rendering.renderer import Renderer


class RenderSystem(BaseSystem):

    def update(self, dt):
        for entity in SceneManager.instance().entities:
            if entity.has_component(Sprite) and entity.has_component(Transform):
                Renderer.instance().draw_sprite(
                    entity.get_component(Transform),
                    entity.get_component(Sprite)
                )
