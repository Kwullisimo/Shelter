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
            f'{self.name} | '
            f'Species: {self.species} | '
            f'Age: {self.age} | '
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
        # len_decore = 25+len(self.employees)+len(self.animals) | IN FUTURE FOR BIG COUNT OF ANIMAL or EMPLOYEE
        return (
                f'{self.name:=^25} \n'
                f'Animals: {len(self.animals)} | '
                f'Employees: {len(self.employees)} \n'
                f'{'='*25}'
                )

    def add_animal(self, animal: Animal) -> None:
        self.animals.append(animal)

    def add_employee(self, employee) -> None:
        self.employees.append(employee)

    def find_animal(self, name: str) -> bool: # SUCCESSFUL -> "True" | FAILED -> "False"
        found = False
    
        for index, animal in enumerate(self.animals, start=1):
            if name.lower() == animal.name.lower():
                print(f'{index}. {animal}')
                found = True

        if not found:
            print('No match found')

        return found
            
    def show_animals(self) -> None: # EARLY RETURN ⬇
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

# ==================== 
# ======MENU==========
# ====================

class Menu():
    def __init__(self, shelter: Shelter):
        self.shelter = shelter
        self.main_menu(self.shelter)

    def main_menu(self, shelter: Shelter):
        while True:
            print(
                f'{'MENU':=^20} \n'
                '1. My shelter \n'
                '2. Exit'
                )

            choice = int(input())
            match choice:
                case 1:
                    self.shelter_menu(shelter)
                case 2:
                    exit()
                case _:
                    print('Unknown command')

    def animals_menu(self, shelter: Shelter):
        while True:
            print(f'{'ANIMALS':=^20}')
            print(
                '1. Add animal \n'
                '2. Show list of animals \n'
                '3. Back'
                )
            choice = int(input())
            match choice:
                case 1: # ADD
                    animal = Animal(input('Name - '), int(input('Age - ')), input('Species - '))
                    shelter.add_animal(animal)
                    print(f'{animal.name} added!')
                case 2: # SHOW LIST
                    shelter.show_animals()
                case 3: # BACK
                    break
                case _:
                    print('Unknown command')

    def employees_menu(self, shelter: Shelter):
        while True:
            print(f'{'EMPLOYEES':=^20}')
            print(
                '1. Add employee \n'
                '2. Show list of employees \n'
                '3. Back'
                )
            choice = int(input())
            match choice:
                case 1: # ADD
                    employee = Employee(input('Name - '), input('Position - '))
                    shelter.add_employee(employee)
                    print(f'{employee.name} added!')
                case 2: # SHOW LIST
                    shelter.show_employees()
                case 3: # BACK
                    break
                case _:
                    print('Unknown command')

    def shelter_menu(self, shelter: Shelter):
        while True:
            print(shelter)
            print(
                '1. Employees \n'
                '2. Animals \n'
                '3. Back'
                )
            choice = int(input())
            match choice:
                case 1: # EMPLOYEE
                    self.employees_menu(shelter)
                case 2: # ANIMAL
                    self.animals_menu(shelter)
                case 3: # BACK
                    break
                case _:
                    print('Unknown command')

# ==================== 
# =====CREATE=========
# ====================

def create_shelter() -> Shelter:
    print(
        f'{'Welcome':=^20} \n'
        '1. Create Shelter \n'
        '2. Exit'
          )
    
    choice = int(input())
    match choice:
        case 1: # CREATE
            shelter_name = input('Name - ')
            shelter = Shelter(shelter_name)
            print('Shelter are created!')
        case 2: # EXIT
            exit()
        case _:
            print('Unknown command')

    return shelter

# ==================== 
# =======MAIN=========
# ====================

def main():
    Menu(create_shelter())

if __name__ == '__main__':
    main()