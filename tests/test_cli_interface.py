# test_board.py
# Alexander Wasserman
# 26 Feb 2025

import unittest
from unittest.mock import patch, call

from hmi.cli_interface import (
    get_column_input,
    show_message,
    show_board,
    _validate_integer_input,
)

from connect_four.defines import GamePieceType

class TestCLIInterface(unittest.TestCase):

    @patch('builtins.input', return_value='2')
    def test_get_column_input_valid_single_try(self, mock_input):
        '''
        If the user enters a valid integer within range, get_column_input 
        should return it immediately.
        '''
        cols = 5
        chosen_col = get_column_input(cols)
        self.assertEqual(chosen_col, 2)
        mock_input.assert_called_once()

    @patch('builtins.input')
    def test_get_column_input_with_retries(self, mock_input):
        '''
        If the user enters invalid values, it should keep asking until 
        we get a valid integer in range.
        '''
        cols = 3
        # side_effect simulates multiple user inputs in sequence:
        #  'a'   -> not an int
        #  '10'  -> out of range (>= 3)
        #  '1'   -> valid
        mock_input.side_effect = ['a', '10', '1']

        chosen_col = get_column_input(cols)
        self.assertEqual(chosen_col, 1)
        self.assertEqual(mock_input.call_count, 3)

    def test_validate_integer_input_valid(self):
        '''
        _validate_integer_input should return (True, int_value)
        if the string is an integer and within [min, max).
        '''
        is_valid, val = _validate_integer_input('2', 0, 5)
        self.assertTrue(is_valid)
        self.assertEqual(val, 2)

    def test_validate_integer_input_not_int(self):
        '''
        If the input string is not an integer, it should return (False, None).
        '''
        is_valid, val = _validate_integer_input('abc', 0, 5)
        self.assertFalse(is_valid)
        self.assertIsNone(val)

    def test_validate_integer_input_out_of_range(self):
        '''
        If the integer is out of the [min, max) range,
        it should return (False, None).
        '''
        is_valid_low, val_low = _validate_integer_input('-1', 0, 5)
        self.assertFalse(is_valid_low)
        self.assertIsNone(val_low)

        is_valid_high, val_high = _validate_integer_input('5', 0, 5)
        self.assertFalse(is_valid_high)
        self.assertIsNone(val_high)

    @patch('builtins.print')
    def test_show_message(self, mock_print):
        '''
        show_message simply prints the message to stdout.
        '''
        message = "Hello from Connect Four"
        show_message(message)
        mock_print.assert_called_once_with(message)