"""
Save Zortan:
------------

The war has just intensified, Thanos army has reach Zortan and are going to
fight along with him. With his army, this time Thanos is going to attach Avengers
and the battle is going to be intense!!!

Since, everything is going in real-time, we don't have control over characters,
instead our characters will choose their own fight.

This time each character gets it own structure and defined parameters, so as you
can see our code is getting better and certainly we are going to make is awesome
as we progress with future modules.
"""

# we need this for generating random nos.
from random import randint
from typing import Final

# -------------------------------------------------------------------------
# TYPE ALIAS:
# ===========
# Each time typing type as dict[str, str | int] is so boring, so we instead
# create a type alias and make our lives simpler.
# -------------------------------------------------------------------------
Character = dict[str, str | int]

# Super Heroes
IRONMAN: Final[Character] = {"name": "Ironman", "attack_power": 250, "life": 1000}
BLACKWIDOW: Final[Character] = {"name": "Blackwidow", "attack_power": 180, "life": 800}
SPIDERMAN: Final[Character] = {"name": "Spiderman", "attack_power": 190, "life": 700}
HULK: Final[Character] = {"name": "Hulk", "attack_power": 300, "life": 1100}

# Super Villains
THANOS: Final[Character] = {"name": "Thanos", "attack_power": 400, "life": 1500}
REDSKULL: Final[Character] = {"name": "Redskull", "attack_power": 300, "life": 800}
PROXIMA: Final[Character] = {"name": "Proxima", "attack_power": 320, "life": 800}

# All Super Heros & Super Villains
superheros: list[Character] = [IRONMAN, BLACKWIDOW, SPIDERMAN, HULK]
villains: list[Character] = [THANOS, REDSKULL, PROXIMA]

# Helper Variables
hero_life = 0
villain_life = 0

WIN_MSG: Final[str] = "Avengers successfully saved Zortan!!! ✨ ✨ ✨"
LOST_MSG: Final[str] = "Thanos killed Avengers and captured Zortan!! 💀 💀 💀"

# Attack
for attack in range(3):
    # each iteration get a new hero & villain
    hero_index = randint(0, 3)
    villain_index = randint(0, 2)
    # helper variables
    current_superhero = superheros[hero_index]
    current_villain = villains[villain_index]
    # life
    hero_life += current_superhero["life"]
    villain_life += current_villain["life"]
    print(
        f"Attack: {attack + 1} => {current_superhero['name']} is going to fight with {current_villain['name']}."
    )
    # Actual attack
    hero_life -= current_villain["attack_power"]
    villain_life -= current_superhero["attack_power"]

# Print a nice separating line
print("=" * 58)

# Win or Loose
if hero_life >= villain_life:
    print(WIN_MSG)
else:
    print(LOST_MSG)
