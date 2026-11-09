from __future__ import annotations # CLASS "Animal" HAVE ARGUMENT "responsible: Employee" | BUT CLASS "Employee" BEING CREATED AFTER CLASS "Animal"
from dataclasses import dataclass, field

import data

from data import get_shelter
from data import get_animal
from data import get_employee

@dataclass
class Animal:
    """ MAKE_SOUND | FEED """

    name: str
    age: int
    species: str
    description: str = None

    is_hungry: bool = True
    id: int = None

    responsible: Employee | None = field( 
        default=None,
        repr=False # ANIMAL HAVE RESPONSIBLE | BUT RESPONSIBLE HAVE ANIMAL LIST = RECURSION -> rep=False
        )

    responsible_id: int = 0


    def __str__(self) -> str:
        is_hungry_text = "Animal fed" if not self.is_hungry else "Animal hungry"

        responsible_name = (
            self.responsible.name
            if self.responsible
            else "No responsible employee"  # RESPONSIBLE CAN TAKE VALUE "None"
            )
        
        return (
            f"{self.name} | "
            f"Species: {self.species} | "
            f"Age: {self.age} | "
            f"{is_hungry_text} | "
            f"Responsible: {responsible_name}"
            )

    def make_sound(self) -> None: 
        match self.species.lower(): # "Dog" or "DOG" -> "dog"
            case "dog":
                print("Woof-Woof")
            case "cat":
                print("Meow")   
            case _:
                print("This animal makes an unknown sound")
    
    def feed(self) -> bool: # SUCCESSFUL -> "True" | FAILED -> "False"
        if not self.is_hungry:
            print(f"{self.name} is not hungry") 
            return False
        
        self.is_hungry = False
        print(f"{self.name} has been fed")
        return True

@dataclass
class Employee:
    """ ADD_ANIMAL | FEED_ALL | SHOW_ANIMALS """

    name: str
    position: str

    description: str = None

    animals: list[Animal] = field( # LIST "animals" CAN TAKE ONLY VALUE CLASS "Animal" -> list[Animal]
        default_factory=list 
        ) 

    def __str__(self) -> str:
        return (
                f"{self.name } | " 
                f"Position: {self.position} | "
                f"Animals in care: {len(self.animals)}"
                )

    def add_animal(self, animal: Animal) -> bool : # SUCCESSFUL -> "True" | FAILED -> "False"
        if animal.responsible:
            return False

        self.animals.append(animal)
        animal.responsible = self
        print(f"{animal.name} now has a new owner - {self.name}")
        return True

    def feed_all(self) -> bool: # SUCCESSFUL -> "True" | FAILED -> "False"
        if not self.animals:
            return False
        
        for animal in self.animals:
            animal.feed()

        print(f"All {self.name}'s animals fed")
        return True


    def show_animals(self) -> None: # EARLY RETURN ⬇
        if not self.animals:
            print("The employee doesn't have animals")
            return
        for index, animal in enumerate(self.animals, start=1):
            print(f"{index}. {animal}")
        
        print(f"{self.name}'s animals:")
        
@dataclass
class Shelter:
    """ ADD_ANIMAL or EMPLOYEE | FIND_ANIMAL | SHOW_ANIMALS or EMPLOYEE"""

    name: str
    id: int | None = None

    def __str__(self) -> str:
        # len_decore = 25+len(self.employees)+len(self.animals) | IN FUTURE FOR BIG COUNT OF ANIMAL or EMPLOYEE
        return (
                f"{self.name:=^25} \n"
                f"Animals: {len(get_animal())} | "
                f"Employees: {len(get_employee())} \n"
                f"{"="*25}"
                )
    
    def find_animal(self, name: str) -> bool: # SUCCESSFUL -> "True" | FAILED -> "False"
        found = False
    
        for index, animal in enumerate(self.animals, start=1):
            if name.lower() == animal.name.lower():
                print(f"{index}. {animal}")
                found = True

        if not found:
            print("No match found")

        return found
            