"""
Class can have class variables as well as instance variables.

Class variables are shared across all instances while instance
variable are only limited to that particular instance.
"""


class Box:

    # Class Variable/Member
    box_type = "Packaging Carton"
    color = "Brown"

    def __init__(self, side_a: int, side_b: int) -> None:
        # Instance Variables/Members
        self.side_a = side_a
        self.side_b = side_b

    def __str__(self) -> str:
        return f"Side A: {self.side_a}, Side B: {self.side_b}"


b1 = Box(3, 4)
print(b1)
print(b1.box_type)
print(b1.color)

print(Box.box_type)
print(Box.color)

b2 = Box(7, 8)
print(b2)
print(b2.box_type)
print(b2.color)
