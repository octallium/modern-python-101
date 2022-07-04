"""
ENUM:
-----

This is a very good data structure for creating choices or varieties
"""

from enum import Enum, auto


class PizzaSize(Enum):
    """Pizza Base Size Options"""

    SMALL = 8
    MEDIUM = 10
    LARGE = 12


choice = PizzaSize.MEDIUM

print(f"One order for {choice.value} inch pizza")


class Colors(Enum):
    """T-Shirt Varieties"""

    RED = "red"
    BLUE = "blue"
    GREEN = "green"


print(f"One order for {Colors.GREEN.value} T-Shirt")


class Role(Enum):
    ASSOCIATE = auto()
    SUPERVISOR = auto()
    MANAGER = auto()


print(Role.MANAGER.value)
