# test_main_cli.py
# Alexander Wasserman
# 27 Feb 2025

import unittest
from unittest.mock import patch
from connect_four.computer import Computer
from connect_four.defines import GamePieceType, GamePlayerType
from connect_four.game import ConnectFourGame
from connect_four.player import Player
import main_cli  # This imports main_cli.py, which defines the global game and play()

def _dummy_move(grid, cols):
    return 0
  
class TestCliGame(unittest.TestCase):

    @patch('main_cli.show_message')
    @patch('main_cli.show_board')
    def test_play_winning_scenario(self, mock_show_board, mock_show_message):
        '''
        Test a scenario in which player1 (human) achieves a vertical win.
        We simulate the following move order:
        
          1. Player1 -> column 0 (piece placed at row 5)
          2. Player2 -> column 1
          3. Player1 -> column 0 (row 4)
          4. Player2 -> column 1
          5. Player1 -> column 0 (row 3)
          6. Player2 -> column 1
          7. Player1 -> column 0 (row 2) => winning move
          
        After these moves, we expect a win message to be shown and the final board
        to have YELLOW_PIECE in column 0 rows 5, 4, 3, 2.
        '''
        # Reinitialize the global game for a fresh start
        main_cli.game = ConnectFourGame(player_move_func=_dummy_move)
        game = main_cli.game  # alias

        # Patch the move() methods so that we control which column is chosen.
        # For the human (Player), we simulate moves: 0, 0, 0, 0.
        # For the computer (Computer), we simulate moves: 1, 1, 1.
        with patch.object(Player, 'move', side_effect=[0, 0, 0, 0]) as mock_player_move, \
             patch.object(Computer, 'move', side_effect=[1, 1, 1]) as mock_computer_move:
            
            # Run the CLI game loop. This will eventually break once a win is detected.
            main_cli.play()
            
            # Check that the final board has a vertical win in column 0 for the human.
            self.assertEqual(game.board.grid[5][0], GamePieceType.YELLOW_PIECE)
            self.assertEqual(game.board.grid[4][0], GamePieceType.YELLOW_PIECE)
            self.assertEqual(game.board.grid[3][0], GamePieceType.YELLOW_PIECE)
            self.assertEqual(game.board.grid[2][0], GamePieceType.YELLOW_PIECE)
            
            # Verify that a win message was shown.
            show_message_calls = [args[0] for args, kwargs in mock_show_message.call_args_list]
            self.assertTrue(
                any("wins!" in msg for msg in show_message_calls),
                "Expected a 'wins!' message in show_message calls."
            )
            
            # Also check that the number of moves made matches our expectations:
            self.assertEqual(mock_player_move.call_count, 4, "Expected 4 moves from the human player.")
            self.assertEqual(mock_computer_move.call_count, 3, "Expected 3 moves from the computer.")