from rps import Game, FixedActionPlayer, RandomActionPlayer


def main():
    # Create players
    players = [
        FixedActionPlayer("jon", 1),
        FixedActionPlayer("don", 2),
        FixedActionPlayer("dave", 1),
        FixedActionPlayer("dave2", 6),  # This will be filtered out as invalid
        # RandomActionPlayer("cave"),
    ]

    game = Game(players, 5)
    
    # Print game information
    print("Game beats mapping:")
    print(game.beats)
    
    print("\nPlayers and their actions:")
    print([(p.name, p.action) for p in game.players])
    
    print("\nEliminated players:")
    print(game.eliminate())


if __name__ == "__main__":
    main()