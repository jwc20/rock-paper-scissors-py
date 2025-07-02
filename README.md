# rock-paper-scissors-py

## motivation

- want to get the winners of multi-action (rock, paper, scissors, lizard, spock, ...) and multiplayer "rock, paper, scissors" game.

- there are n actions and m players where n,m are natural numbers and n >= 3 and m >= 2

  - m and n should be odd numbers?

### Game of size 3 - classic

- Rock wins against scissors.
- Scissors win against paper.
- Paper wins against rock.

### Game of size 5 - Rock-Paper-Scissors-Lizard-Spock

- Scissors cuts Paper
- Paper covers Rock
- Rock crushes Lizard
- Lizard poisons Spock
- Spock smashes Scissors
- Scissors decapitates Lizard
- Lizard eats Paper
- Paper disproves Spock
- Spock vaporizes Rock
- Rock crushes Scissors

### Example Payoff - 3 actions and 3 players

| Row    | P1 P2 P3  | Payoff (P1,P2,P3)                |
| ------ | --------- | -------------------------------- |
| 1      | R R R     | ( 0, 0, 0) All same              |
| **2**  | **R R P** | **(-1, -1, 2) P beats both R's** |
| 3      | R R S     | ( 1, 1, -2) Both R's beat S      |
| 4      | R P R     | (-1, 2, -1) P beats both R's     |
| 5      | R P P     | (-2, 1, 1) Both P's beat R       |
| 6      | R P S     | ( 0, 0, 0) All different         |
| 7      | R S R     | ( 1, -2, 1) Both R's beat S      |
| 8      | R S P     | ( 0, 0, 0) All different         |
| 9      | R S S     | ( 2, -1, -1) R beats both S's    |
| 10     | P R R     | ( 2, -1, -1) P beats both R's    |
| 11     | P R P     | ( 1, -2, 1) Both P's beat R      |
| 12     | P R S     | ( 0, 0, 0) All different         |
| 13     | P P R     | ( 1, 1, -2) Both P's beat R      |
| 14     | P P P     | ( 0, 0, 0) All same              |
| **15** | **P P S** | **(-1, -1, 2) S beats both P's** |
| 16     | P S R     | ( 0, 0, 0) All different         |
| 17     | P S P     | (-1, 2, -1) S beats both P's     |
| 18     | P S S     | (-2, 1, 1) Both S's beat P       |
| 19     | S R R     | (-2, 1, 1) Both R's beat S       |
| 20     | S R P     | ( 0, 0, 0) All different         |
| 21     | S R S     | (-1, 2, -1) R beats both S's     |
| 22     | S P R     | ( 0, 0, 0) All different         |
| 23     | S P P     | ( 2, -1, -1) S beats both P's    |
| 24     | S P S     | ( 1, -2, 1) Both S's beat P      |
| **25** | **S S R** | **(-1, -1, 2) R beats both S's** |
| 26     | S S P     | ( 1, 1, -2) Both S's beat P      |
| 27     | S S S     | ( 0, 0, 0) All same              |

---

See also:

- [ROCK, PAPER, SCISSORS, ETC - TOPICS IN THE THEORY OF REGULAR TOURNAMENTS by ETHAN AKIN](https://arxiv.org/pdf/1806.11241)

Normal-form Matrix:

- https://youtu.be/-1GDMXoMdaY?si=01Bx5GFGrJhCi-dX

- https://www.researchgate.net/publication/10810903_Dressing_the_mind_properly_for_the_game
