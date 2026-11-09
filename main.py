from models import Shelter

from menu import main_menu

from data import init_db, close_db
from data import get_shelter, save_shelter


def main():
    try:
        init_db()
 
        shelter_data = get_shelter()

        if shelter_data is None:
            shelter = main_menu.create_shelter()
            shelter.id = save_shelter(shelter)
        else:
            shelter = Shelter(
                name=shelter_data[1],
                id=shelter_data[0]
            )

        main_menu.run(shelter)

    finally:
        close_db()


if __name__ == "__main__":
    main()