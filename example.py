from rps import Game, FixedActionPlayer, RandomActionPlayer


if __name__ == "__main__":
    game_action_size = 3
    player_jae = FixedActionPlayer("Jae", 0)
    random_player_names = [f"random{i}" for i in range(5)]
    random_players = [RandomActionPlayer(name) for name in random_player_names]

    all_players = random_players + [player_jae]

    print("starting: ", [(p.name, p.action) for p in all_players])
    random_game = Game(all_players, game_action_size)
    random_game.play()
