"""
Decorators:
-----------
They are used to implement particular behavior for our classes.

Summary:
--------
1. property - Acts like a instance variable, no need to call like function.
2. static method - Directly called from the class.
3. class method - Returns a new instance of the class.
4. getter & setter - Used for `Data Encapsulation`.

Info:
-----
We can mark the class as `final` so that no other class can subclass it.

"""

from __future__ import annotations

from datetime import datetime
from enum import Enum, auto
from typing import final

# -------------------------------------------------------------------------


class Role(Enum):
    """Roles for staff members"""

    ASSOCIATE = auto()
    SUPERVISOR = auto()
    MANAGER = auto()


# -------------------------------------------------------------------------


class Person:
    def __init__(self, fname: str, lname: str) -> None:
        self.fname = fname
        self.lname = lname

    def __str__(self) -> str:
        return f"Person: {self.fname} {self.lname}"

    @property
    def fullname(self) -> str:
        """Returns the full name."""
        return f"{self.fname} {self.lname}"


# -------------------------------------------------------------------------


@final
class Staff(Person):
    # Class variable just for practice
    STORE = "Walmart"

    def __init__(self, fname: str, lname: str, staff_id: int, role: Role) -> None:
        # Initialize parent/super class
        super().__init__(fname, lname)
        # Instance Variables/Members
        self.staff_id = staff_id
        self.is_staff = True
        self.role = role
        # Private Member
        self._date_joined = datetime.now()
        # Dynamically create & assign instance variables
        match role:
            case role.ASSOCIATE:
                self.__salary: float = 15
            case role.SUPERVISOR:
                self.__salary = 20
            case role.MANAGER:
                self.__salary = 25

    def __str__(self) -> str:
        return f"Staff => Name: {self.fullname}, ID: {self.staff_id}"

    @classmethod
    def new(cls, person: Person, staff_id: int, role: Role) -> Staff:
        """
        Create a new `Staff` instance

        NOTE: It takes `class` as the first argument and return a instance
        of that class.
        """
        return cls(person.fname, person.lname, staff_id, role)

    @property
    def joined_on(self) -> str:
        """Joining date of staff member."""
        return f"{self._date_joined.strftime('%B %d, %Y')}"

    @staticmethod
    def describe() -> None:
        """
        Describes what the class does.

        NOTE: It does not take `self` as an argument.
        """
        print("Class to create a staff member")

    @property
    def salary(self) -> float:
        """`GETTER` returns the salary."""
        return self.__salary

    @salary.setter
    def salary(self, amt: float) -> None:
        """`SETTER` sets salary after validation."""
        if self.role == Role.ASSOCIATE and amt < 15:
            print("Error! Associate cannot have salary less than $15/hr")
        elif self.role == Role.SUPERVISOR and amt < 20:
            print("Error! Supervisor cannot have salary less than $20/hr")
        elif self.role == Role.MANAGER and amt < 25:
            print("Error! Manager cannot have salary less than $25/hr")
        else:
            self.__salary = amt
            print(f"{self.fullname} now has a salary of ${self.salary}/hr")


# -------------------------------------------------------------------------

p1 = Person("Louis", "Zappa")
print(p1.fullname)

s1 = Staff.new(p1, 1234, Role.SUPERVISOR)
print(s1)
print(s1.joined_on)

s2 = Staff("Chiko", "Jones", 3245, Role.MANAGER)
print(s2)

Staff.describe()

print(s1.salary)
print(s2.salary)

s1.salary = 17
s1.salary = 22
print(s1.salary)


# class HR(Staff):
#     pass
