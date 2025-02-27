# main_cli.py
# Alexander Wasserman
# 25 Feb 2025

import time
from connect_four.defines import GamePlayerType
from connect_four.game import ConnectFourGame
from hmi.cli_interface import show_board, show_message, show_welcome, get_player_move

game = ConnectFourGame(player_move_func=get_player_move)

def play():
        '''
        Main game loop: continue until win or draw.
        '''
        
        while True:
            
            show_board(game.board.ROWS, game.board.ROWS, game.board.grid)
            show_message(game.current_player.name + "'s turn.")
                
            col_choice = game.current_player.move(grid=game.board.grid, cols=game.board.COLS)
            
            if col_choice is None:
                # Invalid move or no moves left
                show_message("Column is full or invalid. Try again.")
                continue
            
            move_result = game.board.place_piece(col_choice, game.current_player.piece_type)
            if move_result is None:
                # Invalid move or no moves left
                show_message("Column is full or invalid. Try again.")
                continue
            
            row, col = move_result
            
            #check for a winner
            if game.board.check_for_winner(row, col, game.win_count):
                show_board(game.board.ROWS, game.board.ROWS, game.board.grid)
                show_message(game.current_player.name + " wins!")
                break
            
            #check for a draw
            if game.board.is_full():
                show_message("It's a draw!")
                break
            
            game.switch_player()
            
            # If it is the machine player next, wait a bit to simulate it thinking
            # and to slow down gameplay a bit.
            if game.current_player == game.player1:
                time.sleep(2)

if __name__ == "__main__":
    
    try:
        show_welcome()
        time.sleep(3)
        play()
    except KeyboardInterrupt:
        print("Game ended!")
        
        
    