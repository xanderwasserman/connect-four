# computer.py
# Alexander Wasserman
# 25 Feb 2025
import random

from connect_four.defines import GamePieceType, GamePlayerType

class Computer():
    def __init__(self, computer_piece_type: GamePieceType, computer_name='Inorganic Player'):
        self.piece_type = computer_piece_type
        self.name = computer_name
        self.type = GamePlayerType.MACHINE
        
    def move(self, grid: list[list[GamePieceType]], cols: int) -> int:
        '''
        Let the computer make a move by picking a random column. Return the column number choice, 
        or None if all columns are full.
        '''
        valid_cols = []
        
        for col in range(cols):
            if grid[0][col] is GamePieceType.NO_PIECE:
                valid_cols.append(col)
                
        if not valid_cols:
            return None
        
        col_choice = random.choice(valid_cols)
        return col_choice