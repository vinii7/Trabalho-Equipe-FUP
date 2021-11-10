# Importando módulos
import turtle
from turtle import *
import math
import pygame
from time import sleep
from random import randint

# Registrar Shapes
register_shape('player1.gif')
register_shape('alien1.gif')
register_shape('laser1.gif')


# Musica
pygame.init()
pygame.mixer.music.load('music.wav')
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)

# Sons
som_laser = pygame.mixer.Sound('shoot.wav')
som_invader_kill = pygame.mixer.Sound('invaderkilled.wav')


# Display
display = turtle.Screen()
display.setup(700, 700)
display.title('Space Invaders')
display.bgcolor('black')
display.tracer(0)


# Borda
borda = turtle.Turtle()
borda.speed(0)
borda.color('white')
borda.penup()
borda.setposition(-300, -300)
borda.pendown()
borda.pensize(3)
for lado in range(0, 4):
    borda.forward(600)
    borda.left(90)
borda.hideturtle()


# Score
score = 0

letra = turtle.Turtle()
letra.color('white')
letra.speed(0)
letra.penup()
letra.setposition(-280, -295)
placar = f'Score:  {score}'
letra.write(placar, False, align='left', font=('Atari Small', 28, 'normal'))
letra.hideturtle()


# Vida
number_of_lives = 2
# Lista vazia de vidas
vidas = []

# Placar de vidas
for n in range(number_of_lives):
    vidas.append(turtle.Turtle())
x = 140
for vida in vidas:
    vida.shape('player1.gif')
    vida.speed(0)
    vida.hideturtle()
    vida.penup()
    vida.setposition(x, -275)
    vida.showturtle()
    x += 60


# Criar Player
player = turtle.Turtle()
player.shape('player1.gif')
player.penup()
player.speed(0)
player.setposition(0, -200)
player.setheading(90)
player.shapesize
player.speed = 0

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
    enemyspeed = 0.1


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
        som_laser.play()
        som_laser.set_volume(0.1)
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


# Loop Principal
while True:

    # Update na tela a cada laço
    display.update()

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
                enemyspeed = 0.1

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
            enemyspeed *= -1

        # Mover para baixo e limitar fronteira do lado esquerdo
        if enemy.xcor() < -280:
            # Mover todos os inimigos para baixo
            for e in enemies:
                y = e.ycor()
                y -= 50
                e.sety(y)

            # Mudar a direção dos inimigos
            enemyspeed *= -1

        # Verificar a colisão entre o laser e o inimigo
        if collision(laser, enemy):
            # Som
            som_invader_kill.play()
            som_invader_kill.set_volume(0.1)

            # Resetar o laser
            laser.hideturtle()
            laserstate = 'ready'
            laser.setposition(0, 400)

            # Resetar o inimigo
            x = randint(-240, 240)
            y = enemy.ycor() + 150
            enemy.setposition(x, y)

            # Score
            score += 10
            placar = f'Score:  {score}'
            letra.clear()
            letra.write(placar, False, align='left',
                        font=('Atari Small', 28, 'normal'))

        # Verificar a colisão entre o player e o inimigo
        if collision(player, enemy):
            # Condição para numero de vidas
            if number_of_lives > 0:

                # Local onde o primeiro vai spawnar
                enemy_x = -210
                enemy_y = 200

                # Estrutura para gerar inimigos
                for enemy in enemies:
                    enemy.color('red')
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

                    enemyspeed = 0.1

                number_of_lives -= 1
                vidas[number_of_lives].hideturtle()
                continue

            # Tela de gameover
            else:
                player.hideturtle()
                enemy.hideturtle()
                display.clear()
                pygame.mixer.music.stop()
                gameover = turtle.Turtle()
                gameover.speed(0)
                gameover.hideturtle()
                gameover.penup()
                gameover.color('black')
                gameover.setposition(-200, 0)
                gameover.write('GAMEOVER', font=('Atari Small', 80, 'normal'))
                sleep(3)
                exit()

    # Mover a bala
    if laserstate == 'fire':
        y = laser.ycor()
        y += laserspeed
        laser.sety(y)

    # Verificar passou do topo
    if laser.ycor() > 290:
        laser.hideturtle()
        laserstate = 'ready'
