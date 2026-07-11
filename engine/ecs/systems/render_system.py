from engine.ecs.components.sprite import Sprite
from engine.ecs.components.transform import Transform

from engine.ecs.systems.base_system import BaseSystem


class RenderSystem(BaseSystem):

    def __init__(self, game):
        self.game = game

    def update(self, dt):
        for entity in self.game.scene_manager.current_scene.entities:
            if entity.has_component(Sprite) and entity.has_component(Transform):
                self.game.renderer.draw_sprite(
                    entity.get_component(Transform),
                    entity.get_component(Sprite)
                )
