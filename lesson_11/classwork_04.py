"""
Создать программу позволяющую осуществлять поиск по имени или возрасту, оба параметра вводятся с клавиатуры.
"""

import sqlite3


def select_user(firstname: str, age: int):
    with sqlite3.connect("my_database.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            SELECT *
            FROM user
            WHERE firstname = ? OR age = ?;
            """,
            (firstname, age,)
        )
        session.commit()
        return cursor.fetchone()

if __name__ == "__main__":
    firstname = input("Введите имя для поиска: ")
    print(select_user(firstname))