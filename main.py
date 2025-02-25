# game.py
# Alexander Wasserman
# 25 Feb 2025

from connect_four.game import ConnectFourGame

if __name__ == "__main__":
    game = ConnectFourGame()
    try:
        game.play()
    except KeyboardInterrupt:
        print("Game ended!")