from turtle import Turtle

from entities.game_shapes import GameShapes


class Life(Turtle):
    def __init__(self, x_poss: int):
        super().__init__(GameShapes.player_shape, 1, True)

        super().speed(0)
        super().hideturtle()
        super().penup()
        super().setposition(x_poss, -275)
        super().showturtle()