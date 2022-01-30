from turtle import Turtle


class FontRenderer(Turtle):
    text: str = "None"
    font_size: int = 28

    def __init__(self, color: str, initial_possition: tuple, text: str, font_size: int = 28):
        super().__init__("arrow", 1, True)

        super().speed(0)
        super().penup()
        super().color(color)

        super().setposition(initial_possition)
        super().hideturtle()

        self.text = text
        self.font_size = font_size

    def Drawn(self):
        super().write(self.text, False, align='left', font=('Atari Small', self.font_size, 'normal'))
    
    def setText(self, text: str, update: bool = True):
        self.text = text
        
        if(update):
            super().clear()
            self.Drawn()