from enum import Enum
from turtle import Turtle

from entities.game_shapes import GameShapes
from system_managers.sound_manager import SoundManager
from utils.collideable import Collideable
from utils.void_object_coordinates import VoidObjectCoordinates

class LaserState(Enum):
    READY = 0
    FIRE = 1

#Collideable is not implemented here
class Laser(Turtle, Collideable):
    _laser_speed: int = 3
    _state: LaserState = LaserState.READY

    def __init__(self) -> None:
        super().__init__(GameShapes.laser_shape, 1, True)

        super().penup()
        super().speed(0)
        super().setheading(90)
        super().hideturtle()
        super().goto(VoidObjectCoordinates.LASER_COORDINATE)
    
    def Fire(self, initial_location: int):
        if(self._state != LaserState.READY):
            return

        self._state = LaserState.FIRE
        super().setx(initial_location)
        super().sety(-180)
        super().showturtle()
        SoundManager.PlayLaserSong()
    
    def Dispose(self):
        super().hideturtle()
        super().goto(VoidObjectCoordinates.LASER_COORDINATE)
        self._state = LaserState.READY
    
    def GoUp(self):
        super().sety(super().ycor() + self._laser_speed)