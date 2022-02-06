from enum import IntEnum
from os.path import exists
from typing import Dict

class OrderBy(IntEnum):
    WAVE = 0
    SCORE = 1

class ScoreBoard:
    _score_board_file = "score_board.txt"
    _score_board_players: Dict = {}

    @staticmethod
    def CreateScoreBoardFile() -> bool:
        '''
        Irá criar apenas se o arquivo não existir.
        Retorno: True se o arquivo não existir e for criado com sucesso;
        False se o arquivo já existir
        '''
        
        if(exists(ScoreBoard._score_board_file)):
            return False
        
        file = open(ScoreBoard._score_board_file, 'w+')
        file.write("\0")
        file.close()

        return True
    
    @staticmethod
    def ReadScoreBoard():
        file = open(ScoreBoard._score_board_file, 'r')
        for line in file.readlines():
            actual_palyer = line.split('-')
            if(len(actual_palyer) < 4):
                continue
            ScoreBoard._score_board_players[actual_palyer[1]] = (int(actual_palyer[2]), int(actual_palyer[3]))
        
        file.close()
    
    @staticmethod
    def WriteScoreBoard():
        ScoreBoard.OrderScoreBoardBy()
        file = open(ScoreBoard._score_board_file, 'w+')
        rank_possition = 1
        for player_name, info in ScoreBoard._score_board_players.items():
            file.write(f"{rank_possition}-{player_name}-{info[0]}-{info[1]}\n")
            rank_possition += 1
        
        file.close()
            
    
    @staticmethod
    def RegisterPlayer(player_name: str):
        if(player_name in ScoreBoard._score_board_players):
            return

        ScoreBoard._score_board_players[player_name] = [0, 0]
    
    def SetPlayerScore(player_name: str, wave: int, score: int):
        '''
        Atualiza a pontuação do jogador apenas se a que ele conseguiu agora
        é maior do que ele já tinha.
        '''

        if(player_name in ScoreBoard._score_board_players):
            if(score < ScoreBoard._score_board_players[player_name][1]):
                return

        ScoreBoard._score_board_players[player_name] = (wave, score)
    
    @staticmethod
    def OrderScoreBoardBy(order_critery: OrderBy = OrderBy.SCORE):
        ordedScoreBoard = dict(sorted(ScoreBoard._score_board_players.items(), key=lambda item: item[order_critery], reverse=True))
        ScoreBoard._score_board_players = ordedScoreBoard