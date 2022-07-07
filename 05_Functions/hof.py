"""
Higher Order Functions:
-----------------------
Please note that this is a advanced topic, so it may take a couple of attempts
to understand these concepts.

Functions under the hood are just `Objects`, they can be passed to other
functions and functions can also return functions!

This data type is called as `Callable`, one which can be called or invoked.

Note:
-----
Till now we have been sending data to our functions, but sending data every time
can be expensive, instead we can send function to data!

Don't spend too much time mastering this topic, it will come naturally as you
progress with your programming skills.
"""
# -------------------------------------------------------------------------

from typing import Callable


def hello() -> None:
    """Prints Hello World"""
    print("Hello World!")


# hello is just a regular object or class of type `function`
print(hello)
print(type(hello))
print(id(hello))

# We can assign function to variables
greet: Callable[[], None] = hello  # just assigns the object `hello` to greet variable
greet()  # we can invoke/call the function using `()` at the end

# -------------------------------------------------------------------------

"""
Let's try to create a universal greeter that can greet a person in multiple
ways.
"""


def zola(name: str) -> str:
    return f"Zola, {name}!"


def good_morning(name: str) -> str:
    return f"Good Morning, {name}!"


def goodbye(name: str) -> str:
    return f"Goodbye, {name}!"


# Function accepting a function
def universal_greeter(name: str, greeter: Callable[[str], str]) -> None:
    """Can greet in multiple ways"""
    msg = greeter(name)
    print(msg)


universal_greeter("Louis", zola)
universal_greeter("Louis", good_morning)
universal_greeter("Louis", goodbye)

# -------------------------------------------------------------------------

"""
Functions returning functions!!
------------------------------

This can be confusing, relax if you can't get it, it took me several attempts
to understand this!
"""


# Function returning a function
def add_by_5(num: int) -> Callable[[], int]:
    """Add by 5"""

    def by_5() -> int:
        return num + 5

    return by_5


sum = add_by_5(5)
print(sum())


# Function returning a function
def unique_adder(num1: int) -> Callable[[int], int]:
    """Adds two numbers and then subtracts by 1"""

    def adder(num2: int) -> int:
        return num1 + num2 - 1

    return adder


addr = unique_adder(5)
print(addr(5))

# -------------------------------------------------------------------------

"""
Lambda:
-------

Perhaps the most neglected, but very powerful technique to work with functions.
Again, don't spend too much time mastering it, it will come naturally!

The way in which we declared functions are very verbose, we can condense them
in a single statement.

Let's try to create a calculator from scratch
"""

add: Callable[[int, int], int] = lambda x, y: x + y
subtract: Callable[[int, int], int] = lambda x, y: x - y
multiply: Callable[[int, int], int] = lambda x, y: x * y


def calc(num1: int, num2: int, operation: Callable[[int, int], int]) -> int:
    """Performs the maths operation on the numbers"""
    return operation(num1, num2)


print(calc(4, 5, add))
print(calc(4, 5, subtract))
print(calc(4, 5, multiply))
