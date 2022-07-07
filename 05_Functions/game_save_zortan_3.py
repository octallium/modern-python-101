"""
Save Zortan:
------------

Let's convert the game logic into small functions.

Principles:
-----------

1. DRY - Don't Repeat Yourself -
================================
Try to keep your code as DRY as possible, group common functionality into
individual functions.

2. SRP - Single Responsibility Principle -
==========================================
Ideally one function should be responsible for only one operation.

Note:
-----
We will also learn about global & local scope of variables (Using scratch pad)
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

# ---------------------------- Life -------------------------------

# Helper Variables
hero_life = 0
villain_life = 0


def inc_hero_life(life: int) -> None:
    """Increases Hero Life"""
    global hero_life
    hero_life += life


def dec_hero_life(life: int) -> None:
    """Decreases Hero Life"""
    global hero_life
    hero_life -= life


def inc_villain_life(life: int) -> None:
    """Increases Villain Life"""
    global villain_life
    villain_life += life


def dec_villain_life(life: int) -> None:
    """Decreases Villain Life"""
    global villain_life
    villain_life -= life


# ---------------------------- Superheros -------------------------------


def get_all_superheros() -> list[Character]:
    """Return a list of all Superheros"""
    IRONMAN: Final[Character] = {"name": "Ironman", "attack_power": 250, "life": 1000}
    # Alternate type declaration with inference
    BLACKWIDOW: Character = {"name": "Blackwidow", "attack_power": 180, "life": 800}
    SPIDERMAN: Character = {"name": "Spiderman", "attack_power": 190, "life": 700}
    HULK: Character = {"name": "Hulk", "attack_power": 300, "life": 1100}

    # All Superheros
    superheros: list[Character] = [IRONMAN, BLACKWIDOW, SPIDERMAN, HULK]

    return superheros


def get_superhero(index: int) -> Character | None:
    """Returns superhero from the given index."""
    superheros = get_all_superheros()
    if index < len(superheros):
        return superheros[index]
    else:
        return None


# ---------------------------- Villains -------------------------------


def get_all_villains() -> list[Character]:
    """Returns a list of all Villains"""
    # Super Villains
    THANOS: Character = {"name": "Thanos", "attack_power": 400, "life": 1500}
    REDSKULL: Character = {"name": "Redskull", "attack_power": 300, "life": 800}
    PROXIMA: Character = {"name": "Proxima", "attack_power": 320, "life": 800}

    # All Villains
    villains: list[Character] = [THANOS, REDSKULL, PROXIMA]

    return villains


def get_villain(index: int) -> Character | None:
    """Returns a single villain from the given index"""
    villains = get_all_villains()
    if index < len(villains):
        return villains[index]
    else:
        return None


# ---------------------------- Main Logic -------------------------------


def attack() -> None:
    """Start the attack"""
    for attack_num in range(3):
        # each iteration get a new hero & villain
        hero_index = randint(0, 3)
        villain_index = randint(0, 2)
        # Current Superhero & Villain
        current_superhero = get_superhero(hero_index)
        current_villain = get_villain(villain_index)
        if current_superhero and current_villain:
            simulate_attack(attack_num, current_superhero, current_villain)
        else:
            print("Error! No superheros or villains to fight.")


def simulate_attack(attack_num: int, superhero: Character, villain: Character) -> None:
    """Simulate the actual attack"""
    # Set life
    inc_hero_life(superhero["life"])
    inc_villain_life(villain["life"])

    # Print attack msg
    print(
        f"Attack: {attack_num + 1} => {superhero['name']} is going to fight with {villian['name']}."
    )

    # Actual attack
    dec_hero_life(villain["attack_power"])
    dec_villain_life(superhero["attack_power"])


# ---------------------------- Final Game Status -------------------------------


def win_or_loose() -> None:
    """Determine if Avengers won or lost"""

    WIN_MSG = "Avengers successfully saved Zortan!!! ✨ ✨ ✨"
    LOST_MSG = "Thanos killed Avengers and captured Zortan!!💀 💀 💀"

    print("=" * 58)

    # Win or Loose
    if hero_life >= villain_life:
        print(WIN_MSG)
    else:
        print(LOST_MSG)


# ---------------------------- Main -------------------------------


def main() -> None:
    """Starts the Game"""
    attack()
    win_or_loose()


# ---------------------------- Start Game -------------------------------
main()
