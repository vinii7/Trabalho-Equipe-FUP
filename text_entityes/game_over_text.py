from text_entityes.font_renderer import FontRenderer


class GameOverText(FontRenderer):
    def __init__(self, color: str, initial_possition: tuple, text: str):
        super().__init__(color, initial_possition, text, 80)