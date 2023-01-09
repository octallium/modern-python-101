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


age: int = 29
planet: str = "Zortan"



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


age: int = 29
planet: str = "Zortan"



planet = "Zortan"

if age < 16 and planet == "Zortan":
    # Evaluation - True and False => False
    print("You are NOT eligible for a license on Earth 🌏")
elif age > 16 and planet == "Earth":
    # Evaluation - False and False => False
    print("You can apply for a license on Earth 🌏")
elif age < 16 or planet == "Zortan":
    # Evaluation - True and True => True
    print("You can apply for a Zortanian 🪐 license!!")
    print(__annotations__)
    
    
    
    
#1. check for the paytm - any transactions
#2. cibil score - no, loan, no bounce cheque, account transaction of salary 



from typing import Final

#declare constants with capital
IRONMAN_ATTACK_POWER1: Final[int] = 250
BLACKWIDOW_ATTACK_POWER1: Final[int] = 180
SPIDERMAN_ATTACK_POWER1: Final[int] = 190
HULK_ATTACK_POWER1: Final[int] = 300

thanos_life1: int = 1500
#constraints
choice1: int = 0
attackno = 0
WIN_MSG: Final[str] = " You have succesfully saved zortan"
LOST_MSG: Final[str] = " Thanos killed avengers and capotured the zortan"
MSG = """---------------------------------------------------------------------
Zortan is under attack, choose the pairs no. that will attack Thanos

1) Ironman & Black Widow
2) Black Widow & Spiderman
3) Spiderman & Hulk
4) Hulk & Ironman
--------------------------------------------------------------------- """

while True:
  #win/lose
  if thanos_life1 <= 0 and attackno <= 3:
  #win
    print(WIN_MSG)
    break
  elif attackno >= 3:
    #loose
    print(LOST_MSG)
    break
  print(MSG)
choice1 = int(input(" ether the choice to start the game>>> "))
if choice1 == 1:
    print("Ironman & Black Widow are attacking Thanos....")
    thanos_life1 = thanos_life1 - IRONMAN_ATTACK_POWER1 - BLACKWIDOW_ATTACK_POWER1
    attackno = attackno + 1
elif choice1 == 2:
    print("Black Widow & Spiderman are attacking Thanos....")
    thanos_life1 = thanos_life1 - BLACKWIDOW_ATTACK_POWER1 - SPIDERMAN_ATTACK_POWER1
    attackno = attackno + 1
elif choice1 == 3:
    print("Spiderman & Hulk are attacking Thanos....")
    thanos_life1 = thanos_life1 - SPIDERMAN_ATTACK_POWER1 - HULK_ATTACK_POWER1
    attackno = attackno + 1
elif choice1 == 4:
     print("Hulk & Ironman are attacking Thanos....")
     thanos_life1 = thanos_life1 - HULK_ATTACK_POWER1 - IRONMAN_ATTACK_POWER1
     attackno = attackno + 1
else:
    print("Invalid choice, choose from 1 to 4")


