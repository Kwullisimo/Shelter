from .database import db

from models import Shelter

def get_shelter():
    cursor = db.execute("""
        SELECT id, name FROM shelters
        ORDER BY id
        LIMIT 1
    """)
    return cursor.fetchone()

def save_shelter(shelter):
    with db:
        cursor = db.execute("""
            INSERT INTO shelters (name)
            VALUES (?)
        """, (shelter.name,))

    return cursor.lastrowid

def rename_shelter(new_name: str, shelter: Shelter) -> None:
    with db:
        db.execute(
            """"
            UPDATE shelters SET name = ? WHERE id = ?
            """,
            (new_name, shelter.id)
        )