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
        # self.check_player_action()
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
    def eliminate_losers(self):
        """
        payoff() gets scores -> eliminate_losers(scores)
        
        
        
        """
        scores = self.payoff()
        pass
        
    
    def play_round(self):
        pass

    # def last_player_eliminations(self, actions, beats):
    #     n = len(actions)
    #     eliminated = []
    # 
    #     for i in range(n):
    #         my_action = actions[i]
    #         for j in range(n):
    #             if i == j:
    #                 continue
    #             opponent_action = actions[j]
    #             if my_action in beats.get(opponent_action, []):
    #                 eliminated.append(i)
    #                 break  # Player i is beaten by someone → eliminate
    #     return eliminated


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


def last_player_eliminations(actions, beats):
    n = len(actions)
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
                
    # if it's a tie 
    if len(eliminated) == len(actions):
        return []
    
    return eliminated



def generate_beats(n):
    beats = {}
    half = (n - 1) // 2
    for i in range(n):
        beats[i] = []
        for k in range(1, half + 1):
            beats[i].append((i + k) % n)
    return beats


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

    # 
    # game_3 = Game([], 3)
    # beats =game_3.beats
    # print(game_3.beats)
    # print(game_3.payoff())
    
    # --------------------------------------------------

    # print(Game([], 3).beats)
    # # simulation
    # action_num = 5
    # for i in range(10):  # ten games
    #     players = []
    #     for i in range(5):  # 5 players
    #         name = f"player_{i}"
    #         players.append(Player(name, random.randrange(0, action_num)))
    # 
    #     game = Game(players, action_num)
    #     print(game.payoff(), [player.action for player in players])

    # --------------------------------------------------

    beats = {
        0: [2],  # Rock beats Scissors
        1: [0],  # Paper beats Rock
        2: [1],  # Scissors beats Paper
    }

    # Case with all 3 actions — no one is eliminated
    print(last_player_eliminations([0, 0, 1, 2, 2], beats))  # []

    # Case with Rock and Scissors — scissors lose
    print(last_player_eliminations([0, 0, 2, 0], beats))  # [2]

    # Case with Rock and Paper — rock loses
    print(last_player_eliminations([1, 1, 0], beats))  # [2]

    # Everyone chooses same — tie
    print(last_player_eliminations([0, 0, 0], beats))  # []



    beats = {
        0: [2, 3],
        1: [0, 4],
        2: [1, 3],
        3: [1, 4],
        4: [0, 2]
    }

    actions = [0, 1, 4, 2, 3]  # Rock, Paper, Spock, Scissors, Lizard
    print(last_player_eliminations(actions, beats))

    # Actions: 0=Rock, 1=Paper, 2=Scissors
    beats_3 = {
        0: [2],  # Rock beats Scissors
        1: [0],  # Paper beats Rock
        2: [1],  # Scissors beats Paper
    }

    # Test 1: All actions present → cyclic → no one eliminated
    actions = [0, 1, 2]
    # Expected: []
    print(last_player_eliminations(actions, beats_3))

    # Test 2: Rock vs Scissors only → Scissors eliminated
    actions = [0, 2, 0]
    # Expected: [1]
    print(last_player_eliminations(actions, beats_3))

    # Test 3: Only Rock → tie
    actions = [0, 0, 0]
    # Expected: []
    print(last_player_eliminations(actions, beats_3))

    # 0: Rock, 1: Paper, 2: Scissors, 3: Lizard, 4: Spock
    beats_5 = {
        0: [2, 3],  # Rock beats Scissors, Lizard
        1: [0, 4],  # Paper beats Rock, Spock
        2: [1, 3],  # Scissors beats Paper, Lizard
        3: [1, 4],  # Lizard beats Paper, Spock
        4: [0, 2],  # Spock beats Rock, Scissors
    }

    # Test 1: All actions → cycle → no elimination
    actions = [0, 1, 2, 3, 4]
    # Expected: []
    print(last_player_eliminations(actions, beats_5))

    # Test 2: Paper, Rock, Rock → Rock loses to Paper
    actions = [1, 0, 0]
    # Expected: [1, 2]
    print(last_player_eliminations(actions, beats_5))

    # Test 3: Spock vs Rock vs Scissors → Rock and Scissors eliminated
    actions = [4, 0, 2]
    # Expected: [1, 2]
    print(last_player_eliminations(actions, beats_5))

    beats_7 = generate_beats(7)

    # Test 1: All 7 actions → cycle → no elimination
    actions = list(range(7))
    # Expected: []
    print(last_player_eliminations(actions, beats_7))

    # Test 2: Players all choose one losing action (0), one player uses 3 (beats 0)
    actions = [0, 0, 0, 3]
    # 3 beats 0 → players 0,1,2 eliminated
    # Expected: [0, 1, 2]
    print(last_player_eliminations(actions, beats_7))

    beats_9 = generate_beats(9)

    # Test 1: All 9 actions → cycle → no one eliminated
    actions = list(range(9))
    # Expected: []
    print(last_player_eliminations(actions, beats_9))

    # Test 2: Majority use action 0, one player uses action 4 (0 is beaten by 4)
    actions = [0, 0, 0, 0, 4]
    # If 4 beats 0 → all 0s eliminated
    print(last_player_eliminations(actions, beats_9))

    # -------------------------------------------------------------------
    beats_3 = {
        0: [2],  # Rock
        1: [0],  # Paper
        2: [1],  # Scissors
    }

    # 10 players all pick random among 0, 1, 2
    actions = [random.randint(0, 2) for _ in range(10)]
    print("10-player actions:", actions)
    print("Eliminated:", last_player_eliminations(actions, beats_3))

    # -------------------------------------------------------------------
    
    beats_5 = generate_beats(5)
    
    # All players choose randomly
    actions = [random.randint(0, 4) for _ in range(20)]
    print("20-player actions:", actions)
    print("Eliminated:", last_player_eliminations(actions, beats_5))
    
    # 15 players choose 0, 5 choose 2 (0 beats 2) → expect 5 eliminated
    actions = [0]*15 + [2]*5
    print("15 Rock vs 5 Scissors:", actions)
    print("Eliminated:", last_player_eliminations(actions, beats_5))

    # -------------------------------------------------------------------
    
    beats_7 = generate_beats(7)

    # Everyone picks randomly
    actions = [random.randint(0, 6) for _ in range(50)]
    print("50-player actions:", actions)
    print("Eliminated:", last_player_eliminations(actions, beats_7))

    # Edge case: all choose same action
    actions = [3] * 50
    print("All same action (Lizard):", actions)
    print("Eliminated:", last_player_eliminations(actions, beats_7))  # Expect []

    # -------------------------------------------------------------------
    
    beats_9 = generate_beats(9)

    # Random distribution
    actions = [random.randint(0, 8) for _ in range(100)]
    print("100-player actions:", actions[:10], "...")  # Print only first 10 for brevity
    print("Eliminated:", last_player_eliminations(actions, beats_9))

    # -------------------------------------------------------------------
    
    # 50 players pick action 0, 1 player picks something that beats 0
    strong_against_0 = beats_7[0]  # e.g., [1,2,3] in 7-action case
    if strong_against_0:
        counter_action = strong_against_0[0]
        actions = [0] * 50 + [counter_action]
        print("50 vs 1 strong:", actions)
        print("Eliminated:", last_player_eliminations(actions, beats_7))  # Expect 50 eliminated
