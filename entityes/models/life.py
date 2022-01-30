from turtle import Turtle


class Life(Turtle):
    def __init__(self, x_poss: int):
        super().__init__("player1.gif", 1, True)

        super().speed(0)
        super().hideturtle()
        super().penup()
        super().setposition(x_poss, -275)
        super().showturtle()