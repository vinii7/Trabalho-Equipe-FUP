from turtle import Turtle
from typing import List
from entityes.models.life import Life


class LifeSystem:
    vidas: List[Turtle] = []
    life_numb: int = None
    init_x_poss: int = 140
    life_spacing_offset = 60

    def __init__(self, life_numb = 2):
        self.life_numb = life_numb
    
    def Init(self):
        for _ in range(self.life_numb):
            self.vidas.append(Life(self.init_x_poss))
            self.init_x_poss += self.life_spacing_offset

    def LoseLife(self):
        self.life_numb -= 1
        self.vidas[self.life_numb].hideturtle()