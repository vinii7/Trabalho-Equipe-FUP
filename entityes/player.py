from turtle import Turtle, register_shape


class Player(Turtle):
    speed: int = 0

    def __init__(self):
        super().__init__("player1.gif", 1, True)
        super().penup()
        super().speed(0)
        super().setposition(0, -200)
        super().setheading(90)