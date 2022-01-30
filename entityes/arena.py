from turtle import Turtle


class Arena(Turtle):
    def __init__(self):
        super().__init__(shape="arrow", undobuffersize=1, visible=True)
        super().speed(0)
        super().color('white')
        super().penup()
        super().setposition(-300, -300)
        super().pendown()
        super().pensize(3)
    
    def DrawnArena(self):
        for _ in range(4):
            super().forward(600)
            super().left(90)
        super().hideturtle()