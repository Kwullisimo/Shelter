from dataclasses import dataclass, field

#=========================== 
#=========ANIMAL============
#=========================== 

@dataclass
class Animal:
    """ MAKE SOUND | FEEED | INFO """
    name: str
    age: int
    species: str
    is_hungry: bool = True
    responsible: Employee | None = None

    def __str__(self) -> str:
        is_hungry_text = 'Animal fed' if not self.is_hungry else 'Animal hungry'
        return f'{self.name} | Species: {self.species} | Age: {self.age} | {is_hungry_text} | Responsible: {self.responsible.name if self.responsible else self.responsible}' # responsible can take value NONE

    def make_sound(self):
        match self.species:
            case 'dog':
                print('Woof-Woof')
            case 'cat':
                print('Meow')   
            case _:
                print('This animal makes an unknown sound')
    
    def feed(self):
        if not self.is_hungry:
            print('Animal not hungry')
        else:
            print(f'{self.name} fed')
            self.is_hungry = False

#=========================== 
#=========EMPLOYEE==========
#=========================== 

@dataclass
class Employee:
    """ ADD | FEED ALL | SHOW | INFO """
    name: str
    position: str
    animals: list = field(default_factory=list)

    def __str__(self) -> str:
        return f'{self.name } | Animals in care: {len(self.animals)}'

    def add_animal(self, animal: Animal): # ADD ANIMAL TO EMPLOYEE'S LIST
        if animal.responsible:
            print('This animal already has an owner')
        else:
            self.animals.append(animal)
            animal.responsible = self

    def feed_all(self): # FEED ALL FROM EMPLOYEE'S LIST
        if self.animals:
            for animal in self.animals:
                animal.feed()
            print(f'All {self.name}\'s animals fed')
        else:
            print('The employee doesn\'t have animals')

    def show_animals(self): # SHOW ALL FROM EMPLOYEE'S LIST
        print(f'{self.name}\'s animals:')
        if self.animals:
            for index, animal in enumerate(self.animals, start=1):
                print(f'{index}. {animal.info()}')
        else:
            print('The employee doesn\'t have animals')

#=========================== 
#=========SHELTER===========
#=========================== 

@dataclass
class Shelter:
    """ FEED | ADD | FIND | SHOW | INFO """
    name: str
    animals: list = field(default_factory=list)
    employees: list = field(default_factory=list)

    def __str__(self) -> str:
        return f'{self.name} | Number of animal: {len(self.animals)} | Number of employees: {len(self.employees)}'

    def feed_all(self): # FEED ALL FROM LIST OF ANIMAL
        if self.animals:
            for animal in self.animals:
                animal.feed()
            print(f'All animals from {self.name} fed')
        else:
            print('There are no animals in the shelter')

    def add_animal(self, animal: Animal): # ADD ANIMAL TO SHELTER LIST
        self.animals.append(animal)

    def add_employee(self, employee): # ADD EMPLOYEE TO SHELTER LIST    
        self.employees.append(employee)

    def find_animal(self, name: str) -> Animal | None: # FIND ANIMAL IN SHELTER LIST
        for animal in self.animals:
            if name == animal.name:
                print('Match found!')
                return animal
        else:
            print('No matches found')
        
    def show_animals(self): # SHOW ALL ANIMALS FROM SHELTER LIST
        if self.animals:
            for index, animal in enumerate(self.animals, start=1):
                print(f'{index}. {animal.info()}')
        else:
            print(f'There are no animals at the {self.name}')

    def show_employees(self): # SHOW ALL EMPLOYEE FROM SHELTER LIST
        if self.employees:
            print(self.name)
            for index, employee in enumerate(self.employees, start=1):
                print(f'{index}. {employee.info()}')
        else:
            print(f'There are no staff at the {self.name}')

def main()

if __name__ == '__main__':
    main()