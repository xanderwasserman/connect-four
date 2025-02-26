# defines.py
# Alexander Wasserman
# 25 Feb 2025
from enum import Enum
import colorama

# Initialize colorama (needed on Windows)
colorama.init()

class GamePieceType(Enum):
    NO_PIECE     = ' '
    RED_PIECE    = f'{colorama.Fore.RED}O{colorama.Style.RESET_ALL}'
    YELLOW_PIECE = f'{colorama.Fore.YELLOW}O{colorama.Style.RESET_ALL}'
    DUMMY_PIECE  = 'T'
    
class GamePlayerType(Enum):
    HUMAN           = 1
    MACHINE         = 2