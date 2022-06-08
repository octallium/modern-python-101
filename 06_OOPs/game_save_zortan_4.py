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
    VILLIAN = auto()


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


class Villian(Character):
    """Villian"""

    def __init__(self, name: str, attack_power: int, life: int) -> None:
        super().__init__(name, attack_power, life)
        self.role = CharacterType.VILLIAN

    def __str__(self) -> str:
        return (
            f"Villian => Name: {self.name}, Attack Power: {self.attack_power},"
            f" Life: {self.life}"
        )


class _Life:
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

        _Life.hero_life += life

    @staticmethod
    def dec_hero_life(life: int) -> None:
        """Decreases Hero Life"""

        _Life.hero_life -= life

    @staticmethod
    def inc_villian_life(life: int) -> None:
        """Increases Villian Life"""

        _Life.villain_life += life

    @staticmethod
    def dec_villian_life(life: int) -> None:
        """Decreases Villian Life"""

        _Life.villain_life -= life


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


# ---------------------------- Villians -------------------------------


def get_all_villians() -> list[Villian]:
    """Returns a list of all Villians"""
    # Super Villains
    thanos = Villian(name="Thanos", attack_power=400, life=1500)
    redskull = Villian(name="Redskull", attack_power=300, life=800)
    proxima = Villian(name="Proxima", attack_power=320, life=800)

    # All Villains
    villains = [thanos, redskull, proxima]

    return villains


def get_villian(index: int) -> Villian | None:
    """Returns a single villian from the given index"""
    villians = get_all_villians()
    if index < len(villians):
        return villians[index]
    else:
        return None


# ---------------------------- Main Logic -------------------------------


def attack() -> None:
    """Start the attack"""
    for attack_num in range(3):
        # each iteration get a new hero & villain
        hero_index = randint(0, 3)
        villain_index = randint(0, 2)
        # Current Superhero & Villian
        current_superhero = get_superhero(hero_index)
        current_villain = get_villian(villain_index)
        if current_superhero and current_villain:
            __simulate_attack(attack_num, current_superhero, current_villain)
        else:
            print("Error! No superheros or villians to fight.")


def __simulate_attack(attack_num: int, superhero: SuperHero, villian: Villian) -> None:
    """Simulate the actual attack"""
    # Set life
    _Life.inc_hero_life(superhero.life)
    _Life.inc_villian_life(villian.life)

    # Print attack msg
    print(
        f"Attack: {attack_num + 1} => {superhero.name} is going to fight with {villian.name}."
    )

    # Actual attack
    _Life.dec_hero_life(villian.attack_power)
    _Life.dec_villian_life(superhero.attack_power)


# ---------------------------- Final Game Status -------------------------------


def win_or_loose() -> None:
    """Determine if Avengers won or lost"""

    WIN_MSG = "Avengers successfully saved Zortan!!! ✨ ✨ ✨"
    LOST_MSG = "Thanos killed Avengers and captured Zortan!!💀 💀 💀"

    print("=" * 58)

    # Win or Loose
    if _Life.hero_life >= _Life.villain_life:
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
