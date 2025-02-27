# game.py
# Alexander Wasserman
# 25 Feb 2025

import time
from connect_four.defines import GamePieceType
from connect_four.board import Board
from connect_four.player import Player
from connect_four.computer import Computer
from hmi.cli_interface import show_message

class ConnectFourGame:
    
    def __init__(self, player_move_func):
        self.board = Board()
        self.player1 = Player(player_piece_type=GamePieceType.YELLOW_PIECE, move_func=player_move_func)
        self.player2 = Computer(computer_piece_type=GamePieceType.RED_PIECE)
        self.current_player = self.player1
        self.win_count = 4
        
    def switch_player(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1