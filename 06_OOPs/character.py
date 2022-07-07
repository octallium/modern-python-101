class Character:
    """Defines a character"""

    def __init__(self, name: str, attack_power: int, life: int) -> None:
        """Creates an instance of `Character`"""
        self.name = name
        self.attack_power = attack_power
        self.life = life

    def __repr__(self) -> str:
        return "<class 'Character'>"

    def __str__(self) -> str:
        return (
            f"Name: {self.name}, Attack Power: {self.attack_power}, Life: {self.life}"
        )


villain_1 = Character("Thanos", 400, 1500)
# Using Key value pairs
villain_2 = Character(name="Redskull", life=800, attack_power=300)

hero_1 = Character(name="Ironman", attack_power=250, life=1000)
hero_2 = Character(name="Blackwidow", attack_power=180, life=800)

print(villain_1)
print(villain_2)

print(hero_1)
print(hero_2)
