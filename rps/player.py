import random
from abc import ABC, abstractmethod
from .game_state import GameState

class Player(ABC):
    def __init__(self, name: str) -> None:
        self.name = name
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

