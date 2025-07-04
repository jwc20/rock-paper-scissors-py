from rps import Game, FixedActionPlayer, RandomActionPlayer


def main():
    game_action_size = 3

    player_jae = FixedActionPlayer("Jae", 0)  # always plays Rock, like an idiot

    random_player_names = [f"random{i}" for i in range(5)]
    random_players = [RandomActionPlayer(name) for name in random_player_names]
    random_players.append(player_jae)
    print("starting: ", [(p.name, p.action) for p in random_players])
    random_game = Game(random_players, game_action_size)

    random_game.play()


if __name__ == "__main__":
    main()
