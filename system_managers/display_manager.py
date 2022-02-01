from time import sleep
import turtle

from ui.game_over_text import GameOverText

class DisplayManager():
    @staticmethod
    def InitDisplay():
        turtle.Screen().setup(700, 700)
        turtle.Screen().title('Space Invaders')
        turtle.Screen().bgcolor('black')
        turtle.Screen().tracer(0)
    
    @staticmethod
    def ClearDisplay():
        turtle.Screen().clear()
    
    @staticmethod
    def UpdateDisplay():
        turtle.Screen().update()

    @staticmethod
    def GameOverScreen():
        DisplayManager.ClearDisplay()
        game_over_text = GameOverText("black", (-200, 0))
        game_over_text.Drawn()
        sleep(3)
        exit()
