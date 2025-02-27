# routes.py
# Alexander Wasserman
# 27 Feb 2025

from flask import render_template, request, redirect, url_for
from connect_four.defines import GamePieceType, GamePlayerType
from connect_four.game import ConnectFourGame

# Define a dummy move function for the human player.
# In a web app, the human move is provided by the route parameter,
# so this function never really gets called.
def _dummy_human_move(grid, cols):
    return None

# Create the game instance
game_instance = ConnectFourGame(player_move_func=_dummy_human_move)

def init_routes(app):

    @app.route("/")
    def home():
        # Show the current board
        global game_instance
        
        board_state = game_instance.board.grid
        cols = game_instance.board.COLS
        rows = game_instance.board.ROWS
        current_player_name = game_instance.current_player.name
        
        return render_template(
                "game.html", 
                board=board_state, 
                cols=cols, 
                rows=rows,
                current_player=current_player_name
            )

    @app.route("/move/<int:col>")
    def make_move(col):
        global game_instance
        
        # 1. Human move
        move_result = game_instance.board.place_piece(col, game_instance.current_player.piece_type)

        if move_result is None:
            # either invalid or full column
            return redirect(url_for('home'))

        row, col_placed = move_result

        # 2. Check winner/draw
        if game_instance.board.check_for_winner(row, col_placed, game_instance.win_count):
            return render_template("game_over.html",
                                winner=game_instance.current_player.name,
                                board=game_instance.board.grid,
                                cols=game_instance.board.COLS,
                                rows=game_instance.board.ROWS)

        if game_instance.board.is_full():
            return render_template("game_over.html",
                                winner=None,  # indicates a draw
                                board=game_instance.board.grid,
                                cols=game_instance.board.COLS,
                                rows=game_instance.board.ROWS)

        # 3. Switch to Computer
        game_instance.switch_player()

        # 4. Computer move
        if game_instance.current_player.type == GamePlayerType.MACHINE:
            
            # Let the AI pick a column
            computer_col_choice = game_instance.current_player.move(
                grid=game_instance.board.grid, 
                cols=game_instance.board.COLS
            )
            
            # Place computer's piece
            comp_result = game_instance.board.place_piece(computer_col_choice, game_instance.current_player.piece_type)
            
            if comp_result is not None:
                comp_row, comp_col_placed = comp_result
                
                # Check for winner/draw after computer's move
                if game_instance.board.check_for_winner(comp_row, comp_col_placed, game_instance.win_count):
                    return render_template("game_over.html",
                                        winner=game_instance.current_player.name,
                                        board=game_instance.board.grid,
                                        cols=game_instance.board.COLS,
                                        rows=game_instance.board.ROWS)
                if game_instance.board.is_full():
                    return render_template("game_over.html",
                                        winner=None,  # indicates a draw
                                        board=game_instance.board.grid,
                                        cols=game_instance.board.COLS,
                                        rows=game_instance.board.ROWS)

            # If still no win/draw, switch back to human for next turn
            game_instance.switch_player()

        # 5. Redirect to home to display updated board
        return redirect(url_for('home'))

    @app.route("/restart")
    def restart():
        # Re-init the game
        global game_instance
        
        game_instance = ConnectFourGame(player_move_func=_dummy_human_move)
        return redirect(url_for('home'))
