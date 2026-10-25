import pandas as pd

from .schema import db, cursor

def add_animal(animal):
    with db:
        cursor.execute("""
            INSERT INTO animals (
                name, age, is_hungry,
                responsible_id, description
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            animal.name,
            animal.age,
            animal.is_hungry,
            animal.responsible_id,
            animal.description
        ))

        return cursor.lastrowid
        

def get_animal():
    df = pd.read_sql_query("SELECT * FROM animals", db)
    
    return df