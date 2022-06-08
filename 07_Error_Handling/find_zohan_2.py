def find_zohan(name: str) -> None:
    friends = ["Cece", "Roko", "Chiko", "Niko", "Zohan", "Mario"]

    if name not in friends:
        raise ValueError(f"{name} not found!")
    else:
        print(f"Found {name}")


find_zohan("Zohan")
find_zohan("Sara")
