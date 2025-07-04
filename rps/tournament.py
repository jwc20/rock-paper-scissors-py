from typing import List
from .game import Game
from .player import Player

class Tournament(Game):
    """
    play the game until there is a clear winner
    """

    def __init__(self, players: List[Player], action_count: int) -> None:
        super().__init__(players, action_count)

    # TODO
    def play(self):
        # while True:
        #     pass
        pass
