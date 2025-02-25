# player.py
# Alexander Wasserman
# 25 Feb 2025

from connect_four.defines import GamePieceType, GamePlayerType
from hmi.cli_interface import get_column_input, show_message

class Player():
    def __init__(self, player_piece_type, player_name='Organic Player'):
        self.piece_type = player_piece_type
        self.name = player_name
        self.type = GamePlayerType.HUMAN
        
    def move(self, grid: list[list[GamePieceType]], cols: int) -> int:
        '''
        Gets an input from the Player to indicate which column the game piece
        should be placed in. Additionally, it checks whether the chosen column is full.
        '''
        while True:
            col = get_column_input(cols)
            # Check if the top of the column is already occupied.
            if grid[0][col] != GamePieceType.NO_PIECE:
                show_message("Column is full. Please choose a different column.")
            else:
                return col