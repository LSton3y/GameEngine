from engine.components.transform import Transform
from engine.components.sprite import Sprite
from game.scripts.player_movement import PlayerMovement

COMPONENT_REGISTRY = {
    "Transform": Transform,
    "Sprite": Sprite,
    "PlayerMovement": PlayerMovement
}