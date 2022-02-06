from turtle import Turtle, listen, onkeypress

from entities.game_shapes import GameShapes
from utils.collideable import Collideable
from entities.laser import Laser

#Collideable is not implemented here
class Player(Turtle, Collideable):
    name: str
    speed: float = 0.3
    laser: Laser

    def __init__(self, name: str):
        super().__init__(GameShapes.player_shape, 1, True)
        super().penup()
        super().speed(0)
        super().setposition(0, -200)
        super().setheading(90)

        self.laser = Laser()
        self.name = name
    
    def ConfigureKeyBindings(self):
        listen()
        onkeypress(self.MoveLeft, 'Left')
        onkeypress(self.MoveRight, 'Right')
        onkeypress(self.FireLaser, 'space')

    #region Moviments and Actions
    def MoveLeft(self):
        self.speed = -0.5
    def MoveRight(self):
        self.speed = 0.5

    def UpdatePlayerState(self):
        #Posição do player
        x = super().xcor() + self.speed
        if(x < -277):
            x = -277
        elif(x > 277):
            x = 277
        super().setx(x)

        #Posição do laser
        self.laser.GoUp()

    def FireLaser(self):
        self.laser.Fire(self.xcor())
    #endregion