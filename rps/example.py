from rps import Game, FixedActionPlayer, RandomActionPlayer


def main():
    # Create players
    # players = [
    #     FixedActionPlayer("jon", 1),
    #     FixedActionPlayer("don", 2),
    #     FixedActionPlayer("dave", 1),
    #     FixedActionPlayer("dave3", 2),
    #     FixedActionPlayer("dave2", 6),  # This will be filtered out as invalid
    #     # RandomActionPlayer("bob"),
    #     # RandomActionPlayer("cave"),
    # ]
    # 
    # game = Game(players, 3)
    
    # # Print game information
    # print("Game beats mapping:")
    # print(game.beats)
    # 
    # print("\nPlayers and their actions:")
    # print([(p.name, p.action) for p in game.players])
    
   
    # game.play_round()
    
    game_action_size = 3
    
    random_player_names = [f"random{i}" for i in range(5)]
    random_players = [RandomActionPlayer(name) for name in random_player_names]
    random_game = Game(random_players, game_action_size)
    
    for i in range(10):
        print(f"Round {i}")
        if len(random_game.players) < 2:
            print("Game over")
            break
        random_game.play_round()
    


if __name__ == "__main__":
    main()