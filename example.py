from rps import Game, FixedActionPlayer, RandomActionPlayer
from collections import deque
from rps.utils import get_player_action_info
import logging

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    game_action_size = 3  # classic rock-paper-scissors

    player_jae = FixedActionPlayer("Jae", 0)  # will only play rock

    action_queue_soo = deque([1, 0, 2, 1, 2])  # the first five moves will be set
    player_soo = FixedActionPlayer("Soo", action_queue_soo, is_cycle=True)

    random_player_names = [f"random{i}" for i in range(5)]
    random_players = [RandomActionPlayer(name) for name in random_player_names]

    all_players = random_players + [player_jae, player_soo]

    print(" ")
    print("starting: ", [(p.name, get_player_action_info(p)) for p in all_players])
    example_game = Game(all_players, game_action_size)

    print(" ")
    random_game_beats = example_game.beats
    print("game rule: ", random_game_beats)
    print(" ")

    example_game.play()
