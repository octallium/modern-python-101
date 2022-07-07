"""
Functions:
----------
Think in data transformations -
`take something -> give something`

Delegate handling responsibility to the caller function.

Tip:
-----
Very useful pattern for testing!!!
"""


# Returns a greeting message to caller function
# Caller function decides what to do with the response.
def greeter(name: str) -> str:
    """Return a greeting message"""
    # greeter `transforms` original string to something useful
    # and returns it.
    return f"Zola {name}!"


def main() -> None:
    friends: list[str] = ["Cece", "Roko", "Chiko", "Niko", "Ziko"]
    # Greet Everyone
    for friend in friends:
        # main acts as the `caller function` for greeter.
        # It can handle response in multiple ways.
        if "Chiko" in greeter(friend):
            print(f"{friend} is cute!")
        else:
            print(greeter(friend))


main()
