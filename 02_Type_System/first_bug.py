"""
First Bug
---------

Undesired behavior in programming is called as `Bug`.

Python is a dynamically typed language so it's easy to introduce a bug.
"""

box = "Balloons"
print(f"Box contains: {box}")

box = 10  # Oh-no! storing 10 in a box doesn't make any sense
print(f"Box contains: {box}")

# ---------------------------------------------------------------------------------
# Introducing `Type Hinting` - Optional Static Type Checking in Python Using `Mypy`
# ---------------------------------------------------------------------------------

food: str = "Milk"
print(f"Louis is going to eat: {food}")

food = "Eggs"
print(f"Louis is going to eat: {food}")

food = False  # Will execute but we can find bugs
print(f"Louis is going to eat: {food}")
