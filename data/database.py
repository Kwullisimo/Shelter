import sqlite3
import pandas as pd

from config import DB_NAME

db = sqlite3.connect(DB_NAME)
cursor = db.cursor()

def get_data(table_name):
    allowed_table = {"animals", "employees", "shelters"}

    if table_name not in allowed_table:
        raise ValueError("Unknown table")

    return pd.read_sql_querry(
        f"SELECT * FROM {table_name}", db
    )

def close_db():
    db.close()