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
    def inc_villian_life(life: int) -> None:
        """Increases Villian Life"""

        Life.villain_life += life

    @staticmethod
    def dec_villian_life(life: int) -> None:
        """Decreases Villian Life"""

        Life.villain_life -= life
