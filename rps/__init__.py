from .game import Game
from .player import Player, FixedActionPlayer, RandomActionPlayer
from .tournament import Tournament


__all__ = [
    "Game",
    "Player",
    "FixedActionPlayer",
    "RandomActionPlayer",
    "Tournament"
]

__version__ = "1.0.0"
__authors__ = ["jwc20"]
__source__ = "https://github.com/jwc20/rock-paper-scissors-py"