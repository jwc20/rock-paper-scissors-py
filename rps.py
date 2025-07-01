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

    @property
    def action(self):
        return self._action


class Game:
    def __init__(self, players: List[Player], action_count: int) -> None:
        self._players = players
        self._action_count = action_count  # TODO: must be an odd number
        self._beats = {}
        self.check_player_action()
        self.generate_beats()

    @property
    def beats(self):
        return self._beats

    def generate_beats(self):
        """this is the logic for creating which actions beat others"""
        beats = {}
        half = (self._action_count - 1) // 2  # number of actions each one beats
        for i in range(self._action_count):
            beat_list = []
            for k in range(1, half + 1):
                beat_index = (i + k) % self._action_count
                beat_list.append(beat_index)
            beats[i] = beat_list
        self._beats = beats

    def payoff(self):
        """for checking who wins"""
        num_players = len(self._players)
        scores = [0] * num_players

        # profiles = list(self._players.action)


        beats = self._beats
        profiles = [player.action for player in self._players]
        print(profiles)


        for i in range(num_players):
            for j in range(num_players):
                if i == j:
                    continue
                a = profiles[i]
                b = profiles[j]
                if b in beats[a]:
                    scores[i] += 1  # i beats j
                elif a in beats[b]:
                    scores[i] -= 1  # i loses to j
                else:
                    pass  # tie, 0 points

        return tuple(scores)

    def check_player_action(self):
        removed = []
        print(self._players)
        for i, player in enumerate(self._players):
            print(player.name, player.action)

            if player.action < 0 or player.action > self._action_count: 
                print(f"removed: {player.name} with action {player.action}")
                # removed.append(player)
                del self._players[i]
                # self._players.remove(player)


        print(removed)



    # TODO
    def play(self):
        pass


if __name__ == "__main__":
    pass
    # actions in {rock, paper, scissors, ...} or {0, 1, 2, ...}

    # players = list(p1, p2, p3)
    # game = Game(players, action_count)
    # game.play()

    # for i in range(3, 10, 2):
    #     current_game_name = f"game_{i}"
    #     current_game = Game([], i)
    #     print(f"game_{i} {current_game.beats}")

    p1 = Player("jon", 1)
    p2 = Player("don", 2)
    p3 = Player("dave", 1)
    p4 = Player("dave2", 6)
    p5 = Player("dave3", -1)

    ps = [p1,p2,p3,p4,p5]

    game_3 = Game(ps , 3)
    print(game_3.beats)
    print(game_3.payoff())
