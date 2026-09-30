from dataclasses import dataclass

from models import Animal, Employee, Shelter

# ==================== 
# ======MENU==========
# ====================

@dataclass
class Menu():
    """ MAIN -> EMPLOYEES | ANIMALS -> ADD | SHOW """

    shelter: Shelter

    def run(self) :
        self.main_menu(self.shelter)

    def main_menu(self, shelter: Shelter):
        while True:
            print(
                f"{"MENU":=^20} \n"
                "1. My shelter \n"
                "2. Exit"
                )

            try:
                choice = int(input())
                match choice:
                    case 1: # MY SHELTER
                        self.shelter_menu(shelter)
                    case 2: # EXIT
                        exit()
                    case _:
                        print("Unknown command")
            except ValueError:
                print("Unknown command")    

    def choose_animal_menu(self):
        while True:
            print(
                "0 - Back\n" \
                "Choose animal - ")
            try:
                choice = int(input())
                match choice:
                    case 0:
                        break
                    case _:
                        print("suck my balls (In development)")
            except ValueError:
                print("Unknown command")

    def animals_menu(self, shelter: Shelter):
        while True:
            print(f"{"ANIMALS":=^20}")
            print(
                "1. Add animal \n"
                "2. Show list of animals \n"
                "3. Back"
                )
            try:
                choice = int(input())
                match choice:
                    case 1: # ADD
                        animal = Animal(input("Name - "), int(input("Age - ")), input("Species - "))
                        shelter.add_animal(animal)
                        print(f"{animal.name} added!")
                    case 2: # SHOW LIST
                        shelter.show_animals()
                        self.choose_animal_menu()
                    case 3: # BACK
                        break
                    case _:
                        print("Unknown command")
            except ValueError:
                print("Unknown command")

    def employees_menu(self, shelter:  Shelter):
        while True:
            print(f"{"EMPLOYEES":=^20}")
            print(
                "1. Add employee \n"
                "2. Show list of employees \n"
                "3. Back"
                )
            try:
                choice = int(input())
                match choice:
                    case 1: # ADD
                        employee = Employee(input("Name - "), input("Position - "))
                        shelter.add_employee(employee)
                        print(f"{employee.name} added!")
                    case 2: # SHOW LIST
                        shelter.show_employees()
                    case 3: # BACK
                        break
                    case _:
                        print("Unknown command")
            except ValueError:
                print("Unknown command")

    def shelter_menu(self, shelter: Shelter):
        while True:
            print(shelter)
            print(
                "1. Employees \n"
                "2. Animals \n"
                "3. Back"
                )
            try:
                choice = int(input())
                match choice:
                    case 1: # EMPLOYEE
                        self.employees_menu(shelter)
                    case 2: # ANIMAL
                        self.animals_menu(shelter)
                    case 3: # BACK
                        break
                    case _:
                        print("Unknown command")
            except ValueError:
                print("Unknown command")

# ==================== 
# =====CREATE=========
# ====================

def create_shelter() -> Shelter:
    print(
        f"{"Welcome":=^20} \n"
        "1. Create Shelter \n"
        "2. Exit"
          )
    while True:
        try:
            choice = int(input())
            match choice:
                case 1: # CREATE
                    shelter_name = input("Name - ")
                    shelter = Shelter(shelter_name)
                    print("Shelter are created!")
                    return shelter
                case 2: # EXIT
                    exit()
                case _:
                    print("Unknown command")  
        except ValueError:
            print("Unknown command")
