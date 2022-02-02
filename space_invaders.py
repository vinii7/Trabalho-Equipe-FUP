# Importando módulos
from turtle import *

from entities.arena import Arena
from entities.game_shapes import GameShapes
from entities.player import Player
from system_managers.display_manager import DisplayManager
from system_managers.enemy_manager import EnemyManager
from system_managers.sound_manager import SoundManager
from ui.life_status import LifeStatus
from ui.score import Score

# Grupo: Vinicius de Oliveira Costa     515129
#        Luan Roger Santos Clementino   517173
#        Kauã Magalhães Paraizo         514906
#        João Augusto Silva Ferreira    514852

# Inicializar Shapes
GameShapes.InitAllShapes()

# Musica
SoundManager.InitSound()
SoundManager.PlayMusic()


# Display
DisplayManager.InitDisplay()

# Arena
arena = Arena()
arena.DrawnArena()

# Score
score = Score("white", (-280, -295))
score.Drawn()

#Vida
life_system = LifeStatus()
life_system.Init()

# Player
player = Player()
player.ConfigureKeyBindings()

# Inimigos 
enemy_system = EnemyManager()
enemy_system.SpawnAllEnemies()

laser_colision = lambda : (score.IncreaseScore(), SoundManager.PlayInvaderKillSong(), player.laser.Dispose())
player_colision = lambda : (life_system.LoseLife(), enemy_system.ResetLineup())

# Loop Principal
while True:
    DisplayManager.UpdateDisplay()

    player.UpdatePlayerState()
    
    enemy_system.UpdateEnemiesPoss()

    enemy_system.CheckCollisionInFrame((laser_colision, player_colision), player.laser, player)

    if(life_system.life_numb < 0):
        DisplayManager.GameOverScreen()