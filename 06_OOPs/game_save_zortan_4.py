"""
Save Zortan:
------------

Let's improve our design by using classes.

"""

from enum import Enum, auto

# we need this for generating random nos.
from random import randint


class CharacterType(Enum):
    """Defines the Character Type"""

    SUPERHERO = auto()
    VILLAIN = auto()


class Character:
    """Defines a character"""

    def __init__(self, name: str, attack_power: int, life: int) -> None:
        """Creates an instance of `Character`"""
        self.name = name
        self.attack_power = attack_power
        self.life = life

    def __str__(self) -> str:
        return (
            f"Name: {self.name}, Attack Power: {self.attack_power}, Life: {self.life}"
        )


class SuperHero(Character):
    """Superhero"""

    def __init__(self, name: str, attack_power: int, life: int) -> None:
        super().__init__(name, attack_power, life)
        self.role = CharacterType.SUPERHERO

    def __str__(self) -> str:
        return (
            f"Superhero => Name: {self.name}, Attack Power: {self.attack_power},"
            f" Life: {self.life}"
        )


class Villain(Character):
    """Villain"""

    def __init__(self, name: str, attack_power: int, life: int) -> None:
        super().__init__(name, attack_power, life)
        self.role = CharacterType.VILLAIN

    def __str__(self) -> str:
        return (
            f"Villain => Name: {self.name}, Attack Power: {self.attack_power},"
            f" Life: {self.life}"
        )


class Life:
    """
    Helper class for managing Life.

    NOTE: Also see `Data Classes` for alternative solution.
    url - https://docs.python.org/3/library/dataclasses.html
    """

    hero_life = 0
    villain_life = 0

    @staticmethod
    def inc_hero_life(life: int) -> None:
        """Increases Hero Life"""

        Life.hero_life += life

    @staticmethod
    def dec_hero_life(life: int) -> None:
        """Decreases Hero Life"""

        Life.hero_life -= life

    @staticmethod
    def inc_villain_life(life: int) -> None:
        """Increases Villain Life"""

        Life.villain_life += life

    @staticmethod
    def dec_villain_life(life: int) -> None:
        """Decreases Villain Life"""

        Life.villain_life -= life


# ---------------------------- Superheros -------------------------------


def get_all_superheros() -> list[SuperHero]:
    """Return a list of all Superheros"""
    ironman = SuperHero(name="Ironman", attack_power=250, life=1000)
    blackwidow = SuperHero(name="Blackwidow", attack_power=180, life=800)
    spiderman = SuperHero(name="Spiderman", attack_power=190, life=700)
    hulk = SuperHero(name="Hulk", attack_power=300, life=1100)

    # All Superheros
    superheros = [ironman, blackwidow, spiderman, hulk]

    return superheros


def get_superhero(index: int) -> SuperHero | None:
    """Returns superhero from the given index."""
    superheros = get_all_superheros()
    if index < len(superheros):
        return superheros[index]
    else:
        return None


# ---------------------------- Villains -------------------------------


def get_all_villains() -> list[Villain]:
    """Returns a list of all Villains"""
    # Super Villains
    thanos = Villain(name="Thanos", attack_power=400, life=1500)
    redskull = Villain(name="Redskull", attack_power=300, life=800)
    proxima = Villain(name="Proxima", attack_power=320, life=800)

    # All Villains
    villains = [thanos, redskull, proxima]

    return villains


def get_villain(index: int) -> Villain | None:
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
            __simulate_attack(attack_num, current_superhero, current_villain)
        else:
            print("Error! No superheros or villains to fight.")


def __simulate_attack(attack_num: int, superhero: SuperHero, villain: Villain) -> None:
    """Simulate the actual attack"""
    # Set life
    Life.inc_hero_life(superhero.life)
    Life.inc_villain_life(villain.life)

    # Print attack msg
    print(
        f"Attack: {attack_num + 1} => {superhero.name} is going to fight with {villain.name}."
    )

    # Actual attack
    Life.dec_hero_life(villain.attack_power)
    Life.dec_villain_life(superhero.attack_power)


# ---------------------------- Final Game Status -------------------------------


def win_or_loose() -> None:
    """Determine if Avengers won or lost"""

    WIN_MSG = "Avengers successfully saved Zortan!!! ✨ ✨ ✨"
    LOST_MSG = "Thanos killed Avengers and captured Zortan!!💀 💀 💀"

    print("=" * 58)

    # Win or Loose
    if Life.hero_life >= Life.villain_life:
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
