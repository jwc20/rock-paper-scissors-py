from typing import List
from itertools import product
import random

from abc import ABC, abstractmethod


class GameState:
    def __init__(self):
        self.round_number = 0
        self.history = []
        self.winner = None
        self.is_finished = False


class Player(ABC):
    def __init__(self, name: str) -> None:
        self._name = name
        self._score = 0
        self._history = []

    @abstractmethod
    def choose_action(self, game_state: GameState, action_count):
        pass


class FixedActionPlayer(Player):
    def __init__(self, name, action):
        super().__init__(name)
        self.action = action

    def choose_action(self, game_state: GameState, action_count):
        return self.action


class RandomActionPlayer(Player):
    def choose_action(self, game_state: GameState, action_count):
        return random.randrange(0, action_count)


class Game:
    def __init__(self, players: List[Player], action_count: int) -> None:
        if action_count % 2 == 0:
            raise ValueError(f"Action count must be odd")
        if action_count < 0:
            raise ValueError(f"Action count must be greater than or equal to 3")
        if not players or len(players) < 2:
            raise ValueError(f"Must have at least two players")

        self._players = players
        self._action_count = action_count  # TODO: must be an odd number
        self._beats = {}
        self.check_player_action()
        self.generate_beats()

    @property
    def beats(self):
        return self._beats

    def generate_beats(self):
        """
        this is the logic for creating which actions beat others
        """
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
        """
        for checking who wins

        Player 0 scored +1 → they beat one other player and lost to none.
        Player 1 scored -1 → they lost to someone and beat no one.
        Player 2 scored 0 → they had a tie or an even outcome.

        returns zero-sum game
        """
        num_players = len(self._players)
        scores = [0] * num_players

        # profiles = list(self._players.action)

        beats = self._beats
        profiles = [player.action for player in self._players]

        # TODO: double loop
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
        valid_players = []
        for player in self._players:
            if 0 <= player.action < self._action_count:
                valid_players.append(player)
        # print("removed", [(p.name, p.action) for p in self._players if p not in valid_players])
        self._players = valid_players

    # TODO
    def check_win(self):
        pass

    # TODO
    def generate_combinations(self):
        """
        generate all possible combination of actions based on
            - number of players
            - number of actions
        """
        pass
    
    # TODO
    def eliminate_losers(self, scores):
        """payoff() -> eliminate_losers(scores)"""
        pass
        
    
    def play_round(self):
        pass


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


if __name__ == "__main__":
    # test beats
    # for i in range(3, 10, 2):
    #     current_game_name = f"game_{i}"
    #     current_game = Game([], i)
    #     print(f"game_{i} {current_game.beats}")

    ps = [
        FixedActionPlayer("jon", 1),
        FixedActionPlayer("don", 2),
        FixedActionPlayer("dave", 1),
        FixedActionPlayer("dave2", 6),
        RandomActionPlayer("cave"),
    ]


    game_3 = Game(ps, 3)
    # print(game_3.beats)
    # print(game_3.payoff())

    print(Game([], 3).beats)
    # simulation
    action_num = 5
    for i in range(10):  # ten games
        players = []
        for i in range(5):  # 5 players
            name = f"player_{i}"
            players.append(Player(name, random.randrange(0, action_num)))

        game = Game(players, action_num)
        print(game.payoff(), [player.action for player in players])
