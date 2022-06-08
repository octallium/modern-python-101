class Customer:
    """Customer Details"""

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self) -> str:
        return "<class 'Customer'>"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def dict(self) -> dict:
        return {"first_name": self.first_name, "last_name": self.last_name}
