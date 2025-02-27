# player.py
# Alexander Wasserman
# 25 Feb 2025

from connect_four.defines import GamePlayerType

class Player:
    def __init__(self, player_piece_type, move_func, player_name='Organic Player'):
        self.piece_type = player_piece_type
        self.move_func = move_func
        self.name = player_name
        self.type = GamePlayerType.HUMAN

    def move(self, grid, cols):
        return self.move_func(grid, cols)