from ui.font_renderer import FontRenderer


class GameOverText(FontRenderer):
    game_over_text = "GAMEOVER"

    def __init__(self, color: str, initial_possition: tuple):
        super().__init__(color, initial_possition, self.game_over_text, 80)