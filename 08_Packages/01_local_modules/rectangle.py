class Rectangle:
    def __init__(self, side_A: float, side_B: float) -> None:
        self.side_A = side_A
        self.side_B = side_B

    def __str__(self) -> str:
        return f"Rectangle: {self.side_A} x {self.side_B}"
