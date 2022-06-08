"""
Louis wants to drive a car 🚙 and wants to know if he can
apply for a driving license or not.
"""

age: int = 13

# ----------------------------------------------------
# If / Else Statement
# ----------------------------------------------------

if age < 16:
    print("You are NOT eligible for a license.")
else:
    print("You can apply for a license!")

# ----------------------------------------------------
# After a couple of years
# ----------------------------------------------------

age = 19

if age < 16:
    print("You are NOT eligible for a license.")
else:
    print("You can apply for a license!")

# ----------------------------------------------------
# Alternative Implementation - Without `Else` block
# ----------------------------------------------------

if age < 16:
    print("You are NOT eligible for a license.")

print("You can apply for a license!")

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
