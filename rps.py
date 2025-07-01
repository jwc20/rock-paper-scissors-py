
"""

1. Players make their actions 
    - actions depend on the number of actions

2. Game rules are set
    - number of actions (action_count) 
    - number of rounds
    - maximum number of players 
"""



from typing import List
from itertools import product
from collections import defaultdict


class Player:
    def __init__(self, name: str, action: int) -> None:
        self._name = name 
        self._action = action


    @property
    def name(self):
        return self._name
    
    # @property
    # def action(self):
    #     return self.action 

    # @action.setter
    # def action(self, new_action):
    #     self.action = new_action


class Game:
    def __init__(self, players: List[Player], action_count: int) -> None:
        self._players = players
        self._action_count = action_count # TODO: must be an odd number
        self.generate_beats()


    def generate_beats(self):
        beats = defaultdict()
        half = (self._action_count - 1) // 2  # number of actions each one beats
        for i in range(self._action_count):
            beat_list = []
            for k in range(1, half + 1):
                beat_index = (i + k) % self._action_count
                beat_list.append(beat_index)
            beats[i] = beat_list
        return beats


    # TODO
    def play(self):
        pass





if __name__ == "__main__":
    pass
    # actions in {rock, paper, scissors, ...} or {0, 1, 2, ...}

    # p1 = Player("jon", 1)
    # p2 = Player("don", 2)
    # p3 = Player("dave", 0)

    # players = list(p1, p2, p3)
    # game = Game(players, action_count)
    # game.play()

    game_0 = Game([], 2)
    print(game_0.generate_beats())

    game_1 = Game([], 3)
    print(game_1.generate_beats())

    game_2 = Game([], 4)
    print(game_2.generate_beats())

    game_3 = Game([], 5)
    print(game_3.generate_beats())

