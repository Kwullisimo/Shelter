import pandas as pd

from .schema import db, cursor

def add_employee(employee):
    with db:
        cursor.execute("""
            INSERT INTO employees (
                name, position, description
            )
            VALUES (?, ?, ?)
        """, (
            employee.name,
            employee.position,
            employee.description
        ))

        return cursor.lastrowid
        

def get_employee():
    df = pd.read_sql_query("SELECT * FROM employees", db)
    
    return df