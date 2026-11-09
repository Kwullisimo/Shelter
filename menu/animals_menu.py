from models import Animal

import data

def run() -> None:
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
                    add_animal()
                case 2: # SHOW LIST
                    show_animal()                    
                case 3: # BACK
                    break
                case _:
                    print("Unknown command")
        except ValueError:
            print("Unknown command")

def add_animal() -> None:
    new_animal = Animal(input("Name - "), int(input("Age - ")), input("Species - "), input("Description - "))
    data.add_animal(new_animal)
    
    print(f"{new_animal.name} added!")

def show_animal() -> None:
    print(data.get_animal().to_string(index=False))


# --------------------
# ----IN DEVELOP------
# --------------------

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
