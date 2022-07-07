"""
Functions:
----------

It's all about data transformation, ideally it should:
`take something -> give something`

Or else, it causes a `side effect`.

Remember people in Zortan greet each other by saying Zola,
Louis wants to write a program which can greet any Zortan!
"""


def greeter(name: str) -> None:
    """Greets Zortan"""
    print(f"Zola {name}!")


def main() -> None:
    friends: list[str] = ["Cece", "Roko", "Chiko", "Niko", "Ziko"]
    # Greet Everyone
    for friend in friends:
        greeter(friend)


# Invoke the `main` function
main()
