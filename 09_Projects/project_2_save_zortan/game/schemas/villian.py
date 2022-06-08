from .character import Character
from .character_type import CharacterType


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
