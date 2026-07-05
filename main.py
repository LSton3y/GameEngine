from engine.components.transform import Transform
from engine.components.sprite import Sprite
from engine.rendering.renderer import Renderer


if __name__ == "__main__":
    ren = Renderer(500, 500)
    tra = Transform(100, 100)
    spr = Sprite()

    
    ren.clear()
    ren.draw_sprite(tra, spr)
    ren.present()