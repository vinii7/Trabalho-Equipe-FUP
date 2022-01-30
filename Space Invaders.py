# Grupo: Vinicius de Oliveira Costa     515129
#        Luan Roger Santos Clementino   517173
#        Kauã Magalhães Paraizo         514906
#        João Augusto Silva Ferreira    514852

# Kauã
# Importando módulos
import turtle
from turtle import *
import math
from time import sleep
from random import randint
from entityes.arena import Arena

from entityes.player import Player

from system_managers.display_manager import DisplayManager
from system_managers.sound_manager import SoundManager
from text_entityes.life_system import LifeSystem
from text_entityes.score import Score

# Registrar Shapes
register_shape('player1.gif')
register_shape('alien1.gif')
register_shape('laser1.gif')


# Musica
sound_manager = SoundManager()
sound_manager.InitSound()
sound_manager.PlayMusic()


# Display
DisplayManager.InitDisplay()

# Arena
arena = Arena()
arena.DrawnArena()


# Score
score = Score("white", (-280, -295))
score.Drawn()

life_system = LifeSystem()
life_system.Init()


# Criar Player
player = Player()

# Roger
# Numero de inimigos
number_of_enemies = 27
# Lista vazia de inimigos
enemies = []
# Adicionar inimigos na lista
for n in range(number_of_enemies):
    # Criar inimigo
    enemies.append(turtle.Turtle())

# Local onde o primeiro vai spawnar
enemy_x = -210
enemy_y = 200
enemy_n = 0

# Estrutura para gerar inimigos
for enemy in enemies:
    enemy.shape('alien1.gif')
    enemy.penup()
    enemy.speed(0)
    x = enemy_x + (52 * enemy_n)
    y = enemy_y
    enemy.setposition(x, y)

    # Atualizar numero de inimigos
    enemy_n += 1
    if enemy_n == 9:
        enemy_y -= 50
        enemy_n = 0

    # Velocidade
    enemyspeed = 2


# Laser do Player
laser = turtle.Turtle()
laser.shape('laser1.gif')
laser.penup()
laser.speed(0)
laser.setheading(90)
laser.hideturtle()
laser.goto(0, -400)

# Velocidade do laser
laserspeed = 2

# Definir Estado do laser
# ready - preparado para atirar
# fire - laser foi disparado
laserstate = 'ready'

# João Augusto
# Funções



def left():
    player.speed = -0.5


def right():
    player.speed = 0.5


def mov_player():
    x = player.xcor()
    x += player.speed
    if x < -277:
        x = -277
    if x > 277:
        x = 277
    player.setx(x)


def fire_laser():
    # Declarar global caso precise altera-lo
    global laserstate
    if laserstate == 'ready':
        sound_manager.PlayLaserSong()
        laserstate = 'fire'

        # Mover a bala para cima
        x = player.xcor()
        y = player.ycor() + 27
        laser.setposition(x, y)
        laser.showturtle()


def collision(o1, o2):
    d = math.sqrt(math.pow(o1.xcor()-o2.xcor(), 2) +
                  math.pow(o1.ycor()-o2.ycor(), 2))
    if d < 22:
        return True
    else:
        return False


# Tecla de movimento
listen()
onkeypress(left, 'Left')
onkeypress(right, 'Right')
onkeypress(fire_laser, 'space')

# Vinicius
# Loop Principal
while True:

    # Update na tela a cada laço
    DisplayManager.UpdateDisplay()

    # Movimentar o jogador
    mov_player()

    for enemy in enemies:
        if enemy.ycor() < -200:

            # Local onde o primeiro vai spawnar
            enemy_x = -210
            enemy_y = 200

            # Estrutura para gerar inimigos
            for enemy in enemies:
                enemy.shape('alien1.gif')
                enemy.penup()
                enemy.speed(0)
                x = enemy_x + (52 * enemy_n)
                y = enemy_y
                enemy.setposition(x, y)

                # Atualizar numero de inimigos
                enemy_n += 1
                if enemy_n == 9:
                    enemy_y -= 50
                    enemy_n = 0

                # Velocidade do inimigo
                enemyspeed = 2

        # Mover inimigo no eixo X
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        # Mover para baixo e limitar fronteira do lado direito
        if enemy.xcor() > 280:
            # Mover todos os inimigos para baixo
            for e in enemies:
                y = e.ycor()
                y -= 50
                e.sety(y)

            # Mudar a direção dos inimigos
            enemyspeed *= -1.3

        # Mover para baixo e limitar fronteira do lado esquerdo
        if enemy.xcor() < -280:
            # Mover todos os inimigos para baixo
            for e in enemies:
                y = e.ycor()
                y -= 50
                e.sety(y)

            # Mudar a direção dos inimigos
            enemyspeed *= -1.3

        # Verificar a colisão entre o laser e o inimigo
        if collision(laser, enemy):
            # Som
            sound_manager.PlayInvaderKillSong()

            # Resetar o laser
            laser.hideturtle()
            laserstate = 'ready'
            laser.setposition(0, 400)

            # Resetar o inimigo
            x = randint(-240, 240)
            y = enemy.ycor() + 150
            enemy.setposition(x, y)

            # Score
            score.IncreaseScore()

        # Verificar a colisão entre o player e o inimigo
        if collision(player, enemy):
            # Condição para numero de vidas
            if life_system.life_numb > 0:

                # Local onde o primeiro vai spawnar
                enemy_x = -210
                enemy_y = 200

                # Estrutura para gerar inimigos
                for enemy in enemies:
                    enemy.shape('alien1.gif')
                    enemy.penup()
                    enemy.speed(0)
                    x = enemy_x + (52 * enemy_n)
                    y = enemy_y
                    enemy.setposition(x, y)

                    # Atualizar numero de inimigos
                    enemy_n += 1
                    if enemy_n == 9:
                        enemy_y -= 50
                        enemy_n = 0

                    enemyspeed = 2

                life_system.LoseLife()
                continue

            # Tela de gameover
            else:
                DisplayManager.GameOverScreen()

    # Mover a bala
    if laserstate == 'fire':
        y = laser.ycor()
        y += laserspeed
        laser.sety(y)

    # Verificar passou do topo
    if laser.ycor() > 290:
        laser.hideturtle()
        laserstate = 'ready'
