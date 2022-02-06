from ui.font_renderer import FontRenderer


class Score(FontRenderer):
    score: int = 0

    def __init__(self, color: str, initial_possition: tuple):
        super().__init__(color, initial_possition, f"Score: {self.score}")
    
    def IncreaseScore(self, amount: int = 10):
        self.score += amount
        super().setText(f"Score: {self.score}")