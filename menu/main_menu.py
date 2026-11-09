from models import Shelter

from menu import shelter_menu

def run(shelter: Shelter) -> None:
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
                    shelter_menu.run(shelter)
                case 2: # EXIT
                    exit()
                case _:
                    print("Unknown command")
        except ValueError:
            print("Unknown command")    

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
