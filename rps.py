
"""

1. Players make their actions 
    - actions depend on the number of actions

2. Game rules are set
    - number of actions (action_count) 
    - number of rounds
    - maximum number of players 
"""





class Game:
    def __init__(self, players, action_count) -> None:
        self.players = players
        self.action_count = action_count
        


class Player:
    def __init__(self, name, action) -> None:
        self.name = name 
        self.action = action








if __name__ == "__main__":
    pass
    # actions in {rock, paper, scissors, ...} or {0, 1, 2, ...}

    # p1 = Player("jon", 1)
    # p2 = Player("don", 2)
    # p3 = Player("dave", 0)

    # players = list(p1, p2, p3)

    # game = Game(players, action_count)
