# rock-paper-scissors-py

## motivation

- to get the winner/winners of multi-action (rock, paper, scissors, lizard, spock, ...) and multiplayer "rock, paper, scissors" game.

- there are m players and n actions where n,m are natural numbers and n >= 3 and m >= 2

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

### Game of size 7

- https://www.umop.com/rps7.htm

- ROCK POUNDS OUT FIRE, CRUSHES SCISSORS & SPONGE.
- FIRE MELTS SCISSORS, BURNS PAPER & SPONGE.
- SCISSORS SWISH THROUGH AIR, CUT PAPER & SPONGE.
- SPONGE SOAKS PAPER, USES AIR POCKETS, ABSORBS WATER.
- PAPER FANS AIR, COVERS ROCK, FLOATS ON WATER.
- AIR BLOWS OUT FIRE, ERODES ROCK, EVAPORATES WATER.
- WATER ERODES ROCK, PUTS OUT FIRE, RUSTS SCISSORS.

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

### Example Payoff - 5 actions and 5 players

| Row  | P1 P2 P3 P4 P5 | Payoff (P1,P2,P3,P4,P5) | Description              |
| ---- | -------------- | ----------------------- | ------------------------ |
| 1    | 0 0 0 0 0      | ( 0, 0, 0, 0, 0)        | All same - tie           |
| 2    | 0 0 0 0 1      | ( 3, 3, 3, 3,-4)        | 1 beats all 0s           |
| 3    | 0 0 0 0 2      | ( 3, 3, 3, 3,-4)        | 2 beats all 0s           |
| 4    | 0 0 0 0 3      | (-3,-3,-3,-3, 4)        | 3 loses to all 0s        |
| 5    | 0 0 0 0 4      | (-3,-3,-3,-3, 4)        | 4 loses to all 0s        |
| ...  | ...            | ...                     |
| 31   | 0 0 0 1 1      | ( 2, 2, 2,-3,-3)        | 0s beat 1s (3v2)         |
| 32   | 0 0 0 1 2      | ( 1, 1, 1,-1,-2)        | Mixed results            |
| 33   | 0 0 0 1 3      | ( 0, 0, 0,-2, 2)        | 0→1,2; 3→0; complex      |
| 34   | 0 0 0 1 4      | (-1,-1,-1, 0, 3)        | 4→0,1 dominates          |
| ...  | ...            | ...                     |
| 156  | 0 0 1 1 1      | ( 1, 1,-2,-2,-2)        | 0s beat 1s (2v3)         |
| 157  | 0 0 1 1 2      | ( 0, 0,-1,-1, 2)        | Complex cycle            |
| 158  | 0 0 1 1 3      | (-1,-1,-2, 0, 4)        | 3 beats most             |
| ...  | ...            | ...                     |
| 781  | 0 1 2 3 4      | ( 0, 0, 0, 0, 0)        | Perfect cycle - all tie! |
| ...  | ...            | ...                     |
| 1563 | 1 1 1 1 1      | ( 0, 0, 0, 0, 0)        | All same - tie           |
| ...  | ..             | ...                     |
| 2401 | 3 0 2 4 1      | (-2, 2,-2, 2,-2)        | Alternating wins         |
| 2402 | 3 0 3 1 2      | (-1, 1, 0,-1, 1)        | Near balance             |
| ...  | ...            | ...                     |
| 3124 | 4 4 4 4 3      | ( 4, 4, 4, 4,-4)        | 4s beat 3                |
| 3125 | 4 4 4 4 4      | ( 0, 0, 0, 0, 0)        | All same - tie           |

---

See also:

- https://www.umop.com/rps.htm

- https://www.samkass.com/theories/RPSSL.html

- [ROCK, PAPER, SCISSORS, ETC - TOPICS IN THE THEORY OF REGULAR TOURNAMENTS by ETHAN AKIN](https://arxiv.org/pdf/1806.11241)

Normal-form Matrix:

- https://youtu.be/-1GDMXoMdaY?si=01Bx5GFGrJhCi-dX

- https://www.researchgate.net/publication/10810903_Dressing_the_mind_properly_for_the_game
