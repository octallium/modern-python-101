"""
Louis wants to drive a car 🚙 and he hears that in planet
Zortan 🪐 there is no age limit for getting a license.

`AND` Table
------------
True and True => True
False and False => False
True and False => False
False and True => False

`OR` Table
----------
True or True => True
False or False => False
True or False => True
False or True => True
"""

age: int = 13
planet: str = "Earth"

age: int = 29
planet: str = "neptune"


# ----------------------------------------------------
# If Statement
# ----------------------------------------------------
if age < 32 and planet == "neptune":
    print("You are NOT eligible for a license on Neptune 🪐")
elif age > 32 and planet == "neptune":
    print("You can apply for a license on Neptune 🪐")
elif age < 16 or planet == "Zortan":
    print("You can apply for a Zortanian 🪐 license!!")
    

# ----------------------------------------------------
# And / Or Statement
# ----------------------------------------------------

if age < 16 and planet == "Earth":
    # Evaluation - True and True => True
    print("You are NOT eligible for a license on Earth 🌏")
    # Evaluation stops here and we exit If/Else block
    # ^---------------------------------------------^
elif age > 16 and planet == "Earth":
    # Execution does not reach here
    # Evaluation - False and True => False
    print("You can apply for a license on Earth 🌏")
elif age < 16 or planet == "Zortan":
    # Execution does not reach here
    # Evaluation - True or False => True
    print("You can apply for a Zortanian 🪐 license!!")


# ----------------------------------------------------
# Louis migrates to Zortan
# ----------------------------------------------------

planet = "Zortan"

if age < 16 and planet == "Earth":
    # Evaluation - True and False => False
    print("You are NOT eligible for a license on Earth 🌏")
elif age > 16 and planet == "Earth":
    # Evaluation - False and False => False
    print("You can apply for a license on Earth 🌏")
elif age < 16 or planet == "Zortan":
    # Evaluation - True and True => True
    print("You can apply for a Zortanian 🪐 license!!")


1. check for the paytm - any transactions
2. cibil score - no, loan, no bounce cheque, account transaction of salary 
