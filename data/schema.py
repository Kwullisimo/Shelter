import sqlite3

from config import DB_NAME

db = sqlite3.connect(DB_NAME)
cursor = db.cursor()


def init_db():
    with db:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS animals (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER,
                is_hungry INTEGER,
                responsible_id INTEGER,
                description TEXT
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY,
                name TEXT,
                position TEXT,
                description TEXT,
                animal_count INTEGER
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS shelters (
                id INTEGER PRIMARY KEY,
                name TEXT,
                animal_count INTEGER,
                employee_count INTEGER
            )
        """)