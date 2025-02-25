# cli_interface.py
# Alexander Wasserman
# 25 Feb 2025
import os

from typing import Tuple, Optional, Union
from connect_four.defines import GamePieceType

def get_column_input(cols: int) -> int:
    '''
    Safely gets a column number from the CLI input in range 0 -> cols-1
    '''
    return _get_integer_input(
        input_text=f"Enter a column (0-{cols-1}): ", 
        range_min=0, 
        range_max=cols
    )
    
    
def show_message(message: str):
    '''
    Shows a message to the user on the cli
    '''
    print(message)
    
    
def show_board(rows: int, cols:int, grid: list[list[GamePieceType]]) -> None:
        """
        Print the board to the console. 
        """
        _clear_console()
        for row in range(rows):
            row_str = '|'
            for col in range(cols):
                cell = grid[row][col]
                row_str += f" {cell.value} |"
            print(row_str)
        print("-" * 29)  # separator
    
def _clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
def _get_integer_input(input_text: str, range_min: int, range_max: int) -> int:
    input_valid = False
    value: Optional[int] = None
    
    while not input_valid:
        input_value = input(input_text)
        input_valid, value = _validate_integer_input(input_value, range_min, range_max)
        
    return value #guaranteed integer
            
            
def _validate_integer_input(value: Union[str, int], min: int, max: int) -> Tuple[bool, Optional[int]]:
        
    # Try convert to integer
    try:
        value_int = int(value)
    except ValueError: 
        return False, None
    
    # check if integer is in range
    if min <= value_int < max:
        return True, value_int
    
    return False, None