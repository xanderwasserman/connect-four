# board.py
# Alexander Wasserman
# 25 Feb 2025
from typing import Tuple, Optional
from connect_four.defines import GamePieceType
from hmi.cli_interface import show_board

class Board:
    ROWS = 6
    COLS = 7
    
    
    def __init__(self):
        # 6x7 grid
        self.grid = [ [GamePieceType.NO_PIECE for _ in range(self.COLS)] for _ in range(self.ROWS)]
        
        
    def place_piece(self, col: int, piece_type: GamePieceType) -> Optional[Tuple[int, int]]:
        '''
        Places the game piece in the specified column (0 - COLS).
        Returns the (row, col) where it was placed, or None if invalid or full.
        '''
        if col < 0 or col >= self.COLS:
            return None # invalid column number
        
        for row in reversed(range(self.ROWS)):
            if self.grid[row][col] is GamePieceType.NO_PIECE:
                self.grid[row][col] = piece_type
                return (row, col)
            
        return None # No opening was found, the column is full
    
    
    def is_full(self) -> bool:
        '''
        Check if the board is completely full (all grid elements occupied by a colour).
        '''
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.grid[row][col] is GamePieceType.NO_PIECE:
                    return False
        return True
    
    
    def check_for_winner(self, row: int, col:int, winning_number: int) -> bool:
        '''
        Check a grid position if there is a winning line of colours.
        '''
        piece_type = self.grid[row][col]
        
        if winning_number <= 0 or winning_number > max(self.ROWS, self.COLS):
            return False # Invalid winning number
        
        if piece_type is GamePieceType.NO_PIECE:
            return False # There is no game piece at the specified position
        
        # Check all directions; horizontal, vertical,  and diagonal
        directions = [
            [ (0, -1),    (0, 1) ], # horizontal column (left and right)
            [ (1, 0),    (-1, 0) ], # vertical row (up and down)
            [ (1, -1),   (-1, 1) ], # diagonal (top left to bottom right)
            [ (-1, 1),   (1, -1) ]  # diagonal (top right to bottom left)
        ]
        
        for direction in directions:
            total_in_line = 1 # First element is the current game piece
            
            for (delta_row, delta_col) in direction:
                total_in_line += self.count_pieces_in_direction(row, col, delta_row, delta_col, piece_type)
                
            if total_in_line >= winning_number:
                return True # Current move is a winning move
            
        return False # No winners
    
    
    def count_pieces_in_direction(self, row: int, col: int, delta_row: int, delta_col: int, piece_type: GamePieceType):
        '''
        Count the number of equal type pieces in a specific direction indicated by (delta_row, delta_col)
        '''
        count = 0
        
        row = row+delta_row
        col = col+delta_col
        
        while 0 <= row < self.ROWS and 0 <= col < self.COLS and self.grid[row][col] == piece_type:
            count += 1
            row += delta_row
            col += delta_col
        
        return count
    