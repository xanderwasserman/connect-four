# test_board.py
# Alexander Wasserman
# 26 Feb 2025

import unittest
from unittest.mock import patch

from connect_four.game import ConnectFourGame
from connect_four.defines import GamePieceType
from connect_four.board import Board
from connect_four.player import Player
from connect_four.computer import Computer

class TestConnectFourGame(unittest.TestCase):
    
    def test_init(self):
        '''
        Test that the game initializes correctly:
        - Board is created
        - Player1 is a Player with YELLOW_PIECE
        - Player2 is a Computer with RED_PIECE
        - Current player is player1
        - Win count is 4
        '''
        game = ConnectFourGame()
        self.assertIsInstance(game.board, Board, "Game should initialize with a Board instance.")
        self.assertIsInstance(game.player1, Player, "player1 should be a Player.")
        self.assertIsInstance(game.player2, Computer, "player2 should be a Computer.")
        self.assertEqual(game.player1.piece_type, GamePieceType.YELLOW_PIECE)
        self.assertEqual(game.player2.piece_type, GamePieceType.RED_PIECE)
        self.assertEqual(game.current_player, game.player1, "Current player should start as player1.")
        self.assertEqual(game.win_count, 4, "Default win_count should be 4.")
    
    def test_switch_player(self):
        '''
        Test that switch_player toggles the current player
        between player1 and player2.
        '''
        game = ConnectFourGame()
        self.assertEqual(game.current_player, game.player1)
        
        game.switch_player()
        self.assertEqual(game.current_player, game.player2)

        game.switch_player()
        self.assertEqual(game.current_player, game.player1)
    
    @patch('connect_four.game.show_message')
    @patch('connect_four.game.Board.display_board')
    def test_play_winning_scenario(self, mock_display_board, mock_show_message):
        '''
        Test a short scenario in which player1 (human) achieves a quick vertical win.
        We'll mock out both the Player (human) and Computer moves so we can control
        exactly which columns are chosen, leading to a fast win for player1.
        
        - Patching display_board & show_message to avoid printing to console
          and to detect certain messages (like "Player 1 wins!").
        '''
        game = ConnectFourGame()
        
        # Player1 = YELLOW, Player2 = RED
        # We'll cause a vertical 4-in-a-row in column 0 for Player1 (YELLOW).
        # The moves array below is the column each player picks, in turn.
        #
        # Move order:
        #   1. Player1 -> col 0 (row 5)
        #   2. Player2 -> col 1
        #   3. Player1 -> col 0 (row 4)
        #   4. Player2 -> col 1
        #   5. Player1 -> col 0 (row 3)
        #   6. Player2 -> col 1
        #   7. Player1 -> col 0 (row 2) => should be winning move
        #
        # After the 7th move, the loop should break.
        
        # We'll patch the "move" method on each player's class so we can
        # return columns from a side_effect list. Each call uses the next value.
        with patch.object(Player, 'move', side_effect=[0, 0, 0, 0]) as mock_player_move, \
             patch.object(Computer, 'move', side_effect=[1, 1, 1]) as mock_computer_move:
            
            game.play()  # Run the game loop
            
            # By the time we exit, we expect player1 (YELLOW) to have won.
            
            # Check that the final message includes "wins!" for player1
            # mock_show_message is called with various arguments, e.g.:
            # - "Player1's turn."
            # - "Column is full or invalid. Try again." if that had happened
            # - "YELLOW wins!" or "Player name wins!"
            
            # Gather all calls to mock_show_message:
            show_message_calls = [call_args[0][0] for call_args in mock_show_message.call_args_list]
            
            # Make sure that "wins!" message was eventually displayed
            # (Player1 default name might be "Player" or "Human" or something else
            #  depending on how it's set in player.py. We can look for the substring "wins!")
            self.assertTrue(
                any("wins!" in msg for msg in show_message_calls),
                "Expected a 'wins!' message in show_message calls."
            )
            
            # Confirm the loop ended within a reasonable number of moves:
            # - The last mock_player_move call is the winning move
            self.assertEqual(mock_player_move.call_count, 4, "Expected 4 moves from player1.")
            self.assertEqual(mock_computer_move.call_count, 3, "Expected 3 moves from player2.")

            # Check that the board has YELLOW in a vertical stack in col 0
            # rows for that stack: 5, 4, 3, 2
            self.assertEqual(game.board.grid[5][0], GamePieceType.YELLOW_PIECE)
            self.assertEqual(game.board.grid[4][0], GamePieceType.YELLOW_PIECE)
            self.assertEqual(game.board.grid[3][0], GamePieceType.YELLOW_PIECE)
            self.assertEqual(game.board.grid[2][0], GamePieceType.YELLOW_PIECE)

