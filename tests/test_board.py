# test_board.py
# Alexander Wasserman
# 25 Feb 2025

import unittest
from connect_four.board import Board
from connect_four.defines import GamePieceType

class TestBoard(unittest.TestCase):

    def setUp(self):
        '''
        Initialize a fresh Board before each test.
        '''
        self.board = Board()

    def test_initial_board_setup(self):
        '''
        Test that the board initializes with NO_PIECE everywhere.
        '''
        for row in range(self.board.ROWS):
            for col in range(self.board.COLS):
                self.assertEqual(self.board.grid[row][col], GamePieceType.NO_PIECE)

    def test_place_piece_valid_column(self):
        '''
        Placing a piece in a valid, empty column should place it in the bottom-most row.
        '''
        result = self.board.place_piece(3, GamePieceType.RED_PIECE)
        self.assertIsNotNone(result, "Expected successful placement in column 3.")
        placed_row, placed_col = result
        self.assertEqual(placed_col, 3)
        self.assertEqual(placed_row, self.board.ROWS - 1, "Piece should drop to the bottom row.")
        self.assertEqual(self.board.grid[placed_row][placed_col], GamePieceType.RED_PIECE)

    def test_place_piece_invalid_column(self):
        '''
        Placing a piece in an out-of-bounds column should return None and not modify the board.
        '''
        result_left = self.board.place_piece(-1, GamePieceType.RED_PIECE)
        self.assertIsNone(result_left, "Column -1 is invalid, expected None.")

        result_right = self.board.place_piece(self.board.COLS, GamePieceType.RED_PIECE)
        self.assertIsNone(result_right, f"Column {self.board.COLS} is invalid, expected None.")

        # Ensure the board is still empty
        for row in range(self.board.ROWS):
            for col in range(self.board.COLS):
                self.assertEqual(self.board.grid[row][col], GamePieceType.NO_PIECE)

    def test_place_piece_column_full(self):
        '''
        Filling a column completely and placing an extra piece should return None.
        '''
        col_index = 0
        
        # Fill the column
        for _ in range(self.board.ROWS):
            result = self.board.place_piece(col_index, GamePieceType.RED_PIECE)
            self.assertIsNotNone(result)

        # Now the column should be full
        result_full = self.board.place_piece(col_index, GamePieceType.RED_PIECE)
        self.assertIsNone(result_full, "Placing a piece in a full column should return None.")

    def test_is_full_false(self):
        '''
        Board should not be full initially or partially.
        '''
        self.assertFalse(self.board.is_full(), "Empty board should not be full.")
        
        # Place a single piece
        self.board.place_piece(0, GamePieceType.RED_PIECE)
        self.assertFalse(self.board.is_full(), "Partially filled board should not be full.")

    def test_is_full_true(self):
        '''
        Test that the board reports full once every cell is occupied.
        '''
        # Fill the entire board
        for col in range(self.board.COLS):
            for _ in range(self.board.ROWS):
                self.board.place_piece(col, GamePieceType.RED_PIECE)

        self.assertTrue(self.board.is_full(), "Board should report full after all slots are taken.")

    def test_check_for_winner_horizontal(self):
        '''
        Place multiple pieces in a row to simulate a horizontal win.
        '''
        # Suppose we have a winning_number of 4
        winning_number = 4

        # Place 4 RED pieces horizontally in row 5 (the bottom row)
        for c in range(4):
            self.board.place_piece(c, GamePieceType.RED_PIECE)

        # The last piece placed should produce a horizontal winner
        row_to_check = self.board.ROWS - 1  # bottom row
        col_to_check = 3  # where the 4th piece was placed

        has_won = self.board.check_for_winner(row_to_check, col_to_check, winning_number)
        self.assertTrue(has_won, "Should detect a horizontal winning condition for RED.")

    def test_check_for_winner_vertical(self):
        '''
        Place multiple pieces in a column to simulate a vertical win.
        '''
        winning_number = 4
        col_index = 2

        # Stack 4 pieces in column 2
        for _ in range(winning_number):
            self.board.place_piece(col_index, GamePieceType.YELLOW_PIECE)

        # Check the top-most of the 4
        row_to_check = self.board.ROWS - 4  # Because we placed 4 pieces from bottom up
        col_to_check = col_index

        has_won = self.board.check_for_winner(row_to_check, col_to_check, winning_number)
        self.assertTrue(has_won, "Should detect a vertical winning condition for YELLOW.")

    def test_check_for_winner_diagonal(self):
        '''
        Place pieces diagonally to simulate a diagonal win.
        '''
        winning_number = 4

        # We'll place RED in a \ diagonal pattern. For example:
        # Row 5, Col 0
        # Row 4, Col 1
        # Row 3, Col 2
        # Row 2, Col 3
        self.board.place_piece(0, GamePieceType.RED_PIECE)  # Goes to (5,0)
        
        self.board.place_piece(1, GamePieceType.DUMMY_PIECE)  # filler so stack is aligned
        self.board.place_piece(1, GamePieceType.RED_PIECE)  # Goes to (4,1)
        
        self.board.place_piece(2, GamePieceType.DUMMY_PIECE)
        self.board.place_piece(2, GamePieceType.DUMMY_PIECE)
        self.board.place_piece(2, GamePieceType.RED_PIECE)  # Goes to (3,2)
        
        self.board.place_piece(3, GamePieceType.DUMMY_PIECE)
        self.board.place_piece(3, GamePieceType.DUMMY_PIECE)
        self.board.place_piece(3, GamePieceType.DUMMY_PIECE)
        self.board.place_piece(3, GamePieceType.RED_PIECE)  # Goes to (2,3)

        # The last piece was at row=2, col=3
        has_won = self.board.check_for_winner(2, 3, winning_number)
        self.assertTrue(has_won, "Should detect a diagonal \\ winning condition for RED.")

    def test_check_for_winner_no_piece(self):
        '''
        check_for_winner on an empty slot should return False.
        '''
        # We haven't placed anything yet, so row=0, col=0 is NO_PIECE
        self.assertFalse(self.board.check_for_winner(0, 0, 4))

    def test_check_for_winner_invalid_win_number(self):
        '''
        Invalid winning_number (e.g., 0 or too large) should return False.
        '''
        # Place a piece so there's something to check
        self.board.place_piece(0, GamePieceType.RED_PIECE)
        row, col = self.board.ROWS - 1, 0

        # Zero or negative or bigger than board size is invalid
        self.assertFalse(self.board.check_for_winner(row, col, 0))
        self.assertFalse(self.board.check_for_winner(row, col, -1))
        self.assertFalse(self.board.check_for_winner(row, col, max(self.board.ROWS, self.board.COLS) + 1))