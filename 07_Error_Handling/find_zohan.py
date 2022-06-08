def find_zohan(name: str) -> None:
    friends = ["Cece", "Roko", "Chiko", "Niko", "Zohan", "Mario"]

    try:
        assert name in friends
    except AssertionError:
        print(f"{name} not found!")
    else:
        print(f"Found {name}")
    finally:
        print("Goodbye")


find_zohan("Zohan")
find_zohan("Sara")
