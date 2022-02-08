# Importando módulos
import sys
from entities.arena import Arena
from entities.game_shapes import GameShapes
from entities.player import Player
from system_managers.display_manager import DisplayManager
from system_managers.enemy_manager import EnemyManager
from system_managers.score_board import ScoreBoard
from system_managers.sound_manager import SoundManager
from ui.life_status import LifeStatus
from ui.score import Score
from ui.waves_counter import WaveCounter

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

# UI
score = Score("white", (-280, -295))
score.Drawn()

life_system = LifeStatus()
life_system.Init()

wave_counter: WaveCounter = WaveCounter("white", (-280, 250))
wave_counter.Drawn()

# Player
player = Player(sys.argv[1] if len(sys.argv) > 1 else "Convidado")
player.ConfigureKeyBindings()


# Inimigos 
enemy_system = EnemyManager()
enemy_system.SpawnAllEnemies()

#ScoreBoard
ScoreBoard.CreateScoreBoardFile()
ScoreBoard.ReadScoreBoard()
ScoreBoard.RegisterPlayer(player.name)

#region Funções de colisão
def laser_collision():
    score.IncreaseScore() 
    SoundManager.PlayInvaderKillSong()
    player.laser.Dispose()

def player_collision():
    life_system.LoseLife()
    if(life_system.life_numb < 0):
            SoundManager.StopMusic()
            ScoreBoard.SetPlayerScore(player.name, wave_counter.wave, score.score)
            ScoreBoard.WriteScoreBoard()
            DisplayManager.GameOverScreen()
    enemy_system.ResetLineup()
#endregion

def onNextWave():
    wave_counter.IncreaseWave()
    enemy_system.IncrementEmenySpeed(wave_counter.wave/100)

# Loop Principal
while True:
    DisplayManager.UpdateDisplay()

    player.UpdatePlayerState()
    
    enemy_system.UpdateEnemiesPoss(onResetCallback=onNextWave)

    enemy_system.CheckCollisionInFrame((laser_collision, player_collision), player.laser, player)