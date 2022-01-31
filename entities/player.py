from turtle import Shape, Turtle

from entities.game_shapes import GameShapes


class Player(Turtle):
    speed: int = 0

    def __init__(self):
        super().__init__(GameShapes.player_shape, 1, True)
        super().penup()
        super().speed(0)
        super().setposition(0, -200)
        super().setheading(90)