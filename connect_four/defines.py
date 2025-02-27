# defines.py
# Alexander Wasserman
# 25 Feb 2025
from enum import Enum, unique

@unique
class GamePieceType(Enum):
    NO_PIECE     = (' ', 'white')   # (display symbol, default color)
    RED_PIECE    = ('O', 'red')
    YELLOW_PIECE = ('O', 'gold')
    DUMMY_PIECE  = ('D', 'white')

    def __init__(self, symbol, default_color):
        self.symbol = symbol
        self.default_color = default_color
    
class GamePlayerType(Enum):
    HUMAN           = 1
    MACHINE         = 2
    

