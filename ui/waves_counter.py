from turtle import Turtle

from ui.font_renderer import FontRenderer


class WaveCounter(FontRenderer):
    wave: int = 1

    def __init__(self, color: str, initial_possition: tuple, font_size: int = 28):
        super().__init__(color, initial_possition, f"Wave: {self.wave}", font_size)
    
    def IncreaseWave(self, amount: int = 1):
        self.wave += amount
        super().setText(f"Wave: {self.wave}")