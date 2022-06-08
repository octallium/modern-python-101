class Square:
    def __init__(self, side: float) -> None:
        self.side = side

    def __str__(self) -> str:
        return f"Square: {self.side} x {self.side}"
