# game.py
# Alexander Wasserman
# 25 Feb 2025

import time
from connect_four.defines import GamePieceType, GamePlayerType
from connect_four.board import Board
from connect_four.player import Player
from connect_four.computer import Computer
from hmi.cli_interface import show_message, show_welcome

class ConnectFourGame:
    
    def __init__(self):
        self.board = Board()
        self.player1 = Player(player_piece_type=GamePieceType.YELLOW_PIECE)
        self.player2 = Computer(computer_piece_type=GamePieceType.RED_PIECE)
        self.current_player = self.player1
        self.win_count = 4
        
    def switch_player(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1
        
    def play(self):
        '''
        Main game loop: continue until win or draw.
        '''
        show_welcome()
        time.sleep(3)
        
        while True:
            
            self.board.display_board()
            
            show_message(self.current_player.name + "'s turn.")
                
            col_choice = self.current_player.move(grid=self.board.grid, cols=self.board.COLS)
            
            if col_choice is None:
                # Invalid move or no moves left
                show_message("Column is full or invalid. Try again.")
                continue
            
            move_result = self.board.place_piece(col_choice, self.current_player.piece_type)
            if move_result is None:
                # Invalid move or no moves left
                show_message("Column is full or invalid. Try again.")
                continue
            
            row, col = move_result
            
            #check for a winner
            if self.board.check_for_winner(row, col, self.win_count):
                self.board.display_board()
                show_message(self.current_player.name + " wins!")
                break
            
            #check for a draw
            if self.board.is_full():
                show_message("It's a draw!")
                break
            
            self.switch_player()
            
            # If it is the machine player next, wait a bit to simulate it thinking
            # and to slow down gameplay a bit.
            if self.current_player == self.player1:
                time.sleep(2)