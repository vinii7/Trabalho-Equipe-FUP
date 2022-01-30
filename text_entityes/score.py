from text_entityes.font_renderer import FontRenderer


class Score(FontRenderer):
    _score: int = 0

    def __init__(self, color: str, initial_possition: tuple):
        super().__init__(color, initial_possition, f"Score: {self._score}")
    
    def IncreaseScore(self, ammount: int = 10):
        self._score += ammount
        super().setText(f"Score: {self._score}")