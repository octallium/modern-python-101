"""
Inheritance:
------------
All species inherit a lot from their parents, may be they have same eyes as
their mother but different voice all together.

Python classes are no different, we can inherit from classes and make them share
common functionality. At the same time we can dynamically add other features and
functionality as well.

Polymorphism:
-------------
Suppose there are two children, one want's to speak in Marathi, other want's to
speak in Sanskrit. This is possible using polymorphism! It's just creating the same
methods but with different behavior.
"""

# -------------------------------------------------------------------------


class Animal:
    def __init__(self, name: str, age: int, num_legs: int) -> None:
        # Create & initialize instance variables
        self.name = name
        self.age = age
        self.num_legs = num_legs

    def __str__(self) -> str:
        return f"Name: {self.name}"

    def talk(self) -> None:
        """Makes the animal talk"""
        print(f"{self.name} can't talk yet!")


a1 = Animal("Robbin", 10, 4)
print(a1)

a1.talk()

# -------------------------------------------------------------------------


class Dog(Animal):
    def __init__(self, name: str, age: int, num_legs: int, breed: str) -> None:
        # Take the common features and pass to the parent(super) class
        super().__init__(name, age, num_legs)
        # Define custom instance variables
        self.breed = breed
        self.type = "Dog"

    def __str__(self) -> str:
        return f"{self.type}: {self.name}, Breed: {self.breed}"

    # We alter the talk method and make it say woff adding polymorphic behavior
    def talk(self) -> None:
        print(f"{self.name} says wofff...")

    def sniff(self, item: str) -> None:
        print(f"{self.name} is sniffing out {item}")


d1 = Dog("Whisky", age=5, num_legs=4, breed="Doberman")

print(d1)
d1.talk()
d1.sniff("ball")

# -------------------------------------------------------------------------


class Cat(Animal):
    def __init__(self, name: str, age: int, num_legs: int, breed: str) -> None:
        super().__init__(name, age, num_legs)
        self.breed = breed
        self.type = "Cat"

    def __str__(self) -> str:
        return f"{self.type}: {self.name}, Breed: {self.breed}"

    def talk(self) -> None:
        print(f"{self.name} says meow...")


c1 = Cat("Jess", age=2, num_legs=4, breed="Persian Cat")

print(c1)
c1.talk()

# -------------------------------------------------------------------------


class Dino(Animal):
    def __init__(self, name: str, age: int, num_legs: int, breed: str) -> None:
        super().__init__(name, age, num_legs)
        self.breed = breed
        self.type = "Dino"

    def __str__(self) -> str:
        return f"{self.type}: {self.name}, Breed: {self.breed}"

    def talk(self) -> None:
        print(f"{self.name} says urrghhhh...")

    def hunt(self) -> None:
        print(f"{self.name} is out for hunting...")


dino1 = Dino("Adam", age=8, num_legs=2, breed="T-Rex")

print(dino1)
dino1.talk()
dino1.hunt()

# -------------------------------------------------------------------------

print(isinstance(d1, Animal))
print(isinstance(d1, Dog))
print(isinstance(d1, Cat))
