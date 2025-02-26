# test_board.py
# Alexander Wasserman
# 26 Feb 2025

import unittest
from unittest.mock import patch, MagicMock
from connect_four.player import Player
from connect_four.defines import GamePieceType, GamePlayerType


class TestPlayer(unittest.TestCase):

    def test_init_default_values(self):
        '''
        Test that a Player is instantiated with the correct default name,
        piece type, and GamePlayerType.HUMAN.
        '''
        # Create a Player with default name, using a known piece type
        p = Player(player_piece_type=GamePieceType.YELLOW_PIECE)
        self.assertEqual(p.piece_type, GamePieceType.YELLOW_PIECE, "Incorrect piece type.")
        self.assertEqual(p.name, 'Organic Player', "Default name should be 'Organic Player'.")
        self.assertEqual(p.type, GamePlayerType.HUMAN, "Player type should be HUMAN.")

    def test_init_custom_name(self):
        '''
        Test that a Player can be instantiated with a custom name.
        '''
        p = Player(player_piece_type=GamePieceType.RED_PIECE, player_name='Alice')
        self.assertEqual(p.name, 'Alice', "Custom player name not set correctly.")
        self.assertEqual(p.piece_type, GamePieceType.RED_PIECE)

    @patch('connect_four.player.show_message')
    @patch('connect_four.player.get_column_input')
    def test_move_valid_column_first_try(self, mock_get_col_input, mock_show_message):
        '''
        If the top cell of the chosen column is free, the method should return that column immediately
        without calling show_message.
        '''
        # Suppose the player picks column 3
        mock_get_col_input.return_value = 3

        # Create a grid with all cells as NO_PIECE (empty)
        grid = [[GamePieceType.NO_PIECE for _ in range(7)] for _ in range(6)]
        cols = 7

        p = Player(GamePieceType.YELLOW_PIECE, 'Test Player')
        chosen_column = p.move(grid, cols)

        self.assertEqual(chosen_column, 3, "Should return the column chosen by user.")
        mock_show_message.assert_not_called()  # No warning needed

    @patch('connect_four.player.show_message')
    @patch('connect_four.player.get_column_input')
    def test_move_full_column_then_valid(self, mock_get_col_input, mock_show_message):
        '''
        If the player first selects a full column, it should show a message 
        and then prompt again until a valid column is chosen.
        '''
        # Simulate user input: 
        #   1) picks column 2 first -> full
        #   2) picks column 5 second -> valid
        mock_get_col_input.side_effect = [2, 5]

        # Create a grid where the top cell in column 2 is already occupied
        grid = [[GamePieceType.NO_PIECE for _ in range(7)] for _ in range(6)]
        # Mark the top cell of col 2 as occupied
        grid[0][2] = GamePieceType.RED_PIECE
        cols = 7

        p = Player(GamePieceType.YELLOW_PIECE, 'Test Player')
        chosen_column = p.move(grid, cols)

        # The first chosen column was 2, which is full at row=0 -> show_message gets called
        # The second chosen column was 5, which is valid and should be returned
        self.assertEqual(chosen_column, 5, "Expected the method to eventually return the second choice (column 5).")

        # Check that show_message was called at least once for "Column is full"
        mock_show_message.assert_any_call("Column is full. Please choose a different column.")

        # Also check get_column_input was called at least twice
        self.assertEqual(mock_get_col_input.call_count, 2, "Expected two attempts: first invalid, then valid.")
