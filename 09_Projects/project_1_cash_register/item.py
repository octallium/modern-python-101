class Item:
    """Simple Item for cash register"""

    def __init__(self, id: int, name: str, price: float, measurement_unit: str) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.measurement_unit = measurement_unit  # E.g -> Kg or ml

    def __repr__(self) -> str:
        return "<class 'Item'>"

    def __str__(self):
        return f"{self.name}: ${self.price}/{self.measurement_unit}"

    def dict(self) -> dict:
        """Return dictionary representation of the instance"""
        return self.__dict__
