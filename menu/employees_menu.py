from models import Employee

import data

def run() -> None:
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
                    add_employee()
                case 2: # SHOW LIST
                    show_employee()
                case 3: # BACK
                    break
                case _:
                    print("Unknown command")
        except ValueError:
            print("Unknown command")

def add_employee() -> None:
    employee = Employee(input("Name - "), input("Position - "), input("Decsription - "))
    data.add_employee(employee)

    print(f"{employee.name} added!")

def show_employee() -> None:
     print(data.get_employee().to_string(index=False))