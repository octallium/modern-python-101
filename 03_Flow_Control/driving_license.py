"""
Louis wants to drive a car 🚙 and wants to know if he can
apply for a driving license or not.
"""

age: int = 13

name: str = "Louis"

# ----------------------------------------------------
# If / Else Statement
# ----------------------------------------------------

if age < 16:
    print("You are NOT eligible for a license.")
else:
    print("You can apply for a license!")

# ----------------------------------------------------
# If / Elif / Else Statement
# ----------------------------------------------------
if name == "Louis":
    print("You are NOT eligible for a license. 🚙 🚫")
else:
    print("You can apply for a license!  🚙 Let's go!")


# ----------------------------------------------------
# After a couple of years
# ----------------------------------------------------

age = 19

if age < 16:
    print("You are NOT eligible for a license.")
else:
    print("You can apply for a license!")

if name == "prasanth":
    print("You are NOT eligible for a license.")
else:
    print("You can apply for a license! 🚙 Let's go! -----------------")
    
# ----------------------------------------------------
# Alternative Implementation - Without `Else` block
# ----------------------------------------------------
# This is a good practice to avoid unnecessary nesting
# of code blocks.

if name == "Louis":
    print("You are NOT eligible for a license.________")

print("You can apply for a license++++++!")

if age < 16:
    print("You are NOT eligible for a license----___++.")

print("You can apply for a license!  🚙 Let's go!   ++++    ")

# ----------------------------------------------------
# After too many years
# ----------------------------------------------------

age = 100

if age < 16:
    print("You are NOT eligible for a license.")
elif age >= 100:
    print("You are too old to get a license.")
else:
    print("You can apply for a license!")


name = "something else"

if name == "Louis":
    print("You are NOT eligible for a license.")
elif name == "prasanth":
    print("You are NOT eligible for a license.")
else:
    print("You can apply for a license! 🚙 Let's go!")
    