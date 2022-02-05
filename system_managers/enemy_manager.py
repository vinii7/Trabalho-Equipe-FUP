from typing import List, Tuple

from entities.enemy import Enemy


class _EnemyLineup:
    enemies_lineup: List[Enemy] = []
    initial_poss: Tuple # cordenadas (x, y)
    enemies_per_row: int
    row_ammount: int
    spacing: int

    def __init__(self, initial_poss: Tuple,
     enemies_per_row = 9,
     row_ammount = 5,
     spacing = 52):
        self.initial_poss = initial_poss
        self.enemies_per_row = enemies_per_row
        self.row_ammount = row_ammount
        self.spacing = spacing

    def PopulateList(self):
        x_poss: int = self.initial_poss[0]
        y_poss: int = self.initial_poss[1]

        for _ in range(self.row_ammount):
            for index in range(self.enemies_per_row):
                current_enemy = Enemy()

                current_enemy.setposition(x_poss + self.spacing * index, y_poss)

                self.enemies_lineup.append(current_enemy)

            y_poss -= self.spacing
    
    def ResetLineup(self):
        x_poss: int = self.initial_poss[0]
        y_poss: int = self.initial_poss[1]

        enemies_lenght = 0
        for _ in range(self.row_ammount):
            for index in range(self.enemies_per_row):
                self.enemies_lineup[enemies_lenght].setposition(x_poss + self.spacing * index, y_poss)
                self.enemies_lineup[enemies_lenght].showturtle()
                enemies_lenght += 1

            y_poss -= self.spacing
        

class EnemyManager:
    _enemies: _EnemyLineup
    _enemies_move_speed: float = 0.3

    def __init__(self):
        self._enemies = _EnemyLineup((-210, 250))

    def SpawnAllEnemies(self):
        self._enemies.PopulateList()

    def UpdateEnemiesPoss(self):
        for enemy in self._enemies.enemies_lineup:
            enemy.setx(enemy.xcor() + self._enemies_move_speed)

            if(enemy.xcor() > 280 or enemy.xcor() < -280):
                self._DownRow()
            
            if(enemy.ycor() < -220 and enemy.isvisible()):
                self.ResetLineup()
                
    def _DownRow(self):
        for enemy in self._enemies.enemies_lineup:
            enemy.sety(enemy.ycor() - self._enemies.spacing)
            self._enemies_move_speed *= -1
    
    def ResetLineup(self):
        self._enemies.ResetLineup()

    def CheckCollisionInFrame(self, callbacks: Tuple, *objects):
        index_counter = 0
        while(index_counter < len(objects)):
            if(self._CheckCollisionAllEnemies(objects[index_counter])):
                callbacks[index_counter]()
            index_counter += 1

    def _CheckCollisionAllEnemies(self, object) -> bool:
        wasCollision = False 

        enemy_index_count = 0
        for enemy in self._enemies.enemies_lineup:
            if(enemy.CheckCollision(object)):
                wasCollision = True
                self._enemies.enemies_lineup[enemy_index_count].setpos(0, -400)
                self._enemies.enemies_lineup[enemy_index_count].hideturtle()

            enemy_index_count += 1

        return wasCollision