from turtle import Turtle
from entities.game_shapes import GameShapes
from utils.collideable import Collideable

#Collideable is not implemented here
class Enemy(Turtle, Collideable):
    def __init__(self):
        super().__init__(GameShapes.alien_shape, 1, True)

        super().speed(0)
        super().penup()