from rps import Game, FixedActionPlayer, RandomActionPlayer


def main():
    game_action_size = 17
    
    random_player_names = [f"random{i}" for i in range(100)]
    random_players = [RandomActionPlayer(name) for name in random_player_names]
    print("starting: ", [(p.name, p.action) for p in random_players])
    random_game = Game(random_players, game_action_size)
    
    # for i in range(10):
    #     print("######################")
    #     print(f"Round {i}")
    #     if len(random_game.players) < 2:
    #         print("Game over")
    #         break
    #     random_game.play_round()
    #     print(" ")
    # 

    print(random_game.play())





if __name__ == "__main__":
    main()