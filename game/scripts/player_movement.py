from engine.components.script import Script
from engine.math.vector2 import Vector2


class PlayerMovement(Script):
    
    def start(self):
        self.speed = 5

    
    def update(self, dt):
        movement = Vector2(0, 0)

        if input.is_action_down("left"):
            movement.x = -1
        if input.is_action_down("right"):
            movement.x = 1
        if input.is_action_down("up"):
            movement.y = -1
        if input.is_action_down("down"):
            movement.y = 1
        
        movement = movement.normalize()

        self.transform.position = movement * self.speed