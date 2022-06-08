from __future__ import annotations


class Box:
    def __init__(self, side_a: int, side_b: int) -> None:
        self.side_a = side_a
        self.side_b = side_b

    def __repr__(self) -> str:
        return "<class 'Box'>"

    def __str__(self) -> str:
        return f"Box => Side A: {self.side_a}, Side B: {self.side_b}"

    @property
    def area(self) -> int:
        return self.side_a * self.side_b

    def __contains__(self, num: object) -> bool:
        """Use `in` operator"""
        if not isinstance(num, int):
            raise NotImplementedError
        return num in [self.side_a, self.side_b]

    def __eq__(self, other: object) -> bool:
        """Checks if two Boxes are equal"""
        if not isinstance(other, Box):
            return NotImplemented
        return self.side_a == other.side_a and self.side_b == other.side_b

    def __lt__(self, other: object) -> bool:
        """Checks if the other box is smaller"""
        if not isinstance(other, Box):
            return NotImplemented
        return self.area < other.area

    def __le__(self, other: object) -> bool:
        """Checks if the other box is smaller or equal"""
        if not isinstance(other, Box):
            return NotImplemented
        return self.area <= other.area

    def __add__(self, other: object) -> int:
        """Adds two Boxes"""
        if not isinstance(other, Box):
            return NotImplemented
        return self.area + other.area

    def __sub__(self, other: object) -> int:
        """Subtracts two Boxes"""
        if not isinstance(other, Box):
            return NotImplemented
        return self.area - other.area

    def __mul__(self, other: object) -> int:
        """Multiplies two Boxes"""
        if not isinstance(other, Box):
            return NotImplemented
        return self.area * other.area

    def __truediv__(self, other: object) -> float:
        """Returns true division"""
        if not isinstance(other, Box):
            return NotImplemented
        return self.area / other.area

    def __floordiv__(self, other: object) -> int:
        """Returns floor division"""
        if not isinstance(other, Box):
            return NotImplemented
        return self.area // other.area


b1 = Box(3, 4)
b2 = Box(2, 5)

print(b1)
print(b2)
print(b1.area)
print(b2.area)
print(b1 - b2)
print(b1 + b2)
print(b1 * b2)
print(b1 / b2)
print(b1 // b2)
print(b1 < b2)
print(b1 > b2)
print(b1 <= b2)
print(b1 >= b2)

print(4 in b1)
print(6 in b1)
# print("a" in b1)
# b1 + [4, 5]
