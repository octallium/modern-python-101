"""
While traveling to Zortan, Louis packed lots of stuff. Let's
see if he has anything that matches your favorite color.

INFO -
------

`match` is a new operator introduced in Python 3.10
"""

fav_color: str = "yellow".lower()

color: str = "green".upper()

name: str = "Prasanth".upper()

match color:
    case "BLACK":
        print(f"{name} has a BLACK T-Shirt.")
    case "RED":
        print(f"{name} has a RED car.")
    case "YELLOW":
        print(f"{name} has YELLOW shoes.")
    case "GREEN":
        print(f"{name} has a GREEN hat")
    case _:
        print(f"{name} has nothing in {color} color.")

match fav_color:
    case "black":
        print("Louis has a BLACK T-Shirt.")
    case "red":
        print("Louis has a RED car.")
    case "yellow":
        print("Louis has YELLOW shoes.")
    case "green":
        print("Louis has a GREEN hat")
    case _:
        print(f"Louis has nothing in {fav_color} color.")
