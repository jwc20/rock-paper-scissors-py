from rps import Game, FixedActionPlayer, RandomActionPlayer


def main():
    # Create players
    players = [
        FixedActionPlayer("jon", 1),
        FixedActionPlayer("don", 2),
        FixedActionPlayer("dave", 1),
        FixedActionPlayer("dave3", 2),
        FixedActionPlayer("dave2", 6),  # This will be filtered out as invalid
        # RandomActionPlayer("bob"),
        # RandomActionPlayer("cave"),
    ]

    game = Game(players, 3)
    
    # Print game information
    print("Game beats mapping:")
    print(game.beats)
    
    print("\nPlayers and their actions:")
    print([(p.name, p.action) for p in game.players])
    
    # print("\nEliminated players:")
    # print(game.eliminate())

    game.play_round()
    
    # 
    # print(Game(players, 3).beats)
    # print(Game(players, 5).beats)
    # print(Game(players, 7).beats)
    # print(Game(players, 9).beats)
    # print(Game(players, 11).beats)
    # print(Game(players, 13).beats)
    # print(Game(players, 15).beats)


if __name__ == "__main__":
    main()