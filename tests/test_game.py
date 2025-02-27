# test_board.py
# Alexander Wasserman
# 26 Feb 2025

import unittest

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


