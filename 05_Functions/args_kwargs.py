"""
Variable & Keyword Arguments:
-----------------------------

What happens if we don't know before hand how many arguments we are
going to receive? We can handle this situation by using variable &
keyword arguments syntax.

Info:
-----
We will first look at unpacking first.
"""
# -------------------------- Unpacking --------------------------------

from typing import Any

fname, lname = ("Louis", "Zappa")
print(fname)
print(lname)

first, *rest = ["Cece", "Roko", "Chiko", "Niko"]
print(first)
print(rest)

specs = {"type": "dynamic", "optional": "static typing", "found": "everywhere"}
lang = {"name": "python", **specs}
print(lang)

# ----------------------------- Variable Argument ---------------------------


def unknown_friends(*args: str) -> None:
    """Accepts and prints variable argument"""
    # variable args are always packed as tuple
    for friend in args:
        print(friend)


unknown_friends("Cece", "Roko", "Chiko", "Niko", "Jake", "Mario")

# ------------------------- Keyword Arguments ---------------------------------


def unknown_product(**kwargs: Any) -> None:
    """Accepts and prints variable keyword argument"""
    # keyword args are always packed as dictionary
    for k, v in kwargs.items():
        print(f"{k}: {v}")


unknown_product(name="pizza", price=3.99, topping="olives", extra_cheese=True)

# -------------------------------- Together ---------------------------------


def invoice(product: str, *args, **kwargs) -> None:
    print(product)
    print(args)
    print(kwargs)


invoice(
    "sneakers",
    "black",
    "white",
    brand="Nike",
    category="Air Jordans",
    price=899.99,
    in_stock=False,
)
