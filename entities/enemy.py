from turtle import Turtle
from entities.game_shapes import GameShapes
from entities.models.i_collideable import ICollideable

#ICollideable is not implemented here
class Enemy(Turtle, ICollideable):
    def __init__(self):
        super().__init__(GameShapes.alien_shape, 1, True)

        super().speed(0)
        super().penup()