from models import Shelter

import data

from menu import animals_menu, employees_menu

def run(shelter: Shelter) -> int | None:
    while True:
        print(shelter)
        print(
            "1. Employees \n"
            "2. Animals \n"
            "3. Rename \n"
            "4. Back"
            )
        try:
            choice = input().strip()
            match choice:
                case "1": # EMPLOYEE
                    employees_menu.run()
                case "2": # ANIMAL
                    animals_menu.run()
                case "3": # RENAME
                    rename(shelter)
                    print("Successful change")
                case "4": # BACK
                    return 0
                case _:
                    print("Unknown command")
        except ValueError:
            print("Unknown command")

def rename(shelter: Shelter) -> None:
    new_name = input("Enter new name - ").strip()
    shelter.name = new_name
    
    data.rename_shelter(new_name, shelter)
