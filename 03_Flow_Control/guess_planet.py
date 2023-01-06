"""
Friends from Earth 🌏 want to know were is Louis, so Louis decides to
write a program that will make his friends guess the name of planet.
"""

correct_guess: bool = False
guess: str = ""
planet: str = "Zortan"

# Display a welcome message
# ----------------------------------------------------
# Alternative 1

guess = "prasad"
guess = input("Louis Says: Can you guess my planet? >>> ")
print(guess)


correct_guess = False
guess: str = ""
planet: str = "Zortan"

# line to try and err
#while LookupError

while True:
    #while correct_guess is not True:
    guess = input("Loius says: can you guess my planet? >>>>")

    if guess.lower() == planet.lower():
        print("right  ")
        break
    else:
        print("wrong try again")
        print("--------------")
        print()


"""
# ----------------------------------------------------
# Alternative 1
# ----------------------------------------------------

while correct_guess is not True:
    # Prompt user to enter a guess and assign it to `guess` variable
    guess = input("Louis Says: Can you guess my planet? >>> ")
    if guess.lower() == planet.lower():
        # Lowercase everything for correct comparison
        print("Right guess!! Louis is at Zortan 🪐")
        # Set the `correct_guess` to `True` and break from `while` loop
        correct_guess = True
    else:
        # Display a message for wrong guess
        print("Louis Says: Wrong Choice, try again!")
        print("------------------------------------")
        print()

# ----------------------------------------------------
# Alternative 2
# ----------------------------------------------------

while True:
    guess = input("Louis Says: Can you guess my planet? >>> ")
    if guess.lower() == planet.lower():
        print("Right guess!! Louis is at Zortan 🪐")
        # break from `while` loop
        break
    else:
        print("Louis Says: Wrong Choice, try again!")
        print("------------------------------------")
        print()
"""
