from __future__ import annotations

from random import randint

from .constants import LOST_MSG, NUM_ATTACKS, WIN_MSG
from .models.superhero import SuperHeroModel
from .models.villain import VillainModel
from .schemas.game_state import GameState
from .schemas.life import Life
from .schemas.player import Player
from .schemas.superhero import SuperHero
from .schemas.villain import Villain


class Game:
    """Creates a Game"""

    def __init__(self, player: Player) -> None:
        self.player = player
        self.state = GameState.INITIALIZING
        self.superheros = SuperHeroModel()
        self.villains = VillainModel()

    def __repr__(self) -> str:
        return "<class 'Game'>"

    def __str__(self) -> str:
        return (
            f"Player: {self.player},\nState: {self.state},\nSuperheros: {self.superheros},\n"
            f"Villains: {self.villains}"
        )

    # ---------------------------- Attack -------------------------------

    def attack(self) -> Game:
        """Start the attack"""
        self.state = GameState.IN_PROGRESS
        print("Starting attack...")
        print(self.state)

        for attack_num in range(NUM_ATTACKS):
            # each iteration get a new hero & villain
            hero_index = randint(0, len(self.superheros.all) - 1)
            villain_index = randint(0, len(self.villains.all) - 1)

            # Current Superhero & Villain
            current_superhero = self.superheros.get_superhero(hero_index)
            current_villain = self.villains.get_villain(villain_index)

            # Proceed only if we have superhero & villain
            if current_superhero and current_villain:
                self.__do_attack(attack_num, current_superhero, current_villain)
            else:
                print("Error! No superheros or villains to fight.")
        return self

    # ---------------------------- Win or Loose -------------------------------

    def win_or_loose(self) -> Game:
        """Determine if Avengers won or lost"""

        print("=" * 58)

        # Win or Loose
        if Life.hero_life >= Life.villain_life:
            self.state = GameState.WIN
            print(WIN_MSG)
        else:
            self.state = GameState.LOST
            print(LOST_MSG)

        return self

    # ---------------------------- Helper Method -------------------------------

    def __do_attack(
        self, attack_num: int, superhero: SuperHero, villain: Villain
    ) -> None:
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
