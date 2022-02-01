from enum import Enum
from turtle import Turtle

from entities.game_shapes import GameShapes
from entities.models.i_collideable import ICollideable

class LaserState(Enum):
    READY = 0
    FIRE = 1

#ICollideable is not implemented here
class Laser(Turtle, ICollideable):
    laser_speed: int = 3
    state: LaserState = LaserState.READY

    def __init__(self) -> None:
        super().__init__(GameShapes.laser_shape, 1, True)

        super().penup()
        super().speed(0)
        super().setheading(90)
        super().hideturtle()
        super().goto(-400, 0)
    
    def Fire(self, initial_location: int):
        if(self.state != LaserState.READY):
            return

        self.state = LaserState.FIRE
        super().setx(initial_location)
        super().sety(-180)
        super().showturtle()
    
    def Dispose(self):
        super().hideturtle()
        self.state = LaserState.READY
        super().goto(-400, 0)
    
    def GoUp(self):
        super().sety(super().ycor() + self.laser_speed)