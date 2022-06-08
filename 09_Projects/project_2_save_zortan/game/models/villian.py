from game.schemas.villian import Villian


class VillianModel:
    def __init__(self) -> None:
        self.all = self._get_all_villians()

    def __str__(self) -> str:
        names: list[str] = []
        for villian in self.all:
            names.append(villian.name)
        return f"{names}"

    def __len__(self) -> int:
        """Magic Method for `len` function"""
        return len(self.all)

    def _get_all_villians(self) -> list[Villian]:
        """Returns a list of all Villians"""
        # Super Villains
        thanos = Villian(name="Thanos", attack_power=400, life=1500)
        redskull = Villian(name="Redskull", attack_power=300, life=800)
        proxima = Villian(name="Proxima", attack_power=320, life=800)

        # All Villains
        villains = [thanos, redskull, proxima]

        return villains

    def get_villian(self, index: int) -> Villian | None:
        """Returns a single villian from the given index"""
        if index < len(self.all):
            return self.all[index]
        else:
            return None
