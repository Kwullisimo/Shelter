from dataclasses import dataclass, field
# from __future__ import annotations # CLASS "Animal" HAVE ARGUMENT "responsible: Employee" | BUT CLASS "Employee" BEING CREATED AFTER CLASS "Animal"

# ====================
# =====ANIMAL=========
# ====================

@dataclass
class Animal:
    """ MAKE_SOUND | FEED """

    name: str
    age: int
    species: str
    is_hungry: bool = True

    responsible: Employee | None = field( 
        default=None,
        repr=False # ANIMAL HAVE RESPONSIBLE | BUT RESPONSIBLE HAVE ANIMAL LIST = RECURSION -> rep=False
        )

    def __str__(self) -> str:
        is_hungry_text = 'Animal fed' if not self.is_hungry else 'Animal hungry'

        responsible_name = (
            self.responsible.name
            if self.responsible
            else 'No responsible employee'  # RESPONSIBLE CAN TAKE VALUE "None"
            )
        
        return (
            f'{self.name} |'
            f'Species: {self.species} |'
            f'Age: {self.age} |'
            f'{is_hungry_text} | '
            f'Responsible: {responsible_name}'
            )

    def make_sound(self) -> None: 
        match self.species.lower(): # "Dog" or "DOG" -> "dog"
            case 'dog':
                print('Woof-Woof')
            case 'cat':
                print('Meow')   
            case _:
                print('This animal makes an unknown sound')
    
    def feed(self) -> bool: # SUCCESSFUL -> "True" | FAILED -> "False"
        if not self.is_hungry:
            print(f'{self.name} is not hungry') 
            return False
        
        self.is_hungry = False
        print(f'{self.name} has been fed')
        return True

# ====================
# =====EMPLOYEE=======
# ====================

@dataclass
class Employee:
    """ ADD_ANIMAL | FEED_ALL | SHOW_ANIMALS """

    name: str
    position: str

    animals: list[Animal] = field( # LIST "animals" CAN TAKE ONLY VALUE CLASS "Animal" -> list[Animal]
        default_factory=list 
        ) 

    def __str__(self) -> str:
        return (
                f'{self.name } | ' 
                f'Position: {self.position} | '
                f'Animals in care: {len(self.animals)}'
                )

    def add_animal(self, animal: Animal) -> bool : # SUCCESSFUL -> "True" | FAILED -> "False"
        if animal.responsible:
            return False

        self.animals.append(animal)
        animal.responsible = self
        print(f'{animal.name} now has a new owner - {self.name}')
        return True

    def feed_all(self) -> bool: # SUCCESSFUL -> "True" | FAILED -> "False"
        if not self.animals:
            return False
        
        for animal in self.animals:
            animal.feed()

        print(f'All {self.name}\'s animals fed')
        return True


    def show_animals(self) -> None: # EARLY RETURN ⬇
        if not self.animals:
            print('The employee doesn\'t have animals')
            return
        
        print(f'{self.name}\'s animals:')
        for index, animal in enumerate(self.animals, start=1):
            print(f'{index}. {animal}')


# ====================
# =====SHELTER========
# ====================
        
@dataclass
class Shelter:
    """ ADD_ANIMAL or EMPLOYEE | FIND_ANIMAL | SHOW_ANIMALS or EMPLOYEE"""

    name: str

    animals: list[Animal] = field(
        default_factory=list, # LIST "animals" CAN TAKE ONLY VALUE CLASS "Animal" -> list[Animal]
        repr=False # PROTECTION FOR LARGE LIST
        ) 
    
    employees: list[Employee] = field(
        default_factory=list, # LIST "employees" CAN TAKE ONLY VALUE CLASS "Employee" -> list[Employee]
        repr=False # PROTECTION FOR LARGE LIST
        )  

    def __str__(self) -> str:
        return (
                f'{self.name} | '
                f'Number of animal: {len(self.animals)} | '
                f'Number of employees: {len(self.employees)}'
                )

    def add_animal(self, animal: Animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def find_animal(self, name: str) -> bool: # SUCCESSFUL -> "True" | FAILED -> "False"
        found = False
    
        for animal in self.animals:
            if name.lower() == animal.name.lower():
                print(animal)
                found = True

        if not found:
            print('No match found')

        return found
            
    def show_animals(self): # EARLY RETURN ⬇
        if not self.animals:
            print(f'There are no animals at the {self.name}')
            return 

        print(f'{self.name} animals:')
        for index, animal in enumerate(self.animals, start=1):
            print(f'{index}. {animal}')

    def show_employees(self) -> None: # EARLY RETURN ⬇
        if not self.employees:
            print(f'There are no staff at the {self.name}')
            return 
        
        print(f'{self.name} employees:')
        for index, employee in enumerate(self.employees, start=1):
            print(f'{index}. {employee}')