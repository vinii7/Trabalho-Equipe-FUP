from turtle import register_shape

class GameShapes:
    player_shape: str = "assets/images/player1.gif"
    alien_shape: str = "assets/images/alien1.gif"
    laser_shape: str = "assets/images/laser1.gif"

    @staticmethod
    def InitAllShapes():
        register_shape('assets/images/player1.gif')
        register_shape('assets/images/alien1.gif')
        register_shape('assets/images/laser1.gif')