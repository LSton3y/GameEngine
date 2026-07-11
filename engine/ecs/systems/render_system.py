import engine.core.game as g

from engine.ecs.components.sprite import Sprite
from engine.ecs.components.transform import Transform

from engine.ecs.systems.base_system import BaseSystem


class RenderSystem(BaseSystem):

    def update(self, dt):
        for entity in g.Game.instance().scene_manager.current_scene.query(Transform, Sprite):
            g.Game.instance().renderer.draw_sprite(
                entity.get_component(Transform),
                entity.get_component(Sprite)
            )
