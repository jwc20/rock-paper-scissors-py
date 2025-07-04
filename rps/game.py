from typing import List
from .game_state import GameState
from .player import Player

class Game:
    def __init__(self, players: List[Player], action_count: int) -> None:
        if action_count % 2 == 0:
            raise ValueError(f"Action count must be odd")
        if action_count < 0:
            raise ValueError(f"Action count must be greater than or equal to 3")

        # TODO: custom games
        # if action_count == 3: => classic rock-paper-scissors
        # if action_count == 5: => RPS-5 (rock-paper-scissors-lizard-spock) https://www.samkass.com/theories/RPSSL.html
        # if action_count == 7: => RPS-7 (rock-paper-scissors-fire-water-air-sponge) https://www.umop.com/rps7.htm
        # if action_count == 9: => RPS-9 (https://www.umop.com/rps9.htm)
        # if action_count == 11: => RPS-11 (https://www.umop.com/rps11.htm)
        # if action_count == 13: => RPS-13 (https://www.umop.com/rps13.htm)
        # if action_count == 15: => RPS-15 (https://www.umop.com/rps15.htm)
        # if action_count == 25: => RPS-25 (https://www.umop.com/rps25.htm)

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

    @property
    def players(self):
        return self._players

    def generate_beats(self):
        """
        for creating which actions beat others

        example for 3 actions (classic rock-paper-scissors):
        {
            0: [1], # rock beats paper
            1: [2], # paper beats scissors
            2: [0] # scissors beats rock
        }

        note: this does not generate beats for rock paper scissors with more actions like rock-paper-scissors-lizard-spock
        it creates a beats dictionary for a valid n-element cyclic game, which is simpler to generalize
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

    # TODO: generate hardcoded beats
    #  for classic rock-paper-scissors, classic rock-paper-scissors-lizard-spock, and etc
    # https://www.umop.com/rps.htm
    def generate_fixed_beats(self):
        pass


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
    def eliminate_losers(self):
        """
        payoff() gets scores -> eliminate_losers(scores)
        """
        scores = self.payoff()
        pass

    def eliminate(self):
        n = len(self._players)
        actions = [player.action for player in self._players]
        beats = self._beats
        eliminated = []

        for i in range(n):
            my_action = actions[i]
            for j in range(n):
                if i == j:
                    continue
                opponent_action = actions[j]
                if my_action in beats.get(opponent_action, []):
                    eliminated.append(i)
                    break  # Player i is beaten by someone → eliminate

        # if it's a tie (everybody is eliminated)
        if len(eliminated) == len(actions):
            return []

        return eliminated

    def play_round(self):
        pass
